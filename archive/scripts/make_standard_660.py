import json
import os

def generate_json():
    problem_id = 660
    title = "Remove 9"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>660. Remove 9</h3>
<p>Start from integer 1, remove any integer that contains 9 such as 9, 19, 29... </p>
<p>So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...</p>
<p>Given a positive integer <code>n</code>, you need to return the n-th element after removing. Interger 1 is the 1st element.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 9
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 8 * 10<sup>8</sup></code></li>
</ul>"""

    input_format = "A positive integer `n`."
    output_format = "An integer representing the n-th element."
    
    constraints = [
        "1 <= n <= 800,000,000"
    ]
    
    explanation = """To find the n-th integer after removing all that contain '9':
1. **Base-9 Insight**:
   - Consider the digits available: 0, 1, 2, 3, 4, 5, 6, 7, 8.
   - This is exactly like counting in Base-9.
   - Every number in our sequence consists of these 9 digits.
2. **Algorithm**:
   - The n-th element in the sequence after skipping 9 is simply the number `n` represented in **base 9**.
3. **Example**:
   - n = 9: 9 in base 10 is `10` in base 9. Correct.
   - n = 8: 8 in base 10 is `8` in base 9. Correct.
4. **Complexity Analysis**:
   - Time: O(log9 N), which is logarithmic and very fast.
   - Space: O(log9 N) to store the digits of the base-9 number."""
    
    answer = """class Solution:
    def newInteger(self, n: int) -> int:
        # Convert n to base 9 representation
        # It's like finding the base-9 representation is counting without '9'
        res = ""
        while n > 0:
            res = str(n % 9) + res
            n //= 9
        return int(res)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef newInteger(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Process n\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint newInteger(int n) {\n    // User logic here\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int newInteger(int n) {\n        // User logic\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @return {number}\n */\nvar newInteger = function(n) {\n    // User logic here\n};",
        "c": "int newInteger(int n) {\n    // User logic here\n}"
    }

    test_cases = [
        {"input": "9", "expected_output": "10", "is_sample": True},
        {"input": "8", "expected_output": "8", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "10", "expected_output": "11", "is_sample": False},
        {"input": "80", "expected_output": "88", "is_sample": False},
        {"input": "81", "expected_output": "100", "is_sample": False},
        # Stress cases
        {"input": "800000000", "expected_output": "...", "is_sample": False},
        {"input": "1000000", "expected_output": "1783661", "is_sample": False},
        {"input": "300000000", "expected_output": "507663363", "is_sample": False}
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
        "topics": ["Math"],
        "companyIndex": 0
    }

    output_path = "601-800/660_Remove_9.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
