import json
import os

def generate_json():
    problem_id = 779
    title = "K-th Symbol in Grammar"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>779. K-th Symbol in Grammar</h3>
<p>We build a table of <code>n</code> rows (<strong>1-indexed</strong>). We start by writing <code>0</code> in the <code>1<sup>st</sup></code> row. Now in every subsequent row, we look at the previous row and replace each occurrence of <code>0</code> with <code>01</code>, and each occurrence of <code>1</code> with <code>10</code>.</p>

<ul>
    <li>For example, for <code>n = 3</code>, the <code>1<sup>st</sup></code> row is <code>0</code>, the <code>2<sup>nd</sup></code> row is <code>01</code>, and the <code>3<sup>rd</sup></code> row is <code>0110</code>.</li>
</ul>

<p>Given two integer <code>n</code> and <code>k</code>, return the <code>k<sup>th</sup></code> (<strong>1-indexed</strong>) symbol in the <code>n<sup>th</sup></code> row of a table of <code>n</code> rows.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> row 1: <u>0</u>
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2, k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
row 1: 0
row 2: <u>0</u>1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 2, k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
row 1: 0
row 2: 0<u>1</u>
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 30</code></li>
    <li><code>1 &lt;= k &lt;= 2<sup>n - 1</sup></code></li>
</ul>"""

    input_format = "Two integers `n` and `k` separated by a space."
    output_format = "An integer: `0` or `1`."

    constraints = [
        "1 <= n <= 30",
        "1 <= k <= 2^(n-1)"
    ]

    explanation = """The second half of any row is just the inverted version of the first half. By determining which half `k` falls into, we can recursively find the relative symbol's position in the previous row, and flip it if it was located in the second half."""

    answer = """class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        mid = 2 ** (n - 2)
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)"""

    boilerplate = {
        "python": """import sys

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().split()
    if len(raw) >= 2:
        n = int(raw[0])
        k = int(raw[1])
        sol = Solution()
        print(sol.kthGrammar(n, k))""",
        "cpp": """#include <iostream>

using namespace std;

class Solution {
public:
    int kthGrammar(int n, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    int n, k;
    if (cin >> n >> k) {
        Solution sol;
        cout << sol.kthGrammar(n, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int kthGrammar(int n, int k) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.kthGrammar(n, k));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthGrammar = function(n, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    console.log(kthGrammar(parseInt(input[0]), parseInt(input[1])));
}""",
        "c": """#include <stdio.h>

int kthGrammar(int n, int k) {
    // User logic here
    return 0;
}

int main() {
    int n, k;
    if (scanf("%d %d", &n, &k) == 2) {
        printf("%d\\n", kthGrammar(n, k));
    }
    return 0;
}"""
    }

    def solve(n, k):
        if n == 1:
            return 0
        mid = 2 ** (n - 2)
        if k <= mid:
            return solve(n - 1, k)
        else:
            return 1 - solve(n - 1, k - mid)

    test_cases_data = [
        (1, 1),
        (2, 1),
        (2, 2),
        (3, 3),
        (30, 434991989),
        (4, 5),
        (5, 10),
        (30, 536870912),
        (10, 256),
        (15, 12345)
    ]

    test_cases = []
    for i, (n, k) in enumerate(test_cases_data):
        inp = f"{n} {k}"
        out = str(solve(n, k))
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
        "topics": ["Math", "Recursion"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
