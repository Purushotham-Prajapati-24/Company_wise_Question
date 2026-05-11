import json
import os

def generate_json():
    problem_id = 965
    title = "Univalued Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>965. Univalued Binary Tree</h3>
<p>A binary tree is <strong>uni-valued</strong> if every node in the tree has the same value.</p>

<p>Given the <code>root</code> of a binary tree, return <code>true</code><em> if the given tree is <strong>uni-valued</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<p><img src="file:///d:/College%20Projects/MNC_based/archive/assets/965_unival_tree_1.png" style="width: 250px; height: 180px;" alt="Uni-valued Tree Example 1"/></p>
<pre>
<strong>Input:</strong> root = [1,1,1,1,1,null,1]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<p><img src="file:///d:/College%20Projects/MNC_based/archive/assets/965_unival_tree_2.png" style="width: 250px; height: 180px;" alt="Uni-valued Tree Example 2"/></p>
<pre>
<strong>Input:</strong> root = [2,2,2,5,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt; 100</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers (or 'null') representing level-order traversal."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= nodes <= 100",
        "0 <= val < 100",
        "O(N) time complexity.",
        "O(H) extra space (recursion stack or queue)."
    ]
    
    explanation = """To determine if a binary tree is univalued:
1. **The Goal**: Every node in the tree must have the exact same value as the root node.
2. **Algorithm Strategy (DFS)**:
   - Perform a Depth-First Search (DFS) starting from the root.
   - For every node encountered:
     - Compare its value with the `root.val`.
     - If the value is different, the tree is not uni-valued; return `false`.
     - Recursively check the left and right children.
3. **Algorithm Strategy (BFS)**:
   - Use a queue for level-order traversal.
   - Compare every dequeued node's value with the `root.val`.
4. **Conclusion**: If the traversal completes without finding a mismatch, return `true`.
5. **Complexity**:
   - Time Complexity: O(N) as we must visit every node once.
   - Space Complexity: O(H) where H is the height of the tree, due to the call stack in DFS or the queue width in BFS."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUnivalTree(root: TreeNode) -> bool:
    if not root: return True
    
    def dfs(node, val):
        if not node: return True
        if node.val != val: return False
        return dfs(node.left, val) and dfs(node.right, val)
        
    return dfs(root, root.val)"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(nodes):\n    if not nodes or nodes[0] == 'null': return None\n    root = TreeNode(int(nodes[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(nodes):\n        node = queue.popleft()\n        if i < len(nodes) and nodes[i] != 'null':\n            node.left = TreeNode(int(nodes[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(nodes) and nodes[i] != 'null':\n            node.right = TreeNode(int(nodes[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef isUnivalTree(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nodes = line.split()\n        root = build_tree(nodes)\n        print('true' if isUnivalTree(root) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nbool isUnivalTree(TreeNode* root) {\n    // User logic\n    return true;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean isUnivalTree(TreeNode root) {\n        // User logic\n        return true;\n    }\n}",
        "javascript": "function isUnivalTree(root) {\n    // User logic\n}",
        "c": "bool isUnivalTree(struct TreeNode* root) {\n    // User logic\n    return true;\n}"
    }

    test_cases = [
        {"input": "1 1 1 1 1 null 1", "expected_output": "true", "is_sample": True},
        {"input": "2 2 2 5 2", "expected_output": "false", "is_sample": True},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "1 2", "expected_output": "false", "is_sample": False},
        {"input": "1 1 1", "expected_output": "true", "is_sample": False},
        {"input": "9 9 9 9 9 9 1", "expected_output": "false", "is_sample": False},
        {"input": "0 0 1", "expected_output": "false", "is_sample": False},
        {"input": "1 1 null 1 1", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join(["9"] * 100), "expected_output": "true", "is_sample": False},
        {"input": " ".join(["9"] * 99 + ["8"]), "expected_output": "false", "is_sample": False}
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

    output_path = "801-1000/965_Univalued_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
