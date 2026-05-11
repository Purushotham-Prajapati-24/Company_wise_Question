import json
import os

def generate_json():
    # 361. Bomb Enemy
    problem_id = 361
    title = "Bomb Enemy"
    difficulty = "MEDIUM"
    marks = 15
    
    html_description = """<h3>361. Bomb Enemy</h3>
<p>Given an <code>m x n</code> matrix <code>grid</code> where each cell is either a wall <code>'W'</code>, an enemy <code>'E'</code> or empty <code>'0'</code>, return the maximum enemies you can kill using one bomb. The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.</p>

<p>Note: You can only put the bomb at an empty cell.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Placing a bomb at (1,1) kills 3 enemies.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Placing a bomb at any "0" cell in the second row kills 1 enemy.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> is either <code>'W'</code>, <code>'E'</code>, or <code>'0'</code>.</li>
</ul>"""

    input_format = "A 2D character array `grid` containing 'W', 'E', and '0'."
    output_format = "The maximum number of enemies killed by one bomb."
    
    constraints = [
        "1 <= m, n <= 500",
        "Bomb only in '0' cells.",
        "Walls ('W') block bomb range in both directions.",
        "Must be O(M * N) to handle 500x500 grids."
    ]
    
    explanation = """### Comprehensive Explanation for 361. Bomb Enemy

The problem asks for the optimal placement of a bomb on a 2D grid to maximize the "line of sight" kill count, where walls block the blast. A naive approach of calculating kills for every '0' cell would take $O(M \\cdot N \\cdot (M+N))$, which is too slow ($O(N^3)$).

#### Optimization Strategy (Pre-calculated Row and Column Segments)
We can achieve $O(M \\cdot N)$ by reusing the counts for the current "segment" of the row and column. A segment is defined as a contiguous range of non-wall cells.

1.  **Row Segments**: For each row, we only need to recount enemies in the current segment if we just passed a wall or are at the start of a row. This count remains valid for all '0' cells in that segment.
2.  **Column Segments**: Since we process the grid row by row, we maintain an array `col_kills` of size $N$. For each column $j$, we only recount enemies in the current column segment if we just passed a wall in that column or are at the start of the grid (row 0).

#### Most Optimized Approach in Python
We iterate through the grid exactly once.
- For each cell $(i, j)$:
  - **Row Update**: If $j=0$ or $grid[i][j-1] == 'W'$, iterate forward to count all 'E's until the next wall. Store in `row_kills`.
  - **Column Update**: If $i=0$ or $grid[i-1][j] == 'W'$, iterate downward to count all 'E's until the next wall. Store in `col_counts[j]`.
  - **Calculation**: If $grid[i][j] == '0'$, the result for that cell is `row_kills + col_counts[j]`.

#### Complexity Analysis
- **Time Complexity**: $O(M \\cdot N)$. Each cell is visited at most 3 times (once in the main loop, once during a row-segment count, and once during a column-segment count).
- **Space Complexity**: $O(N)$ to store the column counts for the current row.

### Performance Analysis
For a 500x500 grid, $M \\cdot N = 250,000$, which is well within the 1-second time limit for a linear-time Python solution."""

    answer = """class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        \"\"\"
        Calculates the maximum enemies killed in O(M*N) time using segment pre-calculation.
        \"\"\"
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_kills = 0
        row_kills = 0
        col_kills = [0] * n  # Pre-calculated kills for current column segments
        
        for i in range(m):
            for j in range(n):
                # 1. Update row kills at the start of each new row segment
                if j == 0 or grid[i][j-1] == 'W':
                    row_kills = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_kills += 1
                        k += 1
                
                # 2. Update column kills at the start of each new column segment
                if i == 0 or grid[i-1][j] == 'W':
                    col_kills[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_kills[j] += 1
                        k += 1
                
                # 3. If cell is empty, it's a candidate for the bomb
                if grid[i][j] == '0':
                    max_kills = max(max_kills, row_kills + col_kills[j])
                    
        return max_kills"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef maxKilledEnemies(grid):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read()\n    matches = re.findall(r'\\[(.*?)\\]', input_data)\n    grid = []\n    for match in matches:\n        row = re.findall(r'\"(.*?)\"', match)\n        if row: grid.append(row)\n    if grid:\n        print(maxKilledEnemies(grid))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\nusing namespace std;\n\nint maxKilledEnemies(vector<vector<char>>& grid) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    vector<vector<char>> grid;\n    regex row_regex(\"\\\\[(.*?)\\\\]\");\n    regex char_regex(\"\\\\\"(.*?)\\\\\"\");\n    auto row_begin = sregex_iterator(input.begin(), input.end(), row_regex);\n    auto row_end = sregex_iterator();\n    for (auto i = row_begin; i != row_end; ++i) {\n        string row_str = i->str();\n        vector<char> row;\n        auto char_begin = sregex_iterator(row_str.begin(), row_str.end(), char_regex);\n        for (auto j = char_begin; j != row_end; ++j) {\n            row.push_back((*j)[1].str()[0]);\n        }\n        if (!row.empty()) grid.push_back(row);\n    }\n    if (!grid.empty()) cout << maxKilledEnemies(grid) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public static int maxKilledEnemies(char[][] grid) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        List<char[]> gridList = new ArrayList<>();\n        Matcher rm = Pattern.compile(\"\\\\[(.*?)\\\\]\").matcher(input);\n        while (rm.find()) {\n            String rowStr = rm.group(1);\n            List<Character> rowChars = new ArrayList<>();\n            Matcher cm = Pattern.compile(\"\\\\\"(.*?)\\\\\"\").matcher(rowStr);\n            while (cm.find()) rowChars.add(cm.group(1).charAt(0));\n            if (!rowChars.isEmpty()) {\n                char[] row = new char[rowChars.size()];\n                for (int i = 0; i < rowChars.size(); i++) row[i] = rowChars.get(i);\n                gridList.add(row);\n            }\n        }\n        if (!gridList.isEmpty()) {\n            System.out.println(maxKilledEnemies(gridList.toArray(new char[0][0])));\n        }\n    }\n}",
        "javascript": "\"use strict\";\nconst fs = require('fs');\n\nfunction maxKilledEnemies(grid) {\n    // User logic here\n    return 0;\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const rowMatches = input.match(/\\[(.*?)\\]/g);\n    if (!rowMatches) return;\n    const grid = rowMatches.map(rowStr => {\n        const charMatches = rowStr.match(/\"(.*?)\"/g);\n        return charMatches ? charMatches.map(s => s.replace(/\"/g, '')) : [];\n    }).filter(row => row.length > 0);\n    if (grid.length > 0) console.log(maxKilledEnemies(grid));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint maxKilledEnemies(char** grid, int rows, int cols) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char *buf = malloc(1000000);\n    int len = fread(buf, 1, 999999, stdin);\n    buf[len] = '\\0';\n    char **grid = malloc(500 * sizeof(char*));\n    int r = 0, max_c = 0;\n    char *p = buf;\n    while (*p) {\n        if (*p == '[') {\n            p++;\n            char *row = malloc(500);\n            int c = 0;\n            while (*p && *p != ']') {\n                if (*p == '\"') {\n                    p++;\n                    if (*p && *p != '\"') row[c++] = *p;\n                    while (*p && *p != '\"') p++;\n                }\n                p++;\n            }\n            if (c > 0) {\n                grid[r++] = row;\n                if (c > max_c) max_c = c;\n            } else free(row);\n        }\n        p++;\n    }\n    if (r > 0) printf(\"%d\\n\", maxKilledEnemies(grid, r, max_c));\n    return 0;\n}"
    }

       
    test_cases = [
        {"input": '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]', "expected_output": "3", "is_sample": True},
        {"input": '[["W","W","W"],["0","0","0"],["E","E","E"]]', "expected_output": "1", "is_sample": True},
        {"input": '[["E","E","E"],["E","0","E"],["E","E","E"]]', "expected_output": "4", "is_sample": False},
        {"input": '[["0"]]', "expected_output": "0", "is_sample": False},
        {"input": '[["E"],["0"],["E"]]', "expected_output": "2", "is_sample": False},
        {"input": '[["0","E","E"],["W","0","E"]]', "expected_output": "2", "is_sample": False},
        {"input": '[["E","W","E"],["0","W","0"],["E","W","E"]]', "expected_output": "0", "is_sample": False},
        {"input": json.dumps([["E" if (i+j)%3==0 else ("W" if (i+j)%3==1 else "0") for j in range(20)] for i in range(20)]), "expected_output": "3", "is_sample": False},
        {"input": json.dumps([["E"]*50 for _ in range(50)]), "expected_output": "0", "is_sample": False},
        {"input": json.dumps([["0" if i==25 and j==25 else "E" for j in range(50)] for i in range(50)]), "expected_output": "99", "is_sample": False},
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
        "companyIndex": 1
    }

    output_path = "301-500/361_Bomb_Enemy.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path} with 10 test cases.")

if __name__ == "__main__":
    generate_json()
