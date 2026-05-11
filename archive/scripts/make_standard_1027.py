import json
import os

def generate_json():
    problem_id = 1027
    title = "Longest Arithmetic Subsequence"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1027. Longest Arithmetic Subsequence</h3>
<p>Given an array <code>nums</code> of integers, return the <strong>length</strong> of the longest arithmetic subsequence in <code>nums</code>.</p>

<p>Recall that a <strong>subsequence</strong> of an array <code>nums</code> is a list <code>nums[i<sub>1</sub>], nums[i<sub>2</sub>], ..., nums[i<sub>k</sub>]</code> with <code>0 &lt;= i<sub>1</sub> &lt; i<sub>2</sub> &lt; ... &lt; i<sub>k</sub> &lt;= nums.length - 1</code>. In addition, such a list is <strong>arithmetic</strong> if <code>nums[i<sub>j+1</sub>] - nums[i<sub>j</sub>]</code> is the same value for all <code>1 &lt;= j &lt; k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,6,9,12]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The whole array is an arithmetic sequence with steps of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [9,4,7,2,10]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The longest arithmetic subsequence is [4,7,10] with steps of 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [20,1,15,3,10,5,8]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest arithmetic subsequence is [20,15,10,5] with steps of -5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 500</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `nums`."
    output_format = "An integer representing the length of the longest arithmetic subsequence."

    constraints = [
        "2 <= nums.length <= 1000",
        "0 <= nums[i] <= 500"
    ]

    explanation = """Objective is to find the longest subsequence with a constant difference.
We use Dynamic Programming. Let `dp[i][diff]` be the length of the longest arithmetic subsequence ending at index `i` with common difference `diff`.
For each `i`, we iterate through all `j < i`. The difference is `d = nums[i] - nums[j]`.
`dp[i][d] = dp[j][d] + 1` (defaulting to 2 if `dp[j][d]` is not set).
The maximum value in the `dp` table is our answer."""

    answer = """import collections
class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = {}
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i, diff] = dp.get((j, diff), 1) + 1
        return max(dp.values())"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.longestArithSeqLength(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string s) {
    vector<int> res;
    string temp = "";
    for (char c : s) {
        if (isdigit(c)) temp += c;
        else if (temp != "") {
            res.push_back(stoi(temp));
            temp = "";
        }
    }
    if (temp != "") res.push_back(stoi(temp));
    return res;
}

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> nums = parseArray(line);
        Solution sol;
        cout << sol.longestArithSeqLength(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int longestArithSeqLength(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[] nums = parse(sc.nextLine());
            System.out.println(new Solution().longestArithSeqLength(nums));
        }
    }
    private static int[] parse(String s) {
        s = s.replaceAll("[\\[\\] ]", "");
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i]);
        return res;
    }
}""",
        "javascript": """var longestArithSeqLength = function(nums) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(longestArithSeqLength(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int longestArithSeqLength(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int* parseArray(int* size) {
    char c;
    while (scanf(" %c", &c) == 1 && c != '[');
    int capacity = 100, s = 0;
    int* arr = malloc(capacity * sizeof(int));
    int val;
    while (scanf("%d", &val) == 1) {
        if (s == capacity) { capacity *= 2; arr = realloc(arr, capacity * sizeof(int)); }
        arr[s++] = val;
        while (scanf(" %c", &c) == 1 && (c == ' ' || c == ','));
        if (c == ']') break;
        ungetc(c, stdin);
    }
    *size = s;
    return arr;
}

int main() {
    int size;
    int* nums = parseArray(&size);
    printf("%d\\n", longestArithSeqLength(nums, size));
    free(nums);
    return 0;
}"""
    }

    def solve(nums):
        dp = {}
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i, diff] = dp.get((j, diff), 1) + 1
        return max(dp.values()) if dp else 1

    test_cases_data = [
        [3,6,9,12],           # LC Sample 1
        [9,4,7,2,10],         # LC Sample 2
        [20,1,15,3,10,5,8],   # LC Sample 3
        [1,1,1,1],            # Constant diff 0
        [1,2,3,4,5],          # Constant diff 1
        [10,1],               # Diff -9, length 2
        [1,7,10,8,19,4,13,16], # Mixed
        # Stress tests (last 3)
        list(range(1000)),
        [500] * 1000,
        [i % 50 for i in range(1000)]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Dynamic Programming"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
