import json
import collections
import os

def generate_json():
    problem_id = 297
    title = "Serialize and Deserialize Binary Tree"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>297. Serialize and Deserialize Binary Tree</h3>
<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p><strong>Clarification:</strong> The input/output format is the same as <a href="https://leetcode.com/faq/#binary-tree" target="_blank">how LeetCode serializes a binary tree</a>. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg" style="width: 442px; height: 324px;" />
<pre><strong>Input:</strong> root = [1,2,3,null,null,4,5]
<strong>Output:</strong> [1,2,3,null,null,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>"""

    input_format = "A stringified array representing a binary tree (root)."
    output_format = "The root of the reconstructed binary tree."
    
    constraints = [
        "0 <= number of nodes <= 10,000",
        "-1000 <= Node.val <= 1000"
    ]
    
    explanation = """To serialize and deserialize a binary tree:
1. **Serialization**: Convert the tree to a string using **Pre-order DFS**.
   - Start from the root.
   - For each node, append its value to the result string.
   - If a node is `None` (null), append a special character (e.g., `#`).
   - Recurse for the left and right children.
2. **Deserialization**: Reconstruct the tree from the string.
   - Split the string into a list of values.
   - Use a pointer or an iterator to consume values one by one.
   - Use the same Pre-order logic: Create a node with the current value, then recurse for left and right children.
   - If the value is `#`, return `None`.
3. **Complexity Analysis**:
   - Time: O(N) for both serialization and deserialization (each node is visited once).
   - Space: O(N) to store the serialized string and the recursion stack."""
    
    answer = """class Codec:
    def serialize(self, root):
        # Pre-order DFS to convert tree to string
        res = []
        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        # Convert string back to tree
        vals = collections.deque(data.split(","))
        
        def build_tree():
            if not vals:
                return None
            val = vals.popleft()
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
            
        return build_tree()"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\nimport re\n\nclass TreeNode:\n    def __init__(self, x):\n        self.val = x\n        self.left = None\n        self.right = None\n\n# User's Code\nclass Codec:\n    def serialize(self, root):\n        # User logic here\n        pass\n\n    def deserialize(self, data):\n        # User logic here\n        pass\n\ndef build_tree(data):\n    if not data or data == '[]': return None\n    vals = data.strip('[]').split(',')\n    if not vals or not vals[0].strip(): return None\n    \n    root = TreeNode(int(vals[0].strip()))\n    queue = collections.deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i].strip() != 'null' and vals[i].strip() != '':\n            node.left = TreeNode(int(vals[i].strip()))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i].strip() != 'null' and vals[i].strip() != '':\n            node.right = TreeNode(int(vals[i].strip()))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef tree_to_list(root):\n    if not root: return []\n    res = []\n    q = collections.deque([root])\n    while q:\n        node = q.popleft()\n        if node:\n            res.append(node.val)\n            q.append(node.left)\n            q.append(node.right)\n        else:\n            res.append(None)\n    while res and res[-1] is None: res.pop()\n    return res\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    match = re.search(r'\\[.*\\]', raw_input)\n    if match:\n        root = build_tree(match.group(0))\n        codec = Codec()\n        serialized = codec.serialize(root)\n        new_root = codec.deserialize(serialized)\n        print(json.dumps(tree_to_list(new_root)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n#include <sstream>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Codec {\npublic:\n    string serialize(TreeNode* root) {\n        // User logic\n        return \"\";\n    }\n    TreeNode* deserialize(string data) {\n        // User logic\n        return NULL;\n    }\n};\n\nTreeNode* buildTree(string data) {\n    if (data == \"[]\" || data == \"\") return NULL;\n    data = data.substr(1, data.length() - 2);\n    stringstream ss(data);\n    string item;\n    vector<string> vals;\n    while (getline(ss, item, ',')) vals.push_back(item);\n    if (vals.empty() || vals[0] == \"null\") return NULL;\n\n    TreeNode* root = new TreeNode(stoi(vals[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < vals.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < vals.size() && vals[i] != \"null\") {\n            curr->left = new TreeNode(stoi(vals[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < vals.size() && vals[i] != \"null\") {\n            curr->right = new TreeNode(stoi(vals[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvoid printTree(TreeNode* root) {\n    if (!root) { cout << \"[]\" << endl; return; }\n    vector<string> res;\n    queue<TreeNode*> q;\n    q.push(root);\n    while (!q.empty()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (curr) {\n            res.push_back(to_string(curr->val));\n            q.push(curr->left);\n            q.push(curr->right);\n        } else res.push_back(\"null\");\n    }\n    while (!res.empty() && res.back() == \"null\") res.pop_back();\n    cout << \"[\";\n    for (int i = 0; i < res.size(); i++) cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n    cout << \"]\" << endl;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line;\n    smatch m;\n    if (regex_search(input, m, regex(R\"(\\[.*\\])\"))) {\n        TreeNode* root = buildTree(m.str());\n        Codec codec;\n        string s = codec.serialize(root);\n        TreeNode* res = codec.deserialize(s);\n        printTree(res);\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        Matcher m = Pattern.compile(\"\\\\[.*\\\\]\").matcher(input);\n        if (m.find()) {\n            TreeNode root = buildTree(m.group());\n            Codec codec = new Codec();\n            String serialized = codec.serialize(root);\n            TreeNode res = codec.deserialize(serialized);\n            System.out.println(treeToList(res));\n        }\n    }\n\n    static TreeNode buildTree(String data) {\n        if (data.equals(\"[]\")) return null;\n        String[] vals = data.substring(1, data.length() - 1).split(\",\");\n        if (vals[0].trim().isEmpty() || vals[0].trim().equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(vals[0].trim()));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < vals.size()) {\n            TreeNode curr = q.poll();\n            if (i < vals.length && !vals[i].trim().equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(vals[i].trim()));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < vals.length && !vals[i].trim().equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(vals[i].trim()));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    static String treeToList(TreeNode root) {\n        if (root == null) return \"[]\";\n        List<String> res = new ArrayList<>();\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        while (!q.isEmpty()) {\n            TreeNode curr = q.poll();\n            if (curr == null) res.add(\"null\");\n            else {\n                res.add(String.valueOf(curr.val));\n                q.add(curr.left);\n                q.add(curr.right);\n            }\n        }\n        while (!res.isEmpty() && res.get(res.size() - 1).equals(\"null\")) res.remove(res.size() - 1);\n        return \"[\" + String.join(\",\", res) + \"]\";\n    }\n}\n\nclass Codec {\n    public String serialize(TreeNode root) { return \"\"; }\n    public TreeNode deserialize(String data) { return null; }\n}",
        "javascript": "const fs = require('fs');\n\nclass TreeNode {\n    constructor(val) {\n        this.val = val;\n        this.left = this.right = null;\n    }\n}\n\n// User Code\nclass Codec {\n    serialize(root) { return \"\"; }\n    deserialize(data) { return null; }\n}\n\nfunction buildTree(data) {\n    if (!data || data === '[]') return null;\n    const vals = data.slice(1, -1).split(',').map(s => s.trim());\n    if (vals[0] === 'null' || vals[0] === '') return null;\n    const root = new TreeNode(parseInt(vals[0]));\n    const q = [root];\n    let i = 1;\n    while (q.length > 0 && i < vals.length) {\n        const curr = q.shift();\n        if (i < vals.length && vals[i] !== 'null') {\n            curr.left = new TreeNode(parseInt(vals[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < vals.length && vals[i] !== 'null') {\n            curr.right = new TreeNode(parseInt(vals[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction treeToList(root) {\n    if (!root) return [];\n    const res = [];\n    const q = [root];\n    while (q.length > 0) {\n        const curr = q.shift();\n        if (curr) {\n            res.push(curr.val);\n            q.push(curr.left);\n            q.push(curr.right);\n        } else res.push(null);\n    }\n    while (res.length > 0 && res[res.length - 1] === null) res.pop();\n    return res;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst match = input.match(/\\[.*\\]/);\nif (match) {\n    const root = buildTree(match[0]);\n    const codec = new Codec();\n    const serialized = codec.serialize(root);\n    const newRoot = codec.deserialize(serialized);\n    console.log(JSON.stringify(treeToList(newRoot)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nchar* serialize(struct TreeNode* root) { return \"\"; }\nstruct TreeNode* deserialize(char* data) { return NULL; }\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,null,null,4,5]", "expected_output": "[1,2,3,null,null,4,5]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,2]", "expected_output": "[1,2]", "is_sample": False},
        {"input": "[1,null,2]", "expected_output": "[1,null,2]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "[1,2,3,4,5,6,7]", "is_sample": False},
        {"input": "[1,2,null,3,null,4]", "expected_output": "[1,2,null,3,null,4]", "is_sample": False},
        # Stress cases
        {"input": "[i for i in range(1000)]", "expected_output": "...", "is_sample": False},
        {"input": "[1]*1000", "expected_output": "...", "is_sample": False},
        {"input": "[-1000]*100", "expected_output": "...", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Design", "String", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "201-400/297_Serialize_and_Deserialize_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
