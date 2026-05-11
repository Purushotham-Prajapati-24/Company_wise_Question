import json
import os

def generate_json():
    problem_id = 783
    title = "Minimum Distance Between BST Nodes"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>783. Minimum Distance Between BST Nodes</h3>
<p>Given the <code>root</code> of a Binary Search Tree (BST), return <em>the minimum difference between the values of any two different nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> root = [4,2,6,1,3]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = [1,0,48,null,null,12,49]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing level-order traversal of BST (space-separated integers or 'null')."
    output_format = "A single integer representing the minimum difference."
    
    constraints = [
        "2 <= number of nodes <= 100",
        "0 <= Node.val <= 10^5",
        "O(N) time complexity.",
        "O(H) space complexity (recursion depth)."
    ]
    
    explanation = """To find the minimum distance between any two nodes in a Binary Search Tree (BST):
1. **The Core Realization**:
   - An in-order traversal (Left, Root, Right) of a BST visits nodes in strictly increasing order.
   - The minimum difference between *any* two nodes must occur between two nodes that are adjacent in the in-order sorted sequence.
2. **Algorithm Strategy**:
   - Perform an in-order traversal using recursion or a stack.
   - Keep track of the `previous_value` visited.
   - For every node, calculate `current_val - previous_value` and update the `min_diff` found so far.
   - Initialize `previous_value` to `None` or negative infinity.
3. **Complexity**:
   - Time Complexity: O(N) to visit each node once.
   - Space Complexity: O(H) where H is the height of the tree, due to the recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root: TreeNode) -> int:
    prev = None
    min_diff = float('inf')
    
    def inorder(node):
        nonlocal prev, min_diff
        if not node: return
        
        inorder(node.left)
        
        if prev is not None:
            min_diff = min(min_diff, node.val - prev)
        prev = node.val
        
        inorder(node.right)
        
    inorder(root)
    return min_diff"""

    boilerplate = {
        "python": "import sys\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(nodes):\n    if not nodes or nodes[0] == \"null\": return None\n    root = TreeNode(int(nodes[0]))\n    queue = [root]\n    i = 1\n    while queue and i < len(nodes):\n        node = queue.pop(0)\n        if i < len(nodes) and nodes[i] != \"null\":\n            node.left = TreeNode(int(nodes[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(nodes) and nodes[i] != \"null\":\n            node.right = TreeNode(int(nodes[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef minDiffInBST(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        nodes = line.split()\n        root = build_tree(nodes)\n        print(minDiffInBST(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nint minDiffInBST(TreeNode* root) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public int minDiffInBST(TreeNode root) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function minDiffInBST(root) {\n    // User logic\n}",
        "c": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint minDiffInBST(struct TreeNode* root) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "4 2 6 1 3", "expected_output": "1", "is_sample": True},
        {"input": "1 0 48 null null 12 49", "expected_output": "1", "is_sample": True},
        {"input": "10 5 15", "expected_output": "5", "is_sample": False},
        {"input": "100 50 150 25 75 125 175", "expected_output": "25", "is_sample": False},
        {"input": "100 1 200", "expected_output": "99", "is_sample": False},
        {"input": "10 1 null", "expected_output": "9", "is_sample": False},
        {"input": "1 1 null", "expected_output": "0", "is_sample": False}, # Note: Problem says distinct pairs, but logic holds for non-distinct too
        {"input": "100 0 1000", "expected_output": "100", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": "1", "is_sample": False}, # Skewed Tree
        {"input": " ".join([str(i*100) for i in range(100)]), "expected_output": "100", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Binary Search Tree", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/783_Minimum_Distance_Between_BST_Nodes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
