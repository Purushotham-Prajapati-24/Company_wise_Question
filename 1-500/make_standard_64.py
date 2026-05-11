import json
import os

def generate_json():
    problem_id = 64
    title = "Minimum Path Sum"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>64. Minimum Path Sum</h3>
<p>Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1&rarr;3&rarr;1&rarr;1&rarr;1 minimizes the sum.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6]]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 200</code></li>
</ul>"""

    input_format = "Two integers m and n, followed by m lines each containing n space-separated integers representing the grid."
    output_format = "An integer representing the minimum path sum."
    
    constraints = [
        "1 <= m, n <= 200",
        "0 <= grid[i][j] <= 200",
        "Only move either down or right at any point."
    ]
    
    explanation = """To find the path from top-left to bottom-right that minimizes the sum of its elements:
1. **Dynamic Programming Strategy**:
   - Let `dp[i][j]` be the minimum path sum to reach cell `(i, j)`.
   - The cell `(i, j)` can only be reached from `(i-1, j)` (top) or `(i, j-1)` (left).
2. **Recurrence Relation**:
   - `dp[0][0] = grid[0][0]` (starting point).
   - For the first row (`i=0`): `dp[0][j] = dp[0][j-1] + grid[0][j]` (can only come from left).
   - For the first column (`j=0`): `dp[i][0] = dp[i-1][0] + grid[i][0]` (can only come from top).
   - For other cells: `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`.
3. **Optimization**:
   - We only need the values from the previous row to calculate the current row.
   - We can use a 1D array `dp` of size `n` to store the minimum sums, updating it for each row.
4. **Complexity**:
   - Time Complexity: O(m * n).
   - Space Complexity: O(n) using 1D space optimization."""
    
    answer = """def minPathSum(grid):
    if not grid or not grid[0]:
        return 0
        
    m, n = len(grid), len(grid[0])
    # dp[j] stores the minimum path sum to reach cell (i, j) in the current row
    dp = [0] * n
    
    # Initialize the first cell
    dp[0] = grid[0][0]
    
    # Initialize the first row (can only come from the left)
    for j in range(1, n):
        dp[j] = dp[j-1] + grid[0][j]
        
    # Fill the DP table row by row
    for i in range(1, m):
        # First column of current row (can only come from above)
        dp[0] += grid[i][0]
        for j in range(1, n):
            # Current cell can come from above (dp[j]) or left (dp[j-1])
            dp[j] = grid[i][j] + min(dp[j], dp[j-1])
            
    return dp[n-1]"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys, re\n\ndef minPathSum(grid):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'\\d+', data)]\n    if len(nums) >= 2:\n        m, n = nums[0], nums[1]\n        grid = []\n        for i in range(m):\n            grid.append(nums[2 + i*n : 2 + (i+1)*n])\n        print(minPathSum(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int minPathSum(vector<vector<int>>& grid) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(\"\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while (iter != end) { nums.push_back(stoi(iter->str())); iter++; }\n    if (nums.size() >= 2) {\n        int m = nums[0], n = nums[1];\n        vector<vector<int>> grid(m, vector<int>(n));\n        for(int i=0; i<m; ++i)\n            for(int j=0; j<n; ++j) grid[i][j] = nums[2 + i*n + j];\n        Solution sol;\n        cout << sol.minPathSum(grid) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int minPathSum(int[][] grid) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        if (list.size() >= 2) {\n            int mVal = list.get(0), nVal = list.get(1);\n            int[][] grid = new int[mVal][nVal];\n            for(int i=0; i<mVal; i++)\n                for(int j=0; j<nVal; j++) grid[i][j] = list.get(2 + i*nVal + j);\n            Solution sol = new Solution();\n            System.out.println(sol.minPathSum(grid));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar minPathSum = function(grid) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = (input.match(/\\d+/g) || []).map(Number);\n    if (nums.length >= 2) {\n        const m = nums[0], n = nums[1];\n        const grid = [];\n        for(let i=0; i<m; i++) grid.push(nums.slice(2 + i*n, 2 + (i+1)*n));\n        console.log(minPathSum(grid));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint minPathSum(int** grid, int gridSize, int* gridColSize) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    int* nums = NULL;\n    int capacity = 10, count = 0, found = 0, c;\n    long long current = 0;\n    nums = malloc(capacity * sizeof(int));\n    while ((c = getchar()) != EOF) {\n        if (isdigit(c)) {\n            if (!found) { found = 1; current = c - '0'; } else current = current * 10 + (c - '0');\n        } else {\n            if (found) {\n                if (count == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); }\n                nums[count++] = (int)current; found = 0;\n            }\n        }\n    }\n    if (found) {\n        if (count == capacity) { capacity += 1; nums = realloc(nums, capacity * sizeof(int)); }\n        nums[count++] = (int)current;\n    }\n    if (count >= 2) {\n        int m = nums[0], n = nums[1];\n        int** grid = malloc(m * sizeof(int*));\n        int colSize = n;\n        for (int i = 0; i < m; i++) {\n            grid[i] = malloc(n * sizeof(int));\n            for (int j = 0; j < n; j++) grid[i][j] = nums[2 + i*n + j];\n        }\n        printf(\"%d\\n\", minPathSum(grid, m, &colSize));\n    }\n    return 0;\n}"
    }

    def _solve(grid):
        m, n = len(grid), len(grid[0])
        dp = [0]*n
        dp[0] = grid[0][0]
        for j in range(1, n): dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        return dp[-1]

    def _fmt(grid):
        m, n = len(grid), len(grid[0])
        s = f"{m} {n}"
        for row in grid:
            s += " " + " ".join(map(str, row))
        return s

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": _fmt([[1,3,1],[1,5,1],[4,2,1]]), "expected_output": "7", "is_sample": True},
        {"input": _fmt([[1,2,3],[4,5,6]]), "expected_output": "12", "is_sample": True},
        # Middle five: Diverse cases
        {"input": _fmt([[0]]), "expected_output": "0", "is_sample": False},
        {"input": _fmt([[1,2,3,4,5]]), "expected_output": "15", "is_sample": False},
        {"input": _fmt([[1],[2],[3],[4],[5]]), "expected_output": "15", "is_sample": False},
        {"input": _fmt([[1,1],[1,1]]), "expected_output": "3", "is_sample": False},
        {"input": _fmt([[1,100,1],[1,100,1],[1,1,1]]), "expected_output": "5", "is_sample": False},
        # Last three: Stress tests
        {"input": _fmt([[1]*200 for _ in range(200)]), "expected_output": "399", "is_sample": False},
        {"input": _fmt([[i+j for j in range(200)] for i in range(200)]), "expected_output": str(_solve([[i+j for j in range(200)] for i in range(200)])), "is_sample": False},
        {"input": _fmt([[200]*200 for _ in range(200)]), "expected_output": "79800", "is_sample": False}
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

    output_path = "1-200/64_Minimum_Path_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
