import json
import os

def generate_json():
    problem_id = 688
    title = "Knight Probability in Chessboard"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>688. Knight Probability in Chessboard</h3>
<p>On an <code>n x n</code> chessboard, a knight starts at the cell <code>(row, column)</code> and attempts to make exactly <code>k</code> moves. The rows and columns are <strong>0-indexed</strong>, so the top-left cell is <code>(0, 0)</code>, and the bottom-right cell is <code>(n - 1, n - 1)</code>.</p>

<p>A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.</p>

<p>Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.</p>

<p>The knight continues moving until it has made exactly <code>k</code> moves or has moved off the chessboard.</p>

<p>Return <em>the probability that the knight remains on the board after it has stopped moving</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 2, row = 0, column = 0
<strong>Output:</strong> 0.06250
<strong>Explanation:</strong> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1, k = 0, row = 0, column = 0
<strong>Output:</strong> 1.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 25</code></li>
    <li><code>0 &lt;= k &lt;= 100</code></li>
    <li><code>0 &lt;= row, column &lt;= n - 1</code></li>
</ul>"""

    input_format = "Four lines: n, k, row, column (one integer each)."
    output_format = "A float rounded to 5 decimal places."

    constraints = [
        "1 <= n <= 25",
        "0 <= k <= 100",
        "0 <= row, column <= n-1"
    ]

    explanation = """Use dynamic programming. dp[r][c] = probability of being at cell (r,c) after some moves. Start with dp[row][col]=1.0. For each move, spread to all 8 neighbors (if on-board), dividing by 8. After k moves, sum all dp values."""

    answer = """class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        
        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                ndp[nr][nc] += dp[r][c] / 8.0
            dp = ndp
        
        return sum(dp[r][c] for r in range(n) for c in range(n))"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # User logic here
        return 0.0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 4:
        n = int(raw[0])
        k = int(raw[1])
        row = int(raw[2])
        column = int(raw[3])
        sol = Solution()
        print(f"{sol.knightProbability(n, k, row, column):.5f}")""",
        "cpp": """#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double knightProbability(int n, int k, int row, int column) {
        // User logic here
        return 0.0;
    }
};

int main() {
    int n, k, row, column;
    if (cin >> n >> k >> row >> column) {
        Solution sol;
        printf("%.5f\\n", sol.knightProbability(n, k, row, column));
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public double knightProbability(int n, int k, int row, int column) {
        // User logic here
        return 0.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt(), k = sc.nextInt(), row = sc.nextInt(), col = sc.nextInt();
            Solution sol = new Solution();
            System.out.printf("%.5f%n", sol.knightProbability(n, k, row, col));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @param {number} k
 * @param {number} row
 * @param {number} column
 * @return {number}
 */
var knightProbability = function(n, k, row, column) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 4) {
    const n = parseInt(input[0], 10);
    const k = parseInt(input[1], 10);
    const row = parseInt(input[2], 10);
    const column = parseInt(input[3], 10);
    console.log(knightProbability(n, k, row, column).toFixed(5));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

double knightProbability(int n, int k, int row, int column) {
    // User logic here
    return 0.0;
}

int main() {
    int n, k, row, column;
    if (scanf("%d %d %d %d", &n, &k, &row, &column) == 4) {
        printf("%.5f\\n", knightProbability(n, k, row, column));
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(n, k, row, column):
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                ndp[nr][nc] += dp[r][c] / 8.0
            dp = ndp
        return sum(dp[r][c] for r in range(n) for c in range(n))

    test_cases_data = [
        (3, 2, 0, 0),
        (1, 0, 0, 0),
        (8, 5, 4, 4),
        (3, 0, 1, 1),
        (5, 3, 2, 2),
        (25, 50, 12, 12),
        (2, 10, 0, 0),
        (10, 100, 5, 5),
        (4, 4, 2, 2),
        (6, 6, 3, 3)
    ]

    test_cases = []
    for i, (n, k, row, column) in enumerate(test_cases_data):
        inp = f"{n}\\n{k}\\n{row}\\n{column}"
        out = f"{solve(n, k, row, column):.5f}"
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
        "topics": ["Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
