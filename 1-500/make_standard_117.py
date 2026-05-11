import json
import os

def generate_json():
    problem_id = 117
    title = "Populating Next Right Pointers in Each Node II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>117. Populating Next Right Pointers in Each Node II</h3>
<p>Given a binary tree</p>

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
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,null,7]
<strong>Output:</strong> [1,#,2,3,#,4,5,7,#]
<strong>Explanation: </strong>Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 6000]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong>
<ul>
	<li>You may only use constant extra space.</li>
	<li>The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.</li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "A single line containing space-separated values representing the level-order traversal with '#' at the end of each level."
    
    constraints = [
        "0 <= number of nodes <= 6000",
        "-100 <= Node.val <= 100.",
        "The tree can be any binary tree (not necessarily perfect)."
    ]
    
    explanation = """To populate the `next` pointers in any binary tree using O(1) extra space:
1. **Level-by-Level Iteration with Dummy Node**:
   - For each level, we use a `dummy` node to act as a placeholder for the head of the next level.
   - We maintain a `prev` pointer initialized to `dummy` to connect nodes in the next level as we find them.
2. **Logic**:
   - Traverse the current level using the existing `next` pointers.
   - For each node `curr` in the current level:
     - If `curr.left` exists, link `prev.next = curr.left` and move `prev`.
     - If `curr.right` exists, link `prev.next = curr.right` and move `prev`.
   - After finishing the current level, move to the head of the next level: `curr = dummy.next`.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited once.
   - Space Complexity: O(1) as we reuse pointers and only use a few temporary variables."""
    
    answer = """class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return root
    
    curr = root
    while curr:
        dummy = Node(0)
        prev = dummy
        while curr:
            if curr.left:
                prev.next = curr.left
                prev = prev.next
            if curr.right:
                prev.next = curr.right
                prev = prev.next
            curr = curr.next
        # Move to the first node of the next level
        curr = dummy.next
        
    return root"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import deque\n\nclass Node:\n    def __init__(self, val: int = 0, left=None, right=None, next=None):\n        self.val = val\n        self.left = left\n        self.right = right\n        self.next = next\n\ndef build_tree(data):\n    if not data or data[0] == 'null': return None\n    root = Node(int(data[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(data):\n        node = queue.popleft()\n        if i < len(data) and data[i] != 'null':\n            node.left = Node(int(data[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] != 'null':\n            node.right = Node(int(data[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef serialize(root):\n    if not root: return \"\"\n    res = []\n    leftmost = root\n    while leftmost:\n        curr = leftmost\n        while curr:\n            res.append(str(curr.val))\n            curr = curr.next\n        res.append(\"#\")\n        temp_dummy = Node(0)\n        curr = leftmost\n        while curr:\n            if curr.left:\n                temp_dummy.next = curr.left\n                break\n            if curr.right:\n                temp_dummy.next = curr.right\n                break\n            curr = curr.next\n        leftmost = temp_dummy.next\n    return \" \".join(res)\n\ndef connect(root):\n    # User logic here\n    return root\n\nif __name__ == \"__main__\":\n    line = sys.stdin.read().strip()\n    if line:\n        data = re.findall(r'null|-?\\d+', line)\n        root = build_tree(data)\n        root = connect(root)\n        print(serialize(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct Node {\n    int val;\n    Node *left;\n    Node *right;\n    Node *next;\n    Node(int x) : val(x), left(NULL), right(NULL), next(NULL) {}\n};\n\nNode* buildTree(vector<string>& data) {\n    if (data.empty() || data[0] == \"null\") return NULL;\n    Node* root = new Node(stoi(data[0]));\n    queue<Node*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < data.size()) {\n        Node* curr = q.front();\n        q.pop();\n        if (i < data.size() && data[i] != \"null\") {\n            curr->left = new Node(stoi(data[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < data.size() && data[i] != \"null\") {\n            curr->right = new Node(stoi(data[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid serialize(Node* root) {\n    if (!root) return;\n    Node* leftmost = root;\n    bool first = true;\n    while (leftmost) {\n        Node* curr = leftmost;\n        while (curr) {\n            if (!first) cout << \" \";\n            cout << curr->val;\n            first = false;\n            curr = curr->next;\n        }\n        cout << \" #\";\n        Node* next_level = NULL;\n        Node* temp = leftmost;\n        while (temp) {\n            if (temp->left) { next_level = temp->left; break; }\n            if (temp->right) { next_level = temp->right; break; }\n            temp = temp->next;\n        }\n        leftmost = next_level;\n    }\n    cout << endl;\n}\n\nNode* connect(Node* root) {\n    // User logic here\n    return root;\n}\n\nint main() {\n    string line;\n    if (!getline(cin, line)) return 0;\n    regex re(\"null|-?\\\\d+\");\n    vector<string> data;\n    for (sregex_iterator it(line.begin(), line.end(), re), end; it != end; ++it) data.push_back(it->str());\n    Node* root = buildTree(data);\n    root = connect(root);\n    serialize(root);\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Node {\n    int val;\n    Node left;\n    Node right;\n    Node next;\n    Node(int x) { val = x; }\n}\n\npublic class Main {\n    public static Node buildTree(String[] data) {\n        if (data.length == 0 || data[0].equals(\"null\")) return null;\n        Node root = new Node(Integer.parseInt(data[0]));\n        Queue<Node> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < data.length) {\n            Node curr = q.poll();\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.left = new Node(Integer.parseInt(data[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.right = new Node(Integer.parseInt(data[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    public static void serialize(Node root) {\n        if (root == null) return;\n        List<String> res = new ArrayList<>();\n        Node leftmost = root;\n        while (leftmost != null) {\n            Node curr = leftmost;\n            while (curr != null) {\n                res.add(String.valueOf(curr.val));\n                curr = curr.next;\n            }\n            res.add(\"#\");\n            Node next_level = null;\n            Node temp = leftmost;\n            while (temp != null) {\n                if (temp.left != null) { next_level = temp.left; break; }\n                if (temp.right != null) { next_level = temp.right; break; }\n                temp = temp.next;\n            }\n            leftmost = next_level;\n        }\n        System.out.println(String.join(\" \", res));\n    }\n\n    public static Node connect(Node root) {\n        // User logic here\n        return root;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        List<String> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(line);\n        while (m.find()) list.add(m.group());\n        Node root = buildTree(list.toArray(new String[0]));\n        root = connect(root);\n        serialize(root);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass Node {\n    constructor(val = 0, left = null, right = null, next = null) {\n        this.val = val;\n        this.left = left;\n        this.right = right;\n        this.next = next;\n    }\n}\n\nfunction buildTree(data) {\n    if (!data.length || data[0] === 'null') return null;\n    let root = new Node(parseInt(data[0]));\n    let q = [root];\n    let i = 1;\n    while (q.length && i < data.length) {\n        let curr = q.shift();\n        if (i < data.length && data[i] !== 'null') {\n            curr.left = new Node(parseInt(data[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < data.length && data[i] !== 'null') {\n            curr.right = new Node(parseInt(data[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction serialize(root) {\n    if (!root) return \"\";\n    let res = [];\n    let leftmost = root;\n    while (leftmost) {\n        let curr = leftmost;\n        while (curr) {\n            res.push(curr.val.toString());\n            curr = curr.next;\n        }\n        res.push(\"#\");\n        let next_level = null;\n        let temp = leftmost;\n        while (temp) {\n            if (temp.left) { next_level = temp.left; break; }\n            if (temp.right) { next_level = temp.right; break; }\n            temp = temp.next;\n        }\n        leftmost = next_level;\n    }\n    return res.join(\" \");\n}\n\nfunction connect(root) {\n    // User logic here\n    return root;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const data = input.match(/null|-?\\d+/g) || [];\n    const root = buildTree(data);\n    const result = connect(root);\n    console.log(serialize(result));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct Node {\n    int val;\n    struct Node *left;\n    struct Node *right;\n    struct Node *next;\n};\n\nstruct Node* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct Node* node = (struct Node*)malloc(sizeof(struct Node));\n    node->val = atoi(val);\n    node->left = node->right = node->next = NULL;\n    return node;\n}\n\nstruct Node* buildTree(char** data, int size) {\n    if (size == 0 || strcmp(data[0], \"null\") == 0) return NULL;\n    struct Node* root = createNode(data[0]);\n    struct Node* q[10000];\n    int head = 0, tail = 0;\n    q[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct Node* curr = q[head++];\n        if (i < size) {\n            curr->left = createNode(data[i]);\n            if (curr->left) q[tail++] = curr->left;\n            i++;\n        }\n        if (i < size) {\n            curr->right = createNode(data[i]);\n            if (curr->right) q[tail++] = curr->right;\n            i++;\n        }\n    }\n    return root;\n}\n\nvoid serialize(struct Node* root) {\n    if (!root) return;\n    struct Node* leftmost = root;\n    bool first = true;\n    while (leftmost) {\n        struct Node* curr = leftmost;\n        while (curr) {\n            if (!first) printf(\" \");\n            printf(\"%d\", curr->val);\n            first = false;\n            curr = curr->next;\n        }\n        printf(\" #\");\n        struct Node* next_level = NULL;\n        struct Node* temp = leftmost;\n        while (temp) {\n            if (temp->left) { next_level = temp->left; break; }\n            if (temp->right) { next_level = temp->right; break; }\n            temp = temp->next;\n        }\n        leftmost = next_level;\n    }\n    printf(\"\\n\");\n}\n\nstruct Node* connect(struct Node* root) {\n    // User logic here\n    return root;\n}\n\nint main() {\n    char line[100000];\n    if (!fgets(line, sizeof(line), stdin)) return 0;\n    char* data[10000];\n    int size = 0;\n    char* t = strtok(line, \" ,[]\\n\\r\");\n    while (t) {\n        data[size++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\");\n    }\n    struct Node* root = buildTree(data, size);\n    root = connect(root);\n    serialize(root);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 5 null 7", "expected_output": "1 # 2 3 # 4 5 7 #", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1 #", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "1 # 2 # 3 #", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "1 # 2 # 3 #", "is_sample": False},
        {"input": "1 2 3 null 4 null 5", "expected_output": "1 # 2 3 # 4 5 #", "is_sample": False},
        {"input": "1 2 2 null 3 null 3", "expected_output": "1 # 2 2 # 3 3 #", "is_sample": False},
        # Stress cases
        {"input": "1 " + "2 null "*50, "expected_output": "1 # " + " ".join(["2"]*51 + ["#"]*51).replace("  ", " ").strip(), "is_sample": False}, # Actually not that simple serialization. I'll use a helper for stress.
        {"input": " ".join(["1"]*15), "expected_output": "1 # 1 1 # 1 1 1 1 # 1 1 1 1 1 1 1 1 #", "is_sample": False},
        {"input": "1 2 3 4 null 5 6 null null null null 7", "expected_output": "1 # 2 3 # 4 5 6 # 7 #", "is_sample": False}
    ]
    
    # Fix stress case 8
    test_cases[7] = {"input": "1 " + "2 null "*10, "expected_output": "1 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 #", "is_sample": False}

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

    output_path = "1-200/117_Populating_Next_Right_Pointers_in_Each_Node_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
