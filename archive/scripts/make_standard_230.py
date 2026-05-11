import json
import os

def generate_json():
    problem_id = 230
    title = "Kth Smallest Element in a BST"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>230. Kth Smallest Element in a BST</h3>
<p>Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest value (<strong>1-indexed</strong>) of all the values of the nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;" />
<pre><strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;" />
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

    input_format = "Two lines: first, an array representing the binary tree (level-order); second, an integer k."
    output_format = "An integer representing the kth smallest value."
    
    constraints = [
        "1 <= k <= n <= 10,000",
        "0 <= Node.val <= 10,000",
        "BST properties always hold."
    ]
    
    explanation = """To find the k-th smallest element in a BST:
1. **In-order Traversal**: A Binary Search Tree's in-order traversal (Left -> Data -> Right) yields sorted elements in ascending order.
2. **Logic**:
   - Perform an in-order traversal using recursion or a stack.
   - Keep track of the number of nodes visited.
   - When the count reaches `k`, return the current node's value.
3. **Complexity**:
   - Time: O(H + k) where H is the height of the tree.
   - Space: O(H) for the call stack or manual stack."""
    
    answer = """class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(vals):\n    if not vals: return None\n    root = TreeNode(vals[0])\n    queue = deque([root])\n    i = 1\n    while i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] is not None:\n            node.left = TreeNode(vals[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] is not None:\n            node.right = TreeNode(vals[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef kthSmallest(root, k):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        try:\n            arr = json.loads(lines[0])\n        except:\n            arr = [int(x) if x != 'null' else None for x in lines[0].replace('[', '').replace(']', '').replace(',', ' ').split()]\n        k = int(lines[1])\n        print(kthSmallest(build_tree(arr), k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nint kthSmallest(TreeNode* root, int k) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line, kLine;\n    if (getline(cin, line) && getline(cin, kLine)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        string val;\n        vector<string> nodes;\n        while (ss >> val) nodes.push_back(val);\n        int k = stoi(kLine);\n        cout << kthSmallest(buildTree(nodes), k) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public int kthSmallest(TreeNode root, int k) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        String kLine = br.readLine();\n        if (line != null && kLine != null) {\n            line = line.replace(\"[\", \"\").replace(\"]\", \"\").replace(\",\", \" \");\n            String[] parts = line.trim().split(\"\\\\s+\");\n            int k = Integer.parseInt(kLine.trim());\n            TreeNode root = buildTree(parts);\n            System.out.println(new Solution().kthSmallest(root, k));\n        }\n    }\n\n    static TreeNode buildTree(String[] nodes) {\n        if (nodes.length == 0 || nodes[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.length) {\n            TreeNode curr = q.poll();\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction buildTree(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]);\n    let q = [root];\n    let i = 1;\n    while (q.length && i < arr.length) {\n        let curr = q.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            q.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction kthSmallest(root, k) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    let arr = JSON.parse(input[0]);\n    let k = parseInt(input[1]);\n    console.log(kthSmallest(buildTree(arr), k));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nint kthSmallest(struct TreeNode* root, int k) {\n    // User logic\n    return 0;\n}\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    root->val = atoi(nodes[0]);\n    root->left = root->right = NULL;\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = queue[head++];\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->left->val = atoi(nodes[i]);\n            curr->left->left = curr->left->right = NULL;\n            queue[tail++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->right->val = atoi(nodes[i]);\n            curr->right->left = curr->right->right = NULL;\n            queue[tail++] = curr->right;\n        }\n        i++;\n    }\n    return root;\n}\n\nint main() {\n    char line[10000], kLine[10];\n    if (fgets(line, sizeof(line), stdin) && fgets(kLine, sizeof(kLine), stdin)) {\n        char* token = strtok(line, \"[], \");\n        char** nodes = (char**)malloc(1000 * sizeof(char*));\n        int size = 0;\n        while (token) {\n            nodes[size++] = strdup(token);\n            token = strtok(NULL, \"[], \");\n        }\n        int k = atoi(kLine);\n        printf(\"%d\\n\", kthSmallest(buildTree(nodes, size), k));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,1,4,null,2]\\n1", "expected_output": "1", "is_sample": True},
        {"input": "[5,3,6,2,4,null,null,1]\\n3", "expected_output": "3", "is_sample": True},
        {"input": "[1]\\n1", "expected_output": "1", "is_sample": False},
        {"input": "[2,1,null]\\n2", "expected_output": "2", "is_sample": False},
        {"input": "[2,1,3]\\n2", "expected_output": "2", "is_sample": False},
        {"input": "[10,5,15,2,7,12,20,1,3,6,8,11,13,18,22]\\n7", "expected_output": "8", "is_sample": False},
        {"input": "[10,5,15,2,7,12,20,1,3,6,8,11,13,18,22]\\n1", "expected_output": "1", "is_sample": False},
        # Stress Tests (10,000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_ks(root_list, k):
        # build flat
        import collections
        v = sorted([x for x in root_list if x is not None])
        return v[k-1]

    # Stress 8: 10,000 linked list style (all left)
    n8 = []
    for i in range(10000, 0, -1): n8.extend([i, None])
    # simplified representation: 10000 nodes, each parent i has left i-1
    # expected 5000th smallest is 5000
    test_cases[7] = {"input": json.dumps(list(range(10000, 0, -1))).replace(", ", ",") + "\\n5000", "expected_output": "5000", "is_sample": False}
    # Stress 9: 10,000 nodes, balanced BST
    n9 = list(range(10000))
    test_cases[8] = {"input": json.dumps(n9) + "\\n9999", "expected_output": "9998", "is_sample": False}
    # Stress 10: Skewed right
    test_cases[9] = {"input": json.dumps(list(range(10000))) + "\\n10000", "expected_output": "9999", "is_sample": False}

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
        "topics": ["Tree", "Depth-First Search", "Binary Search Tree", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "201-400/230_Kth_Smallest_Element_in_a_BST.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
