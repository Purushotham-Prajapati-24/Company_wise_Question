import json
import os

def generate_json():
    problem_id = 376
    title = "Wiggle Subsequence"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>376. Wiggle Subsequence</h3>
<p>A <strong>wiggle sequence</strong> is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.</p>

<ul>
	<li>For example, <code>[1, 7, 4, 9, 2, 5]</code> is a <strong>wiggle sequence</strong> because the differences <code>(6, -3, 5, -7, 3)</code> alternate between positive and negative.</li>
	<li>In contrast, <code>[1, 4, 7, 2, 5]</code> and <code>[1, 7, 4, 5, 5]</code> are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.</li>
</ul>

<p>A <strong>subsequence</strong> is obtained by deleting zero or more elements from the original sequence, leaving the remaining elements in their original order.</p>

<p>Given an integer array <code>nums</code>, return <em>the length of the longest <strong>wiggle subsequence</strong> of </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,7,4,9,2,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,17,5,10,13,15,10,5,16,8]
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,5,6,7,8,9]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve this in <code>O(n)</code> time?</p>"""

    input_format = "An integer array `nums`."
    output_format = "Length of the longest wiggle subsequence."
    
    constraints = [
        "1 <= nums.length <= 1000",
        "0 <= nums[i] <= 1000"
    ]
    
    explanation = """To find the longest wiggle subsequence in $O(N)$ time, we use a **Greedy** approach or **Dynamic Programming**.

### Greedy Approach:
A wiggle subsequence essentially picks the **local extrema** (peaks and valleys) of the original sequence. 
- If the numbers are increasing, we only care about the highest point before they start decreasing.
- If the numbers are decreasing, we only care about the lowest point before they start increasing.

### Algorithm Steps:
1. **Initialize**: If `len(nums) < 2`, return the length.
2. **First Difference**: Find the first non-zero difference between adjacent elements to set the initial direction.
3. **Iterate**:
   - Keep track of `prev_diff` (the sign of the last valid difference).
   - For each adjacent pair `(nums[i-1], nums[i])`, calculate `diff = nums[i] - nums[i-1]`.
   - If `diff` is positive and `prev_diff` was non-positive, or if `diff` is negative and `prev_diff` was non-negative:
     - We found a new "wiggle" element.
     - Increment result count.
     - Update `prev_diff = diff`.
4. **Result**: Return the total count.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the length of `nums`.
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
            
        # Initial count of 1 for the first element
        count = 1
        prev_diff = 0
        
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            # If current diff is positive and previous was non-positive
            # OR current diff is negative and previous was non-negative
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
                
        return count"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def wiggleMaxLength(self, nums: list[int]) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        nums = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.wiggleMaxLength(nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int wiggleMaxLength(vector<int>& nums) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "public class Solution {\n    public int wiggleMaxLength(int[] nums) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar wiggleMaxLength = function(nums) {\n    // Your logic here\n};",
        "c": "int wiggleMaxLength(int* nums, int numsSize) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,7,4,9,2,5]", "expected_output": "6", "is_sample": True},
        {"input": "[1,17,5,10,13,15,10,5,16,8]", "expected_output": "7", "is_sample": True},
        {"input": "[1,2,3,4,5,6,7,8,9]", "expected_output": "2", "is_sample": True},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,1,1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,1,2,1]", "expected_output": "5", "is_sample": False},
        {"input": "[1,7,7,7,4,4,4,9,2,5]", "expected_output": "6", "is_sample": False},
        {"input": "[3,3,3,2,5]", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": "[i % 2 for i in range(1000)]", "expected_output": "1000", "is_sample": False},
        {"input": "[i for i in range(1000)]", "expected_output": "2", "is_sample": False},
        {"input": "[0]*1000", "expected_output": "1", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Greedy"],
        "companyIndex": 1
    }

    output_path = "301-500/376_Wiggle_Subsequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
