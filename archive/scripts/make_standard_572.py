import json
import os

def generate_json():
    problem_id = 572
    title = "Subtree of Another Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>572. Subtree of Another Tree</h3>
<p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values as <code>subRoot</code>, and <code>false</code> otherwise.</p>

<p>A subtree of a binary tree <code>tree</code> is a tree that consists of a node in <code>tree</code> and all of this node's descendants. The tree <code>tree</code> could also be considered as a subtree of itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
<pre>
<strong>Input:</strong> root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>root</code> tree is in the range <code>[1, 2000]</code>.</li>
	<li>The number of nodes in the <code>subRoot</code> tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "Two level-order traversals (space separated integers) representing 'root' and 'subRoot'."
    output_format = "A boolean value (True or False)."
    
    constraints = [
        "Nodes in root range: [1, 2000].",
        "Nodes in subRoot range: [1, 1000].",
        "-10^4 <= Node.val <= 10^4"
    ]
    
    explanation = """To determine if one tree is a subtree of another:
1. Define a helper function `isSameTree(p, q)` that checks if two trees are identical in structure and values.
   - Both null -> True.
   - One null, other not -> False.
   - p.val != q.val -> False.
   - Recursively check left and right subtrees.
2. In the main function `isSubtree(root, subRoot)`:
   - If `root` is None, return `false`.
   - If `isSameTree(root, subRoot)` is True, return `true`.
   - Otherwise, recursively check `isSubtree(root.left, subRoot)` or `isSubtree(root.right, subRoot)`."""
    
    answer = """class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)"""

    boilerplate = {
        "python": "import sys\\nclass TreeNode:\\n    def __init__(self, val=0, left=None, right=None):\\n        self.val = val; self.left = left; self.right = right\\n\\nclass Solution:\\n    def isSubtree(self, root, subRoot):\\n        pass",
        "cpp": "struct TreeNode { int val; TreeNode *left; TreeNode *right; };\\nclass Solution { public: bool isSubtree(TreeNode* root, TreeNode* subRoot) { return false; } };",
        "java": "class Solution { public boolean isSubtree(TreeNode root, TreeNode subRoot) { return false; } }",
        "javascript": "const fs = require('fs');",
        "c": "bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot) { }"
    }

    test_cases = [
        {"input": "3 4 5 1 2\\n4 1 2", "expected_output": "True", "is_sample": True},
        {"input": "3 4 5 1 2 None None None None 0\\n4 1 2", "expected_output": "False", "is_sample": True},
        {"input": "1\\n1", "expected_output": "True", "is_sample": False},
        {"input": "1 2 3\\n2", "expected_output": "True", "is_sample": False},
        {"input": "1 2 3\\n4", "expected_output": "False", "is_sample": False},
        {"input": "1 2 3\\n1 2 3", "expected_output": "True", "is_sample": False},
        {"input": "1 2 None 3 None 4\\n3 None 4", "expected_output": "True", "is_sample": False},
        {"input": "1 2 None 3 None 4\\n2 3", "expected_output": "True", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]) + "\\n99", "expected_output": "True", "is_sample": False},
        {"input": "1 2 3\\n1 2", "expected_output": "False", "is_sample": False}
    ]

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
        "topics": ["Tree", "Binary Tree", "Depth-First Search", "Breadth-First Search", "Hashing"],
        "companyIndex": 0
    }

    output_path = "401-600/572_Subtree_of_Another_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
