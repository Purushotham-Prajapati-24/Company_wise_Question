import json
import os

def generate_json():
    problem_id = 662
    title = "Maximum Width of Binary Tree"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>662. Maximum Width of Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the <b>maximum width</b> of the given tree</em>.</p>

<p>The <b>maximum width</b> of a tree is the maximum width among all levels.</p>

<p>The <b>width</b> of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.</p>

<p>It is <b>guaranteed</b> that the answer will in the range of a <b>32-bit</b> signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width1-tree.jpg" style="width: 359px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,3,2,5,3,null,9]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The maximum width exists in the third level with width 4 (5,3,null,9).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/14/maximum-width-of-binary-tree-v3.png" style="width: 442px; height: 422px;" />
<pre>
<strong>Input:</strong> root = [1,3,2,5,null,null,9,6,null,7]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The maximum width exists in the fourth level with width 7 (6,null,null,null,null,null,7).
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/width3-tree.jpg" style="width: 369px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,3,2,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum width exists in the second level with width 2 (3,2).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A single line containing space-separated Level-Order Traversal (use 'null' for missing)."
    output_format = "A single integer representing the maximum width."
    
    constraints = [
        "1 <= N <= 3000",
        "Width calculation counts internal nulls.",
        "O(N) time complexity.",
        "O(W) extra space (BFS queue)."
    ]
    
    explanation = """To find the maximum width of a binary tree:
1. **The Strategy (Index Assignment)**:
   - Perform a Level-Order traversal (BFS).
   - Assign an index to each node.
   - If a node at index $i$ has children:
     - Left child index: $2 \times i$
     - Right child index: $2 \times i + 1$
   - This indexing mimics the binary heap layout.
2. **Width Calculation**:
   - For each level, find the min index $L$ and max index $R$ among the nodes present.
   - The width of that level is $R - L + 1$.
   - The result is the maximum width across all levels.
3. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(W) where W is the maximum width of the tree."""
    
    answer = """from collections import deque
def widthOfBinaryTree(root) -> int:
    if not root: return 0
    max_width = 0
    queue = deque([(root, 0)])
    while queue:
        level_size = len(queue)
        min_idx = queue[0][1]
        max_idx = queue[-1][1]
        max_width = max(max_width, max_idx - min_idx + 1)
        for _ in range(level_size):
            node, idx = queue.popleft()
            # To avoid large integers, normalize index relative to level start
            rel_idx = idx - min_idx
            if node.left: queue.append((node.left, 2 * rel_idx))
            if node.right: queue.append((node.right, 2 * rel_idx + 1))
    return max_width"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef widthOfBinaryTree(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Parser logic here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public int widthOfBinaryTree(TreeNode root) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function widthOfBinaryTree(root) {\n    // User logic\n}",
        "c": "int widthOfBinaryTree(struct TreeNode* root) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3 2 5 3 null 9", "expected_output": "4", "is_sample": True},
        {"input": "1 3 2 5 null null 9 6 null 7", "expected_output": "7", "is_sample": True},
        {"input": "1 3 2 5", "expected_output": "2", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 3 null 5 3", "expected_output": "2", "is_sample": False},
        {"input": "1 3 2 5 null null null 6", "expected_output": "8", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "4", "is_sample": False},
        {"input": "0 null 0 null 0 null 0", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 2047), "expected_output": "1024", "is_sample": False},
        {"input": " ".join(["1", "null"] * 1000) + " 1", "expected_output": "1", "is_sample": False}
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

    output_path = "601-800/662_Maximum_Width_of_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
