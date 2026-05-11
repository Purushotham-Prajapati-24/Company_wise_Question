import json
import os

def generate_json():
    problem_id = 48
    title = "Rotate Image"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>48. Rotate Image</h3>
<p>You are given an <code>n x n</code> 2D <code>matrix</code> representing an image, rotate the image by <strong>90 degrees (clockwise)</strong>.</p>

<p>You have to rotate the image <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong>, which means you have to modify the input 2D matrix directly. <strong>DO NOT</strong> allocate another 2D matrix and do the rotation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="width: 342px; height: 193px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [[7,4,1],[8,5,2],[9,6,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="width: 542px; height: 233px;" />
<pre>
<strong>Input:</strong> matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
<strong>Output:</strong> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>-1000 &lt;= matrix[i][j] &lt;= 1000</code></li>
</ul>"""

    input_format = "A series of lines, each containing space-separated integers representing a row of the n x n matrix. Input ends at EOF."
    output_format = "The rotated n x n matrix, where each row is printed on a new line with space-separated integers."
    
    constraints = [
        "n == matrix.length == matrix[i].length",
        "1 <= n <= 20",
        "-1000 <= matrix[i][j] <= 1000",
        "Rotation must be done in-place (O(1) auxiliary space)."
    ]
    
    explanation = """To rotate an n x n matrix 90 degrees clockwise in-place, we can utilize two simple linear transformations:
