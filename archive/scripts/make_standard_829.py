import json
import os
import math

def generate_json():
    problem_id = 829
    title = "Consecutive Numbers Sum"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>829. Consecutive Numbers Sum</h3>
<p>Given an integer <code>n</code>, return <em>the number of ways you can write </em><code>n</code><em> as the sum of consecutive positive integers.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 = 2 + 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 9
<strong>Output:</strong> 3
<strong>Explanation:</strong> 9 = 4 + 5 = 2 + 3 + 4
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> 4
<strong>Explanation:</strong> 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing the integer `n`."
    output_format = "An integer representing the number of ways."

    constraints = [
        "1 <= n <= 10^9"
    ]

    explanation = """A sum of `k` consecutive integers starting from `x` is `x + (x+1) + ... + (x+k-1) = kx + k(k-1)/2`. We need this to equal `n`. So `kx = n - k(k-1)/2`. For a valid `x > 0`, we need `n - k(k-1)/2 > 0` and `(n - k(k-1)/2) % k == 0`. We iterate through possible values of `k` starting from 1 until reaching the limit where `k(k-1)/2 >= n`."""

    answer = """class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        upper_limit = int(math.sqrt(2 * n + 0.25) - 0.5)
        for k in range(1, upper_limit + 1):
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1
        return count"""

    boilerplate = {
        "python": """import sys
import json
import math

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n = int(raw)
        sol = Solution()
        print(sol.consecutiveNumbersSum(n))""",
        "cpp": """#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    int consecutiveNumbersSum(int n) {
        // User logic here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.consecutiveNumbersSum(n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int consecutiveNumbersSum(int n) {
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
            System.out.println(sol.consecutiveNumbersSum(n));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @return {number}
 */
var consecutiveNumbersSum = function(n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(consecutiveNumbersSum(parseInt(input)));
}""",
        "c": """#include <stdio.h>
#include <math.h>

int consecutiveNumbersSum(int n) {
    // User logic here
    return 0;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", consecutiveNumbersSum(n));
    }
    return 0;
}"""
    }

    def solve(n):
        count = 0
        k = 1
        while True:
            sub = k * (k - 1) // 2
            if sub >= n: break
            if (n - sub) % k == 0:
                count += 1
            k += 1
        return count

    test_cases_data = [
        5, 9, 15, 1, 3, 100, 1000, 10**6, 10**9, 2
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
        "topics": ["Math", "Enumeration"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
