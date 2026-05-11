import json
import os

def generate_json():
    problem_id = 458
    title = "Poor Pigs"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>458. Poor Pigs</h3>
<p>There are <code>buckets</code> buckets of liquid, where <strong>exactly one</strong> of the buckets is poisonous. To figure out which one is poisonous, you can feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have <code>minutesToTest</code> minutes to determine which bucket is poisonous, and you have to wait <code>minutesToDie</code> minutes for a poison to take effect.</p>

<p>You can feed the pigs according to these steps:</p>

<ol>
	<li>Choose some pigs to feed.</li>
	<li>For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time. Each pig can feed from any number of buckets, and each bucket can be fed from by any number of pigs.</li>
	<li>Wait for <code>minutesToDie</code> minutes. You may not feed any other pigs during this time.</li>
	<li>After <code>minutesToDie</code> minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.</li>
	<li>Repeat this process until you run out of time.</li>
</ol>

<p>Given <code>buckets</code>, <code>minutesToDie</code>, and <code>minutesToTest</code>, return <em>the <strong>minimum</strong> number of pigs needed to figure out which bucket is poisonous within the allotted time</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> buckets = 4, minutesToDie = 15, minutesToTest = 15
<strong>Output:</strong> 2
<strong>Explanation:</strong> At time 0, feed the first pig buckets 1 and 2, and feed the second pig buckets 1 and 3.
At time 15, there are 4 possible outcomes:
- If only the 1st pig dies, then bucket 2 must be poisonous.
- If only the 2nd pig dies, then bucket 3 must be poisonous.
- If both pigs die, then bucket 1 must be poisonous.
- If neither pig dies, then bucket 4 must be poisonous.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> buckets = 4, minutesToDie = 15, minutesToTest = 30
<strong>Output:</strong> 2
<strong>Explanation:</strong> At time 0, feed the first pig bucket 1, and feed the second pig bucket 2.
At time 15, there are 4 possible outcomes:
- If only the 1st pig dies, then bucket 1 must be poisonous.
- If only the 2nd pig dies, then bucket 2 must be poisonous.
- If both pigs die, then the system is invalid, or you can say it's bucket 1 and 2, but only one is poisonous.
- If neither pig dies, then at time 15, feed the first pig bucket 3, and feed the second pig bucket 4.
... (this can be optimized but the point is 2 pigs are enough)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= buckets &lt;= 1000</code></li>
	<li><code>1 &lt;= minutesToDie &lt;= minutesToTest &lt;= 1000</code></li>
</ul>"""

    input_format = "Three integers: buckets, minutesToDie, and minutesToTest."
    output_format = "Integer representing the minimum number of pigs needed."
    
    constraints = ["1 <= buckets <= 1000", "1 <= minutesToDie <= minutesToTest <= 1000"]
    
    explanation = """HARD problem on ."""
    
    answer = """import math

def solve(buckets, minutesToDie, minutesToTest):
    rounds = minutesToTest // minutesToDie
    states = rounds + 1
    # states^p >= buckets => p >= log(buckets) / log(states)
    return math.ceil(math.log(buckets) / math.log(states) - 1e-10)"""

    boilerplate = {
        "python": "import sys\n\ndef solve(buckets, minutesToDie, minutesToTest):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    buckets = input_data[0] if len(input_data) > 0 else \"\"\n    minutesToDie = input_data[1] if len(input_data) > 1 else \"\"\n    minutesToTest = input_data[2] if len(input_data) > 2 else \"\"\n    print(solve(buckets, minutesToDie, minutesToTest))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint solve(string buckets, string minutesToDie, string minutesToTest) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string buckets; cin >> buckets;\n    string minutesToDie; cin >> minutesToDie;\n    string minutesToTest; cin >> minutesToTest;\n    cout << solve(buckets, minutesToDie, minutesToTest) << endl;\n    return 0;\n}",
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
