import json
import os

def generate_json():
    problem_id = 2338
    title = "Count Number of Ideal Arrays"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>2338. Count Number of Ideal Arrays</h3>
<p>You are given two integers <code>n</code> and <code>maxValue</code>. An array of length <code>n</code> is <strong>ideal</strong> if the following conditions are met:</p>

<ul>
	<li>Every element <code>arr[i]</code> is an integer from <code>1</code> to <code>maxValue</code>, for <code>0 &lt;= i &lt; n</code>.</li>
	<li>Every element <code>arr[i]</code> is divisible by <code>arr[i - 1]</code> for <code>0 &lt; i &lt; n</code>.</li>
</ul>

<p>Return <em>the number of <strong>distinct</strong> ideal arrays of length</em> <code>n</code>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2, maxValue = 5
<strong>Output:</strong> 10
<strong>Explanation:</strong> The ideal arrays are:
- Arrays starting with 1: [1,1], [1,2], [1,3], [1,4], [1,5] (5 arrays)
- Arrays starting with 2: [2,2], [2,4] (2 arrays)
- Arrays starting with 3: [3,3] (1 array)
- Arrays starting with 4: [4,4] (1 array)
- Arrays starting with 5: [5,5] (1 array)
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, maxValue = 3
<strong>Output:</strong> 11
<strong>Explanation:</strong> The ideal arrays are:
- Arrays starting with 1: [1,1,1,1,1], [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2], [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3] (9 arrays)
- Arrays starting with 2: [2,2,2,2,2] (1 array)
- Arrays starting with 3: [3,3,3,3,3] (1 array)
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= maxValue &lt;= 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "Two integers `n` and `maxValue` provided as `[n, maxValue]` in JSON."
    output_format = "An integer representing the number of distinct ideal arrays modulo 10^9 + 7."

    constraints = [
        "2 <= n <= 10^4",
        "1 <= maxValue <= 10^4"
    ]

    explanation = """To count ideal arrays:
1. Since each element `arr[i]` must be a multiple of `arr[i-1]`, this is equivalent to finding sequences `x1, x2, ..., xn` such that `x1 | x2 | ... | xn`.
2. Factorize each possible value `V` from 1 to `maxValue`. Let `V = p1^a1 * p2^a2 * ...`.
3. For each prime factor `pi` with exponent `ai`, we need to distribute `ai` increments across `n` steps. However, since the sequence must be non-decreasing and each element divides the next, we use stars and bars.
4. Specifically, for each value `v` in the sequence, the exponent of `pi` in `v` must be non-decreasing. If there are `k` distinct values in the sequence (where each value is a multiple of the previous), we can use combinatorics to count the ways to extend this to length `n`.
5. Precompute combinations `C(n-1, k-1)` and use DP or recursion with memoization to find the number of sequences of length up to `log2(maxValue)` where each element strictly divides the next."""

    answer = """from math import comb
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute counts of sequences of length k where each strictly divides next
        # dp[val][length]
        dp = [[0] * 15 for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1
            
        for length in range(1, 14):
            for i in range(1, maxValue + 1):
                if dp[i][length] == 0: continue
                for next_val in range(2 * i, maxValue + 1, i):
                    dp[next_val][length + 1] = (dp[next_val][length + 1] + dp[i][length]) % MOD
                    
        ans = 0
        for length in range(1, 15):
            ways_to_choose_values = sum(dp[i][length] for i in range(1, maxValue + 1)) % MOD
            # Now we need to distribute these length distinct values into an array of size n
            # This is equivalent to choosing (length-1) positions to change values out of (n-1) positions
            ans = (ans + ways_to_choose_values * comb(n - 1, length - 1)) % MOD
            
        return ans"""

    boilerplate = {
        "python": """import sys
import json
from math import comb

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, maxValue = json.loads(raw)
        sol = Solution()
        print(sol.idealArrays(n, maxValue))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int idealArrays(int n, int maxValue) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0], maxValue = j[1];
        Solution sol;
        cout << sol.idealArrays(n, maxValue) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int idealArrays(int n, int maxValue) {
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
            System.out.println(new Solution().idealArrays(data[0], data[1]));
        }
    }
}""",
        "javascript": """var idealArrays = function(n, maxValue) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, maxValue] = JSON.parse(input);
    console.log(idealArrays(n, maxValue));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int idealArrays(int n, int maxValue) {
    // User logic here
    return 0;
}

int main() {
    int n, maxValue;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    if (scanf("%d", &n) == 1) {
        while ((c = getchar()) != EOF && c != ',');
        if (scanf("%d", &maxValue) == 1) {
            printf("%d\\n", idealArrays(n, maxValue));
        }
    }
    return 0;
}"""
    }

    def solve(n, maxValue):
        from math import comb
        MOD = 10**9 + 7
        dp = [[0] * 15 for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1): dp[i][1] = 1
        for length in range(1, 14):
            for i in range(1, maxValue + 1):
                if dp[i][length] == 0: continue
                for next_val in range(2 * i, maxValue + 1, i):
                    dp[next_val][length+1] = (dp[next_val][length+1] + dp[i][length]) % MOD
        ans = 0
        for length in range(1, 15):
            ways = sum(dp[i][length] for i in range(1, maxValue + 1)) % MOD
            ans = (ans + ways * comb(n - 1, length - 1)) % MOD
        return ans

    test_cases_data = [
        [2, 5],      # Sample 1
        [5, 3],      # Sample 2
        [10, 1],     # min val
        [2, 100],    # larger val
        [100, 2],    # larger n
        [1000, 100], 
        [50, 50],
        # Stress tests
        [10000, 10000],
        [10000, 1],
        [2, 10000]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "Dynamic Programming", "Combinatorics", "Number Theory"], "companyIndex": 0
    }

    output_path = f"2301-2500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
