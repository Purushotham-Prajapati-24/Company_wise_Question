import json
import os

def generate_json():
    problem_id = 200
    title = "Number of Islands"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>200. Number of Islands</h3>
<p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>'1'</code>s (land) and <code>'0'</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>"""

    input_format = "Line 1: m (rows) and n (cols). Subsequent lines: the m x n grid characters."
    output_format = "An integer representing the number of islands."
    
    constraints = [
        "1 <= m, n <= 300",
        "Linear time O(m*n) expected.",
        "Constant extra space (ignoring recursion/queue) is ideal."
    ]
    
    explanation = """To count the number of islands in a 2D grid:
1. **Iterate Through the Grid**:
   - Traverse each cell `(r, c)` in the grid.
2. **Logic**:
   - If a cell contains '1', it marks the start of a potential island.
   - Increment the island count.
   - Perform a traversal (DFS or BFS) starting from `(r, c)` to mark all connected land cells ('1's) as visited (e.g., by changing them to '0').
3. **Traversal Implementation**:
   - Use a helper function (DFS or iterative BFS with a queue) to explore all 4 adjacent cells (up, down, left, right).
   - If an adjacent cell is within bounds and is '1', recursively visit it.
4. **Complexity**:
   - Time Complexity: O(M * N) since each cell is visited at most once.
   - Space Complexity: O(M * N) in the worst case for the recursion stack or BFS queue (e.g., a grid full of '1's)."""
    
    answer = """import collections

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def bfs(r, c):
        q = collections.deque([(r, c)])
        grid[r][c] = '0' # Mark as visited
        while q:
            row, col = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)
                
    return count"""

    boilerplate = {
        "python": "import sys\n\ndef numIslands(grid):\n    # User logic here (modify grid or use visited set)\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        first = lines[0].split()\n        if not first: sys.exit(0)\n        m, n = map(int, first)\n        grid = [list(lines[i+1].strip()) for i in range(m)]\n        print(numIslands(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint numIslands(vector<vector<char>>& grid) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (cin >> m >> n) {\n        vector<vector<char>> grid(m, vector<char>(n));\n        for (int i = 0; i < m; i++) {\n            string s;\n            cin >> s;\n            for (int j = 0; j < n; j++) {\n                grid[i][j] = s[j];\n            }\n        }\n        cout << numIslands(grid) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int numIslands(char[][] grid) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int m = sc.nextInt();\n            int n = sc.nextInt();\n            char[][] grid = new char[m][n];\n            for (int i = 0; i < m; i++) {\n                String s = sc.next();\n                grid[i] = s.toCharArray();\n            }\n            System.out.println(new Solution().numIslands(grid));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction numIslands(grid) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\r?\\n/);\nif (input.length > 0) {\n    const [m, n] = input[0].trim().split(/\\\\s+/).map(Number);\n    const grid = [];\n    for (let i = 0; i < m; i++) {\n        grid.push(input[i+1].trim().split(''));\n    }\n    console.log(numIslands(grid));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint numIslands(char** grid, int gridSize, int* gridColSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        char** grid = (char**)malloc(m * sizeof(char*));\n        int* colSizes = (int*)malloc(m * sizeof(int));\n        for (int i = 0; i < m; i++) {\n            grid[i] = (char*)malloc((n + 1) * sizeof(char));\n            scanf(\"%s\", grid[i]);\n            colSizes[i] = n;\n        }\n        printf(\"%d\\n\", numIslands(grid, m, colSizes));\n        for (int i = 0; i < m; i++) free(grid[i]);\n        free(grid);\n        free(colSizes);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "4 5\\n11110\\n11010\\n11000\\n00000", "expected_output": "1", "is_sample": True},
        {"input": "4 5\\n11000\\n11000\\n00100\\n00011", "expected_output": "3", "is_sample": True},
        {"input": "1 1\\n0", "expected_output": "0", "is_sample": False},
        {"input": "1 1\\n1", "expected_output": "1", "is_sample": False},
        {"input": "3 3\\n101\\n010\\n101", "expected_output": "5", "is_sample": False},
        {"input": "2 2\\n11\\n11", "expected_output": "1", "is_sample": False},
        {"input": "3 4\\n1111\\n0000\\n1111", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": "300 300\\n" + "\\n".join(["1"*300]*300), "expected_output": "1", "is_sample": False},
        {"input": "300 300\\n" + "\\n".join(["0"*300]*300), "expected_output": "0", "is_sample": False},
        {"input": "2 300\\n" + "10"*150 + "\\n" + "01"*150, "expected_output": "300", "is_sample": False}
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
        "topics": ["Array", "Depth-First Search", "Breadth-First Search", "Union Find", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/200_Number_of_Islands.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
