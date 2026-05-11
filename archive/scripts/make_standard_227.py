import json
import os

def generate_json():
    problem_id = 227
    title = "Basic Calculator II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>227. Basic Calculator II</h3>
<p>Given a string <code>s</code> which represents an expression, <em>evaluate this expression and return its value</em>.&nbsp;</p>

<p>The integer division should truncate toward zero.</p>

<p>You may assume that the given expression is always valid. All intermediate results will be in the range of <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>.</p>

<p><strong>Note:</strong> You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "3+2*2"
<strong>Output:</strong> 7
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = " 3/2 "
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = " 3+5 / 2 "
<strong>Output:</strong> 5
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of integers and operators <code>('+', '-', '*', '/')</code> separated by some number of spaces.</li>
	<li><code>s</code> represents a <strong>valid expression</strong>.</li>
	<li>All the integers in the expression are non-negative integers in the range <code>[0, 2<sup>31</sup> - 1]</code>.</li>
	<li>The answer is <strong>guaranteed</strong> to fit in a <strong>32-bit integer</strong>.</li>
</ul>"""

    input_format = "A string representing the expression s."
    output_format = "An integer value of the evaluated expression."
    
    constraints = [
        "1 <= s.length <= 300,000",
        "Operators: +, -, *, /",
        "Non-negative operands.",
        "Must truncate toward zero for division.",
        "Cannot use eval()."
    ]
    
    explanation = """To evaluate the expression with operator precedence (*, / over +, -):
1. **Iterate and Parse**: Traverse the string character by character.
2. **Current Number**: Accumulate digits into a `curr_num`.
3. **Handle Operators**: Maintain a `last_op` (initialized to '+') and a `stack`.
4. **Logic**: When an operator (or end of string) is hit:
   - If `last_op` is `+`: Push `curr_num` onto stack.
   - If `last_op` is `-`: Push `-curr_num` onto stack.
   - If `last_op` is `*`: Pop the last value, multiply with `curr_num`, and push result back.
   - If `last_op` is `/`: Pop the last value, divide by `curr_num` (truncate toward zero), and push result back.
5. **Final Result**: The answer is the sum of all elements in the stack.
6. **Complexity**:
   - Time: O(N) where N is the length of `s`.
   - Space: O(N) for the stack (can be optimized to O(1) by maintaining a running total if needed)."""
    
    answer = """import math

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        last_op = '+'
        s = s.strip()
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            if char in '+-*/' or i == len(s) - 1:
                if last_op == '+':
                    stack.append(curr_num)
                elif last_op == '-':
                    stack.append(-curr_num)
                elif last_op == '*':
                    stack.append(stack.pop() * curr_num)
                elif last_op == '/':
                    top = stack.pop()
                    # Truncate toward zero: int(a/b) in Python for negative numbers works differently
                    # int(top / curr_num) is correct for truncation toward zero
                    stack.append(int(top / curr_num))
                
                last_op = char
                curr_num = 0
                
        return sum(stack)"""

    boilerplate = {
        "python": "import sys\n\ndef calculate(s):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    print(calculate(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint calculate(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        cout << calculate(line) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int calculate(String s) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String s = br.readLine();\n        if (s == null) s = \"\";\n        System.out.println(new Solution().calculate(s));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction calculate(s) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconsole.log(calculate(input));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint calculate(char* s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char s[300005];\n    if (fgets(s, sizeof(s), stdin)) {\n        int len = strlen(s);\n        if (len > 0 && s[len-1] == '\\n') s[len-1] = '\\0';\n        printf(\"%d\\n\", calculate(s));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3+2*2", "expected_output": "7", "is_sample": True},
        {"input": " 3/2 ", "expected_output": "1", "is_sample": True},
        {"input": " 3+5 / 2 ", "expected_output": "5", "is_sample": True},
        {"input": "100", "expected_output": "100", "is_sample": False},
        {"input": "1-1+1", "expected_output": "1", "is_sample": False},
        {"input": "0*0", "expected_output": "0", "is_sample": False},
        {"input": "1+2-3*4/5", "expected_output": "1", "is_sample": False}, # 1+2 - (12/5) = 1+2-2 = 1
        # Stress Tests (Length 3e5)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(s):
        stack = []
        curr = 0
        last = '+'
        ns = s.replace(" ", "")
        for i, char in enumerate(ns):
            if char.isdigit(): curr = curr * 10 + int(char)
            if not char.isdigit() or i == len(ns) - 1:
                if last == '+': stack.append(curr)
                elif last == '-': stack.append(-curr)
                elif last == '*': stack.append(stack.pop() * curr)
                elif last == '/': stack.append(int(stack.pop() / curr))
                last = char
                curr = 0
        return sum(stack)

    # Stress 8: Large sum
    s8 = "+".join(["1"] * 100000)
    test_cases[7] = {"input": s8, "expected_output": "100000", "is_sample": False}
    # Stress 9: Alternating * and /
    s9 = "10" + "*2/2" * 10000
    test_cases[8] = {"input": s9, "expected_output": "10", "is_sample": False}
    # Stress 10: Mixed complex string
    s10 = "1*2*3*4/4/3/2" * 5000 # 1 * 5000 = 5000 (if nested?) or 1? 
    # Actually just 1*2*3*4/4/3/2 = 1. Repeat should be fine.
    s10 = "1" + "+2*3" * 20000
    test_cases[9] = {"input": s10, "expected_output": str(_solve(s10)), "is_sample": False}

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
        "topics": ["Math", "String", "Stack"],
        "companyIndex": 0
    }

    output_path = "201-400/227_Basic_Calculator_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
