import json
import os

def generate_json():
    problem_id = 236
    title = "Lowest Common Ancestor of a Binary Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>236. Lowest Common Ancestor of a Binary Tree</h3>
<p>Given a binary tree, find the lowest common ancestor (LCA) node of two given nodes in the tree.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre><strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The LCA of nodes 5 and 1 is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<pre><strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation:</strong> The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [1,2], p = 1, q = 2
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> will exist in the tree.</li>
</ul>"""

    input_format = "Three lines: first, the tree root (level-order); second, value of p; third, value of q."
    output_format = "The value of the LCA node."
    
    constraints = [
        "2 <= n <= 100,000",
        "Unique node values.",
        "p and q guaranteed to exist."
    ]
    
    explanation = """To find the LCA in a general Binary Tree:
1. **Recursive DFS**: 
   - If the current node is `null`, `p`, or `q`, return the current node.
   - Recursively search the left and right subtrees for nodes `p` and `q`.
2. **Logic**:
   - `left = search(root.left)`
   - `right = search(root.right)`
   - If both `left` and `right` are non-null, it means `p` and `q` are in different subtrees, so the current node is their Lowest Common Ancestor.
   - If only one is non-null, return that non-null value (the target node or their common ancestor found deeper).
3. **Complexity**:
   - Time: O(N) as we visit every node in the worst case.
   - Space: O(H) for the call stack, where H is the height of the tree."""
    
    answer = """class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(vals):\n    if not vals: return None\n    root = TreeNode(vals[0])\n    queue = deque([root])\n    i = 1\n    while i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] is not None:\n            node.left = TreeNode(vals[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] is not None:\n            node.right = TreeNode(vals[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef find_node(root, val):\n    if not root: return None\n    if root.val == val: return root\n    left = find_node(root.left, val)\n    if left: return left\n    return find_node(root.right, val)\n\ndef lowestCommonAncestor(root, p, q):\n    # User logic here\n    return root\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        try:\n            arr = json.loads(lines[0])\n        except:\n            arr = [int(x) if x != 'null' else None for x in lines[0].replace('[', '').replace(']', '').replace(',', ' ').split()]\n        root = build_tree(arr)\n        p = find_node(root, int(lines[1]))\n        q = find_node(root, int(lines[2]))\n        res = lowestCommonAncestor(root, p, q)\n        if res: print(res.val)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nTreeNode* findNode(TreeNode* root, int val) {\n    if (!root) return NULL;\n    if (root->val == val) return root;\n    TreeNode* left = findNode(root->left, val);\n    if (left) return left;\n    return findNode(root->right, val);\n}\n\nTreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n    // User logic\n    return root;\n}\n\nint main() {\n    string line, pLine, qLine;\n    if (getline(cin, line) && getline(cin, pLine) && getline(cin, qLine)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        string val;\n        vector<string> nodes;\n        while (ss >> val) nodes.push_back(val);\n        TreeNode* root = buildTree(nodes);\n        TreeNode* p = findNode(root, stoi(pLine));\n        TreeNode* q = findNode(root, stoi(qLine));\n        TreeNode* res = lowestCommonAncestor(root, p, q);\n        if (res) cout << res->val << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        // User logic\n        return root;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        String pLine = br.readLine();\n        String qLine = br.readLine();\n        if (line != null && pLine != null && qLine != null) {\n            line = line.replace(\"[\", \"\").replace(\"]\", \"\").replace(\",\", \" \");\n            String[] parts = line.trim().split(\"\\\\s+\");\n            TreeNode root = buildTree(parts);\n            TreeNode p = findNode(root, Integer.parseInt(pLine.trim()));\n            TreeNode q = findNode(root, Integer.parseInt(qLine.trim()));\n            TreeNode res = new Solution().lowestCommonAncestor(root, p, q);\n            if (res != null) System.out.println(res.val);\n        }\n    }\n\n    static TreeNode buildTree(String[] nodes) {\n        if (nodes.length == 0 || nodes[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.length) {\n            TreeNode curr = q.poll();\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    static TreeNode findNode(TreeNode root, int val) {\n        if (root == null) return null;\n        if (root.val == val) return root;\n        TreeNode left = findNode(root.left, val);\n        if (left != null) return left;\n        return findNode(root.right, val);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val) {\n    this.val = val;\n    this.left = this.right = null;\n}\n\nfunction buildTree(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]);\n    let q = [root];\n    let i = 1;\n    while (q.length && i < arr.length) {\n        let curr = q.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            q.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction findNode(root, val) {\n    if (!root) return null;\n    if (root.val === val) return root;\n    return findNode(root.left, val) || findNode(root.right, val);\n}\n\nfunction lowestCommonAncestor(root, p, q) {\n    // User logic here\n    return root;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 3) {\n    let arr = JSON.parse(input[0]);\n    let root = buildTree(arr);\n    let p = findNode(root, parseInt(input[1]));\n    let q = findNode(root, parseInt(input[2]));\n    let res = lowestCommonAncestor(root, p, q);\n    if (res) console.log(res.val);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {\n    // User logic\n    return root;\n}\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    root->val = atoi(nodes[0]);\n    root->left = root->right = NULL;\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = queue[head++];\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->left->val = atoi(nodes[i]);\n            curr->left->left = curr->left->right = NULL;\n            queue[tail++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->right->val = atoi(nodes[i]);\n            curr->right->left = curr->right->right = NULL;\n            queue[tail++] = curr->right;\n        }\n        i++;\n    }\n    return root;\n}\n\nstruct TreeNode* findNode(struct TreeNode* root, int val) {\n    if (!root) return NULL;\n    if (root->val == val) return root;\n    struct TreeNode* left = findNode(root->left, val);\n    if (left) return left;\n    return findNode(root->right, val);\n}\n\nint main() {\n    char line[10000], pVal[20], qVal[20];\n    if (fgets(line, sizeof(line), stdin) && fgets(pVal, sizeof(pVal), stdin) && fgets(qVal, sizeof(qVal), stdin)) {\n        char* token = strtok(line, \"[], \");\n        char** nodes = (char**)malloc(1000 * sizeof(char*));\n        int size = 0;\n        while (token) {\n            nodes[size++] = strdup(token);\n            token = strtok(NULL, \"[], \");\n        }\n        struct TreeNode* root = buildTree(nodes, size);\n        struct TreeNode* p = findNode(root, atoi(pVal));\n        struct TreeNode* q = findNode(root, atoi(qVal));\n        struct TreeNode* res = lowestCommonAncestor(root, p, q);\n        if (res) printf(\"%d\\n\", res->val);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,5,1,6,2,0,8,null,null,7,4]\\n5\\n1", "expected_output": "3", "is_sample": True},
        {"input": "[3,5,1,6,2,0,8,null,null,7,4]\\n5\\n4", "expected_output": "5", "is_sample": True},
        {"input": "[1,2]\\n1\\n2", "expected_output": "1", "is_sample": True},
        {"input": "[1,2,3,4,5,6,7]\\n4\\n5", "expected_output": "2", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]\\n4\\n7", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3,null,null,4,5,null,null,6,null,null,7]\\n6\\n7", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]\\n10\\n11", "expected_output": "5", "is_sample": False},
        # Stress Tests (100,000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: 100,000 nodes, Line
    # Deep line, p and q at the end
    test_cases[7] = {"input": json.dumps(list(range(100000))) + "\\n99998\\n99999", "expected_output": "99998", "is_sample": False}
    # Stress 9: 100,000 nodes, star (root connected to 99,999 nodes) -- balanced enough
    # we'll use a larger balanced tree
    test_cases[8] = {"input": json.dumps(list(range(50000))) + "\\n25000\\n49999", "expected_output": "0", "is_sample": False}
    # Stress 10: 100,000 nodes, split at root
    # root=0, left branch has 50k, right branch has 50k
    test_cases[9] = {"input": json.dumps([0, 1, 2] + [i if i%2 else None for i in range(3, 100000)]) + "\\n9999\\n99998", "expected_output": "0", "is_sample": False}

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

    output_path = "201-400/236_Lowest_Common_Ancestor_of_a_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
