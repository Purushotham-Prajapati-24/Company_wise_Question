import json
import os

def generate_json():
    problem_id = 650
    title = "2 Keys Keyboard"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>650. 2 Keys Keyboard</h3>
<p>There is only one character <code>'A'</code> on the screen of a notepad. You can perform one of two operations on this notepad for each step:</p>

<ul>
	<li><b>Copy All</b>: You can copy all the characters currently on the screen (a partial copy is not allowed).</li>
	<li><b>Paste</b>: You can paste the characters which are last copied.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the minimum number of operations to get the character <code>'A'</code> exactly <code>n</code> times on the screen</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>"""

    input_format = "A single integer n."
    output_format = "A single integer representing the minimum operations."
    
    constraints = [
        "1 <= n <= 1000",
        "O(sqrt(N)) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To get exactly $n$ 'A's with minimum operations:
1. **The Insight**:
   - Each operation either copies the existing count or pastes the last copied count.
   - This is equivalent to factorizing $n$. 
   - Suppose we reach $x$ characters and want to reach $n$. If $n$ is divisible by $x$, say $n = x \times k$, we can achieve $n$ by:
     - 1 Copy All (to copy $x$ characters).
     - $k-1$ Pastes (each adds $x$ characters).
     - Total operations for this step: $k$.
   - Thus, the total minimum operations is the **sum of prime factors** of $n$.
2. **Algorithm**:
   - Start with `d = 2`.
   - While $n > 1$:
     - While $n$ is divisible by $d$:
       - Add $d$ to total operations.
       - Divide $n$ by $d$.
     - Increment $d$.
3. **Complexity**:
   - Time Complexity: O(sqrt(N)).
   - Space Complexity: O(1)."""
    
    answer = """def minSteps(n: int) -> int:
    if n == 1: return 0
    res = 0
    d = 2
    while n > 1:
        while n % d == 0:
            res += d
            n //= d
        d += 1
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef minSteps(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(minSteps(int(line)))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint minSteps(int n) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int minSteps(int n) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function minSteps(n) {\n    // User logic\n}",
        "c": "int minSteps(int n) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3", "expected_output": "3", "is_sample": True},
        {"input": "1", "expected_output": "0", "is_sample": True},
        {"input": "2", "expected_output": "2", "is_sample": False},
        {"input": "4", "expected_output": "4", "is_sample": False},
        {"input": "6", "expected_output": "5", "is_sample": False},
        {"input": "8", "expected_output": "6", "is_sample": False},
        {"input": "9", "expected_output": "6", "is_sample": False},
        {"input": "25", "expected_output": "10", "is_sample": False},
        # Stress cases
        {"input": "1000", "expected_output": "21", "is_sample": False},
        {"input": "997", "expected_output": "997", "is_sample": False}
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
        "companyIndex": 0
    }

    output_path = "601-800/650_2_Keys_Keyboard.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
