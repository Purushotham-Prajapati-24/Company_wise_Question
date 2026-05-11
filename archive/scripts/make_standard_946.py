import json
import os

def generate_json():
    problem_id = 946
    title = "Validate Stack Sequences"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>946. Validate Stack Sequences</h3>
<p>Given two integer arrays <code>pushed</code> and <code>popped</code> each with distinct values, return <code>true</code><em> if this could have been the result of a sequence of push and pop operations on an initially empty stack, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> 1 cannot be popped before 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pushed.length &lt;= 1000</code></li>
	<li><code>0 &lt;= pushed[i] &lt;= 1000</code></li>
	<li>All the elements of <code>pushed</code> are <strong>distinct</strong>.</li>
	<li><code>popped.length == pushed.length</code></li>
	<li><code>popped</code> is a permutation of <code>pushed</code>.</li>
</ul>"""

    input_format = "An integer n for length, followed by n space-separated integers for pushed, then n more for popped."
    output_format = "A boolean (true/false)."
    
    constraints = ["1 <= pushed.length <= 1000", "popped is a permutation of pushed.", "pushed elements are distinct."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def validateStackSequences(pushed, popped):
    stack = []
    i = 0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return i == len(popped)"""

    boilerplate = {
        "python": "import sys\n\ndef validateStackSequences(pushed, popped):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    pushed = input_data[0] if len(input_data) > 0 else \"\"\n    popped = input_data[1] if len(input_data) > 1 else \"\"\n    print(validateStackSequences(pushed, popped))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint validateStackSequences(string pushed, string popped) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string pushed; cin >> pushed;\n    string popped; cin >> popped;\n    cout << validateStackSequences(pushed, popped) << endl;\n    return 0;\n}",
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
