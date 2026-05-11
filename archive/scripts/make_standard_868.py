import json
import os

def generate_json():
    problem_id = 868
    title = "Binary Gap"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>868. Binary Gap</h3>
<p>Given a positive integer <code>n</code>, find and return <em>the <strong>longest distance</strong> between any two <strong>adjacent</strong> </em><code>1</code><em>'s in the binary representation of </em><code>n</code>. If there are no two adjacent <code>1</code>'s, return <code>0</code>.</p>

<p>Two <code>1</code>'s are <strong>adjacent</strong> if there are only <code>0</code>'s separating them (possibly no <code>0</code>'s). The <b>distance</b> between two <code>1</code>'s is the absolute difference between their bit positions. For example, if <code>n = 22</code>, its binary representation is <code>10110</code>:</p>

<ul>
    <li>The first adjacent pair of <code>1</code>'s is at index <code>4</code> and <code>2</code>, with a distance of <code>4 - 2 = 2</code>.</li>
    <li>The second adjacent pair of <code>1</code>'s is at index <code>2</code> and <code>1</code>, with a distance of <code>2 - 1 = 1</code>.</li>
    <li>The answer is the maximum of these distances, which is <code>2</code>.</li>
    <li>Note that the <code>1</code> at index <code>4</code> and the <code>1</code> at index <code>1</code> are not adjacent because the <code>1</code> at index <code>2</code> is between them.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 22
<strong>Output:</strong> 2
<strong>Explanation:</strong> 22 in binary is "10110".
The first adjacent pair of 1's is at index 4 and 2, with a distance of 2.
The second adjacent pair of 1's is at index 2 and 1, with a distance of 1.
The answer is the maximum of these distances, which is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 8
<strong>Output:</strong> 0
<strong>Explanation:</strong> 8 in binary is "1000".
There are no adjacent pairs of 1's in the binary representation of 8, so we return 0.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 in binary is "101".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single integer `n`."
    output_format = "An integer representing the longest distance between adjacent 1's."

    constraints = [
        "1 <= n <= 10^9"
    ]

    explanation = """To find the longest distance between adjacent 1's, we iterate through the bits of the binary representation of n. We record the position of the last 1 seen. When we encounter a new 1, we calculate the distance between the current position and the last seen 1, and update the maximum distance."""

    answer = """class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        ans = 0
        for i in range(32):
            if (n >> i) & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
        return ans"""

    boilerplate = {
        "python": """import sys

class Solution:
    def binaryGap(self, n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n = int(raw)
        sol = Solution()
        print(sol.binaryGap(n))""",
        "cpp": """#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int binaryGap(int n) {
        // User logic here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.binaryGap(n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int binaryGap(int n) {
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
            System.out.println(sol.binaryGap(n));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(binaryGap(parseInt(input)));
}""",
        "c": """#include <stdio.h>

int binaryGap(int n) {
    // User logic here
    return 0;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%d\\n", binaryGap(n));
    }
    return 0;
}"""
    }

    def solve(n):
        last = -1
        ans = 0
        for i in range(32):
            if (n >> i) & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
        return ans

    test_cases_data = [
        22, 8, 5, 1, 6, 12, 10, 100, 524288, 1000000000
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
        "topics": ["Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
