import json
import os

def generate_json():
    problem_id = 670
    title = "Maximum Swap"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>670. Maximum Swap</h3>
<p>You are given a non-negative integer <code>num</code>. You can swap two digits at most once to get the maximum valued number.</p>

<p>Return <em>the maximum valued number you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 2736
<strong>Output:</strong> 7236
<strong>Explanation:</strong> Swap the number 2 and the number 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 9973
<strong>Output:</strong> 9973
<strong>Explanation:</strong> No swap.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>"""

    input_format = "A non-negative integer `num`."
    output_format = "An integer representing the maximum value after at most one swap."
    
    constraints = [
        "0 <= num <= 100,000,000"
    ]
    
    explanation = """To get the maximum value by swapping digits at most once:
1. **Greedy Strategy**:
   - To make a number larger, swap a smaller digit at an earlier position (more significant) with a larger digit at a later position (less significant).
   - To make it the *largest* possible:
     - Pre-track the last occurrence of each digit (0-9) in the number.
2. **Algorithm**:
   - Convert the number into a list of digits.
   - For each digit `digits[i]` (from left to right):
     - Check if there exists a larger digit `d` (from 9 down to `digits[i] + 1`).
     - If such a digit `d` exists and its last occurrence index `last[d]` is after `i`:
       - Swap `digits[i]` and `digits[last[d]]`.
       - Immediately return the resulting number (since only one swap is allowed).
   - If no such swap is found, return the original number.
3. **Complexity Analysis**:
   - Time: O(N) where N is the number of digits in `num` (at most 9 digits).
   - Space: O(1) as the `last` array and digit list are small and constant size (~10)."""
    
    answer = """class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        # Store the last seen index of each digit
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i, d in enumerate(digits):
            # Check for a larger digit starting from 9 to d+1
            for larger_digit in range(9, int(d), -1):
                if larger_digit in last and last[larger_digit] > i:
                    # Swap current digit with the last occurrence of the larger digit
                    digits[i], digits[last[larger_digit]] = \
                        digits[last[larger_digit]], digits[i]
                    return int("".join(digits))
                    
        return num"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef maximumSwap(num):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Process num\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <unordered_map>\nusing namespace std;\n\nint maximumSwap(int num) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int maximumSwap(int num) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {number} num\n * @return {number}\n */\nvar maximumSwap = function(num) {\n    // User logic here\n};",
        "c": "int maximumSwap(int num) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "2736", "expected_output": "7236", "is_sample": True},
        {"input": "9973", "expected_output": "9973", "is_sample": True},
        {"input": "1993", "expected_output": "9913", "is_sample": False},
        {"input": "98368", "expected_output": "98863", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "10", "expected_output": "10", "is_sample": False},
        {"input": "12", "expected_output": "21", "is_sample": False},
        {"input": "10909", "expected_output": "90901", "is_sample": False},
        # Stress cases
        {"input": "80000000", "expected_output": "80000000", "is_sample": False},
        {"input": "12345678", "expected_output": "82345671", "is_sample": False},
        {"input": "98765432", "expected_output": "98765432", "is_sample": False}
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
        "topics": ["Math", "Greedy"],
        "companyIndex": 0
    }

    output_path = "601-800/670_Maximum_Swap.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
