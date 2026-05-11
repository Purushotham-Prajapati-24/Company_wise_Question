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
        "python": "import sys\nimport re\nimport json\n\n# User logic here\nclass Solution:\n    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:\n        pass\n\nif __name__ == '__main__':\n    # Lethal parsing: Extract all inner brackets to form a 2D matrix\n    input_data = sys.stdin.read()\n    matrix = []\n    # Find all content inside square brackets\n    rows = re.findall(r'\\[([^\\[\\]]+)\\]', input_data)\n    for r in rows:\n        nums = [int(x) for x in re.findall(r'-?\\d+', r)]\n        if nums: matrix.append(nums)\n    \n    if matrix:\n        sol = Solution()\n        print(json.dumps(sol.longestIncreasingPath(matrix)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\n// User logic here\nclass Solution {\npublic:\n    int longestIncreasingPath(vector<vector<int>>& matrix) {\n        return 0;\n    }\n};\n\nint main() {\n    ios_base::sync_with_stdio(false);\n    cin.tie(NULL);\n    \n    string input;\n    string line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    vector<vector<int>> matrix;\n    regex row_re(\"\\\\[([^\\\\[\\\\]]+)\\\\]\");\n    regex num_re(\"-?\\\\d+\");\n    \n    auto rows_begin = sregex_iterator(input.begin(), input.end(), row_re);\n    auto rows_end = sregex_iterator();\n    \n    for (sregex_iterator i = rows_begin; i != rows_end; ++i) {\n        string row_str = (*i)[1].str();\n        vector<int> row;\n        auto nums_begin = sregex_iterator(row_str.begin(), row_str.end(), num_re);\n        auto nums_end = sregex_iterator();\n        for (sregex_iterator j = nums_begin; j != nums_end; ++j) {\n            row.push_back(stoi(j->str()));\n        }\n        if (!row.empty()) matrix.push_back(row);\n    }\n    \n    if (!matrix.empty()) {\n        Solution sol;\n        cout << sol.longestIncreasingPath(matrix) << endl;\n    }\n    \n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\n// User logic here\nclass Solution {\n    public int longestIncreasingPath(int[][] matrix) {\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        \n        String input = sb.toString();\n        List<int[]> matrixList = new ArrayList<>();\n        \n        Pattern rowPattern = Pattern.compile(\"\\\\[([^\\\\[\\\\]]+)\\\\]\");\n        Matcher rowMatcher = rowPattern.matcher(input);\n        \n        while (rowMatcher.find()) {\n            String rowStr = rowMatcher.group(1);\n            List<Integer> rowNums = new ArrayList<>();\n            Pattern numPattern = Pattern.compile(\"-?\\\\d+\");\n            Matcher numMatcher = numPattern.matcher(rowStr);\n            while (numMatcher.find()) {\n                rowNums.add(Integer.parseInt(numMatcher.group()));\n            }\n            if (!rowNums.isEmpty()) {\n                int[] row = new int[rowNums.size()];\n                for (int i = 0; i < rowNums.size(); i++) row[i] = rowNums.get(i);\n                matrixList.add(row);\n            }\n        }\n        \n        if (!matrixList.isEmpty()) {\n            int[][] matrix = matrixList.toArray(new int[0][]);\n            System.out.println(new Solution().longestIncreasingPath(matrix));\n        }\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\n// User logic here\n/**\n * @param {number[][]} matrix\n * @return {number}\n */\nvar longestIncreasingPath = function(matrix) {\n    return 0;\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const matrix = [];\n    // Lethal parsing: Find content in all inner brackets\n    const rowMatches = input.matchAll(/\\[([^\\[\\]]+)\\]/g);\n    for (const match of rowMatches) {\n        const row = match[1].match(/-?\\d+/g)?.map(Number) || [];\n        if (row.length > 0) matrix.push(row);\n    }\n    \n    if (matrix.length > 0) {\n        console.log(JSON.stringify(longestIncreasingPath(matrix)));\n    }\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// User logic here\nint longestIncreasingPath(int** matrix, int matrixSize, int* matrixColSize) {\n    return 0;\n}\n\nint main() {\n    int capacity = 100;\n    int** matrix = malloc(capacity * sizeof(int*));\n    int* matrixColSize = malloc(capacity * sizeof(int));\n    int size = 0;\n    \n    char input[1000000];\n    if (fread(input, 1, sizeof(input), stdin) > 0) {\n        char* ptr = input;\n        while ((ptr = strchr(ptr, '[')) != NULL) {\n            ptr++;\n            if (*ptr == '[') continue; // Outer bracket\n            \n            int colCap = 100;\n            int* row = malloc(colCap * sizeof(int));\n            int colSize = 0;\n            \n            while (*ptr && *ptr != ']') {\n                int val, charsRead;\n                if (sscanf(ptr, \"%d%n\", &val, &charsRead) == 1) {\n                    if (colSize == colCap) {\n                        colCap *= 2;\n                        row = realloc(row, colCap * sizeof(int));\n                    }\n                    row[colSize++] = val;\n                    ptr += charsRead;\n                } else {\n                    ptr++;\n                }\n            }\n            \n            if (colSize > 0) {\n                if (size == capacity) {\n                    capacity *= 2;\n                    matrix = realloc(matrix, capacity * sizeof(int*));\n                    matrixColSize = realloc(matrixColSize, capacity * sizeof(int));\n                }\n                matrix[size] = row;\n                matrixColSize[size++] = colSize;\n            }\n        }\n    }\n    \n    if (size > 0) {\n        printf(\"%d\\n\", longestIncreasingPath(matrix, size, matrixColSize));\n    }\n    \n    for (int i = 0; i < size; i++) free(matrix[i]);\n    free(matrix);\n    free(matrixColSize);\n    return 0;\n}"
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
