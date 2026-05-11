import json
import os


def generate_json():
    problem_id = 390
    title = "Elimination Game"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>390. Elimination Game</h3>
<p>You have a list of fixed integers <code>n</code> from <code>1</code> to <code>n</code> in strictly increasing order.</p>

<p>The elimination process follows these steps, alternating direction:</p>

<ul>
	<li><strong>Left-to-right pass:</strong> Remove the first number and then every other number from the remaining list until the end is reached.</li>
	<li><strong>Right-to-left pass:</strong> From the numbers still in the list, remove the rightmost number and then every other number from the remaining list, working backward towards the beginning.</li>
</ul>

<p>This alternating pattern continues until only a single number is left. Return <em>the final remaining number</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 9
<strong>Output:</strong> 6
<strong>Explanation:</strong>
1 2 3 4 5 6 7 8 9
2 4 6 8 (from left to right)
2 6 (from right to left)
6 (from left to right)
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = """An integer n."""
    output_format = """An integer representing the last remaining number."""
    
    constraints = ["1 <= n <= 10^9", "O(log n) time complexity."]
    
    explanation = """To find the last remaining number in the elimination game, we track the 'head' (the first element of the current sequence).

### Key Observations:
1. **Head shifts**: The head only moves under two conditions:
   - When we eliminate from **left to right** (the current head is always removed).
   - When we eliminate from **right to left** AND the number of elements remaining is **odd** (the last element and first element are removed in the same pass of every-other-one).
2. **Step size**: After each pass, the distance between remaining elements doubles (1, 2, 4, 8...).
3. **Sequence reduction**: The number of elements remaining is halved in each step.

### Algorithm Steps:
1. Initialize `head = 1`, `step = 1`, `remaining = n`, and `left = True`.
2. While `remaining > 1`:
   - If `left` is `True` OR `remaining` is odd:
     - Update `head = head + step`.
   - Halve `remaining`: `remaining = remaining // 2`.
   - Double `step`: `step = step * 2`.
   - Flip `left`: `left = !left`.
3. Return `head`.

### Complexity:
- **Time Complexity**: $O(\log N)$, as we halve the remaining count in each step.
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left = True
        while remaining > 1:
            if left or remaining % 2 == 1:
                head = head + step
            remaining //= 2
            step *= 2
            left = not left
        return head"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def lastRemaining(self, n: int) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        n = int(line)\n        sol = Solution()\n        print(json.dumps(sol.lastRemaining(n)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int lastRemaining(int n) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    int n;\n    if (cin >> n) {\n        Solution sol;\n        cout << sol.lastRemaining(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int lastRemaining(int n) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            Solution sol = new Solution();\n            System.out.println(sol.lastRemaining(n));\n        }\n    }\n}",
        "javascript": "var lastRemaining = function(n) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const n = parseInt(input);\n    console.log(JSON.stringify(lastRemaining(n)));\n}",
        "c": "#include <stdio.h>\n\nint lastRemaining(int n) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%d\\n\", lastRemaining(n));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "9", "expected_output": "6", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        # 5 Diverse
        {"input": "2", "expected_output": "2", "is_sample": False},
        {"input": "3", "expected_output": "2", "is_sample": False},
        {"input": "4", "expected_output": "2", "is_sample": False},
        {"input": "5", "expected_output": "2", "is_sample": False},
        {"input": "6", "expected_output": "4", "is_sample": False},
        # 3 Stress
        {"input": "100", "expected_output": "54", "is_sample": False},
        {"input": "1000", "expected_output": "510", "is_sample": False},
        {"input": "1000000", "expected_output": "484288", "is_sample": False}
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
        "topics": ["Recursion", "Recursion", "Mathematics"],
        "companyIndex": 0
    }

    output_path = "301-500/390_Elimination_Game.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
