import json
import os

def generate_json():
    problem_id = 991
    title = "Broken Calculator"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>991. Broken Calculator</h3>
<p>There is a broken calculator that has the decimal display and only two buttons on it:</p>

<ul>
    <li><strong>Double:</strong> Multiplies the number on the display by 2, or</li>
    <li><strong>Decrement:</strong> Subtracts 1 from the number on the display.</li>
</ul>

<p>Initially, the calculator displays the integer <code>startValue</code>.</p>

<p>Return <em>the minimum number of operations needed to display the integer <code>target</code></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> startValue = 2, target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Use double operation and then decrement operation {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> startValue = 5, target = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> Use decrement and then double {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> startValue = 3, target = 10
<strong>Output:</strong> 3
<strong>Explanation:</strong> Use double, decrement and double {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= startValue, target &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing two integers: `startValue` and `target`."
    output_format = "An integer representing the minimum number of operations."

    constraints = [
        "1 <= startValue, target <= 10^9"
    ]

    explanation = """Instead of trying to reach `target` from `startValue`, it's easier to work backwards from `target` to `startValue`.
1. If `target` is greater than `startValue`:
   - If `target` is odd, we must have come from `target + 1` (decrement button backwards is increment).
   - If `target` is even, we could have come from `target / 2` (double button backwards is divide by 2). This is always better than incrementing twice.
2. If `target` is less than or equal to `startValue`, the only way to reach it is by decrementing `startValue - target` times."""

    answer = """class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target > startValue:
            count += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        return count + (startValue - target)"""

    boilerplate = {
        "python": """import sys

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    data = sys.stdin.read().split()
    if len(data) >= 2:
        startValue = int(data[0])
        target = int(data[1])
        sol = Solution()
        print(sol.brokenCalc(startValue, target))""",
        "cpp": """#include <iostream>

using namespace std;

class Solution {
public:
    int brokenCalc(int startValue, int target) {
        // User logic here
        return 0;
    }
};

int main() {
    int startValue, target;
    if (cin >> startValue >> target) {
        Solution sol;
        cout << sol.brokenCalc(startValue, target) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int brokenCalc(int startValue, int target) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int startValue = sc.nextInt();
            int target = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.brokenCalc(startValue, target));
        }
    }
}""",
        "javascript": """/**
 * @param {number} startValue
 * @param {number} target
 * @return {number}
 */
var brokenCalc = function(startValue, target) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    console.log(brokenCalc(parseInt(input[0]), parseInt(input[1])));
}""",
        "c": """#include <stdio.h>

int brokenCalc(int startValue, int target) {
    // User logic here
    return 0;
}

int main() {
    int s, t;
    if (scanf("%d %d", &s, &t) == 2) {
        printf("%d\\n", brokenCalc(s, t));
    }
    return 0;
}"""
    }

    def solve(s, t):
        ans = 0
        while t > s:
            ans += 1
            if t % 2 == 1: t += 1
            else: t //= 2
        return ans + s - t

    test_cases_data = [
        (2, 3),
        (5, 8),
        (3, 10),
        (1024, 1),
        (1, 1000000000),
        (100, 100),
        (10, 21),
        (1, 10),
        (3, 11),
        (1, 1)
    ]

    test_cases = []
    for i, (s, t) in enumerate(test_cases_data):
        inp = f"{s} {t}"
        out = str(solve(s, t))
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
        "topics": ["Math", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
