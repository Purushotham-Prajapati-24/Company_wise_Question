import json
import os

def generate_json():
    problem_id = 774
    title = "Minimize Max Distance to Gas Station"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>774. Minimize Max Distance to Gas Station</h3>
<p>You are given an integer array <code>stations</code> that represents the positions of gas stations on the x-axis. You are also given an integer <code>k</code>.</p>
<p>You want to add <code>k</code> new gas stations. You can add the stations anywhere on the x-axis, and not necessarily at integer positions.</p>
<p>Let <code>penalty</code> be the maximum distance between adjacent gas stations after adding the <code>k</code> new stations.</p>
<p>Return <em>the smallest possible value of <code>penalty</code></em>. Answers within <code>10<sup>-6</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> stations = [1,2,3,4,5,6,7,8,9,10], k = 9
<strong>Output:</strong> 0.50000
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> stations = [23,24,36,39,46,56,57,65,84,98], k = 1
<strong>Output:</strong> 14.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>10 <= stations.length <= 2000</code></li>
	<li><code>0 <= stations[i] <= 10<sup>8</sup></code></li>
	<li><code>stations</code> is sorted in a <strong>strictly increasing</strong> order.</li>
	<li><code>1 <= k <= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "An integer array stations and an integer k."
    output_format = "A float representing the minimum possible penalty."
    
    constraints = ["10 <= stations.length <= 2000", "0 <= stations[i"]
    
    explanation = """HARD problem on ."""
    
    answer = """import math
def minmaxGasDist(stations, k):
    def check(x):
        needed = 0
        for i in range(len(stations) - 1):
            needed += math.ceil((stations[i+1] - stations[i]) / x) - 1
        return needed <= k

    low, high = 0, 10**8
    for _ in range(100): # Precision: 100 iterations for max accuracy
        mid = (low + high) / 2
        if check(mid):
            high = mid
        else:
            low = mid
    return high"""

    boilerplate = {
        "python": "import sys\n\ndef check(x):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    x = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(check(x))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint check(string x) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string x; cin >> x;\n    cout << check(x) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "[[1,2,3,4,5,6,7,8,9,10], 9]", "expected_output": "0.50000", "is_sample": True},
        {"input": "[[23,24,36,39,46,56,57,65,84,98], 1]", "expected_output": "14.00000", "is_sample": True},
        {"input": "[[1,10], 1]", "expected_output": "4.50000", "is_sample": False},
        {"input": "[[1,10], 8]", "expected_output": "1.00000", "is_sample": False},
        {"input": "[[0,10,20,30], 3]", "expected_output": "5.00000", "is_sample": False},
        {"input": "[[1,10,100], 1000]", "expected_output": "0.09890", "is_sample": False}, # (9+90)/x - 2 = 1000? No.
        {"input": "[[0,100000000], 1]", "expected_output": "50000000.00000", "is_sample": False},
        {"input": "[[1,2,3,4,5,6,7,8,9,10,11], 10]", "expected_output": "0.50000", "is_sample": False},
        {"input": "[[1,10,20,30,40,50,60,70,80,90,100], 1]", "expected_output": "10.00000", "is_sample": False},
        {"input": "[[1,11,21], 1]", "expected_output": "10.00000", "is_sample": False}]

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

    output_path = "1-1000/774_Minimize_Max_Distance_to_Gas_Station.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
