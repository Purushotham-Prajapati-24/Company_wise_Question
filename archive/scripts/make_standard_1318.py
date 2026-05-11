import json
import os

def generate_json():
    problem_id = 1318
    title = "Minimum Flips to Make a OR b Equal to c"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1318. Minimum Flips to Make a OR b Equal to c</h3>
<p>Given 3 positives numbers <code>a</code>, <code>b</code> and <code>c</code>. Return the minimum flips required in some bits of <code>a</code> and <code>b</code> to make ( <code>a</code> OR <code>b</code> == <code>c</code> ). (bit-wise OR operation).<br>
Flip operation consists of change&nbsp;any&nbsp;single bit 1 to 0 or change the bit 0 to 1&nbsp;in their binary representation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/06/sample_3_1676.png" style="width: 260px; height: 87px;">
<pre><strong>Input:</strong> a = 2, b = 6, c = 5
<strong>Output:</strong> 3
<strong>Explanation: </strong>After flips a = 1 , b = 4 , c = 5 ((1 OR 4) == 5)
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = 4, b = 2, c = 7
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> a = 1, b = 2, c = 3
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= a &lt;= 10^9</code></li>
    <li><code>1 &lt;= b &lt;= 10^9</code></li>
    <li><code>1 &lt;= c &lt;= 10^9</code></li>
</ul>"""

    input_format = "Three integers `a`, `b`, and `c` provided as `[a, b, c]` in JSON."
    output_format = "An integer representing the minimum flips."

    constraints = [
        "1 <= a, b, c <= 10^9"
    ]

    explanation = """To find the minimum flips required:
1. Iterate through each bit position (0 to 31).
2. For each position:
   - Extract the bits of a, b, and c: `bitA = (a >> i) & 1`, `bitB = (b >> i) & 1`, `bitC = (c >> i) & 1`.
   - If `(bitA | bitB) != bitC`:
     - If `bitC == 1`: We need at least one bit to be 1. Since both are 0, we need exactly 1 flip (either a or b).
     - If `bitC == 0`: We need both bits to be 0. We must flip every 1 bit to 0. So, flips = `bitA + bitB`."""

    answer = """class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            bitA = (a >> i) & 1
            bitB = (b >> i) & 1
            bitC = (c >> i) & 1
            
            if (bitA | bitB) != bitC:
                if bitC == 1:
                    res += 1
                else:
                    res += (bitA + bitB)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        args = json.loads(raw)
        a = args[0]
        b = args[1]
        c = args[2]
        sol = Solution()
        print(sol.minFlips(a, b, c))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int minFlips(int a, int b, int c) {
        // User logic here
        return 0;
    }
};

int main() {
    printf("3\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minFlips(int a, int b, int c) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(3);
    }
}""",
        "javascript": """/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var minFlips = function(a, b, c) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [a, b, c] = JSON.parse(input);
    console.log(minFlips(a, b, c));
}""",
        "c": """#include <stdio.h>

int minFlips(int a, int b, int c) {
    // User logic here
    return 0;
}

int main() {
    printf("3\\n");
    return 0;
}"""
    }

    def solve(a, b, c):
        res = 0
        for i in range(32):
            ba, bb, bc = (a>>i)&1, (b>>i)&1, (c>>i)&1
            if (ba|bb) != bc:
                if bc == 1: res += 1
                else: res += (ba + bb)
        return res

    test_cases_data = [
        (2, 6, 5),
        (4, 2, 7),
        (1, 2, 3),
        (8, 3, 5),
        (10, 10, 10),
        (1, 1, 0),
        (0, 0, 0), # although constraints say positive, 0 is good for edge
        (1000000000, 1, 1000000001),
        (7, 2, 3),
        (1, 2, 4)
    ]

    test_cases = []
    for i, data_triple in enumerate(test_cases_data):
        a, b, c = data_triple
        inp = json.dumps([a, b, c]).replace(" ", "")
        out = str(solve(a, b, c))
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

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
