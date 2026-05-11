import json
import os

def generate_json():
    problem_id = 1124
    title = "Longest Well-Performing Interval"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1124. Longest Well-Performing Interval</h3>
<p>We are given <code>hours</code>, a list of the number of hours worked per day for a given employee.</p>

<p>A day is considered to be a <em>tiring day</em> if and only if the number of hours worked is (strictly) greater than <code>8</code>.</p>

<p>A <em>well-performing interval</em> is an interval of days such that the number of tiring days is strictly greater than the number of non-tiring days.</p>

<p>Return the length of the longest well-performing interval.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> hours = [9,9,6,0,6,6,9]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The longest well-performing interval is [9,9,6], which has length 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> hours = [6,6,6]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hours.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hours[i] &lt;= 16</code></li>
</ul>
"""

    input_format = "An array of integers `hours` provided as `[hours]` in JSON."
    output_format = "An integer representing the maximum length of a well-performing interval."

    constraints = [
        "1 <= hours.length <= 10^4",
        "0 <= hours[i] <= 16"
    ]

    explanation = """To find the longest well-performing interval:
1. Transforming the `hours` array into a sequence of `1` (if hours > 8) and `-1` (otherwise).
2. The problem translates to finding the longest subarray with a positive sum.
3. Use a prefix sum approach with a hash map to record the first occurrence of each sum.
4. For each current prefix sum `s`:
   - If `s > 0`, the whole interval from the start is well-performing, length is `i + 1`.
   - If `s <= 0`, check if `s - 1` exists in the hash map. If it does, the subarray from `first_occurrence[s-1] + 1` to `i` has a sum of 1, length is `i - first_occurrence[s-1]`.
5. Keep track of the maximum length."""

    answer = """class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        res = score = 0
        pos = {}
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                res = i + 1
            else:
                if score not in pos:
                    pos[score] = i
                if score - 1 in pos:
                    res = max(res, i - pos[score - 1])
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        hours = json.loads(raw)
        if isinstance(hours[0], list): hours = hours[0]
        sol = Solution()
        print(sol.longestWPI(hours))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int longestWPI(vector<int>& hours) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<int> hours;
        if (j.is_array() && j.size() > 0 && j[0].is_array()) hours = j[0].get<vector<int>>();
        else hours = j.get<vector<int>>();
        Solution sol;
        cout << sol.longestWPI(hours) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int longestWPI(int[] hours) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            int[] hours;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                hours = mapper.convertValue(((List)raw).get(0), int[].class);
            } else {
                hours = mapper.convertValue(raw, int[].class);
            }
            System.out.println(new Solution().longestWPI(hours));
        }
    }
}""",
        "javascript": """var longestWPI = function(hours) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let hours = JSON.parse(input);
    if (Array.isArray(hours[0])) hours = hours[0];
    console.log(longestWPI(hours));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int longestWPI(int* hours, int hoursSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* hours = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; hours = realloc(hours, cap * sizeof(int)); }
        scanf("%d", &hours[s++]);
    }
    printf("%d\\n", longestWPI(hours, s));
    free(hours);
    return 0;
}"""
    }

    def solve(hours):
        res = score = 0
        pos = {}
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                res = i + 1
            else:
                if score not in pos: pos[score] = i
                if score - 1 in pos:
                    res = max(res, i - pos[score - 1])
        return res

    test_cases_data = [
        [[9,9,6,0,6,6,9]],  # Sample 1
        [[6,6,6]],          # Sample 2
        [[9,6,9]],
        [[10,10,10,10]],
        [[1,1,1,10,1,1,1]], # Length 1
        [[9,9,6,9,9,6,6]],
        [[8]],
        # Stress tests
        [[9]*10000],
        [[6]*10000],
        [[9 if i%2==0 else 6 for i in range(10000)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Prefix Sum", "Monotonic Stack"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
