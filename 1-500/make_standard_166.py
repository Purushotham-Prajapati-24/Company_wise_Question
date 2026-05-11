import json
import os

def generate_json():
    problem_id = 166
    title = "Fraction to Recurring Decimal"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>166. Fraction to Recurring Decimal</h3>
<p>Given two integers representing the <code>numerator</code> and <code>denominator</code> of a fraction, return <em>the fraction in string format</em>.</p>

<p>If the fractional part is repeating, enclose the repeating part in parentheses.</p>

<p>If multiple answers are possible, return <strong>any of them</strong>.</p>

<p>It is <strong>guaranteed</strong> that the length of the answer string is less than 10<sup>4</sup> for all the given test cases.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numerator = 1, denominator = 2
<strong>Output:</strong> "0.5"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numerator = 2, denominator = 1
<strong>Output:</strong> "2"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numerator = 4, denominator = 333
<strong>Output:</strong> "0.(012)"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= numerator, denominator &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>denominator != 0</code></li>
</ul>"""

    input_format = "Two lines. Line 1: numerator. Line 2: denominator."
    output_format = "A string representing the fraction. Recurring parts should be in parentheses."
    
    constraints = [
        "-2^31 <= numerator, denominator <= 2^31 - 1",
        "denominator != 0",
        "Answer length < 10^4."
    ]
    
    explanation = """To convert a fraction to a recurring decimal:
1. **Handle Sign and Integer Part**:
   - Determine if the result is negative.
   - Calculate the integer part (`numerator // denominator`).
   - If the remainder is 0, return the integer part.
2. **Handle Fractional Part**:
   - Use a `remainder_map` (Hash Map) to store each remainder and its position in the fractional string.
   - Continue dividing the remainder by the denominator:
     - `remainder *= 10`
     - `digit = remainder // denominator`
     - `remainder %= denominator`
   - Store the `digit` in the result string.
3. **Detect Cycle**:
   - If the current `remainder` has been seen before in `remainder_map`, a cycle is detected.
   - Insert parentheses `(` at the stored position and `)` at the end of the string.
4. **Complexity**:
   - Time Complexity: O(Length of the answer string), which is at most O(Denominator).
   - Space Complexity: O(Length of the answer string)."""
    
    answer = """def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
        
    res = []
    # Sign
    if (numerator < 0) ^ (denominator < 0):
        res.append("-")
        
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Integer part
    res.append(str(numerator // denominator))
    remainder = numerator % denominator
    
    if remainder == 0:
        return "".join(res)
        
    res.append(".")
    
    # Fractional part
    remainder_map = {}
    while remainder != 0:
        if remainder in remainder_map:
            res.insert(remainder_map[remainder], "(")
            res.append(")")
            break
            
        remainder_map[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator
        
    return "".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef fractionToDecimal(numerator, denominator):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().split()\n    if len(lines) >= 2:\n        print(fractionToDecimal(int(lines[0]), int(lines[1])))",
        "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\nstring fractionToDecimal(int numerator, int denominator) {\n    // User logic here\n    return \"\";\n}\nint main() {\n    int numerator, denominator;\n    if (cin >> numerator >> denominator) {\n        cout << fractionToDecimal(numerator, denominator) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static String fractionToDecimal(int numerator, int denominator) {\n        // User logic here\n        return \"\";\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int numerator = sc.nextInt();\n            if (sc.hasNextInt()) {\n                int denominator = sc.nextInt();\n                System.out.println(fractionToDecimal(numerator, denominator));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction fractionToDecimal(numerator, denominator) {\n    // User logic here\n    return \"\";\n}\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (input.length >= 2) {\n    console.log(fractionToDecimal(parseInt(input[0], 10), parseInt(input[1], 10)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\nchar* fractionToDecimal(int numerator, int denominator) {\n    // User logic here\n    return NULL;\n}\nint main() {\n    int numerator, denominator;\n    if (scanf(\"%d %d\", &numerator, &denominator) == 2) {\n        char* res = fractionToDecimal(numerator, denominator);\n        if (res) {\n            printf(\"%s\\n\", res);\n            free(res);\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1\\n2", "expected_output": "0.5", "is_sample": True},
        {"input": "2\\n1", "expected_output": "2", "is_sample": True},
        {"input": "4\\n333", "expected_output": "0.(012)", "is_sample": True},
        {"input": "1\\n6", "expected_output": "0.1(6)", "is_sample": False},
        {"input": "-50\\n8", "expected_output": "-6.25", "is_sample": False},
        {"input": "7\\n-12", "expected_output": "-0.58(3)", "is_sample": False},
        {"input": "22\\n7", "expected_output": "3.(142857)", "is_sample": False},
        # Stress cases
        {"input": "-2147483648\\n-1", "expected_output": "2147483648", "is_sample": False},
        {"input": "1\\n2147483647", "expected_output": "...", "is_sample": False},
        {"input": "1\\n17", "expected_output": "0.(0588235294117647)", "is_sample": False}
    ]
    
    def _solve(n, d):
        if n == 0: return "0"
        res = []
        if (n < 0) ^ (d < 0): res.append("-")
        n, d = abs(n), abs(d)
        res.append(str(n // d))
        rem = n % d
        if rem == 0: return "".join(res)
        res.append(".")
        rmap = {}
        while rem != 0:
            if rem in rmap:
                res.insert(rmap[rem], "(")
                res.append(")")
                break
            rmap[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d
    test_cases[8] = {"input": "1\\n33333", "expected_output": "0.(00003)", "is_sample": False}

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
        "topics": ["Hash Table", "Math", "String"],
        "companyIndex": 0
    }

    output_path = "1-200/166_Fraction_to_Recurring_Decimal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
