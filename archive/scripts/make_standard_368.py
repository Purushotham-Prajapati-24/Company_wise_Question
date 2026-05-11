import json
import os

def generate_json():
    problem_id = 368
    title = "Largest Divisible Subset"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>368. Largest Divisible Subset</h3>
<p>Given a set of <strong>distinct</strong> positive integers <code>nums</code>, return the largest subset <code>answer</code> such that every pair <code>(answer[i], answer[j])</code> of elements in this subset satisfies:</p>
<ul>
	<li><code>answer[i] % answer[j] == 0</code>, or</li>
	<li><code>answer[j] % answer[i] == 0</code></li>
</ul>

<p>If there are multiple solutions, return any of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> [1,3] is also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,4,8]
<strong>Output:</strong> [1,2,4,8]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2 * 10<sup>9</sup></code></li>
	<li>All the integers in <code>nums</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "An array of distinct positive integers `nums`."
    output_format = "A list representing the largest divisible subset."
    
    constraints = [
        "1 <= nums.length <= 1000",
        "1 <= nums[i] <= 2 * 10^9",
        "Integers are unique."
    ]
    
    explanation = """To find the largest divisible subset, we can transform the problem into finding the **Longest Increasing Subsequence** with a different condition.

### Key Observation:
- If we sort the array, for any three numbers $a < b < c$ in a divisible subset:
  - $b \% a == 0$ and $c \% b == 0$ implies $c \% a == 0$.
- So, if we pick a number $x$, the next larger number in the subset must be a multiple of $x$.

### Algorithm Steps:
1. **Sort**: Sort `nums` in ascending order.
2. **DP Formulation**: 
   - Let `dp[i]` be the size of the largest divisible subset ending with `nums[i]`.
   - For each `i`, iterate through all $j < i$. If `nums[i] % nums[j] == 0`, then `dp[i] = max(dp[i], dp[j] + 1)`.
3. **Reconstruct Subsets**:
   - To reconstruct the subset, store the predecessor `prev[i] = j` when updating `dp[i]`.
4. **Result**: Find the index `max_idx` with the largest `dp[max_idx]` and backtrack using `prev` to build the result.

### Complexity Analysis:
- **Time Complexity**: $O(N^2)$, where $N$ is the length of `nums`. Sorting takes $O(N \log N)$, and the nested DP loops take $O(N^2)$.
- **Space Complexity**: $O(N)$ for the `dp` and `prev` arrays."""
    
    answer = """class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        nums.sort()
        n = len(nums)
        # dp[i] is length of largest divisible subset ending at index i
        dp = [1] * n
        # prev[i] to backtrack the subset
        prev = [-1] * n
        
        max_len = 0
        max_idx = -1
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
                
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
            
        return res[::-1]"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        nums = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.largestDivisibleSubset(nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> largestDivisibleSubset(vector<int>& nums) {\n        // Your logic here\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<Integer> largestDivisibleSubset(int[] nums) {\n        // Your logic here\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar largestDivisibleSubset = function(nums) {\n    // Your logic here\n};",
        "c": "/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {\n    // Your logic here\n    *returnSize = 0;\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "[1,2,3]", "expected_output": "[1,2]", "is_sample": True},
        {"input": "[1,2,4,8]", "expected_output": "[1,2,4,8]", "is_sample": True},
        {"input": "[1,2,4,5,10]", "expected_output": "[1,2,4]", "is_sample": False},
        {"input": "[4,8,10,240]", "expected_output": "[4,8,240]", "is_sample": False},
        {"input": "[1,3,9,27,81]", "expected_output": "[1,3,9,27,81]", "is_sample": False},
        {"input": "[5,9,18,54,108]", "expected_output": "[9,18,54,108]", "is_sample": False},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(1, 1001)]", "expected_output": "...", "is_sample": False},
        {"input": "list(range(2, 2000, 2))[:1000]", "expected_output": "...", "is_sample": False},
        {"input": "[1000000000, 500000000, 250000000, 125000000]", "expected_output": "[125000000, 250000000, 500000000, 1000000000]", "is_sample": False}
    ]

    data = {
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Math", "Dynamic Programming", "Sorting"],
        "companyIndex": 1
    }

    output_path = "301-500/368_Largest_Divisible_Subset.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
