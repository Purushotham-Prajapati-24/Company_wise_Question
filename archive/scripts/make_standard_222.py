import json
import os

def generate_json():
    problem_id = 222
    title = "Count Complete Tree Nodes"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>222. Count Complete Tree Nodes</h3>
<p>Given the <code>root</code> of a <strong>complete</strong> binary tree, return the number of the nodes in the tree.</p>

<p>According to <strong><a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a></strong>, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between <code>1</code> and <code>2<sup>h</sup></code> nodes inclusive at the last level <code>h</code>.</p>

<p>Design an algorithm that runs in less than&nbsp;<code class="highlighter-rouge">O(n)</code>&nbsp;time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;" />
<pre><strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 5 * 10<sup>4</sup></code></li>
	<li>The tree is guaranteed to be <strong>complete</strong>.</li>
</ul>"""

    input_format = "A stringified array representing level-order traversal of a complete binary tree."
    output_format = "An integer representing the count of nodes."
    
    constraints = [
        "0 <= number of nodes <= 50,000",
        "0 <= Node.val <= 50,000",
        "Required time complexity: Less than O(N)."
    ]
    
    explanation = """To count nodes in a complete binary tree in O(log^2 N) time:
1. **Perfect Binary Tree Check**:
   - Calculate the height of the left-most branch (always going left).
   - Calculate the height of the right-most branch (always going right).
   - If heights are equal, the tree is perfect. Node count = `2^height - 1`.
2. **Recursive Descent**:
   - If heights are not equal, the total nodes = `1 + count(left_subtree) + count(right_subtree)`.
3. **Complexity**:
   - At each step, at least one subtree is guaranteed to be a perfect binary tree.
   - We calculate height (O(log N)) at each level of recursion (O(log N)).
   - Total time: O(log^2 N)."""
    
    answer = """class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def get_left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
            
        def get_right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
            
        l_h = get_left_height(root)
        r_h = get_right_height(root)
        
        if l_h == r_h:
            return (1 << l_h) - 1
            
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(arr):\n    if not arr: return None\n    root = TreeNode(arr[0])\n    queue = [root]\n    i = 1\n    while i < len(arr):\n        curr = queue.pop(0)\n        if i < len(arr) and arr[i] is not None:\n            curr.left = TreeNode(arr[i])\n            queue.append(curr.left)\n        i += 1\n        if i < len(arr) and arr[i] is not None:\n            curr.right = TreeNode(arr[i])\n            queue.append(curr.right)\n        i += 1\n    return root\n\ndef countNodes(root):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        try:\n            arr = json.loads(line)\n        except:\n            arr = [int(x) if x != 'null' else None for x in line.replace('[', '').replace(']', '').replace(',', ' ').split()]\n        print(countNodes(build_tree(arr)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front();\n        q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nint countNodes(TreeNode* root) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        string val;\n        vector<string> nodes;\n        while (ss >> val) nodes.push_back(val);\n        cout << countNodes(buildTree(nodes)) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public int countNodes(TreeNode root) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            line = line.replace(\"[\", \"\").replace(\"]\", \"\").replace(\",\", \" \");\n            String[] parts = line.trim().split(\"\\\\s+\");\n            TreeNode root = buildTree(parts);\n            System.out.println(new Solution().countNodes(root));\n        }\n    }\n\n    static TreeNode buildTree(String[] nodes) {\n        if (nodes.length == 0 || nodes[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.length) {\n            TreeNode curr = q.poll();\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < nodes.length && !nodes[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val)\n    this.left = (left===undefined ? null : left)\n    this.right = (right===undefined ? null : right)\n}\n\nfunction buildTree(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]);\n    let queue = [root];\n    let i = 1;\n    while (queue.length && i < arr.length) {\n        let curr = queue.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            queue.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            queue.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction countNodes(root) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    let arr = JSON.parse(input);\n    console.log(countNodes(buildTree(arr)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    root->val = atoi(nodes[0]);\n    root->left = root->right = NULL;\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = queue[head++];\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->left->val = atoi(nodes[i]);\n            curr->left->left = curr->left->right = NULL;\n            queue[tail++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->right->val = atoi(nodes[i]);\n            curr->right->left = curr->right->right = NULL;\n            queue[tail++] = curr->right;\n        }\n        i++;\n    }\n    return root;\n}\n\nint countNodes(struct TreeNode* root) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char line[100000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \"[], \");\n        char** nodes = (char**)malloc(10000 * sizeof(char*));\n        int size = 0;\n        while (token) {\n            nodes[size++] = strdup(token);\n            token = strtok(NULL, \"[], \");\n        }\n        printf(\"%d\\n\", countNodes(buildTree(nodes, size)));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4,5,6]", "expected_output": "6", "is_sample": True},
        {"input": "[]", "expected_output": "0", "is_sample": True},
        {"input": "[1]", "expected_output": "1", "is_sample": True},
        {"input": "[1,2,3]", "expected_output": "3", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "7", "is_sample": False},
        {"input": "[1,2,3,4]", "expected_output": "4", "is_sample": False},
        {"input": "[1,2]", "expected_output": "2", "is_sample": False},
        # Stress Tests (Up to 50k nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    # Stress 8: Perfect tree height 14 (16383 nodes)
    b8 = list(range(1, 16384))
    test_cases[7] = {"input": json.dumps(b8), "expected_output": str(len(b8)), "is_sample": False}
    # Stress 9: Max limit 50,000 nodes
    b9 = list(range(1, 50001))
    test_cases[8] = {"input": json.dumps(b9), "expected_output": str(len(b9)), "is_sample": False}
    # Stress 10: Skewed complete (minimum last level)
    b10 = list(range(1, 16385))  # 16383 + 1
    test_cases[9] = {"input": json.dumps(b10), "expected_output": str(len(b10)), "is_sample": False}

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
        "topics": ["Binary Search", "Tree", "Binary Tree", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "201-400/222_Count_Complete_Tree_Nodes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
