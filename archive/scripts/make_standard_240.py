import json
import os

def generate_json():
    problem_id = 240
    title = "Search a 2D Matrix II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>240. Search a 2D Matrix II</h3>
<p>Write an efficient algorithm that searches for a <code>target</code> value in an <code>m x n</code> integer matrix <code>matrix</code>. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg" style="width: 300px; height: 300px;" />
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg" style="width: 300px; height: 300px;" />
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers in each row are <strong>sorted</strong> in ascending order.</li>
	<li>All the integers in each column are <strong>sorted</strong> in ascending order.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Two lines: first, an m x n 2D array of integers; second, an integer target."
    output_format = "A boolean (true/false)."
    
    constraints = [
        "1 <= m, n <= 300",
        "Rows and columns sorted.",
        "O(m + n) time complexity required."
    ]
    
    explanation = """To search in an m x n matrix where both rows and columns are sorted effectively:
1. **Start from Top-Right Corner**: Start at `(0, n-1)`.
2. **Logic**:
   - If `matrix[row][col] == target`, return `true`.
   - If `matrix[row][col] > target`, the current column can't contain the target (since all elements below are even larger), so decrement `col` (move left).
   - If `matrix[row][col] < target`, the current row can't contain the target (since all elements left are even smaller), so increment `row` (move down).
3. **Complexity**:
   - Time: O(M + N) where M is rows and N is columns.
   - Space: O(1)."""
    
    answer = """class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
                
        return False"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef searchMatrix(matrix, target):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if input_data:\n        try:\n            matrix = json.loads(input_data[0])\n            target = int(input_data[1])\n        except:\n            # Try reading m n and then m rows\n            first = input_data[0].split()\n            if len(first) == 2:\n                m, n = map(int, first)\n                matrix = [list(map(int, input_data[i+1].split())) for i in range(m)]\n                target = int(input_data[m+1])\n            else:\n                matrix = []\n                target = 0\n        print(\"true\" if searchMatrix(matrix, target) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nbool searchMatrix(vector<vector<int>>& matrix, int target) {\n    // User logic\n    return false;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        if (line.find('[') != string::npos) {\n            // JSON-like parsing simplified\n            vector<vector<int>> matrix;\n            string targetLine;\n            getline(cin, targetLine);\n            int target = stoi(targetLine);\n            // Placeholder for actual matrix parsing\n            cout << (searchMatrix(matrix, target) ? \"true\" : \"false\") << endl;\n        } else {\n            stringstream ss(line);\n            int m, n;\n            if (ss >> m >> n) {\n                vector<vector<int>> matrix(m, vector<int>(n));\n                for (int i = 0; i < m; i++) {\n                    for (int j = 0; j < n; j++) cin >> matrix[i][j];\n                }\n                int target;\n                cin >> target;\n                cout << (searchMatrix(matrix, target) ? \"true\" : \"false\") << endl;\n            }\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean searchMatrix(int[][] matrix, int target) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String firstToken = sc.next();\n            if (firstToken.startsWith(\"[\")) {\n                // Handle JSON input simplified\n            } else {\n                int m = Integer.parseInt(firstToken);\n                int n = sc.nextInt();\n                int[][] matrix = new int[m][n];\n                for (int i = 0; i < m; i++) {\n                    for (int j = 0; j < n; j++) matrix[i][j] = sc.nextInt();\n                }\n                int target = sc.nextInt();\n                System.out.println(new Solution().searchMatrix(matrix, target) ? \"true\" : \"false\");\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction searchMatrix(matrix, target) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    let matrix = JSON.parse(input[0]);\n    let target = parseInt(input[1]);\n    console.log(searchMatrix(matrix, target) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nbool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int m, n, target;\n    if (scanf(\"%d %d\", &m, &n) == 2) {\n        int** matrix = (int**)malloc(m * sizeof(int*));\n        int* colSizes = (int*)malloc(m * sizeof(int));\n        for (int i = 0; i < m; i++) {\n            matrix[i] = (int*)malloc(n * sizeof(int));\n            colSizes[i] = n;\n            for (int j = 0; j < n; j++) scanf(\"%d\", &matrix[i][j]);\n        }\n        scanf(\"%d\", &target);\n        printf(\"%s\\n\", searchMatrix(matrix, m, colSizes, target) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\\n5", "expected_output": "true", "is_sample": True},
        {"input": "[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\\n20", "expected_output": "false", "is_sample": True},
        {"input": "[[1,1]]\\n1", "expected_output": "true", "is_sample": False},
        {"input": "[[1]]\\n0", "expected_output": "false", "is_sample": False},
        {"input": "[[-5]]\\n-5", "expected_output": "true", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]\\n5", "expected_output": "true", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]\\n10", "expected_output": "false", "is_sample": False},
        # Stress Tests (300x300)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: 300x300 all same 7, target 7
    m8 = [[7]*300 for _ in range(300)]
    test_cases[7] = {"input": json.dumps(m8) + "\\n7", "expected_output": "true", "is_sample": False}
    # Stress 9: 300x300 sequential, target 90000
    m9 = [[i*300 + j for j in range(300)] for i in range(300)]
    test_cases[8] = {"input": json.dumps(m9) + "\\n90000", "expected_output": "false", "is_sample": False}
    # Stress 10: 300x300 sparse diagonal, target 1
    m10 = [[0]*300 for _ in range(300)]
    m10[299][299] = 1
    test_cases[9] = {"input": json.dumps(m10) + "\\n1", "expected_output": "true", "is_sample": False}

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
        "topics": ["Array", "Binary Search", "Divide and Conquer", "Matrix"],
        "companyIndex": 0
    }

    output_path = "201-400/240_Search_a_2D_Matrix_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
