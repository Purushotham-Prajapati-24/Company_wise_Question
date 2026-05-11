import json
import os

def generate_json():
    problem_id = 861
    title = "Score After Flipping Matrix"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>861. Score After Flipping Matrix</h3>
<p>You are given an <code>m x n</code> binary matrix <code>grid</code>.</p>

<p>A <strong>move</strong> consists of choosing any row or column and flipping each value in that row or column (i.e., changing all <code>0</code>'s to <code>1</code>'s, and all <code>1</code>'s to <code>0</code>'s).</p>

<p>Every row of the matrix is interpreted as a binary number, and the <strong>score</strong> of the matrix is the sum of these numbers.</p>

<p>Return <em>the highest possible <strong>score</strong> after making at most any number of <strong>moves</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/matrix.jpg" style="width: 422px; height: 162px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
<strong>Output:</strong> 39
<strong>Explanation:</strong> 0-indexed [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
flip T row 0: [[1,1,0,0],[1,0,1,0],[1,1,0,0]]
flip T column 1: [[1,0,0,0],[1,1,1,0],[1,0,0,0]]
flip T column 2: [[1,0,1,0],[1,1,0,0],[1,0,1,0]]
flip T column 3: [[1,0,1,1],[1,1,0,1],[1,0,1,1]]
Binary: 1011(11) + 1101(13) + 1011(11) = 35? Wait, Example 1 explanation in LeetCode is 39.
Wait, let me check the example result 39.
1011 + 1101 + 1011 = 11 + 13 + 11 = 35. 
Wait, the example result is 39. Let's re-verify.
Original: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Row flip 0: [[1,1,0,0],[1,0,1,0],[1,1,0,0]]
Col 2 flip: [[1,1,1,0],[1,0,0,0],[1,1,1,0]]
Col 3 flip: [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
1111(15) + 1001(9) + 1111(15) = 15+9+15 = 39. Correct.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "Two integers m and n, followed by m lines each containing n binary digits."
    output_format = "An integer representing the maximum score."
    
    constraints = ["1 <= m", "n <= 20", "Row/Column flips allowed.", "Maximize sum of row binary values."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def matrixScore(grid):
    m, n = len(grid), len(grid[0])
    # Flip rows
    for i in range(m):
        if grid[i][0] == 0:
            for j in range(n):
                grid[i][j] ^= 1
    
    res = 0
    for j in range(n):
        count_one = 0
        for i in range(m):
            if grid[i][j] == 1:
                count_one += 1
        res += max(count_one, m - count_one) * (1 << (n - 1 - j))
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef matrixScore(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    grid = input_data[0] if len(input_data) > 0 else \"\"\n    print(matrixScore(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint matrixScore(string grid) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string grid; cin >> grid;\n    cout << matrixScore(grid) << endl;\n    return 0;\n}",
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
