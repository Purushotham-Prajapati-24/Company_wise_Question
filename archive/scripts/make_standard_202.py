import json
import os

def generate_json():
    problem_id = 202
    title = "Happy Number"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>202. Happy Number</h3>
<p>Write an algorithm to determine if a number <code>n</code> is happy.</p>

<p>A <strong>happy number</strong> is a number defined by the following process:</p>

<ul>
	<li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
	<li>Repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1.</li>
	<li>Those numbers for which this process <strong>ends in 1</strong> are happy.</li>
</ul>

<p>Return <code>true</code> <em>if</em> <code>n</code> <em>is a happy number, and</em> <code>false</code> <em>if not</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single positive integer n."
    output_format = "true if the number is happy, false otherwise."
    
    constraints = [
        "1 <= n <= 2^31 - 1",
        "Linear time complexity (logarithmic in value) expected.",
        "Constant space (O(1)) optimization is preferred."
    ]
    
    explanation = """To determine if a number is "happy":
1. **The Process**:
   - Calculate the sum of squares of digits repeatedly.
   - Example (n=19): 19 -> 82 -> 68 -> 100 -> 1 (Happy).
   - If it's not happy, it will eventually enter a cycle (e.g., 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4).
2. **Cycle Detection (Floyd's Algorithm)**:
   - This is similar to link-list cycle detection.
   - Use two pointers: `slow` and `fast`.
   - `slow` performs the operation once per step.
   - `fast` performs the operation twice per step.
   - If `fast` reaches 1, the number is happy.
   - If `slow` and `fast` meet at any other number, they've entered a cycle, and the number is not happy.
3. **Complexity**:
   - Time Complexity: O(log N) - The number of digits in `n` is log10(N), and the cost of summing squares of digits is proportional to the number of digits.
   - Space Complexity: O(1) as we only use two variables for the pointers."""
    
    answer = """def isHappy(n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum
        
    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        
    return fast == 1"""

    boilerplate = {
        "python": "import sys\n\ndef isHappy(n):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        print(\"true\" if isHappy(int(data)) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nbool isHappy(int n) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        cout << (isHappy(n) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean isHappy(int n) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            int n = Integer.parseInt(line.trim());\n            System.out.println(new Solution().isHappy(n) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isHappy(n) {\n    // User logic\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input !== '') {\n    console.log(isHappy(parseInt(input)) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nbool isHappy(int n) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%s\\n\", isHappy(n) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "19", "expected_output": "true", "is_sample": True},
        {"input": "2", "expected_output": "false", "is_sample": True},
        {"input": "7", "expected_output": "true", "is_sample": False},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "4", "expected_output": "false", "is_sample": False},
        {"input": "100", "expected_output": "true", "is_sample": False},
        {"input": "10", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "2147483647", "expected_output": "false", "is_sample": False},
        {"input": "1111111", "expected_output": "false", "is_sample": False},
        {"input": "777", "expected_output": "false", "is_sample": False}
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
        "topics": ["Hash Table", "Math", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/202_Happy_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
