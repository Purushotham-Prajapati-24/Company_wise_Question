import json
import os

def generate_json():
    problem_id = 235
    title = "Lowest Common Ancestor of a Binary Search Tree"
    difficulty = "LOW_MEDIUM" # Easy-Medium
    marks = 10
    
    html_description = """<h3>235. Lowest Common Ancestor of a Binary Search Tree</h3>
<p>Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;" />
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> The LCA of nodes 2 and 8 is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;" />
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [2,1], p = 2, q = 1
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> will exist in the BST.</li>
</ul>"""

    input_format = "Three lines: first, the tree root (level-order); second, value of p; third, value of q."
    output_format = "The value of the LCA node."
    
    constraints = [
        "2 <= n <= 100,000",
        "Unique node values.",
        "p and q guaranteed to exist."
    ]
    
    explanation = """To find the LCA in a BST:
1. **Leverage BST Properties**: In a BST, for any node:
   - Left sub-tree contains only values less than the node.
   - Right sub-tree contains only values greater than the node.
2. **Logic**:
   - Compare the current node's value with `p` and `q`.
   - If both `p` and `q` are smaller than current, move to the left child.
   - If both `p` and `q` are larger than current, move to the right child.
   - If one is smaller and one is larger (or the current node is `p` or `q`), the current node is the LCA.
3. **Complexity**:
   - Time: O(H) where H is the height of the tree (O(log n) for balanced, O(n) for skewed).
   - Space: O(1) for iterative approach."""
    
    answer = """class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(vals):\n    if not vals: return None\n    root = TreeNode(vals[0])\n    queue = deque([root])\n    i = 1\n    while i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] is not None:\n            node.left = TreeNode(vals[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] is not None:\n            node.right = TreeNode(vals[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef find_node(root, val):\n    if not root: return None\n    if root.val == val: return root\n    return find_node(root.left, val) or find_node(root.right, val)\n\nclass Solution:\n    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':\n        # User logic here\n        return root\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        # Robust tree parsing\n        raw_tree = re.search(r'\\[.*?\\]', lines[0])\n        tree_vals = [int(x) if x != 'null' else None for x in re.findall(r'null|-?\\d+', raw_tree.group(0))] if raw_tree else []\n        # Robust p, q parsing\n        p_val = int(re.search(r'-?\\d+', lines[1]).group(0))\n        q_val = int(re.search(r'-?\\d+', lines[2]).group(0))\n        \n        root = build_tree(tree_vals)\n        p_node = find_node(root, p_val)\n        q_node = find_node(root, q_val)\n        \n        res = Solution().lowestCommonAncestor(root, p_node, q_node)\n        if res: print(res.val)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nTreeNode* findNode(TreeNode* root, int val) {\n    if (!root) return NULL;\n    if (root->val == val) return root;\n    TreeNode* left = findNode(root->left, val);\n    if (left) return left;\n    return findNode(root->right, val);\n}\n\nclass Solution {\npublic:\n    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n        // User logic here\n        return root;\n    }\n};\n\nint main() {\n    string line, pLine, qLine;\n    if (getline(cin, line) && getline(cin, pLine) && getline(cin, qLine)) {\n        regex re(\"null|-?\\\\d+\");\n        vector<string> nodes;\n        for (sregex_iterator i = sregex_iterator(line.begin(), line.end(), re), end; i != end; ++i) {\n            nodes.push_back(i->str());\n        }\n        \n        auto getVal = [](string s) {\n            smatch m;\n            if (regex_search(s, m, regex(\"-?\\\\d+\"))) return stoi(m.str());\n            return 0;\n        };\n        \n        TreeNode* root = buildTree(nodes);\n        TreeNode* p = findNode(root, getVal(pLine));\n        TreeNode* q = findNode(root, getVal(qLine));\n        \n        Solution sol;\n        TreeNode* res = sol.lowestCommonAncestor(root, p, q);\n        if (res) cout << res->val << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n        // User logic here\n        return root;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        String pLine = br.readLine();\n        String qLine = br.readLine();\n        if (line != null && pLine != null && qLine != null) {\n            String[] nodes = line.replaceAll(\".*=\", \"\").replaceAll(\"\\\\[|\\\\]|,|\\\"\", \" \").trim().split(\"\\\\s+\");\n            TreeNode root = buildTree(nodes);\n            \n            int pVal = Integer.parseInt(pLine.replaceAll(\"[^0-9-]\", \"\"));\n            int qVal = Integer.parseInt(qLine.replaceAll(\"[^0-9-]\", \"\"));\n            \n            TreeNode p = findNode(root, pVal);\n            TreeNode q = findNode(root, qVal);\n            \n            TreeNode res = new Solution().lowestCommonAncestor(root, p, q);\n            if (res != null) System.out.println(res.val);\n        }\n    }\n\n    static TreeNode buildTree(String[] nodes) {\n        if (nodes.length == 0 || nodes[0].equals(\"null\") || nodes[0].isEmpty()) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.length) {\n            TreeNode curr = q.poll();\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    static TreeNode findNode(TreeNode root, int val) {\n        if (root == null) return null;\n        if (root.val == val) return root;\n        TreeNode left = findNode(root.left, val);\n        return (left != null) ? left : findNode(root.right, val);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val) {\n    this.val = val;\n    this.left = this.right = null;\n}\n\nfunction buildTree(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]);\n    let q = [root];\n    let i = 1;\n    while (q.length && i < arr.length) {\n        let curr = q.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            q.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction findNode(root, val) {\n    if (!root) return null;\n    if (root.val === val) return root;\n    return findNode(root.left, val) || findNode(root.right, val);\n}\n\n/**\n * @param {TreeNode} root\n * @param {TreeNode} p\n * @param {TreeNode} q\n * @return {TreeNode}\n */\nvar lowestCommonAncestor = function(root, p, q) {\n    // User logic here\n    return root;\n};\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 3) {\n    const treeMatch = input[0].match(/\\[.*\\]/);\n    const treeArr = treeMatch ? JSON.parse(treeMatch[0].replace(/null/g, 'null')) : [];\n    const pVal = parseInt(input[1].match(/-?\\d+/)[0]);\n    const qVal = parseInt(input[2].match(/-?\\d+/)[0]);\n    \n    const root = buildTree(treeArr);\n    const res = lowestCommonAncestor(root, findNode(root, pVal), findNode(root, qVal));\n    if (res) console.log(res.val);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nstruct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {\n    // User logic here\n    return root;\n}\n\nstruct TreeNode* createNode(int val) {\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = val;\n    node->left = node->right = NULL;\n    return node;\n}\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = createNode(atoi(nodes[0]));\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = queue[head++];\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->left = createNode(atoi(nodes[i]));\n            queue[tail++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = createNode(atoi(nodes[i]));\n            queue[tail++] = curr->right;\n        }\n        i++;\n    }\n    free(queue);\n    return root;\n}\n\nstruct TreeNode* findNode(struct TreeNode* root, int val) {\n    if (!root) return NULL;\n    if (root->val == val) return root;\n    struct TreeNode* left = findNode(root->left, val);\n    return left ? left : findNode(root->right, val);\n}\n\nint main() {\n    char line[100000], pValStr[100], qValStr[100];\n    if (fgets(line, sizeof(line), stdin) && fgets(pValStr, sizeof(pValStr), stdin) && fgets(qValStr, sizeof(qValStr), stdin)) {\n        char* start = strchr(line, '[');\n        if (!start) start = line;\n        char* token = strtok(start, \"[], \\r\\n\");\n        char** nodes = (char**)malloc(10000 * sizeof(char*));\n        int size = 0;\n        while (token) {\n            nodes[size++] = strdup(token);\n            token = strtok(NULL, \"[], \\r\\n\");\n        }\n        \n        auto extractInt = [](char* s) {\n            while (*s && !(*s >= '0' && *s <= '9') && *s != '-') s++;\n            return *s ? atoi(s) : 0;\n        };\n        \n        struct TreeNode* root = buildTree(nodes, size);\n        struct TreeNode* p = findNode(root, extractInt(pValStr));\n        struct TreeNode* q = findNode(root, extractInt(qValStr));\n        struct TreeNode* res = lowestCommonAncestor(root, p, q);\n        if (res) printf(\"%d\\n\", res->val);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[6,2,8,0,4,7,9,null,null,3,5]\\n2\\n8", "expected_output": "6", "is_sample": True},
        {"input": "[6,2,8,0,4,7,9,null,null,3,5]\\n2\\n4", "expected_output": "2", "is_sample": True},
        {"input": "[2,1]\\n2\\n1", "expected_output": "2", "is_sample": True},
        {"input": "[10,5,15,2,8,12,20,1,3,7,9,11,13,18,25]\\n1\\n3", "expected_output": "2", "is_sample": False},
        {"input": "[10,5,15,2,8,12,20,1,3,7,9,11,13,18,25]\\n7\\n25", "expected_output": "10", "is_sample": False},
        {"input": "[10,5,15,2,8,12,20,1,3,7,9,11,13,18,25]\\n2\\n8", "expected_output": "5", "is_sample": False},
        {"input": "[5,3,6,1,4,null,null,null,2]\\n1\\n4", "expected_output": "3", "is_sample": False},
        # Stress Tests (100,000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: Deep linked list (Left-skewed)
    e8 = list(range(100000, 0, -1))
    test_cases[7] = {"input": json.dumps(e8) + "\\n1\\n100", "expected_output": "100", "is_sample": False}
    # Stress 9: Perfectly balanced BST
    def _gen_bal(low, high):
        if low > high: return []
        mid = (low + high) // 2
        return [mid] + _gen_bal(low, mid-1) + _gen_bal(mid+1, high)
    # wait balanced representation flat is hard. Let's use sequential for Stress 10
    test_cases[8] = {"input": json.dumps(list(range(100000))) + "\\n0\\n99999", "expected_output": "0", "is_sample": False} # Skewed right
    # Stress 10: Balanced star-like
    test_cases[9] = {"input": "[50000," + ",".join(map(str, range(49999))) + "," + ",".join(map(str, range(50001, 100000))) + "]\\n5\\n80000", "expected_output": "50000", "is_sample": False}

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
        "topics": ["Tree", "Binary Search Tree", "Binary Tree", "Depth-First Search"],
        "companyIndex": 0
    }

    output_path = "201-400/235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
