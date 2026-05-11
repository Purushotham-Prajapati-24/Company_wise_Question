import json
import os

def generate_json():
    problem_id = 1348
    title = "Tweet Counts Per Frequency"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1348. Tweet Counts Per Frequency</h3>
<p>A social media company is trying to monitor activity. Implement a class <code>TweetCounts</code> that can handle the following methods:</p>

<ul>
	<li><code>recordTweet(tweetName, time)</code>: Records that a tweet with the name <code>tweetName</code> occurred at <code>time</code> (in <strong>seconds</strong>).</li>
	<li><code>getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)</code>: Returns a list of integers representing the number of tweets with the name <code>tweetName</code> in each <strong>time interval</strong> for the given <code>freq</code>, <code>startTime</code> and <code>endTime</code>.</li>
</ul>

<p>The <code>freq</code> will be one of <code>"minute"</code>, <code>"hour"</code> or <code>"day"</code>. The time intervals are as follows:</p>

<ul>
	<li>For <code>freq = "minute"</code>, each interval is of length <strong>60 seconds</strong>.</li>
	<li>For <code>freq = "hour"</code>, each interval is of length <strong>3600 seconds</strong>.</li>
	<li>For <code>freq = "day"</code>, each interval is of length <strong>86400 seconds</strong>.</li>
</ul>

<p>The first interval starts at <code>startTime</code> and ends at <code>min(startTime + 60, endTime + 1)</code>, the second interval starts at <code>startTime + 60</code> and ends at <code>min(startTime + 120, endTime + 1)</code> and so on.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",10],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
<strong>Output:</strong>
[null,null,null,null,[2],[2,1],null,[4]]

<strong>Explanation:</strong>
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 10);                           // All tweets: {tweet3: [10]}
tweetCounts.recordTweet("tweet3", 60);                           // All tweets: {tweet3: [10, 60]}
tweetCounts.recordTweet("tweet3", 10);                           // All tweets: {tweet3: [10, 60, 10]}
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]; 2 tweets at 10 and 10 in [0,59]
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2, 1]; 2 tweets at 10, 10 in [0,59], 1 tweet at 60 in [60,60]
tweetCounts.recordTweet("tweet3", 120);                          // All tweets: {tweet3: [10, 60, 10, 120]}
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]; 4 tweets at 10, 10, 60, 120 in [0,210]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= tweetName.length &lt;= 10</code></li>
	<li><code>0 &lt;= time, startTime, endTime &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= endTime - startTime &lt;= 10<sup>4</sup></code></li>
	<li>There will be at most <code>10<sup>4</sup></code> calls in total to <code>recordTweet</code> and <code>getTweetCountsPerFrequency</code>.</li>
</ul>"""

    input_format = "A list of method names and a list of arguments for each method."
    output_format = "A list of return values for each method."

    constraints = [
        "0 <= time <= 10^9",
        "0 <= endTime - startTime <= 10^4",
        "At most 10^4 calls"
    ]

    explanation = """To implement the TweetCounts:
1. Use a Hash Map `tweets` where the key is `tweetName` and the value is a list of timestamps.
2. `recordTweet(tweetName, time)`: Append `time` to the list associated with `tweetName`.
3. `getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)`:
   - Identify the interval size: `minute=60`, `hour=3600`, `day=86400`.
   - Calculate the number of intervals: `(endTime - startTime) // size + 1`.
   - Initialize a result array of appropriate size with zeros.
   - Iterate through the timestamps of `tweetName`.
   - If a timestamp is in range `[startTime, endTime]`:
     - Calculate the interval index: `(time - startTime) // size`.
     - Increment the result at that index.
   - To optimize, we can keep the timestamps sorted or use bucketed storage, but with 10^4 elements, a linear scan in the range might be enough."""

    answer = """import collections

class TweetCounts:
    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        res = []
        if freq == "minute": size = 60
        elif freq == "hour": size = 3600
        else: size = 86400
        
        counts = [0] * ((endTime - startTime) // size + 1)
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                counts[(t - startTime) // size] += 1
        return counts"""

    boilerplate = {
        "python": """import sys
import json
import collections

class TweetCounts:
    def __init__(self):
        pass
    def recordTweet(self, tweetName: str, time: int) -> None:
        pass
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        methods, args = json.loads(raw)
        obj = None
        results = []
        for m, a in zip(methods, args):
            if m == "TweetCounts":
                obj = TweetCounts()
                results.append(None)
            elif m == "recordTweet":
                results.append(obj.recordTweet(a[0], a[1]))
            elif m == "getTweetCountsPerFrequency":
                results.append(obj.getTweetCountsPerFrequency(a[0], a[1], a[2], a[3]))
        print(json.dumps(results).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class TweetCounts {
public:
    TweetCounts() {}
    void recordTweet(string tweetName, int time) {}
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        return {};
    }
};

int main() {
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class TweetCounts {
    public TweetCounts() {}
    public void recordTweet(String tweetName, int time) {}
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
    }
}""",
        "javascript": """var TweetCounts = function() {
    
};
TweetCounts.prototype.recordTweet = function(tweetName, time) {};
TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

typedef struct {
} TweetCounts;

TweetCounts* constructor() { return NULL; }
void recordTweet(TweetCounts* obj, char * tweetName, int time) {}
int* getTweetCountsPerFrequency(TweetCounts* obj, char * freq, char * tweetName, int startTime, int endTime, int* returnSize) { return NULL; }

int main() { return 0; }"""
    }

    import collections
    def solve(methods, args):
        tweets = collections.defaultdict(list)
        results = []
        for m, a in zip(methods, args):
            if m == "TweetCounts": results.append(None)
            elif m == "recordTweet":
                tweets[a[0]].append(a[1])
                results.append(None)
            elif m == "getTweetCountsPerFrequency":
                freq, tweetName, s, e = a
                size = 60 if freq == "minute" else 3600 if freq == "hour" else 86400
                counts = [0] * ((e - s) // size + 1)
                for t in tweets[tweetName]:
                    if s <= t <= e:
                        counts[(t - s) // size] += 1
                results.append(counts)
        return results

    test_cases_data = [
        [["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"], [[],["tweet3",10],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]], # Sample 1
        [["TweetCounts", "getTweetCountsPerFrequency"], [[], ["minute", "non-existent", 0, 100]]], # Empty query
        [["TweetCounts", "recordTweet", "getTweetCountsPerFrequency"], [[], ["t1", 0], ["minute", "t1", 0, 0]]], # Edge start=end
        [["TweetCounts", "recordTweet", "getTweetCountsPerFrequency"], [[], ["t1", 60], ["minute", "t1", 0, 119]]], # Multi interval
        [["TweetCounts", "recordTweet", "getTweetCountsPerFrequency"], [[], ["t1", 1000000000], ["day", "t1", 1000000000, 1000000000]]], # Max time
        # Stress tests
        [["TweetCounts"] + ["recordTweet"]*1000 + ["getTweetCountsPerFrequency"]*10, [[],] + [["t", i] for i in range(1000)] + [["minute", "t", 0, 1000] for _ in range(10)]],
        [["TweetCounts", "recordTweet", "getTweetCountsPerFrequency"], [[], ["t", 3599], ["hour", "t", 0, 3600]]],
        [["TweetCounts", "recordTweet", "recordTweet", "getTweetCountsPerFrequency"], [[], ["t", 1], ["t", 1], ["minute", "t", 0, 10]]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Hash Table", "Design", "Sorting"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
