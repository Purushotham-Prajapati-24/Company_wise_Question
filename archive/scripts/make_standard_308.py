import json
import os

def generate_json():
    problem_id = 308
    title = "Range Sum Query 2D - Mutable"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>308. Range Sum Query 2D - Mutable</h3>
<p>Given a 2D matrix <code>matrix</code>, handle multiple queries of the following types:</p>

<ol>
	<li><strong>Update</strong> the value of a cell in <code>matrix</code>.</li>
	<li>Calculate the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.</li>
</ol>

<p>Implement the <code>NumMatrix</code> class:</p>
<ul>
	<li><code>NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix <code>matrix</code>.</li>
	<li><code>void update(int row, int col, int val)</code> Updates the value of <code>matrix[row][col]</code> to be <code>val</code>.</li>
	<li><code>int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0308.Range%20Sum%20Query%202D%20-%20Mutable/images/summut-grid.jpg" style="width: 415px; height: 415px;" />
<pre><strong>Input:</strong>
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
<strong>Output:</strong>
[null, 8, null, 10]

<strong>Explanation:</strong>
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (6+3+2 + 2+0+1 + 1+0+1)
numMatrix.update(3, 2, 2);       // matrix[3][2] is now 2
numMatrix.sumRegion(2, 1, 4, 3); // return 10 (6+3+2 + 2+2+1 + 1+0+1)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
	<li><code>0 &lt;= row &lt; m</code></li>
	<li><code>0 &lt;= col &lt; n</code></li>
	<li><code>-100 &lt;= val &lt;= 100</code></li>
	<li><code>0 &lt;= row1 &lt;= row2 &lt; m</code></li>
	<li><code>0 &lt;= col1 &lt;= col2 &lt; n</code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>update</code> and <code>sumRegion</code>.</li>
</ul>"""

    input_format = "A 2D array matrix and corresponding command arguments."
    output_format = "Integer results for sumRegion, null for others."
    
    constraints = [
        "1 <= m, n <= 200",
        "At most 10,000 calls to update and sumRegion."
    ]
    
    explanation = """To handle frequent point updates and sub-rectangle sum queries in 2D:
1. **2D Binary Indexed Tree (BIT)**: This efficient structure generalizes the 1D BIT.
2. **Operations**:
   - `updateBIT(r, c, diff)`: Update the cell and all its relevant "ancestors" in the 2D BIT grid.
   - `queryBIT(r, c)`: Get the sum of the rectangle from `(0, 0)` to `(r, c)`.
   - `sumRegion(r1, c1, r2, c2)`: Use the Principle of Inclusion-Exclusion for 2D sums:
     `S(r2, c2) - S(r1-1, c2) - S(r2, c1-1) + S(r1-1, c1-1)`.
3. **Logic**:
   - For `update`, iterate up using `i += i & -i` for both row and column.
   - For `query`, iterate down using `i -= i & -i` for both row and column.
