import json
import os

def generate_json():
    problem_id = 545
    title = "Boundary of Binary Tree"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>545. Boundary of Binary Tree</h3>
<p>The <strong>boundary</strong> of a binary tree is the concatenation of the <strong>root</strong>, the <strong>left boundary</strong>, the <strong>leaves</strong> ordered from left-to-right, and the <strong>reverse order</strong> of the <strong>right boundary</strong>.</p>

<p>The <strong>left boundary</strong> is the path from the root to the <strong>leftmost</strong> node. The <strong>right boundary</strong> is the path from the root to the <strong>rightmost</strong> node. If the root doesn't have a left child, then the left boundary is empty. If the root doesn't have a right child, then the right boundary is empty. Note that the root is not included in the left or right boundaries if it is not the only node.</p>

<p>The <strong>leaves</strong> are all the leaf nodes in the tree, collected from left to right.</p>

<p>A node is a <strong>leftmost</strong> node if it is the left child of a leftmost node, or (if the left child doesn't exist) it is the right child of a leftmost node. A node is a <strong>rightmost</strong> node similarly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0545.Boundary%20of%20Binary%20Tree/images/boundary1.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3,4]
<strong>Output:</strong> [1,3,4,2]
<strong>Explanation:</strong>
- The left boundary is empty because the root doesn't have a left child.
- The leaves are [3,4].
- The right boundary is [2], and its reverse is [2].
- Concatenating [1] + [] + [3,4] + [2] gives [1,3,4,2].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0545.Boundary%20of%20Binary%20Tree/images/boundary1.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,None,None,None,7,8]
<strong>Output:</strong> [1,2,4,7,8,6,3]
<strong>Explanation:</strong>
- The left boundary is [2,4].
- The leaves are [7,8,6].
- The right boundary is [3], and its reverse is [3].
- Concatenating [1] + [2,4] + [7,8,6] + [3] gives [1,2,4,7,8,6,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>The node values are unique.</li>
</ul>
"""

    input_format = "A serialized level-order traversal of the tree (e.g., [1,2,3,4,5])."
    output_format = "A list of integers representing the tree boundary."
    
    constraints = [
        "The number of nodes is in the range [1, 10^4].",
        "-1000 <= Node.val <= 1000",
        "Node values are unique."
    ]
    
    explanation = """To find the boundary of a binary tree:
1. Handle the root: Add it to the result (unless it's null).
2. Left Boundary (excluding leaves): From root's left child, follow the left child prefers, then right. Add nodes to result. Stop before leaf.
3. Leaves: Perform a preorder traversal to find all leaf nodes (no children).
4. Right Boundary (excluding leaves): From root's right child, follow right child prefers, then left. Store in a temporary list and add them to result in reverse order. Stop before leaf."""
    
    answer = """class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root: return []
        
        def isLeaf(node):
            return node and not node.left and not node.right
        
        res = [root.val]
        
        # Left boundary
        curr = root.left
        while curr:
            if not isLeaf(curr):
                res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        
        # Leaves
        def addLeaves(node):
            if not node: return
            if isLeaf(node) and node != root:
                res.append(node.val)
            addLeaves(node.left)
            addLeaves(node.right)
        
        addLeaves(root)
        
        # Right boundary (reversed)
        stack = []
        curr = root.right
        while curr:
            if not isLeaf(curr):
                stack.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        while stack:
            res.append(stack.pop())
            
        return res"""

    boilerplate = {
        "python": "import sys\\n\\nclass TreeNode:\\n    def __init__(self, val=0, left=None, right=None):\\n        self.val = val; self.left = left; self.right = right\\n\\nclass Solution:\\n    def boundaryOfBinaryTree(self, root):\\n        pass",
        "cpp": "struct TreeNode { int val; TreeNode *left; TreeNode *right; };\\nclass Solution { public: vector<int> boundaryOfBinaryTree(TreeNode* root) { return {}; } };",
        "java": "public class Solution { public List<Integer> boundaryOfBinaryTree(TreeNode root) { return new ArrayList<>(); } }",
        "javascript": "const fs = require('fs');",
        "c": "int* boundaryOfBinaryTree(struct TreeNode* root, int* returnSize) { }"
    }

    test_cases = [
        {"input": "1 None 2 3 4", "expected_output": "[1, 3, 4, 2]", "is_sample": True},
        {"input": "1 2 3 4 5 6 None None None 7 8", "expected_output": "[1, 2, 4, 7, 8, 6, 3]", "is_sample": True},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "1 None 2", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "[1, 2, 4, 5, 6, 7, 3]", "is_sample": False},
        {"input": "1 2 None 3 None 4", "expected_output": "[1, 2, 3, 4]", "is_sample": False},
        {"input": "1 2 3 None None None None", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": " ".join([str(i+1) for i in range(10)]), "expected_output": "[1, 2, 4, 8, 9, 10, 5, 6, 7, 3]", "is_sample": False}
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
        "topics": ["Tree", "Binary Tree", "Depth-First Search", "Breadth-First Search"],
        "companyIndex": 0
    }

    output_path = "401-600/545_Boundary_of_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
