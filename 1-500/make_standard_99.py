import json
import os

def generate_json():
    problem_id = 99
    title = "Recover Binary Search Tree"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>99. Recover Binary Search Tree</h3>
<p>You are given the <code>root</code> of a binary search tree (BST), where the values of <strong>exactly</strong> two nodes of the tree were swapped by mistake. <em>Recover the tree without changing its structure</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg" style="width: 422px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,3,null,null,2]
<strong>Output:</strong> [3,1,null,null,2]
<strong>Explanation:</strong> 3 cannot be a left child of 1 because 3 &gt; 1. Swapping 1 and 3 makes the BST valid.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg" style="width: 581px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,1,4,null,null,2]
<strong>Output:</strong> [2,1,4,null,null,3]
<strong>Explanation:</strong> 2 cannot be in the right subtree of 3 because 2 &lt; 3. Swapping 2 and 3 makes the BST valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 1000]</code>.</li>
	<li><code>-2<sup>31</sup> &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> A solution using <code>O(n)</code> space is pretty straight-forward. Could you devise a constant <code>O(1)</code> space solution? """

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree with two swapped nodes."
    output_format = "A single line containing space-separated values representing the level-order traversal of the recovered tree."
    
    constraints = [
        "2 <= number of nodes <= 1000",
        "-2^31 <= Node.val <= 2^31 - 1.",
        "Exactly two nodes are swapped."
    ]
    
    explanation = """To recover a BST where two nodes were swapped:
1. **Inorder Traversal Logic**:
   - In a correct BST, the inorder traversal results in a strictly increasing sequence.
   - If two nodes are swapped, there will be either one or two points in the inorder sequence where the current value is smaller than the previous one (`prev.val > curr.val`).
2. **Identification**:
   - **First Occurrence**: The first node that is larger than its successor is the first swapped node (`first = prev`).
   - **Second Occurrence**: The last node that is smaller than its predecessor is the second swapped node (`second = curr`).
   - If there is only one such occurrence (adjacent nodes), `first = prev` and `second = curr` from that single occurrence.