4. **Complexity Analysis**:
   - Update: O(log M * log N).
   - Query: O(log M * log N).
   - Space: O(M * N) to store the 2D BIT and current matrix values."""
    
    answer = """class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += j & (-j)
            i += i & (-i)

    def query(self, row: int, col: int) -> int:
        s = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                s += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.query(row2, col2) - self.query(row1 - 1, col2) - \
               self.query(row2, col1 - 1) + self.query(row1 - 1, col1 - 1)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass NumMatrix:\n    def __init__(self, matrix):\n        # User logic here\n        pass\n    def update(self, row, col, val):\n        pass\n    def sumRegion(self, row1, col1, row2, col2):\n        return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    commands = json.loads(lines[0].strip())\n    arguments = json.loads(lines[1].strip())\n    obj = None\n    results = []\n    for cmd, args in zip(commands, arguments):\n        if cmd == 'NumMatrix':\n            obj = NumMatrix(args[0])\n            results.append(None)\n        elif cmd == 'update':\n            obj.update(args[0], args[1], args[2])\n            results.append(None)\n        elif cmd == 'sumRegion':\n            results.append(obj.sumRegion(args[0], args[1], args[2], args[3]))\n    print(json.dumps(results))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nclass NumMatrix {\npublic:\n    NumMatrix(vector<vector<int>>& matrix) {\n        // User logic here\n    }\n    void update(int row, int col, int val) {\n        // User logic here\n    }\n    int sumRegion(int row1, int col1, int row2, int col2) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    // Command-based input\n    // User logic here\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class NumMatrix {\n    public NumMatrix(int[][] matrix) {\n        // User logic here\n    }\n    public void update(int row, int col, int val) {\n        // User logic here\n    }\n    public int sumRegion(int row1, int col1, int row2, int col2) {\n        // User logic here\n        return 0;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass NumMatrix {\n    constructor(matrix) {\n        // User logic here\n    }\n    update(row, col, val) {\n        // User logic here\n    }\n    sumRegion(row1, col1, row2, col2) {\n        // User logic here\n        return 0;\n    }\n}\n\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst commands = JSON.parse(lines[0]);\nconst args = JSON.parse(lines[1]);\nlet obj = null;\nconst results = [];\nfor (let i = 0; i < commands.length; i++) {\n    if (commands[i]==='NumMatrix') { obj = new NumMatrix(args[i][0]); results.push(null); }\n    else if (commands[i]==='update') { obj.update(args[i][0],args[i][1],args[i][2]); results.push(null); }\n    else if (commands[i]==='sumRegion') results.push(obj.sumRegion(args[i][0],args[i][1],args[i][2],args[i][3]));\n}\nconsole.log(JSON.stringify(results));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct { int** bit; int** mat; int m; int n; } NumMatrix;\n\nNumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {\n    // User logic here\n    return NULL;\n}\nvoid numMatrixUpdate(NumMatrix* obj, int row, int col, int val) {}\nint numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) { return 0; }\nvoid numMatrixFree(NumMatrix* obj) { if(obj) free(obj); }\n\nint main() {\n    // User logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["NumMatrix", "sumRegion", "update", "sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]], [2,1,4,3], [3,2,2], [2,1,4,3]]', "expected_output": "[null, 8, null, 10]", "is_sample": True},
        {"input": '["NumMatrix", "sumRegion"]\n[[[[1,2],[3,4]]], [0,0,1,1]]', "expected_output": "[null, 10]", "is_sample": False},
        {"input": '["NumMatrix", "update", "sumRegion"]\n[[[[1,1],[1,1]]], [0,0,10], [0,0,1,1]]', "expected_output": "[null, null, 13]", "is_sample": False},
        {"input": '["NumMatrix", "sumRegion"]\n[[[[1]]], [0,0,0,0]]', "expected_output": "[null, 1]", "is_sample": False},
        {"input": '["NumMatrix", "sumRegion"]\n[[[[1,0],[0,1]]], [0,0,1,1]]', "expected_output": "[null, 2]", "is_sample": False},
        {"input": '["NumMatrix", "update", "sumRegion"]\n[[[[5]]], [0,0,3], [0,0,0,0]]', "expected_output": "[null, null, 3]", "is_sample": False},
        {"input": '["NumMatrix", "sumRegion"]\n[[[[1,2,3],[4,5,6],[7,8,9]]], [0,0,2,2]]', "expected_output": "[null, 45]", "is_sample": False},
        {"input": '["NumMatrix", "sumRegion", "update", "sumRegion"]\n[[[[1,2],[3,4]]], [0,0,0,1], [0,1,10], [0,0,0,1]]', "expected_output": "[null, 3, null, 11]", "is_sample": False},
        {"input": '["NumMatrix", "sumRegion"]\n[[[[0,0],[0,0]]], [0,0,1,1]]', "expected_output": "[null, 0]", "is_sample": False},
        {"input": '["NumMatrix", "update", "update", "sumRegion"]\n[[[[1,1,1],[1,1,1],[1,1,1]]], [0,0,5], [2,2,5], [0,0,2,2]]', "expected_output": "[null, null, null, 15]", "is_sample": False}
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
        "topics": ["Array", "Binary Indexed Tree", "Segment Tree", "Matrix"],
        "companyIndex": 0
    }

    output_path = "201-400/308_Range_Sum_Query_2D_Mutable.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
