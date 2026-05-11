import json
import os

def generate_json():
    problem_id = 543
    title = "Diameter of Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>543. Diameter of Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the length of the <strong>diameter</strong> of the tree</em>.</p>

<p>The <strong>diameter</strong> of a binary tree is the <strong>length</strong> of the longest path between any two nodes in a tree. This path may or may not pass through the <code>root</code>.</p>

<p>The <strong>length</strong> of a path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 is the length of the path [4,2,1,3] or [5,2,1,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>
"""

    input_format = "A serialized level-order traversal of the tree (e.g., [1,2,3,4,5])."
    output_format = "A single integer representing the diameter."
    
    constraints = [
        "The number of nodes is in the range [1, 10^4].",
        "-100 <= Node.val <= 100"
    ]
    
    explanation = """To find the diameter of a binary tree:
1. The diameter at a given node is the sum of the maximum heights of its left and right subtrees.
2. Use a recursive DFS function to calculate the height of each node:
   - Base case: If the node is None, its height is 0.
   - Recursively find heights of left and right children.
   - Calculate diameter passing through the current node: `left_height + right_height`.
   - Update a global maximum diameter.
   - Return the height of current node to its parent: `1 + max(left_height, right_height)`."""
    
    answer = """class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diam = 0
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.max_diam = max(self.max_diam, left + right)
            return 1 + max(left, right)
        
        height(root)
        return self.max_diam"""

    boilerplate = {
        "python": "import sys\\n\\nclass TreeNode:\\n    def __init__(self, val=0, left=None, right=None):\\n        self.val = val; self.left = left; self.right = right\\n\\nclass Solution:\\n    def diameterOfBinaryTree(self, root):\\n        pass",
        "cpp": "struct TreeNode { int val; TreeNode *left; TreeNode *right; };\\nclass Solution { public: int diameterOfBinaryTree(TreeNode* root) { return 0; } };",
        "java": "public class Solution { public int diameterOfBinaryTree(TreeNode root) { return 0; } }",
        "javascript": "const fs = require('fs');",
        "c": "int diameterOfBinaryTree(struct TreeNode* root){ }"
    }

    test_cases = [
        {"input": "1 2 3 4 5", "expected_output": "3", "is_sample": True},
        {"input": "1 2", "expected_output": "1", "is_sample": True},
        {"input": "1", "expected_output": "0", "is_sample": False},
        {"input": "1 2 3", "expected_output": "2", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "4", "is_sample": False},
        {"input": "1 2 None 3 None 4", "expected_output": "3", "is_sample": False},
        {"input": "1 None 2 None 3 None 4", "expected_output": "3", "is_sample": False},
        {"input": "1 2 3 4 None None 5 6 None None 7", "expected_output": "6", "is_sample": False},
        {"input": " ".join([str(i+1) for i in range(1023)]), "expected_output": "18", "is_sample": False},
        {"input": "1 " + "2 " * 10, "expected_output": "2", "is_sample": False}
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
        "topics": ["Tree", "Binary Tree", "Depth-First Search"],
        "companyIndex": 0
    }

    output_path = "401-600/543_Diameter_of_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
