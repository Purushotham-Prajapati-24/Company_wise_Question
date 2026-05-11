import json
import os

def generate_json():
    problem_id = 404
    title = "Sum of Left Leaves"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>404. Sum of Left Leaves</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the sum of all left leaves.</em></p>

<p>A <strong>leaf</strong> is a node with no children. A <strong>left leaf</strong> is a leaf that is the left child of another node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" style="width: 277px; height: 302px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 24
<strong>Explanation:</strong> There are two left leaves in the binary tree, with values 9 and 15 respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "The root of a binary tree."
    output_format = "An integer sum."
    
    constraints = [
        "1 <= number of nodes <= 1000",
        "-1000 <= val <= 1000"
    ]
    
    explanation = """To find the sum of all left leaves, we can perform a standard tree traversal (DFS or BFS) and keep track of whether a node is a left child.

### Key Observation:
- A node is a **left leaf** if:
  1. It is the **left child** of its parent.
  2. It has **no children** (left and right are both null).

### Algorithm Steps:
1. **Recursive DFS**: 
   - Define a function `dfs(node, is_left)`:
   - Base Case: If `node` is None, return 0.
   - If `node` is a leaf (no children) AND `is_left` is true, return `node.val`.
   - Else, return `dfs(node.left, True) + dfs(node.right, False)`.
2. **Result**: Call `dfs(root, False)` (since the root itself is not a left child of anything).

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the tree. We visit each node once.
- **Space Complexity**: $O(H)$, where $H$ is the height of the tree, for the recursion stack."""
    
    answer = """class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            
            # Check if current node is a leaf
            if not node.left and not node.right:
                return node.val if is_left else 0
            
            # Recurse
            return dfs(node.left, True) + dfs(node.right, False)
            
        return dfs(root, False)"""

    boilerplate = {
        "python": "# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\nimport sys\nimport json\n\nclass Solution:\n    def sumOfLeftLeaves(self, root) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    # Tree deserialization and exec logic here\n    pass",
        "cpp": "class Solution {\npublic:\n    int sumOfLeftLeaves(TreeNode* root) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "public class Solution {\n    public int sumOfLeftLeaves(TreeNode root) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {TreeNode} root\n * @return {number}\n */\nvar sumOfLeftLeaves = function(root) {\n    // Your logic here\n};",
        "c": "int sumOfLeftLeaves(struct TreeNode* root) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,9,20,null,null,15,7]", "expected_output": "24", "is_sample": True},
        {"input": "[1]", "expected_output": "0", "is_sample": True},
        {"input": "[1,2,3,4,5]", "expected_output": "4", "is_sample": False},
        {"input": "[1,null,2]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,null,3,null,4,null,5]", "expected_output": "5", "is_sample": False},
        {"input": "[-1000]", "expected_output": "0", "is_sample": False},
        {"input": "[0,0,0,0,null,null,0]", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(1000)]", "expected_output": "...", "is_sample": False},
        {"input": "[1]*1000", "expected_output": "...", "is_sample": False},
        {"input": "[1000, -1000, 1000, -1000, null, null, 1000]", "expected_output": "-1000", "is_sample": False}
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
        "companyIndex": 1
    }

    output_path = "301-500/404_Sum_of_Left_Leaves.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
