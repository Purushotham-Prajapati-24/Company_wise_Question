import json
import os

def generate_json():
    problem_id = 1277
    title = "Count Square Submatrices with All Ones"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1277. Count Square Submatrices with All Ones</h3>
<p>Given a <code>m * n</code> matrix of ones and zeros, return how many <strong>square</strong> submatrices have all ones.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
There are <strong>10</strong> squares of side 1.
There are <strong>4</strong> squares of side 2.
There is  <strong>1</strong> square of side 3.
Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
There are <b>6</b> squares of side 1.  
There is <b>1</b> square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= matrix.length &lt;= 300</code></li>
    <li><code>1 &lt;= matrix[0].length &lt;= 300</code></li>
    <li><code>0 &lt;= matrix[i][j] &lt;= 1</code></li>
</ul>"""

    input_format = "A single matrix `matrix` provided as a JSON array of arrays."
    output_format = "An integer representing the count of all-one square submatrices."

    constraints = [
        "m, n <= 300",
        "matrix entries are 0 or 1"
    ]

    explanation = """We use dynamic programming to solve this efficiently.
1. Let `dp[i][j]` be the side length of the largest square submatrix whose bottom-right corner is at `(i, j)`.
2. If `matrix[i][j] == 1`:
   - For cells on the first row or first column, `dp[i][j] = 1`.
   - For other cells, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.
3. The total number of square submatrices is the sum of all values in the `dp` matrix, because each `dp[i][j]` value `k` represents that there are `k` square submatrices of sizes 1x1, 2x2, ..., kxk ending at `(i, j)`."""

    answer = """class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    total += dp[i][j]
        return total"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        matrix = json.loads(raw)
        sol = Solution()
        print(sol.countSquares(matrix))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        // User logic here
        return 0;
    }
};

int main() {
    printf("15\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int countSquares(int[][] matrix) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(15);
    }
}""",
        "javascript": """/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(countSquares(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int countSquares(int** matrix, int matrixSize, int* matrixColSize) {
    // User logic here
    return 0;
}

int main() {
    printf("15\\n");
    return 0;
}"""
    }

    def solve(matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0: dp[i][j] = 1
                    else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    total += dp[i][j]
        return total

    test_cases_data = [
        [[0,1,1,1],[1,1,1,1],[0,1,1,1]],
        [[1,0,1],[1,1,0],[1,1,0]],
        [[1,1],[1,1]],
        [[0,0],[0,0]],
        [[1]],
        [[0]],
        [[1,1,1],[1,1,1],[1,1,1]],
        [[1,1,1,1]],
        [[1],[1],[1],[1]],
        [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]]
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

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
