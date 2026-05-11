import json
import os

def generate_json():
    problem_id = 199
    title = "Binary Tree Right Side View"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>199. Binary Tree Right Side View</h3>
<p>Given the <code>root</code> of a binary tree, imagine yourself standing on the <strong>right side</strong> of it, return <em>the values of the nodes you can see ordered from top to bottom</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/14/tree.jpg" style="width: 401px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,5,null,4]
<strong>Output:</strong> [1,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1,null,3]
<strong>Output:</strong> [1,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A single line containing space-separated level-order tree nodes."
    output_format = "A space-separated sequence of integers representing the right side view."
    
    constraints = [
        "Nodes: [0, 100]",
        "-100 <= val <= 100",
        "O(N) time complexity expected."
    ]
    
    explanation = """To find the right side view of a binary tree:
1. **Breadth-First Search (BFS)**:
   - Perform a level-order traversal using a queue.
   - For each level:
     - Record the size of the queue (number of nodes in the current level).
     - Iterate through these nodes.
     - The **last node** explored at each level is the one visible from the right side.
2. **Logic**:
   - Push the root into the queue.
   - While the queue is not empty:
     - For `i` from 1 to `level_size`:
       - Dequeue a node.
       - If `i == level_size`, add the node's value to the result list.
       - Enqueue left and right children if they exist.
3. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(W) where W is the maximum width of the tree."""
    
    answer = """import collections

def rightSideView(root):
    if not root:
        return []
        
    res = []
    queue = collections.deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # If it's the last node of this level
            if i == level_size - 1:
                res.append(node.val)
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            
    return res"""

    boilerplate = {
        "python": "import sys\nimport collections\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(nodes):\n    if not nodes or nodes[0] == 'null': return None\n    root = TreeNode(int(nodes[0]))\n    queue = collections.deque([root])\n    i = 1\n    while queue and i < len(nodes):\n        curr = queue.popleft()\n        if nodes[i] != 'null':\n            curr.left = TreeNode(int(nodes[i]))\n            queue.append(curr.left)\n        i += 1\n        if i < len(nodes) and nodes[i] != 'null':\n            curr.right = TreeNode(int(nodes[i]))\n            queue.append(curr.right)\n        i += 1\n    return root\n\ndef rightSideView(root):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data:\n        sys.exit(0)\n    tree = build_tree(data)\n    res = rightSideView(tree)\n    print(\" \".join(map(str, res)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front();\n        q.pop();\n        if (nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvector<int> rightSideView(TreeNode* root) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        string s;\n        vector<string> nodes;\n        while (ss >> s) nodes.push_back(s);\n        TreeNode* root = buildTree(nodes);\n        vector<int> res = rightSideView(root);\n        for (int i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \" \");\n        }\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public List<Integer> rightSideView(TreeNode root) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static TreeNode buildTree(String[] nodes) {\n        if (nodes.length == 0 || nodes[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.offer(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.length) {\n            TreeNode curr = q.poll();\n            if (!nodes[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes[i]));\n                q.offer(curr.left);\n            }\n            i++;\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes[i]));\n                q.offer(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line == null || line.trim().isEmpty()) return;\n        String[] nodes = line.trim().split(\"\\\\s+\");\n        TreeNode root = buildTree(nodes);\n        List<Integer> res = new Solution().rightSideView(root);\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < res.size(); i++) {\n            sb.append(res.get(i)).append(i == res.size() - 1 ? \"\" : \" \");\n        }\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val)\n    this.left = (left===undefined ? null : left)\n    this.right = (right===undefined ? null : right)\n}\n\nfunction buildTree(nodes) {\n    if (nodes.length === 0 || nodes[0] === 'null') return null;\n    let root = new TreeNode(parseInt(nodes[0]));\n    let q = [root];\n    let i = 1;\n    while (q.length > 0 && i < nodes.length) {\n        let curr = q.shift();\n        if (nodes[i] !== 'null') {\n            curr.left = new TreeNode(parseInt(nodes[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < nodes.length && nodes[i] !== 'null') {\n            curr.right = new TreeNode(parseInt(nodes[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction rightSideView(root) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let root = buildTree(input);\n    let res = rightSideView(root);\n    console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    root->val = atoi(nodes[0]);\n    root->left = root->right = NULL;\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int front = 0, rear = 0;\n    queue[rear++] = root;\n    int i = 1;\n    while (front < rear && i < size) {\n        struct TreeNode* curr = queue[front++];\n        if (strcmp(nodes[i], \"null\") != 0) {\n            curr->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->left->val = atoi(nodes[i]);\n            curr->left->left = curr->left->right = NULL;\n            queue[rear++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->right->val = atoi(nodes[i]);\n            curr->right->left = curr->right->right = NULL;\n            queue[rear++] = curr->right;\n        }\n        i++;\n    }\n    free(queue);\n    return root;\n}\n\nint* rightSideView(struct TreeNode* root, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line[100000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* nodes[10000];\n        int size = 0;\n        char* token = strtok(line, \" \\t\\r\\n\");\n        while (token) {\n            nodes[size++] = token;\n            token = strtok(NULL, \" \\t\\r\\n\");\n        }\n        struct TreeNode* root = buildTree(nodes, size);\n        int returnSize;\n        int* res = rightSideView(root, &returnSize);\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], i == returnSize - 1 ? \"\" : \" \");\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 null 5 null 4", "expected_output": "1 3 4", "is_sample": True},
        {"input": "1 null 3", "expected_output": "1 3", "is_sample": True},
        {"input": "null", "expected_output": "", "is_sample": True},
        {"input": "1 2 3 4", "expected_output": "1 3 4", "is_sample": False},
        {"input": "1 2 null 3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "5 4 8 11 null 13 4 7 2 null null null 1", "expected_output": "5 8 4 1", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "1 3 7", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": "...", "is_sample": False},
        {"input": "1 " + "null 2 " * 50, "expected_output": " ".join([str(i+1) for i in range(51)]), "is_sample": False},
        {"input": "1 " + "2 null " * 50, "expected_output": " ".join([str(i+1) for i in range(51)]), "is_sample": False}
    ]

    # Stress case 8 expected output script
    def _solve(nodes):
        if not nodes or nodes[0] == 'null': return []
        root = {'v': int(nodes[0]), 'l': None, 'r': None}
        q = [root]
        idx = 1
        while q and idx < len(nodes):
            curr = q.pop(0)
            if nodes[idx] != 'null':
                curr['l'] = {'v': int(nodes[idx]), 'l': None, 'r': None}
                q.append(curr['l'])
            idx += 1
            if idx < len(nodes) and nodes[idx] != 'null':
                curr['r'] = {'v': int(nodes[idx]), 'l': None, 'r': None}
                q.append(curr['r'])
            idx += 1
        res = []
        q = [root]
        while q:
            sz = len(q)
            for i in range(sz):
                c = q.pop(0)
                if i == sz - 1: res.append(c['v'])
                if c['l']: q.append(c['l'])
                if c['r']: q.append(c['r'])
        return res
    
    test_cases[7]["expected_output"] = " ".join(map(str, _solve([str(i) for i in range(100)])))

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

    output_path = "1-200/199_Binary_Tree_Right_Side_View.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
