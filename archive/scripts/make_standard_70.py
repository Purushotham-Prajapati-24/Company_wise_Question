import json
import os

def generate_json():
    problem_id = 70
    title = "Climbing Stairs"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>70. Climbing Stairs</h3>
<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>"""

    input_format = "A single integer 'n' representing the number of steps."
    output_format = "An integer representing the number of distinct ways to reach the top."
    
    constraints = [
        "1 <= n <= 45"
    ]
    
    explanation = """To find the number of ways to climb a staircase of n steps:
1. **Recurrence Relation**: To reach step `n`, you must have come from either step `n-1` (by taking 1 step) or step `n-2` (by taking 2 steps).
   - Therefore, the total number of ways to reach step `n` is `Ways(n) = Ways(n-1) + Ways(n-2)`.
2. **Base Cases**:
   - `Ways(1) = 1` (Only one way: [1])
   - `Ways(2) = 2` (Two ways: [1, 1], [2])
3. **Dynamic Programming Strategy**: This is similar to the Fibonacci sequence. We can calculate the value iteratively to save space.
4. **Complexity**:
   - Time Complexity: O(n).
   - Space Complexity: O(1) by using only two variables to store the previous results."""
    
    answer = """def climbStairs(n):
    if n <= 2:
        return n
        
    first = 1
    second = 2
    
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
        
    return second"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\n\ndef climbStairs(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        n = int(input_data)\n        print(climbStairs(n))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint climbStairs(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        cout << climbStairs(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int climbStairs(int n) {\n        // User logic\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            System.out.println(climbStairs(n));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction climbStairs(n) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    console.log(climbStairs(parseInt(input)));\n}",
        "c": "#include <stdio.h>\n\nint climbStairs(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%d\\n\", climbStairs(n));\n    }\n    return 0;\n}"
    }

    def _solve(n):
        if n <= 2: return n
        a, b = 1, 2
        for _ in range(3, n+1): a, b = b, a+b
        return b

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2", "expected_output": "2", "is_sample": True},
        {"input": "3", "expected_output": "3", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "4", "expected_output": "5", "is_sample": False},
        {"input": "5", "expected_output": "8", "is_sample": False},
        {"input": "10", "expected_output": "89", "is_sample": False},
        {"input": "20", "expected_output": "10946", "is_sample": False},
        # Last three: Stress tests
        {"input": "40", "expected_output": str(_solve(40)), "is_sample": False},
        {"input": "44", "expected_output": str(_solve(44)), "is_sample": False},
        {"input": "45", "expected_output": str(_solve(45)), "is_sample": False}
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
        "topics": ["Math", "Dynamic Programming", "Memoization"],
        "companyIndex": 0
    }

    output_path = "1-200/70_Climbing_Stairs.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
