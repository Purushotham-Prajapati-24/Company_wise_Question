import json
import os

def generate_json():
    problem_id = 907
    title = "Sum of Subarray Minimums"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>907. Sum of Subarray Minimums</h3>
<p>Given an array of integers <code>arr</code>, find the sum of <code>min(b)</code>, where <code>b</code> ranges over every (contiguous) subarray of <code>arr</code>. Since the answer may be large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,2,4]
<strong>Output:</strong> 17
<strong>Explanation:</strong> 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 3 + 1 + 2 + 4 + 1 + 1 + 2 + 1 + 1 + 1 = 17.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [11,81,94,43,3]
<strong>Output:</strong> 444
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer n, followed by n space-separated integers."
    output_format = "An integer representing the sum of subarray minimums modulo 10^9 + 7."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    left = [-1] * n
    right = [n] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
        
    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
        
    res = 0
    for i in range(n):
        res = (res + arr[i] * (i - left[i]) * (right[i] - i)) % MOD
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef sumSubarrayMins(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    arr = input_data[0] if len(input_data) > 0 else \"\"\n    print(sumSubarrayMins(arr))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint sumSubarrayMins(string arr) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string arr; cin >> arr;\n    cout << sumSubarrayMins(arr) << endl;\n    return 0;\n}",
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
