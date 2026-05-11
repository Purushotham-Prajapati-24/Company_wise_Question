import json
import os

def generate_json():
    problem_id = 1267
    title = "Count Servers that Communicate"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>1267. Count Servers that Communicate</h3>
<p>You are given a map of a server center, represented as a <code>m * n</code> integer matrix&nbsp;<code>grid</code>, where 1 means that on that cell there is a server and 0 means that it is empty. Two servers are said to communicate if they are on the same row or on the same column.<br />
<br />
Return the number of servers&nbsp;that communicate with any other server.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-6.jpg" style="width: 202px; height: 203px;" />
<pre>
<strong>Input:</strong> grid = [[1,0],[0,1]]
<strong>Output:</strong> 0
<b>Explanation:</b>&nbsp;No servers can communicate with others.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/13/untitled-diagram-4.jpg" style="width: 203px; height: 203px;" />
<pre>
<strong>Input:</strong> grid = [[1,0],[1,1]]
<strong>Output:</strong> 3
<b>Explanation:</b>&nbsp;All three servers can communicate with at least one other server.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-1-3.jpg" style="width: 443px; height: 443px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
<strong>Output:</strong> 4
<b>Explanation:</b>&nbsp;The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at grid[3][3] cannot communicate with any other server.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 250</code></li>
	<li><code>grid[i][j] == 0 or 1</code></li>
</ul>"""

    input_format = "Two integers m and n, followed by the m*n elements of the grid."
    output_format = "An integer representing the count of communicating servers."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def countServers(grid):
    R, C = len(grid), len(grid[0])
    row_count = [sum(row) for row in grid]
    col_count = [sum(grid[r][c] for r in range(R)) for c in range(C)]
    
    ans = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                if row_count[r] > 1 or col_count[c] > 1:
                    ans += 1
    return ans"""

    boilerplate = {
        "python": "import sys\n\ndef countServers(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        m, n = int(data[0]), int(data[1])\n        grid = []\n        for i in range(m):\n            grid.append([int(x) for x in data[2+i*n : 2+(i+1)*n]])\n        print(countServers(grid))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\nint main() {\n    int m, n;\n    if(cin >> m >> n) {\n        vector<vector<int>> grid(m, vector<int>(n));\n        for(int i=0; i<m; i++) for(int j=0; j<n; j++) cin >> grid[i][j];\n        // solve and print\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(sc.hasNextInt()) {\n            int m = sc.nextInt();\n            int n = sc.nextInt();\n            int[][] grid = new int[m][n];\n            for(int i=0; i<m; i++) for(int j=0; j<n; j++) grid[i][j] = sc.nextInt();\n            // solve and print\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nconsole.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
    }

    test_cases = [
        {"input": "2 2 1 0 0 1", "expected_output": "0", "is_sample": True},
        {"input": "2 2 1 0 1 1", "expected_output": "3", "is_sample": True},
        {"input": "4 4 1 1 0 0 0 0 1 0 0 0 1 0 0 0 0 1", "expected_output": "4", "is_sample": True},
        {"input": "1 3 1 1 1", "expected_output": "3", "is_sample": False},
        {"input": "3 1 1 1 1", "expected_output": "3", "is_sample": False},
        {"input": "2 2 0 0 0 0", "expected_output": "0", "is_sample": False},
        {"input": "2 2 1 1 1 1", "expected_output": "4", "is_sample": False},
        {"input": "3 3 1 0 0 0 1 0 0 0 1", "expected_output": "0", "is_sample": False},
        {"input": "4 1 1 0 0 1", "expected_output": "2", "is_sample": False},
        {"input": "1 4 1 0 0 1", "expected_output": "2", "is_sample": False}
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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
