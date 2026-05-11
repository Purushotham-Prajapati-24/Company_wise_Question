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

<p><strong class="example">Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = "([])"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>
"""

    input_format = "A single line containing the string 's'."
    output_format = "true or false."
    
    constraints = [
        "1 <= s.length <= 10^4",
        "s consists of parentheses only '()[]{}'"
    ]
    
    explanation = """To determine if a string of parentheses is valid in O(N) time:
1. Use a 'stack' data structure to keep track of opening brackets.
2. Define a mapping of closing brackets to their corresponding opening brackets: `) -> (, ] -> [, } -> {`.
3. Iterate through the string character by character:
   - If the character is a closing bracket:
     - Check if the stack is not empty and the top of the stack matches its corresponding opening bracket.
     - If so, pop from the stack.
     - Otherwise, the string is invalid.
   - If the character is an opening bracket:
     - Push it onto the stack.
4. After the iteration, if the stack is empty, return True; otherwise False.

Time Complexity: O(N) where N is string length.
Space Complexity: O(N) for the stack in the worst case (all opening brackets)."""
    
    answer = """def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef isValid(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        print(str(isValid(data)).lower())\n    else:\n        print(\"true\")",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nbool isValid(string s) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string s;\n    if (cin >> s) cout << (isValid(s) ? \"true\" : \"false\") << endl;\n    else cout << \"true\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isValid(String s) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            System.out.println(isValid(sc.next()));\n        } else {\n            System.out.println(true);\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isValid(s) {\n    // User logic\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(isValid(input));\n} else {\n    console.log(true);\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nbool isValid(char* s) {\n    // User logic\n    return false;\n}\n\nint main() {\n    char s[10005];\n    if (scanf(\"%10004s\", s) == 1) {\n        printf(\"%s\\n\", isValid(s) ? \"true\" : \"false\");\n    } else {\n        printf(\"true\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "()", "expected_output": "true", "is_sample": True},
        {"input": "()[]{}", "expected_output": "true", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "(]", "expected_output": "false", "is_sample": False},
        {"input": "([)]", "expected_output": "false", "is_sample": False},
        {"input": "([])", "expected_output": "true", "is_sample": False},
        {"input": "{[]}", "expected_output": "true", "is_sample": False},
        {"input": "[", "expected_output": "false", "is_sample": False},
        # Last three: Stress tests
        {"input": "(".join(["("] * 5000) + ")".join([")"] * 5000), "expected_output": "true", "is_sample": False},
        {"input": "(((".join(["("] * 3333) + ")))".join([")"] * 3334), "expected_output": "false", "is_sample": False},
        {"input": "()".join(["[]{}()"] * 1000), "expected_output": "true", "is_sample": False}
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
