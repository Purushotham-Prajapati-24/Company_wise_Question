import json
import os

def generate_json():
    problem_id = 289
    title = "Game of Life"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>289. Game of Life</h3>
<p>According to <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."</p>

<p>The board is made up of an <code>m x n</code> grid of cells, where each cell has an initial state: **live** (represented by a <code>1</code>) or **dead** (represented by a <code>0</code>). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules:</p>

<ol>
	<li>Any **live** cell with **fewer than two live neighbors** dies as if caused by under-population.</li>
	<li>Any **live** cell with **two or three live neighbors** lives on to the next generation.</li>
	<li>Any **live** cell with **more than three live neighbors** dies, as if by over-population.</li>
	<li>Any **dead** cell with **exactly three live neighbors** becomes a live cell, as if by reproduction.</li>
</ol>

<p>The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the <code>m x n</code> grid <code>board</code>, return <em>the next state</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg" style="width: 562px; height: 322px;" />
<pre><strong>Input:</strong> board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg" style="width: 402px; height: 162px;" />
<pre><strong>Input:</strong> board = [[1,1],[1,0]]
<strong>Output:</strong> [[1,1],[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 25</code></li>
	<li><code>board[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong>
<ol>
	<li>Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.</li>
	<li>In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (e.g., live cells are next to the border). How would you address these problems?</li>
</ol>"""

    input_format = "A stringified 2D array representing the board of cell states."
    output_format = "A stringified 2D array representing the next state."
    
    constraints = [
        "1 <= m, n <= 25",
        "Cell values are 0 (dead) or 1 (live)."
    ]
    
    explanation = """To update the Game of Life board in-place:
1. **Original States**: 0 (dead), 1 (live).
2. **State Encoding**: To update simultaneously in-place, we use temporary states to indicate transitions:
   - `2` : **Live to Dead** (was 1, now 0).
   - `-1` : **Dead to Live** (was 0, now 1).
3. **Neighbor Counting**: For each cell, count its 8 neighbors. If a neighbor has state `1` or `2`, it was originally alive.
4. **Apply Rules**:
   - Rule 1 & 3 (Death): If `cell == 1` and `neighbors < 2` or `neighbors > 3`, set `cell = 2`.
   - Rule 4 (Birth): If `cell == 0` and `neighbors == 3`, set `cell = -1`.
5. **Final Pass**: Convert `2` back to `0`, and `-1` back to `1`.
6. **Complexity**:
   - Time: O(M * N) as we iterate over the board twice.
   - Space: O(1) as we update the board in-place."""
    
    answer = """class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return
            
        m, n = len(board), len(board[0])
        
        # 1. State Encoding
        # New State: 2 (Live to Dead), -1 (Dead to Live)
        
        # Directions for neighbors
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        for r in range(m):
            for c in range(n):
                # Count live neighbors
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If neighbor was originally alive (1 or 2)
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1 or board[nr][nc] == 2:
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1
                
                # Apply rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2
                else: # board[r][c] == 0
                    if live_neighbors == 3:
                        board[r][c] = -1
                        
        # 2. Convert to final states
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == -1:
                    board[r][c] = 1"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef gameOfLife(board: list[list[int]]) -> None:\n    # User logic here (modify board in-place)\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        board = json.loads(input_data)\n        gameOfLife(board)\n        print(json.dumps(board))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nvoid gameOfLife(vector<vector<int>>& board) {\n    // User logic here\n}\n\nint main() {\n    string all, line;\n    while (getline(cin, line)) all += line;\n    vector<vector<int>> board;\n    vector<int> row;\n    string num;\n    for (char c : all) {\n        if (c == '[') { num = \"\"; }\n        else if (c == ']') {\n            if (!num.empty()) { row.push_back(stoi(num)); num = \"\"; }\n            if (!row.empty()) { board.push_back(row); row.clear(); }\n        }\n        else if (c == ',') {\n            if (!num.empty()) { row.push_back(stoi(num)); num = \"\"; }\n        }\n        else if (isdigit(c)) num += c;\n    }\n    gameOfLife(board);\n    cout << '[';\n    for (int i = 0; i < (int)board.size(); i++) {\n        if (i) cout << ',';\n        cout << '[';\n        for (int j = 0; j < (int)board[i].size(); j++) {\n            if (j) cout << ',';\n            cout << board[i][j];\n        }\n        cout << ']';\n    }\n    cout << ']' << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public void gameOfLife(int[][] board) {\n        // User logic here\n    }\n\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        String all = sc.useDelimiter(\"\\\\A\").next().trim().replaceAll(\"\\\\s\", \"\");\n        all = all.substring(1, all.length()-1);\n        String[] rowStrs = all.split(\"\\\\],\\\\[\");\n        int[][] board = new int[rowStrs.length][];\n        for (int i = 0; i < rowStrs.length; i++) {\n            String r = rowStrs[i].replaceAll(\"[\\\\[\\\\]]\", \"\");\n            String[] parts = r.split(\",\");\n            board[i] = new int[parts.length];\n            for (int j = 0; j < parts.length; j++) board[i][j] = Integer.parseInt(parts[j]);\n        }\n        new Solution().gameOfLife(board);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < board.length; i++) {\n            if (i > 0) sb.append(',');\n            sb.append('[');\n            for (int j = 0; j < board[i].length; j++) {\n                if (j > 0) sb.append(',');\n                sb.append(board[i][j]);\n            }\n            sb.append(']');\n        }\n        System.out.println(sb.append(']'));\n    }\n}",
        "javascript": "const fs = require('fs');\nconst board = JSON.parse(fs.readFileSync(0, 'utf-8').trim());\n\nfunction gameOfLife(board) {\n    // User logic here\n}\n\ngameOfLife(board);\nconsole.log(JSON.stringify(board));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid gameOfLife(int** board, int boardSize, int* boardColSize) {\n    // User logic here\n}\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]", "expected_output": "[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]", "is_sample": True},
        {"input": "[[1,1],[1,0]]", "expected_output": "[[1,1],[1,1]]", "is_sample": True},
        {"input": "[[0,0],[0,0]]", "expected_output": "[[0,0],[0,0]]", "is_sample": False},
        {"input": "[[1,1],[1,1]]", "expected_output": "[[1,1],[1,1]]", "is_sample": False},
        {"input": "[[0,1,0],[0,1,0],[0,1,0]]", "expected_output": "[[0,0,0],[1,1,1],[0,0,0]]", "is_sample": False},
        {"input": "[[1,0,0],[0,1,0],[0,0,1]]", "expected_output": "[[0,0,0],[0,1,0],[0,0,0]]", "is_sample": False},
        {"input": "[ [1] ]", "expected_output": "[[0]]", "is_sample": False},
        # Stress cases
        {"input": "[[1 if i==j else 0 for j in range(25)] for i in range(25)]", "expected_output": "...", "is_sample": False},
        {"input": "[[1 for j in range(25)] for i in range(25)]", "expected_output": "...", "is_sample": False},
        {"input": "[[0 for j in range(25)] for i in range(25)]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Matrix", "Simulation"],
        "companyIndex": 0
    }

    output_path = "201-400/289_Game_of_Life.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
