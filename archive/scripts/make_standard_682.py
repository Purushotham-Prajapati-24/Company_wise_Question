import json
import os

def generate_json():
    problem_id = 682
    title = "Baseball Game"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>682. Baseball Game</h3>
<p>You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.</p>

<p>You are given a list of strings <code>operations</code>, where <code>operations[i]</code> is the <code>i<sup>th</sup></code> operation you must apply to the record and is one of the following:</p>

<ul>
	<li>An integer <code>x</code>: Record a new score of <code>x</code>.</li>
	<li><code>'+'</code>: Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.</li>
	<li><code>'D'</code>: Record a new score that is double the previous score. It is guaranteed there will always be one previous score.</li>
	<li><code>'C'</code>: Invalidate the previous score, removing it from the record. It is guaranteed there will always be one previous score.</li>
</ul>

<p>Return <em>the sum of all the scores on the record after applying all the operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> ops = ["5","2","C","D","+"]
<strong>Output:</strong> 30
<strong>Explanation:</strong>
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> ops = ["5","-2","4","C","D","9","+","+"]
<strong>Output:</strong> 27
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> ops = ["1","C"]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= operations.length &lt;= 1000</code></li>
	<li><code>operations[i]</code> is <code>"C"</code>, <code>"D"</code>, <code>"+"</code>, or a string representing an integer in the range <code>[-3 * 10<sup>4</sup>, 3 * 10<sup>4</sup>]</code>.</li>
	<li>For operation <code>"+"</code>, there will always be at least two previous scores on the record.</li>
	<li>For operations <code>"C"</code> and <code>"D"</code>, there will always be at least one previous score on the record.</li>
</ul>"""

    input_format = "A single line containing space-separated operation strings."
    output_format = "A single integer representing the final sum."
    
    constraints = [
        "1 <= operations.length <= 1000",
        "Operations: integer, +, D, C.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To track the scores in a baseball game:
1. **The Data Structure (Stack)**:
   - Use a stack (list in Python) to keep track of valid scores.
2. **Operations**:
   - `integer`: Convert to `int` and push to stack.
   - `'+'`: Peek the last two elements, sum them, and push.
   - `'D'`: Peek the last element, multiply by 2, and push.
   - `'C'`: Pop the last element from the stack.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of operations. Each operation is O(1).
   - Space Complexity: O(N) to store the scores."""
    
    answer = """def calPoints(operations: list[str]) -> int:
    stack = []
    for op in operations:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)"""

    boilerplate = {
        "python": "import sys\n\ndef calPoints(operations):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(calPoints(line.split()))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint calPoints(vector<string>& operations) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int calPoints(String[] operations) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function calPoints(operations) {\n    // User logic\n}",
        "c": "int calPoints(char** operations, int operationsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5 2 C D +", "expected_output": "30", "is_sample": True},
        {"input": "5 -2 4 C D 9 + +", "expected_output": "27", "is_sample": True},
        {"input": "1 C", "expected_output": "0", "is_sample": True},
        {"input": "10 20 +", "expected_output": "60", "is_sample": False},
        {"input": "5 D D", "expected_output": "35", "is_sample": False},
        {"input": "100 -50 C 25", "expected_output": "125", "is_sample": False},
        {"input": "1 2 3 + D C", "expected_output": "6", "is_sample": False},
        {"input": "-1 -2 -3 + D", "expected_output": "-16", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 1000), "expected_output": "1000", "is_sample": False},
        {"input": " ".join(["1", "D"] * 50).split()[0] + " D " * 10, "expected_output": "...", "is_sample": False}
    ]
    # Update stress Case 10 to be predictable
    test_cases[9] = {"input": "1 " + "D " * 10, "expected_output": "2047", "is_sample": False}

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
        "topics": ["Array", "Stack", "Simulation"],
        "companyIndex": 0
    }

    output_path = "601-800/682_Baseball_Game.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
