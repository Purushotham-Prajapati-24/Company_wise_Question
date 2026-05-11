import json
import os
import collections

def generate_json():
    problem_id = 740
    title = "Delete and Earn"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>740. Delete and Earn</h3>
<p>You are given an integer array <code>nums</code>. You want to maximize the number of points you can earn by performing the following operation any number of times:</p>

<ul>
    <li>Pick any <code>nums[i]</code> and delete it to earn <code>nums[i]</code> points. Afterwards, you must delete <b>every</b> element equal to <code>nums[i] - 1</code> and <b>every</b> element equal to <code>nums[i] + 1</code>.</li>
</ul>

<p>Return <em>the <strong>maximum number of points</strong> you can earn by applying the above operation some number of times</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,4,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,3,3,3,4]
<strong>Output:</strong> 9
<strong>Explanation:</strong> You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing the JSON array `nums`."
    output_format = "An integer representing the maximum points."

    constraints = [
        "1 <= nums.length <= 2 * 10^4",
        "1 <= nums[i] <= 10^4"
    ]

    explanation = """Recognize that taking `x` forces you to take all `x`s and lose all `x-1`s and `x+1`s. We can convert this to the House Robber problem: compute the total points for each number `x` and store it in an array `points` indexed by value up to the maximum value in `nums`. Then, iterate `i` from `1` to `max_val`, taking the maximum of `dp[i-1]` (not taking `i`) and `dp[i-2] + points[i]` (taking `i`)."""

    answer = """class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        dp = [0] * (max_val + 1)
        dp[1] = points[1]
        for i in range(2, max_val + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        return dp[max_val]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.deleteAndEarn(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            int val = 0;
            while (i < input.length() && isdigit(input[i])) {
                val = val * 10 + (input[i] - '0');
                i++;
            }
            res.push_back(val);
        } else i++;
    }
    return res;
}

int main() {
    string n_str;
    if (getline(cin, n_str)) {
        vector<int> nums = parseArray(n_str);
        Solution sol;
        cout << sol.deleteAndEarn(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int deleteAndEarn(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String n_str = sc.nextLine().trim();
            int[] nums = parseArray(n_str);
            Solution sol = new Solution();
            System.out.println(sol.deleteAndEarn(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(deleteAndEarn(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int deleteAndEarn(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
            int val, off = 0;
            sscanf(input+i, "%d%n", &val, &off);
            if (!off) { i++; continue; }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
            res[size++] = val;
            i += off;
        } else i++;
    }
    *outSize = size;
    return res;
}

int main() {
    char n_str[200000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int numsSize;
        int* nums = parseArray(n_str, &numsSize);
        printf("%d\\n", deleteAndEarn(nums, numsSize));
        free(nums);
    }
    return 0;
}"""
    }

    def solve(nums):
        if not nums:
            return 0
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        dp = [0] * (max_val + 1)
        dp[1] = points[1]
        for i in range(2, max_val + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
        return dp[max_val]

    test_cases_data = [
        [3,4,2],
        [2,2,3,3,3,4],
        [1],
        [1,2,3,4,5,6],
        [1,1,1,1,1],
        [10000, 9999, 10000],
        [10000]*20000,
        [x%100 + 1 for x in range(20000)],
        [1,3,5,7,9,11],
        [x for x in range(1, 10001)] + [x for x in range(1, 10001)]
    ]

    test_cases = []
    for i, nums in enumerate(test_cases_data):
        inp = json.dumps(nums)
        out = str(solve(nums))
        is_sample = i < 2
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

    data = {
        "question_id": problem_id,
        "question_text": html_description,
        "difficulty": difficulty,
        "marks": marks,
        "input_format": input_format,
        "output_format": output_format,
        "constraints": constraints,
        "explanation": explanation,
        "answer": answer,
        "boilerplate": boilerplate,
        "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
