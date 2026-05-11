import json
import os

def generate_json():
    problem_id = 509
    title = "Fibonacci Number"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>509. Fibonacci Number</h3>
<p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is:</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>"""

    input_format = "Line 1: An integer `n`."
    output_format = "An integer representing F(n)."
    
    constraints = [
        "0 <= n <= 30"
    ]
    
    explanation = "The Fibonacci sequence starts with F(0) = 0 and F(1) = 1. For n > 1, each element is the sum of the previous two. You can solve this iteratively using two variables to track the two most recent values, which is O(n) time and O(1) space."
    
    answer = """class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def fib(self, n: int) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        n = int(line)
        sol = Solution()
        print(json.dumps(sol.fib(n)))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int fib(int n) {
        // User Logic Here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.fib(n) << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int fib(int n) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.fib(n));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const n = parseInt(input);
    console.log(fib(n));
}""",
        "c": r"""#include <stdio.h>

int fib(int n) {
    // User Logic Here
    return 0;
}

int main() {
    int n;
    if (scanf("%d", &n) != EOF) {
        printf("%d\n", fib(n));
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "2", "expected_output": "1", "is_sample": True},
        {"input": "3", "expected_output": "2", "is_sample": True},
        
        # Five Diverse Cases
        {"input": "4", "expected_output": "3", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "5", "expected_output": "5", "is_sample": False},
        {"input": "10", "expected_output": "55", "is_sample": False},
        
        # Three Stress Test Cases
        {"input": "20", "expected_output": "6765", "is_sample": False},
        {"input": "25", "expected_output": "75025", "is_sample": False},
        {"input": "30", "expected_output": "832040", "is_sample": False}
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
        "topics": ["Math", "Dynamic Programming", "Recursion", "Memoization"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Fibonacci_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
