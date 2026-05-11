import json
import os

def generate_json():
    problem_id = 921
    title = "Minimum Add to Make Parentheses Valid"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>921. Minimum Add to Make Parentheses Valid</h3>
<p>A parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

<ul>
	<li>For example, if <code>s = "()))"</code>, you can insert an opening parenthesis to be <code>"(()))"</code> or a closing parenthesis to be <code>"())))"</code>.</li>
</ul>

<p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "())"
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "((("
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>'('</code> or <code>')'</code>.</li>
</ul>"""

    input_format = "A single string s."
    output_format = "An integer representing the minimum additions."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def minAddToMakeValid(s):
    ans = 0
    bal = 0
    for char in s:
        if char == '(':
            bal += 1
        else:
            if bal > 0:
                bal -= 1
            else:
                ans += 1
    return ans + bal"""

    boilerplate = {
        "python": "import sys\n\ndef minAddToMakeValid(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    s = input_data[0] if len(input_data) > 0 else \"\"\n    print(minAddToMakeValid(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint minAddToMakeValid(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s; cin >> s;\n    cout << minAddToMakeValid(s) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
