import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 145
    title = "Binary Tree Postorder Traversal"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>145. Binary Tree Postorder Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the postorder traversal of its nodes' values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/preorder_1.jpg" style="width: 125px; height: 200px;" />
<pre><strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of the nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>"""

    input_format = "A single line containing space-separated values representing level-order traversal of the tree (use 'null' for missing nodes)."
    output_format = "A bracketed array of integers representing the postorder traversal."
    
    constraints = [
        "0 <= Number of nodes <= 100",
        "-100 <= Node.val <= 100",
        "Linear time complexity O(n)",
        "Iterative implementation encouraged."
    ]
    
    explanation = """To perform postorder traversal (Left -> Right -> Root) iteratively:
1. **Modified Preorder Strategy**:
   - Standard preorder is (Root -> Left -> Right).
   - If we modify it to (Root -> Right -> Left) and then reverse the entire result, we get (Left -> Right -> Root), which is postorder.
2. **Algorithm**:
   - Initialize an empty stack and add the root if it exists.
   - Use a result list `res`.
   - While the stack is not empty:
     - Pop a node and append its value to `res`.
     - Push the left child, then the right child to the stack (so the right child is processed first in the next iteration).
   - Reverse `res` and return it.
3. **Complexity**:
   - Time Complexity: O(n) as each node is visited once.
   - Space Complexity: O(n) for the stack or the result list."""
    
    answer = """class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return res[::-1]"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(lst):\n    if not lst: return None\n    root = TreeNode(int(lst[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(lst):\n        node = queue.popleft()\n        if i < len(lst) and lst[i] != 'null':\n            node.left = TreeNode(int(lst[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(lst) and lst[i] != 'null':\n            node.right = TreeNode(int(lst[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef postorderTraversal(root):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if not input_data: print('[]'); sys.exit()\n    root = build_tree(input_data)\n    print(json.dumps(postorderTraversal(root)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <algorithm>\nusing namespace std;\n\nstruct TreeNode {\n    int val; TreeNode *left; TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nvector<int> postorderTraversal(TreeNode* root) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val; TreeNode left; TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static List<Integer> postorderTraversal(TreeNode root) {\n        // User logic\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\n/**\n * @param {TreeNode} root\n * @return {number[]}\n */\nvar postorderTraversal = function(root) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val; struct TreeNode *left; struct TreeNode *right;\n};\n\nint* postorderTraversal(struct TreeNode* root, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 null 2 3", "expected_output": "[3, 2, 1]", "is_sample": True},
        {"input": "", "expected_output": "[]", "is_sample": True},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[2, 3, 1]", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "[3, 2, 1]", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "[3, 2, 1]", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "[4, 5, 2, 3, 1]", "is_sample": False},
        # Stress Tests
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": "...", "is_sample": False},
        {"input": " ".join([str(i) if i % 2 == 0 else "null" for i in range(200)]), "expected_output": "...", "is_sample": False},
        {"input": "1 " + " ".join(["null " + str(i+1) for i in range(99)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _postorder(lst):
        if not lst or lst[0] == "": return []
        def build(l):
            if not l: return None
            r = TreeNode(int(l[0]))
            q = deque([r])
            idx = 1
            while q and idx < len(l):
                curr = q.popleft()
                if idx < len(l) and l[idx] != 'null':
                    curr.left = TreeNode(int(l[idx])); q.append(curr.left)
                idx += 1
                if idx < len(l) and l[idx] != 'null':
                    curr.right = TreeNode(int(l[idx])); q.append(curr.right)
                idx += 1
            return r
        def traverse(node):
            if not node: return []
            return traverse(node.left) + traverse(node.right) + [node.val]
        return traverse(build(lst))

    test_cases[7]["expected_output"] = json.dumps(_postorder(test_cases[7]["input"].split()))
    test_cases[8]["expected_output"] = json.dumps(_postorder(test_cases[8]["input"].split()))
    test_cases[9]["expected_output"] = json.dumps(_postorder(test_cases[9]["input"].split()))

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
        "topics": ["Stack", "Tree", "Depth-First Search", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/145_Binary_Tree_Postorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
