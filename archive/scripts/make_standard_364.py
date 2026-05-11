import json
import os

def generate_json():
    problem_id = 364
    title = "Nested List Weight Sum II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>364. Nested List Weight Sum II</h3>
<p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists.</p>

<p>The <strong>depth</strong> of an integer is the number of lists that it is inside of. For example, the nested list <code>[1,[2,2],[[3],2],1]</code> has each integer's value and its depth as follows:</p>

<ul>
	<li><code>1</code> at depth 1</li>
	<li><code>2</code> at depth 2 (from <code>[2,2]</code>)</li>
	<li><code>2</code> at depth 2 (from <code>[2,2]</code>)</li>
	<li><code>3</code> at depth 3 (from <code>[[3]]</code>)</li>
	<li><code>2</code> at depth 2 (from <code>[[3],2]</code>)</li>
	<li><code>1</code> at depth 1</li>
</ul>

<p>The <strong>weight</strong> of an integer is <code>maxDepth - (the depth of the integer) + 1</code>, where <code>maxDepth</code> is the maximum depth of any integer in the list.</p>

<p>Return <em>the sum of each integer in </em><code>nestedList</code><em> multiplied by its <strong>weight</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex1.png" style="width: 426px; height: 181px;" />
<pre><strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Four 1's at depth 2, one 2 at depth 1.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex2.png" style="width: 612px; height: 201px;" />
<pre><strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> 17
<strong>Explanation:</strong> One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.
1*3 + 4*2 + 6*1 = 17.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 50</code></li>
	<li>The values of integers in the nested list is in the range <code>[-100, 100]</code>.</li>
	<li>The maximum depth of any integer is less than or equal to <code>50</code>.</li>
</ul>"""

    input_format = "A nested list of integers and list of objects."
    output_format = "An integer representing the weighted sum."
    
    constraints = ["1 <= nestedList.length <= 50", "-100 <= value <= 100", "maxDepth <= 50"]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """class Solution:
    def depthSumInverse(self, nestedList):
        unweighted = 0
        weighted = 0
        while nestedList:
            next_level = []
            for item in nestedList:
                if isinstance(item, int):
                    unweighted += item
                else:
                    for sub_item in item:
                        next_level.append(sub_item)
            weighted += unweighted
            nestedList = next_level
        return weighted"""

    boilerplate = {
        "python": "import sys\n\ndef depthSumInverse(nestedList):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    nestedList = input_data[0].strip() if len(input_data) > 0 else \"\"\n    print(depthSumInverse(nestedList))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint depthSumInverse(string nestedList) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string nestedList; cin >> nestedList;\n    cout << depthSumInverse(nestedList) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "[[1,1],2,[1,1]]", "expected_output": "8", "is_sample": True},
        {"input": "[1,[4,[6]]]", "expected_output": "17", "is_sample": True},
        {"input": "[[[5]]]", "expected_output": "5", "is_sample": False},
        {"input": "[-1,[-2,[-3]]]", "expected_output": "-10", "is_sample": False},
        {"input": "[1,2,3,4,5]", "expected_output": "15", "is_sample": False},
        {"input": "[[1],[2],[3]]", "expected_output": "6", "is_sample": False},
        {"input": "[0,[0,[0]]]", "expected_output": "0", "is_sample": False},
        # Stress tests
        {"input": str([1]*50), "expected_output": "50", "is_sample": False},
        {"input": str([[[[1]]]] * 10), "expected_output": "10", "is_sample": False},]

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
