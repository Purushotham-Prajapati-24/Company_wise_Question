import json
import os

def generate_json():
    problem_id = 479
    title = "Largest Palindrome Product"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>479. Largest Palindrome Product</h3>
<p>Given an integer <code>n</code>, return <em>the <strong>largest palindromic integer</strong> that can be represented as the product of two <code>n</code>-digit integers</em>. Since the answer can be very large, return it <strong>modulo</strong> <code>1337</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 987
<strong>Explanation:</strong> 99 x 91 = 9009, 9009 % 1337 = 987
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>"""

    input_format = "Line 1: An integer `n`."
    output_format = "An integer representing the largest palindromic product modulo 1337."
    
    constraints = [
        "1 <= n <= 8"
    ]
    
    explanation = "For a given n, the largest n-digit product is between (10^n-1)^2 and (10^{n-1})^2. We can construct palindromes in descending order by taking a number 'half' from 10^n-1 down to 10^{n-1} and appending its reverse. For each palindrome, check if it can be factored into two n-digit integers."
    
    answer = """class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        upper = 10**n - 1
        lower = 10**(n-1)
        
        for left in range(upper, lower - 1, -1):
            s = str(left)
            p = int(s + s[::-1])
            
            for i in range(upper, lower - 1, -1):
                if i * i < p:
                    break
                if p % i == 0:
                    return p % 1337
        return 0"""

    boilerplate = {
        "python": r"""import sys

class Solution:
    def largestPalindrome(self, n: int) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        n = int(line)
        sol = Solution()
        print(sol.largestPalindrome(n))""",
        "cpp": r"""#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    int largestPalindrome(int n) {
        // User Logic Here
        return 0;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << sol.largestPalindrome(n) << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int largestPalindrome(int n) {
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
            System.out.println(sol.largestPalindrome(n));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number} n
 * @return {number}
 */
var largestPalindrome = function(n) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const n = parseInt(input);
    console.log(largestPalindrome(n));
}""",
        "c": r"""#include <stdio.h>

int largestPalindrome(int n) {
    // User Logic Here
    return 0;
}

int main() {
    int n;
    if (scanf("%d", &n) != EOF) {
        printf("%d\n", largestPalindrome(n));
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "2", "expected_output": "987", "is_sample": True},
        {"input": "1", "expected_output": "9", "is_sample": True},
        {"input": "3", "expected_output": "123", "is_sample": False},
        {"input": "4", "expected_output": "597", "is_sample": False},
        {"input": "5", "expected_output": "677", "is_sample": False},
        {"input": "6", "expected_output": "1218", "is_sample": False},
        {"input": "7", "expected_output": "877", "is_sample": False},
        {"input": "8", "expected_output": "475", "is_sample": False},
        {"input": "1", "expected_output": "9", "is_sample": False},
        {"input": "2", "expected_output": "987", "is_sample": False}
    ]

    data = {
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
            "time_limit_ms": 2000, # Hard problem, might need a bit more time
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Math", "Enumeration"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Largest_Palindrome_Product.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
