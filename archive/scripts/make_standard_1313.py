import json
import os

def generate_json():
    problem_id = 1313
    title = "Decompress Run-Length Encoded List"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1313. Decompress Run-Length Encoded List</h3>
<p>We are given a list <code>nums</code> of integers representing a list compressed with run-length encoding.</p>

<p>Consider each adjacent pair of elements <code>[freq, val] = [nums[2*i], nums[2*i+1]]</code>&nbsp;(with <code>i &gt;= 0</code>).&nbsp; For each such pair, there are <code>freq</code> elements with value <code>val</code> concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.</p>

<p>Return the decompressed list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [2,4,4,4]
<strong>Explanation:</strong> The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,3]
<strong>Output:</strong> [1,3,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums.length % 2 == 0</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the nums array."
    output_format = "A single line containing space-separated integers for the decompressed list."
    
    constraints = [
        "2 <= nums.length <= 100",
        "nums.length is even.",
        "1 <= nums[i] <= 100",
        "O(TotalElements) time complexity.",
        "O(TotalElements) space complexity."
    ]
    
    explanation = """To decompress a run-length encoded list:
1. **Understand Encoding**:
   - The input `nums` consists of pairs `[freq, val]`.
   - `freq` is at index `0, 2, 4...` and `val` is at index `1, 3, 5...`.
2. **Decompression**:
   - Initialize an empty result list `res`.
   - Iterate through the input array with a step of 2:
     - Extract `freq = nums[i]` and `val = nums[i+1]`.
     - Append the value `val` to `res`, `freq` number of times.
     - In Python, this is simple: `res.extend([val] * freq)`.
3. **Complexity**:
   - Time Complexity: O(TotalElements) where TotalElements is the sum of all frequencies in the input. Since `len(nums) <= 100` and each `freq <= 100`, the maximum result size is 5000.
   - Space Complexity: O(TotalElements) to store the result."""
    
    answer = """def decompressRLElist(nums: list[int]) -> list[int]:
    res = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i+1]
        res.extend([val] * freq)
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef decompressRLElist(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        res = decompressRLElist(nums)\n        print(\" \".join(map(str, res)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<int> decompressRLElist(vector<int>& nums) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] decompressRLElist(int[] nums) {\n        // User logic\n        return new int[0];\n    }\n}",
        "javascript": "function decompressRLElist(nums) {\n    // User logic\n}",
        "c": "int* decompressRLElist(int* nums, int numsSize, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4", "expected_output": "2 4 4 4", "is_sample": True},
        {"input": "1 1 2 3", "expected_output": "1 3 3", "is_sample": True},
        {"input": "1 5", "expected_output": "5", "is_sample": False},
        {"input": "10 0", "expected_output": " ".join(["0"] * 10), "is_sample": False},
        {"input": "2 1 2 2 2 3", "expected_output": "1 1 2 2 3 3", "is_sample": False},
        {"input": "1 1 1 2 1 3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "3 10 2 20", "expected_output": "10 10 10 20 20", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1", "99"] * 50), "expected_output": " ".join(["99"] * 50), "is_sample": False},
        {"input": " ".join(["100", "1"] * 50), "expected_output": " ".join(["1"] * 5000), "is_sample": False},
        {"input": " ".join(["2", "7"] * 50), "expected_output": " ".join(["7"] * 100), "is_sample": False}
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

    output_path = "1201-1400/1313_Decompress_Run_Length_Encoded_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
