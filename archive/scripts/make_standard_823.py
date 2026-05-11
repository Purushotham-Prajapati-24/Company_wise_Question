import json
import os

def generate_json():
    problem_id = 823
    title = "Binary Trees With Factors"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>823. Binary Trees With Factors</h3>
<p>Given an array of unique integers, <code>arr</code>, where each integer <code>arr[i]</code> is strictly greater than <code>1</code>.</p>

<p>We make a binary tree using these integers. Each node must have a value in <code>arr</code>, and for every non-leaf node, its value should be equal to the product of the values of its children.</p>

<p>Return <em>the number of binary trees we can make</em>. The answer may be too large so return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,4,5,10]
<strong>Output:</strong> 7
<strong>Explanation:</strong> We can make these trees: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>2 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li>All the values of <code>arr</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "An integer n, followed by n space-separated integers."
    output_format = "An integer representing the number of binary trees modulo 10^9 + 7."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def numFactoredBinaryTrees(arr):
    MOD = 10**9 + 7
    arr.sort()
    dp = {x: 1 for x in arr}
    for i, x in enumerate(arr):
        for j in range(i):
            if x % arr[j] == 0:
                y = x // arr[j]
                if y in dp:
                    dp[x] = (dp[x] + dp[arr[j]] * dp[y]) % MOD
    return sum(dp.values()) % MOD"""

    boilerplate = {
        "python": "import sys\n\ndef numFactoredBinaryTrees(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    arr = input_data[0] if len(input_data) > 0 else \"\"\n    print(numFactoredBinaryTrees(arr))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint numFactoredBinaryTrees(string arr) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string arr; cin >> arr;\n    cout << numFactoredBinaryTrees(arr) << endl;\n    return 0;\n}",
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
