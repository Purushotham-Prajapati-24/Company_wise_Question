import json
import os

def generate_json():
    problem_id = 20
    title = "Valid Parentheses"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>20. Valid Parentheses</h3>
<p>Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>
<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>"""

    input_format = "A string 's' consisting of parentheses."
    output_format = "Boolean true or false."
    
    constraints = [
        "1 <= s.length <= 10^4",
        "s consists of parentheses only '()[]{}'"
    ]
    
    explanation = """Use a stack to store opening brackets.
When a closing bracket is encountered, check if it matches the top of the stack.
If it doesn't match or the stack is empty, return false.
Finally, check if the stack is empty."""
    
    answer = """def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top: return False
        else:
            stack.append(char)
    return not stack"""

    boilerplate = {
        "python": "import sys\n\ndef isValid(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    s = data.replace('\"', '').replace(\"'\", \"\").split('=')[-1].strip()\n    print(str(isValid(s)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <stack>\n#include <algorithm>\n\nusing namespace std;\n\nbool isValid(string s) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        string s = \"\";\n        size_t eq = line.find('=');\n        string clean = (eq != string::npos) ? line.substr(eq + 1) : line;\n        for(char c : clean) {\n            if (c == '(' || c == ')' || c == '[' || c == ']' || c == '{' || c == '}') s += c;\n        }\n        cout << (isValid(s) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isValid(String s) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        if (line.contains(\"=\")) line = line.substring(line.indexOf('=') + 1);\n        StringBuilder sb = new StringBuilder();\n        for (char c : line.toCharArray()) {\n            if (\"()[]{}\".indexOf(c) != -1) sb.append(c);\n        }\n        System.out.println(isValid(sb.toString()));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isValid(s) {\n    // User logic\n    return false;\n}\n\nlet input = fs.readFileSync(0, 'utf-8').trim();\nif (input.includes('=')) input = input.split('=')[1];\nconst s = input.replace(/[^\\(\\)\\[\\]\\{\\}]/g, '');\nconsole.log(isValid(s));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nbool isValid(char* s) {\n    // User logic\n    return false;\n}\n\nint main() {\n    char line[100000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char s[100000];\n        int sIdx = 0;\n        char* p = line;\n        if (strchr(line, '=')) p = strchr(line, '=') + 1;\n        while (*p) {\n            if (strchr(\"()[]{}\", *p)) s[sIdx++] = *p;\n            p++;\n        }\n        s[sIdx] = '\\0';\n        printf(\"%s\\n\", isValid(s) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "\"()\"", "expected_output": "true", "is_sample": True},
        {"input": "\"()[]{}\"", "expected_output": "true", "is_sample": True},
        {"input": "\"(]\"", "expected_output": "false", "is_sample": True},
        {"input": "([])", "expected_output": "true", "is_sample": False},
        {"input": "([)]", "expected_output": "false", "is_sample": False},
        {"input": "{[]}", "expected_output": "true", "is_sample": False},
        {"input": "((()))", "expected_output": "true", "is_sample": False},
        {"input": "()()()", "expected_output": "true", "is_sample": False},
        {"input": "((", "expected_output": "false", "is_sample": False},
        {"input": "]]", "expected_output": "false", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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
        "topics": ["String", "Stack"],
        "companyIndex": 0
    }

    output_path = "1-200/20_Valid_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
