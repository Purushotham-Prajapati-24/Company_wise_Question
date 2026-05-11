import json
import os

def generate_json():
    problem_id = 723
    title = "Candy Crush"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>723. Candy Crush</h3>
<p>This problem involves implementing a basic elimination algorithm for a Candy Crush-like game.</p>
<p>You are given an <code>m x n</code> integer array <code>board</code> representing a grid of candy, where <code>board[i][j]</code> indicates the type of candy. A value of <code>0</code> means the cell is empty.</p>
<p>The goal is to restore the board to a <b>stable state</b> by repeatedly crushing candies according to these rules:</p>
<ol>
	<li>If three or more candies of the same type are adjacent vertically or horizontally, crush them all simultaneously. These positions become empty (set to <code>0</code>).</li>
	<li>After crushing, if an empty space has candies above it, those candies will drop down until they hit another candy or the bottom of the board. No new candies drop from outside the top boundary.</li>
	<li>Steps 1 and 2 are repeated until no more candies can be crushed (i.e., the board is stable).</li>
</ol>
<p>Return the stable board.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
<strong>Output:</strong> [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>3 <= m, n <= 50</code></li>
	<li><code>1 <= board[i][j] <= 2000</code></li>
</ul>"""

    input_format = "A 2D integer matrix board."
    output_format = "A 2D integer matrix representing the stable board."
    
    constraints = ["3 <= m", "n <= 50", "1 <= board[i"]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def candyCrush(board):
    R, C = len(board), len(board[0])
    while True:
        crush = set()
        for r in range(R):
            for c in range(C - 2):
                if board[r][c] != 0 and board[r][c] == board[r][c+1] == board[r][c+2]:
                    crush.update({(r, c), (r, c+1), (r, c+2)})
        for r in range(R - 2):
            for c in range(C):
                if board[r][c] != 0 and board[r][c] == board[r+1][c] == board[r+2][c]:
                    crush.update({(r, c), (r+1, c), (r+2, c)})
        if not crush: break
        for r, c in crush: board[r][c] = 0
        for c in range(C):
            idx = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] != 0:
                    board[idx][c] = board[r][c]
                    idx -= 1
            for r in range(idx, -1, -1):
                board[r][c] = 0
    return board"""

    boilerplate = {
        "python": "import sys\n\ndef candyCrush(board):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    board = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(candyCrush(board))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint candyCrush(string board) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string board; cin >> board;\n    cout << candyCrush(board) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]", "expected_output": "[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [210, 0, 0, 0, 214], [310, 0, 0, 113, 314], [410, 0, 0, 213, 414], [610, 211, 112, 313, 614], [710, 311, 412, 613, 714], [810, 411, 512, 713, 1014]]", "is_sample": True},
        {"input": "[[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]", "expected_output": "[[1, 3, 0, 0, 0], [3, 4, 0, 5, 2], [3, 2, 0, 3, 1], [2, 4, 0, 5, 2], [1, 4, 3, 1, 1]]", "is_sample": True},
        {"input": "[[1,1,1],[2,3,4],[5,6,7]]", "expected_output": "[[0, 0, 0], [2, 3, 4], [5, 6, 7]]", "is_sample": False},
        {"input": "[[1,2,3],[1,2,3],[1,2,3]]", "expected_output": "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]", "is_sample": False},
        {"input": "[[1,1,1,1,1]]", "expected_output": "[[0, 0, 0, 0, 0]]", "is_sample": False},
        {"input": "[[1],[1],[1],[1]]", "expected_output": "[[0], [0], [0], [0]]", "is_sample": False},
        {"input": "[[2,2,2,3,3],[2,2,2,3,3],[4,4,4,5,5]]", "expected_output": "[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]", "is_sample": False},
        {"input": "[[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1]]", "expected_output": "[[1, 2, 1, 2, 1], [2, 1, 2, 1, 2], [1, 2, 1, 2, 1]]", "is_sample": False},
        {"input": "[[1,1,2,2],[1,1,2,2],[1,1,3,3],[2,2,3,3]]", "expected_output": "[[1, 1, 2, 2], [1, 1, 2, 2], [1, 1, 3, 3], [2, 2, 3, 3]]", "is_sample": False},
        {"input": "[[10,10,10,10],[2,3,4,5],[2,3,4,5],[2,3,4,5]]", "expected_output": "[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]", "is_sample": False}]

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

    output_path = "1-1000/723_Candy_Crush.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
