import json
import os

def generate_json():
    problem_id = 2829
    title = "Determine the Minimum Sum of a k-avoiding Array"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>2829. Determine the Minimum Sum of a k-avoiding Array</h3>
<p>You are given two integers, <code>n</code> and <code>k</code>.</p>

<p>An array of <strong>distinct</strong> positive integers is called <b>k-avoiding</b> if there does not exist any pair of distinct elements that sum to <code>k</code>.</p>

<p>Return <em>the <strong>minimum</strong> possible sum of a k-avoiding array of length </em><code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5, k = 4
<strong>Output:</strong> 18
<strong>Explanation:</strong> Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> Consider the k-avoiding array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 50</code></li>
</ul>
"""

    input_format = "Two integers `n` and `k` provided as `[n, k]` in JSON."
    output_format = "An integer representing the minimum possible sum."

    constraints = [
        "1 <= n, k <= 50"
    ]

    explanation = """To find the minimum sum of a k-avoiding array:
1. To minimize the sum, we should always try to include the smallest possible positive integers (1, 2, 3, ...).
2. For each number `x` starting from 1, we can include it in our array if `k - x` is not already in the array.
3. Since we want to minimize the sum, we greedily pick the smallest available integers that satisfy the condition.
4. Continue until the array has `n` elements."""

    answer = """class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        s = set()
        total_sum = 0
        i = 1
        while len(s) < n:
            if k - i not in s:
                s.add(i)
                total_sum += i
            i += 1
        return total_sum"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, k = json.loads(raw)
        sol = Solution()
        print(sol.minimumSum(n, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumSum(int n, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0], k = j[1];
        Solution sol;
        cout << sol.minimumSum(n, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minimumSum(int n, int k) {
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
            System.out.println(new Solution().minimumSum(data[0], data[1]));
        }
    }
}""",
        "javascript": """var minimumSum = function(n, k) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, k] = JSON.parse(input);
    console.log(minimumSum(n, k));
}""",
        "c": """#include <stdio.h>

int minimumSum(int n, int k) {
    // User logic here
    return 0;
}

int main() {
    int n, k;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    if (scanf("%d", &n) == 1) {
        while ((c = getchar()) != EOF && c != ',');
        if (scanf("%d", &k) == 1) {
            printf("%d\\n", minimumSum(n, k));
        }
    }
    return 0;
}"""
    }

    def solve(n, k):
        res = []
        i = 1
        while len(res) < n:
            valid = True
            for x in res:
                if x + i == k:
                    valid = False
                    break
            if valid: res.append(i)
            i += 1
        return sum(res)

    test_cases_data = [
        [5, 4], # Sample 1
        [2, 6], # Sample 2
        [1, 1],
        [10, 1],
        [5, 10],
        [1, 50],
        [50, 1],
        # Stress tests
        [50, 50],
        [50, 2],
        [2, 50]
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
        "topics": ["Array", "Greedy", "Hash Table", "Math"], "companyIndex": 0
    }

    output_path = f"2801-3000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
