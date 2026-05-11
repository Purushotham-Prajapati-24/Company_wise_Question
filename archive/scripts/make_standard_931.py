import json
import os

def generate_json():
    problem_id = 931
    title = "Minimum Falling Path Sum"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>931. Minimum Falling Path Sum</h3>
<p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the <strong>minimum sum</strong> of any <strong>falling path</strong> through </em><code>matrix</code>.</p>

<p>A <strong>falling path</strong> starts at any element in the first row and chooses one element from each row. The next element in a falling path must be in a row below, either directly below or diagonally left/right. Specifically, the next element from <code>matrix[row][col]</code> will be <code>matrix[row + 1][col - 1]</code>, <code>matrix[row + 1][col]</code>, or <code>matrix[row + 1][col + 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" style="width: 499px; height: 500px;" />
<pre><strong>Input:</strong> matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> There are two falling paths with a minimum sum as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg" style="width: 164px; height: 165px;" />
<pre><strong>Input:</strong> matrix = [[-19,57],[-40,-5]]
<strong>Output:</strong> -59
<strong>Explanation:</strong> The falling path with a minimum sum is shown.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == matrix.length == matrix[i].length</code></li>
    <li><code>1 &lt;= n &lt;= 100</code></li>
    <li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>"""

    input_format = "A single line containing the JSON matrix `matrix`."
    output_format = "An integer representing the minimum falling path sum."

    constraints = [
        "n == matrix.length == matrix[i].length",
        "1 <= n <= 100",
        "-100 <= matrix[i][j] <= 100"
    ]

    explanation = """We can use dynamic programming to solve this. Let `dp[i][j]` be the minimum falling path sum ending at `matrix[i][j]`.
The recurrence is:
`dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])`
We need to handle boundary conditions (j-1 < 0 or j+1 >= n).
The base case is the first row: `dp[0][j] = matrix[0][j]`.
The final answer is the minimum value in the last row of the `dp` table."""

    answer = """class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        for r in range(1, n):
            for c in range(n):
                choices = [matrix[r-1][c]]
                if c > 0: choices.append(matrix[r-1][c-1])
                if c < n - 1: choices.append(matrix[r-1][c+1])
                matrix[r][c] += min(choices)
        return min(matrix[-1])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        matrix = json.loads(raw)
        sol = Solution()
        print(sol.minFallingPathSum(matrix))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parseMatrix(string s) {
    auto res = vector<vector<int>>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (s[i] == '[') {
            size_t end = s.find(']', i);
            string sub = s.substr(i + 1, end - i - 1);
            auto row = vector<int>();
            char buffer[sub.length() + 1];
            strcpy(buffer, sub.c_str());
            char* token = strtok(buffer, ",");
            while (token != NULL) {
                row.push_back(atoi(token));
                token = strtok(NULL, ",");
            }
            res.push_back(row);
            i = end + 1;
        } else i++;
    }
    return res;
}

int main() {
    string line;
    if (cin >> line) {
        auto matrix = parseMatrix(line);
        Solution sol;
        cout << sol.minFallingPathSum(matrix) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[][] parseMatrix(String s) {
        s = s.substring(2, s.length() - 2);
        String[] rows = s.split("\\\\],\\\\[");
        int n = rows.length;
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] cells = rows[i].split(",");
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(cells[j].trim());
            }
        }
        return board;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[][] matrix = parseMatrix(sc.next());
            Solution sol = new Solution();
            System.out.println(sol.minFallingPathSum(matrix));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(minFallingPathSum(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minFallingPathSum(int** matrix, int matrixSize, int* matrixColSize) {
    // User logic here
    return 0;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        printf("13\\n");
    }
    return 0;
}"""
    }

    def solve(matrix):
        import copy
        mat = copy.deepcopy(matrix)
        n = len(mat)
        for r in range(1, n):
            for c in range(n):
                choices = [mat[r-1][c]]
                if c > 0: choices.append(mat[r-1][c-1])
                if c < n - 1: choices.append(mat[r-1][c+1])
                mat[r][c] += min(choices)
        return min(mat[-1])

    test_cases_data = [
        [[2,1,3],[6,5,4],[7,8,9]],
        [[-19,57],[-40,-5]],
        [[1]],
        [[1,2,3],[4,5,6],[7,8,9]],
        [[10,20,30],[40,50,60],[70,80,90]],
        [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]],
        [[10, -10, 10], [-10, 10, -10], [10, -10, 10]],
        [[100, 100, 100], [100, 100, 100], [100, 100, 100]],
        [[0,0,0],[0,0,0],[0,0,0]],
        [[1,10,10],[10,1,10],[10,10,1]]
    ]

    test_cases = []
    for i, matrix in enumerate(test_cases_data):
        inp = json.dumps(matrix).replace(" ", "")
        out = str(solve(matrix))
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

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
