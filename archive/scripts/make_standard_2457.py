import json
import os

def generate_json():
    problem_id = 2457
    title = "Minimum Addition to Make Integer Beautiful"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>2457. Minimum Addition to Make Integer Beautiful</h3>
<p>You are given two positive integers <code>n</code> and <code>target</code>.</p>

<p>An integer is considered <strong>beautiful</strong> if the sum of its digits is less than or equal to <code>target</code>.</p>

<p>Return the minimum <strong>non-negative</strong> integer <code>x</code> such that <code>n + x</code> is beautiful. The input will be generated such that it is always possible to make <code>n</code> beautiful.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 16, target = 6
<strong>Output:</strong> 4
<strong>Explanation:</strong> Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and its digit sum becomes 2 + 0 = 2. It can be shown that 4 is the minimum non-negative integer to make n beautiful.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 467, target = 6
<strong>Output:</strong> 33
<strong>Explanation:</strong> Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and its digit sum becomes 5 + 0 + 0 = 5. It can be shown that 33 is the minimum non-negative integer to make n beautiful.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1, target = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> Initially n is 1 and its digit sum is 1, which is already less than or equal to target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>12</sup></code></li>
	<li><code>1 &lt;= target &lt;= 150</code></li>
	<li>The input will be generated such that it is always possible to make <code>n</code> beautiful.</li>
</ul>
"""

    input_format = "An integer `n` and an integer `target` provided as `[n, target]` in JSON."
    output_format = "A long integer representing the minimum addition `x`."

    constraints = [
        "1 <= n <= 10^12",
        "1 <= target <= 150"
    ]

    explanation = """To find the minimum addition:
1. Calculate the sum of digits of `n`. If it's already <= `target`, return 0.
2. Otherwise, we need to make some suffix of `n` zero to reduce the digit sum.
3. Start from the last digit (units place). Round `n` up to the next multiple of 10, then 100, then 1000, and so on.
4. For each rounding step, recalculate the sum of digits.
5. As soon as the sum of digits of the rounded number is <= `target`, the result is `rounded_n - original_n`."""

    answer = """class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sum_digits(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
            
        if sum_digits(n) <= target: return 0
        
        n0 = n
        mul = 10
        while sum_digits(n) > target:
            # Round n up to next power of 10
            n = (n // mul + 1) * mul
            mul *= 10
        return n - n0"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, target = json.loads(raw)
        sol = Solution()
        print(sol.makeIntegerBeautiful(n, target))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        long long n = j[0];
        int target = j[1];
        Solution sol;
        cout << sol.makeIntegerBeautiful(n, target) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public long makeIntegerBeautiful(long n, int target) {
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
            long n = ((Number) data[0]).longValue();
            int target = (Integer) data[1];
            System.out.println(new Solution().makeIntegerBeautiful(n, target));
        }
    }
}""",
        "javascript": """var makeIntegerBeautiful = function(n, target) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, target] = JSON.parse(input);
    console.log(makeIntegerBeautiful(n, target).toString());
}""",
        "c": """#include <stdio.h>

long long makeIntegerBeautiful(long long n, int target) {
    // User logic here
    return 0;
}

int main() {
    long long n;
    int target;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    if (scanf("%lld", &n) == 1) {
        while ((c = getchar()) != EOF && c != ',');
        if (scanf("%d", &target) == 1) {
            printf("%lld\\n", makeIntegerBeautiful(n, target));
        }
    }
    return 0;
}"""
    }

    def solve(n, target):
        def sd(x): return sum(int(d) for d in str(x))
        if sd(n) <= target: return 0
        n0 = n
        mul = 10
        while sd(n) > target:
            n = (n // mul + 1) * mul
            mul *= 10
        return n - n0

    test_cases_data = [
        [16, 6],           # Sample 1
        [467, 6],          # Sample 2
        [1, 1],            # Sample 3
        [100, 1],          # Already beautiful
        [999, 1],          # Rounding to 1000
        [8, 2],            # Simple round
        [7345047, 10],     # Large
        # Stress tests
        [10**12 - 1, 1],
        [1, 150],
        [10**12 - 7, 5]
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Greedy", "Math"], "companyIndex": 0
    }

    output_path = f"2401-2600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
