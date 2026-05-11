import json
import os

def generate_json():
    problem_id = 29
    title = "Divide Two Integers"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>29. Divide Two Integers</h3>
<p>Given two integers <code>dividend</code> and <code>divisor</code>, divide two integers <strong>without</strong> using multiplication, division, and mod operator.</p>

<p>The integer division should truncate toward zero, which means losing its fractional part. For example, <code>8.345</code> would be truncated to <code>8</code>, and <code>-2.7335</code> would be truncated to <code>-2</code>.</p>

<p>Return <em>the <strong>quotient</strong> after dividing </em><code>dividend</code><em> by </em><code>divisor</code>.</p>

<p><strong>Note: </strong>Assume we are dealing with an environment that could only store integers within the <strong>32-bit signed integer range</strong>: [−2<sup>31</sup>, 2<sup>31</sup> − 1]. For this problem, if the quotient is <strong>strictly greater than</strong> 2<sup>31</sup> - 1, return 2<sup>31</sup> - 1, and if the quotient is <strong>strictly less than</strong> -2<sup>31</sup>, return -2<sup>31</sup>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dividend = 10, divisor = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10/3 = 3.33333... which is truncated to 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dividend = 7, divisor = -3
<strong>Output:</strong> -2
<strong>Explanation:</strong> 7/-3 = -2.33333... which is truncated to -2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= dividend, divisor &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>divisor != 0</code></li>
</ul>"""

    input_format = "A single line containing two integers: 'dividend' and 'divisor'."
    output_format = "An integer representing the quotient."
    
    constraints = [
        "-2^31 <= dividend, divisor <= 2^31 - 1",
        "divisor != 0",
        "Must not use multiplication, division, or modulo operators."
    ]
    
    explanation = """To divide two integers without using standard division operators:
1. Handle the overflow case where `dividend` is -2^31 and `divisor` is -1, which would result in 2^31 (exceeding 32-bit signed range). In this case, return 2^31 - 1.
2. Determine the sign of the quotient using XOR: `negative = (dividend < 0) ^ (divisor < 0)`.
3. Work with the absolute values of `dividend` and `divisor`.
4. Use a bit-manipulation loop to find how many times the `divisor` fits into the `dividend`:
   - Keep doubling the `divisor` (`temp = temp << 1`) while it is less than or equal to the remaining `dividend`.
   - Also keep doubling a counter `i` (`i = i << 1`).
   - Subtract the largest doubled `divisor` from the `dividend` and add the corresponding `i` to the result.
5. Repeat the process until the `dividend` is smaller than the `divisor`.
6. Apply the stored sign to the result and ensure it stays within the [-2^31, 2^31 - 1] range.

Time Complexity: O(log^2 N) where N is the dividend.
Space Complexity: O(1)."""
    
    answer = """def divide(dividend, divisor):
    MAX_INT = 2147483647
    MIN_INT = -2147483648
    
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT
    
    negative = (dividend < 0) ^ (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            i <<= 1
        dividend -= temp
        res += i
    
    if negative:
        res = -res
    
    return min(max(MIN_INT, res), MAX_INT)"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef divide(dividend, divisor):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        parts = [int(x) for x in data.split()]\n        if len(parts) >= 2:\n            print(divide(parts[0], parts[1]))",
        "cpp": "#include <iostream>\n#include <climits>\n\nusing namespace std;\n\nint divide(int dividend, int divisor) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int a, b;\n    if (cin >> a >> b) {\n        cout << divide(a, b) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int divide(int dividend, int divisor) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int a = sc.nextInt();\n            if (sc.hasNextInt()) {\n                int b = sc.nextInt();\n                System.out.println(divide(a, b));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction divide(dividend, divisor) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length >= 2) {\n    const a = parseInt(input[0], 10);\n    const b = parseInt(input[1], 10);\n    console.log(divide(a, b));\n}",
        "c": "#include <stdio.h>\n#include <limits.h>\n\nint divide(int dividend, int divisor) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int a, b;\n    if (scanf(\"%d %d\", &a, &b) == 2) {\n        printf(\"%d\\n\", divide(a, b));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "10 3", "expected_output": "3", "is_sample": True},
        {"input": "7 -3", "expected_output": "-2", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "0 1", "expected_output": "0", "is_sample": False},
        {"input": "1 1", "expected_output": "1", "is_sample": False},
        {"input": "-2147483648 -1", "expected_output": "2147483647", "is_sample": False},
        {"input": "-2147483648 1", "expected_output": "-2147483648", "is_sample": False},
        {"input": "2147483647 1", "expected_output": "2147483647", "is_sample": False},
        # Last three: Stress tests
        {"input": "2147483647 2", "expected_output": "1073741823", "is_sample": False},
        {"input": "-2147483648 2", "expected_output": "-1073741824", "is_sample": False},
        {"input": "100 10", "expected_output": "10", "is_sample": False}
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
        "topics": ["Math", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/29_Divide_Two_Integers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
