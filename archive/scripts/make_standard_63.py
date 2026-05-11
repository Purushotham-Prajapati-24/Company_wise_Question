import json
import os

def generate_json():
    problem_id = 63
    title = "Unique Paths II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>63. Unique Paths II</h3>
<p>You are given an <code>m x n</code> integer array <code>grid</code>. There is a robot initially located at the <b>top-left corner</b> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <b>bottom-right corner</b> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>An obstacle and space are marked as <code>1</code> or <code>0</code> respectively in <code>grid</code>. A path that the robot takes cannot include <strong>any</strong> square that is an obstacle.</p>

<p>Return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The test cases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" style="width: 162px; height: 162px;" />
<pre>
<strong>Input:</strong> obstacleGrid = [[0,1],[0,0]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == obstacleGrid.length</code></li>
	<li><code>n == obstacleGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>obstacleGrid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "Two integers m and n, followed by m lines each containing n space-separated integers (0 or 1)."
    output_format = "An integer representing the number of unique paths."
    
    constraints = [
        "1 <= m, n <= 100",
        "obstacleGrid[i][j] is either 0 or 1.",
        "The answer will be less than or equal to 2 * 10^9."
    ]
    
    explanation = """To find the number of unique paths in a grid with obstacles:
1. **Dynamic Programming Approach**:
   - Let `dp[i][j]` be the number of unique paths to reach cell `(i, j)`.
   - If `obstacleGrid[i][j] == 1`, then `dp[i][j] = 0` (cannot reach this cell).
   - If `obstacleGrid[i][j] == 0`, then:
     - The cell can be reached from above `(i-1, j)` or from the left `(i, j-1)`.
     - `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (handle boundaries by treating paths from outside as 0).
2. **Base Case**:
   - `dp[0][0] = 1` if `obstacleGrid[0][0] == 0`, otherwise `0`.
3. **Space Optimization**:
   - We only need the previous row (or column) to compute the current one.
   - We can reduce the space complexity to O(n) using a single-dimensional DP array.
4. **Complexity**:
   - Time Complexity: O(m * n).
   - Space Complexity: O(n)."""
    
    answer = """def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
        return 0
        
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    
    # Use 1D DP to optimize space
    dp = [0] * cols
    dp[0] = 1
    
    for r in range(rows):
        for c in range(cols):
            if obstacleGrid[r][c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c-1]
                
    return dp[cols-1]"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef solve(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        m = int(data[0])\n        n = int(data[1])\n        grid = []\n        for i in range(m):\n            grid.append([int(x) for x in data[2 + i*n : 2 + (i+1)*n]])\n        print(solve(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (cin >> m >> n) {\n        vector<vector<int>> grid(m, vector<int>(n));\n        for(int i=0; i<m; ++i) \n            for(int j=0; j<n; ++j) cin >> grid[i][j];\n        cout << uniquePathsWithObstacles(grid) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int uniquePathsWithObstacles(int[][] obstacleGrid) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int m = sc.nextInt();\n            int n = sc.nextInt();\n            int[][] grid = new int[m][n];\n            for(int i=0; i<m; i++) for(int j=0; j<n; j++) grid[i][j] = sc.nextInt();\n            System.out.println(uniquePathsWithObstacles(grid));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction solve(grid) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nif (input.length >= 2) {\n    const m = input[0], n = input[1];\n    const grid = [];\n    for(let i=0; i<m; i++) grid.push(input.slice(2 + i*n, 2 + (i+1)*n));\n    console.log(solve(grid));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) != 2) return 0;\n    int** grid = (int**)malloc(m * sizeof(int*));\n    int* cols = (int*)malloc(m * sizeof(int));\n    for (int i = 0; i < m; i++) {\n        grid[i] = (int*)malloc(n * sizeof(int));\n        cols[i] = n;\n        for (int j = 0; j < n; j++) scanf(\"%d\", &grid[i][j]);\n    }\n    printf(\"%d\\n\", uniquePathsWithObstacles(grid, m, cols));\n    for (int i = 0; i < m; i++) free(grid[i]);\n    free(grid);\n    free(cols);\n    return 0;\n}"
    }

    def _solve(grid):
        if not grid or grid[0][0] == 1: return 0
        m, n = len(grid), len(grid[0])
        dp = [0]*n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: dp[j] = 0
                elif j > 0: dp[j] += dp[j-1]
        return dp[-1]

    def _fmt(grid):
        m, n = len(grid), len(grid[0])
        s = f"{m} {n}"
        for row in grid:
            s += " " + " ".join(map(str, row))
        return s

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": _fmt([[0,0,0],[0,1,0],[0,0,0]]), "expected_output": "2", "is_sample": True},
        {"input": _fmt([[0,1],[0,0]]), "expected_output": "1", "is_sample": True},
        # Middle five: Diverse cases
        {"input": _fmt([[1,0]]), "expected_output": "0", "is_sample": False},
        {"input": _fmt([[0,0]]), "expected_output": "1", "is_sample": False},
        {"input": _fmt([[0],[1]]), "expected_output": "0", "is_sample": False},
        {"input": _fmt([[0,0],[0,0]]), "expected_output": "2", "is_sample": False},
        {"input": _fmt([[0,0,0,0],[0,0,0,0],[0,0,0,0]]), "expected_output": "10", "is_sample": False},
        # Last three: Stress tests
        {"input": _fmt([[0]*100 for _ in range(2)]), "expected_output": "100", "is_sample": False},
        {"input": _fmt([[0]*5 for _ in range(5)]), "expected_output": str(_solve([[0]*5 for _ in range(5)])), "is_sample": False},
        {"input": _fmt([[0 if (i+j)%2==0 else 1 for j in range(10)] for i in range(10)]), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/63_Unique_Paths_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
