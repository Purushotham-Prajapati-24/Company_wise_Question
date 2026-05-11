import json
import os

def generate_json():
    problem_id = 343
    title = "Integer Break"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>343. Integer Break</h3>
<p>Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 &times; 1 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>"""

    input_format = "An integer `n`."
    output_format = "An integer representing the maximum product."
    
    constraints = [
        "2 <= n <= 58"
    ]
    
    explanation = """To maximize the product of integers summing to $n$, we can use **Dynamic Programming** or a **Mathematical Observation**.

### Mathematical Observation:
- If we break $n$ into several factors, to maximize their product, the factors should be as close to each other as possible.
- More specifically, the optimal factor is $e \approx 2.718$. Since we need integers, the optimal factors are **2** and **3**.
- **3** is better than **2** because $3 \times 3 > 2 \times 2 \times 2$ (for sum 6, $3 \times 3 = 9$ vs $2 \times 2 \times 2 = 8$).
- Therefore, we should use as many **3s** as possible.

### Algorithm Steps:
1. **Base Cases**: 
   - $n=2$: return 1 ($1+1$).
   - $n=3$: return 2 ($1+2$).
2. **General Case ($n > 3$)**:
   - Divide $n$ by 3.
   - If the remainder is **0**: The product is $3^{(n/3)}$.
   - If the remainder is **1**: One 3 and the remainder 1 combine to form $3+1=4$. We should use $2 \times 2$ instead of $3 \times 1$. The product is $3^{(n//3 - 1)} \times 4$.
   - If the remainder is **2**: The product is $3^{(n//3)} \times 2$.

### Complexity Analysis:
- **Time Complexity**: $O(1)$ if using the math formula, or $O(n)$ if using a simple loop.
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        
        times_3 = n // 3
        remainder = n % 3
        
        if remainder == 0:
            return 3 ** times_3
        elif remainder == 1:
            # Instead of ..., 3, 1 (product 3), use ..., 2, 2 (product 4)
            return 3 ** (times_3 - 1) * 4
        else:
            # Remainder is 2
            return 3 ** times_3 * 2"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def integerBreak(self, n: int) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        n = int(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.integerBreak(n)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    int integerBreak(int n) {\n        // Your logic here\n        return 0;\n    }\n};\n\nint main() {\n    int n;\n    if (cin >> n) {\n        Solution sol;\n        cout << sol.integerBreak(n) << \"\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int integerBreak(int n) {\n        // Your logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            Solution sol = new Solution();\n            System.out.println(sol.integerBreak(n));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @return {number}\n */\nvar integerBreak = function(n) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const n = parseInt(input);\n    console.log(integerBreak(n));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint integerBreak(int n) {\n    // Your logic here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%d\\n\", integerBreak(n));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2", "expected_output": "1", "is_sample": True},
        {"input": "10", "expected_output": "36", "is_sample": True},
        {"input": "3", "expected_output": "2", "is_sample": False},
        {"input": "4", "expected_output": "4", "is_sample": False},
        {"input": "5", "expected_output": "6", "is_sample": False},
        {"input": "6", "expected_output": "9", "is_sample": False},
        {"input": "7", "expected_output": "12", "is_sample": False},
        # Stress cases
        {"input": "58", "expected_output": "1549681956", "is_sample": False},
        {"input": "57", "expected_output": "1162261467", "is_sample": False},
        {"input": "50", "expected_output": "21523360", "is_sample": False}
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
        "topics": ["Math", "Dynamic Programming"],
        "companyIndex": 1
    }

    output_path = "301-500/343_Integer_Break.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
