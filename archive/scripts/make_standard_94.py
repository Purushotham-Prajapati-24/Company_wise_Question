import json
import os

def generate_json():
    problem_id = 94
    title = "Binary Tree Inorder Traversal"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>94. Binary Tree Inorder Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the inorder traversal of its nodes' values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 322px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively? """

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree (integers or 'null' for empty nodes)."
    output_format = "A single line containing space-separated integers representing the inorder traversal of the tree."
    
    constraints = [
        "0 <= number of nodes <= 100",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To perform an inorder traversal (Left -> Visit -> Right) of a binary tree:
1. **Recursive Approach**:
   - Base Case: If node is null, return.
   - Recursive Step:
     - `dfs(node.left)`
     - Add `node.val` to result list.
     - `dfs(node.right)`
2. **Iterative Approach (using a Stack)**:
   - Use a stack to keep track of nodes.
   - Starting from `curr = root`, go as far left as possible, pushing each node onto the stack.
   - Once `curr` becomes null, pop from the stack (this is the next node in inorder).
   - Add the popped node's value to the result.
   - Move `curr` to the popped node's right child and repeat.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) where H is the height of the tree (for the recursion stack or explicit stack). In the worst case, O(N)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
        
    return res"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef inorderTraversal(root):\n    # User logic here\n    pass\n\ndef build_tree(vals):\n    if not vals: return None\n    root = TreeNode(int(vals[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != \"null\":\n            node.left = TreeNode(int(vals[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != \"null\":\n            node.right = TreeNode(int(vals[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    if input_data:\n        root = build_tree(input_data)\n        res = inorderTraversal(root)\n        print(*(res))\n    else:\n        print(\"\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <stack>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nvector<int> inorderTraversal(TreeNode* root) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string tok;\n    queue<TreeNode*> q;\n    TreeNode* root = NULL;\n    bool first = true;\n    while (cin >> tok) {\n        TreeNode* node = (tok == \"null\") ? NULL : new TreeNode(stoi(tok));\n        if (first) { root = node; first = false; if (root) q.push(root); }\n        else if (!q.empty()) {\n            TreeNode* p = q.front();\n            if (!p->left) { p->left = node; if (node) q.push(node); }\n            else { p->right = node; if (node) q.push(node); q.pop(); }\n        }\n    }\n    auto res = inorderTraversal(root);\n    for (int i = 0; i < (int)res.size(); i++) cout << res[i] << (i+1<(int)res.size() ? \" \" : \"\");\n    cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static List<Integer> inorderTraversal(TreeNode root) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Queue<TreeNode> q = new LinkedList<>();\n        TreeNode root = null;\n        boolean first = true;\n        while (sc.hasNext()) {\n            String tok = sc.next();\n            TreeNode node = tok.equals(\"null\") ? null : new TreeNode(Integer.parseInt(tok));\n            if (first) { root = node; first = false; if (root != null) q.add(root); }\n            else if (!q.isEmpty()) {\n                TreeNode p = q.peek();\n                if (p.left == null) { p.left = node; if (node != null) q.add(node); }\n                else { p.right = node; if (node != null) q.add(node); q.poll(); }\n            }\n        }\n        List<Integer> res = inorderTraversal(root);\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < res.size(); i++) { if (i > 0) sb.append(' '); sb.append(res.get(i)); }\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val)\n    this.left = (left===undefined ? null : left)\n    this.right = (right===undefined ? null : right)\n}\n\nfunction inorderTraversal(root) {\n    // User logic\n    return [];\n}\n\nconst tokens = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif (tokens.length > 0 && tokens[0] !== '') {\n    let root = null, q = [], i = 0;\n    const mk = t => t === 'null' ? null : new TreeNode(parseInt(t));\n    root = mk(tokens[i++]); if (root) q.push(root);\n    while (q.length && i < tokens.length) {\n        let p = q[0];\n        p.left = mk(tokens[i++]); if (p.left) q.push(p.left);\n        if (i < tokens.length) { p.right = mk(tokens[i++]); if (p.right) q.push(p.right); }\n        q.shift();\n    }\n    console.log(inorderTraversal(root).join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint* inorderTraversal(struct TreeNode* root, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    // Tree parsing from level-order tokens\n    struct TreeNode* nodes[101];\n    int cnt = 0;\n    char tok[20];\n    while (cnt < 101 && scanf(\"%s\", tok) == 1) {\n        if (strcmp(tok, \"null\") == 0) nodes[cnt++] = NULL;\n        else { nodes[cnt] = (struct TreeNode*)malloc(sizeof(struct TreeNode)); nodes[cnt]->val = atoi(tok); nodes[cnt]->left = nodes[cnt]->right = NULL; cnt++; }\n    }\n    if (cnt == 0) { printf(\"\\n\"); return 0; }\n    int qi = 0, ni = 1;\n    while (ni < cnt) {\n        if (nodes[qi]) { nodes[qi]->left = (ni < cnt ? nodes[ni++] : NULL); nodes[qi]->right = (ni < cnt ? nodes[ni++] : NULL); }\n        qi++;\n    }\n    int sz = 0;\n    int* res = inorderTraversal(nodes[0], &sz);\n    for (int i = 0; i < sz; i++) { printf(\"%d\", res[i]); if (i+1<sz) printf(\" \"); }\n    printf(\"\\n\");\n    return 0;\n}"
    }
    

    def _solve(vals):
        if not vals or vals[0] == "null": return []
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
        
        res = []
        def dfs(n):
            if n:
                dfs(n.left)
                res.append(n.val)
                dfs(n.right)
        dfs(root)
        return res

    sample1 = ["1", "null", "2", "3"]
    test_cases = [
        {"input": " ".join(sample1), "expected_output": " ".join(map(str, _solve(sample1))), "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        {"input": "1 2 3", "expected_output": "2 1 3", "is_sample": False},
        {"input": "1 2 null 3 null 4", "expected_output": "4 3 2 1", "is_sample": False},
        {"input": "1 null 2 null 3 null 4", "expected_output": "1 2 3 4", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "4 2 5 1 6 3 7", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(1, 101))), "expected_output": " ".join(map(str, _solve([str(x) for x in range(1, 101)]))), "is_sample": False},
        {"input": " ".join(["1"] + ["null", "1"]*49), "expected_output": " ".join(["1"]*50), "is_sample": False},
        {"input": " ".join(["1"] + ["1", "null"]*49), "expected_output": " ".join(["1"]*50), "is_sample": False}
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
        "topics": ["Tree", "Stack", "Binary Tree", "Inorder Traversal"],
        "companyIndex": 0
    }

    output_path = "1-200/94_Binary_Tree_Inorder_Traversal.json"
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
