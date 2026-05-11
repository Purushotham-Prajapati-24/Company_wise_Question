import json
import os

def generate_json():
    problem_id = 687
    title = "Longest Univalue Path"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>687. Longest Univalue Path</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the length of the longest path where each node in the path has the same value</em>. This path may or may not pass through the root.</p>

<p>The <b>length</b> of the path between two nodes is represented by the number of edges between them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg" style="width: 450px; height: 238px;" />
<pre>
<strong>Input:</strong> root = [5,4,5,1,1,null,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The shown image shows that the longest path of the same value (5) has length 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg" style="width: 450px; height: 238px;" />
<pre>
<strong>Input:</strong> root = [1,4,5,4,4,null,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The shown image shows that the longest path of the same value (4) has length 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>The depth of the tree will not exceed <code>1000</code>.</li>
</ul>"""

    input_format = "A single line containing space-separated Level-Order Traversal (use 'null' for missing)."
    output_format = "A single integer representing the length of the longest univalue path."
    
    constraints = [
        "0 <= N <= 10^4",
        "Path length is count of edges.",
        "O(N) time complexity.",
        "O(H) extra space (recursion stack)."
    ]
    
    explanation = """To find the longest univalue path in a binary tree:
1. **The Recursive Goal**:
   - For each node, find the longest univalue path starting from that node and moving down to its children.
2. **Implementation (DFS)**:
   - Perform a post-order traversal (bottom-up).
   - If `node.left` exists and `node.left.val == node.val`:
     - `left_path = left_len + 1`
   - Else: `left_path = 0`.
   - If `node.right` exists and `node.right.val == node.val`:
     - `right_path = right_len + 1`
   - Else: `right_path = 0`.
   - Update the global maximum length: `max_ans = max(max_ans, left_path + right_path)`.
   - Return `max(left_path, right_path)` to the parent.
3. **Complexity**:
   - Time Complexity: O(N) as we visit each node once.
   - Space Complexity: O(H) for recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUnivaluePath(root) -> int:
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node: return 0
        left_len = dfs(node.left)
        right_len = dfs(node.right)
        
        left_arrow = right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left_len + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_len + 1
            
        ans = max(ans, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)
        
    dfs(root)
    return ans"""

    boilerplate = {
        "python": "import sys\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef longestUnivaluePath(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # Parser and Level-Order Processing\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n};",
        "java": "public class Solution {\n    public int longestUnivaluePath(TreeNode root) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function longestUnivaluePath(root) {\n    // User logic\n}",
        "c": "int longestUnivaluePath(struct TreeNode* root) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5 4 5 1 1 null 5", "expected_output": "2", "is_sample": True},
        {"input": "1 4 5 4 4 null 5", "expected_output": "2", "is_sample": True},
        {"input": "1", "expected_output": "0", "is_sample": False},
        {"input": "1 1 1", "expected_output": "2", "is_sample": False},
        {"input": "1 null 1 null 1", "expected_output": "2", "is_sample": False},
        {"input": "5 5 5 1 1 5 5", "expected_output": "2", "is_sample": False},
        {"input": "1 2 3", "expected_output": "0", "is_sample": False},
        {"input": "4 4 4 4 4 4 4", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 2047), "expected_output": "20", "is_sample": False},
        {"input": "null", "expected_output": "0", "is_sample": False}
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

    output_path = "601-800/687_Longest_Univalue_Path.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
