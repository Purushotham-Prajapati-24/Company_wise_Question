import json
import os

def generate_json():
    problem_id = 1295
    title = "Find Numbers with Even Number of Digits"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1295. Find Numbers with Even Number of Digits</h3>
<p>Given an array <code>nums</code> of integers, return how many of them contain an <strong>even number</strong> of digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [12,345,2,6,7896]
<strong>Output:</strong> 2
<strong>Explanation: 
</strong>12 contains 2 digits (even number of digits).&nbsp;
345 contains 3 digits (odd number of digits).&nbsp;
2 contains 1 digit (odd number of digits).&nbsp;
6 contains 1 digit (odd number of digits).&nbsp;
7896 contains 4 digits (even number of digits).&nbsp;
Therefore only 12 and 7896 contain an even number of digits.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [555,901,482,1771]
<strong>Output:</strong> 1 
<strong>Explanation: </strong>
Only 1771 contains an even number of digits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An array of integers nums."
    output_format = "An integer representing the count of numbers with even digits."
    
    constraints = [
        "1 <= nums.length <= 500",
        "1 <= nums[i] <= 10^5"
    ]
    
    explanation = """To find the numbers with an even count of digits:
1. **Iterate through the array**: For each number in `nums`:
   - Determine its digit count.
   - Increment a counter if the digit count is even.
2. **Determine Digit Count**:
   - **String Method**: Convert the number to a string and check its length: `len(str(num))`.
   - **Math Method**: Use logarithm `floor(log10(num)) + 1` or repeatedly divide by 10.
   - **Range Check**: Since `num <= 10^5`, even digits occur for [10, 99], [1000, 9999], and 100000.
3. **Complexity**:
   - **Time**: O(N * D), where N is the numbers array size and D is the average digit count (at most 6).
   - **Space**: O(1) or O(D) depending on the string conversion."""
    
    answer = """def findNumbers(nums):
    count = 0
    for num in nums:
        # String conversion is straightforward for N=500
        if len(str(num)) % 2 == 0:
            count += 1
    return count"""

    boilerplate = {
        "python": "import sys, json\n\ndef findNumbers(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = json.loads(line)\n        print(findNumbers(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int findNumbers(vector<int>& nums) {\n        // implementation\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public int findNumbers(int[] nums) {\n        // implementation\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findNumbers = function(nums) {\n    \n};",
        "c": "int findNumbers(int* nums, int numsSize){\n    \n}"
    }

    test_cases = [
        {"input": "[12,345,2,6,7896]", "expected_output": "2", "is_sample": True},
        {"input": "[555,901,482,1771]", "expected_output": "1", "is_sample": True},
        {"input": "[1]", "expected_output": "0", "is_sample": False},
        {"input": "[10]", "expected_output": "1", "is_sample": False},
        {"input": "[100]", "expected_output": "0", "is_sample": False},
        {"input": "[1000]", "expected_output": "1", "is_sample": False},
        {"input": "[10000]", "expected_output": "0", "is_sample": False},
        {"input": "[100000]", "expected_output": "1", "is_sample": False}, # Max value 10^5 is 6 digits (even)
        {"input": "[i for i in range(1, 101)]", "expected_output": "90", "is_sample": False}, # 10-99 = 90 numbers
        {"input": "[9, 99, 999, 9999, 99999]", "expected_output": "2", "is_sample": False}
    ]

    # STRESS logic
    test_cases[8]["input"] = json.dumps(list(range(1, 101)))

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

    output_path = "1201-1400/1295_Find_Numbers_with_Even_Number_of_Digits.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
