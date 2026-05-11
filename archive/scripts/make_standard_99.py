import json
import os

def generate_json():
    problem_id = 99
    title = "Recover Binary Search Tree"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>99. Recover Binary Search Tree</h3>
<p>You are given the <code>root</code> of a binary search tree (BST), where the values of <strong>exactly</strong> two nodes of the tree were swapped by mistake. <em>Recover the tree without changing its structure</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg" style="width: 422px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,3,null,null,2]
<strong>Output:</strong> [3,1,null,null,2]
<strong>Explanation:</strong> 3 cannot be a left child of 1 because 3 &gt; 1. Swapping 1 and 3 makes the BST valid.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg" style="width: 581px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,1,4,null,null,2]
<strong>Output:</strong> [2,1,4,null,null,3]
<strong>Explanation:</strong> 2 cannot be in the right subtree of 3 because 2 &lt; 3. Swapping 2 and 3 makes the BST valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 1000]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> A solution using <code>O(n)</code> space is pretty straight-forward. Could you devise a constant <code>O(1)</code> space solution? """

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree with two swapped nodes."
    output_format = "A single line containing space-separated values representing the level-order traversal of the recovered tree."
    
    constraints = [
        "2 <= number of nodes <= 1000",
        "-2^31 <= Node.val <= 2^31 - 1.",
        "Exactly two nodes are swapped."
    ]
    
    explanation = """To recover a BST where two nodes were swapped:
1. **Inorder Traversal Logic**:
   - In a correct BST, the inorder traversal results in a strictly increasing sequence.
   - If two nodes are swapped, there will be either one or two points in the inorder sequence where the current value is smaller than the previous one (`prev.val > curr.val`).
2. **Identification**:
   - **First Occurrence**: The first node that is larger than its successor is the first swapped node (`first = prev`).
   - **Second Occurrence**: The last node that is smaller than its predecessor is the second swapped node (`second = curr`).
   - If there is only one such occurrence (adjacent nodes), `first = prev` and `second = curr` from that single occurrence.
