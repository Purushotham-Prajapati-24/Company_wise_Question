import json
import os

def generate_json():
    problem_id = 694
    title = "Number of Distinct Islands"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>694. Number of Distinct Islands</h3>
<p>You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>'s (representing land) connected <strong>4-directionally</strong> (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.</p>

<p>An island is considered to be the same as another if and only if one island can be translated (moved horizontally or vertically) to equal the other.</p>

<p>Return <em>the number of <b>distinct</b> islands</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-1-grid.jpg" style="width: 413px; height: 145px;" />
<pre><strong>Input:</strong> grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The two 2x2 islands are considered the same shape.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/05/01/distinctisland1-2-grid.jpg" style="width: 413px; height: 145px;" />
<pre><strong>Input:</strong> grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>m == grid.length</code></li>
    <li><code>n == grid[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 50</code></li>
    <li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "A single line: JSON 2D array `grid`."
    output_format = "An integer: the number of distinct islands."

    constraints = [
        "1 <= m, n <= 50",
        "grid[i][j] is 0 or 1"
    ]

    explanation = """Find each island using DFS. As we traverse, record the path taken relative to the starting row and column (e.g., coordinates `(r - r0, c - c0)`). Add this path signature to a set. The number of unique signatures in the set is the answer."""

    answer = """class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        distinct = set()
        
        def dfs(r, c, r0, c0, shape):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0
                shape.append((r - r0, c - c0))
                dfs(r + 1, c, r0, c0, shape)
                dfs(r - 1, c, r0, c0, shape)
                dfs(r, c + 1, r0, c0, shape)
                dfs(r, c - 1, r0, c0, shape)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = []
                    dfs(i, j, i, j, shape)
                    distinct.add(tuple(shape))
        
        return len(distinct)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        grid = json.loads(raw)
        sol = Solution()
        print(sol.numDistinctIslands(grid))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parseGrid(string input) {
    vector<vector<int>> res;
    vector<int> row;
    int cur = 0;
    bool in_num = false;
    int depth = 0;
    for (char c : input) {
        if (c == '[') depth++;
        else if (c == ']') {
            if (in_num) { row.push_back(cur); cur = 0; in_num = false; }
            if (depth == 2 && !row.empty()) { res.push_back(row); row.clear(); }
            depth--;
        } else if (c >= '0' && c <= '9') {
            cur = cur * 10 + (c - '0');
            in_num = true;
        } else if (c == ',') {
            if (in_num) { row.push_back(cur); cur = 0; in_num = false; }
        }
    }
    return res;
}

int main() {
    string input;
    if (getline(cin, input)) {
        vector<vector<int>> grid = parseGrid(input);
        Solution sol;
        cout << sol.numDistinctIslands(grid) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numDistinctIslands(int[][] grid) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            if (input.length() > 2) {
                input = input.substring(1, input.length() - 1);
                List<int[]> gridList = new ArrayList<>();
                int depth = 0, last = 0;
                for (int i = 0; i < input.length(); i++) {
                    if (input.charAt(i) == '[') depth++;
                    else if (input.charAt(i) == ']') {
                        depth--;
                        if (depth == 0) {
                            String rowStr = input.substring(last + 1, i);
                            if (!rowStr.trim().isEmpty()) {
                                String[] parts = rowStr.split(",");
                                int[] row = new int[parts.length];
                                for (int j = 0; j < parts.length; j++) row[j] = Integer.parseInt(parts[j].trim());
                                gridList.add(row);
                            }
                            last = i + 2;
                        }
                    }
                }
                int[][] grid = new int[gridList.size()][];
                for (int i = 0; i < gridList.size(); i++) grid[i] = gridList.get(i);
                Solution sol = new Solution();
                System.out.println(sol.numDistinctIslands(grid));
            } else {
                System.out.println(0);
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} grid
 * @return {number}
 */
var numDistinctIslands = function(grid) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const grid = JSON.parse(input);
    console.log(numDistinctIslands(grid));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

int numDistinctIslands(int** grid, int gridSize, int* gridColSize) {
    // User logic here
    return 0;
}

int main() {
    char input[20000];
    if (fgets(input, sizeof(input), stdin)) {
        int cap = 50, rows = 0;
        int** grid = malloc(cap * sizeof(int*));
        int* colSizes = malloc(cap * sizeof(int));
        int* curRow = NULL;
        int curCap = 0, curSize = 0, val = 0;
        bool inNum = false;
        
        for (int i = 0; input[i]; i++) {
            if (input[i] == '[') {
                curSize = 0; curCap = 50;
                curRow = malloc(curCap * sizeof(int));
            } else if (isdigit(input[i])) {
                val = val * 10 + (input[i] - '0');
                inNum = true;
            } else if (input[i] == ',' || input[i] == ']') {
                if (inNum && curRow) {
                    if (curSize == curCap) { curCap *= 2; curRow = realloc(curRow, curCap * sizeof(int)); }
                    curRow[curSize++] = val;
                    val = 0; inNum = false;
                }
                if (input[i] == ']' && curRow) {
                    if (rows == cap) { cap *= 2; grid = realloc(grid, cap * sizeof(int*)); colSizes = realloc(colSizes, cap * sizeof(int)); }
                    grid[rows] = curRow;
                    colSizes[rows] = curSize;
                    rows++;
                    curRow = NULL;
                }
            }
        }
        // Exclude the outer array brackets parsing empty row at end if any
        int actualRows = rows > 0 ? rows - 1 : 0; 
        if (actualRows > 0) {
            printf("%d\\n", numDistinctIslands(grid, actualRows, colSizes));
        } else {
            printf("0\\n");
        }
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(grid):
        if not grid or not grid[0]: return 0
        from copy import deepcopy
        g = deepcopy(grid)
        m, n = len(g), len(g[0])
        distinct = set()
        def dfs(r, c, r0, c0, shape):
            if 0 <= r < m and 0 <= c < n and g[r][c] == 1:
                g[r][c] = 0
                shape.append((r - r0, c - c0))
                dfs(r + 1, c, r0, c0, shape)
                dfs(r - 1, c, r0, c0, shape)
                dfs(r, c + 1, r0, c0, shape)
                dfs(r, c - 1, r0, c0, shape)
        
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    shape = []
                    dfs(i, j, i, j, shape)
                    distinct.add(tuple(shape))
        return len(distinct)

    test_cases_data = [
        [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
        [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]],
        [[1,1,1],[1,0,1],[1,1,1]],
        [[1]],
        [[0]],
        [[1,1],[1,1],[0,0],[1,1],[1,1]],
        [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]],
        [[1,1,0,1,1],[0,0,0,0,0],[1,1,0,1,1]],
        [[1,0,0],[0,1,0],[0,0,1]],
        [[1,1],[1,0],[0,0],[0,1],[1,1]]
    ]

    test_cases = []
    for i, grid in enumerate(test_cases_data):
        inp = json.dumps(grid)
        out = str(solve(grid))
        is_sample = i < 2
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Hash Table", "Depth-First Search", "Breadth-First Search", "Union Find"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
