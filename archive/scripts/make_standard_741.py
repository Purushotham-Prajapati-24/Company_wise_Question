import json
import os

def generate_json():
    problem_id = 741
    title = "Cherry Pickup"
    difficulty = "HARD"
    marks = 15

    html_description = """<h3>741. Cherry Pickup</h3>
<p>You are given an <code>n x n</code> <code>grid</code> representing a field of cherries, each cell is one of three possible integers.</p>

<ul>
    <li><code>0</code> means the cell is empty, so you can pass through,</li>
    <li><code>1</code> means the cell contains a cherry that you can pick up and pass through, or</li>
    <li><code>-1</code> means the cell contains a thorn that blocks your way.</li>
</ul>

<p>Return <em>the maximum number of cherries you can collect by following the rules below</em>:</p>

<ul>
    <li>Starting at position <code>(0, 0)</code> and reaching <code>(n - 1, n - 1)</code> by moving right or down through valid path cells (cells with value <code>0</code> or <code>1</code>).</li>
    <li>After reaching <code>(n - 1, n - 1)</code>, returning to <code>(0, 0)</code> by moving left or up through valid path cells.</li>
    <li>When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell <code>0</code>.</li>
    <li>If there is no valid path between <code>(0, 0)</code> and <code>(n - 1, n - 1)</code>, then no cherries can be collected.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> grid = [[0,1,-1],[1,0,-1],[1,1,1]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == grid.length</code></li>
    <li><code>n == grid[i].length</code></li>
    <li><code>1 &lt;= n &lt;= 50</code></li>
    <li><code>grid[i][j]</code> is <code>-1</code>, <code>0</code>, or <code>1</code>.</li>
    <li><code>grid[0][0] != -1</code></li>
    <li><code>grid[n - 1][n - 1] != -1</code></li>
</ul>"""

    input_format = "A single line containing the 2D JSON array `grid`."
    output_format = "An integer representing the maximum cherries."

    constraints = [
        "1 <= n <= 50",
        "grid[i][j] in {-1, 0, 1}"
    ]

    explanation = """Instead of doing a round trip, we can imagine two people starting from (0,0) and trying to reach (n-1,n-1) simultaneously. Both persons take `t` steps where `r + c = t`. Let DP state be `dp(r1, c1, c2)` representing the max cherries collected if person 1 is at `(r1, c1)` and person 2 is at `(r2 = r1 + c1 - c2, c2)`. Since they move simultaneously, if they land on the same cell, the cherry is only collected once. Use a bottom-up DP to avoid recursion depth issues or memoized recursion."""

    answer = """class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = [[-float('inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        for t in range(1, 2 * n - 1):
            next_dp = [[-float('inf')] * n for _ in range(n)]
            # i is r1, j is r2
            for i in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                for j in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                    # Person 1 at (i, t-i), Person 2 at (j, t-j)
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    
                    val = grid[i][t - i]
                    if i != j:
                        val += grid[j][t - j]
                        
                    next_dp[i][j] = val + max(
                        dp[i][j],          # right, right
                        dp[i-1][j] if i > 0 else -float('inf'),        # down, right
                        dp[i][j-1] if j > 0 else -float('inf'),        # right, down
                        dp[i-1][j-1] if i > 0 and j > 0 else -float('inf')     # down, down
                    )
            dp = next_dp
            
        return max(0, dp[n - 1][n - 1])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        grid = json.loads(raw)
        sol = Solution()
        print(sol.cherryPickup(grid))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parse2DArray(string input) {
    vector<vector<int>> res;
    size_t i = 1;
    while (i < input.length() - 1) {
        if (input[i] == '[') {
            vector<int> row;
            i++;
            while (input[i] != ']') {
                if (input[i] == '-' || isdigit(input[i])) {
                    int sign = 1, val = 0;
                    if (input[i] == '-') { sign = -1; i++; }
                    while (isdigit(input[i])) { val = val * 10 + (input[i] - '0'); i++; }
                    row.push_back(val * sign);
                } else {
                    i++;
                }
            }
            res.push_back(row);
            i++;
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string input;
    if (getline(cin, input)) {
        vector<vector<int>> grid = parse2DArray(input);
        Solution sol;
        cout << sol.cherryPickup(grid) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int cherryPickup(int[][] grid) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[][] parse2DArray(String raw) {
        // Simple manual parsing
        raw = raw.trim();
        if (raw.length() < 2) return new int[0][0];
        raw = raw.substring(1, raw.length() - 1).trim();
        if (raw.isEmpty()) return new int[0][0];
        
        List<int[]> resList = new ArrayList<>();
        int i = 0;
        while (i < raw.length()) {
            if (raw.charAt(i) == '[') {
                int j = i;
                while (raw.charAt(j) != ']') j++;
                String rowStr = raw.substring(i + 1, j);
                if (rowStr.trim().isEmpty()) {
                    resList.add(new int[0]);
                } else {
                    String[] parts = rowStr.split(",");
                    int[] row = new int[parts.length];
                    for (int k = 0; k < parts.length; k++) {
                        row[k] = Integer.parseInt(parts[k].trim());
                    }
                    resList.add(row);
                }
                i = j + 1;
            } else {
                i++;
            }
        }
        int[][] res = new int[resList.size()][];
        for (int k = 0; k < resList.size(); k++) res[k] = resList.get(k);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            int[][] grid = parse2DArray(input);
            Solution sol = new Solution();
            System.out.println(sol.cherryPickup(grid));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} grid
 * @return {number}
 */
var cherryPickup = function(grid) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const grid = JSON.parse(input);
    console.log(cherryPickup(grid));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int cherryPickup(int** grid, int gridSize, int* gridColSize) {
    // User logic here
    return 0;
}

int** parse2DArray(char* input, int* outSize, int** outColSizes) {
    int cap = 10, size = 0, i = 0;
    int** res = (int**)malloc(cap * sizeof(int*));
    int* cols = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '[') {
            i++;
            if (input[i] == '[') continue;
            int rcap = 10, csize = 0;
            int* row = (int*)malloc(rcap * sizeof(int));
            while (input[i] && input[i] != ']') {
                if (input[i] == '-' || isdigit(input[i])) {
                    int val, off = 0;
                    sscanf(input+i, "%d%n", &val, &off);
                    if (!off) { i++; continue; }
                    if (csize == rcap) { rcap *= 2; row = realloc(row, rcap * sizeof(int)); }
                    row[csize++] = val;
                    i += off;
                } else {
                    i++;
                }
            }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int*)); cols = realloc(cols, cap * sizeof(int)); }
            res[size] = row;
            cols[size++] = csize;
        }
        i++;
    }
    *outSize = size;
    *outColSizes = cols;
    return res;
}

int main() {
    char input[50000];
    if (fgets(input, sizeof(input), stdin)) {
        int gridSize;
        int* colSizes;
        int** grid = parse2DArray(input, &gridSize, &colSizes);
        printf("%d\\n", cherryPickup(grid, gridSize, colSizes));
        for(int i=0; i<gridSize; i++) free(grid[i]);
        free(grid);
        free(colSizes);
    }
    return 0;
}"""
    }

    def solve(grid):
        n = len(grid)
        dp = [[-float('inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        for t in range(1, 2 * n - 1):
            next_dp = [[-float('inf')] * n for _ in range(n)]
            for i in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                for j in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    val = grid[i][t - i]
                    if i != j:
                        val += grid[j][t - j]
                    next_dp[i][j] = val + max(
                        dp[i][j],
                        dp[i-1][j] if i > 0 else -float('inf'),
                        dp[i][j-1] if j > 0 else -float('inf'),
                        dp[i-1][j-1] if i > 0 and j > 0 else -float('inf')
                    )
            dp = next_dp
        return max(0, dp[n - 1][n - 1])

    test_cases_data = [
        [[0,1,-1],[1,0,-1],[1,1,1]],
        [[1,1,-1],[1,-1,1],[-1,1,1]],
        [[1]],
        [[0,0],[0,0]],
        [[1,1],[1,1]],
        [[1,-1,-1],[-1,-1,-1],[-1,-1,1]],
        [[0,1,0,0,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,1,0],[1,1,1,1,1]],
        [[1 for _ in range(50)] for _ in range(50)],
        [[(1 if (i+j)%2==0 else 0) for j in range(50)] for i in range(50)],
        [[(0 if i==j else 1) for j in range(50)] for i in range(50)]
    ]

    test_cases = []
    for i, grid in enumerate(test_cases_data):
        inp = json.dumps(grid).replace(" ", "")
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
        "topics": ["Array", "Dynamic Programming", "Matrix"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
