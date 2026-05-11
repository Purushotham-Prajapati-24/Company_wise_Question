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
        "python": "import sys, re\n\ndef isNumber(s: str) -> bool:\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    match = re.search(r's\\s*=\\s*\"(.*?)\"', data)\n    if not match: match = re.search(r'\"(.*?)\"', data)\n    s = match.group(1) if match else data\n    print(str(isNumber(s)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    bool isNumber(string s) {\n        // User Logic Here\n        return false;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(R\"(s\\s*=\\s*\"(.*?)\")\");\n    smatch m;\n    string s;\n    if (regex_search(input, m, rgx)) s = m[1];\n    else {\n        regex rgx2(R\"(\"(.*?)\")\");\n        if (regex_search(input, m, rgx2)) s = m[1];\n        else {\n            s = input;\n            size_t first = s.find_first_not_of(\" \\t\\r\\n\");\n            size_t last = s.find_last_not_of(\" \\t\\r\\n\");\n            if (first != string::npos) s = s.substr(first, (last - first + 1));\n        }\n    }\n    Solution sol;\n    cout << (sol.isNumber(s) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public boolean isNumber(String s) {\n        // User Logic Here\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString().trim();\n        String s = input;\n        Matcher m = Pattern.compile(\"s\\\\s*=\\\\s*\\\"(.*?)\\\"\").matcher(input);\n        if (m.find()) s = m.group(1);\n        else {\n            m = Pattern.compile(\"\\\"(.*?)\\\"\").matcher(input);\n            if (m.find()) s = m.group(1);\n        }\n        Solution sol = new Solution();\n        System.out.println(sol.isNumber(s));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {string} s\n * @return {boolean}\n */\nvar isNumber = function(s) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    let s = input;\n    let match = input.match(/s\\s*=\\s*\"(.*?)\"/);\n    if (!match) match = input.match(/\"(.*?)\"/);\n    if (match) s = match[1];\n    console.log(isNumber(s).toString());\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nbool isNumber(char* s) {\n    // User Logic Here\n    return false;\n}\n\nint main() {\n    char input[1024];\n    if (!fgets(input, sizeof(input), stdin)) return 0;\n    char* s = input;\n    char* start = strchr(input, '\"');\n    if (start) {\n        char* end = strchr(start + 1, '\"');\n        if (end) { *end = '\\0'; s = start + 1; }\n    } else {\n        char* end = input + strlen(input) - 1;\n        while(end > input && (*end == '\\n' || *end == '\\r' || *end == ' ')) { *end = '\\0'; end--; }\n        while(*s == ' ') s++;\n    }\n    printf(\"%s\\n\", isNumber(s) ? \"true\" : \"false\");\n    return 0;\n}"
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
