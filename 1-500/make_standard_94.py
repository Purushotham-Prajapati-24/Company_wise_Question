import json
import os

def generate_json():
    problem_id = 94
    title = "Binary Tree Inorder Traversal"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>94. Binary Tree Inorder Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the inorder traversal of its nodes' values</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 322px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively? """

    input_format = "A single line containing space-separated values representing the level-order traversal of the tree (integers or 'null' for empty nodes)."
    output_format = "A single line containing space-separated integers representing the inorder traversal of the tree."
    
    constraints = [
        "0 <= number of nodes <= 100",
        "-100 <= Node.val <= 100."
    ]
    
    explanation = """To perform an inorder traversal (Left -> Visit -> Right) of a binary tree:
1. **Recursive Approach**:
   - Base Case: If node is null, return.
   - Recursive Step:
     - `dfs(node.left)`
     - Add `node.val` to result list.
     - `dfs(node.right)`
2. **Iterative Approach (using a Stack)**:
   - Use a stack to keep track of nodes.
   - Starting from `curr = root`, go as far left as possible, pushing each node onto the stack.
   - Once `curr` becomes null, pop from the stack (this is the next node in inorder).
   - Add the popped node's value to the result.
   - Move `curr` to the popped node's right child and repeat.
3. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(H) where H is the height of the tree (for the recursion stack or explicit stack). In the worst case, O(N)."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
        
    return res"""

    boilerplate = {
        "python": "import sys, re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass Solution:\n    def inorderTraversal(self, root):\n        # User Logic Here\n        return []\n\ndef build_tree(data):\n    # Extract values from [1, null, 2] or 1 null 2\n    tokens = re.findall(r'null|-?\\d+', data)\n    if not tokens: return None\n    def to_val(t): return None if t == 'null' else int(t)\n    root = TreeNode(to_val(tokens[0]))\n    if root.val is None: return None\n    queue = deque([root])\n    i = 1\n    while queue and i < len(tokens):\n        node = queue.popleft()\n        if i < len(tokens):\n            val = to_val(tokens[i])\n            if val is not None:\n                node.left = TreeNode(val)\n                queue.append(node.left)\n            i += 1\n        if i < len(tokens):\n            val = to_val(tokens[i])\n            if val is not None:\n                node.right = TreeNode(val)\n                queue.append(node.right)\n            i += 1\n    return root\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    root = build_tree(data)\n    sol = Solution()\n    print(sol.inorderTraversal(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    vector<int> inorderTraversal(TreeNode* root) {\n        // User Logic Here\n        return {};\n    }\n};\n\nTreeNode* buildTree(string data) {\n    regex rgx(\"null|-?\\\\d+\");\n    auto words_begin = sregex_iterator(data.begin(), data.end(), rgx);\n    auto words_end = sregex_iterator();\n    if (words_begin == words_end) return NULL;\n    \n    string first = words_begin->str();\n    if (first == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(first));\n    queue<TreeNode*> q;\n    q.push(root);\n    words_begin++;\n\n    while (!q.empty() && words_begin != words_end) {\n        TreeNode* node = q.front(); q.pop();\n        \n        string leftVal = words_begin->str();\n        words_begin++;\n        if (leftVal != \"null\") {\n            node->left = new TreeNode(stoi(leftVal));\n            q.push(node->left);\n        }\n        \n        if (words_begin == words_end) break;\n        string rightVal = words_begin->str();\n        words_begin++;\n        if (rightVal != \"null\") {\n            node->right = new TreeNode(stoi(rightVal));\n            q.push(node->right);\n        }\n    }\n    return root;\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    TreeNode* root = buildTree(input);\n    Solution sol;\n    vector<int> res = sol.inorderTraversal(root);\n    cout << \"[\";\n    for(int i=0; i<res.size(); ++i) cout << res[i] << (i==res.size()-1 ? \"\" : \",\");\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public List<Integer> inorderTraversal(TreeNode root) {\n        // User Logic Here\n        return new ArrayList<>();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        List<String> tokens = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(input);\n        while (m.find()) tokens.add(m.group());\n        \n        if (tokens.isEmpty() || tokens.get(0).equals(\"null\")) {\n            System.out.println(\"[]\");\n            return;\n        }\n\n        TreeNode root = new TreeNode(Integer.parseInt(tokens.get(0)));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < tokens.size()) {\n            TreeNode node = q.poll();\n            if (i < tokens.size()) {\n                String val = tokens.get(i++);\n                if (!val.equals(\"null\")) {\n                    node.left = new TreeNode(Integer.parseInt(val));\n                    q.add(node.left);\n                }\n            }\n            if (i < tokens.size()) {\n                String val = tokens.get(i++);\n                if (!val.equals(\"null\")) {\n                    node.right = new TreeNode(Integer.parseInt(val));\n                    q.add(node.right);\n                }\n            }\n        }\n        System.out.println(new Solution().inorderTraversal(root));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val)\n    this.left = (left===undefined ? null : left)\n    this.right = (right===undefined ? null : right)\n}\n\n/**\n * @param {TreeNode} root\n * @return {number[]}\n */\nvar inorderTraversal = function(root) {\n    // User Logic Here\n    return [];\n};\n\nfunction buildTree(input) {\n    const tokens = input.match(/null|-?\\d+/g);\n    if (!tokens || tokens[0] === 'null') return null;\n    const root = new TreeNode(parseInt(tokens[0]));\n    const queue = [root];\n    let i = 1;\n    while (queue.length && i < tokens.length) {\n        const node = queue.shift();\n        if (i < tokens.length) {\n            const val = tokens[i++];\n            if (val !== 'null') {\n                node.left = new TreeNode(parseInt(val));\n                queue.push(node.left);\n            }\n        }\n        if (i < tokens.length) {\n            const val = tokens[i++];\n            if (val !== 'null') {\n                node.right = new TreeNode(parseInt(val));\n                queue.push(node.right);\n            }\n        }\n    }\n    return root;\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const root = buildTree(input);\n    console.log(JSON.stringify(inorderTraversal(root)));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\n/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* inorderTraversal(struct TreeNode* root, int* returnSize) {\n    // User Logic Here\n    *returnSize = 0;\n    return NULL;\n}\n\nstruct TreeNode* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = atoi(val);\n    node->left = node->right = NULL;\n    return node;\n}\n\nint main() {\n    char input[4000];\n    if (!fgets(input, 4000, stdin)) return 0;\n    char* tokens[500];\n    int count = 0;\n    char* t = strtok(input, \" ,[]\\n\\r\\t\");\n    while (t) {\n        tokens[count++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\\t\");\n    }\n    if (count == 0 || strcmp(tokens[0], \"null\") == 0) {\n        printf(\"[]\\n\");\n        return 0;\n    }\n    struct TreeNode* root = createNode(tokens[0]);\n    struct TreeNode* queue[500];\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < count) {\n        struct TreeNode* node = queue[head++];\n        if (i < count) {\n            struct TreeNode* left = createNode(tokens[i++]);\n            if (left) { node->left = left; queue[tail++] = left; }\n        }\n        if (i < count) {\n            struct TreeNode* right = createNode(tokens[i++]);\n            if (right) { node->right = right; queue[tail++] = right; }\n        }\n    }\n    int returnSize = 0;\n    int* res = inorderTraversal(root, &returnSize);\n    printf(\"[\");\n    for (int j = 0; j < returnSize; j++) {\n        printf(\"%d\", res[j]);\n        if (j < returnSize - 1) printf(\",\");\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }
    

    def _solve(vals):
        if not vals or vals[0] == "null": return []
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
        
        res = []
        def dfs(n):
            if n:
                dfs(n.left)
                res.append(n.val)
                dfs(n.right)
        dfs(root)
        return res

    sample1 = ["1", "null", "2", "3"]
    test_cases = [
        {"input": " ".join(sample1), "expected_output": " ".join(map(str, _solve(sample1))), "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        {"input": "1 2 3", "expected_output": "2 1 3", "is_sample": False},
        {"input": "1 2 null 3 null 4", "expected_output": "4 3 2 1", "is_sample": False},
        {"input": "1 null 2 null 3 null 4", "expected_output": "1 2 3 4", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "4 2 5 1 6 3 7", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(1, 101))), "expected_output": " ".join(map(str, _solve([str(x) for x in range(1, 101)]))), "is_sample": False},
        {"input": " ".join(["1"] + ["null", "1"]*49), "expected_output": " ".join(["1"]*50), "is_sample": False},
        {"input": " ".join(["1"] + ["1", "null"]*49), "expected_output": " ".join(["1"]*50), "is_sample": False}
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
        "topics": ["Tree", "Stack", "Binary Tree", "Inorder Traversal"],
        "companyIndex": 0
    }

    output_path = "1-200/94_Binary_Tree_Inorder_Traversal.json"
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
