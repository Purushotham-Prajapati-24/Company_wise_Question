import json
import os

def generate_json():
    problem_id = 1636
    title = "Sort Array by Increasing Frequency"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1636. Sort Array by Increasing Frequency</h3>
<p>Given an array of integers <code>nums</code>, sort the array in <strong>increasing</strong> order based on the frequency of the values. If multiple values have the same frequency, sort them in <strong>decreasing</strong> order.</p>

<p>Return the <em>sorted array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [1,1,2,2,2,3]
<strong>Output:</strong> [3,1,1,2,2,2]
<strong>Explanation:</strong> '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [2,3,1,3,2]
<strong>Output:</strong> [1,3,3,2,2]
<strong>Explanation:</strong> '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums = [-1,1,-6,4,5,-6,1,4,1]
<strong>Output:</strong> [5,-1,4,4,-6,-6,1,1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>"""

    input_format = "An array of integers nums."
    output_format = "An array of integers sorted according to the described rules."
    
    constraints = [
        "1 <= nums.length <= 100",
        "-100 <= nums[i] <= 100"
    ]
    
    explanation = """To sort the array by frequency and then by value:
1. **Count Frequencies**: Use a frequency map (dictionary in Python) to count how many times each number appears in the array.
2. **Custom Sort Key**: Sort the unique numbers using a tuple as the key: `(frequency, -value)`.
   - `frequency` (ascending): Elements with lower counts come first.
   - `-value` (ascending) or `value` (descending): If frequencies are tied, the element with the larger value (more negative `-value`) comes first.
3. **Construct Result**: For each sorted unique number, append it to the result list as many times as its original frequency.
4. **Complexity**:
   - **Time**: $O(N \log N)$ due to sorting, where $N$ is the number of elements.
   - **Space**: $O(N)$ to store frequencies."""
    
    answer = """from collections import Counter

def frequencySort(nums):
    count = Counter(nums)
    # Sort by frequency (asc), then by value (desc)
    return sorted(nums, key=lambda x: (count[x], -x))"""

    boilerplate = {
        "python": "import sys, json\nfrom collections import Counter\n\ndef frequencySort(nums):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(frequencySort(data))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <map>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> frequencySort(vector<int>& nums) {\n        // implementation\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public int[] frequencySort(int[] nums) {\n        // implementation\n        return new int[0];\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar frequencySort = function(nums) {\n    \n};",
        "c": "/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* frequencySort(int* nums, int numsSize, int* returnSize){\n    \n}"
    }

    test_cases = [
        {"input": "[1,1,2,2,2,3]", "expected_output": "[3,1,1,2,2,2]", "is_sample": True},
        {"input": "[2,3,1,3,2]", "expected_output": "[1,3,3,2,2]", "is_sample": True},
        {"input": "[-1,1,-6,4,5,-6,1,4,1]", "expected_output": "[5,-1,4,4,-6,-6,1,1,1]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,1,1,1,1]", "expected_output": "[1,1,1,1,1]", "is_sample": False},
        {"input": "[5,4,3,2,1]", "expected_output": "[5,4,3,2,1]", "is_sample": False}, # All freq 1, sort desc val
        {"input": "[1,2,3,4,5]", "expected_output": "[5,4,3,2,1]", "is_sample": False},
        {"input": "[1,1,2,2]", "expected_output": "[2,2,1,1]", "is_sample": False}, # Same freq, desc val
        {"input": json.dumps([i for i in range(-100, 101)]), "expected_output": json.dumps([i for i in range(100, -101, -1)]), "is_sample": False}, # Stress Max
        {"input": "[100, -100, 100, -100, 0]", "expected_output": "[0, 100, 100, -100, -100]", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1001-2000/1636_Sort_Array_by_Increasing_Frequency.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
