import json
import os
import math

def generate_json():
    problem_id = 633
    title = "Sum of Square Numbers"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>633. Sum of Square Numbers</h3>
<p>Given a non-negative integer <code>c</code>, decide whether there <b>exist</b> two integers <code>a</code> and <code>b</code> such that <code>a<sup>2</sup> + b<sup>2</sup> = c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> c = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 * 1 + 2 * 2 = 5
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> c = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= c &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
"""

    input_format = "A single non-negative integer c."
    output_format = "A boolean (true/false) representing if a^2 + b^2 = c exists."
    
    constraints = [
        "0 <= c <= 2^31 - 1"
    ]
    
    explanation = """To check if a^2 + b^2 = c:
1. Use the two-pointers approach.
2. Initialize `a = 0` and `b = int(sqrt(c))`.
3. While `a <= b`:
   - Calculate `sum_sq = a*a + b*b`.
   - If `sum_sq == c`, return `True`.
   - If `sum_sq < c`, increment `a` to increase the sum.
   - If `sum_sq > c`, decrement `b` to decrease the sum.
4. If no such `a, b` are found, return `False`."""
    
    answer = """import math

def judgeSquareSum(c):
    a = 0
    b = int(math.sqrt(c))
    while a <= b:
        sum_sq = a*a + b*b
        if sum_sq == c:
            return True
        elif sum_sq < c:
            a += 1
        else:
            b -= 1
    return False"""

    boilerplate = {
        "python": "import sys\\nimport math\\n\\ndef judgeSquareSum(c):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <cmath>\\n\\nusing namespace std;\\n\\nclass Solution { public: bool judgeSquareSum(int c) { return false; } };",
        "java": "class Solution { public boolean judgeSquareSum(int c) { return false; } }",
        "javascript": "const fs = require('fs');",
        "c": "bool judgeSquareSum(int c) { }"
    }

    test_cases = [
        {"input": "5", "expected_output": "true", "is_sample": True},
        {"input": "3", "expected_output": "false", "is_sample": True},
        {"input": "0", "expected_output": "true", "is_sample": False},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "2", "expected_output": "true", "is_sample": False},
        {"input": "4", "expected_output": "true", "is_sample": False},
        {"input": "10", "expected_output": "true", "is_sample": False},
        {"input": "2147483647", "expected_output": "false", "is_sample": False},
        {"input": "2147483646", "expected_output": "false", "is_sample": False},
        {"input": "2147482624", "expected_output": "true", "is_sample": False}
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
        "topics": ["Two Pointers", "Math", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "401-600/633_Sum_of_Square_Numbers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
