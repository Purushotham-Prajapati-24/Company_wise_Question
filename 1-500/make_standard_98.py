import json
import os

def generate_json():
    problem_id = 98
    title = "Validate Binary Search Tree"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>98. Validate Binary Search Tree</h3>
<p>Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary search tree (BST)</em>.</p>

<p>A <strong>valid BST</strong> is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>strictly less than</strong> the node's key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>strictly greater than</strong> the node's key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" />
<pre>
<strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree (integers or 'null')."
    output_format = "A boolean (true/false) representing if the tree is a valid BST."
    
    constraints = [
        "1 <= number of nodes <= 10^4",
        "-2^31 <= Node.val <= 2^31 - 1."
    ]
    
    explanation = """To validate a Binary Search Tree (BST):
1. **Range-based DFS**:
   - A node is valid if its value lies strictly within a range `(low, high)`.
   - For the root, the range is `(-infinity, +infinity)`.
   - When moving to the **left** child, update the upper bound: `(low, node.val)`.
   - When moving to the **right** child, update the lower bound: `(node.val, high)`.
   - If any node violates this range, or any child subtree is invalid, return `false`.
2. **Inorder Traversal Approach**:
   - An inorder traversal of a valid BST must result in a strictly increasing sequence of values.
   - Keep track of the previously visited node's value and compare it with the current node's value.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) where H is the height of the tree, for the recursion stack."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
                
    return validate(root)"""

    boilerplate = {
        "python": "import sys, re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass Solution:\n    def isValidBST(self, root):\n        # User Logic Here\n        return True\n\ndef build_tree(data):\n    tokens = re.findall(r'null|-?\\d+', data)\n    if not tokens: return None\n    def to_val(t): return None if t == 'null' else int(t)\n    root = TreeNode(to_val(tokens[0]))\n    if root.val is None: return None\n    queue = deque([root])\n    i = 1\n    while queue and i < len(tokens):\n        node = queue.popleft()\n        if i < len(tokens):\n            val = to_val(tokens[i])\n            if val is not None:\n                node.left = TreeNode(val)\n                queue.append(node.left)\n            i += 1\n        if i < len(tokens):\n            val = to_val(tokens[i])\n            if val is not None:\n                node.right = TreeNode(val)\n                queue.append(node.right)\n            i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    root = build_tree(data)\n    sol = Solution()\n    print(str(sol.isValidBST(root)).lower())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    bool isValidBST(TreeNode* root) {\n        // User Logic Here\n        return true;\n    }\n};\n\nTreeNode* buildTree(string data) {\n    regex rgx(\"null|-?\\\\d+\");\n    auto words_begin = sregex_iterator(data.begin(), data.end(), rgx);\n    auto words_end = sregex_iterator();\n    if (words_begin == words_end) return NULL;\n    \n    string first = words_begin->str();\n    if (first == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(first));\n    queue<TreeNode*> q;\n    q.push(root);\n    words_begin++;\n\n    while (!q.empty() && words_begin != words_end) {\n        TreeNode* node = q.front(); q.pop();\n        \n        string leftVal = words_begin->str();\n        words_begin++;\n        if (leftVal != \"null\") {\n            node->left = new TreeNode(stoi(leftVal));\n            q.push(node->left);\n        }\n        \n        if (words_begin == words_end) break;\n        string rightVal = words_begin->str();\n        words_begin++;\n        if (rightVal != \"null\") {\n            node->right = new TreeNode(stoi(rightVal));\n            q.push(node->right);\n        }\n    }\n    return root;\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    TreeNode* root = buildTree(input);\n    Solution sol;\n    cout << (sol.isValidBST(root) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public boolean isValidBST(TreeNode root) {\n        // User Logic Here\n        return true;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        List<String> tokens = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(input);\n        while (m.find()) tokens.add(m.group());\n        \n        if (tokens.isEmpty() || tokens.get(0).equals(\"null\")) {\n            System.out.println(\"true\");\n            return;\n        }\n\n        TreeNode root = new TreeNode(Integer.parseInt(tokens.get(0)));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < tokens.size()) {\n            TreeNode node = q.poll();\n            if (i < tokens.size()) {\n                String val = tokens.get(i++);\n                if (!val.equals(\"null\")) {\n                    node.left = new TreeNode(Integer.parseInt(val));\n                    q.add(node.left);\n                }\n            }\n            if (i < tokens.size()) {\n                String val = tokens.get(i++);\n                if (!val.equals(\"null\")) {\n                    node.right = new TreeNode(Integer.parseInt(val));\n                    q.add(node.right);\n                }\n            }\n        }\n        System.out.println(new Solution().isValidBST(root));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val)\n    this.left = (left===undefined ? null : left)\n    this.right = (right===undefined ? null : right)\n}\n\n/**\n * @param {TreeNode} root\n * @return {boolean}\n */\nvar isValidBST = function(root) {\n    // User Logic Here\n    return true;\n};\n\nfunction buildTree(input) {\n    const tokens = input.match(/null|-?\\d+/g);\n    if (!tokens || tokens[0] === 'null') return null;\n    const root = new TreeNode(parseInt(tokens[0]));\n    const queue = [root];\n    let i = 1;\n    while (queue.length && i < tokens.length) {\n        const node = queue.shift();\n        if (i < tokens.length) {\n            const val = tokens[i++];\n            if (val !== 'null') {\n                node.left = new TreeNode(parseInt(val));\n                queue.push(node.left);\n            }\n        }\n        if (i < tokens.length) {\n            const val = tokens[i++];\n            if (val !== 'null') {\n                node.right = new TreeNode(parseInt(val));\n                queue.push(node.right);\n            }\n        }\n    }\n    return root;\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const root = buildTree(input);\n    console.log(isValidBST(root).toString());\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nbool isValidBST(struct TreeNode* root) {\n    // User Logic Here\n    return true;\n}\n\nstruct TreeNode* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = atoi(val);\n    node->left = node->right = NULL;\n    return node;\n}\n\nint main() {\n    char input[4000];\n    if (!fgets(input, 4000, stdin)) return 0;\n    char* tokens[500];\n    int count = 0;\n    char* t = strtok(input, \" ,[]\\n\\r\\t\");\n    while (t) {\n        tokens[count++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\\t\");\n    }\n    if (count == 0 || strcmp(tokens[0], \"null\") == 0) {\n        printf(\"true\\n\");\n        return 0;\n    }\n    struct TreeNode* root = createNode(tokens[0]);\n    struct TreeNode* queue[500];\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < count) {\n        struct TreeNode* node = queue[head++];\n        if (i < count) {\n            struct TreeNode* left = createNode(tokens[i++]);\n            if (left) { node->left = left; queue[tail++] = left; }\n        }\n        if (i < count) {\n            struct TreeNode* right = createNode(tokens[i++]);\n            if (right) { node->right = right; queue[tail++] = right; }\n        }\n    }\n    printf(\"%s\\n\", isValidBST(root) ? \"true\" : \"false\");\n    return 0;\n}"
    }
    

    def _solve(vals):
        if not vals or vals[0] == "null": return True
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
            
        def validate(node, low, high):
            if not node: return True
            if not (low < node.val < high): return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, -float('inf'), float('inf'))

    test_cases = [
        {"input": "2 1 3", "expected_output": "true", "is_sample": True},
        {"input": "5 1 4 null null 3 6", "expected_output": "false", "is_sample": True},
        {"input": "1 1", "expected_output": "false", "is_sample": False},
        {"input": "2 2 2", "expected_output": "false", "is_sample": False},
        {"input": "10 5 15 null null 6 20", "expected_output": "false", "is_sample": False},
        {"input": "2147483647", "expected_output": "true", "is_sample": False},
        {"input": "-2147483648 null 2147483647", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(100))), "expected_output": "false", "is_sample": False},
        {"input": "25 null 30", "expected_output": "true", "is_sample": False},
        {"input": " ".join([str(i) if i%2==0 else "null" for i in range(100)]), "expected_output": "false", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Search Tree", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "1-200/98_Validate_Binary_Search_Tree.json"
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