3. **Execution**:
   - Perform iterative or recursive inorder traversal.
   - Identify `first` and `second`.
   - Swap their values.
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) for the stack/recursion. Constant space O(1) is possible using Morris Traversal."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    stack = []
    curr = root
    prev = None
    first = second = None
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        
        if prev and prev.val > curr.val:
            if not first:
                first = prev
            second = curr # Always update second to find the last drop
            
        prev = curr
        curr = curr.right
        
    if first and second:
        first.val, second.val = second.val, first.val"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef recoverTree(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == \"null\": return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef level_order(root):\n    if not root: return \"\"\n    res = []\n    queue = deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            res.append(str(node.val))\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \" \".join(res)\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        root = build_tree(data)\n        recoverTree(root)\n        print(level_order(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nvoid recoverTree(TreeNode* root) {\n    // User logic\n}\n\nint main() {\n    string tok;\n    queue<TreeNode*> q;\n    TreeNode* root = NULL;\n    bool first = true;\n    while (cin >> tok) {\n        TreeNode* node = (tok == \"null\") ? NULL : new TreeNode(stoi(tok));\n        if (first) { root = node; first = false; if (root) q.push(root); }\n        else if (!q.empty()) {\n            TreeNode* p = q.front();\n            if (!p->left) { p->left = node; if (node) q.push(node); }\n            else { p->right = node; if (node) q.push(node); q.pop(); }\n        }\n    }\n    recoverTree(root);\n    // Level-order print\n    queue<TreeNode*> pq;\n    if (root) pq.push(root);\n    bool pr = false;\n    while (!pq.empty()) {\n        TreeNode* n = pq.front(); pq.pop();\n        if (pr) cout << \" \"; pr = true;\n        if (n) { cout << n->val; if (n->left) pq.push(n->left); if (n->right) pq.push(n->right); }\n    }\n    cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static void recoverTree(TreeNode root) {\n        // User logic\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Queue<TreeNode> q = new LinkedList<>();\n        TreeNode root = null;\n        boolean first = true;\n        while (sc.hasNext()) {\n            String tok = sc.next();\n            TreeNode node = tok.equals(\"null\") ? null : new TreeNode(Integer.parseInt(tok));\n            if (first) { root = node; first = false; if (root != null) q.add(root); }\n            else if (!q.isEmpty()) {\n                TreeNode p = q.peek();\n                if (p.left == null) { p.left = node; if (node != null) q.add(node); }\n                else { p.right = node; if (node != null) q.add(node); q.poll(); }\n            }\n        }\n        recoverTree(root);\n        Queue<TreeNode> pq = new LinkedList<>();\n        if (root != null) pq.add(root);\n        StringBuilder sb = new StringBuilder();\n        while (!pq.isEmpty()) { TreeNode n = pq.poll(); if (sb.length() > 0) sb.append(' '); sb.append(n.val); if (n.left != null) pq.add(n.left); if (n.right != null) pq.add(n.right); }\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction recoverTree(root) {\n    // User logic\n}\n\nconst tokens = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (tokens.length > 0 && tokens[0] !== '') {\n    let root = null, q = [], i = 0;\n    const mk = t => t === 'null' ? null : new TreeNode(parseInt(t));\n    root = mk(tokens[i++]); if (root) q.push(root);\n    while (q.length && i < tokens.length) {\n        let p = q[0];\n        p.left = mk(tokens[i++]); if (p.left) q.push(p.left);\n        if (i < tokens.length) { p.right = mk(tokens[i++]); if (p.right) q.push(p.right); }\n        q.shift();\n    }\n    recoverTree(root);\n    const out = [], bfs = [root];\n    while (bfs.length) { const n = bfs.shift(); if (n) { out.push(n.val); bfs.push(n.left, n.right); } }\n    console.log(out.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nvoid recoverTree(struct TreeNode* root) {\n    // User logic\n}\n\nint main() {\n    struct TreeNode* nodes[1001];\n    int cnt = 0;\n    char tok[20];\n    while (cnt < 1001 && scanf(\"%s\", tok) == 1) {\n        if (strcmp(tok, \"null\") == 0) nodes[cnt++] = NULL;\n        else { nodes[cnt] = (struct TreeNode*)malloc(sizeof(struct TreeNode)); nodes[cnt]->val = atoi(tok); nodes[cnt]->left = nodes[cnt]->right = NULL; cnt++; }\n    }\n    if (cnt == 0) return 0;\n    int qi = 0, ni = 1;\n    while (ni < cnt) {\n        if (nodes[qi]) { nodes[qi]->left = (ni < cnt ? nodes[ni++] : NULL); nodes[qi]->right = (ni < cnt ? nodes[ni++] : NULL); }\n        qi++;\n    }\n    recoverTree(nodes[0]);\n    struct TreeNode* bfs[1001]; int h = 0, t = 0;\n    bfs[t++] = nodes[0];\n    int first = 1;\n    while (h < t) { struct TreeNode* n = bfs[h++]; if (!first) printf(\" \"); first = 0; printf(\"%d\", n->val); if (n->left) bfs[t++] = n->left; if (n->right) bfs[t++] = n->right; }\n    printf(\"\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3 null null 2", "expected_output": "3 1 null null 2", "is_sample": True},
        {"input": "3 1 4 null null 2", "expected_output": "2 1 4 null null 3", "is_sample": True},
        {"input": "3 2 1", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1 2", "expected_output": "2 1", "is_sample": False},
        {"input": "2 null 1", "expected_output": "1 null 2", "is_sample": False},
        {"input": "3 1 4 null null 2 5", "expected_output": "2 1 4 null null 3 5", "is_sample": False},
        {"input": "5 3 7 2 6 4 8", "expected_output": "5 3 7 2 4 6 8", "is_sample": False},
        {"input": "10 5 15 null null 7 20", "expected_output": "10 5 15 null null 7 20", "is_sample": False},
        {"input": "4 2 6 1 3 5 8", "expected_output": "4 2 6 1 3 5 8", "is_sample": False},
        {"input": "6 2 8 1 5 3 9", "expected_output": "6 2 8 1 5 3 9", "is_sample": False}
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

    output_path = "1-200/99_Recover_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
