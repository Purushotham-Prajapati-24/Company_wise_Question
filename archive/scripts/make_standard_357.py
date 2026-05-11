import json
import os

def generate_json():
    problem_id = 357
    title = "Count Numbers with Unique Digits"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>357. Count Numbers with Unique Digits</h3>
<p>Given an integer <code>n</code>, return the count of all numbers with unique digits, <code>x</code>, where <code>0 &lt;= x &lt; 10<sup>n</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 91
<strong>Explanation:</strong> The answer should be the total numbers in the range of 0 &le; x &lt; 100, excluding 11, 22, 33, 44, 55, 66, 77, 88, 99.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 0
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 8</code></li>
</ul>"""

    input_format = "An integer n."
    output_format = "The count of numbers with unique digits in the range [0, 10^n)."
    
    constraints = ["0 <= n <= 8", "Linear time O(n) solution is expected."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def countNumbersWithUniqueDigits(n):
    if n == 0: return 1
    res = 10
    unique_digits = 9
    available_number = 9
    while n > 1 and available_number > 0:
        unique_digits *= available_number
        res += unique_digits
        available_number -= 1
        n -= 1
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef countNumbersWithUniqueDigits(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    n = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(countNumbersWithUniqueDigits(n))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint countNumbersWithUniqueDigits(string n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string n; cin >> n;\n    cout << countNumbersWithUniqueDigits(n) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "2", "expected_output": "91", "is_sample": True},
        {"input": "0", "expected_output": "1", "is_sample": True},
        {"input": "1", "expected_output": "10", "is_sample": False},
        {"input": "3", "expected_output": "739", "is_sample": False},
        {"input": "4", "expected_output": "5275", "is_sample": False},
        {"input": "5", "expected_output": "32491", "is_sample": False},
        {"input": "6", "expected_output": "168571", "is_sample": False},
        {"input": "7", "expected_output": "712891", "is_sample": False}, # Stressish
        {"input": "8", "expected_output": "2345851", "is_sample": False}, # Max case
        {"input": "1", "expected_output": "10", "is_sample": False}, # Redundant]

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
