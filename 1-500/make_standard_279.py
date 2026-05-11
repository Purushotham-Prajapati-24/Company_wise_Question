import json
import os

def generate_json():
    problem_id = 279
    title = "Perfect Squares"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>279. Perfect Squares</h3>
<p>Given an integer <code>n</code>, return <em>the least number of perfect square numbers that sum to</em> <code>n</code>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, <code>1</code>, <code>4</code>, <code>9</code>, and <code>16</code> are perfect squares while <code>3</code> and <code>11</code> are not.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 12
<strong>Output:</strong> 3
<strong>Explanation:</strong> 12 = 4 + 4 + 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 13
<strong>Output:</strong> 2
<strong>Explanation:</strong> 13 = 4 + 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer `n`."
    output_format = "An integer representing the minimum number of perfect square numbers."
    
    constraints = [
        "1 <= n <= 10,000"
    ]
    
    explanation = """To find the minimum number of perfect squares that sum to `n`:
1. **Dynamic Programming**: We use a `dp` array where `dp[i]` is the minimum number of perfect squares to sum to `i`.
2. **Transition**: For each `i` from 1 to `n`:
   - `dp[i] = min(dp[i - square] + 1)` for all `square` such that `square <= i` and `square` is a perfect square (i.e., `square = j * j`).
3. **Initialization**: `dp[0] = 0`, and other `dp[i]` values are initialized to infinity (or `i`, since `i` can always be formed by summing `1` squared `i` times).
4. **Complexity Analysis**:
   - Time: O(N * sqrt(N)) because for each of the `N` numbers, we check at most `sqrt(N)` perfect squares.
   - Space: O(N) to store the `dp` array."""
    
    answer = """import math

class Solution:
    def numSquares(self, n: int) -> int:
        # Initializing dp array where dp[i] is the min count of perfect square numbers summing to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Pre-calculating perfect squares up to n
        squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        
        # Iterate over each number from 1 to n
        for i in range(1, n + 1):
            # For each number i, try all perfect squares less than or equal to i
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
                
        return dp[n]"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef numSquares(n: int) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    match = re.search(r'\\d+', raw_input)\n    if match:\n        n = int(match.group())\n        print(numSquares(n))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <regex>\n\nusing namespace std;\n\nint numSquares(int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_num(R\"(\\d+)\");\n    smatch match;\n    if (regex_search(input, match, re_num)) {\n        int n = stoi(match.str());\n        cout << numSquares(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int numSquares(int n) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (sc.hasNext()) {\n            String input = sc.next();\n            Matcher m = Pattern.compile(\"\\\\d+\").matcher(input);\n            if (m.find()) {\n                int n = Integer.parseInt(m.group());\n                System.out.println(new Solution().numSquares(n));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction numSquares(n) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/\\d+/);\nif (match) {\n    const n = parseInt(match[0]);\n    console.log(numSquares(n));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint numSquares(int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    static char buffer[100000];\n    if (fread(buffer, 1, 99999, stdin) > 0) {\n        char *p = buffer;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) {\n            int n = atoi(p);\n            printf(\"%d\\n\", numSquares(n));\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "12", "expected_output": "3", "is_sample": True},
        {"input": "13", "expected_output": "2", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "2", "expected_output": "2", "is_sample": False},
        {"input": "3", "expected_output": "3", "is_sample": False},
        {"input": "4", "expected_output": "1", "is_sample": False},
        {"input": "16", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "10000", "expected_output": "1", "is_sample": False},
        {"input": "9999", "expected_output": "4", "is_sample": False}, # Legendre's 4-square theorem (3-square fails, so it must be 4)
        {"input": "7168", "expected_output": "4", "is_sample": False} # 7168 is 7 * 1024. 7 is not sum of 3 squares (7 mod 8 is 7), so 7168 is also 4 squares.
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
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Math", "Dynamic Programming", "Breadth-First Search"],
        "companyIndex": 0
    }

    output_path = "201-400/279_Perfect_Squares.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
