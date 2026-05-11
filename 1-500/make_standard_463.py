import json
import os

def generate_json():
    problem_id = 463
    title = "Island Perimeter"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>463. Island Perimeter</h3>
<p>You are given <code>row x col</code> <code>grid</code> representing a map where <code>grid[i][j] = 1</code> represents&nbsp;land and <code>grid[i][j] = 0</code> represents water.</p>

<p>Grid cells are connected <strong>horizontally/vertically</strong> (not diagonally). The <code>grid</code> is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn't have "lakes", i.e., the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;" />
<pre><strong>Input:</strong> grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
<strong>Output:</strong> 16
<strong>Explanation:</strong> The perimeter is the 16 yellow edges in the image above.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> grid = [[1,0]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>row == grid.length</code></li>
	<li><code>col == grid[i].length</code></li>
	<li><code>1 &lt;= row, col &lt;= 100</code></li>
	<li><code>grid[i][j]</code> is <code>0</code> or <code>1</code>.</li>
	<li>There is exactly one island in <code>grid</code>.</li>
</ul>"""

    input_format = "Line 1: A JSON 2D array `grid` where 1 represents land and 0 represents water."
    output_format = "An integer representing the perimeter of the island."
    
    constraints = [
        "1 <= row, col <= 100",
        "grid[i][j] is 0 or 1",
        "There is exactly one island."
    ]
    
    explanation = "Iterate through each cell in the grid. If a cell is land (1), add 4 to the perimeter. Then, check its neighbors (top and left). For each adjacent land cell, subtract 2 from the perimeter (as those two cells share an edge)."
    
    answer = """class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
        return perimeter"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def islandPerimeter(self, grid: list[list[int]]) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        grid = json.loads(line)\n        sol = Solution()\n        print(sol.islandPerimeter(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int islandPerimeter(vector<vector<int>>& grid) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line; if (getline(cin, line)) {\n        vector<vector<int>> grid; string r; stringstream ss(line); \n        while (getline(ss, r, ']')) {\n            size_t start = r.find('[');\n            if (start != string::npos) {\n                vector<int> row; stringstream ss2(r.substr(start + 1)); string val;\n                while (getline(ss2, val, ',')) {\n                    if (!val.empty()) row.push_back(stoi(val));\n                }\n                if (!row.empty()) grid.push_back(row);\n            }\n        }\n        Solution sol; cout << sol.islandPerimeter(grid) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int islandPerimeter(int[][] grid) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            String[] rows = line.substring(1, line.length() - 1).split(\"\\\\],\\\\s*\\\\[\");\n            List<int[]> gridList = new ArrayList<>();\n            for (String r : rows) {\n                String clean = r.replaceAll(\"[\\\\[\\\\]]\", \"\");\n                if (clean.isEmpty()) continue;\n                String[] nums = clean.split(\",\\\\s*\");\n                int[] row = new int[nums.length];\n                for (int i = 0; i < nums.length; i++) row[i] = Integer.parseInt(nums[i]);\n                gridList.add(row);\n            }\n            System.out.println(new Solution().islandPerimeter(gridList.toArray(new int[0][])));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar islandPerimeter = function(grid) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const grid = JSON.parse(input);\n    console.log(islandPerimeter(grid));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint islandPerimeter(int** grid, int gridSize, int* gridColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    printf(\"0\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]", "expected_output": "16", "is_sample": True},
        {"input": "[[1]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1,0]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1,1],[1,1]]", "expected_output": "8", "is_sample": False},
        {"input": "[[0,1,0],[1,1,1],[0,1,0]]", "expected_output": "12", "is_sample": False},
        {"input": "[[1,1,1]]", "expected_output": "8", "is_sample": False},
        {"input": "[[1],[1],[1]]", "expected_output": "8", "is_sample": False},
        {"input": "[[0,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,1]]", "expected_output": "14", "is_sample": False},
        {"input": "[[1,1,1,1],[1,0,0,1],[1,1,1,1]]", "expected_output": "22", "is_sample": False},
        {"input": json.dumps([[1 if (i+j)%2==0 else 0 for j in range(10)] for i in range(10)][:1]), "expected_output": "22", "is_sample": False} # Simple row case
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
        "topics": ["Array", "Hash Table", "Matrix", "Depth-First Search", "Breadth-First Search"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Island_Perimeter.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
