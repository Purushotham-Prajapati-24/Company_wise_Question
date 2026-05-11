import json
import os

def generate_json():
    problem_id = 665
    title = "Non-decreasing Array"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>665. Non-decreasing Array</h3>
<p>Given an array <code>nums</code> with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <b>at most one element</b>.</p>

<p>We define an array is non-decreasing if <code>nums[i] &lt;= nums[i + 1]</code> holds for every <code>i</code> (<b>0-indexed</b>) such that (<code>0 &lt;= i &lt;= n - 2</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [4,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You could modify the first 4 to 1 to get a non-decreasing array [1,2,3].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [4,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot get a non-decreasing array by modifying at most one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= n <= 10^4",
        "Modification: max 1 element.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To check if at most one modification makes an array non-decreasing:
1. **The Core Logic**:
   - Traverse the array once.
   - For each index $i$ where $nums[i] > nums[i+1]$, we have a violation.
   - If we have more than one violation, return `false`.
2. **The Decision (Which element to modify?)**:
   - When a violation occurs at $i$, we can either change $nums[i]$ or $nums[i+1]$.
   - Case 1: Change $nums[i]$ to $nums[i+1]$ (the smaller value).
     - This is valid only if it doesn't break the order with $nums[i-1]$. 
     - Check: $i == 0$ or $nums[i-1] \le nums[i+1]$.
   - Case 2: Change $nums[i+1]$ to $nums[i]$ (the larger value).
     - If Case 1 is not possible, we must do this.
3. **Complexity**:
   - Time Complexity: O(N) single pass.
   - Space Complexity: O(1)."""
    
    answer = """def checkPossibility(nums: list[int]) -> bool:
    violations = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            violations += 1
            if violations > 1:
                return False
            # Modifying nums[i] or nums[i+1]
            if i > 0 and nums[i-1] > nums[i+1]:
                nums[i+1] = nums[i]
            else:
                nums[i] = nums[i+1]
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef checkPossibility(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(str(checkPossibility(nums)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nbool checkPossibility(vector<int>& nums) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean checkPossibility(int[] nums) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function checkPossibility(nums) {\n    // User logic\n}",
        "c": "bool checkPossibility(int* nums, int numsSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "4 2 3", "expected_output": "true", "is_sample": True},
        {"input": "4 2 1", "expected_output": "false", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3", "expected_output": "true", "is_sample": False},
        {"input": "3 4 2 3", "expected_output": "false", "is_sample": False},
        {"input": "5 7 1 8", "expected_output": "true", "is_sample": False},
        {"input": "1 1 1", "expected_output": "true", "is_sample": False},
        {"input": "10 5 1", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000, 0, -1)]), "expected_output": "false", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 10001)]), "expected_output": "true", "is_sample": False}
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

    output_path = "601-800/665_Non_decreasing_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
