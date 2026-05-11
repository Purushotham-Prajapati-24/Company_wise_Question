import json
import os

def generate_json():
    problem_id = 695
    title = "Max Area of Island"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>695. Max Area of Island</h3>
<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An <b>island</b> is a group of <code>1</code>'s (representing land) connected <b>4-directionally</b> (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>The <b>area</b> of an island is the number of cells with a value <code>1</code> in the island.</p>

<p>Return <em>the maximum <b>area</b> of an island in </em><code>grid</code>. If there is no island, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The answer is not 11, because the island must be connected 4-directionally.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> grid = [[0,0,0,0,0,0,0,0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "Three parts: 1) integer m 2) integer n 3) m lines of n space-separated integers (the grid)."
    output_format = "A single integer representing the maximum area."
    
    constraints = [
        "1 <= m, n <= 50",
        "Grid consists of 0s and 1s.",
        "O(M \u00d7 N) time complexity.",
        "O(M \u00d7 N) extra space (recursion/queue)."
    ]
    
    explanation = """To find the maximum area of an island:
1. **The Principle (Graph Traversal)**:
   - This is a classic grid-based connected component problem.
   - We traverse each cell of the grid. If we encounter a `1` (land), we initiate a traversal (DFS or BFS) to visit all reachable `1`s.
2. **Implementation (DFS)**:
   - For a starting land cell `(r, c)`:
     - Mark it as visited (e.g., set `grid[r][c] = 0` to avoid revisit).
     - Recursively call DFS for neighbors in 4 directions.
     - Sum of the current cell (1) + sum of DFS on neighbors = Area of the island.
3. **Calculation**:
   - Keep track of the `max_area` encountered during the grid iteration.
4. **Complexity**:
   - Time Complexity: O(M \u00d7 N) because each cell is visited once.
   - Space Complexity: O(M \u00d7 N) for the recursion stack in the worst case (e.g., a snake-like island)."""
    
    answer = """def maxAreaOfIsland(grid: list[list[int]]) -> int:
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    max_area = 0
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        grid[r][c] = 0 # Mark as visited
        area = 1
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area"""

    boilerplate = {
        "python": "import sys\n\ndef maxAreaOfIsland(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if lines:\n        m = int(lines[0].strip())\n        n = int(lines[1].strip())\n        grid = [list(map(int, line.split())) for line in lines[2:] if line.strip()]\n        print(maxAreaOfIsland(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint maxAreaOfIsland(vector<vector<int>>& grid) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int maxAreaOfIsland(int[][] grid) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function maxAreaOfIsland(grid) {\n    // User logic\n}",
        "c": "int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "8\\n13\\n0 0 1 0 0 0 0 1 0 0 0 0 0\\n0 0 0 0 0 0 0 1 1 1 0 0 0\\n0 1 1 0 1 0 0 0 0 0 0 0 0\\n0 1 0 0 1 1 0 0 1 0 1 0 0\\n0 1 0 0 1 1 0 0 1 1 1 0 0\\n0 0 0 0 0 0 0 0 0 0 1 0 0\\n0 0 0 0 0 0 0 1 1 1 0 0 0\\n0 0 0 0 0 0 0 1 1 0 0 0 0", "expected_output": "6", "is_sample": True},
        {"input": "1\\n8\\n0 0 0 0 0 0 0 0", "expected_output": "0", "is_sample": True},
        {"input": "1\\n1\\n1", "expected_output": "1", "is_sample": False},
        {"input": "1\\n1\\n0", "expected_output": "0", "is_sample": False},
        {"input": "2\\n2\\n1 1\\n1 1", "expected_output": "4", "is_sample": False},
        {"input": "3\\n3\\n1 0 1\\n0 1 0\\n1 0 1", "expected_output": "1", "is_sample": False},
        {"input": "3\\n3\\n1 1 1\\n1 0 1\\n1 1 1", "expected_output": "8", "is_sample": False},
        {"input": "5\\n5\\n1 1 0 0 0\\n1 1 0 0 0\\n0 0 1 1 1\\n0 0 1 1 1\\n0 0 0 0 0", "expected_output": "6", "is_sample": False},
        # Stress cases
        {"input": "50\\n1\\n" + "\\n".join(["1"] * 50), "expected_output": "50", "is_sample": False},
        {"input": "50\\n50\\n" + "\\n".join([" ".join(["1"] * 50)] * 50), "expected_output": "2500", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "DFS", "BFS", "Union Find", "Matrix"],
        "companyIndex": 0
    }

    output_path = "601-800/695_Max_Area_of_Island.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
