import json
import os

def generate_json():
    problem_id = 311
    title = "Sparse Matrix Multiplication"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>311. Sparse Matrix Multiplication</h3>
<p>Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> <code>mat1</code> of size <code>m x k</code> and <code>mat2</code> of size <code>k x n</code>, return the result of <code>mat1 x mat2</code>. You may assume that multiplication is always possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0311.Sparse%20Matrix%20Multiplication/images/mult-grid.jpg" style="width: 500px; height: 142px;" />
<pre><strong>Input:</strong> mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> [[7,0,0],[-7,0,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> mat1 = [[0]], mat2 = [[0]]
<strong>Output:</strong> [[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == mat1.length</code></li>
	<li><code>k == mat1[i].length == mat2.length</code></li>
	<li><code>n == mat2[i].length</code></li>
	<li><code>1 &lt;= m, n, k &lt;= 100</code></li>
	<li><code>-100 &lt;= mat1[i][j], mat2[i][j] &lt;= 100</code></li>
</ul>"""

    input_format = "Two 2D arrays: `mat1` and `mat2`."
    output_format = "A 2D array representing the product of `mat1` and `mat2`."
    
    constraints = [
        "1 <= m, n, k <= 100",
        "Sparse matrices (many zeros)."
    ]
    
    explanation = """To multiply two sparse matrices efficiently:
1. **Standard Multiplication**: Typically takes O(m * k * n). For sparse matrices, we can skip operations involving zero.
2. **Optimized Approach**:
   - Iterate through each row `i` of `mat1` and each column `k_idx` of `mat1`.
   - If `mat1[i][k_idx]` is non-zero:
     - Iterate through each column `j` of `mat2` for the specified row `k_idx`.
     - If `mat2[k_idx][j]` is also non-zero:
       - Update the result matrix: `res[i][j] += mat1[i][k_idx] * mat2[k_idx][j]`.
3. **Data Structure Alternative**: We can pre-process `mat1` and `mat2` into a list of coordinates `(row, col, value)` for non-zero elements to explicitly skip zeroes, but the nested loop with a simple `if` check is often sufficient and clean for these constraints.
4. **Complexity Analysis**:
   - Time: O(M * K * N) in worst case, but much faster for sparse matrices as the inner loop only executes for non-zero entries.
   - Space: O(M * N) for the result matrix."""
    
    answer = """class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k_dim, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        
        # Optimize by skipping zeros in mat1
        for i in range(m):
            for k_idx in range(k_dim):
                if mat1[i][k_idx] != 0:
                    # If non-zero, apply its contribution to all columns j in mat2
                    for j in range(n):
                        if mat2[k_idx][j] != 0:
                            res[i][j] += mat1[i][k_idx] * mat2[k_idx][j]
                            
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef multiply(mat1, mat2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    mat1 = json.loads(lines[0].strip().replace(' ', ''))\n    mat2 = json.loads(lines[1].strip().replace(' ', ''))\n    result = multiply(mat1, mat2)\n    print(json.dumps(result))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nvector<vector<int>> parseMatrix(const string& line) {\n    vector<vector<int>> mat;\n    vector<int> row;\n    string clean = line;\n    // parse [[a,b],[c,d]]\n    bool inRow = false;\n    string num = \"\";\n    for (char ch : clean) {\n        if (ch == '[') { if(inRow) {} else inRow = false; }\n        else if (ch == ']') {\n            if (!num.empty()) { row.push_back(stoi(num)); num = \"\"; }\n            if (!row.empty()) { mat.push_back(row); row.clear(); }\n        } else if (ch == ',') {\n            if (!num.empty()) { row.push_back(stoi(num)); num = \"\"; }\n        } else if ((ch >= '0' && ch <= '9') || ch == '-') num += ch;\n    }\n    return mat;\n}\n\nvector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line1, line2;\n    getline(cin, line1);\n    getline(cin, line2);\n    auto mat1 = parseMatrix(line1);\n    auto mat2 = parseMatrix(line2);\n    auto res = multiply(mat1, mat2);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        if (i) cout << \",\";\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); j++) {\n            if (j) cout << \",\";\n            cout << res[i][j];\n        }\n        cout << \"]\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[][] multiply(int[][] mat1, int[][] mat2) {\n        // User logic here\n        return new int[0][0];\n    }\n\n    static int[][] parseMatrix(String line) {\n        line = line.trim().replaceAll(\"\\\\s\", \"\");\n        line = line.substring(1, line.length()-1);\n        String[] rows = line.split(\"\\\\],\\\\[\");\n        int[][] mat = new int[rows.length][];\n        for (int i = 0; i < rows.length; i++) {\n            String row = rows[i].replaceAll(\"[\\\\[\\\\]]\", \"\");\n            String[] nums = row.split(\",\");\n            mat[i] = new int[nums.length];\n            for (int j = 0; j < nums.length; j++) mat[i][j] = Integer.parseInt(nums[j]);\n        }\n        return mat;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int[][] mat1 = parseMatrix(sc.nextLine());\n        int[][] mat2 = parseMatrix(sc.nextLine());\n        int[][] res = new Solution().multiply(mat1, mat2);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.length; i++) {\n            if (i > 0) sb.append(\",\");\n            sb.append(\"[\");\n            for (int j = 0; j < res[i].length; j++) {\n                if (j > 0) sb.append(\",\");\n                sb.append(res[i][j]);\n            }\n            sb.append(\"]\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction multiply(mat1, mat2) {\n    // User logic here\n    return [];\n}\n\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst mat1 = JSON.parse(lines[0].replace(/\\s/g,''));\nconst mat2 = JSON.parse(lines[1].replace(/\\s/g,''));\nconsole.log(JSON.stringify(multiply(mat1, mat2)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint** multiply(int** mat1, int m, int k, int** mat2, int n, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    // Simplified: read two lines, parse manually\n    // User logic here - implement full solution\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]", "expected_output": "[[7,0,0],[-7,0,3]]", "is_sample": True},
        {"input": "[[0]]\n[[0]]", "expected_output": "[[0]]", "is_sample": True},
        {"input": "[[1,1]]\n[[1],[1]]", "expected_output": "[[2]]", "is_sample": False},
        {"input": "[[1,2],[3,4]]\n[[1,0],[0,1]]", "expected_output": "[[1,2],[3,4]]", "is_sample": False},
        {"input": "[[1,0],[0,1]]\n[[2,2],[2,2]]", "expected_output": "[[2,2],[2,2]]", "is_sample": False},
        {"input": "[[0,0],[0,0]]\n[[0,0],[0,0]]", "expected_output": "[[0,0],[0,0]]", "is_sample": False},
        {"input": "[[1,2,3]]\n[[1],[2],[3]]", "expected_output": "[[14]]", "is_sample": False},
        {"input": "[[1,0],[0,2]]\n[[3,0],[0,4]]", "expected_output": "[[3,0],[0,8]]", "is_sample": False},
        {"input": "[[1,2],[0,0]]\n[[0,0],[1,2]]", "expected_output": "[[2,4],[0,0]]", "is_sample": False},
        {"input": "[[5]]\n[[3]]", "expected_output": "[[15]]", "is_sample": False}
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

    output_path = "201-400/311_Sparse_Matrix_Multiplication.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
