 import json
import os

def generate_json():
    problem_id = 671
    title = "Second Minimum Node In a Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>671. Second Minimum Node In a Binary Tree</h3>
<p>Given a non-empty special binary tree consisting of nodes with non-negative values, where each node in this tree has exactly <code>two</code> or <code>zero</code> sub-nodes. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property <code>root.val = min(root.left.val, root.right.val)</code> always holds.</p>

<p>Given such a binary tree, you need to output the <b>second minimum value</b> in the set made of all the nodes' values in the whole tree.</p>

<p>If no such second minimum value exists, output -1 instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg" style="width: 431px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [2,2,5,null,null,5,7]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The smallest value is 2, the second smallest value is 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg" style="width: 321px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,2,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The smallest value is 2, but there isn't any second smallest value.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 25]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>root.val == min(root.left.val, root.right.val)</code> for each internal node of the tree.</li>
</ul>"""

    input_format = "A single line containing space-separated Level-Order Traversal (use 'null' for missing)."
    output_format = "A single integer representing the second minimum value, or -1 if it doesn't exist."
    
    constraints = [
        "1 <= N <= 25 (Small N)",
        "Node value up to 2^31 - 1.",
        "root.val is always the minimum.",
        "O(N) time complexity.",
        "O(H) extra space."
    ]
    
    explanation = """To find the second minimum node in this special tree:
1. **The Core Property**:
   - For every node, `val = min(left.val, right.val)`.
   - This implies the root value is the absolute minimum in the entire tree.
2. **The Goal**:
   - Find the smallest value in the tree that is strictly greater than `root.val`.
3. **Implementation (DFS)**:
   - Traverse the tree.
   - If a node's value is greater than `root.val`, it's a candidate for the second minimum. We don't need to traverse its children because their values will be $\ge$ the current node's value.
   - Keep track of the minimum candidate found.
4. **Complexity**:
   - Time Complexity: O(N) as we visit each node at most once.
   - Space Complexity: O(H) for recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSecondMinimumValue(root) -> int:
    self_min = root.val
    ans = float('inf')
    
    def dfs(node):
        nonlocal ans
        if not node: return
        if self_min < node.val < ans:
            ans = node.val
        elif node.val == self_min:
            dfs(node.left)
            dfs(node.right)
            
    dfs(root)
    return ans if ans != float('inf') else -1"""

    boilerplate = {
        "python": "import sys\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef findSecondMinimumValue(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Parser and logic\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public int findSecondMinimumValue(TreeNode root) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function findSecondMinimumValue(root) {\n    // User logic\n}",
        "c": "int findSecondMinimumValue(struct TreeNode* root) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2 2 5 null null 5 7", "expected_output": "5", "is_sample": True},
        {"input": "2 2 2", "expected_output": "-1", "is_sample": True},
        {"input": "1", "expected_output": "-1", "is_sample": False},
        {"input": "1 1 3", "expected_output": "3", "is_sample": False},
        {"input": "1 2 1 null null 1 3", "expected_output": "2", "is_sample": False},
        {"input": "5 8 5 null null 5 10", "expected_output": "8", "is_sample": False},
        {"input": "2 2 3", "expected_output": "3", "is_sample": False},
        {"input": "1 1 1 1 1 1 1", "expected_output": "-1", "is_sample": False},
        # Stress cases
        {"input": "2147483647", "expected_output": "-1", "is_sample": False},
        {"input": "1 1 2147483647", "expected_output": "2147483647", "is_sample": False}
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

    output_path = "601-800/671_Second_Minimum_Node_In_a_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
