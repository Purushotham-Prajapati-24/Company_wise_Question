import json
import os

def generate_json():
    problem_id = 150
    title = "Evaluate Reverse Polish Notation"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>150. Evaluate Reverse Polish Notation</h3>
<p>You are given an array of strings <code>tokens</code> that represents an arithmetic expression in a <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.</p>

<p>Evaluate the expression. Return <em>an integer that represents the value of the expression</em>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The valid operators are <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, and <code>'/'</code>.</li>
	<li>Each operand may be an integer or another expression.</li>
	<li>The division between two integers always <strong>truncates toward zero</strong>.</li>
	<li>There will not be any division by zero.</li>
	<li>The input represents a valid arithmetic expression in reverse polish notation.</li>
	<li>The answer and all the intermediate calculations can be represented in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tokens = ["2","1","+","3","*"]
<strong>Output:</strong> 9
<strong>Explanation:</strong> ((2 + 1) * 3) = 9
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tokens = ["4","13","5","/","+"]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (4 + (13 / 5)) = 6
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
<strong>Output:</strong> 22
<strong>Explanation:</strong> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tokens.length &lt;= 10<sup>4</sup></code></li>
	<li><code>tokens[i]</code> is either an operator: <code>"+"</code>, <code>"-"</code>, <code>"*"</code>, or <code>"/"</code>, or an integer in the range <code>[-200, 200]</code>.</li>
</ul>"""

    input_format = "A single line containing space-separated tokens representing the RPN expression."
    output_format = "An integer representing the evaluated value."
    
    constraints = [
        "1 <= tokens.length <= 10^4",
        "tokens[i] is an operator or integer in [-200, 200].",
        "Division truncates toward zero."
    ]
    
    explanation = """To evaluate a Reverse Polish Notation (Postfix) expression:
1. **Use a Stack**:
   - Iterate through each token in the list.
   - If the token is a number, push it onto the stack.
   - If the token is an operator (+, -, *, /):
     - Pop the top two elements from the stack (let them be `b` and `a`).
     - Perform the operation `a op b`.
     - Push the result back onto the stack.
2. **Handle Division (Truncate toward Zero)**:
   - In Python, `a // b` floored division is not the same as truncation for negative results.
   - Use `int(a / b)` to achieve truncation toward zero.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of tokens.
   - Space Complexity: O(N) for the stack."""
    
    answer = """def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                # Division truncation toward zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]"""

    boilerplate = {
        "python": "import sys\n\ndef evalRPN(tokens):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(evalRPN(data))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <stack>\n#include <sstream>\nusing namespace std;\nint evalRPN(vector<string>& tokens){\n    // User logic\n    return 0;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<string> toks; string t;\n    while(ss>>t) toks.push_back(t);\n    cout<<evalRPN(toks)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int evalRPN(String[] tokens){\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null||line.trim().isEmpty()) return;\n        String[] toks=line.trim().split(\"\\\\s+\");\n        System.out.println(evalRPN(toks));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction evalRPN(tokens){\n    // User logic\n    return 0;\n}\nconsole.log(evalRPN(fs.readFileSync(0,'utf8').trim().split(/\\s+/)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint evalRPN(char** tokens, int tokensSize){\n    // User logic\n    return 0;\n}\nint main(){\n    char buf[100000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    char*arr[10001]; int cnt=0;\n    char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<10001){arr[cnt++]=tok;tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",evalRPN(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "2 1 + 3 *", "expected_output": "9", "is_sample": True},
        {"input": "4 13 5 / +", "expected_output": "6", "is_sample": True},
        {"input": "10 6 9 3 + -11 * / * 17 + 5 +", "expected_output": "22", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2 +", "expected_output": "3", "is_sample": False},
        {"input": "1 2 -", "expected_output": "-1", "is_sample": False},
        {"input": "10 3 /", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"]*5000 + ["2"]*4999 + ["+"]*4999), "expected_output": "...", "is_sample": False},
        {"input": " ".join(["-200"]*5000 + ["1"]*4999 + ["+"]*4999), "expected_output": "...", "is_sample": False},
        {"input": "100 2 / 2 / 2 / 2 /", "expected_output": "6", "is_sample": False}
    ]

    def _solve(tokens):
        st = []
        for t in tokens:
            if t in "+-*/":
                b = st.pop(); a = st.pop()
                if t == "+": st.append(a + b)
                elif t == "-": st.append(a - b)
                elif t == "*": st.append(a * b)
                else: st.append(int(a / b))
            else: st.append(int(t))
        return str(st[0])

    for i in [7, 8]:
        test_cases[i]["expected_output"] = _solve(test_cases[i]["input"].split())

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
        "topics": ["Array", "Math", "Stack"],
        "companyIndex": 0
    }

    output_path = "1-200/150_Evaluate_Reverse_Polish_Notation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
