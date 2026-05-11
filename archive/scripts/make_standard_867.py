import json
import os

def generate_json():
    problem_id = 867
    title = "Transpose Matrix"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>867. Transpose Matrix</h3>
<p>Given a 2D integer array <code>matrix</code>, return <em>the <strong>transpose</strong> of</em> <code>matrix</code>.</p>

<p>The <strong>transpose</strong> of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png" style="width: 600px; height: 197px;" /></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [[1,4,7],[2,5,8],[3,6,9]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6]]
<strong>Output:</strong> [[1,4],[2,5],[3,6]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Line 1: m n. Following m lines: space-separated integers for each row."
    output_format = "The transposed n x m matrix, each row on a new line with space-separated integers."
    
    constraints = [
        "1 <= m, n <= 1000",
        "1 <= m * n <= 10^5",
        "O(M * N) time complexity.",
        "O(M * N) space complexity (for result)."
    ]
    
    explanation = """To transpose an m x n matrix:
1. **Initialize Result Matrix**:
   - Create a new matrix of dimensions n x m (swapped from m x n).
2. **Copy Elements**:
   - Iterate through the original matrix using row index `i` (0 to m-1) and column index `j` (0 to n-1).
   - Set `result[j][i] = matrix[i][j]`.
3. **Return**:
   - Return the new transposed matrix.
4. **Complexity**:
   - Time Complexity: O(M * N) since we visit every element once.
   - Space Complexity: O(M * N) for the transposed matrix result."""
    
    answer = """def transpose(matrix: list[list[int]]) -> list[list[int]]:
    m, n = len(matrix), len(matrix[0])
    res = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            res[j][i] = matrix[i][j]
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef transpose(matrix):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if not lines: sys.exit(0)\n    m, n = map(int, lines[0].split())\n    matrix = []\n    for i in range(1, 1 + m):\n        matrix.append(list(map(int, lines[i].split())))\n    res = transpose(matrix)\n    for row in res:\n        print(\" \".join(map(str, row)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<vector<int>> transpose(vector<vector<int>>& matrix) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[][] transpose(int[][] matrix) {\n        // User logic\n        return new int[0][0];\n    }\n}",
        "javascript": "function transpose(matrix) {\n    // User logic\n}",
        "c": "int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "3 3\\n1 2 3\\n4 5 6\\n7 8 9", "expected_output": "1 4 7\\n2 5 8\\n3 6 9", "is_sample": True},
        {"input": "2 3\\n1 2 3\\n4 5 6", "expected_output": "1 4\\n2 5\\n3 6", "is_sample": True},
        {"input": "1 1\\n42", "expected_output": "42", "is_sample": True},
        {"input": "3 1\\n1\\n2\\n3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1 3\\n1 2 3", "expected_output": "1\\n2\\n3", "is_sample": False},
        {"input": "2 2\\n1 2\\n3 4", "expected_output": "1 3\\n2 4", "is_sample": False},
        {"input": "4 2\\n1 2\\n3 4\\n5 6\\n7 8", "expected_output": "1 3 5 7\\n2 4 6 8", "is_sample": False},
        # Stress cases
        {"input": "10 10\\n" + "\\n".join([" ".join([str(i+j) for j in range(10)]) for i in range(10)]), "expected_output": "\\n".join([" ".join([str(i+j) for j in range(10)]) for i in range(10)]), "is_sample": False},
        {"input": "5 1\\n1\\n2\\n3\\n4\\n5", "expected_output": "1 2 3 4 5", "is_sample": False},
        {"input": "1 5\\n1 2 3 4 5", "expected_output": "1\\n2\\n3\\n4\\n5", "is_sample": False}
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
        "topics": ["Array", "Matrix", "Simulation"],
        "companyIndex": 0
    }

    output_path = "801-1000/867_Transpose_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
