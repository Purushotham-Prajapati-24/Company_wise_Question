import json
import os

def generate_json():
    problem_id = 329
    title = "Longest Increasing Path in a Matrix"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>329. Longest Increasing Path in a Matrix</h3>
<p>Given an <code>m x n</code> integers <code>matrix</code>, return <em>the length of the longest strictly increasing path in </em><code>matrix</code>.</p>

<p>From each cell, you can move in four directions: left, right, up, or down. You <strong>may not</strong> move <strong>diagonally</strong> or move <strong>outside the boundary</strong> (i.e., wrap-around is not allowed).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" style="width: 242px; height: 242px;" />
<pre><strong>Input:</strong> matrix = [[9,9,4],[6,6,8],[2,1,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing path is [1, 2, 6, 9].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" style="width: 252px; height: 253px;" />
<pre><strong>Input:</strong> matrix = [[3,4,5],[3,2,6],[2,2,1]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> matrix = [[1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A 2D integer array `matrix`."
    output_format = "An integer representing the length of the longest increasing path."
    
    constraints = [
        "1 <= m, n <= 200",
        "0 <= matrix[i][j] <= 2^31 - 1"
    ]
    
    explanation = """To find the longest strictly increasing path in a matrix, we use **Depth-First Search (DFS)** with **Memoization**.

### Algorithm Steps:
1. **Memoization Table**: Initialize a 2D table `memo` with zeros to store the result of the longest path starting from each cell $(i, j)$.
2. **DFS Function**:
   - For a given cell `(i, j)`, visit its neighbors (up, down, left, right).
   - A move is valid if the neighbor is within boundaries and its value is strictly greater than the current cell's value.
   - The longest path starting at `(i, j)` is $1 + \max(\text{longest path from neighbors})$.
   - If `memo[i][j]` is already computed, return it immediately to avoid redundant calculations.
3. **Global Maximum**: Iterate through all cells in the matrix, call the DFS for each, and maintain the global maximum length.

### Complexity Analysis:
- **Time Complexity**: $O(M \times N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell is processed and cached exactly once. 
- **Space Complexity**: $O(M \times N)$ for the memoization table and the DFS recursion stack."""
    
    answer = """class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            
            memo[(r, c)] = res
            return res
            
        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))
                
        return max_path"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        matrix = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.longestIncreasingPath(matrix)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int longestIncreasingPath(vector<vector<int>>& matrix) {\n        // Your logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        string cleaned;\n        for (char c : line) if (c != ' ') cleaned += c;\n        line = cleaned;\n        vector<vector<int>> matrix;\n        if (line.length() >= 2) {\n            line = line.substr(1, line.length() - 2);\n            int i = 0;\n            while (i < line.length()) {\n                if (line[i] == '[') {\n                    int j = i + 1;\n                    while (j < line.length() && line[j] != ']') j++;\n                    string inner = line.substr(i + 1, j - i - 1);\n                    vector<int> row;\n                    if (!inner.empty()) {\n                        stringstream ss(inner);\n                        string item;\n                        while (getline(ss, item, ',')) {\n                            row.push_back(stoi(item));\n                        }\n                    }\n                    matrix.push_back(row);\n                    i = j + 1;\n                } else {\n                    i++;\n                }\n            }\n        }\n        Solution sol;\n        cout << sol.longestIncreasingPath(matrix) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int longestIncreasingPath(int[][] matrix) {\n        // Your logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            String line = scanner.nextLine().replaceAll(\"\\\\s+\", \"\");\n            List<int[]> matrixList = new ArrayList<>();\n            if (line.length() >= 2) {\n                line = line.substring(1, line.length() - 1);\n                int i = 0;\n                while (i < line.length()) {\n                    if (line.charAt(i) == '[') {\n                        int j = i + 1;\n                        while (j < line.length() && line.charAt(j) != ']') j++;\n                        String inner = line.substring(i + 1, j);\n                        if (inner.isEmpty()) {\n                            matrixList.add(new int[0]);\n                        } else {\n                            String[] parts = inner.split(\",\");\n                            int[] row = new int[parts.length];\n                            for (int k = 0; k < parts.length; k++) {\n                                row[k] = Integer.parseInt(parts[k]);\n                            }\n                            matrixList.add(row);\n                        }\n                        i = j + 1;\n                    } else {\n                        i++;\n                    }\n                }\n            }\n            int[][] matrix = matrixList.toArray(new int[0][]);\n            Solution sol = new Solution();\n            System.out.println(sol.longestIncreasingPath(matrix));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[][]} matrix\n * @return {number}\n */\nvar longestIncreasingPath = function(matrix) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim();\nif (input) {\n    const matrix = JSON.parse(input);\n    console.log(JSON.stringify(longestIncreasingPath(matrix)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint longestIncreasingPath(int** matrix, int matrixSize, int* matrixColSize) {\n    // Your logic here\n    return 0;\n}\n\nint main() {\n    char line[500000];\n    if (fgets(line, sizeof(line), stdin)) {\n        line[strcspn(line, \"\\r\\n\")] = 0;\n        int capacity = 100;\n        int** matrix = malloc(capacity * sizeof(int*));\n        int* matrixColSize = malloc(capacity * sizeof(int));\n        int size = 0;\n        char* ptr = line;\n        while (*ptr && *ptr != '[') ptr++;\n        if (*ptr == '[') ptr++;\n        while (*ptr && *ptr != ']') {\n            if (*ptr == '[') {\n                ptr++;\n                int colCap = 100;\n                int* row = malloc(colCap * sizeof(int));\n                int colSize = 0;\n                while (*ptr && *ptr != ']') {\n                    int val, charsRead;\n                    if (sscanf(ptr, \"%d%n\", &val, &charsRead) == 1) {\n                        if (colSize >= colCap) {\n                            colCap *= 2;\n                            row = realloc(row, colCap * sizeof(int));\n                        }\n                        row[colSize++] = val;\n                        ptr += charsRead;\n                    } else {\n                        ptr++;\n                    }\n                }\n                if (size >= capacity) {\n                    capacity *= 2;\n                    matrix = realloc(matrix, capacity * sizeof(int*));\n                    matrixColSize = realloc(matrixColSize, capacity * sizeof(int));\n                }\n                matrix[size] = row;\n                matrixColSize[size] = colSize;\n                size++;\n                if (*ptr == ']') ptr++;\n            } else {\n                ptr++;\n            }\n        }\n        printf(\"%d\\n\", longestIncreasingPath(matrix, size, matrixColSize));\n        for (int i = 0; i < size; i++) free(matrix[i]);\n        free(matrix);\n        free(matrixColSize);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[9,9,4],[6,6,8],[2,1,1]]", "expected_output": "4", "is_sample": True},
        {"input": "[[3,4,5],[3,2,6],[2,2,1]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1]]", "expected_output": "1", "is_sample": True},
        {"input": "[[1,2],[3,4]]", "expected_output": "3", "is_sample": False},
        {"input": "[[7,8,9],[1,2,3],[4,5,6]]", "expected_output": "5", "is_sample": False},
        {"input": "[[1,2,3],[4,5,6],[7,8,9]]", "expected_output": "5", "is_sample": False},
        {"input": "[[5,5,5],[5,5,5],[5,5,5]]", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": json.dumps([[1] * 200 for _ in range(200)]), "expected_output": "1", "is_sample": False},
        {"input": json.dumps([[i * 200 + j for j in range(200)] for i in range(200)]), "expected_output": "399", "is_sample": False},
        {"input": json.dumps([[i * 200 + j + (i % 2) for j in range(200)] for i in range(200)]), "expected_output": "399", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming", "DFS", "Memoization", "Graph", "Matrix"],
        "companyIndex": 1
    }

    output_path = "301-500/329_Longest_Increasing_Path_in_a_Matrix.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
