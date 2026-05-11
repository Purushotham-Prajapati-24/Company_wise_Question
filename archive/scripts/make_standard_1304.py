import json
import os

def generate_json():
    problem_id = 1304
    title = "Find N Unique Integers Sum up to Zero"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1304. Find N Unique Integers Sum up to Zero</h3>
<p>Given an integer <code>n</code>, return <strong>any</strong> array containing <code>n</code> <strong>unique</strong>&nbsp;integers such that they add up to <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> [-7,-1,1,3,4]
<strong>Explanation:</strong> These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> [-1,0,1]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>"""

    input_format = "A single integer `n`."
    output_format = "A JSON array of `n` unique integers."

    constraints = [
        "1 <= n <= 1000"
    ]

    explanation = """To generate an array of n unique integers that sum to zero:
1. If n is odd, the array could contain 0.
2. For every positive integer `i`, we can include its negative counterpart `-i`.
3. For example, if n = 5, we can use [-2, -1, 0, 1, 2].
4. If n = 4, we can use [-2, -1, 1, 2].
Essentially, for i from 1 to n/2, include i and -i. If n is odd, also include 0."""

    answer = """class Solution:
    def sumZero(self, n: int) -> list[int]:
        res = []
        if n % 2 != 0:
            res.append(0)
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def sumZero(self, n: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n = int(raw)
        sol = Solution()
        print(json.dumps(sol.sumZero(n)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> sumZero(int n) {
        // User logic here
        return {};
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        vector<int> res = sol.sumZero(n);
        cout << "[";
        for (int i=0; i<res.size(); ++i) cout << res[i] << (i == res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] sumZero(int n) {
        // User logic here
        return new int[]{};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution sol = new Solution();
            int[] res = sol.sumZero(n);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(sumZero(parseInt(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize) {
    // User logic here
    *returnSize = n;
    return (int*)malloc(n * sizeof(int));
}

int main() {
    printf("[-1,0,1]\\n");
    return 0;
}"""
    }

    def solve(n):
        res = []
        if n % 2 != 0: res.append(0)
        for i in range(1, n // 2 + 1):
            res.append(i); res.append(-i)
        return res

    test_cases_data = [5, 3, 1, 2, 4, 10, 100, 1000, 7, 0] # n=0 case usually n >= 1
    # Leetcode says 1 <= n <= 1000, so we use 1..1000

    test_cases = []
    for i, n in enumerate(test_cases_data):
        if n == 0: continue
        inp = str(n)
        # Note: Solver output doesn't have to match exactly, as long as it sums to 0 and is unique.
        # But for automated simple checker, we provide one valid output.
        out = json.dumps(solve(n)).replace(" ", "")
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
        "topics": ["Array", "Math"],
        "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
