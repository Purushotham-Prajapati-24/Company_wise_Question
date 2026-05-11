import json
import os

def generate_json():
    problem_id = 114
    title = "Flatten Binary Tree to Linked List"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>114. Flatten Binary Tree to Linked List</h3>
<p>Given the <code>root</code> of a binary tree, flatten the tree into a "linked list":</p>

<ul>
	<li>The "linked list" should use the same <code>TreeNode</code> class where the <code>right</code> child pointer points to the next node in the list and the <code>left</code> child pointer is always <code>null</code>.</li>
	<li>The "linked list" should be in the same order as a <a href="http://en.wikipedia.org/wiki/Tree_traversal#Pre-order" target="_blank"><strong>pre-order</strong><strong> traversal</strong></a> of the binary tree.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;" />
<pre>
<strong>Input:</strong> root = [1,2,5,3,4,null,6]
<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you flatten the tree in-place (with <code>O(1)</code> extra space)? """

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree (integers or 'null')."
    output_format = "A single line containing space-separated values representing the level-order traversal of the flattened tree (linked list structure)."
    
    constraints = [
        "0 <= number of nodes <= 2000",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To flatten a binary tree into a linked list in-place:
1. **Iterative In-place Approach (O(1) space)**:
   - For each node `curr` starting from the root:
     - If `curr.left` exists:
       - Find the **rightmost** node in the left subtree. This node is the inorder predecessor of `curr.right` in a preorder traversal.
       - Connect the rightmost node's `right` pointer to `curr.right`.
       - Move the entire left subtree to the right: `curr.right = curr.left`.
       - Set `curr.left = null`.
     - Move to the next node on the right: `curr = curr.right`.
2. **Why this works**:
   - In a preorder traversal (Root -> Left -> Right), the entire left subtree comes before the right subtree.
   - By attaching the right subtree to the end of the left subtree, we maintain the correct preorder sequence while linearizing the tree.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited at most twice.
   - Space Complexity: O(1) as we reuse existing pointers and don't use a recursion stack or extra data structures."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    curr = root
    while curr:
        if curr.left:
            # Find the rightmost node in the left subtree
            predecessor = curr.left
            while predecessor.right:
                predecessor = predecessor.right
            
            # Connect the original right subtree to the predecessor
            predecessor.right = curr.right
            
            # Move left subtree to the right
            curr.right = curr.left
            curr.left = None
            
        # Move to the next node
        curr = curr.right"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data or data[0] == 'null': return None\n    root = TreeNode(int(data[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(data):\n        node = queue.popleft()\n        if i < len(data) and data[i] != 'null':\n            node.left = TreeNode(int(data[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] != 'null':\n            node.right = TreeNode(int(data[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef serialize(root):\n    if not root: return \"\"\n    res = []\n    queue = deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            res.append(str(node.val))\n            queue.append(node.left)\n            queue.append(node.right)\n        else:\n            res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \" \".join(res)\n\ndef flatten(root):\n    # User logic here\n    pass\n\nif __name__ == \"__main__\":\n    line = sys.stdin.read().strip()\n    if line:\n        data = re.findall(r'null|-?\\d+', line)\n        root = build_tree(data)\n        flatten(root)\n        print(serialize(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& data) {\n    if (data.empty() || data[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(data[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < data.size()) {\n        TreeNode* curr = q.front();\n        q.pop();\n        if (i < data.size() && data[i] != \"null\") {\n            curr->left = new TreeNode(stoi(data[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < data.size() && data[i] != \"null\") {\n            curr->right = new TreeNode(stoi(data[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid serialize(TreeNode* root) {\n    if (!root) return;\n    vector<string> res;\n    queue<TreeNode*> q;\n    q.push(root);\n    while (!q.empty()) {\n        TreeNode* curr = q.front();\n        q.pop();\n        if (curr) {\n            res.push_back(to_string(curr->val));\n            q.push(curr->left);\n            q.push(curr->right);\n        } else {\n            res.push_back(\"null\");\n        }\n    }\n    while (!res.empty() && res.back() == \"null\") res.pop_back();\n    for (int i = 0; i < (int)res.size(); i++) cout << res[i] << (i + 1 < (int)res.size() ? \" \" : \"\");\n    cout << endl;\n}\n\nvoid flatten(TreeNode* root) {\n    // User logic here\n}\n\nint main() {\n    string line;\n    if (!getline(cin, line)) return 0;\n    regex re(\"null|-?\\\\d+\");\n    vector<string> data;\n    for (sregex_iterator it(line.begin(), line.end(), re), end; it != end; ++it) data.push_back(it->str());\n    TreeNode* root = buildTree(data);\n    flatten(root);\n    serialize(root);\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static TreeNode buildTree(String[] data) {\n        if (data.length == 0 || data[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(data[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < data.length) {\n            TreeNode curr = q.poll();\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(data[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(data[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    public static void serialize(TreeNode root) {\n        if (root == null) return;\n        List<String> res = new ArrayList<>();\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        while (!q.isEmpty()) {\n            TreeNode curr = q.poll();\n            if (curr != null) {\n                res.add(String.valueOf(curr.val));\n                q.add(curr.left);\n                q.add(curr.right);\n            } else {\n                res.add(\"null\");\n            }\n        }\n        while (!res.isEmpty() && res.get(res.size() - 1).equals(\"null\")) res.remove(res.size() - 1);\n        System.out.println(String.join(\" \", res));\n    }\n\n    public static void flatten(TreeNode root) {\n        // User logic here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        List<String> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(line);\n        while (m.find()) list.add(m.group());\n        TreeNode root = buildTree(list.toArray(new String[0]));\n        flatten(root);\n        serialize(root);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass TreeNode {\n    constructor(val = 0, left = null, right = null) {\n        this.val = val;\n        this.left = left;\n        this.right = right;\n    }\n}\n\nfunction buildTree(data) {\n    if (!data.length || data[0] === 'null') return null;\n    let root = new TreeNode(parseInt(data[0]));\n    let q = [root];\n    let i = 1;\n    while (q.length && i < data.length) {\n        let curr = q.shift();\n        if (i < data.length && data[i] !== 'null') {\n            curr.left = new TreeNode(parseInt(data[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < data.length && data[i] !== 'null') {\n            curr.right = new TreeNode(parseInt(data[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction serialize(root) {\n    if (!root) return \"\";\n    let res = [];\n    let q = [root];\n    while (q.length) {\n        let curr = q.shift();\n        if (curr) {\n            res.push(curr.val.toString());\n            q.push(curr.left);\n            q.push(curr.right);\n        } else {\n            res.push(\"null\");\n        }\n    }\n    while (res.length && res[res.length - 1] === \"null\") res.pop();\n    return res.join(\" \");\n}\n\nfunction flatten(root) {\n    // User logic here\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const data = input.match(/null|-?\\d+/g) || [];\n    const root = buildTree(data);\n    flatten(root);\n    console.log(serialize(root));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = atoi(val);\n    node->left = node->right = NULL;\n    return node;\n}\n\nstruct TreeNode* buildTree(char** data, int size) {\n    if (size == 0 || strcmp(data[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = createNode(data[0]);\n    struct TreeNode* q[10000];\n    int head = 0, tail = 0;\n    q[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = q[head++];\n        if (i < size) {\n            curr->left = createNode(data[i]);\n            if (curr->left) q[tail++] = curr->left;\n            i++;\n        }\n        if (i < size) {\n            curr->right = createNode(data[i]);\n            if (curr->right) q[tail++] = curr->right;\n            i++;\n        }\n    }\n    return root;\n}\n\nvoid serialize(struct TreeNode* root) {\n    if (!root) return;\n    struct TreeNode* q[20000];\n    int head = 0, tail = 0;\n    q[tail++] = root;\n    char* res[20000];\n    int rSize = 0;\n    while (head < tail) {\n        struct TreeNode* curr = q[head++];\n        if (curr) {\n            char* s = (char*)malloc(10);\n            sprintf(s, \"%d\", curr->val);\n            res[rSize++] = s;\n            q[tail++] = curr->left;\n            q[tail++] = curr->right;\n        } else {\n            res[rSize++] = \"null\";\n        }\n    }\n    while (rSize > 0 && strcmp(res[rSize - 1], \"null\") == 0) rSize--;\n    for (int i = 0; i < rSize; i++) {\n        printf(\"%s%s\", res[i], (i + 1 < rSize ? \" \" : \"\"));\n    }\n    printf(\"\\n\");\n}\n\nvoid flatten(struct TreeNode* root) {\n    // User logic here\n}\n\nint main() {\n    char line[100000];\n    if (!fgets(line, sizeof(line), stdin)) return 0;\n    char* data[10000];\n    int size = 0;\n    char* t = strtok(line, \" ,[]\\n\\r\");\n    while (t) {\n        data[size++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\");\n    }\n    struct TreeNode* root = buildTree(data, size);\n    flatten(root);\n    serialize(root);\n    return 0;\n}"
    }

    def _solve(vals):
        if not vals or vals[0] == "null": return ""
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
            
        curr = root
        while curr:
            if curr.left:
                p = curr.left
                while p.right: p = p.right
                p.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
            
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        while res and res[-1] == "null": res.pop()
        return " ".join(res)

    test_cases = [
        {"input": "1 2 5 3 4 null 6", "expected_output": "1 null 2 null 3 null 4 null 5 null 6", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "1 2", "expected_output": "1 null 2", "is_sample": False},
        {"input": "1 null 2", "expected_output": "1 null 2", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 null 2 null 3", "is_sample": False},
        {"input": "1 2 2", "expected_output": "1 null 2 null 2", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(1, 11))), "expected_output": _solve(list(map(str, range(1, 11)))), "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": _solve(["1"] + ["2", "null"]*50), "is_sample": False},
        {"input": "1 " + "null 2 "*50, "expected_output": _solve(["1"] + ["null", "2"]*50), "is_sample": False}
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
        "topics": ["Tree", "DFS", "Linked List", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/114_Flatten_Binary_Tree_to_Linked_List.json"
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
