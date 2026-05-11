import json
import os

def generate_json():
    problem_id = 98
    title = "Validate Binary Search Tree"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>98. Validate Binary Search Tree</h3>
<p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>strictly less than</strong> the node's key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>strictly greater than</strong> the node's key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" />
<pre>
<strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree (integers or 'null')."
    output_format = "A boolean (true/false) representing if the tree is a valid BST."
    
    constraints = [
        "1 <= number of nodes <= 10^4",
        "-2^31 <= Node.val <= 2^31 - 1."
    ]
    
    explanation = """To validate a Binary Search Tree (BST):
1. **Range-based DFS**:
   - A node is valid if its value lies strictly within a range `(low, high)`.
   - For the root, the range is `(-infinity, +infinity)`.
   - When moving to the **left** child, update the upper bound: `(low, node.val)`.
   - When moving to the **right** child, update the lower bound: `(node.val, high)`.
   - If any node violates this range, or any child subtree is invalid, return `false`.
2. **Inorder Traversal Approach**:
   - An inorder traversal of a valid BST must result in a strictly increasing sequence of values.
   - Keep track of the previously visited node's value and compare it with the current node's value.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) where H is the height of the tree, for the recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
                
    return validate(root)"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef isValidBST(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(str(isValidBST(build_tree(data))).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <climits>\n\nusing namespace std;\n\nstruct TreeNode {\n    long long val;\n    TreeNode *left, *right;\n    TreeNode(long long x) : val(x), left(NULL), right(NULL) {}\n};\n\nbool isValidBST(TreeNode* root) {\n    // User logic\n    return true;\n}\n\nint main() {\n    string tok;\n    queue<TreeNode*> q;\n    TreeNode* root = NULL;\n    bool first = true;\n    while (cin >> tok) {\n        TreeNode* node = (tok == \"null\") ? NULL : new TreeNode(stoll(tok));\n        if (first) { root = node; first = false; if (root) q.push(root); }\n        else if (!q.empty()) {\n            TreeNode* p = q.front();\n            if (!p->left) { p->left = node; if (node) q.push(node); }\n            else { p->right = node; if (node) q.push(node); q.pop(); }\n        }\n    }\n    cout << (isValidBST(root) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static boolean isValidBST(TreeNode root) {\n        // User logic\n        return true;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Queue<TreeNode> q = new LinkedList<>();\n        TreeNode root = null;\n        boolean first = true;\n        while (sc.hasNext()) {\n            String tok = sc.next();\n            TreeNode node = tok.equals(\"null\") ? null : new TreeNode(Integer.parseInt(tok));\n            if (first) { root = node; first = false; if (root != null) q.add(root); }\n            else if (!q.isEmpty()) {\n                TreeNode p = q.peek();\n                if (p.left == null) { p.left = node; if (node != null) q.add(node); }\n                else { p.right = node; if (node != null) q.add(node); q.poll(); }\n            }\n        }\n        System.out.println(isValidBST(root) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val)\n    this.left = (left===undefined ? null : left)\n    this.right = (right===undefined ? null : right)\n}\n\nfunction isValidBST(root) {\n    // User logic\n    return true;\n}\n\nconst tokens = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (tokens.length > 0 && tokens[0] !== '') {\n    let root = null, q = [], i = 0;\n    const mk = t => t === 'null' ? null : new TreeNode(parseInt(t));\n    root = mk(tokens[i++]); if (root) q.push(root);\n    while (q.length && i < tokens.length) {\n        let p = q[0];\n        p.left = mk(tokens[i++]); if (p.left) q.push(p.left);\n        if (i < tokens.length) { p.right = mk(tokens[i++]); if (p.right) q.push(p.right); }\n        q.shift();\n    }\n    console.log(isValidBST(root).toString());\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nbool isValidBST(struct TreeNode* root) {\n    // User logic\n    return true;\n}\n\nint main() {\n    struct TreeNode* nodes[10001];\n    int cnt = 0;\n    char tok[20];\n    while (cnt < 10001 && scanf(\"%s\", tok) == 1) {\n        if (strcmp(tok, \"null\") == 0) nodes[cnt++] = NULL;\n        else { nodes[cnt] = (struct TreeNode*)malloc(sizeof(struct TreeNode)); nodes[cnt]->val = atoi(tok); nodes[cnt]->left = nodes[cnt]->right = NULL; cnt++; }\n    }\n    if (cnt == 0) { printf(\"true\\n\"); return 0; }\n    int qi = 0, ni = 1;\n    while (ni < cnt) {\n        if (nodes[qi]) { nodes[qi]->left = (ni < cnt ? nodes[ni++] : NULL); nodes[qi]->right = (ni < cnt ? nodes[ni++] : NULL); }\n        qi++;\n    }\n    printf(\"%s\\n\", isValidBST(nodes[0]) ? \"true\" : \"false\");\n    return 0;\n}"
    }
    

    def _solve(vals):
        if not vals or vals[0] == "null": return True
        from collections import deque
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
            
        def validate(node, low, high):
            if not node: return True
            if not (low < node.val < high): return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, -float('inf'), float('inf'))

    test_cases = [
        {"input": "2 1 3", "expected_output": "true", "is_sample": True},
        {"input": "5 1 4 null null 3 6", "expected_output": "false", "is_sample": True},
        {"input": "1 1", "expected_output": "false", "is_sample": False},
        {"input": "2 2 2", "expected_output": "false", "is_sample": False},
        {"input": "10 5 15 null null 6 20", "expected_output": "false", "is_sample": False},
        {"input": "2147483647", "expected_output": "true", "is_sample": False},
        {"input": "-2147483648 null 2147483647", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(100))), "expected_output": "false", "is_sample": False},
        {"input": "25 null 30", "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i) if i%2==0 else "null" for i in range(100)]), "expected_output": "false", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Search Tree", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/98_Validate_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

# Local TreeNode for script logic
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    generate_json()
