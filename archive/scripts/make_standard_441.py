import json
import os

def generate_json():
    problem_id = 441
    title = "Arranging Coins"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>441. Arranging Coins</h3>
<p>You have <code>n</code> coins and you want to build a staircase with these coins. The staircase consists of <code>k</code> rows where the <code>i<sup>th</sup></code> row has exactly <code>i</code> coins. The last row of the staircase <strong>may be</strong> incomplete.</p>

<p>Given the integer <code>n</code>, return <em>the number of <strong>complete rows</strong> of the staircase you will build</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/coinrecord-grid.jpg" style="width: 253px; height: 253px;" />
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> Because the 3<sup>rd</sup> row is incomplete, we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/coinrecord-grid.jpg" style="width: 253px; height: 253px;" />
<pre><strong>Input:</strong> n = 8
<strong>Output:</strong> 3
<strong>Explanation:</strong> Because the 4<sup>th</sup> row is incomplete, we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "An integer n."
    output_format = "An integer k representing the number of complete rows."
    
    constraints = ["1 <= n <= 2^31 - 1", "O(1) time complexity using math or O(log n) using binary search."]
    
    explanation = """EASY problem on ."""
    
    answer = """import math
def arrangeCoins(n):
    return int((math.sqrt(8 * n + 1) - 1) / 2)"""

    boilerplate = {
        "python": "import sys\n\ndef arrangeCoins(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    n = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(arrangeCoins(n))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint arrangeCoins(string n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string n; cin >> n;\n    cout << arrangeCoins(n) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "5", "expected_output": "2", "is_sample": True},
        {"input": "8", "expected_output": "3", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "3", "expected_output": "2", "is_sample": False},
        {"input": "6", "expected_output": "3", "is_sample": False},
        {"input": "10", "expected_output": "4", "is_sample": False},
        {"input": "15", "expected_output": "5", "is_sample": False},
        {"input": "21", "expected_output": "6", "is_sample": False},
        {"input": "28", "expected_output": "7", "is_sample": False},
        # Stress tests]

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
