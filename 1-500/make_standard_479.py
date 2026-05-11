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
        "python": "import sys\n\nclass Solution:\n    def largestPalindrome(self, n: int) -> int:\n        # User logic here\n        return 0\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        n = int(line)\n        sol = Solution()\n        print(sol.largestPalindrome(n))",
        "cpp": "#include <iostream>\n#include <string>\n#include <cmath>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int largestPalindrome(int n) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    int n;\n    if (cin >> n) {\n        Solution sol;\n        cout << sol.largestPalindrome(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int largestPalindrome(int n) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            Solution sol = new Solution();\n            System.out.println(sol.largestPalindrome(n));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @return {number}\n */\nvar largestPalindrome = function(n) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const n = parseInt(input);\n    console.log(largestPalindrome(n));\n}",
        "c": "#include <stdio.h>\n\nint largestPalindrome(int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) != EOF) {\n        printf(\"%d\\n\", largestPalindrome(n));\n    }\n    return 0;\n}"
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
