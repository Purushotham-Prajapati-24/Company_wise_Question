import json
import os

def generate_json():
    problem_id = 85
    title = "Maximal Rectangle"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>85. Maximal Rectangle</h3>
<p>Given a <code>rows x cols</code>&nbsp;binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, find the largest rectangle containing only <code>1</code>'s and return <em>its area</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" />
<pre>
<strong>Input:</strong> matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The maximal rectangle is shown in the above picture.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> matrix = [["0"]]
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> matrix = [["1"]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix[i].length</code></li>
	<li><code>1 &lt;= row, cols &lt;= 200</code></li>
	<li><code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>"""

    input_format = "Line 1: m n (rows and columns). Next m lines: n space-separated characters ('0' or '1')."
    output_format = "An integer representing the area of the largest rectangle of 1s."
    
    constraints = [
        "1 <= rows, cols <= 200",
        "matrix[i][j] is '0' or '1'."
    ]
    
    explanation = """To find the maximal rectangle of 1s in a binary matrix:
1. **Histogram Reduction**:
   - Treat each row as the base of a histogram.
   - Maintain a 'heights' array where `heights[j]` stores the number of consecutive 1s ending at the current row in column `j`.
   - As we iterate through each row:
     - If `matrix[i][j] == '1'`, increment `heights[j]`.
     - If `matrix[i][j] == '0'`, reset `heights[j]` to 0.
     - Apply the **Largest Rectangle in Histogram** (O(N) algorithm) on the current row's `heights` array.
2. **Complexity**:
   - Time Complexity: O(M * N) where M is the number of rows and N is the number of columns.
   - Space Complexity: O(N) to store the heights and the stack for the histogram calculation."""
    
    answer = """def maximalRectangle(matrix):
    if not matrix or not matrix[0]: return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * (cols + 1)
    max_area = 0
    
    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        
        # Largest Rectangle in Histogram logic
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
            
    return max_area"""

    boilerplate = {
        "python": "import sys\n\ndef maximalRectangle(matrix):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if input_data:\n        m, n = int(input_data[0]), int(input_data[1])\n        matrix = []\n        idx = 2\n        for _ in range(m):\n            matrix.append(input_data[idx:idx+n])\n            idx += n\n        print(maximalRectangle(matrix))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <algorithm>\n\nusing namespace std;\n\nint maximalRectangle(vector<vector<char>>& matrix) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (!(cin >> m >> n)) return 0;\n    vector<vector<char>> matrix(m, vector<char>(n));\n    for(int i=0; i<m; ++i)\n        for(int j=0; j<n; ++j)\n            cin >> matrix[i][j];\n    cout << maximalRectangle(matrix) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int maximalRectangle(char[][] matrix) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int m = sc.nextInt();\n        int n = sc.nextInt();\n        char[][] matrix = new char[m][n];\n        for(int i=0; i<m; i++)\n            for(int j=0; j<n; j++)\n                matrix[i][j] = sc.next().charAt(0);\n        System.out.println(maximalRectangle(matrix));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maximalRectangle(matrix) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (input.length > 2) {\n    const m = parseInt(input[0]);\n    const n = parseInt(input[1]);\n    const matrix = [];\n    let idx = 2;\n    for(let i=0; i<m; i++) {\n        matrix.push(input.slice(idx, idx + n));\n        idx += n;\n    }\n    console.log(maximalRectangle(matrix));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        char** matrix = (char**)malloc(m * sizeof(char*));\n        int colSize = n;\n        char cell[3];\n        for (int i = 0; i < m; i++) {\n            matrix[i] = (char*)malloc((n + 1) * sizeof(char));\n            for (int j = 0; j < n; j++) {\n                scanf(\"%1s\", cell);\n                matrix[i][j] = cell[0];\n            }\n            matrix[i][n] = '\\0';\n        }\n        printf(\"%d\\n\", maximalRectangle(matrix, m, &colSize));\n        for (int i = 0; i < m; i++) free(matrix[i]);\n        free(matrix);\n    }\n    return 0;\n}"
    }

    def _solve(matrix):
        if not matrix or not matrix[0]: return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area

    def format_matrix(matrix):
        m, n = len(matrix), len(matrix[0])
        res = [f"{m} {n}"]
        for row in matrix:
            res.append(" ".join(row))
        return "\n".join(res)

    mat1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    test_cases = [
        {"input": format_matrix(mat1), "expected_output": str(_solve(mat1)), "is_sample": True},
        {"input": format_matrix([["0"]]), "expected_output": "0", "is_sample": True},
        {"input": format_matrix([["1"]]), "expected_output": "1", "is_sample": True},
        {"input": format_matrix([["0","0"]]), "expected_output": "0", "is_sample": False},
        {"input": format_matrix([["1","1"]]), "expected_output": "2", "is_sample": False},
        {"input": format_matrix([["1","0"],["1","0"]]), "expected_output": "2", "is_sample": False},
        {"input": format_matrix([["1","1"],["1","1"]]), "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": format_matrix([["1"]*20 for _ in range(20)]), "expected_output": "400", "is_sample": False},
        {"input": format_matrix([["0"]*20 for _ in range(20)]), "expected_output": "0", "is_sample": False},
        {"input": format_matrix([["1" if (i+j)%2==0 else "0" for i in range(20)] for j in range(20)]), "expected_output": "1", "is_sample": False}
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
        "topics": ["Array", "Stack", "Dynamic Programming", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/85_Maximal_Rectangle.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
