import json
import os

def generate_json():
    problem_id = 113
    title = "Path Sum II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>113. Path Sum II</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>all <strong>root-to-leaf</strong> paths where the sum of the node values in the path equals </em><code>targetSum</code><em>. Each path should be returned as a list of the node values, not node references</em>.</p>
<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;" />
<pre>
<strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>Output:</strong> [[5,4,11,2],[5,8,4,5]]
<strong>Explanation:</strong> There are two paths whose sum equals targetSum:
5 -&gt; 4 -&gt; 11 -&gt; 2 = 22
5 -&gt; 8 -&gt; 4 -&gt; 5 = 22
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;" />
<pre>
<strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> root = [1,2], targetSum = 0
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>"""

    input_format = "Line 1: space-separated level-order traversal of the tree (integers or 'null'). Line 2: An integer representing targetSum."
    output_format = "A JSON formatted list of all root-to-leaf paths that sum to targetSum."
    
    constraints = [
        "0 <= number of nodes <= 5000",
        "-1000 <= Node.val <= 1000",
        "-1000 <= targetSum <= 1000."
    ]
    
    explanation = """To find all root-to-leaf paths with a specific sum:
1. **DFS with Backtracking**:
   - Traverse the tree from root to leaf using Depth-First Search.
   - Maintain a `current_path` list to store values of nodes visited during the current recursion.
   - At each node:
     - Add the node's value to `current_path`.
     - **Base Case**: If the node is a **leaf** and `node.val` equals the remaining `targetSum`, add a copy of `current_path` to the final `results` list.
     - **Recursive Step**: Recursively call DFS on left and right children with updated `targetSum - node.val`.
     - **Backtrack**: After exploring both children, remove the current node's value from `current_path` to restore the state for the parent.
2. **Efficiency**:
   - This approach visits each node once (O(N)).
   - Backtracking ensures we don't create unnecessary copies of the path except when a valid path is found.
