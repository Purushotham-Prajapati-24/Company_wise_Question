import json
import os

def generate_json():
    problem_id = 507
    title = "Perfect Number"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>507. Perfect Number</h3>
<p>A <strong>perfect number</strong> is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer <code>x</code> is an integer that can divide <code>x</code> evenly.</p>

<p>Given an integer <code>num</code>, return <code>true</code> if <code>num</code> is a perfect number, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 28
<strong>Output:</strong> true
<strong>Explanation:</strong> 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 7
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>"""

    input_format = "A single line: an integer `num`."
    output_format = "A boolean value: `true` or `false`."
    
    constraints = [
        "1 <= num <= 10^8"
    ]
    
    explanation = """To find the sum of divisors efficiently, we only need to iterate up to the square root of `num`. For every divisor `i` found, we also add `num / i` to the sum, provided they are distinct. Note that 1 is a divisor but `num` itself shouldn't be added. If the sum equals `num`, it's a perfect number."""
    
    answer = """class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i * i != num:
                    total += num // i
            i += 1
        return total == num"""

    boilerplate = {
        "python": """import sys

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        num = int(raw)
        sol = Solution()
        print("true" if sol.checkPerfectNumber(num) else "false")""",
        "cpp": """#include <iostream>

using namespace std;

class Solution {
public:
    bool checkPerfectNumber(int num) {
        // User logic here
        return false;
    }
};

int main() {
    int num;
    if (cin >> num) {
        Solution sol;
        cout << (sol.checkPerfectNumber(num) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean checkPerfectNumber(int num) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.checkPerfectNumber(num) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const num = parseInt(input, 10);
    console.log(checkPerfectNumber(num) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdbool.h>

bool checkPerfectNumber(int num) {
    // User logic here
    return false;
}

int main() {
    int num;
    if (scanf("%d", &num) == 1) {
        if (checkPerfectNumber(num)) printf("true\\n");
        else printf("false\\n");
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "28", "expected_output": "true", "is_sample": True},
        {"input": "7", "expected_output": "false", "is_sample": True},
        
        # Five Diverse Cases
        {"input": "6", "expected_output": "true", "is_sample": False},
        {"input": "496", "expected_output": "true", "is_sample": False},
        {"input": "8128", "expected_output": "true", "is_sample": False},
        {"input": "2", "expected_output": "false", "is_sample": False},
        {"input": "12", "expected_output": "false", "is_sample": False},
        
        # Three Stress Test Cases (large bounds constraints)
        {"input": "99999999", "expected_output": "false", "is_sample": False},
        {"input": "33550336", "expected_output": "true", "is_sample": False},
        {"input": "1", "expected_output": "false", "is_sample": False}
    ]

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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Math"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
