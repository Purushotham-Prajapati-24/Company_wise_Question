import json
import os

def generate_json():
    problem_id = 116
    title = "Populating Next Right Pointers in Each Node"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>116. Populating Next Right Pointers in Each Node</h3>
<p>You are given a <strong>perfect binary tree</strong> where all leaves are at the same level, and every parent node has exactly two children. The binary tree has the following definition:</p>

<pre>
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
</pre>

<p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p>
<p>Initially, all next pointers are set to <code>NULL</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="width: 500px; height: 171px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7]
<strong>Output:</strong> [1,#,2,3,#,4,5,6,7,#]
<strong>Explanation: </strong>Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2<sup>12</sup> - 1]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong>
<ul>
	<li>You may only use constant extra space.</li>
	<li>The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.</li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a perfect binary tree (integers or 'null')."
    output_format = "A single line containing space-separated values representing the level-order traversal with '#' at the end of each level."
    
    constraints = [
        "0 <= number of nodes <= 4095 (2^12 - 1)",
        "-1000 <= Node.val <= 1000.",
        "The tree is a perfect binary tree."
    ]
    
    explanation = """To populate the `next` pointers in a perfect binary tree using O(1) extra space:
1. **Level-by-Level Iteration**: Start with the root level. For each level, we use the `next` pointers already established in the levels above to traverse the current level and connect its children.
2. **Connection Logic**: 
   - Connect left child to right child: `curr.left.next = curr.right`.
   - If `curr.next` exists, connect `curr.right` to `curr.next.left`.
3. **Traversal**: Maintain a `leftmost` pointer to jump to the next level.
4. **Complexity**: O(N) time and O(1) space."""
    
    answer = """class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return root
    leftmost = root
    while leftmost.left:
        curr = leftmost
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        leftmost = leftmost.left
    return root"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import deque\n\nclass Node:\n    def __init__(self, val: int = 0, left=None, right=None, next=None):\n        self.val = val\n        self.left = left\n        self.right = right\n        self.next = next\n\ndef build_tree(data):\n    if not data or data[0] == 'null': return None\n    root = Node(int(data[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(data):\n        node = queue.popleft()\n        if i < len(data) and data[i] != 'null':\n            node.left = Node(int(data[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] != 'null':\n            node.right = Node(int(data[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef serialize(root):\n    if not root: return \"\"\n    res, l = [], root\n    while l:\n        c = l\n        while c:\n            res.append(str(c.val))\n            c = c.next\n        res.append(\"#\")\n        l = l.left\n    return \" \".join(res)\n\ndef connect(root):\n    # User logic here\n    return root\n\nif __name__ == \"__main__\":\n    line = sys.stdin.read().strip()\n    if line:\n        data = re.findall(r'null|-?\\d+', line)\n        root = build_tree(data)\n        root = connect(root)\n        print(serialize(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct Node {\n    int val;\n    Node *left;\n    Node *right;\n    Node *next;\n    Node(int x) : val(x), left(NULL), right(NULL), next(NULL) {}\n};\n\nNode* buildTree(vector<string>& data) {\n    if (data.empty() || data[0] == \"null\") return NULL;\n    Node* root = new Node(stoi(data[0]));\n    queue<Node*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < data.size()) {\n        Node* curr = q.front();\n        q.pop();\n        if (i < data.size() && data[i] != \"null\") {\n            curr->left = new Node(stoi(data[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < data.size() && data[i] != \"null\") {\n            curr->right = new Node(stoi(data[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid serialize(Node* root) {\n    if (!root) return;\n    Node* l = root;\n    bool first = true;\n    while (l) {\n        Node* c = l;\n        while (c) {\n            if (!first) cout << \" \";\n            cout << c->val;\n            first = false;\n            c = c->next;\n        }\n        cout << \" #\";\n        l = l->left;\n    }\n    cout << endl;\n}\n\nNode* connect(Node* root) {\n    // User logic here\n    return root;\n}\n\nint main() {\n    string line;\n    if (!getline(cin, line)) return 0;\n    regex re(\"null|-?\\\\d+\");\n    vector<string> data;\n    for (sregex_iterator it(line.begin(), line.end(), re), end; it != end; ++it) data.push_back(it->str());\n    Node* root = buildTree(data);\n    root = connect(root);\n    serialize(root);\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Node {\n    int val;\n    Node left;\n    Node right;\n    Node next;\n    Node(int x) { val = x; }\n}\n\npublic class Main {\n    public static Node buildTree(String[] data) {\n        if (data.length == 0 || data[0].equals(\"null\")) return null;\n        Node root = new Node(Integer.parseInt(data[0]));\n        Queue<Node> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < data.length) {\n            Node curr = q.poll();\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.left = new Node(Integer.parseInt(data[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.right = new Node(Integer.parseInt(data[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    public static void serialize(Node root) {\n        if (root == null) return;\n        List<String> res = new ArrayList<>();\n        Node l = root;\n        while (l != null) {\n            Node c = l;\n            while (c != null) {\n                res.add(String.valueOf(c.val));\n                c = c.next;\n            }\n            res.add(\"#\");\n            l = l.left;\n        }\n        System.out.println(String.join(\" \", res));\n    }\n\n    public static Node connect(Node root) {\n        // User logic here\n        return root;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        List<String> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(line);\n        while (m.find()) list.add(m.group());\n        Node root = buildTree(list.toArray(new String[0]));\n        root = connect(root);\n        serialize(root);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass Node {\n    constructor(val = 0, left = null, right = null, next = null) {\n        this.val = val;\n        this.left = left;\n        this.right = right;\n        this.next = next;\n    }\n}\n\nfunction buildTree(data) {\n    if (!data.length || data[0] === 'null') return null;\n    let root = new Node(parseInt(data[0]));\n    let q = [root];\n    let i = 1;\n    while (q.length && i < data.length) {\n        let curr = q.shift();\n        if (i < data.length && data[i] !== 'null') {\n            curr.left = new Node(parseInt(data[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < data.length && data[i] !== 'null') {\n            curr.right = new Node(parseInt(data[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction serialize(root) {\n    if (!root) return \"\";\n    let res = [];\n    let l = root;\n    while (l) {\n        let c = l;\n        while (c) {\n            res.push(c.val.toString());\n            c = c.next;\n        }\n        res.push(\"#\");\n        l = l.left;\n    }\n    return res.join(\" \");\n}\n\nfunction connect(root) {\n    // User logic here\n    return root;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const data = input.match(/null|-?\\d+/g) || [];\n    const root = buildTree(data);\n    const result = connect(root);\n    console.log(serialize(result));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct Node {\n    int val;\n    struct Node *left;\n    struct Node *right;\n    struct Node *next;\n};\n\nstruct Node* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct Node* node = (struct Node*)malloc(sizeof(struct Node));\n    node->val = atoi(val);\n    node->left = node->right = node->next = NULL;\n    return node;\n}\n\nstruct Node* buildTree(char** data, int size) {\n    if (size == 0 || strcmp(data[0], \"null\") == 0) return NULL;\n    struct Node* root = createNode(data[0]);\n    struct Node* q[10000];\n    int head = 0, tail = 0;\n    q[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct Node* curr = q[head++];\n        if (i < size) {\n            curr->left = createNode(data[i]);\n            if (curr->left) q[tail++] = curr->left;\n            i++;\n        }\n        if (i < size) {\n            curr->right = createNode(data[i]);\n            if (curr->right) q[tail++] = curr->right;\n            i++;\n        }\n    }\n    return root;\n}\n\nvoid serialize(struct Node* root) {\n    if (!root) return;\n    struct Node* l = root;\n    bool first = true;\n    while (l) {\n        struct Node* c = l;\n        while (c) {\n            if (!first) printf(\" \");\n            printf(\"%d\", c->val);\n            first = false;\n            c = c->next;\n        }\n        printf(\" #\");\n        l = l->left;\n    }\n    printf(\"\\n\");\n}\n\nstruct Node* connect(struct Node* root) {\n    // User logic here\n    return root;\n}\n\nint main() {\n    char line[100000];\n    if (!fgets(line, sizeof(line), stdin)) return 0;\n    char* data[10000];\n    int size = 0;\n    char* t = strtok(line, \" ,[]\\n\\r\");\n    while (t) {\n        data[size++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\");\n    }\n    struct Node* root = buildTree(data, size);\n    root = connect(root);\n    serialize(root);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 5 6 7", "expected_output": "1 # 2 3 # 4 5 6 7 #", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1 #", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 # 2 3 #", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "expected_output": "1 # 2 3 # 4 5 6 7 # 8 9 10 11 12 13 14 15 #", "is_sample": False},
        # Diverse cases
        {"input": "0 0 0 0 0 0 0", "expected_output": "0 # 0 0 # 0 0 0 0 #", "is_sample": False},
        {"input": "-1 -2 -3 -4 -5 -6 -7", "expected_output": "-1 # -2 -3 # -4 -5 -6 -7 #", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"]*3), "expected_output": "1 # 1 1 #", "is_sample": False},
        {"input": " ".join(["1"]*7), "expected_output": "1 # 1 1 # 1 1 1 1 #", "is_sample": False},
        {"input": " ".join(["1"]*31), "expected_output": "1 # 1 1 # 1 1 1 1 # 1 1 1 1 1 1 1 1 # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 #", "is_sample": False}
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

    output_path = "1-200/116_Populating_Next_Right_Pointers_in_Each_Node.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
