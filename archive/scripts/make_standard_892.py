import json
import os

def generate_json():
    problem_id = 892
    title = "Surface Area of 3D Shapes"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>892. Surface Area of 3D Shapes</h3>
<p>You are given an <code>n x n</code> <code>grid</code> where you have placed some <code>1 x 1 x 1</code> cubes. Each value <code>v = grid[i][j]</code> represents a tower of <code>v</code> cubes placed on top of cell <code>(i, j)</code>.</p>

<p>After placing these cubes, you have a single 3D shape. We are looking for the total surface area of this shape.</p>

<p>Note: The total surface area is the sum of the areas of all the outer faces of the 3D shape.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid1.jpg" style="width: 130px; height: 130px;" />
<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> 34
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg" style="width: 130px; height: 130px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> 32
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/08/tmp-grid3.jpg" style="width: 130px; height: 130px;" />
<pre>
<strong>Input:</strong> grid = [[2,2,2],[2,1,2],[2,2,2]]
<strong>Output:</strong> 46
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>
"""

    input_format = "A 2D integer array grid."
    output_format = "The surface area as an integer."
    
    constraints = [
        "1 <= n <= 50",
        "0 <= grid[i][j] <= 50"
    ]
    
    explanation = """To calculate the total surface area of the 3D shape:
1. **Understand Each Stack**:
   - A stack of `v` cubes at position `(i, j)` has:
     - 1 top face and 1 bottom face (if `v > 0`).
     - 4 * `v` side faces.
   - Total base area contribution = `2` if `v > 0`.
   - Total side area contribution = `4 * v`.
2. **Handle Adjacent Occlusion**:
   - When two stacks of cubes are adjacent, some surfaces are *blocked* (internal faces).
   - If position `(i, j)` has height `v1` and its neighbor has height `v2`, they touch along a surface with area `min(v1, v2)`.
   - This blocked area must be subtracted twice (once for each stack).
3. **The Algorithm**:
   - For every cell `(i, j)`:
     - If `grid[i][j] > 0`:
       - Add `2 + 4 * grid[i][j]` to total.
       - Check neighbor to the Right `(i, j+1)` and Down `(i+1, j)`.
       - For each valid neighbor, subtract `2 * min(height_current, height_neighbor)`.

Complexity:
- Time: O(N^2) where N is the grid dimension.
- Space: O(1)."""
    
    answer = """def surfaceArea(grid: list[list[int]]) -> int:
    n = len(grid)
    res = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] > 0:
                res += 2 + 4 * grid[r][c]
                # Neighbor Up
                if r > 0: res -= 2 * min(grid[r][c], grid[r-1][c])
                # Neighbor Left
                if c > 0: res -= 2 * min(grid[r][c], grid[r][c-1])
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef surfaceArea(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    grid = json.loads(sys.stdin.read().strip())\n    print(surfaceArea(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int surfaceArea(vector<vector<int>>& grid) {\n        return 0;\n    }\n};",
        "java": "class Solution {\n    public int surfaceArea(int[][] grid) {\n        return 0;\n    }\n}",
        "javascript": "var surfaceArea = function(grid) {\n    return 0;\n};",
        "c": "int surfaceArea(int** grid, int gridSize, int* gridColSize){\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,2],[3,4]]", "expected_output": "34", "is_sample": True},
        {"input": "[[1,1,1],[1,0,1],[1,1,1]]", "expected_output": "32", "is_sample": True},
        {"input": "[[2,2,2],[2,1,2],[2,2,2]]", "expected_output": "46", "is_sample": True},
        # Diverse cases
        {"input": "[[0]]", "expected_output": "0", "is_sample": False},
        {"input": "[[1]]", "expected_output": "6", "is_sample": False},
        {"input": "[[50]]", "expected_output": "202", "is_sample": False},
        {"input": "[[1,1],[1,1]]", "expected_output": "16", "is_sample": False},
        {"input": "[[10,0],[0,10]]", "expected_output": "84", "is_sample": False},
        {"input": "[[2,3],[4,5]]", "expected_output": "54", "is_sample": False},
        # Stress cases
        {"input": "[[50]*50]*50", "expected_output": "15200", "is_sample": False}
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
        "topics": ["Array", "Math", "Matrix", "Geometry"],
        "companyIndex": 0
    }

    output_path = "801-1000/892_Surface_Area_of_3D_Shapes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
