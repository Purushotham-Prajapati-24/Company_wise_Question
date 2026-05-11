import json
import os

def generate_json():
    problem_id = 73
    title = "Set Matrix Zeroes"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>73. Set Matrix Zeroes</h3>
<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>'s.</p>

<p>You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px;" />
<pre>
<strong>Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px;" />
<pre>
<strong>Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong>Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>-2<sup>31</sup> &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>A straightforward solution using <code>O(mn)</code> space is probably a bad idea.</li>
	<li>A simple improvement uses <code>O(m + n)</code> space, but still not the best solution.</li>
	<li>Could you devise a constant space solution?</li>
</ul>"""

    input_format = "Two integers 'm' and 'n' on the first line, followed by 'm' lines, each containing 'n' space-separated integers representing the matrix rows."
    output_format = "The modified matrix (row-by-row, space-separated)."
    
    constraints = [
        "1 <= m, n <= 200",
        "-2^31 <= matrix[i][j] <= 2^31 - 1",
        "Must be performed in-place."
    ]
    
    explanation = """To set matrix zeroes in-place with O(1) space:
1. **Marker Strategy**: Use the first row and the first column of the matrix to mark whether a particular row or column should be set to zero.
2. **Initial Checks**: Check if the first row and the first column originally contain any zeroes. Store this in two variables (`first_row_has_zero`, `first_col_has_zero`).
3. **Marking**: Iterate through the rest of the matrix (excluding the first row and column). If `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`.
4. **Setting Zeroes**: Iterate through the matrix again (excluding the first row and column). If `matrix[i][0] == 0` or `matrix[0][j] == 0`, set `matrix[i][j] = 0`.
5. **Final Step**: Based on the variables from step 2, set the first row and/or first column to zero if needed.
6. **Complexity**:
   - Time Complexity: O(m * n), as we traverse the matrix a few times.
   - Space Complexity: O(1) beyond the input matrix."""
    
    answer = """def setZeroes(matrix):
    if not matrix or not matrix[0]:
        return
        
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
    
    # Use first row and first column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # Update based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # Update first row and first column
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0
            
    return matrix"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef setZeroes(matrix):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        m = int(data[0])\n        n = int(data[1])\n        matrix = []\n        idx = 2\n        for i in range(m):\n            matrix.append([int(x) for x in data[idx:idx+n]])\n            idx += n\n        setZeroes(matrix)\n        for row in matrix:\n            print(' '.join(map(str, row)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid setZeroes(vector<vector<int>>& matrix) {\n    // User logic\n}\n\nint main() {\n    int m, n;\n    if (cin >> m >> n) {\n        vector<vector<int>> matrix(m, vector<int>(n));\n        for (int i = 0; i < m; ++i)\n            for (int j = 0; j < n; ++j)\n                cin >> matrix[i][j];\n        setZeroes(matrix);\n        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j)\n                cout << matrix[i][j] << (j == n - 1 ? \"\" : \" \");\n            cout << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static void setZeroes(int[][] matrix) {\n        // User logic\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int m = sc.nextInt();\n            int n = sc.nextInt();\n            int[][] matrix = new int[m][n];\n            for (int i = 0; i < m; i++)\n                for (int j = 0; j < n; j++)\n                    matrix[i][j] = sc.nextInt();\n            setZeroes(matrix);\n            for (int i = 0; i < m; i++) {\n                for (int j = 0; j < n; j++) {\n                    System.out.print(matrix[i][j] + (j == n - 1 ? \"\" : \" \"));\n                }\n                System.out.println();\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction setZeroes(matrix) {\n    // User logic\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nif (input.length >= 2) {\n    const m = input[0];\n    const n = input[1];\n    let matrix = [];\n    let idx = 2;\n    for (let i = 0; i < m; i++) {\n        matrix.push(input.slice(idx, idx + n));\n        idx += n;\n    }\n    setZeroes(matrix);\n    matrix.forEach(row => console.log(row.join(' ')));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid setZeroes(int** matrix, int matrixSize, int* matrixColSize) {\n    // User logic\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        int** matrix = (int**)malloc(m * sizeof(int*));\n        int colSize = n;\n        for (int i = 0; i < m; i++) {\n            matrix[i] = (int*)malloc(n * sizeof(int));\n            for (int j = 0; j < n; j++) scanf(\"%d\", &matrix[i][j]);\n        }\n        setZeroes(matrix, m, &colSize);\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n                printf(\"%d\", matrix[i][j]);\n                if (j < n - 1) printf(\" \");\n            }\n            printf(\"\\n\");\n            free(matrix[i]);\n        }\n        free(matrix);\n    }\n    return 0;\n}"
    }

    def _solve(mat):
        m, n = len(mat), len(mat[0])
        r0 = any(mat[0][j] == 0 for j in range(n))
        c0 = any(mat[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        if r0:
            for j in range(n): mat[0][j] = 0
        if c0:
            for i in range(m): mat[i][0] = 0
        return mat

    def _mat_str(mat):
        return "\n".join(" ".join(map(str, row)) for row in mat)

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3 3\n1 1 1\n1 0 1\n1 1 1", "expected_output": _mat_str(_solve([[1,1,1],[1,0,1],[1,1,1]])), "is_sample": True},
        {"input": "3 4\n0 1 2 0\n3 4 5 2\n1 3 1 5", "expected_output": _mat_str(_solve([[0,1,2,0],[3,4,5,2],[1,3,1,5]])), "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1 1\n1", "expected_output": "1", "is_sample": False},
        {"input": "1 1\n0", "expected_output": "0", "is_sample": False},
        {"input": "1 2\n1 0", "expected_output": "0 0", "is_sample": False},
        {"input": "2 1\n1\n0", "expected_output": "0\n0", "is_sample": False},
        {"input": "2 3\n1 2 3\n4 5 6", "expected_output": "1 2 3\n4 5 6", "is_sample": False},
        # Last three: Stress tests
        {"input": "200 200\n" + "\n".join([" ".join(["1"]*200)]*200), "expected_output": _mat_str(_solve([[1]*200 for _ in range(200)])), "is_sample": False},
        {"input": "20 20\n" + "\n".join([" ".join(["0" if i==j else "1" for i in range(20)]) for j in range(20)]), "expected_output": _mat_str(_solve([[0 if i==j else 1 for i in range(20)] for j in range(20)])), "is_sample": False},
        {"input": "20 20\n" + "\n".join([" ".join(["0" if i==0 or j==0 else "1" for i in range(20)]) for j in range(20)]), "expected_output": _mat_str(_solve([[0 if i==0 or j==0 else 1 for i in range(20)] for j in range(20)])), "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/73_Set_Matrix_Zeroes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
