import json
import os

def generate_json():
    problem_id = 897
    title = "Increasing Order Search Tree"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>897. Increasing Order Search Tree</h3>
<p>Given the <code>root</code> of a binary search tree, rearrange the tree in <strong>in-order</strong> so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg" style="width: 600px; height: 350px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg" style="width: 300px; height: 114px;" />
<pre>
<strong>Input:</strong> root = [5,1,7]
<strong>Output:</strong> [1,null,5,null,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree will be in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "A level-order traversal of the BST."
    output_format = "A level-order traversal of the rearranged tree (a right-only chain)."
    
    constraints = ["Nodes: 1 to 100.", "BST values: 0 to 1000.", "Reshape into right-skewed tree."]
    
    explanation = """EASY problem on ."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root):
    dummy = TreeNode(0)
    curr = dummy
    
    def inorder(node):
        nonlocal curr
        if not node: return
        inorder(node.left)
        node.left = None
        curr.right = node
        curr = node
        inorder(node.right)
        
    inorder(root)
    return dummy.right"""

    boilerplate = {
        "python": "import sys\n\ndef inorder(node):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    node = input_data[0] if len(input_data) > 0 else \"\"\n    print(inorder(node))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint inorder(string node) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string node; cin >> node;\n    cout << inorder(node) << endl;\n    return 0;\n}",
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
