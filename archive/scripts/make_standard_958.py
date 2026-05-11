import json
import os

def generate_json():
    problem_id = 958
    title = "Check Completeness of a Binary Tree"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>958. Check Completeness of a Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, determine if it is a <em>complete binary tree</em>.</p>

<p>In a <strong><a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">complete binary tree</a></strong>, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between <code>1</code> and <code>2<sup>h</sup></code> nodes inclusive at the last level <code>h</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-1.png" style="width: 180px; height: 145px;" />
<pre><strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> Every level before the last is full (i.e. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
</pre><p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/complete-binary-tree-2.png" style="width: 200px; height: 145px;" />
<pre><strong>Input:</strong> root = [1,2,3,4,5,null,7]
<strong>Output:</strong> false
<strong>Explanation:</strong> The node with value 7 isn't as far left as possible.
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>
"""

    input_format = "A level-order representation of a binary tree."
    output_format = "Boolean true or false."
    
    constraints = [
        "1 <= Number of nodes <= 100",
        "Complete binary tree definition: all levels full except last, last level nodes far left"
    ]
    
    explanation = """To check if a binary tree is complete:
1. **The Core Approach (BFS)**:
   - Perform a Level-Order Traversal (BFS) using a queue.
   - Unlike standard BFS, we add even the **null child nodes** into the queue.
2. **The Observation**:
   - In a complete binary tree, once we encounter a `null` node while traversing level-by-level, **every subsequent node** in the traversal must also be `null`.
3. **The Logic**:
   - Initialize a variable `found_null = False`.
   - While processing nodes from the queue:
     - If the current node is `null`, set `found_null = True`.
     - If the current node is **not** `null`:
       - If `found_null` is already `True`, return `False` (because we found a non-null node after a gap).
       - Otherwise, add left and right children (including nulls) to the queue.
4. **Conclusion**:
   - If the queue is emptied without violation, return `True`.

Complexity:
- Time: O(N) where N is the number of nodes.
- Space: O(N) in the worst case for the queue."""
    
    answer = """def isCompleteTree(root) -> bool:
    if not root: return True
    queue = [root]
    found_null = False
    
    while queue:
        node = queue.pop(0)
        if not node:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(node.left)
            queue.append(node.right)
            
    return True"""

    boilerplate = {
        "python": "class TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef isCompleteTree(root):\n    # User logic here\n    pass",
        "cpp": "struct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode() : val(0), left(nullptr), right(nullptr) {}\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};",
        "java": "public class TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}",
        "c": "struct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};"
    }

    test_cases = [
        {"input": "[1,2,3,4,5,6]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,3,4,5,null,7]", "expected_output": "false", "is_sample": True},
        # Diverse cases
        {"input": "[1]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,null,null,4,5]", "expected_output": "false", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]", "expected_output": "true", "is_sample": False},
        {"input": "[1,null,2]", "expected_output": "false", "is_sample": False},
        {"input": "[1,2,null]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,null,null,null,null]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4,5,null,null]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4,null,null,null]", "expected_output": "true", "is_sample": False}
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
        "topics": ["Tree", "Breadth-First Search", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "standardized_json/801-1000/958_Check_Completeness_of_a_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
