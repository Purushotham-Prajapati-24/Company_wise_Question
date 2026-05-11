import json
import os

def generate_json():
    problem_id = 79
    title = "Word Search"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>79. Word Search</h3>
<p>Given an <code>m x n</code> grid of characters <code>board</code> and a string <code>word</code>, return <code>true</code> if <code>word</code> exists in the grid.</p>

<p>The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 6</code></li>
	<li><code>1 &lt;= word.length &lt;= 15</code></li>
	<li><code>board</code> and <code>word</code> consist of only lowercase and uppercase English letters.</li>
</ul>"""

    input_format = "Line 1: m n (rows and columns). Next m lines: n space-separated characters. Last line: the word to search."
    output_format = "A boolean string 'True' or 'False'."
    
    constraints = [
        "1 <= m, n <= 6",
        "1 <= word.length <= 15",
        "All characters are English letters."
    ]
    
    explanation = """To check if a word exists in a character grid:
1. **Backtracking (DFS)**:
   - Iterate through every cell in the grid.
   - If the first character of the word matches the cell, start a DFS from that cell.
   - In the recursive `dfs(r, c, index)` function:
     - Base Case: If `index == len(word)`, return `True` (all characters matched).
     - Boundary/Match Check: If `r, c` are out of bounds or `board[r][c] != word[index]`, return `False`.
     - Marking: Temporarily mark the current cell as visited (e.g., using a non-letter character like `#`) to avoid reusing it in the same word path.
     - Recursion: Check all 4 adjacent neighbors (up, down, left, right) for the next character: `dfs(r+1, c, index+1) or ...`.
     - Backtrack: Restore the original character in the cell so it can be used in other potential paths.
2. **Complexity**:
   - Time Complexity: O(M * N * 3^L), where M*N is the grid size and L is the word length. Each step has 3 directions to explore (excluding the one we came from).
   - Space Complexity: O(L) for the recursion stack."""
    
    answer = """def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        
        temp = board[r][c]
        board[r][c] = '#'  # Mark as visited
        
        # Explore neighbors
        res = (backtrack(r + 1, c, i + 1) or 
               backtrack(r - 1, c, i + 1) or 
               backtrack(r, c + 1, i + 1) or 
               backtrack(r, c - 1, i + 1))
        
        board[r][c] = temp  # Backtrack
        return res

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False"""

    boilerplate = {
        "python": "import sys\n\ndef exist(board, word):\n    # User logic\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if input_data:\n        m, n = int(input_data[0]), int(input_data[1])\n        board = []\n        idx = 2\n        for _ in range(m):\n            board.append(input_data[idx:idx+n])\n            idx += n\n        word = input_data[idx]\n        print(exist(board, word))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nbool exist(vector<vector<char>>& board, string word) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int m, n;\n    if (!(cin >> m >> n)) return 0;\n    vector<vector<char>> board(m, vector<char>(n));\n    for(int i=0; i<m; ++i)\n        for(int j=0; j<n; ++j)\n            cin >> board[i][j];\n    string word;\n    cin >> word;\n    cout << (exist(board, word) ? \"True\" : \"False\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean exist(char[][] board, String word) {\n        // User logic\n        return false;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int m = sc.nextInt();\n        int n = sc.nextInt();\n        char[][] board = new char[m][n];\n        for(int i=0; i<m; i++)\n            for(int j=0; j<n; j++)\n                board[i][j] = sc.next().charAt(0);\n        String word = sc.next();\n        System.out.println(exist(board, word) ? \"True\" : \"False\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction exist(board, word) {\n    // User logic\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (input.length > 2) {\n    const m = parseInt(input[0]);\n    const n = parseInt(input[1]);\n    const board = [];\n    let idx = 2;\n    for(let i=0; i<m; i++) {\n        board.push(input.slice(idx, idx + n));\n        idx += n;\n    }\n    const word = input[idx];\n    console.log(exist(board, word));\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <stdlib.h>\n\nbool exist(char** board, int boardSize, int* boardColSize, char* word) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        char** board = (char**)malloc(m * sizeof(char*));\n        int colSize = n;\n        char cell[3];\n        for (int i = 0; i < m; i++) {\n            board[i] = (char*)malloc((n + 1) * sizeof(char));\n            for (int j = 0; j < n; j++) {\n                scanf(\"%1s\", cell);\n                board[i][j] = cell[0];\n            }\n            board[i][n] = '\\0';\n        }\n        char word[20];\n        scanf(\"%19s\", word);\n        printf(\"%s\\n\", exist(board, m, &colSize, word) ? \"True\" : \"False\");\n        for (int i = 0; i < m; i++) free(board[i]);\n        free(board);\n    }\n    return 0;\n}"
    }

    def _solve(board, word):
        rows, cols = len(board), len(board[0])
        def backtrack(r, c, i):
            if i == len(word): return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]: return False
            temp = board[r][c]
            board[r][c] = '#'
            res = (backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or 
                   backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1))
            board[r][c] = temp
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0): return True
        return False

    def format_input(board, word):
        m = len(board)
        n = len(board[0])
        lines = [f"{m} {n}"]
        for row in board:
            lines.append(" ".join(row))
        lines.append(word)
        return "\n".join(lines)

    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    test_cases = [
        {"input": format_input(board1, "ABCCED"), "expected_output": str(_solve([r[:] for r in board1], "ABCCED")), "is_sample": True},
        {"input": format_input(board1, "SEE"), "expected_output": str(_solve([r[:] for r in board1], "SEE")), "is_sample": True},
        {"input": format_input(board1, "ABCB"), "expected_output": str(_solve([r[:] for r in board1], "ABCB")), "is_sample": False},
        {"input": format_input([["A"]], "A"), "expected_output": str(_solve([["A"]], "A")), "is_sample": False},
        {"input": format_input([["A"]], "B"), "expected_output": str(_solve([["A"]], "B")), "is_sample": False},
        {"input": format_input([["A","B"],["C","D"]], "ACDB"), "expected_output": str(_solve([["A","B"],["C","D"]], "ACDB")), "is_sample": False},
        {"input": format_input([["A","B"],["C","D"]], "ABCD"), "expected_output": str(_solve([["A","B"],["C","D"]], "ABCD")), "is_sample": False},
        # Stress cases
        {"input": format_input([["A"]*6 for _ in range(6)], "A"*15), "expected_output": str(_solve([["A"]*6 for _ in range(6)], "A"*15)), "is_sample": False},
        {"input": format_input([["A"]*6 for _ in range(6)], "A"*14 + "B"), "expected_output": str(_solve([["A"]*6 for _ in range(6)], "A"*14 + "B")), "is_sample": False},
        {"input": format_input([["A","B"]*3 for _ in range(6)], "ABABABABABABABA"), "expected_output": str(_solve([["A","B"]*3 for _ in range(6)], "ABABABABABABABA")), "is_sample": False}
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
        "topics": ["Array", "Backtracking", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/79_Word_Search.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
