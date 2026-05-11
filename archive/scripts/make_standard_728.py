import json
import os

def generate_json():
    problem_id = 728
    title = "Self Dividing Numbers"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>728. Self Dividing Numbers</h3>
<p>A <strong>self-dividing number</strong> is a number that is divisible by every digit it contains.</p>

<ul>
    <li>For example, <code>128</code> is a self-dividing number because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.</li>
</ul>

<p>A self-dividing number is not allowed to contain the digit zero.</p>

<p>Given two integers <code>left</code> and <code>right</code>, return <em>a list of all the <strong>self-dividing numbers</strong> in the range</em> <code>[left, right]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> left = 1, right = 22
<strong>Output:</strong> [1,2,3,4,5,6,7,8,9,11,12,15,22]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> left = 47, right = 85
<strong>Output:</strong> [48,55,66,77]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= left &lt;= right &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two integers on separate lines: `left` and `right`."
    output_format = "A JSON array of integers."

    constraints = [
        "1 <= left <= right <= 10^4"
    ]

    explanation = """To check if a number is self-dividing, repeatedly divide it by 10 to extract the digits. If any digit is 0 or the number is not divisible by the digit, it's not a self-dividing number. Check every number in the range [left, right] and add to the result if valid."""

    answer = """class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(n):
            original = n
            while n > 0:
                digit = n % 10
                if digit == 0 or original % digit != 0:
                    return False
                n //= 10
            return True
        return [i for i in range(left, right + 1) if is_self_dividing(i)]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split()
    if len(raw) >= 2:
        left = int(raw[0])
        right = int(raw[1])
        sol = Solution()
        print(json.dumps(sol.selfDividingNumbers(left, right)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        // User logic here
        return {};
    }
};

int main() {
    int left, right;
    if (cin >> left >> right) {
        Solution sol;
        vector<int> res = sol.selfDividingNumbers(left, right);
        cout << "[";
        for (size_t i = 0; i < res.size(); ++i) {
            cout << res[i] << (i + 1 == res.size() ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int left = sc.nextInt();
            int right = sc.nextInt();
            Solution sol = new Solution();
            List<Integer> res = sol.selfDividingNumbers(left, right);
            System.out.print("[");
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i) + (i + 1 == res.size() ? "" : ","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    const left = parseInt(input[0], 10);
    const right = parseInt(input[1], 10);
    console.log(JSON.stringify(selfDividingNumbers(left, right)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* selfDividingNumbers(int left, int right, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    int left, right;
    if (scanf("%d %d", &left, &right) == 2) {
        int returnSize;
        int* res = selfDividingNumbers(left, right, &returnSize);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("%d%s", res[i], i == returnSize - 1 ? "" : ",");
        }
        printf("]\\n");
        if(res) free(res);
    }
    return 0;
}"""
    }

    def solve(left, right):
        def is_self_dividing(n):
            original = n
            while n > 0:
                digit = n % 10
                if digit == 0 or original % digit != 0:
                    return False
                n //= 10
            return True
        return [i for i in range(left, right + 1) if is_self_dividing(i)]

    test_cases_data = [
        (1, 22),
        (47, 85),
        (1, 100),
        (100, 200),
        (9900, 10000),
        (1, 1),
        (10000, 10000),
        (1, 9999),
        (128, 128),
        (85, 200)
    ]

    test_cases = []
    for i, (left, right) in enumerate(test_cases_data):
        inp = str(left) + "\\n" + str(right)
        out = json.dumps(solve(left, right)).replace(" ", "")
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
        "topics": ["Math"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
