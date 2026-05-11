import json
import os

def generate_json():
    problem_id = 780
    title = "Reaching Points"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>780. Reaching Points</h3>
<p>Given four integers <code>sx</code>, <code>sy</code>, <code>tx</code>, and <code>ty</code>, return <code>true</code><em> if it is possible to convert the point </em><code>(sx, sy)</code><em> to the point </em><code>(tx, ty)</code> <em>through some number of <strong>transformations</strong></em>.</p>
<p>A <strong>transformation</strong> on a point <code>(x, y)</code> consists of converting it to either <code>(x, x + y)</code> or <code>(x + y, y)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> sx = 1, sy = 1, tx = 3, ty = 5
<strong>Output:</strong> true
<strong>Explanation:</strong>
One series of transformations is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> sx = 1, sy = 1, tx = 2, ty = 2
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> sx = 1, sy = 1, tx = 1, ty = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 <= sx, sy, tx, ty <= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Four integers sx, sy, tx, and ty."
    output_format = "A boolean representing if (tx, ty) is reachable from (sx, sy)."
    
    constraints = ["1 <= sx", "sy", "tx", "ty <= 10^9"]
    
    explanation = """HARD problem on ."""
    
    answer = """def reachingPoints(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if tx == sx and ty == sy:
            return True
        if tx > ty:
            if ty > sy:
                tx %= ty
            else:
                return (tx - sx) % ty == 0
        elif ty > tx:
            if tx > sx:
                ty %= tx
            else:
                return (ty - sy) % tx == 0
        else:
            break
    return tx == sx and ty == sy"""

    boilerplate = {
        "python": "import sys\n\ndef reachingPoints(sx, sy, tx, ty):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    sx = input_data[0].strip() if len(input_data) > 0 else \"\"\n    sy = input_data[1].strip() if len(input_data) > 1 else \"\"\n    tx = input_data[2].strip() if len(input_data) > 2 else \"\"\n    ty = input_data[3].strip() if len(input_data) > 3 else \"\"\n    print(reachingPoints(sx, sy, tx, ty))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint reachingPoints(string sx, string sy, string tx, string ty) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string sx; cin >> sx;\n    string sy; cin >> sy;\n    string tx; cin >> tx;\n    string ty; cin >> ty;\n    cout << reachingPoints(sx, sy, tx, ty) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "[1, 1, 3, 5]", "expected_output": "true", "is_sample": True},
        {"input": "[1, 1, 2, 2]", "expected_output": "false", "is_sample": True},
        {"input": "[1, 1, 1, 1]", "expected_output": "true", "is_sample": True},
        {"input": "[1, 1, 10, 1]", "expected_output": "true", "is_sample": False},
        {"input": "[2, 2, 10, 2]", "expected_output": "true", "is_sample": False},
        {"input": "[2, 2, 11, 2]", "expected_output": "false", "is_sample": False},
        {"input": "[1, 1, 1000000000, 1]", "expected_output": "true", "is_sample": False},
        {"input": "[10, 10, 100, 100]", "expected_output": "false", "is_sample": False},
        {"input": "[3, 3, 12, 9]", "expected_output": "true", "is_sample": False}, # (3,3)->(3,6)->(3,9)->(12,9)
        {"input": "[3, 7, 3, 17]", "expected_output": "false", "is_sample": False}]

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

    output_path = "1-1000/780_Reaching_Points.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
