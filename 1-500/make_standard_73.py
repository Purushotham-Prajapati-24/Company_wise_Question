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
        "python": "import sys, re\n\ndef setZeroes(matrix):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    if len(nums) >= 2:\n        m, n = nums[0], nums[1]\n        matrix = []\n        for i in range(m):\n            matrix.append(nums[2 + i*n : 2 + (i+1)*n])\n        setZeroes(matrix)\n        for row in matrix:\n            print(' '.join(map(str, row)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    void setZeroes(vector<vector<int>>& matrix) {\n        // User Logic Here\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"-?\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while(iter != end) { nums.push_back(stoi((*iter).str())); iter++; }\n    if (nums.size() >= 2) {\n        int m = nums[0], n = nums[1];\n        vector<vector<int>> matrix(m, vector<int>(n));\n        for(int i=0; i<m; i++) for(int j=0; j<n; j++) matrix[i][j] = nums[2 + i*n + j];\n        Solution sol;\n        sol.setZeroes(matrix);\n        for(int i=0; i<m; i++) {\n            for(int j=0; j<n; j++) cout << matrix[i][j] << (j == n-1 ? \"\" : \" \");\n            cout << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public void setZeroes(int[][] matrix) {\n        // User Logic Here\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        List<Integer> nums = new ArrayList<>();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        while (m.find()) nums.add(Integer.parseInt(m.group()));\n        if (nums.size() >= 2) {\n            int rows = nums.get(0), cols = nums.get(1);\n            int[][] matrix = new int[rows][cols];\n            for (int i=0; i<rows; i++) for (int j=0; j<cols; j++) matrix[i][j] = nums.get(2 + i*cols + j);\n            new Solution().setZeroes(matrix);\n            for (int i=0; i<rows; i++) {\n                for (int j=0; j<cols; j++) System.out.print(matrix[i][j] + (j == cols-1 ? \"\" : \" \"));\n                System.out.println();\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[][]} matrix\n * @return {void} Do not return anything, modify matrix in-place instead.\n */\nvar setZeroes = function(matrix) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const nums = (input.match(/-?\\d+/g) || []).map(Number);\n    if (nums.length >= 2) {\n        const m = nums[0], n = nums[1];\n        let matrix = [];\n        for (let i = 0; i < m; i++) matrix.push(nums.slice(2 + i * n, 2 + (i + 1) * n));\n        setZeroes(matrix);\n        matrix.forEach(row => console.log(row.join(' ')));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nvoid setZeroes(int** matrix, int matrixSize, int* matrixColSize) {\n    // User Logic Here\n}\n\nint main() {\n    char line[4096];\n    int* nums = malloc(40005 * sizeof(int));\n    int count = 0;\n    while (scanf(\"%d\", &nums[count]) == 1) count++;\n    if (count >= 2) {\n        int m = nums[0], n = nums[1];\n        int** matrix = malloc(m * sizeof(int*));\n        int colSize = n;\n        for (int i = 0; i < m; i++) {\n            matrix[i] = malloc(n * sizeof(int));\n            for (int j = 0; j < n; j++) matrix[i][j] = nums[2 + i * n + j];\n        }\n        setZeroes(matrix, m, &colSize);\n        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) printf(\"%d%s\", matrix[i][j], (j == n - 1 ? \"\" : \" \"));\n            printf(\"\\n\");\n        }\n    }\n    return 0;\n}"
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
