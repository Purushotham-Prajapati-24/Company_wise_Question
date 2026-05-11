import json
import os

def generate_json():
    problem_id = 993
    title = "Cousins in Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>993. Cousins in Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree with unique values and the values of two different nodes of the tree <code>x</code> and <code>y</code>, return <code>true</code><em> if the nodes corresponding to the values </em><code>x</code><em> and </em><code>y</code><em> in the tree are <strong>cousins</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>Two nodes of a binary tree are <strong>cousins</strong> if they have the same depth with different parents.</p>

<p>Note that in a binary tree, the root node is at depth 0, and children of each node at depth <code>k</code> are at depth <code>k + 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<p><img src="file:///d:/College%20Projects/MNC_based/archive/assets/993_tree_1.png" style="width: 270px; height: 160px;" alt="Cousins Tree Example 1"/></p>
<pre>
<strong>Input:</strong> root = [1,2,3,4], x = 4, y = 3
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 2:</strong></p>
<p><img src="file:///d:/College%20Projects/MNC_based/archive/assets/993_tree_2.png" style="width: 270px; height: 160px;" alt="Cousins Tree Example 2"/></p>
<pre>
<strong>Input:</strong> root = [1,2,3,null,4,null,5], x = 5, y = 4
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<p><img src="file:///d:/College%20Projects/MNC_based/archive/assets/993_tree_3.png" style="width: 270px; height: 160px;" alt="Cousins Tree Example 3"/></p>
<pre>
<strong>Input:</strong> root = [1,2,3,null,4], x = 2, y = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
	<li>Each node has a unique value.</li>
	<li><code>x != y</code></li>
	<li><code>x</code> and <code>y</code> are exist in the tree.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for tree (level-order). Line 2: integers x and y."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "2 <= nodes <= 100",
        "Unique node values.",
        "x and y exist in tree.",
        "O(N) time complexity.",
        "O(H) extra space."
    ]
    
    explanation = """To determine if two nodes `x` and `y` are cousins (same depth, different parents):
1. **The Core Definition**:
   Two nodes are cousins if:
   - `Depth(x) == Depth(y)`
   - `Parent(x) != Parent(y)`
2. **Algorithm Strategy (Traversal)**:
   - We need to find the depth and the parent of both nodes.
   - We can use either DFS or BFS.
3. **DFS Approach**:
   - Maintain a dictionary or variables to store `parent` and `depth` for `x` and `y`.
   - Traverse the tree, passing the current depth and parent information to recursive calls.
   - If current node value matches `x` or `y`, store its depth and its parent node.
4. **BFS Approach**:
   - Traverse layer by layer.
   - For each node dequeued, check its children.
   - If children's values are `x` and `y`, check if they belong to different parents.
   - If both `x` and `y` are found in the same level but with different parents, return `true`.
5. **Complexity**:
   - Time Complexity: O(N) as we visit every node at most once.
   - Space Complexity: O(H) where H is the height of the tree (stack space or queue space)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root: TreeNode, x: int, y: int) -> bool:
    res = [] # To store (parent, depth)
    
    def dfs(node, parent, depth):
        if not node: return
        if node.val == x or node.val == y:
            res.append((parent, depth))
        dfs(node.left, node, depth + 1)
        dfs(node.right, node, depth + 1)
        
    dfs(root, None, 0)
    
    # Check candidates
    node1, node2 = res[0], res[1]
    return node1[1] == node2[1] and node1[0] != node2[0]"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(nodes):\n    if not nodes or nodes[0] == 'null': return None\n    root = TreeNode(int(nodes[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(nodes):\n        node = queue.popleft()\n        if i < len(nodes) and nodes[i] != 'null':\n            node.left = TreeNode(int(nodes[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(nodes) and nodes[i] != 'null':\n            node.right = TreeNode(int(nodes[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef isCousins(root, x, y):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        tree_nodes = lines[0].strip().split()\n        target_vals = list(map(int, lines[1].strip().split()))\n        if len(target_vals) == 2:\n            root = build_tree(tree_nodes)\n            print('true' if isCousins(root, target_vals[0], target_vals[1]) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <unordered_map>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nbool isCousins(TreeNode* root, int x, int y) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean isCousins(TreeNode root, int x, int y) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function isCousins(root, x, y) {\n    // User logic\n}",
        "c": "bool isCousins(struct TreeNode* root, int x, int y) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4\\n4 3", "expected_output": "false", "is_sample": True},
        {"input": "1 2 3 null 4 null 5\\n5 4", "expected_output": "true", "is_sample": True},
        {"input": "1 2 3 null 4\\n2 3", "expected_output": "false", "is_sample": True},
        {"input": "1 2 3 4 5 6 7\\n4 6", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3 4 5 6 7\\n4 5", "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 4 5 6 7\\n2 3", "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 null 4 null 5 null null 6\\n4 5", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3 null 4 null 5 null null 6\\n6 4", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n90 100", "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\\n2 3", "expected_output": "false", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "801-1000/993_Cousins_in_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
