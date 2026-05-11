import json
import os

def generate_json():
    problem_id = 674
    title = "Longest Continuous Increasing Subsequence"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>674. Longest Continuous Increasing Subsequence</h3>
<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest <b>continuous</b> increasing subsequence (i.e. subarray)</em>. The subsequence must be <b>strictly</b> increasing.</p>

<p>A <b>continuous increasing subsequence</b> is defined by two indices <code>l</code> and <code>r</code> (<code>l &lt; r</code>) such that it is <code>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</code> and for each <code>l &lt;= i &lt; r</code>, <code>nums[i] &lt; nums[i + 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest continuous increasing subsequence is [2] with length 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "An integer array `nums`."
    output_format = "An integer representing the length of the longest continuous increasing subsequence."
    
    constraints = [
        "1 <= nums.length <= 10,000",
        "-10^9 <= nums[i] <= 10^9"
    ]
    
    explanation = """To find the longest continuous increasing subsequence:
1. **Single Pass Strategy**:
   - Maintain a `max_len` to store the result and a `current_len` for the current segment.
2. **Algorithm**:
   - Iterate through the array starting from the second element.
   - If the current element is strictly greater than the previous one (`nums[i] > nums[i-1]`), increment `current_len`.
   - Otherwise, update `max_len = max(max_len, current_len)` and reset `current_len = 1`.
   - After the loop, perform one final update to `max_len` to capture the last segment.
3. **Complexity Analysis**:
   - Time: O(N) where N is the length of `nums`.
   - Space: O(1) as we only use a few integer variables."""
    
    answer = """class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        
        max_len = 1
        current_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1
                
        return max(max_len, current_len)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef findLengthOfLCIS(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Process input\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint findLengthOfLCIS(vector<int>& nums) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int findLengthOfLCIS(int[] nums) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findLengthOfLCIS = function(nums) {\n    // User logic here\n};",
        "c": "int findLengthOfLCIS(int* nums, int numsSize) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "[1,3,5,4,7]", "expected_output": "3", "is_sample": True},
        {"input": "[2,2,2,2,2]", "expected_output": "1", "is_sample": True},
        {"input": "[1,2,3]", "expected_output": "3", "is_sample": False},
        {"input": "[3,2,1]", "expected_output": "1", "is_sample": False},
        {"input": "[]", "expected_output": "0", "is_sample": False},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[-100, -50, 0, 50, 100]", "expected_output": "5", "is_sample": False},
        {"input": "[1,3,5,7,9,1,3,5,7,9,1,3,5,7,9]", "expected_output": "5", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(10000)]", "expected_output": "10000", "is_sample": False},
        {"input": "[10000 - i for i in range(10000)]", "expected_output": "1", "is_sample": False},
        {"input": "[1 for _ in range(10000)]", "expected_output": "1", "is_sample": False}
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
        "topics": ["Array"],
        "companyIndex": 0
    }

    output_path = "601-800/674_Longest_Continuous_Increasing_Subsequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
