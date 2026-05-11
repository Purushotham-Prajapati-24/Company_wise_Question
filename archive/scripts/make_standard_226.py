import json
import os

def generate_json():
    problem_id = 226
    title = "Invert Binary Tree"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>226. Invert Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, invert the tree, and return <em>its root</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg" style="width: 500px; height: 165px;" />
<pre><strong>Input:</strong> root = [4,2,7,1,3,6,9]
<strong>Output:</strong> [4,7,2,9,6,3,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg" style="width: 500px; height: 120px;" />
<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [2,3,1]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A stringified array representing level-order traversal of a binary tree."
    output_format = "A stringified array representing level-order traversal of the inverted binary tree."
    
    constraints = [
        "Number of nodes in range [0, 100]",
        "-100 <= Node.val <= 100"
    ]
    
    explanation = """To invert a binary tree:
1. **Recursive Swap**: For any given node:
   - Base Case: If the node is `null`, return `null`.
   - Swap the left and right children.
   - Recursively call the function for both original left and right children.
2. **Iterative BFS/Stack**: Alternatively, traverse the tree (BFS/DFS) and swap children at each node.
3. **Complexity**:
   - Time: O(N) where N is the number of nodes.
   - Space: O(H) for recursion stack or O(W) for BFS queue."""
    
    answer = """class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        # Swap children
        root.left, root.right = root.right, root.left
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(arr):\n    if not arr: return None\n    root = TreeNode(arr[0])\n    q = deque([root])\n    i = 1\n    while q and i < len(arr):\n        curr = q.popleft()\n        if i < len(arr) and arr[i] is not None:\n            curr.left = TreeNode(arr[i])\n            q.append(curr.left)\n        i += 1\n        if i < len(arr) and arr[i] is not None:\n            curr.right = TreeNode(arr[i])\n            q.append(curr.right)\n        i += 1\n    return root\n\ndef serialize_tree(root):\n    if not root: return []\n    res, q = [], deque([root])\n    while q:\n        node = q.popleft()\n        if node:\n            res.append(node.val)\n            q.append(node.left)\n            q.append(node.right)\n        else: res.append(None)\n    while res and res[-1] is None: res.pop()\n    return res\n\ndef invertTree(root):\n    # User logic here\n    return root\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        try:\n            arr = json.loads(line)\n        except:\n            arr = [int(x) if x != 'null' else None for x in line.replace('[', '').replace(']', '').replace(',', ' ').split()]\n        root = build_tree(arr)\n        inverted = invertTree(root)\n        print(json.dumps(serialize_tree(inverted)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid serializeTree(TreeNode* root) {\n    if (!root) {\n        cout << \"[]\" << endl;\n        return;\n    }\n    vector<string> res;\n    queue<TreeNode*> q;\n    q.push(root);\n    while (!q.empty()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (curr) {\n            res.push_back(to_string(curr->val));\n            q.push(curr->left);\n            q.push(curr->right);\n        } else {\n            res.push_back(\"null\");\n        }\n    }\n    while (!res.empty() && res.back() == \"null\") res.pop_back();\n    cout << \"[\";\n    for (int i = 0; i < res.size(); i++) {\n        cout << res[i] << (i == res.size() - 1 ? \"\" : \", \");\n    }\n    cout << \"]\" << endl;\n}\n\nTreeNode* invertTree(TreeNode* root) {\n    // User logic\n    return root;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        string val;\n        vector<string> nodes;\n        while (ss >> val) nodes.push_back(val);\n        TreeNode* root = buildTree(nodes);\n        serializeTree(invertTree(root));\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public TreeNode invertTree(TreeNode root) {\n        // User logic\n        return root;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            line = line.replace(\"[\", \"\").replace(\"]\", \"\").replace(\",\", \" \");\n            String[] parts = line.trim().split(\"\\\\s+\");\n            TreeNode root = buildTree(parts);\n            TreeNode inverted = new Solution().invertTree(root);\n            printTree(inverted);\n        }\n    }\n\n    static TreeNode buildTree(String[] chars) {\n        if (chars.length == 0 || chars[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(chars[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < chars.length) {\n            TreeNode curr = q.poll();\n            if (i < chars.length && !chars[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(chars[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < chars.length && !chars[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(chars[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    static void printTree(TreeNode root) {\n        if (root == null) {\n            System.out.println(\"[]\");\n            return;\n        }\n        List<String> res = new ArrayList<>();\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        while (!q.isEmpty()) {\n            TreeNode curr = q.poll();\n            if (curr != null) {\n                res.add(String.valueOf(curr.val));\n                q.add(curr.left);\n                q.add(curr.right);\n            } else {\n                res.add(\"null\");\n            }\n        }\n        while (!res.isEmpty() && res.get(res.size() - 1).equals(\"null\")) res.remove(res.size() - 1);\n        System.out.println(\"[\" + String.join(\", \", res) + \"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction buildTree(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]);\n    let q = [root];\n    let i = 1;\n    while (q.length && i < arr.length) {\n        let curr = q.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            q.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction serializeTree(root) {\n    if (!root) return [];\n    let res = [];\n    let q = [root];\n    while (q.length) {\n        let curr = q.shift();\n        if (curr) {\n            res.push(curr.val);\n            q.push(curr.left);\n            q.push(curr.right);\n        } else {\n            res.push(null);\n        }\n    }\n    while (res.length && res[res.length - 1] === null) res.pop();\n    return res;\n}\n\nfunction invertTree(root) {\n    // User logic here\n    return root;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    let arr = JSON.parse(input);\n    let root = buildTree(arr);\n    console.log(JSON.stringify(serializeTree(invertTree(root))));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* invertTree(struct TreeNode* root) {\n    // User logic\n    return root;\n}\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    root->val = atoi(nodes[0]);\n    root->left = root->right = NULL;\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = queue[head++];\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->left->val = atoi(nodes[i]);\n            curr->left->left = curr->left->right = NULL;\n            queue[tail++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->right->val = atoi(nodes[i]);\n            curr->right->left = curr->right->right = NULL;\n            queue[tail++] = curr->right;\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid serializeTree(struct TreeNode* root) {\n    if (!root) { printf(\"[]\\n\"); return; }\n    struct TreeNode** queue = (struct TreeNode**)malloc(1000 * sizeof(struct TreeNode*));\n    char** res = (char**)malloc(1000 * sizeof(char*));\n    int head = 0, tail = 0, rSize = 0;\n    queue[tail++] = root;\n    while (head < tail) {\n        struct TreeNode* curr = queue[head++];\n        if (curr) {\n            char buf[12]; sprintf(buf, \"%d\", curr->val);\n            res[rSize++] = strdup(buf);\n            queue[tail++] = curr->left;\n            queue[tail++] = curr->right;\n        } else {\n            res[rSize++] = strdup(\"null\");\n        }\n    }\n    while (rSize > 0 && strcmp(res[rSize-1], \"null\") == 0) rSize--;\n    printf(\"[\");\n    for (int i = 0; i < rSize; i++) {\n        printf(\"%s%s\", res[i], (i == rSize - 1 ? \"\" : \", \"));\n    }\n    printf(\"]\\n\");\n}\n\nint main() {\n    char line[10000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \"[], \");\n        char** nodes = (char**)malloc(1000 * sizeof(char*));\n        int size = 0;\n        while (token) {\n            nodes[size++] = strdup(token);\n            token = strtok(NULL, \"[], \");\n        }\n        struct TreeNode* root = buildTree(nodes, size);\n        serializeTree(invertTree(root));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[4,2,7,1,3,6,9]", "expected_output": "[4, 7, 2, 9, 6, 3, 1]", "is_sample": True},
        {"input": "[2,1,3]", "expected_output": "[2, 3, 1]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,2]", "expected_output": "[1, null, 2]", "is_sample": False},
        {"input": "[1,null,2]", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "[1,2,3,4,null,null,5]", "expected_output": "[1, 3, 2, 5, null, null, 4]", "is_sample": False},
        # Stress Tests (Max 100 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _invert_solve(arr):
        if not arr: return []
        def build_q(a):
            if not a: return None
            r = {"v": a[0], "l": None, "r": None}
            q = [r]
            idx = 1
            for current in q:
                if idx < len(a):
                    if a[idx] is not None:
                        current["l"] = {"v": a[idx], "l": None, "r": None}
                        q.append(current["l"])
                    idx += 1
                if idx < len(a):
                    if a[idx] is not None:
                        current["r"] = {"v": a[idx], "l": None, "r": None}
                        q.append(current["r"])
                    idx += 1
            return r
        root = build_q(arr)
        def inv(n):
            if not n: return
            n["l"], n["r"] = n["r"], n["l"]
            inv(n["l"]); inv(n["r"])
        inv(root)
        def ser(r):
            if not r: return []
            res, q = [], [r]
            for n in q:
                if n:
                    res.append(n["v"])
                    q.append(n.get("l"))
                    q.append(n.get("r"))
                else: res.append(None)
            while res and res[-1] is None: res.pop()
            return res
        return ser(root)

    # Stress 8: Full perfect tree of 3 levels
    b8 = [1,2,3,4,5,6,7]
    test_cases[7] = {"input": json.dumps(b8), "expected_output": json.dumps(_invert_solve(b8)), "is_sample": False}
    # Stress 9: Max limit 100 nodes (complete)
    b9 = list(range(1, 101))
    test_cases[8] = {"input": json.dumps(b9), "expected_output": json.dumps(_invert_solve(b9)), "is_sample": False}
    # Stress 10: Deep skewed
    b10 = [i if i % 2 == 1 else None for i in range(1, 11)] # something with nulls?
    b10 = [1, 2, None, 3, None, None, None, 4] # mostly left
    test_cases[9] = {"input": json.dumps(b10), "expected_output": json.dumps(_invert_solve(b10)), "is_sample": False}

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
        "companyIndex": 0
    }

    output_path = "201-400/226_Invert_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
