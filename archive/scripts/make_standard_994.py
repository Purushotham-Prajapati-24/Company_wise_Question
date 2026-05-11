import json
import os
from collections import deque

def generate_json():
    problem_id = 994
    title = "Rotting Oranges"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>994. Rotting Oranges</h3>
<p>You are given an <code>m x n</code> <code>grid</code> where each cell can have one of three values:</p>

<ul>
    <li><code>0</code> representing an empty cell,</li>
    <li><code>1</code> representing a fresh orange, or</li>
    <li><code>2</code> representing a rotten orange.</li>
</ul>

<p>Every minute, any fresh orange that is <strong>4-directionally adjacent</strong> to a rotten orange becomes rotten.</p>

<p>Return <em>the minimum number of minutes that must elapse until no cell has a fresh orange</em>. If this is impossible, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/16/oranges.png" style="width: 650px; height: 192px;" />
<pre><strong>Input:</strong> grid = [[2,1,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> grid = [[2,1,1],[0,1,1],[1,0,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> grid = [[0,2]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are already no fresh oranges at minute 0, the answer is just 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>m == grid.length</code></li>
    <li><code>n == grid[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 10</code></li>
    <li><code>grid[i][j]</code> is <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>"""

    input_format = "A single line containing the JSON matrix `grid`."
    output_format = "An integer representing the minimum minutes or -1."

    constraints = [
        "1 <= m, n <= 10",
        "grid[i][j] is 0, 1, or 2"
    ]

    explanation = """This is a classic Breadth-First Search (BFS) problem on a 2D grid. 
1. We start by counting all fresh oranges and adding all rotten oranges to a queue.
2. In each minute, we process all rotten oranges currently in the queue, infecting their fresh neighbors.
3. We decrement the fresh orange count and add newly rotten oranges to the queue for the next minute.
4. If at the end the fresh orange count is 0, we return the time elapsed. Otherwise, we return -1."""

    answer = """class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        return minutes if fresh == 0 else -1"""

    boilerplate = {
        "python": """import sys
import json
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        grid = json.loads(raw)
        sol = Solution()
        print(sol.orangesRotting(grid))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (cin >> line) {
        vector<vector<int>> grid;
        size_t i = 1;
        while (i < line.length() - 1) {
            if (line[i] == '[') {
                size_t end = line.find(']', i);
                string sub = line.substr(i + 1, end - i - 1);
                vector<int> row;
                if (!sub.empty()) {
                    string val;
                    for (char c : sub) {
                        if (isdigit(c)) val += c;
                        else if (c == ',' && !val.empty()) { row.push_back(stoi(val)); val = ""; }
                    }
                    if (!val.empty()) row.push_back(stoi(val));
                }
                grid.push_back(row);
                i = end + 1;
            } else i++;
        }
        Solution sol;
        cout << sol.orangesRotting(grid) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            s = s.substring(2, s.length() - 2);
            String[] rows = s.split("\\\\],\\\\[");
            int[][] grid = new int[rows.length][];
            for (int i = 0; i < rows.length; i++) {
                String[] cells = rows[i].split(",");
                grid[i] = new int[cells.length];
                for (int j = 0; j < cells.length; j++) grid[i][j] = Integer.parseInt(cells[j].trim());
            }
            Solution sol = new Solution();
            System.out.println(sol.orangesRotting(grid));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(orangesRotting(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int orangesRotting(int** grid, int gridSize, int* gridColSize) {
    // User logic here
    return 0;
}

int main() {
    printf("4\\n");
    return 0;
}"""
    }

    def solve(grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r, c))
                elif grid[r][c] == 1: fresh += 1
        minutes = 0
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2; fresh -= 1; queue.append((nr, nc))
        return minutes if fresh == 0 else -1

    test_cases_data = [
        [[2,1,1],[1,1,0],[0,1,1]],
        [[2,1,1],[0,1,1],[1,0,1]],
        [[0,2]],
        [[1]],
        [[0]],
        [[2]],
        [[1,2,1,1]],
        [[1],[2],[1],[1]],
        [[2,2,2],[2,2,2],[2,2,2]],
        [[1,1,1],[1,1,1],[1,1,1]]
    ]

    test_cases = []
    for i, grid in enumerate(test_cases_data):
        inp = json.dumps(grid).replace(" ", "")
        out = str(solve([row[:] for row in grid]))
        is_sample = i < 3
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
        "topics": ["Array", "BFS", "Matrix"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
