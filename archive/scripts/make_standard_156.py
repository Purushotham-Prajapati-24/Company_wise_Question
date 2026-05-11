import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 156
    title = "Binary Tree Upside Down"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>156. Binary Tree Upside Down</h3>
<p>Given the <code>root</code> of a binary tree, flip it upside down and return the new root.</p>

<p>You can flip the binary tree upside down with the following steps:</p>

<ol>
	<li>The original left child becomes the new root.</li>
	<li>The original root becomes the new right child.</li>
	<li>The original right child becomes the new left child.</li>
</ol>

<p>The above steps are applied recursively for each level. Every right node in the tree has no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/29/updown.jpg" style="width: 800px; height: 161px;" />
<pre><strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> [4,5,2,null,null,3,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10</code></li>
	<li>Every right node in the tree has a sibling (a left node that shares the same parent).</li>
	<li>Every right node in the tree has no children.</li>
</ul>"""

    input_format = "A single line containing space-separated values representing level-order traversal of the tree (use 'null' for missing nodes)."
    output_format = "A bracketed array of integers representing the flipped tree in level-order traversal."
    
    constraints = [
        "0 <= Number of nodes <= 10",
        "1 <= Node.val <= 10",
        "Every right node has a left sibling and no children.",
        "Constant extra space implementation is possible."
    ]
    
    explanation = """To flip the tree upside down:
1. **Vertical/Left Spine Traversal**: Note that the problem guarantee means the tree is essentially a "left-heavy" spine.
2. **Recursive Logic**:
   - Recursively call `upsideDownBinaryTree` on `root.left`. This goes to the leftmost leaf, which will become the new root.
   - At each level during backtracking:
     - `root.left.left = root.right`
     - `root.left.right = root`
     - Clear original pointers: `root.left = None`, `root.right = None`.
3. **Complexity**:
   - Time Complexity: O(n)
   - Space Complexity: O(n) for recursion stack."""
    
    answer = """class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
            
        new_root = self.upsideDownBinaryTree(root.left)
        
        root.left.left = root.right
        root.left.right = root
        
        root.left = None
        root.right = None
        
        return new_root"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(lst):\n    if not lst: return None\n    root = TreeNode(int(lst[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(lst):\n        node = queue.popleft()\n        if i < len(lst) and lst[i] != 'null':\n            node.left = TreeNode(int(lst[i])); queue.append(node.left)\n        i += 1\n        if i < len(lst) and lst[i] != 'null':\n            node.right = TreeNode(int(lst[i])); queue.append(node.right)\n        i += 1\n    return root\n\ndef serialize(root):\n    if not root: return []\n    res, q = [], deque([root])\n    while q:\n        node = q.popleft()\n        if node:\n            res.append(node.val); q.append(node.left); q.append(node.right)\n        else: res.append(None)\n    while res and res[-1] is None: res.pop()\n    return [x if x is not None else \"null\" for x in res]\n\ndef upsideDownBinaryTree(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    root = build_tree(input_data)\n    new_root = upsideDownBinaryTree(root)\n    print(json.dumps(serialize(new_root)))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nstruct TreeNode {\n    int val; TreeNode *left; TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* upsideDownBinaryTree(TreeNode* root) {\n    // User logic\n    return NULL;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val; TreeNode left; TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static TreeNode upsideDownBinaryTree(TreeNode root) {\n        // User logic\n        return null;\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n/**\n * @param {TreeNode} root\n * @return {TreeNode}\n */\nvar upsideDownBinaryTree = function(root) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val; struct TreeNode *left; struct TreeNode *right;\n};\n\nstruct TreeNode* upsideDownBinaryTree(struct TreeNode* root) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 5", "expected_output": "[4, 5, 2, \"null\", \"null\", 3, 1]", "is_sample": True},
        {"input": "", "expected_output": "[]", "is_sample": True},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[2, 3, 1]", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "[3, \"null\", 2, \"null\", \"null\", \"null\", 1]", "is_sample": False},
        {"input": "1 2 null 3 null 4", "expected_output": "[4, \"null\", 3, \"null\", \"null\", \"null\", 2, \"null\", \"null\", \"null\", \"null\", \"null\", \"null\", \"null\", 1]", "is_sample": False},
        {"input": "10 5 15", "expected_output": "[5, 15, 10]", "is_sample": False},
        # Stress Tests (Max nodes=10)
        {"input": "1 2 3 4 5 6 7 8 9 10", "expected_output": "...", "is_sample": False},
        {"input": "1 2 null 3 null 4 null 5 null 6 null 7 null 8 null 9 null 10", "expected_output": "...", "is_sample": False},
        {"input": "10 9 8 7 6 5 4 3 2 1", "expected_output": "...", "is_sample": False}
    ]
    
    def _flip(lst):
        if not lst: return []
        def build(l):
            if not l: return None
            r = TreeNode(int(l[0]))
            q = deque([r])
            idx = 1
            while q and idx < len(l):
                curr = q.popleft()
                if idx < len(l) and l[idx] != 'null':
                    curr.left = TreeNode(int(l[idx])); q.append(curr.left)
                idx += 1
                if idx < len(l) and l[idx] != 'null':
                    curr.right = TreeNode(int(l[idx])); q.append(curr.right)
                idx += 1
            return r
        def flip_core(node):
            if not node or not node.left: return node
            new_r = flip_core(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = None; node.right = None
            return new_r
        def ser(node):
            if not node: return []
            res, q = [], deque([node])
            while q:
                n = q.popleft()
                if n:
                    res.append(n.val); q.append(n.left); q.append(n.right)
                else: res.append(None)
            while res and res[-1] is None: res.pop()
            return [x if x is not None else "null" for x in res]
        return ser(flip_core(build(lst)))

    for i in range(len(test_cases)):
        if test_cases[i]["input"] == "": 
            test_cases[i]["expected_output"] = "[]"
            continue
        test_cases[i]["expected_output"] = json.dumps(_flip(test_cases[i]["input"].split()))

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
        "topics": ["Tree", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/156_Binary_Tree_Upside_Down.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
