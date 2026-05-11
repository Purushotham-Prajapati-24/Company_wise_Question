import json
import os

def generate_json():
    problem_id = 576
    title = "Out of Boundary Paths"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>576. Out of Boundary Paths</h3>
<p>There is an <code>m x n</code> grid with a ball. The ball is initially at the position <code>[startRow, startColumn]</code>. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid boundary). You can apply <strong>at most</strong> <code>maxMove</code> moves to the ball.</p>

<p>Given the five integers <code>m</code>, <code>n</code>, <code>maxMove</code>, <code>startRow</code>, <code>startColumn</code>, return <em>the number of paths to move the ball out of the grid boundary</em>. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png" style="width: 500px; height: 296px;" />
<pre>
<strong>Input:</strong> m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 293px;" />
<pre>
<strong>Input:</strong> m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= maxMove &lt;= 50</code></li>
	<li><code>0 &lt;= startRow &lt; m</code></li>
	<li><code>0 &lt;= startColumn &lt; n</code></li>
</ul>
"""

    input_format = "A single line containing space-separated integers for m, n, maxMove, startRow, startColumn."
    output_format = "A single integer representing the number of paths modulo 10^9 + 7."
    
    constraints = [
        "1 <= m, n <= 50",
        "0 <= maxMove <= 50",
        "0 <= startRow < m",
        "0 <= startColumn < n"
    ]
    
    explanation = """To find the number of paths:
1. Use dynamic programming with memoization or iterative approach. 
2. Let `dp[k][i][j]` be the number of ways to reach boundary from position `(i, j)` with `k` moves left.
3. Recursive step: `dp[k][i][j] = (dp[k-1][i-1][j] + dp[k-1][i+1][j] + dp[k-1][i][j-1] + dp[k-1][i][j+1]) % mod`. 
4. Base Case: If `(i, j)` is out of grid bounds, return 1. If `k == 0`, return 0."""
    
    answer = """class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        self.memo = {}
        self.mod = 10**9 + 7
        return self.dfs(m, n, maxMove, startRow, startColumn)
    
    def dfs(self, m, n, k, i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        if k == 0:
            return 0
        if (k, i, j) in self.memo:
            return self.memo[(k, i, j)]
        
        res = 0
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            res = (res + self.dfs(m, n, k - 1, i + di, j + dj)) % self.mod
        
        self.memo[(k, i, j)] = res
        return res"""

    boilerplate = {
        "python": "import sys\\n\\nclass Solution:\\n    def findPaths(self, m, n, maxMove, startRow, startColumn):\\n        # User logic here\\n        pass\\n\\nif __name__ == '__main__':\\n    # Custom input handler\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\n\\nusing namespace std;\\n\\nclass Solution { public: int findPaths(int m, int n, int maxMove, int startRow, int startColumn) { return 0; } };",
        "java": "class Solution { public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int findPaths(int m, int n, int maxMove, int startRow, int startColumn) { }"
    }

    test_cases = [
        {"input": "2 2 2 0 0", "expected_output": "6", "is_sample": True},
        {"input": "1 3 3 0 1", "expected_output": "12", "is_sample": True},
        {"input": "1 1 1 0 0", "expected_output": "4", "is_sample": False},
        {"input": "1 1 0 0 0", "expected_output": "0", "is_sample": False},
        {"input": "50 50 50 0 0", "expected_output": "110154788", "is_sample": False},
        {"input": "2 2 1 0 0", "expected_output": "2", "is_sample": False},
        {"input": "1 2 1 0 0", "expected_output": "3", "is_sample": False},
        {"input": "3 1 3 0 0", "expected_output": "11", "is_sample": False},
        {"input": "8 7 20 1 1", "expected_output": "1029841", "is_sample": False},
        {"input": "10 10 0 5 5", "expected_output": "0", "is_sample": False}
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
        "topics": ["Dynamic Programming", "Grid", "Memoization"],
        "companyIndex": 0
    }

    output_path = "401-600/576_Out_of_Boundary_Paths.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
