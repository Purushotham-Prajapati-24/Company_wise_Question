import json
import os

def generate_json():
    problem_id = 1221
    title = "Split a String in Balanced Strings"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1221. Split a String in Balanced Strings</h3>
<p><strong>Balanced</strong> strings are those that have an equal quantity of <code>'L'</code> and <code>'R'</code> characters.</p>

<p>Given a <strong>balanced</strong> string <code>s</code>, split it into some number of substrings such that:</p>

<ul>
	<li>Each substring is balanced.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of balanced strings you can obtain.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "RLRRLLRLRL"
<strong>Output:</strong> 4
<strong>Explanation:</strong> s can be split into "RL", "RRLL", "RL", "RL", each substring contains an equal number of 'L' and 'R'.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "RLRRRLLRLL"
<strong>Output:</strong> 2
<strong>Explanation:</strong> s can be split into "RL", "RRRLLRLL", each substring contains an equal number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "RL", "LL", because tokens "RR" and "LL" are not balanced.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "LLLLRRRR"
<strong>Output:</strong> 1
<strong>Explanation:</strong> s can be split into "LLLLRRRR".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>'L'</code> or <code>'R'</code>.</li>
	<li><code>s</code> is a balanced string.</li>
</ul>"""

    input_format = "A single line containing the balanced string s."
    output_format = "An integer representing the maximum number of balanced substrings."
    
    constraints = [
        "2 <= s.length <= 1000",
        "s contains only 'L' and 'R'.",
        "s is already balanced.",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To maximize the number of balanced strings:
1. **Greedy Approach**:
   - We want to split the string as soon as we encounter a balanced substring.
   - A substring is balanced if the number of 'L's equals the number of 'R's.
2. **Implementation**:
   - Use a counter `balance` initialized to 0.
   - Iterate through the string:
     - If the character is 'R', increment `balance`.
     - If the character is 'L', decrement `balance`.
     - Whenever `balance` becomes 0, it means we have reached a point where the number of 'L's and 'R's encountered so far are equal.
     - Increment a `count` variable whenever `balance == 0`.
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of the string `s`.
   - Space Complexity: O(1) as we only use a few integer variables."""
    
    answer = """def balancedStringSplit(s: str) -> int:
    count = 0
    balance = 0
    for char in s:
        if char == 'R':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            count += 1
    return count"""

    boilerplate = {
        "python": "import sys\n\ndef balancedStringSplit(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(balancedStringSplit(line))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint balancedStringSplit(string s) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int balancedStringSplit(String s) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function balancedStringSplit(s) {\n    // User logic\n}",
        "c": "int balancedStringSplit(char* s) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "RLRRLLRLRL", "expected_output": "4", "is_sample": True},
        {"input": "RLRRRLLRLL", "expected_output": "2", "is_sample": True},
        {"input": "LLLLRRRR", "expected_output": "1", "is_sample": True},
        {"input": "RRLL", "expected_output": "1", "is_sample": False},
        {"input": "RLRLRL", "expected_output": "3", "is_sample": False},
        {"input": "RLLRLLRR", "expected_output": "2", "is_sample": False},
        {"input": "RRLRLL", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "RL" * 500, "expected_output": "500", "is_sample": False},
        {"input": "R" * 500 + "L" * 500, "expected_output": "1", "is_sample": False},
        {"input": ("RRLL" * 250), "expected_output": "250", "is_sample": False}
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
        "topics": ["String", "Greedy", "Counting"],
        "companyIndex": 0
    }

    output_path = "1201-1400/1221_Split_a_String_in_Balanced_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
