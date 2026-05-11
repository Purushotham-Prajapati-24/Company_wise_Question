import json
import os

def generate_json():
    problem_id = 872
    title = "Leaf-Similar Trees"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>872. Leaf-Similar Trees</h3>
<p>Consider all the leaves of a binary tree. From&nbsp;left to right order, the values of those&nbsp;leaves form a <strong>leaf value sequence</strong>.</p>

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 400px; height: 336px;" />

<p>For example, in the given tree above, the leaf value sequence is <code>(6, 7, 4, 9, 8)</code>.</p>

<p>Two binary trees are considered <em>leaf-similar</em>&nbsp;if their leaf value sequence is the same.</p>

<p>Return <code>true</code> if and only if the two given trees with head nodes <code>root1</code> and <code>root2</code> are leaf-similar.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg" style="width: 600px; height: 237px;" />
<pre>
<strong>Input:</strong> root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg" style="width: 450px; height: 165px;" />
<pre>
<strong>Input:</strong> root1 = [1,2,3], root2 = [1,3,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each tree will be in the range <code>[1, 200]</code>.</li>
	<li>Both of the given trees will have values in the range <code>[0, 200]</code>.</li>
</ul>
"""

    input_format = "Two root nodes of binary trees in JSON format."
    output_format = "A boolean value (true/false)."
    
    constraints = [
        "1 <= Number of nodes <= 200",
        "0 <= Node.val <= 200"
    ]
    
    explanation = """To determine if two binary trees are leaf-similar:
1. **The Core Approach (DFS)**:
   - Identify the "leaf value sequence" by collecting all leaf nodes in order from left to right.
   - For a binary tree, a leaf is a node where `left` and `right` children are both `null`.

2. **The Logic**:
   - Use **Depth-First Search (DFS)** to traverse each tree.
   - For each node `p`:
     - If it's a leaf, append `p.val` to the sequence.
     - Else, recursively visit `p.left` then `p.right`.
   - After processing both trees, compare the resulting sequences.

Complexity:
- Time: O(N + M) where N and M are nodes in root1 and root2.
- Space: O(H1 + H2) where H is the height of the tree (for the recursion stack)."""
    
    answer = """def leafSimilar(root1, root2) -> bool:
    def get_leaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return get_leaves(node.left) + get_leaves(node.right)
    
    return get_leaves(root1) == get_leaves(root2)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef leafSimilar(root1, root2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Tree deserialization code goes here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\ntypedef struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n} TreeNode;",
        "java": "import java.util.*;\n\nclass Solution {\n    public boolean leafSimilar(TreeNode root1, TreeNode root2) {\n        return false;\n    }\n}",
        "javascript": "var leafSimilar = function(root1, root2) {\n    return false;\n};",
        "c": "bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){\n    return false;\n}"
    }

    test_cases = [
        {"input": "[3,5,1,6,2,9,8,null,null,7,4]\\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,3]\\n[1,3,2]", "expected_output": "false", "is_sample": True},
        # Diverse cases
        {"input": "[1,2,3]\\n[1,2,3]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2]\\n[2,2]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2]\\n[1,null,2]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]\\n[1,2,3,4,5,6,7]", "expected_output": "true", "is_sample": False},
        {"input": "[1,null,2,null,3]\\n[1,null,2,null,3]", "expected_output": "true", "is_sample": False},
        {"input": "[1]\\n[2]", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "[0 to 199 left tilted]\\n[0 to 199 right tilted]", "expected_output": "true", "is_sample": False},
        {"input": "[0 to 199 tree]\\n[different leaves]", "expected_output": "false", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "801-1000/872_Leaf-Similar_Trees.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
