import json
import os

def generate_json():
    problem_id = 8
    title = "String to Integer (atoi)"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>8. String to Integer (atoi)</h3>
<p>Implement the <code>myAtoi(string s)</code> function, which converts a string to a 32-bit signed integer.</p>

<p>The algorithm for <code>myAtoi(string s)</code> is as follows:</p>

<ol>
	<li><strong>Whitespace</strong>: Ignore any leading whitespace (<code>" "</code>).</li>
	<li><strong>Signedness</strong>: Determine whether the final result is negative or positive by checking if the next character is <code>'-'</code> or <code>'+'</code>. If neither is present, assume the result is positive.</li>
	<li><strong>Conversion</strong>: Read the next characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.</li>
	<li><strong>Rounding</strong>: If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then round the integer to remain in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be rounded to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup> - 1</code> should be rounded to <code>2<sup>31</sup> - 1</code>.</li>
</ol>

<p>Return the integer as the final result.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "42"</span></p>

<p><strong>Output:</strong> <span class="example-io">42</span></p>

<p><strong>Explanation:</strong></p>

<pre>
The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>42</u>" ("42" is read in)
           ^
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = " -042"</span></p>

<p><strong>Output:</strong> <span class="example-io">-42</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: "<u> </u>-042" (leading whitespace is read and ignored)
          ^
Step 2: " -<u>-</u>042" ('-' is read, so the result should be negative)
           ^
Step 3: " -<u>042</u>" ("042" is read in, leading zeros ignored in the result)
               ^
</pre>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "1337c0d3"</span></p>

<p><strong>Output:</strong> <span class="example-io">1337</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>1337</u>c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
</pre>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "0-1"</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<pre>
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>0</u>-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
</pre>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "words and 987"</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Reading stops at the first non-digit character 'w'.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), digits (<code>0-9</code>), <code>' '</code>, <code>'+'</code>, <code>'-'</code>, and <code>'.'</code>.</li>
</ul>
"""

    input_format = "A single line containing the string 's'."
    output_format = "An integer representing the converted 32-bit signed value."
    
    constraints = [
        "0 <= s.length <= 200",
        "s consists of English letters, digits, spaces, '+', '-', and '.'"
    ]
    
    explanation = """To implement String to Integer (atoi) following 32-bit signed rules:
1. Strip leading whitespace.
2. Check for an optional '+' or '-' sign. If present, set the sign resulting variable accordingly.
3. Read characters from left to right until a non-digit character or end of string.
4. Convert digits to an integer while ensuring we handle the digits one by one.
5. In each step, if the intermediate value exceeds the 32-bit signed integer range ([-2^31, 2^31 - 1]), clamp it to the nearest edge (INT_MIN or INT_MAX).
6. Return the final signed clampled integer.

This logic ensures correct conversion and bounds handling as specified."""
    
    answer = """def myAtoi(s):
    s = s.strip()
    if not s: return 0
    sign = 1
    if s[0] in ['-', '+']:
        if s[0] == '-': sign = -1
        s = s[1:]
    res = 0
    for char in s:
        if not char.isdigit(): break
        res = res * 10 + int(char)
    res *= sign
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    return max(INT_MIN, min(INT_MAX, res))"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef myAtoi(s: str) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if data:\n        s = data[0].strip()\n        if (s.startswith('\"') and s.endswith('\"')) or (s.startswith(\"'\") and s.endswith(\"'\")):\n            s = s[1:-1]\n        print(myAtoi(s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint myAtoi(string s) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string s;\n    if (getline(cin, s)) {\n        // Robustly strip surrounding quotes and whitespace\n        s.erase(0, s.find_first_not_of(\" \\t\\n\\r\"));\n        s.erase(s.find_last_not_of(\" \\t\\n\\r\") + 1);\n        if (s.size() >= 2 && ((s.front() == '\"' && s.back() == '\"') || (s.front() == '\\'' && s.back() == '\\''))) {\n            s = s.substr(1, s.size() - 2);\n        }\n        cout << myAtoi(s) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int myAtoi(String s) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.length() >= 2 && ((s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) || (s.startsWith(\"'\") && s.endsWith(\"'\")))) {\n                s = s.substring(1, s.length() - 1);\n            }\n            System.out.println(myAtoi(s));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction myAtoi(s) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length > 0) {\n    let s = input[0].trim();\n    if ((s.startsWith('\"') && s.endsWith('\"')) || (s.startsWith(\"'\") && s.endsWith(\"'\"))) {\n        s = s.substring(1, s.length - 1);\n    }\n    console.log(myAtoi(s));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <ctype.h>\n\nint myAtoi(char* s) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char s[2000];\n    if (fgets(s, sizeof(s), stdin)) {\n        // Strip trailing newline\n        s[strcspn(s, \"\\r\\n\")] = 0;\n        char* start = s;\n        // Trim leading space\n        while(isspace(*start)) start++;\n        // Trim surrounding quotes\n        int len = strlen(start);\n        if (len >= 2 && ((start[0] == '\"' && start[len-1] == '\"') || (start[0] == '\\'' && start[len-1] == '\\''))) {\n            start[len-1] = 0;\n            start++;\n        }\n        printf(\"%d\\n\", myAtoi(start));\n    }\n    return 0;\n}"
    }
  

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "42", "expected_output": "42", "is_sample": True},
        {"input": " -42", "expected_output": "-42", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "4193 with words", "expected_output": "4193", "is_sample": False},
        {"input": "words and 987", "expected_output": "0", "is_sample": False},
        {"input": "+1", "expected_output": "1", "is_sample": False},
        {"input": "  +0 123", "expected_output": "0", "is_sample": False},
        {"input": "0-1", "expected_output": "0", "is_sample": False},
        # Last three: Stress tests
        {"input": "-91283472332", "expected_output": "-2147483648", "is_sample": False},
        {"input": "2147483648", "expected_output": "2147483647", "is_sample": False},
        {"input": " ".join(["9"] * 50), "expected_output": "2147483647", "is_sample": False}
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
        "topics": ["String", "Math"],
        "companyIndex": 0
    }

    output_path = "1-200/8_String_to_Integer_atoi.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
