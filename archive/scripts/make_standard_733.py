import json
import os

def generate_json():
    problem_id = 733
    title = "Flood Fill"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>733. Flood Fill</h3>
<p>An image is represented by an <code>m x n</code> integer grid <code>image</code> where <code>image[i][j]</code> represents the pixel value of the image.</p>
<p>You are also given three integers <code>sr</code>, <code>sc</code>, and <code>color</code>. You should perform a <b>flood fill</b> on the image starting from the pixel <code>image[sr][sc]</code>.</p>
<p>To perform a <b>flood fill</b>, consider the starting pixel, plus any pixels connected <b>4-directionally</b> to the starting pixel of the same color as the starting pixel, plus any pixels connected <b>4-directionally</b> to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with <code>color</code>.</p>
<p>Return <i>the modified image after performing the flood fill</i>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/flood1-grid.jpg" style="width: 613px; height: 253px;" />
<pre><strong>Input:</strong> image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
<strong>Output:</strong> [[2,2,2],[2,2,0],[2,0,1]]
<strong>Explanation:</strong> From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by its color (i.e., the color 1) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
<strong>Output:</strong> [[0,0,0],[0,0,0]]
<strong>Explanation:</strong> The starting pixel is already colored 0, so no changes are made to the image.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= image[i][j], color &lt; 2<sup>16</sup></code></li>
	<li><code>0 &lt;= sr &lt; m</code></li>
	<li><code>0 &lt;= sc &lt; n</code></li>
</ul>
"""

    input_format = "Four lines path: 1. image (grid), 2. sr, 3. sc, 4. color."
    output_format = "A JSON grid (modified image)."
    
    constraints = [
        "1 <= m, n <= 50",
        "0 <= color < 65536",
        "Handle case where new color is same as old color."
    ]
    
    explanation = """To perform Flood Fill:
1. **Identify Starting Color**: `original_color = image[sr][sc]`.
2. **Handle Identity Case**: If `original_color == newColor`, return the image immediately to avoid infinite recursion.
3. **DFS/BFS Traversal**:
   - Start from `(sr, sc)`.
   - For every 4-directional neighbor `(r, c)`:
     - If it is within bounds AND its color is `original_color`:
       - Change its color to `newColor`.
       - Recursively visit its neighbors.
4. **Complexity**:
   - Time: O(M * N) as we visit each pixel at most once.
   - Space: O(M * N) for the recursion stack or queue.

Complexity:
- Time: O(M * N).
- Space: O(M * N).
"""
    
    answer = """def floodFill(image, sr, sc, color):
    R, C = len(image), len(image[0])
    old_color = image[sr][sc]
    if old_color == color: return image
    def dfs(r, c):
        if image[r][c] == old_color:
            image[r][c] = color
            if r >= 1: dfs(r-1, c)
            if r + 1 < R: dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c + 1 < C: dfs(r, c+1)
    dfs(sr, sc)
    return image"""

    boilerplate = {
        "python": "import sys\\nimport json\\n\\ndef floodFill(image, sr, sc, color):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    input_data = json.loads(sys.stdin.read().strip())\\n    print(json.dumps(floodFill(input_data['image'], input_data['sr'], input_data['sc'], input_data['color'])))",
        "cpp": "#include <iostream>\\n#include <vector>\\nusing namespace std;\\n\\nvector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) { return {}; }",
        "java": "class Solution { public int[][] floodFill(int[][] image, int sr, int sc, int color) { } }",
        "javascript": "var floodFill = function(image, sr, sc, color) { };",
        "c": "int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) { }"
    }

    test_cases = [
        {"input": '{"image": [[1,1,1],[1,1,0],[1,0,1]], "sr": 1, "sc": 1, "color": 2}', "expected_output": "[[2,2,2],[2,2,0],[2,0,1]]", "is_sample": True},
        {"input": '{"image": [[0,0,0],[0,0,0]], "sr": 0, "sc": 0, "color": 0}', "expected_output": "[[0,0,0],[0,0,0]]", "is_sample": True},
        {"input": '{"image": [[0,0,0],[0,1,1]], "sr": 1, "sc": 1, "color": 1}', "expected_output": "[[0,0,0],[0,1,1]]", "is_sample": False},
        {"input": '{"image": [[1,1,1],[1,1,1],[1,1,1]], "sr": 1, "sc": 1, "color": 5}', "expected_output": "[[5,5,5],[5,5,5],[5,5,5]]", "is_sample": False},
        {"input": '{"image": [[1,0,1],[0,1,0],[1,0,1]], "sr": 1, "sc": 1, "color": 2}', "expected_output": "[[1,0,1],[0,2,0],[1,0,1]]", "is_sample": False},
        {"input": '{"image": [[1]], "sr": 0, "sc": 0, "color": 2}', "expected_output": "[[2]]", "is_sample": False},
        {"input": '{"image": [[0,1,5],[3,1,7],[1,1,1]], "sr": 1, "sc": 1, "color": 0}', "expected_output": "[[0,0,5],[3,0,7],[0,0,0]]", "is_sample": False},
        {"input": '{"image": [[1,1,1],[0,0,0],[1,1,1]], "sr": 0, "sc": 0, "color": 2}', "expected_output": "[[2,2,2],[0,0,0],[1,1,1]]", "is_sample": False},
        # Stress cases
        {"input": json.dumps({"image": [[1]*50 for _ in range(50)], "sr": 25, "sc": 25, "color": 2}), "expected_output": "[[2]*50 for _ in range(50)]", "is_sample": False},
        {"input": json.dumps({"image": [[i*j for j in range(50)] for i in range(50)], "sr": 0, "sc": 0, "color": 99}), "expected_output": "Only first pixel changed usually or specific range", "is_sample": False}
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
        "topics": ["Array", "DFS", "BFS", "Matrix"],
        "companyIndex": 0
    }

    output_path = "601-800/733_Flood_Fill.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
