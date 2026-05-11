import json
import os

def generate_json():
    problem_id = 258
    title = "Add Digits"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>258. Add Digits</h3>
<p>Given an integer <code>num</code>, repeatedly add all its digits until the result has only one digit, and return it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 38
<strong>Output:</strong> 2
<strong>Explanation:</strong> The process is
38 --&gt; 3 + 8 --&gt; 11
11 --&gt; 1 + 1 --&gt; 2 
Since 2 has only one digit, return it.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without any loop/recursion in <code>O(1)</code> runtime?</p>"""

    input_format = "An integer `num`."
    output_format = "A single-digit integer."
    
    constraints = [
        "0 <= num <= 2,147,483,647"
    ]
    
    explanation = """The problem asks for the digital root of a number. 
1. **Simulation**: We can repeatedly sum the digits using a loop until the result is less than 10.
2. **O(1) Mathematical Approach**:
   - The digital root follows a periodic pattern every 9 numbers.
   - For `num = 0`, the answer is 0.
   - For `num % 9 == 0` (and `num > 0`), the answer is 9.
   - For other cases, the answer is `num % 9`.
   - Formula: `1 + (num - 1) % 9` for `num > 0`.
3. **Complexity Analysis**:
   - Time: O(1).
   - Space: O(1)."""
    
    answer = """class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9"""

    boilerplate = {
        "python": "import sys\n\ndef addDigits(num: int) -> int:\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        num = int(line)\n        print(addDigits(num))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint addDigits(int num) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int num;\n    if (cin >> num) {\n        cout << addDigits(num) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int addDigits(int num) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            System.out.println(new Solution().addDigits(sc.nextInt()));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction addDigits(num) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    console.log(addDigits(parseInt(input)));\n}",
        "c": "#include <stdio.h>\n\nint addDigits(int num) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int num;\n    if (scanf(\"%d\", &num) == 1) {\n        printf(\"%d\\n\", addDigits(num));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "38", "expected_output": "2", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "9", "expected_output": "9", "is_sample": False},
        {"input": "10", "expected_output": "1", "is_sample": False},
        {"input": "11", "expected_output": "2", "is_sample": False},
        {"input": "18", "expected_output": "9", "is_sample": False},
        {"input": "99", "expected_output": "9", "is_sample": False},
        # Stress cases
        {"input": str(2**31-1), "expected_output": "1", "is_sample": False}, # 2147483647 -> 2+1+4+7+4+8+3+6+4+7=46 -> 4+6=10 -> 1+0=1
        {"input": str(10**100 - 1), "expected_output": "9", "is_sample": False}, # Not in constraints but good for math check
        {"input": "123456789", "expected_output": "9", "is_sample": False}
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
        "topics": ["Math", "Simulation", "Number Theory"],
        "companyIndex": 0
    }

    output_path = "201-400/258_Add_Digits.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
