import json
import os

def generate_json():
    problem_id = 1262
    title = "Greatest Sum Divisible by Three"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1262. Greatest Sum Divisible by Three</h3>
<p>Given an array <code>nums</code> of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,6,5,1,8]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Pick numbers 3, 6, 1 and 8, their sum is 18 (maximum sum divisible by 3).</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since 4 is not divisible by 3, do not pick any number.</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,4]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Pick numbers 1, 3, 4 and 4, their sum is 12 (maximum sum divisible by 3).</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A list of integers `nums` as a JSON array."
    output_format = "An integer representing the maximum sum."

    constraints = [
        "1 <= nums.length <= 4 * 10^4",
        "1 <= nums[i] <= 10^4"
    ]

    explanation = """To find the maximum sum divisible by 3:
1. Use dynamic programming. Let `dp[r]` be the maximum sum whose remainder when divided by 3 is `r`.
2. Initialize `dp = [0, -infinity, -infinity]` where `dp[0]` is 0 and others are negative infinity.
3. For each number `x` in `nums`:
   - Calculate new `dp` states based on the previous ones:
     `new_dp[(r + x) % 3] = max(dp[(r + x) % 3], dp[r] + x)` for `r = 0, 1, 2`.
4. The result is `dp[0]`."""

    answer = """class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp = [0] * 3
        for x in nums:
            for i in [i for i in dp]:
                dp[(i + x) % 3] = max(dp[(i + x) % 3], i + x)
        return dp[0]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.maxSumDivThree(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> nums = json::parse(line);
        Solution sol;
        cout << sol.maxSumDivThree(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maxSumDivThree(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            int[] nums = mapper.readValue(sc.nextLine(), int[].class);
            System.out.println(new Solution().maxSumDivThree(nums));
        }
    }
}""",
        "javascript": """var maxSumDivThree = function(nums) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(maxSumDivThree(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int maxSumDivThree(int* nums, int numsSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(nums):
        dp = [0, -float('inf'), -float('inf')]
        for x in nums:
            new_dp = list(dp)
            for i in dp:
                if i == -float('inf'): continue
                new_dp[(i + x) % 3] = max(new_dp[(i + x) % 3], i + x)
            dp = new_dp
        return dp[0] if dp[0] != -float('inf') else 0

    test_cases_data = [
        [3,6,5,1,8],      # Sample 1
        [4],              # Sample 2
        [1,2,3,4,4],      # Sample 3
        [1,1,1],          # All same rem
        [2,2,2],          # All same rem
        [1,2],            # Combine to 3
        [1,2,3],          # Combine to 6
        # Stress tests
        [1,1] * 10000,
        [2,2] * 10000,
        [3] * 10000
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(int(solve(t)))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Greedy"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
