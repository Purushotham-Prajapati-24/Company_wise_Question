import json
import os

def generate_json():
    problem_id = 935
    title = "Knight Dialer"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>935. Knight Dialer</h3>
<p>The chess knight has a <strong>unique movement</strong>, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an <strong>L</strong>). The possible movements of chess knight are shown in this diagaram:</p>

<p>A chess knight can move as indicated in the chess board below:</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0935.Knight%20Dialer/images/chess.jpg" style="width: 402px; height: 402px;" />

<p>We have a chess knight and a phone pad as shown below, the knight <strong>can only stand on a numeric cell</strong> (i.e. blue cell).</p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0900-0999/0935.Knight%20Dialer/images/phone.jpg" style="width: 242px; height: 322px;" />

<p>Given an integer <code>n</code>, return how many distinct phone numbers of length <code>n</code> we can dial.</p>

<p>You are allowed to place the knight on <strong>any numeric cell</strong> initially and then you should perform <code>n - 1</code> jumps to dial a number of length <code>n</code>. All jumps should be <strong>valid knight jumps</strong>.</p>

<p>As the answer may be very large, <strong>return the answer modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 10
<strong>Explanation:</strong> All the valid number of length 1 are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 20
<strong>Explanation:</strong> All the valid number of length 2 are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3131
<strong>Output:</strong> 136006598
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 5000</code></li>
</ul>"""

    input_format = "A single integer `n`."
    output_format = "An integer representing the count modulo 10^9 + 7."

    constraints = [
        "1 <= n <= 5000"
    ]

    explanation = """This problem can be solved using dynamic programming. For each digit 0-9, we define the set of digits it can reach in one knight jump. 
Let `dp[i][j]` be the number of ways to dial a phone number of length `i` ending with digit `j`.
The recurrence is: `dp[i][j] = sum(dp[i-1][k])` where `k` is a digit that can reach `j`.
Base case: `dp[1][j] = 1` for all `j \in [0, 9]`.
Final result: `sum(dp[n][j]) % (10^9 + 7)`."""

    answer = """class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        dp = [1] * 10
        for _ in range(n - 1):
            new_dp = [0] * 10
            for i in range(10):
                for move in moves[i]:
                    new_dp[move] = (new_dp[move] + dp[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD"""

    boilerplate = {
        "python": """import sys

class Solution:
    def knightDialer(self, n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n = int(raw)
        sol = Solution()
        print(sol.knightDialer(n))""",
        "cpp": """#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int knightDialer(int n) {
        // User logic here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.knightDialer(n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int knightDialer(int n) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.knightDialer(n));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @return {number}
 */
var knightDialer = function(n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(knightDialer(parseInt(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int knightDialer(int n) {
    // User logic here
    return 0;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", knightDialer(n));
    }
    return 0;
}"""
    }

    def solve(n):
        if n == 1: return 10
        MOD = 10**9 + 7
        moves = {
            0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
            5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
        }
        dp = [1] * 10
        for _ in range(n - 1):
            new_dp = [0] * 10
            for i in range(10):
                for move in moves[i]:
                    new_dp[move] = (new_dp[move] + dp[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD

    test_cases_data = [
        1, 2, 3, 4, 10, 50, 100, 500, 1000, 3131
    ]

    test_cases = []
    for i, n in enumerate(test_cases_data):
        inp = str(n)
        out = str(solve(n))
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
        "topics": ["Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
