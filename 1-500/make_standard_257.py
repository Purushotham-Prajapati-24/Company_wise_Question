import json
import os

def generate_json():
    problem_id = 257
    title = "Binary Tree Paths"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>257. Binary Tree Paths</h3>
<p>Given the <code>root</code> of a binary tree, return <em>all root-to-leaf paths in <strong>any order</strong></em>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre><strong>Input:</strong> root = [1,2,3,null,5]
<strong>Output:</strong> ["1-&gt;2-&gt;5","1-&gt;3"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> ["1"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A stringified array representing a binary tree (level-order traversal)."
    output_format = "A stringified array of strings representing paths (e.g., '1->2->5')."
    
    constraints = [
        "1 <= number of nodes <= 100",
        "-100 <= Node.val <= 100"
    ]
    
    explanation = """To find all root-to-leaf paths in a binary tree:
1. **DFS Traversal**: We can use Depth-First Search (DFS) to traverse from the root to every leaf node.
2. **Path Maintenance**: As we traverse through the nodes, we maintain the current path.
3. **Leaf Check**: When a node is reached that has no left or right children (a leaf), we append the current path to the result list.
4. **Complexity Analysis**:
   - Time: O(N) where N is the number of nodes, as we visit each node exactly once.
   - Space: O(H) where H is the height of the tree for the recursion stack (O(N) in worst case for a skewed tree, O(log N) for a balanced tree)."""
    
    answer = """class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
            
        res = []
        
        def dfs(node, path):
            # Form current path string
            curr_path = path + str(node.val)
            
            # If leaf, add to result
            if not node.left and not node.right:
                res.append(curr_path)
                return
                
            # Recurse for children
            if node.left:
                dfs(node.left, curr_path + "->")
            if node.right:
                dfs(node.right, curr_path + "->")
                
        dfs(root, "")
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(vals):\n    if not vals: return None\n    root = TreeNode(vals[0])\n    queue = deque([root])\n    i = 1\n    while i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] is not None:\n            node.left = TreeNode(vals[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] is not None:\n            node.right = TreeNode(vals[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef binaryTreePaths(root):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Extract content inside brackets\n    match = re.search(r'\\[(.*)\\]', raw_input, re.DOTALL)\n    if match:\n        content = match.group(1)\n        # Split by comma and strip whitespace\n        tokens = [t.strip() for t in content.split(',') if t.strip()]\n        vals = [int(t) if t.lower() != 'null' else None for t in tokens]\n        root = build_tree(vals)\n        res = binaryTreePaths(root)\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(const vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvector<string> binaryTreePaths(TreeNode* root) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    smatch m;\n    if (regex_search(input, m, regex(\"\\\\[(.*)\\\\]\"))) {\n        string content = m[1].str();\n        regex re_token(\"[^,\\\\s]+\");\n        auto b = sregex_iterator(content.begin(), content.end(), re_token);\n        auto e = sregex_iterator();\n        vector<string> nodes;\n        for (auto i = b; i != e; ++i) nodes.push_back(i->str());\n        \n        vector<string> res = binaryTreePaths(buildTree(nodes));\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << \"\\\"\" << res[i] << \"\\\"\" << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public List<String> binaryTreePaths(TreeNode root) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        Matcher m = Pattern.compile(\"\\\\[(.*)\\\\]\").matcher(input);\n        if (m.find()) {\n            String content = m.group(1);\n            String[] tokens = content.split(\",\");\n            List<String> nodes = new ArrayList<>();\n            for (String t : tokens) {\n                String trimmed = t.trim();\n                if (!trimmed.isEmpty()) nodes.add(trimmed);\n            }\n            TreeNode root = buildTree(nodes);\n            List<String> res = new Solution().binaryTreePaths(root);\n            StringBuilder resSb = new StringBuilder(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                resSb.append(\"\\\"\").append(res.get(i)).append(\"\\\"\").append(i == res.size() - 1 ? \"\" : \",\");\n            }\n            resSb.append(\"]\");\n            System.out.println(resSb.toString());\n        }\n    }\n\n    static TreeNode buildTree(List<String> nodes) {\n        if (nodes.isEmpty() || nodes.get(0).equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(nodes.get(0)));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.size()) {\n            TreeNode curr = q.poll();\n            if (i < nodes.size() && !nodes.get(i).equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes.get(i)));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < nodes.size() && !nodes.get(i).equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes.get(i)));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val, left, right) {\n    this.val = (val===undefined ? 0 : val);\n    this.left = (left===undefined ? null : left);\n    this.right = (right===undefined ? null : right);\n}\n\nfunction buildTree(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]);\n    let q = [root];\n    let i = 1;\n    while (q.length && i < arr.length) {\n        let curr = q.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            q.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction binaryTreePaths(root) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst match = input.match(/\\[(.*?)\\]/s);\nif (match) {\n    const content = match[1];\n    const tokens = content.split(',').map(t => t.trim()).filter(t => t.length > 0);\n    const arr = tokens.map(t => t.toLowerCase() === 'null' ? null : parseInt(t));\n    console.log(JSON.stringify(binaryTreePaths(buildTree(arr))));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nchar** binaryTreePaths(struct TreeNode* root, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nstruct TreeNode* buildTree(char** nodes, int size) {\n    if (size == 0 || strcmp(nodes[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    root->val = atoi(nodes[0]);\n    root->left = root->right = NULL;\n    struct TreeNode** queue = (struct TreeNode**)malloc(size * sizeof(struct TreeNode*));\n    int head = 0, tail = 0;\n    queue[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = queue[head++];\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->left->val = atoi(nodes[i]);\n            curr->left->left = curr->left->right = NULL;\n            queue[tail++] = curr->left;\n        }\n        i++;\n        if (i < size && strcmp(nodes[i], \"null\") != 0) {\n            curr->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            curr->right->val = atoi(nodes[i]);\n            curr->right->left = curr->right->right = NULL;\n            queue[tail++] = curr->right;\n        }\n        i++;\n    }\n    free(queue);\n    return root;\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    char* start = strchr(buffer, '[');\n    char* end = strrchr(buffer, ']');\n    if (start && end && end > start) {\n        *end = '\\0';\n        char* content = start + 1;\n        char** nodes = (char**)malloc(10000 * sizeof(char*));\n        int size = 0;\n        char* token = strtok(content, \",\");\n        while (token) {\n            while (*token && isspace(*token)) token++;\n            char* e = token + strlen(token) - 1;\n            while (e > token && isspace(*e)) { *e = '\\0'; e--; }\n            if (*token) nodes[size++] = strdup(token);\n            token = strtok(NULL, \",\");\n        }\n        int returnSize = 0;\n        char** res = binaryTreePaths(buildTree(nodes, size), &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\"%s\\\"%s\", res[i], i == returnSize - 1 ? \"\" : \",\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree(vals):
        if not vals: return None
        root = TreeNode(vals[0])
        from collections import deque
        queue = deque([root])
        i = 1
        while i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root

    def binaryTreePaths(root):
        if not root: return []
        res = []
        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            if node.left: dfs(node.left, path + str(node.val) + "->")
            if node.right: dfs(node.right, path + str(node.val) + "->")
        dfs(root, "")
        return res

    raw_inputs = [
        "[1,2,3,null,5]",
        "[1]",
        "[1,2]",
        "[1,null,3]",
        "[1,2,3,4,5,6,7]",
        "[1,2,3,4,null,null,null,5]",
        "[1,2,null,3,null,4,null,5]",
        "[" + ",".join(str(i) for i in range(1, 101)) + "]",
        "[" + ",".join("1" if i == 0 else "null" for i in range(2**10 - 1)) + "]",
        "[" + ",".join(str(i) if i % 2 == 1 else "null" for i in range(1, 201)) + "]"
    ]

    test_cases = []
    for i, inp in enumerate(raw_inputs):
        try:
            arr = json.loads(inp)
        except:
            arr = [int(x) if x != 'null' else None for x in inp.replace('[', '').replace(']', '').replace(',', ' ').split()]
        root = build_tree(arr)
        out = binaryTreePaths(root)
        test_cases.append({
            "input": inp,
            "expected_output": json.dumps(out).replace(' ', ''),
            "is_sample": i < 2
        })

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
        "topics": ["Tree", "Depth-First Search", "Binary Tree", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "201-400/257_Binary_Tree_Paths.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
