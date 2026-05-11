import json
import os

def generate_json():
    problem_id = 1137
    title = "N-th Tribonacci Number"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1137. N-th Tribonacci Number</h3>
<p>The Tribonacci sequence <code>T<sub>n</sub></code> is defined as follows:&nbsp;</p>

<p><code>T<sub>0</sub> = 0</code>, <code>T<sub>1</sub> = 1</code>, <code>T<sub>2</sub> = 1</code>, and <code>T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub></code> for <code>n &gt;= 0</code>.</p>

<p>Given <code>n</code>, return the value of <code>T<sub>n</sub></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
T_3 = T_0 + T_1 + T_2 = 0 + 1 + 1 = 2
T_4 = T_1 + T_2 + T_3 = 1 + 1 + 2 = 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 25
<strong>Output:</strong> 1389537
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer &lt;= 2^31 - 1</code>.</li>
</ul>"""

    input_format = "A single integer n."
    output_format = "The n-th Tribonacci number."
    
    constraints = [
        "0 <= n <= 37",
        "Result fits in 32-bit integer (max ~2*10^9).",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To compute the n-th Tribonacci number efficiently:
1. **Definition**:
   - $T_0 = 0, T_1 = 1, T_2 = 1$
   - $T_n = T_{n-1} + T_{n-2} + T_{n-3}$ for $n \ge 3$.
2. **Iterative Approach (Bottom-Up)**:
   - Instead of recursion (which is O(3^N) without memoization), use three variables to store the last three values.
   - Start with `a=0, b=1, c=1`.
   - In each step from 3 to $n$, compute `next = a + b + c`, then shift: `a=b, b=c, c=next`.
3. **Complexity**:
   - Time Complexity: O(N) as we iterate from 3 to $n$.
   - Space Complexity: O(1) as we only use a fixed number of variables regardless of $n$."""
    
    answer = """def tribonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c"""

    boilerplate = {
        "python": "import sys\n\ndef tribonacci(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(tribonacci(int(line)))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint tribonacci(int n) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int tribonacci(int n) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function tribonacci(n) {\n    // User logic\n}",
        "c": "int tribonacci(int n) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "4", "expected_output": "4", "is_sample": True},
        {"input": "25", "expected_output": "1389537", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "2", "expected_output": "1", "is_sample": False},
        {"input": "3", "expected_output": "2", "is_sample": False},
        {"input": "10", "expected_output": "149", "is_sample": False},
        # Stress cases
        {"input": "37", "expected_output": "2082876103", "is_sample": False},
        {"input": "30", "expected_output": "15902591", "is_sample": False},
        {"input": "36", "expected_output": "1132436852", "is_sample": False}
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
        "topics": ["Dynamic Programming", "Math", "Memoization"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1137_N_th_Tribonacci_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
