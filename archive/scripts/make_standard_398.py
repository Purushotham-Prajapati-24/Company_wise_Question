import json
import os

def generate_json():
    problem_id = 398
    title = "Random Pick Index"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>398. Random Pick Index</h3>
<p>Given an integer array <code>nums</code> with possible duplicates, randomly output the index of a given <code>target</code> number. You can assume that the given target number must exist in the array.</p>

<p>Implement the <code>Solution</code> class:</p>

<ul>
	<li><code>Solution(int[] nums)</code> Initializes the object with the array <code>nums</code>.</li>
	<li><code>int pick(int target)</code> Picks a random index <code>i</code> from <code>nums</code> such that <code>nums[i] == target</code>. If there are multiple valid i's, each index should have the same probability of being returned.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
<strong>Output</strong>
[null, 4, 0, 2]

<strong>Explanation</strong>
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have a probability of 1/3.
solution.pick(1); // It should return 0. Since there is only one 1, it must return 0.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have a probability of 1/3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2*10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>target</code> is guaranteed to be in <code>nums</code>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>pick</code>.</li>
</ul>"""

    input_format = "An array of integers and a sequence of pick commands."
    output_format = "A list of results for each command."
    
    constraints = ["1 <= nums.length <= 2*10^4", "Target is guaranteed to be in nums.", "At most 10^4 calls for pick."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """import random
from collections import defaultdict

class Solution:
    def __init__(self, nums):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        return random.choice(self.indices[target])"""

    boilerplate = {
        "python": "import sys\n\ndef pick(target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    target = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(pick(target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint pick(string target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string target; cin >> target;\n    cout << pick(target) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": '["Solution", "pick", "pick", "pick"]\\n[[[1, 2, 3, 3, 3]], [3], [1], [3]]', "expected_output": "[null, 2, 0, 4]", "is_sample": True},
        {"input": '["Solution", "pick"]\\n[[[1]], [1]]', "expected_output": "[null, 0]", "is_sample": False},
        {"input": '["Solution", "pick", "pick"]\\n[[[1, 1, 1]], [1], [1]]', "expected_output": "[null, 0, 1]", "is_sample": False},
        # Stress tests]

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
