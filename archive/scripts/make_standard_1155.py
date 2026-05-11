import json
import os

def generate_json():
    problem_id = 1155
    title = "Number of Dice Rolls With Target Sum"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1155. Number of Dice Rolls With Target Sum</h3>
<p>You have <code>n</code> dice, and each die has <code>k</code> faces numbered from <code>1</code> to <code>k</code>.</p>

<p>Given three integers <code>n</code>, <code>k</code>, and <code>target</code>, return <em>the number of possible ways (out of the </em><code>k<sup>n</sup></code><em> total ways) </em><em>to roll the dice, so the sum of the face-up numbers equals </em><code>target</code>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 6, target = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> You throw one die with 6 faces. There is only one way to get a sum of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 6, target = 7
<strong>Output:</strong> 6
<strong>Explanation:</strong> You throw two dice, each with 6 faces. There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 30, k = 30, target = 500
<strong>Output:</strong> 222616187
<strong>Explanation:</strong> The answer must be returned modulo 10<sup>9</sup> + 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 30</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>
"""

    input_format = "Three integers `n`, `k`, and `target` provided as `[n, k, target]` in JSON."
    output_format = "An integer representing the number of ways modulo 10^9 + 7."

    constraints = [
        "1 <= n, k <= 30",
        "1 <= target <= 1000"
    ]

    explanation = """To solve this using Dynamic Programming:
1. Define `dp[i][j]` as the number of ways to get a sum `j` using `i` dice.
2. Base case: `dp[0][0] = 1` (zero dice, zero sum).
3. Transition: For `i` from 1 to `n` and `j` from 1 to `target`:
   - `dp[i][j] = sum(dp[i-1][j-f])` where `1 <= f <= k` and `j-f >= 0`.
4. The answer is `dp[n][target] % (10^9 + 7)`.
5. Optimize space to `O(target)` using a 1D array."""

    answer = """class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            new_dp = [0] * (target + 1)
            for j in range(target + 1):
                if dp[j]:
                    for f in range(1, k + 1):
                        if j + f <= target:
                            new_dp[j+f] = (new_dp[j+f] + dp[j]) % MOD
            dp = new_dp
        return dp[target]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        data = json.loads(raw)
        n, k, target = data
        sol = Solution()
        print(sol.numRollsToTarget(n, k, target))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        int n = j[0].get<int>();
        int k = j[1].get<int>();
        int t = j[2].get<int>();
        Solution sol;
        cout << sol.numRollsToTarget(n, k, t) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            int[] data = mapper.readValue(sc.nextLine(), int[].class);
            System.out.println(new Solution().numRollsToTarget(data[0], data[1], data[2]));
        }
    }
}""",
        "javascript": """var numRollsToTarget = function(n, k, target) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, k, target] = JSON.parse(input);
    console.log(numRollsToTarget(n, k, target));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int numRollsToTarget(int n, int k, int target) {
    // User logic here
    return 0;
}

int main() {
    int n, k, t;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    if (scanf("%d", &n) != 1) return 0;
    while ((c = getchar()) != EOF && c != ',');
    if (scanf("%d", &k) != 1) return 0;
    while ((c = getchar()) != EOF && c != ',');
    if (scanf("%d", &t) != 1) return 0;
    printf("%d\\n", numRollsToTarget(n, k, t));
    return 0;
}"""
    }

    def solve(n, k, target):
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            new_dp = [0] * (target + 1)
            for j in range(target + 1):
                if dp[j]:
                    for f in range(1, k + 1):
                        if j + f <= target:
                            new_dp[j+f] = (new_dp[j+f] + dp[j]) % MOD
            dp = new_dp
        return dp[target]

    test_cases_data = [
        [1, 6, 3],      # Sample 1
        [2, 6, 7],      # Sample 2
        [30, 30, 500],  # Sample 3
        [1, 1, 1],
        [2, 5, 10],     # Exactly 1 way (5+5)
        [3, 2, 6],      # Exactly 1 way (2+2+2)
        [2, 6, 12],     # Max sum for 2 dice
        # Stress tests
        [30, 30, 1000],
        [30, 10, 300],
        [30, 1, 30]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Dynamic Programming"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
