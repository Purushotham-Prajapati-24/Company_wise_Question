import json
import os

def generate_json():
    problem_id = 326
    title = "Power of Three"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>326. Power of Three</h3>
<p>Given an integer <code>n</code>, return <code>true</code> if it is a power of three. Otherwise, return <code>false</code>.</p>

<p>An integer <code>n</code> is a power of three if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 27
<strong>Output:</strong> true
<strong>Explanation:</strong> 27 = 3<sup>3</sup>
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without using any loop / recursion? """

    input_format = "An integer `n`."
    output_format = "A boolean `true` if `n` is a power of three, otherwise `false`."
    
    constraints = [
        "-2^31 <= n <= 2^31 - 1"
    ]
    
    explanation = """To determine if a number is a power of three without using loops or recursion:

### Concept:
In the range of a 32-bit signed integer ($-2^{31}$ to $2^{31}-1$), there is a **largest power of three**. 
Any number $n$ that is a power of three must be a **divisor** of this largest power of three.

### Algorithm Steps:
1. **Find the Max Power**: The largest power of three that fits in a 32-bit signed integer (where $n \le 2^{31}-1 = 2,147,483,647$) is $3^{19} = 1,162,261,467$.
2. **Handle Edge Cases**: If $n \le 0$, it cannot be a power of three. 
3. **Check Divisibility**: Return the result of $1162261467 \pmod n == 0$.

### Complexity Analysis:
- **Time Complexity**: $O(1)$ constant time as we only perform one modulo operation.
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Largest power of three in 32-bit signed integer is 3^19 = 1162261467
        # n must be greater than zero and divide the largest power perfectly.
        return n > 0 and 1162261467 % n == 0"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\n# User logic here\nclass Solution:\n    def isPowerOfThree(self, n: int) -> bool:\n        pass\n\nif __name__ == '__main__':\n    # Lethal parsing: Extract the first integer\n    input_data = sys.stdin.read()\n    match = re.search(r'-?\\d+', input_data)\n    if match:\n        n = int(match.group())\n        sol = Solution()\n        print(str(sol.isPowerOfThree(n)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\n// User logic here\nclass Solution {\npublic:\n    bool isPowerOfThree(int n) {\n        return false;\n    }\n};\n\nint main() {\n    string input;\n    string line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    // Lethal parsing: Extract the first integer\n    regex re(\"-?\\\\d+\");\n    smatch match;\n    if (regex_search(input, match, re)) {\n        int n = stoi(match.str());\n        Solution sol;\n        cout << (sol.isPowerOfThree(n) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\n// User logic here\nclass Solution {\n    public boolean isPowerOfThree(int n) {\n        return false;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        \n        // Lethal parsing: Extract the first integer\n        Pattern p = Pattern.compile(\"-?\\\\d+\");\n        Matcher m = p.matcher(sb.toString());\n        if (m.find()) {\n            int n = Integer.parseInt(m.group());\n            System.out.println(new Solution().isPowerOfThree(n) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\n// User logic here\n/**\n * @param {number} n\n * @return {boolean}\n */\nvar isPowerOfThree = function(n) {\n    return false;\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    // Lethal parsing: Extract the first integer\n    const match = input.match(/-?\\d+/);\n    if (match) {\n        const n = parseInt(match[0], 10);\n        console.log(isPowerOfThree(n) ? \"true\" : \"false\");\n    }\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\n// User logic here\nbool isPowerOfThree(int n) {\n    return false;\n}\n\nint main() {\n    int n;\n    // Lethal parsing: skip non-digit characters and read integer\n    while (scanf(\" %[^0-9-]\", (char[]){0}) || 1) {\n        if (scanf(\"%d\", &n) == 1) {\n            printf(\"%s\\n\", isPowerOfThree(n) ? \"true\" : \"false\");\n            break;\n        } else {\n            if (getchar() == EOF) break;\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "27", "expected_output": "true", "is_sample": True},
        {"input": "0", "expected_output": "false", "is_sample": True},
        {"input": "-1", "expected_output": "false", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "3", "expected_output": "true", "is_sample": False},
        {"input": "9", "expected_output": "true", "is_sample": False},
        {"input": "10", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "1162261467", "expected_output": "true", "is_sample": False},
        {"input": "2147483647", "expected_output": "false", "is_sample": False},
        {"input": "-2147483648", "expected_output": "false", "is_sample": False}
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
        "topics": ["Math", "Recursion"],
        "companyIndex": 1
    }

    output_path = "301-500/326_Power_of_Three.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
