import json
import os

def generate_json():
    problem_id = 967
    title = "Numbers With Same Consecutive Differences"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>967. Numbers With Same Consecutive Differences</h3>
<p>Given two integers n and k, return an array of all the integers of length <code>n</code> such that the absolute difference between every two consecutive digits is <code>k</code>.</p>

<p>Note that every number in the answer <strong>must not</strong> have leading zeros <strong>except</strong> for the number <code>0</code> itself. For example, <code>01</code> has one leading zero and is invalid, but <code>0</code> is valid.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 7
<strong>Output:</strong> [181,292,707,818,929]
<strong>Explanation:</strong> Note that 070 is not a valid number, because it has leading zeroes.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 1
<strong>Output:</strong> [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 9</code></li>
	<li><code>0 &lt;= k &lt;= 9</code></li>
</ul>"""

    input_format = "Two space-separated integers n and k."
    output_format = "A list of space-separated integers in any order."
    
    constraints = ["2 <= n <= 9", "0 <= k <= 9", "No leading zeros."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def numsSameConsecDiff(n, k):
    res = []
    if n == 1: res.append(0)
    
    queue = deque(range(1, 10))
    for _ in range(n - 1):
        for _ in range(len(queue)):
            num = queue.popleft()
            last_digit = num % 10
            # Try adding k
            if last_digit + k <= 9:
                queue.append(num * 10 + last_digit + k)
            # Try subtracting k, but only if k > 0 to avoid duplicates
            if k > 0 and last_digit - k >= 0:
                queue.append(num * 10 + last_digit - k)
    return list(queue)"""

    boilerplate = {
        "python": "import sys\n\ndef numsSameConsecDiff(n, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    n = input_data[0] if len(input_data) > 0 else \"\"\n    k = input_data[1] if len(input_data) > 1 else \"\"\n    print(numsSameConsecDiff(n, k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint numsSameConsecDiff(string n, string k) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string n; cin >> n;\n    string k; cin >> k;\n    cout << numsSameConsecDiff(n, k) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
