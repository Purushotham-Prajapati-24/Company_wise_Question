import json
import os

def generate_json():
    problem_id = 231
    title = "Power of Two"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>231. Power of Two</h3>
<p>Given an integer <code>n</code>, return <code>true</code> if it is a power of two. Otherwise, return <code>false</code>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?"""

    input_format = "A single integer n."
    output_format = "A boolean (true/false)."
    
    constraints = [
        "-2^31 <= n <= 2^31 - 1"
    ]
    
    explanation = """To determine if a number is a power of two without loops:
1. **Definition**: A power of two in binary has exactly one '1' bit (e.g., 2=10, 4=100, 8=1000).
2. **Bit Manipulation**:
   - If `n` is a power of two, then `n & (n - 1)` will be exactly `0`.
   - For example: `8 (1000) & 7 (0111) = 0`.
   - We must also ensure `n > 0` because negative numbers and 0 cannot be powers of two.
3. **Complexity**: O(1) time and O(1) space."""
    
    answer = """class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0"""

    boilerplate = {
        "python": "import sys\n\ndef isPowerOfTwo(n):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(\"true\" if isPowerOfTwo(int(line)) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nbool isPowerOfTwo(long long n) {\n    // User logic\n    return false;\n}\n\nint main() {\n    long long n;\n    if (cin >> n) {\n        cout << (isPowerOfTwo(n) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean isPowerOfTwo(long n) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLong()) {\n            long n = sc.nextLong();\n            System.out.println(new Solution().isPowerOfTwo(n) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isPowerOfTwo(n) {\n    // User logic\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(isPowerOfTwo(BigInt(input)) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nbool isPowerOfTwo(long long n) {\n    // User logic\n    return false;\n}\n\nint main() {\n    long long n;\n    if (scanf(\"%lld\", &n) == 1) {\n        printf(\"%s\\n\", isPowerOfTwo(n) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1", "expected_output": "true", "is_sample": True},
        {"input": "16", "expected_output": "true", "is_sample": True},
        {"input": "3", "expected_output": "false", "is_sample": True},
        {"input": "0", "expected_output": "false", "is_sample": False},
        {"input": "-16", "expected_output": "false", "is_sample": False},
        {"input": "536870912", "expected_output": "true", "is_sample": False}, # 2^29
        {"input": "1073741824", "expected_output": "true", "is_sample": False}, # 2^30
        {"input": "2147483647", "expected_output": "false", "is_sample": False}, # Max Int
        {"input": "2147483648", "expected_output": "true", "is_sample": False}, # 2^31
        {"input": "-2147483648", "expected_output": "false", "is_sample": False}  # Min Int
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
        "topics": ["Math", "Bit Manipulation", "Recursion"],
        "companyIndex": 0
    }

    output_path = "201-400/231_Power_of_Two.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