1. **Transpose the Matrix**: Flip the matrix over its main diagonal. This is done by swapping `matrix[i][j]` with `matrix[j][i]` for all `0 <= i < j < n`. After this step, the rows of the original matrix become the columns of the transposed matrix.
2. **Reverse Each Row**: Iterate through each row of the transposed matrix and reverse the order of its elements. Reverse is done by swapping `matrix[i][j]` with `matrix[i][n - 1 - j]` for `0 <= j < n // 2`.
3. Complexity:
   - Time Complexity: O(n^2), as we visit each element of the matrix a constant number of times.
   - Space Complexity: O(1), as we modify the input matrix directly without using additional data structures proportional to the size of the matrix."""
    
    answer = """def rotate(matrix):
    n = len(matrix)
    
    # 1. Transpose: Swap matrix[i][j] with matrix[j][i]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # 2. Reverse each row
    for i in range(n):
        matrix[i].reverse()"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef rotate(matrix):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    matrix = []\n    for line in input_data:\n        if line.strip():\n            matrix.append([int(x) for x in line.split()])\n    if matrix:\n        rotate(matrix)\n        for row in matrix:\n            print(\" \".join(map(str, row)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvoid rotate(vector<vector<int>>& matrix) {\n    // User logic\n}\n\nint main() {\n    string line;\n    vector<vector<int>> matrix;\n    while (getline(cin, line)) {\n        if (line.empty()) continue;\n        stringstream ss(line);\n        int val;\n        vector<int> row;\n        while (ss >> val) row.push_back(val);\n        matrix.push_back(row);\n    }\n    rotate(matrix);\n    for (const auto& row : matrix) {\n        for (int i = 0; i < row.size(); ++i)\n            cout << row[i] << (i == row.size() - 1 ? \"\" : \" \");\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static void rotate(int[][] matrix) {\n        // User logic\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<int[]> list = new ArrayList<>();\n        while (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            if (line.isEmpty()) continue;\n            String[] parts = line.split(\"\\\\s+\");\n            int[] row = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) row[i] = Integer.parseInt(parts[i]);\n            list.add(row);\n        }\n        int[][] matrix = list.toArray(new int[0][]);\n        rotate(matrix);\n        for (int[] row : matrix) {\n            for (int i = 0; i < row.length; i++) \n                System.out.print(row[i] + (i == row.length - 1 ? \"\" : \" \"));\n            System.out.println();\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction rotate(matrix) {\n    // User logic\n}\n\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n');\nconst matrix = lines.map(line => line.trim().split(/\\s+/).map(Number));\nrotate(matrix);\nmatrix.forEach(row => console.log(row.join(' ')));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid rotate(int** matrix, int matrixSize, int* matrixColSize) {\n    // User logic\n}\n\nint main() {\n    char line[500];\n    int rows[20][20], n = 0;\n    while (n < 20 && fgets(line, sizeof(line), stdin)) {\n        if (line[0] == '\\n') continue;\n        char* token = strtok(line, \" \\t\\r\\n\");\n        int col = 0;\n        while (token && col < 20) { rows[n][col++] = atoi(token); token = strtok(NULL, \" \\t\\r\\n\"); }\n        if (col > 0) n++;\n    }\n    if (n > 0) {\n        int** matrix = (int**)malloc(n * sizeof(int*));\n        int colSize = n;\n        for (int i = 0; i < n; i++) {\n            matrix[i] = (int*)malloc(n * sizeof(int));\n            for (int j = 0; j < n; j++) matrix[i][j] = rows[i][j];\n        }\n        rotate(matrix, n, &colSize);\n        for (int i = 0; i < n; i++) {\n            for (int j = 0; j < n; j++) {\n                printf(\"%d\", matrix[i][j]);\n                if (j + 1 < n) printf(\" \");\n            }\n            printf(\"\\n\");\n            free(matrix[i]);\n        }\n        free(matrix);\n    }\n    return 0;\n}"
    }

    def _rotate_matrix(mat_str):
        # Helper to calculate expected output format
        import ast
        try:
            mat = ast.literal_eval(mat_str.replace("[[", "[").replace("]]", "]").replace("],[", " | ").split(" | "))
        except:
            # Simple fallback for manual grid construction
            mat = [list(map(int, row.split())) for row in mat_str.strip().split("\n")]
        
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for row in mat:
            row.reverse()
        return "\n".join([" ".join(map(str, r)) for r in mat])

    test_cases = [
        # First two: Sample LeetCode cases (formatted for stdin)
        {"input": "1 2 3\n4 5 6\n7 8 9", "expected_output": "7 4 1\n8 5 2\n9 6 3", "is_sample": True},
        {"input": "5 1 9 11\n2 4 8 10\n13 3 6 7\n15 14 12 16", "expected_output": "15 13 2 5\n14 3 4 1\n12 6 8 9\n16 7 10 11", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2\n3 4", "expected_output": "3 1\n4 2", "is_sample": False},
        {"input": "1 1\n1 1", "expected_output": "1 1\n1 1", "is_sample": False},
        {"input": "-1 -2\n-3 -4", "expected_output": "-3 -1\n-4 -2", "is_sample": False},
        {"input": "1 2 3\n1 2 3\n1 2 3", "expected_output": "1 1 1\n2 2 2\n3 3 3", "is_sample": False},
        # Last three: Stress tests
        {"input": "\n".join([" ".join([str(i*20 + j) for j in range(20)]) for i in range(20)]), "expected_output": "...", "is_sample": False},
        {"input": "\n".join([" ".join(["0"] * 20) for _ in range(20)]), "expected_output": "\n".join([" ".join(["0"] * 20) for _ in range(20)]), "is_sample": False},
        {"input": "\n".join([" ".join([str((i+j)%1000) for j in range(20)]) for i in range(20)]), "expected_output": "...", "is_sample": False}
    ]
    
    # Fill stress outputs
    for i in [7, 9]:
        mat = [list(map(int, test_cases[i]["input"].split())) for _ in range(1)] # Dummy
        # Correctly reconstruct 20x20
        mat = []
        rows = test_cases[i]["input"].split("\n")
        for r in rows:
            mat.append(list(map(int, r.split())))
        
        n = len(mat)
        for r_idx in range(n):
            for c_idx in range(r_idx + 1, n):
                mat[r_idx][c_idx], mat[c_idx][r_idx] = mat[c_idx][r_idx], mat[r_idx][c_idx]
        for row in mat:
            row.reverse()
        test_cases[i]["expected_output"] = "\n".join([" ".join(map(str, r)) for r in mat])

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
        "topics": ["Array", "Math", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/48_Rotate_Image.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
