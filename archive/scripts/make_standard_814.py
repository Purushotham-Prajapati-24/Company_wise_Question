import json
import os

def generate_json():
    problem_id = 814
    title = "Binary Tree Pruning"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>814. Binary Tree Pruning</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the same tree where every subtree (of the given tree) not containing a <code>1</code> has been removed</em>.</p>

<p>A subtree of a node <code>node</code> is <code>node</code> plus every node that is a descendant of <code>node</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width: 450px; height: 350px;" />
<pre>
<strong>Input:</strong> root = [1,null,0,0,1]
<strong>Output:</strong> [1,null,0,null,1]
<strong>Explanation:</strong> 
Only the red nodes satisfy the property "every subtree not containing a 1 has been removed".
The diagram on the right represents the answer.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width: 450px; height: 350px;" />
<pre>
<strong>Input:</strong> root = [1,0,1,0,0,0,1]
<strong>Output:</strong> [1,null,1,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 200]</code>.</li>
	<li><code>Node.val</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
"""

    input_format = "A root of a binary tree in level-order JSON array."
    output_format = "The pruned tree in level-order JSON array."
    
    constraints = [
        "The number of nodes is between 1 and 200.",
        "Node.val is either 0 or 1."
    ]
    
    explanation = """To prune the binary tree so only subtrees containing '1' remain:
1. **The Post-order Traversal Strategy**:
   - We must decide whether to prune a child before we can decide whether to prune the parent. This is a clear case for **Post-order traversal** (Left-Right-Node).
2. **Recursive Logic**:
   - Base case: If `root` is `None`, return `None`.
   - Recursive call: Update `root.left = pruneTree(root.left)` and `root.right = pruneTree(root.right)`.
   - Pruning condition: If after recursing, `root.left` is `None`, `root.right` is `None`, AND `root.val == 0`, it means this subtree contains no `1`s. We return `None` to the parent.
   - Otherwise, return `root`.

Complexity:
- Time: O(N) where N is the number of nodes. We visit each node once.
- Space: O(H) where H is the height of the tree, representing the recursion stack depth."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pruneTree(root: TreeNode) -> TreeNode:
    if not root: 
        return None
    
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    
    if root.val == 0 and not root.left and not root.right:
        return None
        
    return root"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef pruneTree(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Tree deserialization code goes here\n    pass",
        "cpp": "#include <iostream>\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n};",
        "java": "class Solution {\n    public TreeNode pruneTree(TreeNode root) {\n        return null;\n    }\n}",
        "javascript": "var pruneTree = function(root) {\n    \n};",
        "c": "struct TreeNode* pruneTree(struct TreeNode* root){\n\n}"
    }

    test_cases = [
        {"input": "[1,null,0,0,1]", "expected_output": "[1,null,0,null,1]", "is_sample": True},
        {"input": "[1,0,1,0,0,0,1]", "expected_output": "[1,null,1,null,1]", "is_sample": True},
        {"input": "[1,1,0,1,1,0,1,0]", "expected_output": "[1,1,0,1,1,null,1]", "is_sample": True},
        # Diverse cases
        {"input": "[0,0,0]", "expected_output": "[]", "is_sample": False},
        {"input": "[1,0,0]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,1,1]", "expected_output": "[1,1,1]", "is_sample": False},
        {"input": "[0,null,1]", "expected_output": "[0,null,1]", "is_sample": False},
        {"input": "[1,0,null,0,null,1]", "expected_output": "[1,0,null,null,null,1]", "is_sample": False},
        {"input": "[0,0,null,1]", "expected_output": "[0,0,null,1]", "is_sample": False},
        {"input": "[0,null,0,null,0]", "expected_output": "[]", "is_sample": False}
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

    output_path = "801-1000/814_Binary_Tree_Pruning.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
