import json
import os

def generate_json():
    problem_id = 440
    title = "K-th Smallest in Lexicographical Order"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>440. K-th Smallest in Lexicographical Order</h3>
<p>Given two integers <code>n</code> and <code>k</code>, return <em>the </em><code>k<sup>th</sup></code><em> lexicographically smallest integer in the range </em><code>[1, n]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 13, k = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Two integers n and k."
    output_format = "The kth lexicographical integer."
    
    constraints = ["1 <= k <= n <= 10^9", "O(log^2 n) or better time complexity."]
    
    explanation = """HARD problem on ."""
    
    answer = """def findKthNumber(n, k):
    def count_steps(curr, n):
        steps = 0
        first = curr
        last = curr
        while first <= n:
            steps += min(n, last) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    curr = 1
    k -= 1
    while k > 0:
        steps = count_steps(curr, n)
        if steps <= k:
            k -= steps
            curr += 1
        else:
            curr *= 10
            k -= 1
    return curr"""

    boilerplate = {
        "python": "import sys\n\ndef count_steps(curr, n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    curr = input_data[0].strip() if len(input_data) > 0 else \"\"\n    n = input_data[1].strip() if len(input_data) > 1 else \"\"\n    print(count_steps(curr, n))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint count_steps(string curr, string n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string curr; cin >> curr;\n    string n; cin >> n;\n    cout << count_steps(curr, n) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "13\\n2", "expected_output": "10", "is_sample": True},
        {"input": "1\\n1", "expected_output": "1", "is_sample": True},
        {"input": "100\\n10", "expected_output": "18", "is_sample": False},
        {"input": "100\\n1", "expected_output": "1", "is_sample": False},
        {"input": "1000\\n1000", "expected_output": "999", "is_sample": False},
        {"input": "123456\\n10", "expected_output": "100003", "is_sample": False},
        {"input": "20\\n5", "expected_output": "13", "is_sample": False},
        # Stress tests]

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
