import json
import os

def generate_json():
    problem_id = 669
    title = "Trim a Binary Search Tree"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>669. Trim a Binary Search Tree</h3>
<p>Given the <code>root</code> of a binary search tree and the lowest and highest boundaries as <code>low</code> and <code>high</code>, trim the tree so that all its elements lies in <code>[low, high]</code>. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.</p>

<p>Return <em>the root of the trimmed binary search tree</em>. Note that the root may change depending on the given bounds.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg" style="width: 450px; height: 126px;" />
<pre>
<strong>Input:</strong> root = [1,0,2], low = 1, high = 2
<strong>Output:</strong> [1,null,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg" style="width: 450px; height: 277px;" />
<pre>
<strong>Input:</strong> root = [3,0,4,null,2,null,null,1], low = 1, high = 3
<strong>Output:</strong> [3,2,null,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The value of each node in the tree is <b>unique</b>.</li>
	<li><code>root</code> is guaranteed to be a valid binary search tree.</li>
	<li><code>0 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Three lines: 1) Space-separated Level-Order tree string 2) integer low 3) integer high."
    output_format = "Space-separated Level-Order traversal of the trimmed tree (use 'null' for missing)."
    
    constraints = [
        "1 <= N <= 10^4",
        "Unique nodes, valid BST.",
        "O(N) time complexity.",
        "O(H) extra space (recursion stack)."
    ]
    
    explanation = """To trim a BST while maintaining its relative structure:
1. **The Recursive Approach**:
   - If `root` is `null`, return `null`.
   - If `root.val < low`:
     - Entire left subtree and the root itself are out of range.
     - Move to the right child: return `trimBST(root.right, low, high)`.
   - If `root.val > high`:
     - Entire right subtree and the root itself are out of range.
     - Move to the left child: return `trimBST(root.left, low, high)`.
2. **If `root.val` is in range**:
   - Trim the left child and assign to `root.left`.
   - Trim the right child and assign to `root.right`.
   - Return the root.
3. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(H) where H is the height of the tree, due to recursion."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trimBST(root, low: int, high: int):
    if not root:
        return None
    
    if root.val < low:
        return trimBST(root.right, low, high)
    if root.val > high:
        return trimBST(root.left, low, high)
    
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    return root"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef trimBST(root, low, high):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Parser and Level-Order Printer here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public TreeNode trimBST(TreeNode root, int low, int high) {\n        // User logic\n        return null;\n    }\n}",
        "javascript": "function trimBST(root, low, high) {\n    // User logic\n}",
        "c": "struct TreeNode* trimBST(struct TreeNode* root, int low, int high) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 0 2\\n1\\n2", "expected_output": "1 null 2", "is_sample": True},
        {"input": "3 0 4 null 2 null null 1\\n1\\n3", "expected_output": "3 2 null 1", "is_sample": True},
        {"input": "1\\n1\\n1", "expected_output": "1", "is_sample": False},
        {"input": "2 1 3\\n1\\n2", "expected_output": "2 1", "is_sample": False},
        {"input": "2 1 3\\n3\\n3", "expected_output": "3", "is_sample": False},
        {"input": "5 3 7 2 4 6 8\\n3\\n6", "expected_output": "5 3 6 null 4", "is_sample": False},
        {"input": "10 5 15 2 7 12 20\\n10\\n20", "expected_output": "10 null 15 12 20", "is_sample": False},
        {"input": "4 2 6 1 3 5 7\\n2\\n5", "expected_output": "4 2 5 null 3", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 1001)]) + "\\n500\\n500", "expected_output": "500", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 1001)]) + "\\n1001\\n1005", "expected_output": "null", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Search Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/669_Trim_a_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
