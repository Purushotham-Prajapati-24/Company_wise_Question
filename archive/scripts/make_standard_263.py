import json
import os

def generate_json():
    problem_id = 263
    title = "Ugly Number"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>263 Ugly Number</h3>
<p>An <strong>ugly number</strong> is a positive integer whose prime factors are limited to <code>2</code>, <code>3</code>, and <code>5</code>.</p>
<p>Given an integer <code>n</code>, return <code>true</code> <em>if</em> <code>n</code> <em>is an <strong>ugly number</strong></em>.</p>

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> 6 = 2 &times; 3</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> 14 is not ugly because it includes the prime factor 7.</pre>"""

    input_format = """A single integer n."""
    output_format = """A boolean (true/false) representing if n is an ugly number."""
    
    constraints = [
        "-2^31 <= n <= 2^31 - 1"
    ]
    
    explanation = """To check if a number is ugly, we divide it by 2, 3, and 5 as many times as possible. If the resulting number is 1, the original number was ugly. Numbers less than or equal to 0 are not ugly."""
    
    answer = """def isUgly(n):
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1"""

    boilerplate = {
        "python": "import sys\n\ndef isUgly(n: int) -> bool:\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        n = int(line)\n        print(\"true\" if isUgly(n) else \"false\")",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nbool isUgly(int n) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        cout << (isUgly(n) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean isUgly(int n) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            System.out.println(new Solution().isUgly(sc.nextInt()) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isUgly(n) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(isUgly(parseInt(input)) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nbool isUgly(int n) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%s\\n\", isUgly(n) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "6", "expected_output": "true", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": True},
        {"input": "14", "expected_output": "false", "is_sample": False},
        {"input": "8", "expected_output": "true", "is_sample": False},
        {"input": "15", "expected_output": "true", "is_sample": False},
        {"input": "30", "expected_output": "true", "is_sample": False},
        {"input": "0", "expected_output": "false", "is_sample": False},
        {"input": "-1", "expected_output": "false", "is_sample": False},
        {"input": "2147483647", "expected_output": "false", "is_sample": False},
        {"input": "536870912", "expected_output": "true", "is_sample": False}
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

    output_path = "1-200/263_Ugly_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
