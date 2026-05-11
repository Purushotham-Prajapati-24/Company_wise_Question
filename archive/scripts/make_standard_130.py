import json
import os
import sys

def generate_json():
    problem_id = 130
    title = "Surrounded Regions"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>130. Surrounded Regions</h3>
<p>Given an <code>m x n</code> matrix <code>board</code> containing <code>'X'</code> and <code>'O'</code>, <em>flip all regions that are <strong>surrounded</strong></em>.</p>

<p>A region is <strong>surrounded</strong> if it is bordered by <code>'X'</code> and none of the cells in the region are on the edge of the board.</p>

<p>To flip a <strong>surrounded</strong> region, change all <code>'O'</code>s in that region to <code>'X'</code>s in-place.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 550px; height: 237px;" />
<pre><strong>Input:</strong> board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
<strong>Output:</strong> [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
<strong>Explanation:</strong> Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O's are surrounded because they are not on the border and are not adjacent to any 'O' on the border.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> board = [["X"]]
<strong>Output:</strong> [["X"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>board[i][j]</code> is <code>'X'</code> or <code>'O'</code>.</li>
</ul>"""

    input_format = "A stringified 2D array of characters 'X' and 'O'."
    output_format = "A stringified 2D array of characters after flipping surrounded regions."
    
    constraints = [
        "1 <= m, n <= 200",
        "board[i][j] is 'X' or 'O'",
        "Modification must be in-place."
    ]
    
    explanation = """To identify which 'O' regions are surrounded:
1. **Pigeonhole Border 'O's**: Any 'O' on the border, and any 'O' connected to such a border 'O', can NEVER be surrounded.
2. **Mark Non-Surrounded Regions**:
   - Traverse the four boundaries of the matrix.
   - For every 'O' on the boundary, perform a DFS/BFS to mark it and all reachable 'O's with a temporary marker (e.g., '#').
3. **Capture & Flip**:
   - After marking, iterate through the entire board:
     - If a cell is 'O', it must be surrounded (since it wasn't reached from the border). Flip it to 'X'.
     - If a cell is '#', it belongs to a border-connected region. Restore it to 'O'.
4. **Complexity**:
   - Time Complexity: O(M * N) as each cell is visited at most twice.
   - Space Complexity: O(M * N) in the worst case for recursion stack depth."""
    
    answer = """class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        R, C = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] != 'O':
                return
            board[r][c] = '#'
            # Check 4 directions
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
            
        # Step 1: Mark from borders
        for r in range(R):
            dfs(r, 0)
            dfs(r, C-1)
        for c in range(C):
            dfs(0, c)
            dfs(R-1, c)
            
        # Step 2: Flip 'O' to 'X' and '#' back to 'O'
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef solve(board):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if not input_data: sys.exit()\n    board = json.loads(input_data)\n    solve(board)\n    print(json.dumps(board))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\n\nvoid solve(vector<vector<char>>& board) {\n    // User logic\n}\n\nint main() {\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static void solve(char[][] board) {\n        // User logic\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "/**\n * @param {character[][]} board\n * @return {void} Do not return anything, modify board in-place instead.\n */\nvar solve = function(board) {\n    // User logic\n};",
        "c": "void solve(char** board, int boardSize, int* boardColSize) {\n    // User logic\n}"
    }

    test_cases = [
        {"input": '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]', "expected_output": '[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]', "is_sample": True},
        {"input": '[["X"]]', "expected_output": '[["X"]]', "is_sample": True},
        {"input": '[["O","O"],["O","O"]]', "expected_output": '[["O", "O"], ["O", "O"]]', "is_sample": False},
        {"input": '[["X","X","X"],["X","O","X"],["X","X","X"]]', "expected_output": '[["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]', "is_sample": False},
        {"input": '[["X","O","X"],["O","X","O"],["X","O","X"]]', "expected_output": '[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]', "is_sample": False},
        {"input": '[["O","X"],["X","O"]]', "expected_output": '[["O", "X"], ["X", "O"]]', "is_sample": False},
        {"input": '[["O","O","O"],["O","X","O"],["O","O","O"]]', "expected_output": '[["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]', "is_sample": False},
        # Stress Tests (Max 200x200)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(board):
        if not board: return board
        R, C = len(board), len(board[0])
        from collections import deque
        def bfs(r, c):
            if board[r][c] != 'O': return
            queue = deque([(r, c)])
            board[r][c] = '#'
            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'O':
                        board[nr][nc] = '#'
                        queue.append((nr, nc))
        for r in range(R):
            bfs(r, 0); bfs(r, C-1)
        for c in range(C):
            bfs(0, c); bfs(R-1, c)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == '#': board[r][c] = 'O'
        return board

    # Stress Test 8: Large filled circle
    circle = [["X"]*200 for _ in range(200)]
    for r in range(50, 150):
        for c in range(50, 150): circle[r][c] = "O"
    test_cases[7] = {"input": json.dumps(circle), "expected_output": json.dumps(_solve(circle)), "is_sample": False}
    
    # Stress Test 9: Checkerboard
    check = [["X" if (i+j)%2==0 else "O" for j in range(200)] for i in range(200)]
    test_cases[8] = {"input": json.dumps(check), "expected_output": json.dumps(_solve(check)), "is_sample": False}
    
    # Stress Test 10: All 'O's
    all_o = [["O"]*200 for _ in range(200)]
    test_cases[9] = {"input": json.dumps(all_o), "expected_output": json.dumps(_solve(all_o)), "is_sample": False}

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
        "topics": ["Array", "DFS", "BFS", "Union Find", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/130_Surrounded_Regions.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
