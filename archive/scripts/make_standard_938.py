import json
import os

def generate_json():
    problem_id = 938
    title = "Range Sum of BST"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>938. Range Sum of BST</h3>
<p>Given the <code>root</code> node of a binary search tree and two integers <code>low</code> and <code>high</code>, return <em>the sum of values of all nodes with a value in the <strong>inclusive</strong> range </em><code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/14/bst1.jpg" style="width: 400px; height: 267px;" />
<pre>
<strong>Input:</strong> root = [10,5,15,3,7,null,18], low = 7, high = 15
<strong>Output:</strong> 32
<strong>Explanation:</strong> Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/14/bst2.jpg" style="width: 400px; height: 335px;" />
<pre>
<strong>Input:</strong> root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<strong>Output:</strong> 23
<strong>Explanation:</strong> Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>5</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A level-order traversal of the BST, followed by low and high."
    output_format = "An integer representing the sum."
    
    constraints = ["Nodes: 1 to 20", "000.", "Values: 1 to 100", "000.", "BST properties apply."]
    
    explanation = """EASY problem on ."""
    
    answer = """def rangeSumBST(root, low, high):
    res = 0
    def dfs(node):
        nonlocal res
        if not node: return
        if low <= node.val <= high:
            res += node.val
        if node.val > low:
            dfs(node.left)
        if node.val < high:
            dfs(node.right)
    dfs(root)
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef dfs(node):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    node = input_data[0] if len(input_data) > 0 else \"\"\n    print(dfs(node))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint dfs(string node) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string node; cin >> node;\n    cout << dfs(node) << endl;\n    return 0;\n}",
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
