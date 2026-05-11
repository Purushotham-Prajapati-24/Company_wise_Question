import json
import os

def generate_json():
    problem_id = 366
    title = "Find Leaves of Binary Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>366. Find Leaves of Binary Tree</h3>
<p>Given the <code>root</code> of a binary tree, collect a tree's nodes as if you were doing this:</p>

<ol>
	<li>Collect all the leaf nodes.</li>
	<li>Remove all the leaf nodes.</li>
	<li>Repeat until the tree is empty.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0366.Find%20Leaves%20of%20Binary%20Tree/images/remleaves-tree.jpg" style="width: 500px; height: 215px;" />
<pre><strong>Input:</strong> root = [1,2,3,4,5]
<strong>Output:</strong> [[4,5,3],[2],[1]]
<strong>Explanation:</strong>
[[4,5,3],[2],[1]] is also accepted because [[5,4,3],[2],[1]] is corrected.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "The `root` of a binary tree represented as an array (level-order)."
    output_format = "A list of lists of integers, where each internal list contains the leaves collected in one step."
    
    constraints = [
        "1 <= number of nodes <= 100",
        "-100 <= Node.val <= 100"
    ]
    
    explanation = """To collect the leaves level-by-level (starting from the bottom), we can use **DFS** to calculate the **height** of each node relative to its deepest descendant.

### Key Strategy:
- The height of a leaf node is 0.
- The height of any node is `1 + max(height(left_child), height(right_child))`.
- Nodes with the same height belong to the same collection in the result.

### Algorithm Steps:
1. **Initialize**: `self.res = []`.
2. **DFS Function**: `get_height(node)`:
   - If `node` is `None`, return `-1`.
   - Calculate `left_h = get_height(node.left)`.
   - Calculate `right_h = get_height(node.right)`.
   - `curr_h = 1 + max(left_h, right_h)`.
   - **Store Node**:
     - If `len(self.res) == curr_h`, append an empty list to `self.res`.
     - Append `node.val` to `self.res[curr_h]`.
   - Return `curr_h`.
3. **Execute**: Call `get_height(root)`.
4. **Result**: `self.res` will contain the lists of nodes organized by their distance from the leaves.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes. Each node is visited exactly once.
- **Space Complexity**: $O(H)$, where $H$ is the height of the tree, for the recursion stack. $O(N)$ for the result storage."""
    
    answer = """def findLeaves(root):
    res = []
    
    def get_height(node):
        if not node:
            return -1
        
        # Height is 1 + max height of children
        h = 1 + max(get_height(node.left), get_height(node.right))
        
        # If the current height exceeds list size, add a new nested list
        if len(res) == h:
            res.append([])
        
        res[h].append(node.val)
        return h
        
    get_height(root)
    return res"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(nodes):\n    if not nodes or nodes[0] is None:\n        return None\n    root = TreeNode(nodes[0])\n    queue = deque([root])\n    i = 1\n    while queue and i < len(nodes):\n        node = queue.popleft()\n        if i < len(nodes) and nodes[i] is not None:\n            node.left = TreeNode(nodes[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(nodes) and nodes[i] is not None:\n            node.right = TreeNode(nodes[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\ndef findLeaves(root):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read()\n    tokens = re.findall(r'null|-?\\d+', input_data)\n    nodes = [None if t == 'null' else int(t) for t in tokens]\n    if nodes:\n        res = findLeaves(build_tree(nodes))\n        print('[' + ','.join('[' + ','.join(map(str, row)) + ']' for row in res) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nTreeNode* build(vector<string>& nodes) {\n    if (nodes.empty() || nodes[0] == \"null\") return nullptr;\n    TreeNode* root = new TreeNode(stoi(nodes[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < nodes.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->left = new TreeNode(stoi(nodes[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < nodes.size() && nodes[i] != \"null\") {\n            curr->right = new TreeNode(stoi(nodes[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nvector<vector<int>> findLeaves(TreeNode* root) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    regex re(\"null|-?\\\\d+\");\n    vector<string> nodes;\n    for (sregex_iterator i(input.begin(), input.end(), re), end; i != end; ++i) nodes.push_back(i->str());\n    auto res = findLeaves(build(nodes));\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); ++i) {\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); ++j) {\n            cout << res[i][j] << (j == (int)res[i].size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << (i == (int)res.size() - 1 ? \"\" : \",\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class TreeNode {\n        int val; TreeNode left, right;\n        TreeNode(int x) { val = x; }\n    }\n    public static List<List<Integer>> findLeaves(TreeNode root) {\n        // User logic here\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        List<String> nodes = new ArrayList<>();\n        Matcher m = Pattern.compile(\"null|-?\\\\d+\").matcher(input);\n        while (m.find()) nodes.add(m.group());\n        if (nodes.isEmpty() || nodes.get(0).equals(\"null\")) { System.out.println(\"[]\"); return; }\n        TreeNode root = new TreeNode(Integer.parseInt(nodes.get(0)));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < nodes.size()) {\n            TreeNode curr = q.poll();\n            if (i < nodes.size() && !nodes.get(i).equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(nodes.get(i)));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < nodes.size() && !nodes.get(i).equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(nodes.get(i)));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        List<List<Integer>> res = findLeaves(root);\n        System.out.println(res.toString().replace(\" \", \"\"));\n    }\n}",
        "javascript": "\"use strict\";\nconst fs = require('fs');\n\nfunction TreeNode(val) {\n    this.val = val; this.left = this.right = null;\n}\n\nfunction build(arr) {\n    if (!arr.length || arr[0] === null) return null;\n    let root = new TreeNode(arr[0]), q = [root], i = 1;\n    while (q.length && i < arr.length) {\n        let curr = q.shift();\n        if (i < arr.length && arr[i] !== null) {\n            curr.left = new TreeNode(arr[i]);\n            q.push(curr.left);\n        }\n        i++;\n        if (i < arr.length && arr[i] !== null) {\n            curr.right = new TreeNode(arr[i]);\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction findLeaves(root) {\n    // User logic here\n    return [];\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const tokens = input.match(/null|-?\\d+/g);\n    if (!tokens) return;\n    const arr = tokens.map(t => t === 'null' ? null : parseInt(t));\n    console.log(JSON.stringify(findLeaves(build(arr))));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\n// User logic here\n// Note: This problem is hard to implement in C due to nested list result.\n// Usually, returnSize and returnColumnSizes are used.\n\nint** findLeaves(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }


    test_cases = [
        {"input": "[1,2,3,4,5]", "expected_output": "[[4,5,3],[2],[1]]", "is_sample": True},
        {"input": "[1]", "expected_output": "[[1]]", "is_sample": True},
        # 5 Diverse Cases
        {"input": "[1,2,3,4,5,null,6]", "expected_output": "[[4,5,6],[2,3],[1]]", "is_sample": False},
        {"input": "[1,2,null,3,null,4]", "expected_output": "[[4],[3],[2],[1]]", "is_sample": False},
        {"input": "[1,null,2,null,3,null,4]", "expected_output": "[[4],[3],[2],[1]]", "is_sample": False},
        {"input": "[1,2,3,4,null,null,5]", "expected_output": "[[4,5],[2,3],[1]]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "[[4,5,6,7],[2,3],[1]]", "is_sample": False},
        # 3 Stress Cases
        {"input": "[1,2,null,3,null,4,null,5]", "expected_output": "[[5],[4],[3],[2],[1]]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10]", "expected_output": "[[8,9,10,6,7],[4,5,3],[2],[1]]", "is_sample": False},
        {"input": "[1,2,2,3,null,null,3,4,null,null,4]", "expected_output": "[[4,4],[3,3],[2,2],[1]]", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Binary Tree"],
        "companyIndex": 1
    }

    output_path = "301-500/366_Find_Leaves_of_Binary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
