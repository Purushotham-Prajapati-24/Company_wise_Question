import json
import os

def generate_json():
    problem_id = 54
    title = "Spiral Matrix"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>54. Spiral Matrix</h3>
<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the </em><code>matrix</code><em> in spiral order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>"""

    input_format = "A 2D array of integers matrix."
    output_format = "An array of integers in spiral order."
    
    constraints = [
        "1 <= m, n <= 10",
        "-100 <= matrix[i][j] <= 100"
    ]
    
    explanation = """To traverse a matrix in spiral order:
1. **Define Boundaries**: `top = 0`, `bottom = m-1`, `left = 0`, `right = n-1`.
2. **Loop**: While `top <= bottom` and `left <= right`:
   - Traverse **Right**: From `left` to `right` along `top`. Increment `top`.
   - Traverse **Down**: From `top` to `bottom` along `right`. Decrement `right`.
   - If `top <= bottom`:
     - Traverse **Left**: From `right` to `left` along `bottom`. Decrement `bottom`.
   - If `left <= right`:
     - Traverse **Up**: From `bottom` to `top` along `left`. Increment `left`.
3. **Complexity**:
   - **Time**: $O(M \times N)$
   - **Space**: $O(1)$ additional space (result array excluded)."""
    
    answer = """def spiralOrder(matrix):
    if not matrix: return []
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Right
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        
        # Down
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            # Up
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef spiralOrder(matrix):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    matrix = []\n    for line in lines:\n        if line.strip():\n            matrix.append([int(x) for x in line.split()])\n    res = spiralOrder(matrix)\n    print('[' + ', '.join(map(str, res)) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\n\nusing namespace std;\n\nvector<int> spiralOrder(vector<vector<int>>& matrix) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<vector<int>> matrix;\n    while (getline(cin, line)) {\n        if (line.empty()) continue;\n        stringstream ss(line);\n        int val;\n        vector<int> row;\n        while (ss >> val) row.push_back(val);\n        if (!row.empty()) matrix.push_back(row);\n    }\n    auto res = spiralOrder(matrix);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << res[i];\n        if (i + 1 < (int)res.size()) cout << \",\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<Integer> spiralOrder(int[][] matrix) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<int[]> list = new ArrayList<>();\n        while (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            if (line.isEmpty()) continue;\n            String[] parts = line.split(\"\\\\s+\");\n            int[] row = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) row[i] = Integer.parseInt(parts[i]);\n            list.add(row);\n        }\n        int[][] matrix = list.toArray(new int[0][]);\n        List<Integer> res = spiralOrder(matrix);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            sb.append(res.get(i));\n            if (i + 1 < res.size()) sb.append(\",\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction spiralOrder(matrix) {\n    // User logic\n    return [];\n}\n\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n');\nconst matrix = lines.map(l => l.trim().split(/\\s+/).map(Number));\nconst res = spiralOrder(matrix);\nconsole.log('[' + res.join(',') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line[500];\n    int rows[10][10], m = 0, n = 0;\n    while (m < 10 && fgets(line, sizeof(line), stdin)) {\n        if (line[0] == '\\n') continue;\n        char* token = strtok(line, \" \\t\\r\\n\");\n        int col = 0;\n        while (token && col < 10) { rows[m][col++] = atoi(token); token = strtok(NULL, \" \\t\\r\\n\"); }\n        if (col > 0) { if (m == 0) n = col; m++; }\n    }\n    if (m > 0) {\n        int** matrix = (int**)malloc(m * sizeof(int*));\n        for (int i = 0; i < m; i++) {\n            matrix[i] = (int*)malloc(n * sizeof(int));\n            for (int j = 0; j < n; j++) matrix[i][j] = rows[i][j];\n        }\n        int returnSize = 0;\n        int* res = spiralOrder(matrix, m, &n, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d\", res[i]);\n            if (i + 1 < returnSize) printf(\",\");\n        }\n        printf(\"]\\n\");\n        if (res) free(res);\n        for (int i = 0; i < m; i++) free(matrix[i]);\n        free(matrix);\n    }\n    return 0;\n}"

    }

    test_cases = [
        {"input": "1 2 3\n4 5 6\n7 8 9", "expected_output": "[1,2,3,6,9,8,7,4,5]", "is_sample": True},
        {"input": "1 2 3 4\n5 6 7 8\n9 10 11 12", "expected_output": "[1,2,3,4,8,12,11,10,9,5,6,7]", "is_sample": True},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2\n3 4", "expected_output": "[1,2,4,3]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[1,2,3]", "is_sample": False},
        {"input": "1\n2\n3", "expected_output": "[1,2,3]", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "1\n2\n3\n4\n5", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "1 2\n3 4\n5 6", "expected_output": "[1,2,4,6,5,3]", "is_sample": False},
        {"input": "10 20\n30 40", "expected_output": "[10,20,40,30]", "is_sample": False}
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

    output_path = "1-200/54_Spiral_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