3. **Complexity**:
   - Time Complexity: O(N^2) in the worst case (a full tree where every path is a match, requiring O(N) to copy each O(log N) path). More typically O(N).
   - Space Complexity: O(H) where H is the height of the tree for recursion and path storage."""
    
    answer = """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    res = []
    
    def dfs(node, currentSum, path):
        if not node:
            return
            
        path.append(node.val)
        
        # Check if it's a leaf
        if not node.left and not node.right:
            if node.val == currentSum:
                res.append(list(path))
        else:
            dfs(node.left, currentSum - node.val, path)
            dfs(node.right, currentSum - node.val, path)
            
        # Backtrack
        path.pop()
        
    dfs(root, targetSum, [])
    return res"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data or data[0] == 'null': return None\n    root = TreeNode(int(data[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(data):\n        node = queue.popleft()\n        if i < len(data) and data[i] != 'null':\n            node.left = TreeNode(int(data[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] != 'null':\n            node.right = TreeNode(int(data[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef pathSum(root, targetSum):\n    # User logic here\n    return []\n\nif __name__ == \"__main__\":\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        tree_tokens = re.findall(r'null|-?\\d+', lines[0])\n        target_match = re.search(r'-?\\d+', lines[1])\n        if target_match:\n            target = int(target_match.group())\n            root = build_tree(tree_tokens)\n            print(json.dumps(pathSum(root, target)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left;\n    TreeNode *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& data) {\n    if (data.empty() || data[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(data[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < data.size()) {\n        TreeNode* curr = q.front();\n        q.pop();\n        if (i < data.size() && data[i] != \"null\") {\n            curr->left = new TreeNode(stoi(data[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < data.size() && data[i] != \"null\") {\n            curr->right = new TreeNode(stoi(data[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvector<vector<int>> pathSum(TreeNode* root, int targetSum) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line1, line2;\n    if (!getline(cin, line1)) return 0;\n    if (!getline(cin, line2)) return 0;\n    regex re_tree(\"null|-?\\\\d+\");\n    vector<string> tree_tokens;\n    for (sregex_iterator it(line1.begin(), line1.end(), re_tree), end; it != end; ++it) tree_tokens.push_back(it->str());\n    TreeNode* root = buildTree(tree_tokens);\n    regex re_val(\"-?\\\\d+\");\n    smatch m;\n    int target = 0;\n    if (regex_search(line2, m, re_val)) target = stoi(m.str());\n    vector<vector<int>> res = pathSum(root, target);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); j++) {\n            cout << res[i][j] << (j + 1 < (int)res[i].size() ? \", \" : \"\");\n        }\n        cout << \"]\" << (i + 1 < (int)res.size() ? \", \" : \"\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left;\n    TreeNode right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static TreeNode buildTree(String[] data) {\n        if (data.length == 0 || data[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(data[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < data.length) {\n            TreeNode curr = q.poll();\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(data[i]));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < data.length && !data[i].equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(data[i]));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n\n    public static List<List<Integer>> pathSum(TreeNode root, int targetSum) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine();\n        if (!sc.hasNextLine()) return;\n        String line2 = sc.nextLine();\n        List<String> treeTokens = new ArrayList<>();\n        Matcher m1 = Pattern.compile(\"null|-?\\\\d+\").matcher(line1);\n        while (m1.find()) treeTokens.add(m1.group());\n        TreeNode root = buildTree(treeTokens.toArray(new String[0]));\n        Matcher m2 = Pattern.compile(\"-?\\\\d+\").matcher(line2);\n        int target = 0;\n        if (m2.find()) target = Integer.parseInt(m2.group());\n        List<List<Integer>> res = pathSum(root, target);\n        System.out.println(res.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass TreeNode {\n    constructor(val = 0, left = null, right = null) {\n        this.val = val;\n        this.left = left;\n        this.right = right;\n    }\n}\n\nfunction buildTree(data) {\n    if (!data.length || data[0] === 'null') return null;\n    let root = new TreeNode(parseInt(data[0]));\n    let q = [root];\n    let i = 1;\n    while (q.length && i < data.length) {\n        let curr = q.shift();\n        if (i < data.length && data[i] !== 'null') {\n            curr.left = new TreeNode(parseInt(data[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < data.length && data[i] !== 'null') {\n            curr.right = new TreeNode(parseInt(data[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction pathSum(root, targetSum) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const treeTokens = input[0].match(/null|-?\\d+/g) || [];\n    const targetMatch = input[1].match(/-?\\d+/);\n    if (targetMatch) {\n        const target = parseInt(targetMatch[0]);\n        const root = buildTree(treeTokens);\n        console.log(JSON.stringify(pathSum(root, target)));\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left;\n    struct TreeNode *right;\n};\n\nstruct TreeNode* createNode(char* val) {\n    if (strcmp(val, \"null\") == 0) return NULL;\n    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n    node->val = atoi(val);\n    node->left = node->right = NULL;\n    return node;\n}\n\nstruct TreeNode* buildTree(char** data, int size) {\n    if (size == 0 || strcmp(data[0], \"null\") == 0) return NULL;\n    struct TreeNode* root = createNode(data[0]);\n    struct TreeNode* q[10000];\n    int head = 0, tail = 0;\n    q[tail++] = root;\n    int i = 1;\n    while (head < tail && i < size) {\n        struct TreeNode* curr = q[head++];\n        if (i < size) {\n            curr->left = createNode(data[i]);\n            if (curr->left) q[tail++] = curr->left;\n            i++;\n        }\n        if (i < size) {\n            curr->right = createNode(data[i]);\n            if (curr->right) q[tail++] = curr->right;\n            i++;\n        }\n    }\n    return root;\n}\n\nint** pathSum(struct TreeNode* root, int targetSum, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    char line1[100000], line2[1000];\n    if (!fgets(line1, sizeof(line1), stdin)) return 0;\n    if (!fgets(line2, sizeof(line2), stdin)) return 0;\n    char* data[10000];\n    int size = 0;\n    char* t = strtok(line1, \" ,[]\\n\\r\");\n    while (t) {\n        data[size++] = t;\n        t = strtok(NULL, \" ,[]\\n\\r\");\n    }\n    struct TreeNode* root = buildTree(data, size);\n    int target = atoi(line2);\n    int returnSize = 0;\n    int* returnColumnSizes = NULL;\n    int** res = pathSum(root, target, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[\");\n        for (int j = 0; j < returnColumnSizes[i]; j++) {\n            printf(\"%d%s\", res[i][j], (j + 1 < returnColumnSizes[i] ? \", \" : \"\"));\n        }\n        printf(\"]%s\", (i + 1 < returnSize ? \", \" : \"\"));\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    def _solve(vals, target):
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
        def dfs(n, s, p):
            if not n: return
            p.append(n.val)
            if not n.left and not n.right:
                if n.val == s: res.append(list(p))
            else:
                dfs(n.left, s - n.val, p)
                dfs(n.right, s - n.val, p)
            p.pop()
        dfs(root, target, [])
        return res

    test_cases = [
        {"input": "5 4 8 11 null 13 4 7 2 null null 5 1\n22", "expected_output": "[[5, 4, 11, 2], [5, 8, 4, 5]]", "is_sample": True},
        {"input": "1 2 3\n5", "expected_output": "[]", "is_sample": True},
        {"input": "1 2\n1", "expected_output": "[]", "is_sample": False},
        {"input": "1 2\n3", "expected_output": "[[1, 2]]", "is_sample": False},
        {"input": "1 2 2\n3", "expected_output": "[[1, 2], [1, 2]]", "is_sample": False},
        {"input": "1\n1", "expected_output": "[[1]]", "is_sample": False},
        {"input": "1 2 3\n4", "expected_output": "[[1, 3]]", "is_sample": False},
        # Stress cases
        {"input": " ".join(["0"]*15) + "\n0", "expected_output": str(_solve(["0"]*15, 0)), "is_sample": False},
        {"input": " ".join(["1"]*50) + "\n100", "expected_output": "[]", "is_sample": False},
        {"input": "1 " + "null 1 "*50 + "\n51", "expected_output": "[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Binary Tree", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "1-200/113_Path_Sum_II.json"
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
