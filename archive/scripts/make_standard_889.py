import json
import os

def generate_json():
    problem_id = 889
    title = "Construct Binary Tree from Preorder and Postorder Traversal"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>889. Construct Binary Tree from Preorder and Postorder Traversal</h3>
<p>Given two integer arrays, <code>preorder</code> and <code>postorder</code> where <code>preorder</code> is the preorder traversal of a binary tree of <strong>distinct</strong> values and <code>postorder</code> is the postorder traversal of the same tree, reconstruct and return <em>the binary tree</em>.</p>

<p>If there exist multiple answers, you can return <strong>any</strong> of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg" style="width: 304px; height: 158px;" />
<pre>
<strong>Input:</strong> preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
<strong>Output:</strong> [1,2,3,4,5,6,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> preorder = [1], postorder = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= preorder.length &lt;= 30</code></li>
	<li><code>1 &lt;= preorder[i] &lt;= preorder.length</code></li>
	<li>All the values of <code>preorder</code> are <strong>unique</strong>.</li>
	<li><code>postorder.length == preorder.length</code></li>
	<li><code>1 &lt;= postorder[i] &lt;= postorder.length</code></li>
	<li>All the values of <code>postorder</code> are <strong>unique</strong>.</li>
	<li>It is guaranteed that <code>preorder</code> and <code>postorder</code> are the preorder traversal and postorder traversal of the same binary tree.</li>
</ul>"""

    input_format = "An integer n, followed by n integers for preorder and n integers for postorder."
    output_format = "A level-order traversal of the reconstructed tree."
    
    constraints = ["1 <= n <= 30", "Values are unique.", "Preorder and Postorder are consistent."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(preorder, postorder):
    if not preorder: return None
    root = TreeNode(preorder[0])
    if len(preorder) == 1: return root
    
    # Second element is left child root
    left_root_val = preorder[1]
    # Find its index in postorder
    idx = postorder.index(left_root_val)
    
    # Left subtree has idx + 1 elements
    root.left = constructFromPrePost(preorder[1:idx+2], postorder[:idx+1])
    root.right = constructFromPrePost(preorder[idx+2:], postorder[idx+1:-1])
    
    return root"""

    boilerplate = {
        "python": "import sys\n\ndef constructFromPrePost(preorder, postorder):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    preorder = input_data[0] if len(input_data) > 0 else \"\"\n    postorder = input_data[1] if len(input_data) > 1 else \"\"\n    print(constructFromPrePost(preorder, postorder))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint constructFromPrePost(string preorder, string postorder) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string preorder; cin >> preorder;\n    string postorder; cin >> postorder;\n    cout << constructFromPrePost(preorder, postorder) << endl;\n    return 0;\n}",
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
