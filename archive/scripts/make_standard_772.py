import json
import os

def generate_json():
    problem_id = 772
    title = "Basic Calculator III"
    difficulty = "Hard"
    marks = 30
    
    html_description = """<h3>772. Basic Calculator III</h3>
<p>Implement a basic calculator to evaluate a simple expression string.</p>

<p>The expression string may contain open <code>(</code> and closing parentheses <code>)</code>, the plus <code>+</code> or minus sign <code>-</code>, non-negative integers and empty spaces <code> </code>.</p>

<p>The expression string contains only non-negative integers, <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> operators, open <code>(</code> and closing parentheses <code>)</code> and empty spaces <code> </code>. The integer division should truncate toward zero.</p>

<p>You may assume that the given expression is always valid. All intermediate results will be in the range of <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "1 + 1"
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = " 6-4 / 2 "
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "2*(5+5*2)/3+(6/2+8)"
<strong>Output:</strong> 21
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of digits, <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, <code>'/'</code>, <code>'('</code>, and <code>')'</code>.</li>
	<li><code>s</code> is a <strong>valid</strong> expression.</li>
</ul>
"""

    input_format = "A string s."
    output_format = "An integer result."
    
    constraints = [
        "1 <= s.length <= 10000",
        "Materials: digits, +, -, *, /, (, )",
        "Intermediate results within 32-bit signed range."
    ]
    
    explanation = """To evaluate a complex expression with multiple operator precedences and parentheses:
1. **The Parsing Logic**:
   - Use a recursive helper function `calculate(idx)` that returns the evaluation result and the position after consuming the expression.
   - Use a stack to store terms that are waiting to be summed at the end of the current parenthesis level.
   
2. **Handling Operators**:
   - For `+`: Push the current number into the stack.
   - For `-`: Push the negative of the current number into the stack.
   - For `*`: Pop the top number, multiply it by the current number, and push the result back.
   - For `/`: Pop the top number, divide it by the current number (rounding toward zero), and push back.

3. **Handling Parentheses**:
   - When encountering `(`, recurse. The result of recursion is treated as the "current number" for the current level.
   - When encountering `)`, return the sum of the stack.

Complexity:
- Time: O(N) where N is length of the string. Each character is visited once.
- Space: O(N) for the recursive call stack and the evaluation stack."""
    
    answer = """def calculate(s: str) -> int:
    s = s.replace(" ", "")
    n = len(s)
    
    def helper(idx):
        stack = []
        num = 0
        sign = '+'
        i = idx
        while i < n:
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            
            if char == '(':
                num, i = helper(i + 1)
            
            if not char.isdigit() or i == n - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    top = stack.pop()
                    # Python's // rounds toward floor, we need truncate towards zero
                    if top < 0:
                        stack.append(-(-top // num))
                    else:
                        stack.append(top // num)
                sign = char
                num = 0
                
            if char == ')':
                return sum(stack), i
            i += 1
        return sum(stack), n

    res, _ = helper(0)
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef calculate(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    print(calculate(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int calculate(string s) {\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public int calculate(String s) {\n        return 0;\n    }\n}",
        "javascript": "var calculate = function(s) {\n    return 0;\n};",
        "c": "int calculate(char * s){\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 + 1", "expected_output": "2", "is_sample": True},
        {"input": " 6-4 / 2 ", "expected_output": "4", "is_sample": True},
        {"input": "2*(5+5*2)/3+(6/2+8)", "expected_output": "21", "is_sample": True},
        # Diverse cases
        {"input": "100", "expected_output": "100", "is_sample": False},
        {"input": "(1+2)*(3+4)", "expected_output": "21", "is_sample": False},
        {"input": "10/3*3", "expected_output": "9", "is_sample": False},
        {"input": "2 + 3 * 4 / 2 - 5", "expected_output": "3", "is_sample": False},
        {"input": "1-1+1", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "((((1+1)*2)+3)/7)", "expected_output": "1", "is_sample": False},
        {"input": "10000/10/10/10/10", "expected_output": "1", "is_sample": False}
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
        "topics": ["Math", "String", "Stack", "Recursion"],
        "companyIndex": 0
    }

    output_path = "601-800/772_Basic_Calculator_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
