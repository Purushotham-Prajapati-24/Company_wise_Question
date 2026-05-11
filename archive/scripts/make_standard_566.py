import json
import os

def generate_json():
    problem_id = 566
    title = "Reshape the Matrix"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>566. Reshape the Matrix</h3>
<p>In MATLAB, there is a handy function called <code>reshape</code> which can reshape an <code>m x n</code> matrix into a new one with a different size <code>r x c</code> keeping its original data.</p>

<p>You are given an <code>m x n</code> matrix <code>mat</code> and two integers <code>r</code> and <code>c</code> representing the number of rows and the number of columns of the wanted reshaped matrix.</p>

<p>The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.</p>

<p>If the <code>reshape</code> operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg" style="width: 613px; height: 173px;" />
<pre><strong>Input:</strong> mat = [[1,2],[3,4]], r = 1, c = 4
<strong>Output:</strong> [[1,2,3,4]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg" style="width: 453px; height: 173px;" />
<pre><strong>Input:</strong> mat = [[1,2],[3,4]], r = 2, c = 4
<strong>Output:</strong> [[1,2],[3,4]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-1000 &lt;= mat[i][j] &lt;= 1000</code></li>
	<li><code>1 &lt;= r, c &lt;= 300</code></li>
</ul>"""

    input_format = "Line 1: r c. Line 2: m n. Following m lines: space-separated integers for each row."
    output_format = "Multiple lines (one per row), each containing space-separated integers of the reshaped matrix."
    
    constraints = [
        "1 <= m, n <= 100",
        "1 <= r, c <= 300",
        "If m * n != r * c, return the original matrix.",
        "O(m * n) time complexity.",
        "O(r * c) space complexity."
    ]
    
    explanation = """To reshape a matrix while maintaining row-traversing order:
1. **Check Validity**:
   - Compares the total number of elements in the original matrix (`m * n`) with the total number of elements in the target matrix (`r * c`).
   - If they are not equal, the reshape is impossible; return the original matrix.
2. **Flattening and Rebuilding**:
   - Create a new `r x c` matrix.
   - Use a counter `idx` to track the absolute position of elements in a flattened version (from `0` to `m*n - 1`).
   - For each element at `mat[i][j]`, its absolute position is `k = i * n + j`.
   - In the reshaped matrix, this element goes to `new_mat[k // c][k % c]`.
3. **Complexity**:
   - Time Complexity: O(m * n) because we visit each element exactly once.
   - Space Complexity: O(r * c) to store the reshaped matrix."""
    
    answer = """def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
        
    res = [[0] * c for _ in range(r)]
    for i in range(m * n):
        res[i // c][i % c] = mat[i // n][i % n]
        
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef matrixReshape(mat, r, c):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if not lines: sys.exit(0)\n    r, c = map(int, lines[0].split())\n    m, n = map(int, lines[1].split())\n    mat = []\n    for i in range(2, 2 + m):\n        mat.append(list(map(int, lines[i].split())))\n    res = matrixReshape(mat, r, c)\n    for row in res:\n        print(\" \".join(map(str, row)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[][] matrixReshape(int[][] mat, int r, int c) {\n        // User logic\n        return new int[0][0];\n    }\n}",
        "javascript": "function matrixReshape(mat, r, c) {\n    // User logic\n}",
        "c": "int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 4\\n2 2\\n1 2\\n3 4", "expected_output": "1 2 3 4", "is_sample": True},
        {"input": "2 4\\n2 2\\n1 2\\n3 4", "expected_output": "1 2\\n3 4", "is_sample": True},
        {"input": "2 2\\n2 2\\n1 2\\n3 4", "expected_output": "1 2\\n3 4", "is_sample": True},
        {"input": "4 1\\n2 2\\n1 2\\n3 4", "expected_output": "1\\n2\\n3\\n4", "is_sample": False},
        {"input": "1 1\\n1 1\\n42", "expected_output": "42", "is_sample": False},
        {"input": "2 3\\n3 2\\n1 2\\n3 4\\n5 6", "expected_output": "1 2 3\\n4 5 6", "is_sample": False},
        {"input": "3 2\\n1 6\\n1 2 3 4 5 6", "expected_output": "1 2\\n3 4\\n5 6", "is_sample": False},
        # Stress cases
        {"input": "1 10000\\n100 100\\n" + "\\n".join([" ".join([str(j) for j in range(100)]) for i in range(100)]), "expected_output": " ".join([str(j) for i in range(100) for j in range(100)]), "is_sample": False},
        {"input": "10000 1\\n100 100\\n" + "\\n".join([" ".join([str(j) for j in range(100)]) for i in range(100)]), "expected_output": "\\n".join([str(j) for i in range(100) for j in range(100)]), "is_sample": False},
        {"input": "50 200\\n100 100\\n" + "\\n".join([" ".join(["0"]*100) for i in range(100)]), "expected_output": "\\n".join([" ".join(["0"]*200) for i in range(50)]), "is_sample": False}
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

    output_path = "401-600/566_Reshape_the_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
