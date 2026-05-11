import json
import os

def generate_json():
    problem_id = 653
    title = "Two Sum IV - Input is a BST"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>653. Two Sum IV - Input is a BST</h3>
<p>Given the <code>root</code> of a binary search tree and an integer <code>k</code>, return <code>true</code> <em>if there exist two elements in the BST such that their sum is equal to the given target</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="width: 400px; height: 229px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 9
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="width: 400px; height: 229px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], k = 28
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li><code>root</code> is guaranteed to be a valid binary search tree.</li>
	<li><code>-10<sup>5</sup> &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "Two lines: 1) Space-separated Level-Order Traversal (use 'null' for missing) 2) integer k."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= N <= 10^4",
        "Target k can be large.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To check if any two nodes in a BST sum to $k$:
1. **The Strategy (HashSet)**:
   - Traverse the tree (using BFS or DFS).
   - Maintain a set `seen` of values we've encountered.
   - For each node with value `v`, check if `k - v` is in `seen`.
   - If yes, return `true`.
   - If no, add `v` to `seen`.
2. **Alternative (Sorted In-order)**:
   - Perform an in-order traversal to get a sorted array of values.
   - Use two pointers to find the target sum in the sorted array.
3. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(N) to store the hash set or the flattened array."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k: int) -> bool:
    seen = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if (k - node.val) in seen:
            return True
        seen.add(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return False"""

    boilerplate = {
        "python": "import sys\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef findTarget(root, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Parser logic here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n#include <string>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public boolean findTarget(TreeNode root, int k) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function findTarget(root, k) {\n    // User logic\n}",
        "c": "bool findTarget(struct TreeNode* root, int k) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "5 3 6 2 4 null 7\\n9", "expected_output": "true", "is_sample": True},
        {"input": "5 3 6 2 4 null 7\\n28", "expected_output": "false", "is_sample": True},
        {"input": "1\\n2", "expected_output": "false", "is_sample": False},
        {"input": "2 1 3\\n4", "expected_output": "true", "is_sample": False},
        {"input": "1 null 2 null 3\\n4", "expected_output": "true", "is_sample": False},
        {"input": "0 -1 2\\n1", "expected_output": "true", "is_sample": False},
        {"input": "10 5 15 3 7 null 18\\n22", "expected_output": "true", "is_sample": False},
        {"input": "1 null 2\\n0", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 100)]).replace("null", "null") + "\\n500", "expected_output": "false", "is_sample": False},
        {"input": "2147483647 null null\\n0", "expected_output": "false", "is_sample": False}
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
        "topics": ["Tree", "DFS", "BFS", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "601-800/653_Two_Sum_IV_Input_is_a_BST.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
