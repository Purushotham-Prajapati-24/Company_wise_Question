import json
import os

def generate_json():
    problem_id = 623
    title = "Add One Row to Tree"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>623. Add One Row to Tree</h3>
<p>Given the <code>root</code> of a binary tree and two integers <code>val</code> and <code>depth</code>, add a row of nodes with value <code>val</code> at the given depth <code>depth</code>.</p>

<p>Note that the root node is at depth <code>1</code>.</p>

<p>The adding rule is:</p>
<ul>
	<li>Given the integer <code>depth</code>, for each not-null tree node <code>cur</code> at the depth <code>depth - 1</code>, create two tree nodes with value <code>val</code> as <code>cur</code>'s left subtree root and right subtree root.</li>
	<li><code>cur</code>'s original left subtree should be the left subtree of the new left subtree root.</li>
	<li><code>cur</code>'s original right subtree should be the right subtree of the new right subtree root.</li>
	<li>If <code>depth == 1</code> that means there is no depth <code>depth - 1</code> at all, then create a tree node with value <code>val</code> as the new root of the whole original tree, and the original tree is the new root's left subtree.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/10/addrow-tree.jpg" style="width: 500px; height: 231px;" />
<pre>
<strong>Input:</strong> root = [4,2,6,3,1,5], val = 1, depth = 2
<strong>Output:</strong> [4,1,1,2,null,null,6,3,1,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/10/add2-tree.jpg" style="width: 500px; height: 277px;" />
<pre>
<strong>Input:</strong> root = [4,2,null,3,1], val = 1, depth = 3
<strong>Output:</strong> [4,2,null,1,1,3,null,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li>The depth of the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>-10<sup>5</sup> &lt;= val &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= depth &lt;= the depth of tree + 1</code></li>
</ul>"""

    input_format = "Three lines: 1) Space-separated Level-Order Traversal (use 'null' for missing) 2) val 3) depth."
    output_format = "Space-separated Level-Order Traversal of the modified tree."
    
    constraints = [
        "1 <= N <= 10^4",
        "Depth 1 case: New root.",
        "Maintain subtrees as specified.",
        "O(N) time complexity.",
        "O(H) extra space."
    ]
    
    explanation = """To add a row at depth $d$:
1. **Handle Depth 1**:
   - Create a new node with `val`.
   - Set the original root as its left child.
   - Return this new node.
2. **Handle Depth > 1**:
   - Traverse the tree (BFS or DFS) to find all nodes at depth $d-1$.
   - For each node at depth $d-1$:
     - Store its current left and right children.
     - Create a new left child with `val`. Set its left child as the stored old left child.
     - Create a new right child with `val`. Set its right child as the stored old right child.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) or O(W) (Height or Width depending on BFS/DFS)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root, val, depth):
    if depth == 1:
        return TreeNode(val, left=root)
    
    queue = [root]
    curr_depth = 1
    while curr_depth < depth - 1:
        next_queue = []
        for node in queue:
            if node.left: next_queue.append(node.left)
            if node.right: next_queue.append(node.right)
        queue = next_queue
        curr_depth += 1
    
    for node in queue:
        node.left = TreeNode(val, left=node.left)
        node.right = TreeNode(val, right=node.right)
    
    return root"""

    boilerplate = {
        "python": "import sys\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef addOneRow(root, val, depth):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Parser logic here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public TreeNode addOneRow(TreeNode root, int val, int depth) {\n        // User logic\n        return null;\n    }\n}",
        "javascript": "function addOneRow(root, val, depth) {\n    // User logic\n}",
        "c": "struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "4 2 6 3 1 5\\n1\\n2", "expected_output": "4 1 1 2 null null 6 3 1 5", "is_sample": True},
        {"input": "4 2 null 3 1\\n1\\n3", "expected_output": "4 2 null 1 1 3 null null 1", "is_sample": True},
        {"input": "1 2 3\\n4\\n1", "expected_output": "4 1 null 2 3", "is_sample": False},
        {"input": "1\\n2\\n2", "expected_output": "1 2 2", "is_sample": False},
        {"input": "1 2 3 4\\n5\\n3", "expected_output": "1 2 3 5 5 null null 4", "is_sample": False},
        {"input": "1 2 3 4\\n5\\n4", "expected_output": "1 2 3 4 null null null 5 5", "is_sample": False},
        {"input": "1 2 null 3\\n4\\n3", "expected_output": "1 2 null 4 4 3", "is_sample": False},
        {"input": "1 2 3\\n0\\n2", "expected_output": "1 0 0 2 null null 3", "is_sample": False},
        # Stress cases
        {"input": "1\\n100\\n1", "expected_output": "100 1", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n99\\n50", "expected_output": "Complex Output...", "is_sample": False}
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
        "topics": ["Tree", "DFS", "BFS"],
        "companyIndex": 0
    }

    output_path = "601-800/623_Add_One_Row_to_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
