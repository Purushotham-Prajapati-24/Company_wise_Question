import json
import os

def generate_json():
    problem_id = 450
    title = "Delete Node in a BST"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>450. Delete Node in a BST</h3>
<p>Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.</p>

<p>Basically, the deletion can be divided into two stages:</p>
<ol>
	<li>Search for a node to remove.</li>
	<li>If the node is found, delete the node.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 3
<strong>Output:</strong> [5,4,6,2,null,null,7]
<strong>Explanation:</strong> Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 0
<strong>Output:</strong> [5,3,6,2,4,null,7]
<strong>Explanation:</strong> The tree does not contain a node with value = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [], key = 0
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>Each node has a <strong>unique</strong> value.</li>
	<li><code>root</code> is a valid binary search tree.</li>
	<li><code>-10<sup>5</sup> &lt;= key &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it with time complexity <code>O(height of tree)</code>?</p>"""

    input_format = "Two lines: the first line is a JSON array representing the BST, and the second line is an integer `key`."
    output_format = "A JSON array representing the level-order traversal of the updated BST."
    
    constraints = [
        "0 <= number of nodes <= 10^4",
        "-10^5 <= Node.val <= 10^5",
        "Each node has a unique value.",
        "root is a valid BST.",
        "-10^5 <= key <= 10^5"
    ]
    
    explanation = "To delete a node in a BST: 1. If key < root.val, recurse left. 2. If key > root.val, recurse right. 3. If key == root.val: a) If leaf or 1 child, return the other child. b) If 2 children, find the inorder successor (min in right subtree), replace current node's value with successor's value, and delete the successor from the right subtree."
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            temp = root.right
            while temp.left: temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data: return None\n    root = TreeNode(data[0])\n    q = deque([root])\n    i = 1\n    while q and i < len(data):\n        node = q.popleft()\n        if i < len(data) and data[i] is not None:\n            node.left = TreeNode(data[i])\n            q.append(node.left)\n        i += 1\n        if i < len(data) and data[i] is not None:\n            node.right = TreeNode(data[i])\n            q.append(node.right)\n        i += 1\n    return root\n\ndef serialize_tree(root):\n    if not root: return []\n    res, q = [], deque([root])\n    while q:\n        node = q.popleft()\n        if node:\n            res.append(node.val)\n            q.append(node.left)\n            q.append(node.right)\n        else: res.append(None)\n    while res and res[-1] is None: res.pop()\n    return res\n\nclass Solution:\n    def deleteNode(self, root, key):\n        # User logic here\n        return root\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        root = build_tree(json.loads(input_data[0]))\n        key = int(input_data[1])\n        sol = Solution()\n        print(json.dumps(serialize_tree(sol.deleteNode(root, key))).replace(\" \", \"\"))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    TreeNode* deleteNode(TreeNode* root, int key) {\n        // User logic here\n        return root;\n    }\n};\n\nTreeNode* buildTree(string s) {\n    if (s == \"[]\" || s == \"\") return NULL;\n    s = s.substr(1, s.length() - 2);\n    stringstream ss(s);\n    string item;\n    vector<string> data;\n    while (getline(ss, item, ',')) {\n        size_t first = item.find_first_not_of(\" \");\n        size_t last = item.find_last_not_of(\" \");\n        data.push_back(item.substr(first, last - first + 1));\n    }\n    TreeNode* root = new TreeNode(stoi(data[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < data.size()) {\n        TreeNode* node = q.front(); q.pop();\n        if (data[i] != \"null\") {\n            node->left = new TreeNode(stoi(data[i]));\n            q.push(node->left);\n        }\n        i++;\n        if (i < data.size() && data[i] != \"null\") {\n            node->right = new TreeNode(stoi(data[i]));\n            q.push(node->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid printTree(TreeNode* root) {\n    if (!root) { cout << \"[]\" << endl; return; }\n    vector<string> res;\n    queue<TreeNode*> q;\n    q.push(root);\n    while (!q.empty()) {\n        TreeNode* node = q.front(); q.pop();\n        if (node) {\n            res.push_back(to_string(node->val));\n            q.push(node->left);\n            q.push(node->right);\n        } else res.push_back(\"null\");\n    }\n    while (res.back() == \"null\") res.pop_back();\n    cout << \"[\";\n    for (int i = 0; i < res.size(); i++) cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n    cout << \"]\" << endl;\n}\n\nint main() {\n    string s, k;\n    if (getline(cin, s) && getline(cin, k)) {\n        Solution sol;\n        printTree(sol.deleteNode(buildTree(s), stoi(k)));\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public TreeNode deleteNode(TreeNode root, int key) {\n        // User logic here\n        return root;\n    }\n}\n\npublic class Main {\n    static TreeNode buildTree(String s) {\n        if (s.equals(\"[]\") || s.isEmpty()) return null;\n        String[] data = s.substring(1, s.length() - 1).split(\",\");\n        for (int i = 0; i < data.length; i++) data[i] = data[i].trim();\n        TreeNode root = new TreeNode(Integer.parseInt(data[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < data.length) {\n            TreeNode node = q.poll();\n            if (!data[i].equals(\"null\")) {\n                node.left = new TreeNode(Integer.parseInt(data[i]));\n                q.add(node.left);\n            }\n            i++;\n            if (i < data.length && !data[i].equals(\"null\")) {\n                node.right = new TreeNode(Integer.parseInt(data[i]));\n                q.add(node.right);\n            }\n            i++;\n        }\n        return root;\n    }\n    static void printTree(TreeNode root) {\n        if (root == null) { System.out.println(\"[]\"); return; }\n        List<String> res = new ArrayList<>();\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        while (!q.isEmpty()) {\n            TreeNode node = q.poll();\n            if (node != null) {\n                res.add(String.valueOf(node.val));\n                q.add(node.left);\n                q.add(node.right);\n            } else res.add(\"null\");\n        }\n        while (res.get(res.size() - 1).equals(\"null\")) res.remove(res.size() - 1);\n        System.out.println(\"[\" + String.join(\",\", res) + \"]\");\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine();\n            int k = sc.hasNextInt() ? sc.nextInt() : 0;\n            printTree(new Solution().deleteNode(buildTree(s), k));\n        }\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nvar deleteNode = function(root, key) {\n    // User logic here\n};\n\nconst fs = require('fs');\nfunction buildTree(data) {\n    if (!data.length) return null;\n    let root = new TreeNode(data[0]), q = [root], i = 1;\n    while (q.length && i < data.length) {\n        let node = q.shift();\n        if (data[i] !== null) { node.left = new TreeNode(data[i]); q.push(node.left); }\n        i++;\n        if (i < data.length && data[i] !== null) { node.right = new TreeNode(data[i]); q.push(node.right); }\n        i++;\n    }\n    return root;\n}\nfunction serialize(root) {\n    if (!root) return [];\n    let res = [], q = [root];\n    while (q.length) {\n        let node = q.shift();\n        if (node) { res.push(node.val); q.push(node.left); q.push(node.right); } else res.push(null);\n    }\n    while (res[res.length - 1] === null) res.pop();\n    return res;\n}\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const root = buildTree(JSON.parse(input[0]));\n    const key = parseInt(input[1]);\n    console.log(JSON.stringify(serialize(deleteNode(root, key))).replace(/\\s/g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* deleteNode(struct TreeNode* root, int key) {\n    // User logic here\n    return root;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[5,3,6,2,4,null,7]\\n3", "expected_output": "[5,4,6,2,null,null,7]", "is_sample": True},
        {"input": "[5,3,6,2,4,null,7]\\n0", "expected_output": "[5,3,6,2,4,null,7]", "is_sample": True},
        {"input": "[]\\n0", "expected_output": "[]", "is_sample": False},
        {"input": "[1,null,2]\\n1", "expected_output": "[2]", "is_sample": False},
        {"input": "[2,1]\\n2", "expected_output": "[1]", "is_sample": False},
        {"input": "[  5, 3, 6  ]\\n3", "expected_output": "[5,null,6]", "is_sample": False}, # Spaces
        {"input": "[8,0,31,null,6,28,45,1,7,25,30,32,49]\\n31", "expected_output": "[8,0,32,null,6,28,45,1,7,25,30,null,49]", "is_sample": False},
        {"input": "[10,5,15]\\n10", "expected_output": "[15,5]", "is_sample": False},
        # Stress
        {"input": json.dumps(list(range(500, 0, -1))) + "\\n250", "expected_output": "[]", "is_sample": False}, # We'll just check if it runs. Correct output depends on successor logic.
        {"input": "[5,3,6,2,4,null,7]\\n7", "expected_output": "[5,3,6,2,4]", "is_sample": False}
    ]
    # Redo the stress test output correctly for the first stress case.
    # For a purely left-skewed tree [500, 499, ..., 1], deleting 250 would result in 249 moving up.
    # Actually, a simple deletion from a linked list style BST is easy to predict.
    # But let's use a smaller stress case for predictable output.
    test_cases[8] = {"input": "[10,9,null,8,null,7,null,6,null,5,null,4,null,3,null,2,null,1]\\n5", "expected_output": "[10,9,null,8,null,7,null,6,null,4,null,3,null,2,null,1]", "is_sample": False}

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
        "topics": ["Tree", "Binary Search Tree", "Binary Tree"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Delete_Node_in_a_BST.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
