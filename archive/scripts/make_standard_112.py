import json
import os

def generate_json():
    problem_id = 112
    title = "Path Sum"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>112. Path Sum</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <code>true</code> if the tree has a <strong>root-to-leaf</strong> path such that adding up all the values along the path equals <code>targetSum</code>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;" />
<pre><strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>Output:</strong> true
<strong>Explanation:</strong> The root-to-leaf path with the target sum is shown.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />
<pre><strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> false
<strong>Explanation:</strong> There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [], targetSum = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> Since the tree is empty, there are no root-to-leaf paths.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated level-order binary tree values. Line 2: targetSum integer."
    output_format = "true if such path exists, false otherwise."
    
    constraints = [
        "0 <= number of nodes <= 5000",
        "-1000 <= Node.val <= 1000",
        "-1000 <= targetSum <= 1000."
    ]
    
    explanation = """To check for a root-to-leaf path sum:
1. **Recursive DFS**:
   - At each node, check if it's a leaf.
   - If it is a leaf, check if its value equals the remaining `targetSum`.
   - If it's not a leaf, recursively check its children with an updated `targetSum = targetSum - node.val`.
2. **Termination**:
   - If the node is `None`, return `False`.
3. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(H) where H is the height of the tree, for the recursion stack."""
    
    answer = """def hasPathSum(root, targetSum):
    if not root:
        return False
        
    if not root.left and not root.right:
        return root.val == targetSum
        
    return (hasPathSum(root.left, targetSum - root.val) or 
            hasPathSum(root.right, targetSum - root.val))"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef hasPathSum(root, targetSum):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        root = build_tree(lines[0].split())\n        target = int(lines[1].strip())\n        print(str(hasPathSum(root, target)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nbool hasPathSum(TreeNode* root, int targetSum) {\n    // User logic\n    return true;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static boolean hasPathSum(TreeNode root, int targetSum) {\n        // User logic\n        return true;\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction hasPathSum(root, targetSum) {\n    // User logic\n}",
        "c": "#include <stdbool.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nbool hasPathSum(struct TreeNode* root, int targetSum) {\n    // User logic\n    return true;\n}"
    }

    test_cases = [
        {"input": "5 4 8 11 null 13 4 7 2 null null null 1\\n22", "expected_output": "true", "is_sample": True},
        {"input": "1 2 3\\n5", "expected_output": "false", "is_sample": True},
        {"input": "\\n0", "expected_output": "false", "is_sample": True},
        {"input": "1 2\\n1", "expected_output": "false", "is_sample": False},
        {"input": "1 2\\n3", "expected_output": "true", "is_sample": False},
        {"input": "1 2 3\\n4", "expected_output": "true", "is_sample": False},
        {"input": "1 -2 -3\\n-1", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "1 " + "2 null "*50 + "\\n" + str(1 + 2 * 50), "expected_output": "true", "is_sample": False},
        {"input": "1 " + "null 2 "*50 + "\\n" + "10", "expected_output": "false", "is_sample": False},
        {"input": " ".join(["1"]*1023) + "\\n10", "expected_output": "true", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/112_Path_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
