import json
import collections
import os

def generate_json():
    problem_id = 314
    title = "Binary Tree Vertical Order Traversal"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>314. Binary Tree Vertical Order Traversal</h3>
<p>Given the <code>root</code> of a binary tree, return <strong>the vertical order traversal</strong> of its nodes' values. (i.e., from top to bottom, column by column).</p>

<p>If two nodes are in the same row and column, the order should be from <strong>left to right</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/vtree1.jpg" style="width: 282px; height: 301px;" />
<pre><strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3],[15,20],[7]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/vtree2-1.jpg" style="width: 462px; height: 222px;" />
<pre><strong>Input:</strong> root = [3,9,8,4,0,1,7]
<strong>Output:</strong> [[4],[9],[3,0,1],[8],[7]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/vtree2.jpg" style="width: 462px; height: 302px;" />
<pre><strong>Input:</strong> root = [3,9,8,4,0,1,7,null,null,null,2,5]
<strong>Output:</strong> [[4],[9,5],[3,0,1],[8,2],[7]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A root of a binary tree represented as an array."
    output_format = "A list of lists of integers representing nodes' values column by column."
    
    constraints = [
        "0 <= number of nodes <= 100",
        "-100 <= Node.val <= 100"
    ]
    
    explanation = """To perform vertical order traversal:
1. **BFS with Column Tracking**:
   - Use a queue for BFS level-order traversal. Each item in the queue is a tuple `(node, column)`.
   - The root starts at `column = 0`.
   - When moving left, `column -= 1`.
   - When moving right, `column += 1`.
2. **Grouping by Column**:
   - Store the values in a hash map where keys are columns and values are lists of node values.
   - Using BFS ensures that nodes at the same column are ordered from top to bottom and, for nodes on the same level, from left to right.
3. **Range**: Keep track of the minimum and maximum column encountered to output results in the correct order.
4. **Complexity Analysis**:
   - Time: O(N) to visit each node. Sorting keys would take O(K log K) where K is number of columns, but since we track min/max, it's O(N).
   - Space: O(N) to store node values in the hash map and the queue."""
    
    answer = """class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        column_map = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        min_col = max_col = 0
        
        while queue:
            node, col = queue.popleft()
            column_map[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
                
        return [column_map[i] for i in range(min_col, max_col + 1)]"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef verticalOrder(root):\n    # User logic here\n    pass\n\ndef build_tree(data):\n    if not data or data[0] is None or data[0] == 'null': return None\n    root = TreeNode(int(data[0]))\n    queue = deque([root])\n    i = 1\n    while queue and i < len(data):\n        node = queue.popleft()\n        if i < len(data) and data[i] is not None and data[i] != 'null':\n            node.left = TreeNode(int(data[i]))\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] is not None and data[i] != 'null':\n            node.right = TreeNode(int(data[i]))\n            queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    # Lethal extraction: handles both [1,2,null] and 1 2 null formats\n    data = re.split(r'[\\s,]+', raw_input.strip('[]'))\n    root = build_tree(data)\n    print(json.dumps(verticalOrder(root)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n#include <string>\n#include <regex>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nTreeNode* buildTree(vector<string>& vals) {\n    if (vals.empty() || vals[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(vals[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < (int)vals.size()) {\n        TreeNode* node = q.front(); q.pop();\n        if (i < (int)vals.size() && vals[i] != \"null\") {\n            node->left = new TreeNode(stoi(vals[i])); q.push(node->left);\n        } i++;\n        if (i < (int)vals.size() && vals[i] != \"null\") {\n            node->right = new TreeNode(stoi(vals[i])); q.push(node->right);\n        } i++;\n    }\n    return root;\n}\n\nvector<vector<int>> verticalOrder(TreeNode* root) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input, token;\n    while(cin >> token) input += token + \" \";\n    regex re(\"[^\\\\s,\\\\[\\\\]]+\");\n    vector<string> vals;\n    auto begin = sregex_iterator(input.begin(), input.end(), re);\n    for (auto i = begin; i != sregex_iterator(); ++i) vals.push_back((*i).str());\n    \n    TreeNode* root = buildTree(vals);\n    auto res = verticalOrder(root);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        if (i) cout << \",\";\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); j++) {\n            if (j) cout << \",\";\n            cout << res[i][j];\n        }\n        cout << \"]\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }\n\n    static TreeNode buildTree(String[] vals) {\n        if (vals.length == 0 || vals[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < vals.length) {\n            TreeNode node = q.poll();\n            if (i < vals.length && !vals[i].equals(\"null\")) { node.left = new TreeNode(Integer.parseInt(vals[i])); q.add(node.left); } i++;\n            if (i < vals.length && !vals[i].equals(\"null\")) { node.right = new TreeNode(Integer.parseInt(vals[i])); q.add(node.right); } i++;\n        }\n        return root;\n    }\n\n    public List<List<Integer>> verticalOrder(TreeNode root) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while(sc.hasNext()) sb.append(sc.next()).append(\" \");\n        String input = sb.toString().replaceAll(\"[\\\\[\\\\]]\", \"\");\n        String[] vals = input.split(\"[,\\\\s]+\");\n        TreeNode root = buildTree(vals);\n        List<List<Integer>> res = new Solution().verticalOrder(root);\n        System.out.println(res.toString().replace(\" \", \"\"));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction TreeNode(val) { this.val = val; this.left = this.right = null; }\n\nfunction buildTree(vals) {\n    if (!vals.length || vals[0]==='null') return null;\n    const root = new TreeNode(parseInt(vals[0]));\n    const q = [root]; let i = 1;\n    while (q.length && i < vals.length) {\n        const node = q.shift();\n        if (i < vals.length && vals[i]!=='null') { node.left = new TreeNode(parseInt(vals[i])); q.push(node.left); } i++;\n        if (i < vals.length && vals[i]!=='null') { node.right = new TreeNode(parseInt(vals[i])); q.push(node.right); } i++;\n    }\n    return root;\n}\n\nfunction verticalOrder(root) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst vals = input.replace(/[\\[\\]]/g, '').split(/[,\\s]+/);\nconsole.log(JSON.stringify(verticalOrder(buildTree(vals))));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode { int val; struct TreeNode *left, *right; };\n\nstruct TreeNode* newNode(int v) {\n    struct TreeNode* n = malloc(sizeof(struct TreeNode));\n    n->val = v; n->left = n->right = NULL; return n;\n}\n\nint** verticalOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {\n    // User logic here\n    *returnSize = 0; return NULL;\n}\n\nint main() {\n    // Build tree simulation\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3 9 20 null null 15 7", "expected_output": "[[9],[3],[15,20],[7]]", "is_sample": True},
        {"input": "3 9 8 4 0 1 7", "expected_output": "[[4],[9],[3,0,1],[8],[7]]", "is_sample": True},
        {"input": "3 9 8 4 0 1 7 null null null 2 5", "expected_output": "[[4],[9,5],[3,0,1],[8,2],[7]]", "is_sample": True},
        {"input": "null", "expected_output": "[]", "is_sample": False},
        {"input": "1", "expected_output": "[[1]]", "is_sample": False},
        {"input": "1 2 3 4 5 6 7", "expected_output": "[[4],[2],[1,5,6],[3],[7]]", "is_sample": False},
        {"input": "1 2 null 3 null 4", "expected_output": "[[3],[2,4],[1]]", "is_sample": False},
        {"input": "1 null 2 null 3 null 4", "expected_output": "[[1],[2],[3],[4]]", "is_sample": False},
        {"input": "5 3 8 1 4 7 9", "expected_output": "[[1],[3],[5,4,7],[8],[9]]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[[2],[1],[3]]", "is_sample": False}
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
        "topics": ["Tree", "Breadth-First Search", "Hash Table", "Binary Tree"],
        "companyIndex": 0
    }

    output_path = "201-400/314_Binary_Tree_Vertical_Order_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