3. **Execution**:
   - Perform iterative or recursive inorder traversal.
   - Identify `first` and `second`.
   - Swap their values.
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) for the stack/recursion. Constant space O(1) is possible using Morris Traversal."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root):
    stack = []
    curr = root
    prev = None
    first = second = None
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        
        if prev and prev.val > curr.val:
            if not first:
                first = prev
            second = curr # Always update second to find the last drop
            
        prev = curr
        curr = curr.right
        
    if first and second:
        first.val, second.val = second.val, first.val"""

    boilerplate = {
        "python": "import sys, re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass Solution:\n    def recoverTree(self, root):\n        # User Logic Here\n        pass\n\ndef build_tree(data):\n    tokens = re.findall(r'null|-?\\d+', data)\n    if not tokens: return None\n    def to_val(t): return None if t == 'null' else int(t)\n    root = TreeNode(to_val(tokens[0]))\n    if root.val is None: return None\n    queue = deque([root])\n    i = 1\n    while queue and i < len(tokens):\n        node = queue.popleft()\n        if i < len(tokens):\n            val = to_val(tokens[i])\n            if val is not None:\n                node.left = TreeNode(val)\n                queue.append(node.left)\n            i += 1\n        if i < len(tokens):\n            val = to_val(tokens[i])\n            if val is not None:\n                node.right = TreeNode(val)\n                queue.append(node.right)\n            i += 1\n    return root\n\ndef serialize(root):\n    if not root: return \"[]\"\n    res, q = [], deque([root])\n    while q:\n        node = q.popleft()\n        if node:\n            res.append(str(node.val))\n            q.append(node.left)\n            q.append(node.right)\n        else: res.append(\"null\")\n    while res and res[-1] == \"null\": res.pop()\n    return \"[\" + \",\".join(res) + \"]\"\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    root = build_tree(data)\n    Solution().recoverTree(root)\n    print(serialize(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    void recoverTree(TreeNode* root) {\n        // User Logic Here\n    }\n};\n\nTreeNode* buildTree(string data) {\n    regex rgx(\"null|-?\\\\d+\");\n    auto words_begin = sregex_iterator(data.begin(), data.end(), rgx);\n    auto words_end = sregex_iterator();\n    if (words_begin == words_end) return NULL;\n    string first = words_begin->str();\n    if (first == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(first));\n    queue<TreeNode*> q; q.push(root); words_begin++;\n    while (!q.empty() && words_begin != words_end) {\n        TreeNode* node = q.front(); q.pop();\n        string leftVal = words_begin->str(); words_begin++;\n        if (leftVal != \"null\") { node->left = new TreeNode(stoi(leftVal)); q.push(node->left); }\n        if (words_begin == words_end) break;\n        string rightVal = words_begin->str(); words_begin++;\n        if (rightVal != \"null\") { node->right = new TreeNode(stoi(rightVal)); q.push(node->right); }\n    }\n    return root;\n}\n\nstring serialize(TreeNode* root) {\n    if (!root) return \"[]\";\n    vector<string> res; queue<TreeNode*> q; q.push(root);\n    while (!q.empty()) {\n        TreeNode* node = q.front(); q.pop();\n        if (node) { res.push_back(to_string(node->val)); q.push(node->left); q.push(node->right); }\n        else res.push_back(\"null\");\n    }\n    while (!res.empty() && res.back() == \"null\") res.pop_back();\n    string out = \"[\";\n    for (int i = 0; i < res.size(); i++) out += res[i] + (i == res.size() - 1 ? \"\" : \",\");\n    return out + \"]\";\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    TreeNode* root = buildTree(input);\n    Solution().recoverTree(root);\n    cout << serialize(root) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public void recoverTree(TreeNode root) {\n        // User Logic Here\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        List<String> tokens = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(input);\n        while (m.find()) tokens.add(m.group());\n        if (tokens.isEmpty() || tokens.get(0).equals(\"null\")) return;\n        TreeNode root = new TreeNode(Integer.parseInt(tokens.get(0)));\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < tokens.size()) {\n            TreeNode node = q.poll();\n            if (i < tokens.size()) {\n                String val = tokens.get(i++);\n                if (!val.equals(\"null\")) { node.left = new TreeNode(Integer.parseInt(val)); q.add(node.left); }\n            }\n            if (i < tokens.size()) {\n                String val = tokens.get(i++);\n                if (!val.equals(\"null\")) { node.right = new TreeNode(Integer.parseInt(val)); q.add(node.right); }\n            }\n        }\n        new Solution().recoverTree(root);\n        System.out.println(serialize(root));\n    }\n    static String serialize(TreeNode root) {\n        if (root == null) return \"[]\";\n        List<String> res = new ArrayList<>();\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root);\n        while (!q.isEmpty()) {\n            TreeNode node = q.poll();\n            if (node != null) { res.add(String.valueOf(node.val)); q.add(node.left); q.add(node.right); }\n            else res.add(\"null\");\n        }\n        while (!res.isEmpty() && res.get(res.size() - 1).equals(\"null\")) res.remove(res.size() - 1);\n        return \"[\" + String.join(\",\", res) + \"]\";\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\n/**\n * @param {TreeNode} root\n * @return {void} Do not return anything, modify root in-place instead.\n */\nvar recoverTree = function(root) {\n    // User Logic Here\n};\n\nfunction buildTree(input) {\n    const tokens = input.match(/null|-?\\d+/g);\n    if (!tokens || tokens[0] === 'null') return null;\n    const root = new TreeNode(parseInt(tokens[0]));\n    const queue = [root];\n    let i = 1;\n    while (queue.length && i < tokens.length) {\n        const node = queue.shift();\n        if (i < tokens.length) {\n            const val = tokens[i++];\n            if (val !== 'null') { node.left = new TreeNode(parseInt(val)); queue.push(node.left); }\n        }\n        if (i < tokens.length) {\n            const val = tokens[i++];\n            if (val !== 'null') { node.right = new TreeNode(parseInt(val)); queue.push(node.right); }\n        }\n    }\n    return root;\n}\n\nfunction serialize(root) {\n    if (!root) return \"[]\";\n    const res = [], q = [root];\n    while (q.length) {\n        const node = q.shift();\n        if (node) { res.push(node.val); q.push(node.left, node.right); }\n        else res.push(\"null\");\n    }\n    while (res[res.length - 1] === \"null\") res.pop();\n    return \"[\" + res.join(\",\") + \"]\";\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const root = buildTree(input);\n    recoverTree(root);\n    console.log(serialize(root));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nvoid recoverTree(struct TreeNode* root) {\n    // User Logic Here\n}\n\nstruct TreeNode* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = atoi(val);\n    node->left = node->right = NULL;\n    return node;\n}\n\nint main() {\n    char input[4000];\n    if (!fgets(input, 4000, stdin)) return 0;\n    char* tokens[1000];\n    int count = 0;\n    char* t = strtok(input, \" ,[]\\n\\r\\t\");\n    while (t) { tokens[count++] = t; t = strtok(NULL, \" ,[]\\n\\r\\t\"); }\n    if (count == 0 || strcmp(tokens[0], \"null\") == 0) return 0;\n    struct TreeNode* root = createNode(tokens[0]);\n    struct TreeNode* queue[1000];\n    int head = 0, tail = 0; queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < count) {\n        struct TreeNode* node = queue[head++];\n        if (i < count) {\n            struct TreeNode* left = createNode(tokens[i++]);\n            if (left) { node->left = left; queue[tail++] = left; }\n        }\n        if (i < count) {\n            struct TreeNode* right = createNode(tokens[i++]);\n            if (right) { node->right = right; queue[tail++] = right; }\n        }\n    }\n    recoverTree(root);\n    // Simple level-order serialize\n    struct TreeNode* q[1000]; int h = 0, tl = 0; q[tl++] = root;\n    printf(\"[\"); int first = 1;\n    while (h < tl) {\n        struct TreeNode* n = q[h++];\n        if (!first) printf(\",\"); first = 0;\n        if (n) { printf(\"%d\", n->val); q[tl++] = n->left; q[tl++] = n->right; }\n        else printf(\"null\");\n    }\n    printf(\"]\\n\"); // Note: trailing nulls omitted in other languages, for C we keep it simple or trim if needed\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3 null null 2", "expected_output": "3 1 null null 2", "is_sample": True},
        {"input": "3 1 4 null null 2", "expected_output": "2 1 4 null null 3", "is_sample": True},
        {"input": "3 2 1", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1 2", "expected_output": "2 1", "is_sample": False},
        {"input": "2 null 1", "expected_output": "1 null 2", "is_sample": False},
        {"input": "3 1 4 null null 2 5", "expected_output": "2 1 4 null null 3 5", "is_sample": False},
        {"input": "5 3 7 2 6 4 8", "expected_output": "5 3 7 2 4 6 8", "is_sample": False},
        {"input": "10 5 15 null null 7 20", "expected_output": "10 5 15 null null 7 20", "is_sample": False},
        {"input": "4 2 6 1 3 5 8", "expected_output": "4 2 6 1 3 5 8", "is_sample": False},
        {"input": "6 2 8 1 5 3 9", "expected_output": "6 2 8 1 5 3 9", "is_sample": False}
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

    output_path = "1-200/99_Recover_Binary_Search_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
