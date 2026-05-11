import json
import os

def generate_json():
    problem_id = 581
    title = "Shortest Unsorted Continuous Subarray"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>581. Shortest Unsorted Continuous Subarray</h3>
<p>Given an integer array <code>nums</code>, you need to find one <b>continuous subarray</b> such that if you only sort this subarray in non-decreasing order, the entire array will be sorted in non-decreasing order.</p>

<p>Return <em>the length of the shortest such subarray</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,6,4,8,10,9,15]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "A single line containing space-separated integers for 'nums'."
    output_format = "A single integer representing the length of the shortest unsorted subarray."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "-10^5 <= nums[i] <= 10^5"
    ]
    
    explanation = """To find the shortest unsorted subarray:
1. Find the boundaries of the unsorted segment.
2. Scan from left to right: Track the current maximum. If the current element is smaller than the maximum, it is out of order. The last such index is the `right` boundary.
3. Scan from right to left: Track the current minimum. If the current element is larger than the minimum, it is out of order. The last such index is the `left` boundary.
4. If no such indices are found, the array is already sorted, so return 0.
5. Otherwise, return `right - left + 1`."""
    
    answer = """def findUnsortedSubarray(nums):
    n = len(nums)
    if n <= 1:
        return 0
    
    left, right = -1, -2
    max_val = nums[0]
    for i in range(1, n):
        if nums[i] < max_val:
            right = i
        else:
            max_val = nums[i]
            
    min_val = nums[n-1]
    for i in range(n-2, -1, -1):
        if nums[i] > min_val:
            left = i
        else:
            min_val = nums[i]
            
    return right - left + 1"""

    boilerplate = {
        "python": "import sys\\n\\ndef findUnsortedSubarray(nums):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    line = sys.stdin.read().strip()\\n    if line:\\n        nums = [int(x) for x in line.split()]\\n        print(findUnsortedSubarray(nums))",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <algorithm>\\n\\nusing namespace std;\\n\\nclass Solution { public: int findUnsortedSubarray(vector<int>& nums) { return 0; } };",
        "java": "class Solution { public int findUnsortedSubarray(int[] nums) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int findUnsortedSubarray(int* nums, int numsSize) { }"
    }

    test_cases = [
        {"input": "2 6 4 8 10 9 15", "expected_output": "5", "is_sample": True},
        {"input": "1 2 3 4", "expected_output": "0", "is_sample": True},
        {"input": "1", "expected_output": "0", "is_sample": True},
        {"input": "5 4 3 2 1", "expected_output": "5", "is_sample": False},
        {"input": "1 3 2 4 5", "expected_output": "2", "is_sample": False},
        {"input": "1 2 4 5 3", "expected_output": "3", "is_sample": False},
        {"input": "2 3 3 2 4", "expected_output": "3", "is_sample": False},
        {"input": "1 2 3 3 3", "expected_output": "0", "is_sample": False},
        {"input": "1 3 2 2 2", "expected_output": "4", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Sorting", "Stack", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = "401-600/581_Shortest_Unsorted_Continuous_Subarray.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
