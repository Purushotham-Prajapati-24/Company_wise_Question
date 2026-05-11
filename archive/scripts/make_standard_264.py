import json
import os

def generate_json():
    problem_id = 264
    title = "Ugly Number II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>264. Ugly Number II</h3>
<p>An <strong>ugly number</strong> is a positive integer whose prime factors are limited to <code>2</code>, <code>3</code>, and <code>5</code>.</p>

<p>Given an integer <code>n</code>, return <em>the</em> <code>n<sup>th</sup></code> <em><strong>ugly number</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 10
<strong>Output:</strong> 12
<strong>Explanation:</strong> [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1690</code></li>
</ul>"""

    input_format = "A single integer N."
    output_format = "The N-th ugly number."
    
    constraints = ["1 <= n <= 1690\n", "O(N) time complexity required.\n"]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def solve(n):
    ugly = [1] * n
    i2 = i3 = i5 = 0
    for i in range(1, n):
        next_val = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        ugly[i] = next_val
        if next_val == ugly[i2] * 2:
            i2 += 1
        if next_val == ugly[i3] * 3:
            i3 += 1
        if next_val == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]"""

    boilerplate = {
        "python": "import sys\n\ndef nthUglyNumber(n: int) -> int:\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        n = int(line)\n        print(nthUglyNumber(n))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint nthUglyNumber(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        cout << nthUglyNumber(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int nthUglyNumber(int n) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            System.out.println(new Solution().nthUglyNumber(sc.nextInt()));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction nthUglyNumber(n) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(nthUglyNumber(parseInt(input)));\n}",
        "c": "#include <stdio.h>\n\nint nthUglyNumber(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%d\\n\", nthUglyNumber(n));\n    }\n    return 0;\n}"
    }

    test_cases = [{"input": "10", "expected_output": "12", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        {"input": "7", "expected_output": "8", "is_sample": False},
        {"input": "11", "expected_output": "15", "is_sample": False},
        {"input": "1690", "expected_output": "2123366400", "is_sample": False}, # Max n
        {"input": "500", "expected_output": "937500", "is_sample": False},
        {"input": "100", "expected_output": "1536", "is_sample": False},
        {"input": "15", "expected_output": "24", "is_sample": False},
        {"input": "20", "expected_output": "36", "is_sample": False},
        {"input": "30", "expected_output": "80", "is_sample": False},]

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
        "topics": ["Hash Table", "Math", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "201-400/264_Ugly_Number_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
