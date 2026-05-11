import json
import os

def generate_json():
    problem_id = 1281
    title = "Subtract the Product and Sum of Digits of an Integer"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1281. Subtract the Product and Sum of Digits of an Integer</h3>
<p>Given an integer number <code>n</code>, return the difference between the product of its digits and the sum of its digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 234
<strong>Output:</strong> 15 
<strong>Explanation:</strong> 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 4421
<strong>Output:</strong> 21
<strong>Explanation: 
</strong>Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>"""

    input_format = "An integer `n` as a JSON number."
    output_format = "An integer representing the result."

    constraints = [
        "1 <= n <= 10^5"
    ]

    explanation = """To find the difference between product and sum of digits:
1. Initialize `product = 1` and `sum = 0`.
2. Extract each digit from the number `n`:
   - Use `n % 10` to get the last digit.
   - Update `product *= digit`.
   - Update `sum += digit`.
   - Update `n //= 10` to remove the last digit.
3. Repeat until `n` becomes 0.
4. Return `product - sum`."""

    answer = """class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        for digit in str(n):
            d = int(digit)
            p *= d
            s += d
        return p - s"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n = int(raw)
        sol = Solution()
        print(sol.subtractProductAndSum(n))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int subtractProductAndSum(int n) {
        // User logic here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.subtractProductAndSum(n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int subtractProductAndSum(int n) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            System.out.println(new Solution().subtractProductAndSum(sc.nextInt()));
        }
    }
}""",
        "javascript": """var subtractProductAndSum = function(n) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    console.log(subtractProductAndSum(parseInt(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int subtractProductAndSum(int n){
    // User logic here
    return 0;
}

int main() {
    int n;
    if(scanf("%d", &n) == 1) {
        printf("%d\\n", subtractProductAndSum(n));
    }
    return 0;
}"""
    }

    def solve(n):
        p, s = 1, 0
        for digit in str(n):
            d = int(digit)
            p *= d
            s += d
        return p - s

    test_cases_data = [
        234,   # Sample 1
        4421,  # Sample 2
        1,     # Single digit
        10,    # Contains zero prod
        123,   # Small
        100000,# Max range
        99999, # Large
        # Stress tests
        100000,
        1,
        55555
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = str(t)
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
