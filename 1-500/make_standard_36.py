import json
import os

def generate_json():
    problem_id = 36
    title = "Valid Sudoku"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>36. Valid Sudoku</h3>
<p>Determine if a&nbsp;<code>9 x 9</code> Sudoku board&nbsp;is valid.&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:</p>

<ol>
	<li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.</li>
	<li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
	<li>Each of the nine&nbsp;<code>3 x 3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
	<li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" />
<pre>
<strong>Input:</strong> board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,["..",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being <strong>8</strong>. Since there are two 8&#39;s in the top left 3x3 sub-box, it is invalid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> is a digit <code>1-9</code> or <code>&#39;.&#39;</code>.</li>
</ul>"""

    input_format = "9 lines, each with 9 characters representing a row of the Sudoku board."
    output_format = "A boolean 'true' if the board is valid, 'false' otherwise."
    
    constraints = [
        "board.length == 9",
        "board[i].length == 9",
        "board[i][j] is a digit '1'-'9' or '.'"
    ]
    
    explanation = """To determine if a 9x9 Sudoku board is valid in a single pass:
1. Use three collections of sets: 
   - `rows`: 9 sets to track digits in each row.
   - `cols`: 9 sets to track digits in each column.
   - `boxes`: 9 sets to track digits in each 3x3 sub-box.
2. Iterate through every cell `(r, c)` of the board.
3. If the cell contains a digit `val`:
   - Calculate the corresponding box index: `box_idx = (r // 3) * 3 + (c // 3)`.
   - Check if `val` already exists in `rows[r]`, `cols[c]`, or `boxes[box_idx]`.
   - If it does, a rule is violated; return `False`.
   - If not, add `val` to all three relevant sets.
4. If the entire board is processed without violations, return `True`.

This approach ensures that every filled cell satisfies the row, column, and 3x3 sub-box constraints.

Time Complexity: O(1) as the board size is fixed at 9x9 (81 cells).
Space Complexity: O(1) for the sets tracking a maximum of 81 digits."""
    
    answer = """def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            
            box_idx = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
            
    return True"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef isValidSudoku(board):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    chars = re.findall(r'[1-9.]', data)\n    if len(chars) >= 81:\n        board = [chars[i:i+9] for i in range(0, 81, 9)]\n        print(str(isValidSudoku(board)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nbool isValidSudoku(vector<vector<char>>& board) {\n    // User logic\n    return true;\n}\n\nint main() {\n    vector<char> all_chars;\n    char c;\n    while (cin >> c) {\n        if ((c >= '1' && c <= '9') || c == '.') {\n            all_chars.push_back(c);\n        }\n    }\n    if (all_chars.size() >= 81) {\n        vector<vector<char>> board(9, vector<char>(9));\n        for (int i = 0; i < 81; ++i) board[i/9][i%9] = all_chars[i];\n        cout << (isValidSudoku(board) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isValidSudoku(char[][] board) {\n        // User logic\n        return true;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNext()) {\n            sb.append(sc.next());\n        }\n        String s = sb.toString().replaceAll(\"[^1-9.]\", \"\");\n        if (s.length() >= 81) {\n            char[][] board = new char[9][9];\n            for (int i = 0; i < 81; i++) board[i/9][i%9] = s.charAt(i);\n            System.out.println(isValidSudoku(board) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isValidSudoku(board) {\n    // User logic\n    return true;\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst chars = (data.match(/[1-9.]/g) || []);\nif (chars.length >= 81) {\n    const board = [];\n    for (let i = 0; i < 9; i++) board.push(chars.slice(i * 9, i * 9 + 9));\n    console.log(isValidSudoku(board) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <ctype.h>\n\nbool isValidSudoku(char** board, int boardSize, int* boardColSize) {\n    // User logic\n    return true;\n}\n\nint main() {\n    char all_chars[1000];\n    int count = 0;\n    int c;\n    while ((c = getchar()) != EOF) {\n        if ((c >= '1' && c <= '9') || c == '.') {\n            all_chars[count++] = (char)c;\n        }\n    }\n    if (count >= 81) {\n        char* board[9];\n        int colSizes[9];\n        for (int i = 0; i < 9; i++) {\n            board[i] = malloc(10);\n            for (int j = 0; j < 9; j++) board[i][j] = all_chars[i * 9 + j];\n            board[i][9] = '\\0';\n            colSizes[i] = 9;\n        }\n        printf(isValidSudoku(board, 9, colSizes) ? \"true\\n\" : \"false\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {
            "input": "53..7....\n6..195...\n.98....6.\n8...6...3\n4..8.3..1\n7...2...6\n.6....28.\n...419..5\n....8..79",
            "expected_output": "true",
            "is_sample": True
        },
        {
            "input": "83..7....\n6..195...\n.98....6.\n8...6...3\n4..8.3..1\n7...2...6\n.6....28.\n...419..5\n....8..79",
            "expected_output": "false",
            "is_sample": True
        },
        # Middle five: Diverse non-duplicate cases
        {
            "input": ".........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........",
            "expected_output": "true",
            "is_sample": False
        },
        {
            "input": "123456789\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........",
            "expected_output": "true",
            "is_sample": False
        },
        {
            "input": "11.......\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........",
            "expected_output": "false",
            "is_sample": False
        },
        {
            "input": "1........\n1........\n.........\n.........\n.........\n.........\n.........\n.........\n.........",
            "expected_output": "false",
            "is_sample": False
        },
        {
            "input": "1........\n..1......\n.........\n.........\n.........\n.........\n.........\n.........\n.........",
            "expected_output": "false",
            "is_sample": False
        },
        # Last three: Stress tests
        {
            "input": "123456789\n456789123\n789123456\n231564897\n564897231\n897231564\n312645978\n645978312\n978312645",
            "expected_output": "true",
            "is_sample": False
        },
        {
            "input": "123456789\n456789123\n789123456\n231564897\n564897231\n897231564\n312645978\n645978312\n978312649",
            "expected_output": "false",
            "is_sample": False
        },
        {
            "input": ".2.4.6.8.\n1.3.5.7.9\n.2.4.6.8.\n1.3.5.7.9\n.2.4.6.8.\n1.3.5.7.9\n.2.4.6.8.\n1.3.5.7.9\n.2.4.6.8.",
            "expected_output": "false",
            "is_sample": False
        }
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
        "topics": ["Array", "Hash Table", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/36_Valid_Sudoku.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
