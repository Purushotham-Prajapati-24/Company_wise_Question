import json
import os

def generate_json():
    problem_id = 738
    title = "Monotone Increasing Digits"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>738. Monotone Increasing Digits</h3>
<p>An integer has <strong>monotone increasing digits</strong> if and only if each pair of adjacent digits <code>x</code> and <code>y</code> satisfy <code>x &lt;= y</code>.</p>

<p>Given an integer <code>n</code>, return <em>the largest number that is less than or equal to </em><code>n</code><em> with <strong>monotone increasing digits</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 10
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1234
<strong>Output:</strong> 1234
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 332
<strong>Output:</strong> 299
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single integer `n`."
    output_format = "An integer."

    constraints = [
        "0 <= n <= 10^9"
    ]

    explanation = """Convert the number to an array of digits. Iterate from left to right to find the first drop (where digits[i] > digits[i+1]). From that drop, decrement the current digit and if it becomes smaller than previous ones, propagate the decrement backwards. Finally, set all digits after the decremented one to 9 and reconstruct the number."""

    answer = """class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        maker = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                maker = i
                digits[i - 1] = str(int(digits[i - 1]) - 1)
        
        for i in range(maker, len(digits)):
            digits[i] = '9'
            
        return int("".join(digits))"""

    boilerplate = {
        "python": """import sys

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n = int(raw)
        sol = Solution()
        print(sol.monotoneIncreasingDigits(n))""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        // User logic here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.monotoneIncreasingDigits(n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int monotoneIncreasingDigits(int n) {
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
            System.out.println(sol.monotoneIncreasingDigits(n));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @return {number}
 */
var monotoneIncreasingDigits = function(n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const n = parseInt(input, 10);
    console.log(monotoneIncreasingDigits(n));
}""",
        "c": """#include <stdio.h>

int monotoneIncreasingDigits(int n) {
    // User logic here
    return 0;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", monotoneIncreasingDigits(n));
    }
    return 0;
}"""
    }

    def solve(n):
        digits = list(str(n))
        maker = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                maker = i
                digits[i - 1] = str(int(digits[i - 1]) - 1)
        for i in range(maker, len(digits)):
            digits[i] = '9'
        return int("".join(digits))

    test_cases_data = [
        10,
        1234,
        332,
        0,
        9,
        1111,
        120,
        1000000000,
        987654321,
        138847
    ]

    test_cases = []
    for i, n in enumerate(test_cases_data):
        inp = str(n)
        out = str(solve(n))
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
        "topics": ["Math", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
