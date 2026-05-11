import json
import os

def generate_json():
    problem_id = 296
    title = "Best Meeting Point"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>296. Best Meeting Point</h3>
<p>Given an <code>m x n</code> binary grid <code>grid</code> where each <code>1</code> marks the home of a friend, return <em>the minimal total <strong>Manhattan distance</strong> to a meeting point</em>.</p>

<p>The <strong>Manhattan distance</strong> between two points <code>(p1, p2)</code> and <code>(q1, q2)</code> is <code>|p1 - q1| + |p2 - q2|</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/meetingpoint-grid.jpg" style="width: 413px; height: 253px;" />
<pre><strong>Input:</strong> grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> grid = [[1,1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There will be at least two friends in the <code>grid</code>.</li>
</ul>"""

    input_format = "A stringified 2D binary grid."
    output_format = "An integer representing the minimal total Manhattan distance."
    
    constraints = [
        "1 <= m, n <= 200",
        "At least two friends in the grid."
    ]
    
    explanation = """To find the point that minimizes the total Manhattan distance to all friends:
1. **Separability**: The Manhattan distance is the sum of differences in X and Y coordinates: `dist = |x1 - x2| + |y1 - y2|`. This means we can minimize the distances for X and Y separately.
2. **Median Rule**: For 1D distance minimization, the point that minimizes the total absolute distance to a set of points is the **median** of those points.
3. **Algorithm**:
   - Collect all row indices `r` where `grid[r][c] == 1`.
   - Collect all column indices `c` where `grid[r][c] == 1`.
   - To find the distance in X (rows):
     - Sort the list of row indices.
     - Calculate the total distance from each index to the median.
   - To find the distance in Y (columns):
     - Sort the list of column indices.
     - Calculate the total distance from each index to the median.
   - Return the sum of minimal X distance and minimal Y distance.
4. **Complexity Analysis**:
   - Time: O(M * N) to collect indices and then O(H log H) to sort (H = number of houses). Given rows and columns are collected in sorted order, we can avoid explicit sorting.
   - Space: O(H) to store the indices."""
    
    answer = """class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Manhattan distance is separable (DistX + DistY)
        # 1D median minimizes the sum of absolute distances
        
        # 1. Collect Row indices (already in sorted order if we scan row-by-row)
        rows = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
        
        # 2. Collect Column indices (already in sorted order if we scan column-by-column)
        cols = []
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    cols.append(c)
                    
        # 3. Calculate min distance for 1D using two pointers (instead of finding median explicitly)
        def get_min_dist(points):
            dist = 0
            i, j = 0, len(points) - 1
            while i < j:
                dist += points[j] - points[i]
                i += 1
                j -= 1
            return dist
            
        return get_min_dist(rows) + get_min_dist(cols)"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef minTotalDistance(grid: list[list[int]]) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        grid = json.loads(input_data)\n        print(minTotalDistance(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint minTotalDistance(vector<vector<int>>& grid) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string all, line;\n    while (getline(cin, line)) all += line;\n    vector<vector<int>> grid;\n    vector<int> row;\n    string num;\n    for (char c : all) {\n        if (c == '[') num = \"\";\n        else if (c == ']') {\n            if (!num.empty()) { row.push_back(stoi(num)); num = \"\"; }\n            if (!row.empty()) { grid.push_back(row); row.clear(); }\n        }\n        else if (c == ',') {\n            if (!num.empty()) { row.push_back(stoi(num)); num = \"\"; }\n        }\n        else if (isdigit(c)) num += c;\n    }\n    cout << minTotalDistance(grid) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int minTotalDistance(int[][] grid) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) throws Exception {\n        Scanner sc = new Scanner(System.in);\n        String all = sc.useDelimiter(\"\\\\A\").next().trim().replaceAll(\"\\\\s\", \"\");\n        all = all.substring(1, all.length()-1);\n        String[] rowStrs = all.split(\"\\\\],\\\\[\");\n        int[][] grid = new int[rowStrs.length][];\n        for (int i = 0; i < rowStrs.length; i++) {\n            String r = rowStrs[i].replaceAll(\"[\\\\[\\\\]]\", \"\");\n            String[] parts = r.split(\",\");\n            grid[i] = new int[parts.length];\n            for (int j = 0; j < parts.length; j++) grid[i][j] = Integer.parseInt(parts[j]);\n        }\n        System.out.println(new Solution().minTotalDistance(grid));\n    }\n}",
        "javascript": "const fs = require('fs');\nconst grid = JSON.parse(fs.readFileSync(0, 'utf-8').trim());\n\nfunction minTotalDistance(grid) {\n    // User logic here\n    return 0;\n}\n\nconsole.log(minTotalDistance(grid));",
        "c": "int minTotalDistance(int** grid, int gridSize, int* gridColSize) {\n    // User logic here\n    return 0;\n}\n\n#include <stdio.h>\nint main() {\n    printf(\"0\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]", "expected_output": "6", "is_sample": True},
        {"input": "[[1,1]]", "expected_output": "1", "is_sample": True},
        {"input": "[[1,0,1]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1],[0],[1]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1,0,0],[0,0,0],[0,0,1]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1,1,1]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1,0],[0,1]]", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": "[[1 if i==j else 0 for j in range(200)] for i in range(200)]", "expected_output": "...", "is_sample": False},
        {"input": "[[1 if i==0 or i==199 else 0 for j in range(200)] for i in range(200)]", "expected_output": "...", "is_sample": False},
        {"input": "[[1 for j in range(200)] for i in range(200)]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Math", "Matrix", "Sorting"],
        "companyIndex": 0
    }

    output_path = "201-400/296_Best_Meeting_Point.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
