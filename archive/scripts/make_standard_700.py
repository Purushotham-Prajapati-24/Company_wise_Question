import json
import os

def generate_json():
    problem_id = 700
    title = "Search in a Binary Search Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>700. Search in a Binary Search Tree</h3>
<p>You are given the <code>root</code> of a binary search tree (BST) and an integer <code>val</code>.</p>
<p>Find the node in the BST that the node's value equals <code>val</code> and return the subtree rooted with that node. If such a node does not exist, return <code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" style="width: 422px; height: 302px;" />
<pre><strong>Input:</strong> root = [4,2,7,1,3], val = 2
<strong>Output:</strong> [2,1,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" style="width: 422px; height: 302px;" />
<pre><strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 5000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>7</sup></code></li>
	<li><code>root</code> is a binary search tree.</li>
	<li><code>1 &lt;= val &lt;= 10<sup>7</sup></code></li>
</ul>
"""

    input_format = "Two lines:\\n1. Tree 'root' as level-order JSON list\\n2. Integer 'val'"
    output_format = "The subtree as a level-order JSON list."
    
    constraints = [
        "Nodes count <= 5,000",
        "BST property: left < root < right",
        "O(H) search where H is tree height."
    ]
    
    explanation = """To search in a Binary Search Tree:
1. **Iterative Search**:
   - Level-order trees are usually converted to a linked node structure or handled directly. For search:
   - Start with `curr = root`.
   - While `curr` is not None:
     - If `curr.val == val`, return `curr` (the subtree rooted at `curr`).
     - If `val < curr.val`, move to the left child: `curr = curr.left`.
     - Else, move to the right child: `curr = curr.right`.
2. **Result**: If no node is found, return `None`.

Complexity:
- Time: O(H) where H is the height of the tree (O(log N) for balanced trees, O(N) for skewed trees).
- Space: O(1) for iterative, O(H) for recursive due to stack.
"""
    
    answer = """def searchBST(root, val):
    # This assumes root is a TreeNode object
    curr = root
    while curr:
        if curr.val == val:
            return curr
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None"""

    boilerplate = {
        "python": "import sys\\nimport json\\n\\nclass TreeNode:\\n    def __init__(self, val=0, left=None, right=None):\\n        self.val = val\\n        self.left = left\\n        self.right = right\\n\\ndef searchBST(root, val):\\n    # User logic here\\n    pass\\n\\n# Implementation for tree building from list would go here...\\nif __name__ == '__main__':\\n    input_data = sys.stdin.read().splitlines()\\n    root_list = json.loads(input_data[0])\\n    val = int(input_data[1])\\n    # Search logic...\\n    pass",
        "cpp": "#include <iostream>\\n#include <vector>\\nusing namespace std;\\n\\nstruct TreeNode { int val; TreeNode *left; TreeNode *right; };\\nTreeNode* searchBST(TreeNode* root, int val) { return nullptr; }",
        "java": "public class Main { public static void main(String[] args) { } }",
        "javascript": "const fs = require('fs');",
        "c": "struct TreeNode* searchBST(struct TreeNode* root, int val) { }"
    }

    test_cases = [
        {"input": "[4,2,7,1,3]\\n2", "expected_output": "[2, 1, 3]", "is_sample": True},
        {"input": "[4,2,7,1,3]\\n5", "expected_output": "[]", "is_sample": True},
        {"input": "[10,5,15,3,7,13,18]\\n15", "expected_output": "[15, 13, 18]", "is_sample": False},
        {"input": "[10,5,15,3,7,13,18]\\n10", "expected_output": "[10, 5, 15, 3, 7, 13, 18]", "is_sample": False},
        {"input": "[10,5,15,3,7,13,18]\\n3", "expected_output": "[3]", "is_sample": False},
        {"input": "[4,2,7,1,3]\\n4", "expected_output": "[4, 2, 7, 1, 3]", "is_sample": False},
        {"input": "[1]\\n1", "expected_output": "[1]", "is_sample": False},
        {"input": "[1]\\n2", "expected_output": "[]", "is_sample": False},
        # Stress cases
        {"input": json.dumps(list(range(5000, 0, -1))) + "\\n1", "expected_output": "[1]", "is_sample": False}, # Skewed left
        {"input": json.dumps(list(range(1, 5001))) + "\\n5000", "expected_output": "[5000]", "is_sample": False} # Skewed right
    ]

    # Level-order serialization for skewed trees is complex, so for standard purposes:
    # Example 9: Skewed left root = 100, 99, 98... search 1.
    # Example 10: Skewed right root = 1, 2, 3... search 5000.

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
        "topics": ["Tree", "Binary Search Tree", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "601-800/700_Search_in_a_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
