import json
import os

def generate_json():
    problem_id = 673
    title = "Number of Longest Increasing Subsequence"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>673. Number of Longest Increasing Subsequence</h3>
<p>Given an integer array <code>nums</code>, return <em>the number of longest increasing subsequences</em>.</p>

<p><b>Notice</b> that the sequence has to be <b>strictly</b> increasing.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The length of the longest increasing subsequence is 1, and there are 5 subsequences of length 1, so output 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "An integer array `nums`."
    output_format = "An integer representing the count of the longest increasing subsequences."
    
    constraints = [
        "1 <= nums.length <= 2000",
        "-10^6 <= nums[i] <= 10^6"
    ]
    
    explanation = """To find the number of longest increasing subsequences:
1. **Dynamic Programming Strategy**:
   - Use two arrays: `lengths` and `counts`.
   - `lengths[i]` stores the length of the longest increasing subsequence ending at index `i`.
   - `counts[i]` stores the number of subsequences of length `lengths[i]` ending at index `i`.
2. **Algorithm**:
   - Initialize `lengths` and `counts` to 1 for each element.
   - For each pair of indices `(i, j)` where `j < i`:
     - If `nums[i] > nums[j]`:
       - If `lengths[j] + 1 > lengths[i]`:
         - Update `lengths[i] = lengths[j] + 1`.
         - Inherit `counts[i] = counts[j]`.
       - If `lengths[j] + 1 == lengths[i]`:
         - Add more ways: `counts[i] += counts[j]`.
3. **Final Step**:
   - Identify the maximum length `max_len` across the `lengths` array.
   - Sum up all `counts[i]` for which `lengths[i] == max_len`.
4. **Complexity Analysis**:
   - Time: O(N^2) where N is the length of `nums`.
   - Space: O(N) to store `lengths` and `counts`."""
    
    answer = """class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        
        lengths = [1] * n
        counts = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        max_len = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == max_len)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef findNumberOfLIS(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Handle input conversion\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint findNumberOfLIS(vector<int>& nums) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int findNumberOfLIS(int[] nums) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findNumberOfLIS = function(nums) {\n    // User logic here\n};",
        "c": "int findNumberOfLIS(int* nums, int numsSize) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "[1,3,5,4,7]", "expected_output": "2", "is_sample": True},
        {"input": "[2,2,2,2,2]", "expected_output": "5", "is_sample": True},
        {"input": "[1,2,3]", "expected_output": "1", "is_sample": False},
        {"input": "[3,2,1]", "expected_output": "3", "is_sample": False},
        {"input": "[1,1,1,2,2,2]", "expected_output": "9", "is_sample": False},
        {"input": "[1,3,2,4]", "expected_output": "2", "is_sample": False},
        {"input": "[1,2,4,3,5,4,7,2]", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(2000)]", "expected_output": "1", "is_sample": False},
        {"input": "[1 for _ in range(2000)]", "expected_output": "2000", "is_sample": False},
        {"input": "[i % 2 for i in range(2000)]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Binary Indexed Tree", "Segment Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/673_Number_of_Longest_Increasing_Subsequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
