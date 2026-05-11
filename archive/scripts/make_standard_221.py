import json
import os

def generate_json():
    problem_id = 221
    title = "Maximal Square"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>221. Maximal Square</h3>
<p>Given an <code>m x n</code> binary <code>matrix</code> filled with <code>'0'</code>s and <code>'1'</code>s, <em>find the largest square containing only </em><code>'1'</code><em>s and return its area</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;" />
<pre>
<strong>Input:</strong> matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;" />
<pre>
<strong>Input:</strong> matrix = [["0","1"],["1","0"]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [["0"]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.</li>
</ul>"""

    input_format = "Line 1: m and n. Next m lines: binary row strings."
    output_format = "An integer representing the maximum square area."
    
    constraints = [
        "Matrix dimensions: [1, 300] x [1, 300]",
        "Values: '0' or '1'",
        "O(M*N) time complexity expected.",
        "O(N) space complexity is achievable."
    ]
    
    explanation = """To find the largest square area of 1s:
1. **Dynamic Programming**:
   - Let `dp[i][j]` be the side length of the largest square whose bottom-right corner is at `(i, j)`.
   - If `matrix[i][j] == '1'`:
     - `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.
     - This is because a square of side `s` can only be formed if the squares to the top, left, and top-left are all at least of side `s-1`.
   - If `matrix[i][j] == '0'`:
     - `dp[i][j] = 0`.
2. **Space Optimization**:
   - Notice that `dp[i][j]` only depends on the previous row and the current row's previous element.
   - We can use a single array `dp` of size `n+1` to store results, updating it in place while keeping track of the "top-left" value using a temporary variable.
3. **Complexity**:
   - Time Complexity: O(M * N) to fill the DP table.
   - Space Complexity: O(N) using the optimized row approach."""
    
    answer = """def maximalSquare(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [0] * (n + 1)
    max_side = 0
    prev = 0 # Top-left (dp[i-1][j-1])
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = dp[j]
            if matrix[i-1][j-1] == '1':
                # dp[j] is dp[i-1][j], dp[j-1] is dp[i][j-1], prev is dp[i-1][j-1]
                dp[j] = min(dp[j], dp[j-1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp
            
    return max_side * max_side"""

    boilerplate = {
        "python": "import sys\n\ndef maximalSquare(matrix):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        first = lines[0].split()\n        m, n = int(first[0]), int(first[1])\n        matrix = [list(lines[i+1].strip()) for i in range(m)]\n        print(maximalSquare(matrix))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint maximalSquare(vector<vector<char>>& matrix) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (cin >> m >> n) {\n        vector<vector<char>> matrix(m, vector<char>(n));\n        for (int i = 0; i < m; i++) {\n            string row;\n            cin >> row;\n            for (int j = 0; j < n; j++) matrix[i][j] = row[j];\n        }\n        cout << maximalSquare(matrix) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int maximalSquare(char[][] matrix) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String first = br.readLine();\n        if (first == null) return;\n        String[] mn = first.trim().split(\"\\\\s+\");\n        int m = Integer.parseInt(mn[0]);\n        int n = Integer.parseInt(mn[1]);\n        char[][] matrix = new char[m][n];\n        for (int i = 0; i < m; i++) {\n            String row = br.readLine().trim();\n            for (int j = 0; j < n; j++) matrix[i][j] = row.charAt(j);\n        }\n        System.out.println(new Solution().maximalSquare(matrix));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maximalSquare(matrix) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 1) {\n    const first = input[0].trim().split(/\\\\s+/);\n    if (first.length >= 2) {\n        const m = parseInt(first[0]);\n        const n = parseInt(first[1]);\n        let matrix = [];\n        for (let i = 0; i < m; i++) {\n            matrix.push(input[i+1].trim().split(''));\n        }\n        console.log(maximalSquare(matrix));\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint maximalSquare(char** matrix, int matrixSize, int* matrixColSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        char** matrix = (char**)malloc(m * sizeof(char*));\n        int* colSizes = (int*)malloc(m * sizeof(int));\n        for (int i = 0; i < m; i++) {\n            matrix[i] = (char*)malloc((n + 1) * sizeof(char));\n            scanf(\"%s\", matrix[i]);\n            colSizes[i] = n;\n        }\n        printf(\"%d\\n\", maximalSquare(matrix, m, colSizes));\n        for (int i = 0; i < m; i++) free(matrix[i]);\n        free(matrix);\n        free(colSizes);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "4 5\\n10100\\n10111\\n11111\\n10010", "expected_output": "4", "is_sample": True},
        {"input": "2 2\\n01\\n10", "expected_output": "1", "is_sample": True},
        {"input": "1 1\\n0", "expected_output": "0", "is_sample": True},
        {"input": "1 1\\n1", "expected_output": "1", "is_sample": False},
        {"input": "3 3\\n111\\n111\\n111", "expected_output": "9", "is_sample": False},
        {"input": "5 5\\n00000\\n00000\\n00110\\n00110\\n00000", "expected_output": "4", "is_sample": False},
        {"input": "2 3\\n111\\n111", "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": "300 300\\n" + "\\n".join(["1"*300]*300), "expected_output": "90000", "is_sample": False},
        {"input": "300 300\\n" + "\\n".join(["0"*300]*300), "expected_output": "0", "is_sample": False},
        {"input": "300 300\\n" + "\\n".join([("10"*150) if i%2==0 else ("01"*150) for i in range(300)]), "expected_output": "1", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "Matrix"],
        "companyIndex": 0
    }

    output_path = "1-200/221_Maximal_Square.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
