import json
import os

def generate_json():
    problem_id = 459
    title = "Repeated Substring Pattern"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>459. Repeated Substring Pattern</h3>
<p>Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abab"
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring "ab" twice.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "abcabcabcabc"
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring "abc" four times or the substring "abcabc" twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single string s representing the input string."
    output_format = "Boolean representing if the string can be constructed by repeating a substring."
    
    constraints = ["1 <= s.length <= 10^4", "s consists of lowercase English letters."]
    
    explanation = """EASY problem on ."""
    
    answer = """def solve(s):
    if not s:
        return False
    return s in (s + s)[1:-1]"""

    boilerplate = {
        "python": "import sys\n\ndef solve(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    s = input_data[0] if len(input_data) > 0 else \"\"\n    print(solve(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint solve(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s; cin >> s;\n    cout << solve(s) << endl;\n    return 0;\n}",
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
