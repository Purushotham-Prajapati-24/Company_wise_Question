import json
import os

def generate_json():
    problem_id = 110
    title = "Balanced Binary Tree"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>110. Balanced Binary Tree</h3>
<p>Given a binary tree, determine if it is <strong>height-balanced</strong>.</p>

<p>A <strong>height-balanced</strong> binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre><strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of a binary tree (integers or 'null')."
    output_format = "true if the tree is height-balanced, false otherwise."
    
    constraints = [
        "0 <= number of nodes <= 5000",
        "-10^4 <= Node.val <= 10^4."
    ]
    
    explanation = """To determine if a binary tree is height-balanced:
1. **Definition**: For every node, the difference in height between its left and right subtrees `abs(height(left) - height(right))` must be `<= 1`.
2. **Optimized Bottom-Up DFS**:
   - Instead of checking the height of subtrees repeatedly (which would be O(N^2)), we can return the height from a helper function.
   - If a subtree is unbalanced, the helper returns `-1`.
   - If both subtrees are balanced and their height difference is `<= 1`, return the calculated height: `1 + max(left_height, right_height)`.
   - Otherwise, return `-1`.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited once.
   - Space Complexity: O(H) where H is the height of the tree, for the recursion stack."""
    
    answer = """def isBalanced(root):
    def checkHeight(node):
        if not node:
            return 0
        
        left_h = checkHeight(node.left)
        if left_h == -1: return -1
        
        right_h = checkHeight(node.right)
        if right_h == -1: return -1
        
        if abs(left_h - right_h) > 1:
            return -1
            
        return 1 + max(left_h, right_h)
        
    return checkHeight(root) != -1"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data or data[0] == 'null': return None\n    root = TreeNode(int(data[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(data):\n        node = queue.popleft()\n        if i < len(data) and data[i] != 'null':\n            node.left = TreeNode(int(data[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] != 'null':\n            node.right = TreeNode(int(data[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef isBalanced(root):\n    # User logic here\n    return True\n\nif __name__ == \"__main__\":\n    line = sys.stdin.read().strip()\n    if line:\n        data = re.findall(r'null|-?\\d+', line)\n        root = build_tree(data)\n        result = isBalanced(root)\n        print(str(result).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& data) {\n    if (data.empty() || data[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(data[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < data.size()) {\n        TreeNode* curr = q.front();\n        q.pop();\n        if (i < data.size() && data[i] != \"null\") {\n            curr->left = new TreeNode(stoi(data[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < data.size() && data[i] != \"null\") {\n            curr->right = new TreeNode(stoi(data[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nbool isBalanced(TreeNode* root) {\n    // User logic here\n    return true;\n}\n\nint main() {\n    string line;\n    if (!getline(cin, line)) return 0;\n    regex re(\"null|-?\\\\d+\");\n    vector<string> data;\n    for (sregex_iterator it(line.begin(), line.end(), re), end; it != end; ++it) data.push_back(it->str());\n    TreeNode* root = buildTree(data);\n    cout << (isBalanced(root) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static TreeNode buildTree(String[] data) {\n        if (data.length == 0 || data[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(data[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < data.length) {\n            TreeNode curr = q.poll();\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(data[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(data[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    public static boolean isBalanced(TreeNode root) {\n        // User logic here\n        return true;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine();\n        List<String> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(line);\n        while (m.find()) list.add(m.group());\n        TreeNode root = buildTree(list.toArray(new String[0]));\n        System.out.println(isBalanced(root) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass TreeNode {\n    constructor(val = 0, left = null, right = null) {\n        this.val = val;\n        this.left = left;\n        this.right = right;\n    }\n}\n\nfunction buildTree(data) {\n    if (!data.length || data[0] === 'null') return null;\n    let root = new TreeNode(parseInt(data[0]));\n    let q = [root];\n    let i = 1;\n    while (q.length && i < data.length) {\n        let curr = q.shift();\n        if (i < data.length && data[i] !== 'null') {\n            curr.left = new TreeNode(parseInt(data[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < data.length && data[i] !== 'null') {\n            curr.right = new TreeNode(parseInt(data[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction isBalanced(root) {\n    // User logic here\n    return true;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const data = input.match(/null|-?\\d+/g) || [];\n    const root = buildTree(data);\n    console.log(isBalanced(root) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = atoi(val);\n    node->left = node->right = NULL;\n    return node;\n}\n\nstruct TreeNode* buildTree(char** data, int size) {\n    if (size == 0 || strcmp(data[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = createNode(data[0]);\n    struct TreeNode* q[10000];\n    int head = 0, tail = 0;\n    q[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = q[head++];\n        if (i < size) {\n            curr->left = createNode(data[i]);\n            if (curr->left) q[tail++] = curr->left;\n            i++;\n        }\n        if (i < size) {\n            curr->right = createNode(data[i]);\n            if (curr->right) q[tail++] = curr->right;\n            i++;\n        }\n    }\n    return root;\n}\n\nbool isBalanced(struct TreeNode* root) {\n    // User logic here\n    return true;\n}\n\nint main() {\n    char line[100000];\n    if (!fgets(line, sizeof(line), stdin)) return 0;\n    char* data[10000];\n    int size = 0;\n    char* t = strtok(line, \" ,[]\\n\\r\");\n    while (t) {\n        data[size++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\");\n    }\n    struct TreeNode* root = buildTree(data, size);\n    printf(\"%s\\n\", isBalanced(root) ? \"true\" : \"false\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 null null 15 7", "expected_output": "true", "is_sample": True},
        {"input": "1 2 2 3 3 null null 4 4", "expected_output": "false", "is_sample": True},
        {"input": "", "expected_output": "true", "is_sample": False},
        {"input": "1", "expected_output": "true", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "false", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "false", "is_sample": False},
        {"input": "1 2 2 3 null null 3 4 null null 4", "expected_output": "false", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 1025)]), "expected_output": "true", "is_sample": False},
        {"input": "1 " + "2 null "*50, "expected_output": "false", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "expected_output": "true", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/110_Balanced_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
