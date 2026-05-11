import json
import os

def generate_json():
    problem_id = 1326
    title = "Minimum Number of Taps to Open to Water a Garden"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1326. Minimum Number of Taps to Open to Water a Garden</h3>
<p>There is a one-dimensional garden on the x-axis. The garden starts at the point <code>0</code> and ends at the point <code>n</code>. (i.e., the length of the garden is <code>n</code>).</p>

<p>There are <code>n + 1</code> taps located at points <code>[0, 1, ..., n]</code> in the garden.</p>

<p>Given an integer <code>n</code> and an integer array <code>ranges</code> of length <code>n + 1</code> where <code>ranges[i]</code> (0-indexed) means the <code>i-th</code> tap can water the area <code>[i - ranges[i], i + ranges[i]]</code> if it was open.</p>

<p>Return <em>the minimum number of taps</em> that should be open to water the whole garden <code>[0, n]</code>. If the garden cannot be watered return <strong>-1</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/1685_example_1.png" style="width: 521px; height: 123px;">
<pre><strong>Input:</strong> n = 5, ranges = [3,4,1,1,0,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The tap at point 0 can cover the interval [-3,3].
The tap at point 1 can cover the interval [-3,5].
The tap at point 2 can cover the interval [1,3].
The tap at point 3 can cover the interval [2,4].
The tap at point 4 can cover the interval [4,4].
The tap at point 5 can cover the interval [5,5].
Opening Only the second tap will water the whole garden [0,5].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 3, ranges = [0,0,0,0]
<strong>Output:</strong> -1
<strong>Explanation:</strong> Even if you open all the taps, you can only water [0,0], [1,1], [2,2], [3,3], which is not the whole garden [0,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>ranges.length == n + 1</code></li>
	<li><code>0 &lt;= ranges[i] &lt;= 100</code></li>
</ul>"""

    input_format = "An integer `n` and a JSON array `ranges` provided as `[n, ranges]` in JSON."
    output_format = "An integer representing the minimum taps or -1."

    constraints = [
        "1 <= n <= 10^4",
        "ranges.length == n + 1",
        "0 <= ranges[i] <= 100"
    ]

    explanation = """To find the minimum number of taps to cover [0, n]:
1. Convert each tap's range into a coverage interval `[max(0, i - ranges[i]), min(n, i + ranges[i])]`.
2. This is equivalent to the jump game problem where we want to reach `n` from `0`.
3. Create a representation `max_range[start] = end` which stores the farthest point reachcable from a given `start` point.
4. For each interval `[start, end]`, update `max_range[start] = max(max_range[start], end)`.
5. Iterate through the garden using a greedy strategy:
   - Keep track of `current_end` (farthest point reachable with current number of taps).
   - Keep track of `farthest` (farthest point reachable with one additional tap).
   - If at any point `i > farthest`, return -1 (gap in coverage).
   - If `i == current_end`, increment tap count and set `current_end = farthest`.
   - If `current_end >= n`, return tap count."""

    answer = """class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_reach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            max_reach[start] = max(max_reach[start], end)
            
        taps = 0
        curr_end = 0
        farthest = 0
        for i in range(n):
            if i > farthest:
                return -1
            farthest = max(farthest, max_reach[i])
            if i == curr_end:
                taps += 1
                curr_end = farthest
                
        return taps if curr_end >= n else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, ranges = json.loads(raw)
        sol = Solution()
        print(sol.minTaps(n, ranges))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0];
        vector<int> ranges = j[1].get<vector<int>>();
        Solution sol;
        cout << sol.minTaps(n, ranges) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minTaps(int n, int[] ranges) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (Integer) data[0];
            int[] ranges = mapper.convertValue(data[1], int[].class);
            System.out.println(new Solution().minTaps(n, ranges));
        }
    }
}""",
        "javascript": """var minTaps = function(n, ranges) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [n, ranges] = JSON.parse(input);
    console.log(minTaps(n, ranges));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int minTaps(int n, int* ranges, int rangesSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(n, ranges):
        max_reach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            max_reach[start] = max(max_reach[start], end)
        taps = 0
        curr_end = 0
        farthest = 0
        for i in range(n):
            if i > farthest: return -1
            farthest = max(farthest, max_reach[i])
            if i == curr_end:
                taps += 1
                curr_end = farthest
        return taps if curr_end >= n else -1

    test_cases_data = [
        [5, [3,4,1,1,0,0]], # Sample 1
        [3, [0,0,0,0]],     # Sample 2
        [7, [1,2,1,0,2,1,0,1]], # Multiple overlapping
        [1, [1,1]],         # Single step covered
        [1, [0,0]],         # Single step fail
        [2, [1,0,1]],       # Gap in middle
        [100, [0]*101],     # Large fail
        # Stress tests
        [10000, [100]*10001],
        [10000, [0]*10001],
        [1000, [1]*1001]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Greedy"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
