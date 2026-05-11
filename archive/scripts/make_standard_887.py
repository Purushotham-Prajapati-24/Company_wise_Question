import json
import os

def generate_json():
    problem_id = 887
    title = "Super Egg Drop"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>887. Super Egg Drop</h3>
<p>You are given <code>k</code> identical eggs and you have access to a building with <code>n</code> floors labeled from <code>1</code> to <code>n</code>.</p>

<p>You know that there exists a floor <code>f</code> where <code>0 &lt;= f &lt;= n</code> such that any egg dropped at a floor higher than <code>f</code> will break, and any egg dropped at or below floor <code>f</code> will not break.</p>

<p>Each move, you may take an unbroken egg and drop it from any floor <code>x</code> (where <code>1 &lt;= x &lt;= n</code>). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.</p>

<p>Return <em>the minimum number of moves that you need to determine with certainty what the value of </em><code>f</code><em> is</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> k = 1, n = 2
<strong>Output:</strong> 2
<strong>Explanation: </strong>
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, we know that f = 2.
Hence, we need at minimum 2 moves to determine with certainty what f is.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> k = 2, n = 6
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> k = 3, n = 14
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= k &lt;= 100</code></li>
    <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two integers k and n, on separate lines or space-separated."
    output_format = "An integer representing the minimum number of moves."

    constraints = [
        "1 <= k <= 100",
        "1 <= n <= 10000"
    ]

    explanation = """This is a classic dynamic programming problem. The question asks for the minimum number of drops in the worst case. Let `dp[m][k]` be the maximum number of floors we can check with `m` moves and `k` eggs.
The recurrence relation is `dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1`:
- If the egg breaks, we can check `dp[m-1][k-1]` floors below.
- If the egg doesn't break, we can check `dp[m-1][k]` floors above.
- Plus the current floor we just dropped from.
We search for the smallest `m` such that `dp[m][k] >= n`."""

    answer = """class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i-1] + 1
        return m"""

    boilerplate = {
        "python": """import sys

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().split()
    if len(raw) >= 2:
        k = int(raw[0])
        n = int(raw[1])
        sol = Solution()
        print(sol.superEggDrop(k, n))""",
        "cpp": """#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int superEggDrop(int k, int n) {
        // User logic here
        return 0;
    }
};

int main() {
    int k, n;
    if (cin >> k >> n) {
        Solution sol;
        cout << sol.superEggDrop(k, n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int superEggDrop(int k, int n) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.superEggDrop(k, n));
        }
    }
}""",
        "javascript": """/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var superEggDrop = function(k, n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    console.log(superEggDrop(parseInt(input[0]), parseInt(input[1])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int superEggDrop(int k, int n) {
    // User logic here
    return 0;
}

int main() {
    int k, n;
    if (scanf("%d %d", &k, &n) == 2) {
        printf("%d\\n", superEggDrop(k, n));
    }
    return 0;
}"""
    }

    def solve(k, n):
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i-1] + 1
        return m

    test_cases_data = [
        (1, 2),
        (2, 6),
        (3, 14),
        (2, 2),
        (2, 1),
        (4, 5000),
        (5, 10000),
        (10, 10000),
        (1, 100),
        (100, 10000)
    ]

    test_cases = []
    for i, (k, n) in enumerate(test_cases_data):
        inp = f"{k}\n{n}"
        out = str(solve(k, n))
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
        "topics": ["Math", "Binary Search", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
