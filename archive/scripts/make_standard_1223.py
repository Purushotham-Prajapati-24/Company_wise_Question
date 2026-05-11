import json
import os

def generate_json():
    problem_id = 1223
    title = "Dice Roll Simulation"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1223. Dice Roll Simulation</h3>
<p>A die simulator generates a random number from <code>1</code> to <code>6</code> for each roll. You introduced a constraint to the generator such that it cannot roll the number <code>i</code> more than <code>rollMax[i]</code> (<strong>1-indexed</strong>) consecutive times. </p>

<p>Given an integer array <code>rollMax</code> and an integer <code>n</code>, return <em>the number of distinct sequences that can be obtained with exactly </em><code>n</code><em> rolls</em>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>Two sequences are considered different if at least one element differs from each other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2, rollMax = [1,1,2,2,2,3]
<strong>Output:</strong> 34
<strong>Explanation:</strong> There will be 2 rolls of a die, so there are 6 * 6 = 36 possible sequences. In this case, the sequences (1,1) and (2,2) are invalid, because 1 and 2 can appear at most once consecutively. 36 - 2 = 34.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2, rollMax = [1,1,1,1,1,1]
<strong>Output:</strong> 30
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3, rollMax = [1,1,1,2,2,3]
<strong>Output:</strong> 181
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>rollMax.length == 6</code></li>
	<li><code>1 &lt;= rollMax[i] &lt;= 15</code></li>
</ul>"""

    input_format = "An integer `n` and a JSON array `rollMax` as `[n, rollMax]`."
    output_format = "An integer representing the number of valid sequences modulo 10^9 + 7."

    constraints = [
        "1 <= n <= 5000",
        "rollMax.length == 6",
        "1 <= rollMax[i] <= 15"
    ]

    explanation = """To simulate dice rolls with consecutive limits:
1. Use dynamic programming. Let `dp[i][j][k]` be the number of sequences of length `i` ending with face `j` repeated `k` times.
2. `i` ranges from 1 to `n`, `j` from 0 to 5, and `k` from 1 to `rollMax[j]`.
3. Base case: For length 1, `dp[1][j][1] = 1` for all faces `j`.
4. Transitions: For length `i` from 2 to `n`:
   - If we roll face `j` and it's the same as the last face:
     `dp[i][j][k] = dp[i-1][j][k-1]` for `k > 1`.
   - If we roll face `j` and it's different from the last face:
     `dp[i][j][1] = sum(dp[i-1][other_face][any_k])` for all `other_face != j`.
5. The result is the sum of all `dp[n][j][k]` for all `j, k`.
6. To optimize space, use only the previous length's states."""

    answer = """class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 16 for _ in range(6)]
        for j in range(6):
            dp[j][1] = 1
            
        for _ in range(n - 1):
            new_dp = [[0] * 16 for _ in range(6)]
            total_sum = sum(sum(row) for row in dp) % MOD
            for j in range(6):
                # Different face
                new_dp[j][1] = (total_sum - sum(dp[j])) % MOD
                # Same face
                for k in range(2, rollMax[j] + 1):
                    new_dp[j][k] = dp[j][k - 1]
            dp = new_dp
            
        return sum(sum(row) for row in dp) % MOD"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, rollMax = json.loads(raw)
        sol = Solution()
        print(sol.dieSimulator(n, rollMax))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0];
        vector<int> rollMax = j[1].get<vector<int>>();
        Solution sol;
        cout << sol.dieSimulator(n, rollMax) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int dieSimulator(int n, int[] rollMax) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (Integer) data[0];
            int[] rollMax = mapper.convertValue(data[1], int[].class);
            System.out.println(new Solution().dieSimulator(n, rollMax));
        }
    }
}""",
        "javascript": """var dieSimulator = function(n, rollMax) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [n, rollMax] = JSON.parse(input);
    console.log(dieSimulator(n, rollMax));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int dieSimulator(int n, int* rollMax, int rollMaxSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(n, rollMax):
        MOD = 10**9 + 7
        dp = [[0] * 16 for _ in range(6)]
        for j in range(6):
            dp[j][1] = 1
        for _ in range(n - 1):
            new_dp = [[0] * 16 for _ in range(6)]
            total_sum = sum(sum(row) for row in dp) % MOD
            for j in range(6):
                new_dp[j][1] = (total_sum - sum(dp[j])) % MOD
                for k in range(2, rollMax[j] + 1):
                    new_dp[j][k] = dp[j][k - 1]
            dp = new_dp
        return sum(sum(row) for row in dp) % MOD

    test_cases_data = [
        [2, [1,1,2,2,2,3]], # Sample 1
        [2, [1,1,1,1,1,1]], # Sample 2
        [3, [1,1,1,2,2,3]], # Sample 3
        [1, [1,1,1,1,1,1]], # Simple hit
        [5000, [15,15,15,15,15,15]], # Large n
        [4, [1,1,1,1,1,1]], # Consecutive power
        [5, [2,2,2,2,2,2]],
        # Stress tests
        [5000, [1,1,1,1,1,1]],
        [100, [1,2,3,4,5,6]],
        [100, [15,1,15,1,15,1]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Dynamic Programming"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
