import json
import os

def generate_json():
    problem_id = 954
    title = "Array of Doubled Pairs"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>954. Array of Doubled Pairs</h3>
<p>Given an integer array of even length <code>arr</code>, return <code>true</code><em> if it is possible to reorder </em><code>arr</code><em> such that </em><code>arr[2 * i + 1] = 2 * arr[2 * i]</code><em> for every </em><code>0 &lt;= i &lt; len(arr) / 2</code><em>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,3,6]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,1,2,6]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,-2,2,-4]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>arr.length</code> is even.</li>
	<li><code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An integer n for length, followed by n space-separated integers."
    output_format = "A boolean (true/false)."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """from collections import Counter

def canReorderDoubled(arr):
    count = Counter(arr)
    for x in sorted(count, key=abs):
        if count[x] > count[2 * x]:
            return False
        count[2 * x] -= count[x]
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef canReorderDoubled(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    arr = input_data[0] if len(input_data) > 0 else \"\"\n    print(canReorderDoubled(arr))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint canReorderDoubled(string arr) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string arr; cin >> arr;\n    cout << canReorderDoubled(arr) << endl;\n    return 0;\n}",
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
