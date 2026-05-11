import json
import os

def generate_json():
    problem_id = 111
    title = "Minimum Depth of Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>111. Minimum Depth of Binary Tree</h3>
<p>Given a binary tree, find its minimum depth.</p>

<p>The <strong>minimum depth</strong> is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [2,null,3,null,4,null,5,null,6]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>5</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "An integer representing the minimum depth of the tree."
    
    constraints = [
        "0 <= number of nodes <= 10^5",
        "-1000 <= Node.val <= 1000."
    ]
    
    explanation = """To find the minimum depth of a binary tree:
1. **BFS (Level-Order Traversal)**:
   - This is the most efficient approach because we search level by level.
   - The first node we encounter that is a **leaf** (no left and no right child) will reside on the level of the minimum depth.
2. **Logic**:
   - Use a queue for BFS. For every level, increment the depth.
   - For every node at the current level:
     - Check if it's a leaf. If yes, return current depth.
     - Otherwise, add children to the queue.
3. **Complexity**:
   - Time Complexity: O(N) in the worst case, but typically much faster than DFS for this specific problem as it stops early.
   - Space Complexity: O(W) where W is the maximum width of the tree."""
    
    answer = """from collections import deque

def minDepth(root):
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        
        # If it's a leaf node, we found the min depth
        if not node.left and not node.right:
            return depth
            
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
            
    return 0"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef minDepth(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(minDepth(build_tree(data)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nint minDepth(TreeNode* root) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static int minDepth(TreeNode root) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction minDepth(root) {\n    // User logic\n}",
        "c": "int minDepth(struct TreeNode* root) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 null null 15 7", "expected_output": "2", "is_sample": True},
        {"input": "2 null 3 null 4 null 5 null 6", "expected_output": "5", "is_sample": True},
        {"input": "", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2", "expected_output": "2", "is_sample": False},
        {"input": "1 2 3", "expected_output": "2", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 1025)]), "expected_output": "10", "is_sample": False},
        {"input": "1 " + "null 2 "*50, "expected_output": "51", "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": "51", "is_sample": False}
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
        "topics": ["Tree", "DFS", "BFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/111_Minimum_Depth_of_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
