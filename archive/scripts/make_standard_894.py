import json
import os

def generate_json():
    problem_id = 894
    title = "All Possible Full Binary Trees"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>894. All Possible Full Binary Trees</h3>
<p>Given an integer <code>n</code>, return <em>a list of all possible <strong>full binary trees</strong> with</em> <code>n</code> <em>nodes</em>. Each node of each tree in the answer must have <code>Node.val == 0</code>.</p>

<p>Each element of the answer is the root node of one possible tree. You may return the final list of trees in <strong>any order</strong>.</p>

<p>A <strong>full binary tree</strong> is a binary tree where each node has either <code>0</code> or <code>2</code> children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fbtall.png" style="width: 600px; height: 225px;" />
<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[0,0,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 19</code></li>
</ul>"""

    input_format = "An integer n."
    output_format = "A list of level-order traversals (space-separated lists of 0s and nulls)."
    
    constraints = ["1 <= n <= 19", "Full binary tree: 0 or 2 children.", "n must be odd for a full binary tree to exist."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

memo = {0: [], 1: [TreeNode(0)]}

def allPossibleFBT(n):
    if n % 2 == 0: return []
    if n in memo: return memo[n]
    
    res = []
    for i in range(1, n, 2):
        left_trees = allPossibleFBT(i)
        right_trees = allPossibleFBT(n - 1 - i)
        for l in left_trees:
            for r in right_trees:
                root = TreeNode(0)
                root.left = l
                root.right = r
                res.append(root)
    memo[n] = res
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef allPossibleFBT(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    n = input_data[0] if len(input_data) > 0 else \"\"\n    print(allPossibleFBT(n))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint allPossibleFBT(string n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string n; cin >> n;\n    cout << allPossibleFBT(n) << endl;\n    return 0;\n}",
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
