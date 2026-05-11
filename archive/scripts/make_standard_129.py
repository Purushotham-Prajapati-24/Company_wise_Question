import json
import os
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_json():
    problem_id = 129
    title = "Sum Root to Leaf Numbers"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>129. Sum Root to Leaf Numbers</h3>
<p>You are given the <code>root</code> of a binary tree containing digits from <code>0</code> to <code>9</code> only.</p>

<p>Each root-to-leaf path in the tree represents a number.</p>

<ul>
	<li>For example, the root-to-leaf path <code>1 -&gt; 2 -&gt; 3</code> represents the number <code>123</code>.</li>
</ul>

<p>Return <em>the total sum of all root-to-leaf numbers</em>. Test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>A <strong>leaf</strong> node is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/30/num1tree.jpg" style="width: 212px; height: 182px;" />
<pre><strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 25
<strong>Explanation:</strong>
The root-to-leaf path <code>1-&gt;2</code> represents the number <code>12</code>.
The root-to-leaf path <code>1-&gt;3</code> represents the number <code>13</code>.
Therefore, sum = 12 + 13 = 25.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/30/num2tree.jpg" style="width: 292px; height: 302px;" />
<pre><strong>Input:</strong> root = [4,9,0,5,1]
<strong>Output:</strong> 1026
<strong>Explanation:</strong>
The root-to-leaf path <code>4-&gt;9-&gt;5</code> represents the number <code>495</code>.
The root-to-leaf path <code>4-&gt;9-&gt;1</code> represents the number <code>491</code>.
The root-to-leaf path <code>4-&gt;0</code> represents the number <code>40</code>.
Therefore, sum = 495 + 491 + 40 = 1026.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>The depth of the tree will not exceed <code>10</code>.</li>
</ul>"""

    input_format = "A single line containing a bracketed array representing level-order traversal of the tree."
    output_format = "An integer representing the total sum of all root-to-leaf numbers."
    
    constraints = [
        "1 <= Number of nodes <= 1000",
        "0 <= Node.val <= 9",
        "Max tree depth = 10",
        "Result fits in a 32-bit integer."
    ]
    
    explanation = """To find the sum of all root-to-leaf numbers:
1. **DFS Traversal**: Use Depth-First Search to explore all paths from root to leaf.
2. **Current Number Tracking**: Maintain `current_num` as you descend. For each node, `current_num = current_num * 10 + node.val`.
3. **Leaf Check**: If a node is a leaf (no children), add the `current_num` to the total total.
4. **Complexity**:
   - Time Complexity: O(n) as each node is visited once.
   - Space Complexity: O(h) for the recursion stack, where h is the tree's height (max 10)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum = curr_sum * 10 + node.val
            
            # If leaf, return current path sum
            if not node.left and not node.right:
                return curr_sum
            
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
            
        return dfs(root, 0)"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(lst):\n    if not lst: return None\n    root = TreeNode(lst[0])\n    queue = deque([root])\n    idx = 1\n    while queue and idx < len(lst):\n        curr = queue.popleft()\n        if idx < len(lst) and lst[idx] is not None:\n            curr.left = TreeNode(lst[idx]); queue.append(curr.left)\n        idx += 1\n        if idx < len(lst) and lst[idx] is not None:\n            curr.right = TreeNode(lst[idx]); queue.append(curr.right)\n        idx += 1\n    return root\n\ndef sumNumbers(root):\n    # User logic\n    return 0\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if not line: sys.exit()\n    vals = [x if x == 'null' else int(x) for x in line.replace('[','').replace(']','').replace(',',' ').split()]\n    vals = [None if x == 'null' else x for x in vals]\n    print(sumNumbers(build_tree(vals)))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nstruct TreeNode {\n    int val; TreeNode *left; TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nint sumNumbers(TreeNode* root) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val; TreeNode left; TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static int sumNumbers(TreeNode root) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\n/**\n * @param {TreeNode} root\n * @return {number}\n */\nvar sumNumbers = function(root) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val; struct TreeNode *left; struct TreeNode *right;\n};\n\nint sumNumbers(struct TreeNode* root) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3", "expected_output": "25", "is_sample": True},
        {"input": "4 9 0 5 1", "expected_output": "1026", "is_sample": True},
        {"input": "1 0", "expected_output": "10", "is_sample": False},
        {"input": "9", "expected_output": "9", "is_sample": False},
        {"input": "1 2 3 4", "expected_output": "137", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "123", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "532", "is_sample": False},
        # Stress Tests
        {"input": "1 " + " ".join(["0"] * 9), "expected_output": "...", "is_sample": False},
        {"input": " ".join(["9"] * 10), "expected_output": "...", "is_sample": False},
        {"input": "9 8 7 6 5 4 3 2 1 0", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(lst):
        if not lst: return 0
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
        def dfs(n, s):
            if not n: return 0
            s = s * 10 + n.val
            if not n.left and not n.right: return s
            return dfs(n.left, s) + dfs(n.right, s)
        return dfs(build(lst), 0)

    for i in range(len(test_cases)):
        test_cases[i]["expected_output"] = str(_solve(test_cases[i]["input"].split()))

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
        "topics": ["Tree", "Depth-First Search", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/129_Sum_Root_to_Leaf_Numbers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
