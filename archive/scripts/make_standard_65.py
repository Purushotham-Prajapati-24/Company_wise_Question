import json
import os

def generate_json():
    problem_id = 65
    title = "Valid Number"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>65. Valid Number</h3>
<p>Given a string <code>s</code>, return <code>true</code> if <code>s</code> is a <strong>valid number</strong>.</p>

<p>For example, all the following are valid numbers: <code>"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"</code>, while the following are not valid numbers: <code>"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"</code>.</p>

<p>Formally, a <strong>valid number</strong> is defined using one of the following definitions:</p>

<ol>
	<li>An <strong>integer number</strong> followed by an optional <strong>exponent</strong>.</li>
	<li>A <strong>decimal number</strong> followed by an optional <strong>exponent</strong>.</li>
</ol>

<p>An <strong>integer number</strong> is defined with an optional sign <code>'-'</code> or <code>'+'</code> followed by digits.</p>

<p>A <strong>decimal number</strong> is defined with an optional sign <code>'-'</code> or <code>'+'</code> followed by one of the following formats:</p>

<ul>
	<li>One or more digits, followed by a dot <code>'.'</code>.</li>
	<li>One or more digits, followed by a dot <code>'.'</code>, followed by one or more digits.</li>
	<li>A dot <code>'.'</code>, followed by one or more digits.</li>
</ul>

<p>An <strong>exponent</strong> is defined with an exponent letter <code>'e'</code> or <code>'E'</code>, followed by an <strong>integer number</strong>.</p>

<p>The digits are defined as one or more digits from <code>0</code> to <code>9</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "0"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "e"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "."
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> consists of only English letters (both uppercase and lowercase), digits (<code>0-9</code>), plus <code>'+'</code>, minus <code>'-'</code>, or dot <code>'.'</code>.</li>
</ul>"""

    input_format = "A single line containing the string s."
    output_format = "true or false as a string."
    
    constraints = [
        "1 <= s.length <= 20",
        "s contains only optional sign (+/-), digits, one dot (.), and one exponent (e/E)."
    ]
    
    explanation = """To validate if a string represents a valid number:
1. **Initialize Flags**: Track `seenDigit`, `seenDot`, and `seenExponent`.
2. **Iterate through characters**:
   - **Digits**: Set `seenDigit = true`.
   - **Signs (+/-)**: Only allowed at index 0 OR immediately after an exponent ('e' or 'E').
   - **Exponent (e/E)**: 
     - Must not have been seen before.
     - Must appear after at least one digit has been seen.
     - Reset `seenDigit = false` for the following integer requirement.
   - **Dot (.)**: 
     - Must not have been seen before.
     - Cannot appear after an exponent has been seen.
   - **Invalid Characters**: Any other character returns false immediately.
3. **Final Condition**: Returns `true` if `seenDigit` is true at the end (mandatory to have digits in the mantissa or as the exponent's integer)."""
    
    answer = """class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit = seenDot = seenExponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seenDigit = True
            elif char in "+-":
                if i > 0 and s[i-1] not in "eE":
                    return False
            elif char in "eE":
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False
            elif char == ".":
                if seenDot or seenExponent:
                    return False
                seenDot = True
            else:
                return False
        
        return seenDigit"""

    boilerplate = {
        "python": "import sys\n\ndef isNumber(s: str) -> bool:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    if not s: sys.exit()\n    print(str(isNumber(s)).lower())",
        "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nbool isNumber(string s) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string s;\n    if (!(cin >> s)) s = \"\";\n    cout << (isNumber(s) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isNumber(String s) {\n        // User logic\n        return false;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine())\n            System.out.println(isNumber(sc.nextLine().trim()));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isNumber(s) {\n    // User logic\n    return false;\n}\n\nconst s = fs.readFileSync(0, 'utf8').trim();\nconsole.log(isNumber(s) ? 'true' : 'false');",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool isNumber(char* s) {\n    // User logic\n    return false;\n}\n\nint main() {\n    char s[25];\n    if (scanf(\"%20s\", s) == 1) {\n        printf(\"%s\\n\", isNumber(s) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "0", "expected_output": "true", "is_sample": True},
        {"input": "e", "expected_output": "false", "is_sample": True},
        {"input": ".", "expected_output": "false", "is_sample": False},
        {"input": "2.", "expected_output": "true", "is_sample": False},
        {"input": ".1", "expected_output": "true", "is_sample": False},
        {"input": "46.e3", "expected_output": "true", "is_sample": False},
        {"input": "+.8", "expected_output": "true", "is_sample": False},
        # Stress Tests (20 chars limit)
        {"input": "-123.456e+78912345", "expected_output": "true", "is_sample": False},
        {"input": "9" * 10 + "." + "8" * 9, "expected_output": "true", "is_sample": False},
        {"input": "+.e+123456789012345", "expected_output": "false", "is_sample": False}
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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = "1-200/65_Valid_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
