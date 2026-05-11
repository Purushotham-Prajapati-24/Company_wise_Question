import json
import os

def generate_json():
    problem_id = 419
    title = "Battleships in a Board"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>419. Battleships in a Board</h3>
<p>Given an <code>m x n</code> matrix <code>board</code> where each cell is a battleship <code>'X'</code> or empty <code>'.'</code>, return <em>the number of the <strong>battleships</strong> on </em><code>board</code>.</p>

<p><strong>Battleships</strong> can only be placed horizontally or vertically on <code>board</code>. In other words, they can only be made of the shape <code>1 x k</code> (1 row, <code>k</code> columns) or <code>k x 1</code> (<code>k</code> rows, 1 column), where <code>k</code> can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> board = [["."]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is either <code>'.'</code> or <code>'X'</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it in one-pass, using only <code>O(1)</code> extra memory and without modifying the values of the board?</p>"""

    input_format = "A 2D matrix `board`."
    output_format = "An integer representing the number of battleships."
    
    constraints = [
        "1 <= m, n <= 200",
        "At least one cell separates two battleships."
    ]
    
    explanation = """To count battleships without modifying the board or using extra space, we only count the "head" of each battleship. A cell (r, c) is a "head" if it contains 'X' and does not have an 'X' above it (r-1, c) or to its left (r, c-1)."""
    
    answer = """class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    if (r == 0 or board[r-1][c] == '.') and (c == 0 or board[r][c-1] == '.'):
                        count += 1
        return count"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def countBattleships(self, board: list[list[str]]) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        board = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.countBattleships(board)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int countBattleships(vector<vector<char>>& board) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<vector<char>> board;\n        string inner;\n        size_t start = 0;\n        while ((start = line.find('[', start + (board.empty() ? 1 : 0))) != string::npos) {\n            size_t end = line.find(']', start);\n            if (end == string::npos) break;\n            string rowStr = line.substr(start + 1, end - start - 1);\n            vector<char> row;\n            stringstream ss(rowStr);\n            string cell;\n            while (getline(ss, cell, ',')) {\n                if (cell.find('X') != string::npos) row.push_back('X');\n                else if (cell.find('.') != string::npos) row.push_back('.');\n            }\n            if(!row.empty()) board.push_back(row);\n            start = end + 1;\n        }\n        Solution sol;\n        cout << sol.countBattleships(board) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int countBattleships(char[][] board) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            List<char[]> rows = new ArrayList<>();\n            int i = 0;\n            while (i < line.length()) {\n                if (line.charAt(i) == '[') {\n                    int end = line.indexOf(']', i);\n                    if (end == -1 || end < i) break;\n                    String rowStr = line.substring(i + 1, end).trim();\n                    if (!rowStr.isEmpty() && !rowStr.startsWith(\"[\")) {\n                        String[] parts = rowStr.split(\",\");\n                        char[] row = new char[parts.length];\n                        for (int k = 0; k < parts.length; k++) {\n                            if (parts[k].contains(\"X\")) row[k] = 'X';\n                            else row[k] = '.';\n                        }\n                        rows.add(row);\n                    }\n                    i = end + 1;\n                } else i++;\n            }\n            char[][] board = rows.toArray(new char[0][0]);\n            Solution sol = new Solution();\n            System.out.println(sol.countBattleships(board));\n        }\n    }\n}",
        "javascript": "var countBattleships = function(board) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    console.log(JSON.stringify(countBattleships(JSON.parse(input))));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint countBattleships(char** board, int boardSize, int* boardColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": '[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]', "expected_output": "2", "is_sample": True},
        {"input": '[["."]]', "expected_output": "0", "is_sample": True},
        {"input": '[["X"]]', "expected_output": "1", "is_sample": False},
        {"input": '[["X","X","X"]]', "expected_output": "1", "is_sample": False},
        {"input": '[["X",".","X"],[".",".","."]]', "expected_output": "2", "is_sample": False},
        {"input": '[["X",".",".","X"],["X",".",".","X"]]', "expected_output": "2", "is_sample": False},
        {"input": '[["X","X"],[".","."],[".","."]]', "expected_output": "1", "is_sample": False},
        # 3 Stress
        {"input": json.dumps([["X" if i == j else "." for j in range(200)] for i in range(200)]), "expected_output": "200", "is_sample": False},
        {"input": json.dumps([["."]*200 for _ in range(200)]), "expected_output": "0", "is_sample": False},
        {"input": json.dumps([["X"]*200 for _ in range(200)]), "expected_output": "1", "is_sample": False}
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
        "topics": ["Array", "Matrix"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Battleships_in_a_Board.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
