import json
import os

def generate_json():
    problem_id = 224
    title = "Basic Calculator"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>224. Basic Calculator</h3>
<p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it and return the result of the evaluation.</p>

<p><strong>Note:</strong> You are <strong>not</strong> allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "1 + 1"
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = " 2-1 + 2 "
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(1+(4+5+2)-3)+(6+8)"
<strong>Output:</strong> 23
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of digits, <code>'+'</code>, <code>'-'</code>, <code>'('</code>, <code>')'</code>, and <code>' '</code>.</li>
	<li><code>s</code> represents a valid expression.</li>
	<li><code>'+'</code> is <strong>not</strong> used as a unary operation (e.g., <code>"+1"</code> and <code>"+(2 + 3)"</code> are invalid).</li>
	<li><code>'-'</code> <strong>can</strong> be used as a unary operation (e.g., <code>"-1"</code> and <code>"-(2 + 3)"</code> are valid).</li>
	<li>There will be no two consecutive operators in the input.</li>
	<li>Every number and running calculation will fit in a signed 32-bit integer.</li>
</ul>"""

    input_format = "A single string s representing a mathematical expression."
    output_format = "An integer representing the result of the expression."
    
    constraints = [
        "1 <= s.length <= 3 * 10^5",
        "O(N) time complexity expected.",
        "O(N) space complexity expected for the recursion stack or custom stack."
    ]
    
    explanation = """To evaluate a basic calculator expression with parentheses:
1. **Stack for State Persistence**:
   - Use a stack to save the current result and the sign before an opening parenthesis `(`.
   - Maintain a `res` (running total), a `num` (current parsed integer), and a `sign` (1 for '+', -1 for '-').
2. **Parsing Logic**:
   - Iterate through the string character by character:
     - If it's a **digit**: Update `num`.
     - If it's **'+'** or **'-'**: add `sign * num` to `res`, reset `num`, and update `sign`.
     - If it's **'('**: Push current `res` and `sign` onto the stack. Reset `res` and `sign` to evaluate the inner expression.
     - If it's **')'**: Add `sign * num` to `res`. Multiply `res` by the sign popped from the stack, then add the result popped from the stack.
3. **Complexity**:
   - Time Complexity: O(N) since we visit each character once.
   - Space Complexity: O(N) in the worst case (deeply nested parentheses) to store state on the stack."""
    
    answer = """def calculate(s: str) -> int:
    stack = []
    res = 0
    num = 0
    sign = 1
    
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '+':
            res += sign * num
            num = 0
            sign = 1
        elif c == '-':
            res += sign * num
            num = 0
            sign = -1
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            num = 0
            res *= stack.pop() # sign
            res += stack.pop() # prev res
            
    res += sign * num
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef calculate(s):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    print(calculate(s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint calculate(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        cout << calculate(line) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int calculate(String s) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String s = br.readLine();\n        if (s == null) s = \"\";\n        System.out.println(new Solution().calculate(s));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction calculate(s) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconsole.log(calculate(input));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint calculate(char* s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char s[300005];\n    if (fgets(s, sizeof(s), stdin)) {\n        int len = strlen(s);\n        if (len > 0 && s[len-1] == '\\n') s[len-1] = '\\0';\n        printf(\"%d\\n\", calculate(s));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 + 1", "expected_output": "2", "is_sample": True},
        {"input": " 2-1 + 2 ", "expected_output": "3", "is_sample": True},
        {"input": "(1+(4+5+2)-3)+(6+8)", "expected_output": "23", "is_sample": True},
        {"input": "-2+1", "expected_output": "-1", "is_sample": False},
        {"input": "-(2 + 3)", "expected_output": "-5", "is_sample": False},
        {"input": "2147483647", "expected_output": "2147483647", "is_sample": False},
        {"input": "1-(5)", "expected_output": "-4", "is_sample": False},
        # Stress cases
        {"input": "(".join(["1+1"]*100) + " )"*100, "expected_output": "..." , "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": " - ( - 2)", "expected_output": "2", "is_sample": False}
    ]
    
    # Correcting stress case 8 logic
    def _solve(s):
        stack = []; res = 0; num = 0; sign = 1
        for i in range(len(s)):
            c = s[i]
            if c.isdigit(): num = num * 10 + int(c)
            elif c == '+': res += sign * num; num = 0; sign = 1
            elif c == '-': res += sign * num; num = 0; sign = -1
            elif c == '(': stack.append(res); stack.append(sign); res = 0; sign = 1
            elif c == ')': res += sign * num; num = 0; res *= stack.pop(); res += stack.pop()
        res += sign * num
        return res
        
    test_cases[7]["input"] = "1 + " + "+".join(["(1+1)"]*100)
    test_cases[7]["expected_output"] = str(_solve(test_cases[7]["input"]))

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
        "topics": ["Math", "String", "Stack", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/224_Basic_Calculator.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
