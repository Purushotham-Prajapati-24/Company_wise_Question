import json
import os

def generate_json():
    problem_id = 485
    title = "Max Consecutive Ones"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>485. Max Consecutive Ones</h3>
<p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "A single line containing space-separated integers for the array nums."
    output_format = "An integer representing the maximum number of consecutive 1s."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "nums[i] is either 0 or 1.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To find the maximum consecutive ones in a binary array:
1. **Single Pass Counting**:
   - Maintain a `max_count` and a `current_count`.
   - Iterate through the array:
     - If the element is `1`, increment `current_count` and update `max_count = max(max_count, current_count)`.
     - If the element is `0`, reset `current_count` to 0.
2. **Result**:
   - After the loop, `max_count` will hold the highest number of consecutive ones found.
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of the array.
   - Space Complexity: O(1) as only two counters are needed."""
    
    answer = """def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_count = 0
    current_count = 0
    for x in nums:
        if x == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count"""

    boilerplate = {
        "python": "import sys\n\ndef findMaxConsecutiveOnes(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(findMaxConsecutiveOnes(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint findMaxConsecutiveOnes(vector<int>& nums) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int findMaxConsecutiveOnes(int[] nums) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function findMaxConsecutiveOnes(nums) {\n    // User logic\n}",
        "c": "int findMaxConsecutiveOnes(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 1 0 1 1 1", "expected_output": "3", "is_sample": True},
        {"input": "1 0 1 1 0 1", "expected_output": "2", "is_sample": True},
        {"input": "0 0 0", "expected_output": "0", "is_sample": True},
        {"input": "1 1 1 1", "expected_output": "4", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "0 1 0 1 0 1", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"]*100000), "expected_output": "100000", "is_sample": False},
        {"input": " ".join(["0"]*100000), "expected_output": "0", "is_sample": False},
        {"input": " ".join(["1", "0"]*50000), "expected_output": "1", "is_sample": False}
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

    output_path = "401-600/485_Max_Consecutive_Ones.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
