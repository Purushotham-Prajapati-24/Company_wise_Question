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
        "python": (
            "import sys, json\n"
            "from collections import deque\n\n"
            "class TreeNode:\n"
            "    def __init__(self, val=0, left=None, right=None):\n"
            "        self.val = val; self.left = left; self.right = right\n\n"
            "def build(arr):\n"
            "    if not arr: return None\n"
            "    root = TreeNode(arr[0])\n"
            "    q = deque([root]); i = 1\n"
            "    while i < len(arr):\n"
            "        n = q.popleft()\n"
            "        if i < len(arr) and arr[i] is not None:\n"
            "            n.left = TreeNode(arr[i]); q.append(n.left)\n"
            "        i += 1\n"
            "        if i < len(arr) and arr[i] is not None:\n"
            "            n.right = TreeNode(arr[i]); q.append(n.right)\n"
            "        i += 1\n"
            "    return root\n\n"
            "def findLeaves(root):\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    root = build(json.loads(sys.stdin.read().strip()))\n"
            "    print(json.dumps(findLeaves(root)))"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <queue>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "struct TreeNode { int val; TreeNode *left, *right;\n"
            "    TreeNode(int x): val(x), left(nullptr), right(nullptr){} };\n\n"
            "vector<vector<int>> findLeaves(TreeNode* root) {\n"
            "    // User logic here\n"
            "    return {};\n"
            "}\n\n"
            "TreeNode* build(vector<int>& arr) {\n"
            "    if (arr.empty() || arr[0] == -1000000) return nullptr;\n"
            "    TreeNode* root = new TreeNode(arr[0]);\n"
            "    queue<TreeNode*> q; q.push(root);\n"
            "    for (int i = 1; !q.empty() && i < (int)arr.size(); ) {\n"
            "        TreeNode* n = q.front(); q.pop();\n"
            "        if (i < (int)arr.size() && arr[i] != -1000000) { n->left = new TreeNode(arr[i]); q.push(n->left); }\n"
            "        i++;\n"
            "        if (i < (int)arr.size() && arr[i] != -1000000) { n->right = new TreeNode(arr[i]); q.push(n->right); }\n"
            "        i++;\n"
            "    }\n"
            "    return root;\n"
            "}\n\n"
            "int main() {\n"
            "    string line; if (!getline(cin, line)) return 0;\n"
            "    vector<int> arr;\n"
            "    int i = 0, n = line.length();\n"
            "    while (i < n) {\n"
            "        if (line[i] == 'n') { arr.push_back(-1000000); i += 4; }\n"
            "        else if (line[i] == '-' || (line[i] >= '0' && line[i] <= '9')) {\n"
            "            int v = 0, sign = 1;\n"
            "            if (line[i] == '-') { sign = -1; i++; }\n"
            "            while (i < n && line[i] >= '0' && line[i] <= '9') { v = v * 10 + (line[i] - '0'); i++; }\n"
            "            arr.push_back(v * sign);\n"
            "        } else { i++; }\n"
            "    }\n"
            "    auto res = findLeaves(build(arr));\n"
            "    cout << '[';\n"
            "    for (int j = 0; j < (int)res.size(); j++) {\n"
            "        cout << '[';\n"
            "        for (int k = 0; k < (int)res[j].size(); k++) {\n"
            "            if (k > 0) cout << ','; cout << res[j][k];\n"
            "        }\n"
            "        cout << ']'; if (j + 1 < (int)res.size()) cout << ',';\n"
            "    }\n"
            "    cout << ']' << endl;\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }\n\n"
            "    static List<List<Integer>> findLeaves(TreeNode root) {\n"
            "        // User logic here\n"
            "        return new ArrayList<>();\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (!sc.hasNextLine()) return;\n"
            "        String line = sc.nextLine().trim();\n"
            "        line = line.substring(1, line.length() - 1);\n"
            "        String[] parts = line.split(\",\");\n"
            "        List<Integer> vals = new ArrayList<>();\n"
            "        for (String p : parts) {\n"
            "            p = p.trim();\n"
            "            if (p.isEmpty()) continue;\n"
            "            if (p.equals(\"null\")) vals.add(null);\n"
            "            else vals.add(Integer.parseInt(p));\n"
            "        }\n"
            "        TreeNode root = vals.isEmpty() || vals.get(0) == null ? null : new TreeNode(vals.get(0));\n"
            "        Queue<TreeNode> q = new LinkedList<>(); \n"
            "        if (root != null) q.add(root);\n"
            "        for (int i = 1; !q.isEmpty() && i < vals.size(); ) {\n"
            "            TreeNode n = q.poll();\n"
            "            if (i < vals.size() && vals.get(i) != null) { n.left = new TreeNode(vals.get(i)); q.add(n.left); }\n"
            "            i++;\n"
            "            if (i < vals.size() && vals.get(i) != null) { n.right = new TreeNode(vals.get(i)); q.add(n.right); }\n"
            "            i++;\n"
            "        }\n"
            "        List<List<Integer>> res = findLeaves(root);\n"
            "        StringBuilder sb = new StringBuilder(\"[\");\n"
            "        for (int i=0;i<res.size();i++) {\n"
            "            sb.append(\"[\");\n"
            "            for (int k=0; k<res.get(i).size(); k++) {\n"
            "                if (k>0) sb.append(\",\");\n"
            "                sb.append(res.get(i).get(k));\n"
            "            }\n"
            "            sb.append(\"]\");\n"
            "            if(i+1<res.size()) sb.append(',');\n"
            "        }\n"
            "        System.out.println(sb.append(']'));\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "function TreeNode(val) { this.val=val; this.left=this.right=null; }\n"
            "function build(arr) {\n"
            "    if (!arr.length || arr[0] === null) return null;\n"
            "    const root = new TreeNode(arr[0]);\n"
            "    const q = [root]; let i = 1;\n"
            "    while (q.length > 0 && i < arr.length) {\n"
            "        const n = q.shift();\n"
            "        if (i < arr.length && arr[i] !== null) { n.left = new TreeNode(arr[i]); q.push(n.left); } i++;\n"
            "        if (i < arr.length && arr[i] !== null) { n.right = new TreeNode(arr[i]); q.push(n.right); } i++;\n"
            "    }\n"
            "    return root;\n"
            "}\n\n"
            "var findLeaves = function(root) {\n"
            "    // User logic here\n"
            "    return [];\n"
            "};\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0,'utf8').trim();\n"
            "    if (!input) return;\n"
            "    const root = build(JSON.parse(input));\n"
            "    console.log(JSON.stringify(findLeaves(root)));\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n\n"
            "struct TreeNode { int val; struct TreeNode *left, *right; };\n\n"
            "int** findLeaves(struct TreeNode* root, int* retSz, int** retColSz) {\n"
            "    // User logic here\n"
            "    *retSz = 0; return NULL;\n"
            "}\n\n"
            "struct TreeNode* build(int* arr, int sz) {\n"
            "    if (sz == 0 || arr[0] == -1000000) return NULL;\n"
            "    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n"
            "    root->val = arr[0]; root->left = NULL; root->right = NULL;\n"
            "    struct TreeNode** q = (struct TreeNode**)malloc(sz * sizeof(struct TreeNode*));\n"
            "    int head = 0, tail = 0; q[tail++] = root;\n"
            "    for (int i = 1; head < tail && i < sz; ) {\n"
            "        struct TreeNode* n = q[head++];\n"
            "        if (i < sz && arr[i] != -1000000) {\n"
            "            n->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n"
            "            n->left->val = arr[i]; n->left->left = NULL; n->left->right = NULL;\n"
            "            q[tail++] = n->left;\n"
            "        }\n"
            "        i++;\n"
            "        if (i < sz && arr[i] != -1000000) {\n"
            "            n->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n"
            "            n->right->val = arr[i]; n->right->left = NULL; n->right->right = NULL;\n"
            "            q[tail++] = n->right;\n"
            "        }\n"
            "        i++;\n"
            "    }\n"
            "    free(q); return root;\n"
            "}\n\n"
            "int main() {\n"
            "    char buf[10000];\n"
            "    if (!fgets(buf, sizeof(buf), stdin)) return 0;\n"
            "    int arr[10000]; int sz = 0, i = 0;\n"
            "    while (buf[i]) {\n"
            "        if (buf[i] == 'n') { arr[sz++] = -1000000; i += 4; }\n"
            "        else if (buf[i] == '-' || (buf[i] >= '0' && buf[i] <= '9')) {\n"
            "            int v = 0, sign = 1;\n"
            "            if (buf[i] == '-') { sign = -1; i++; }\n"
            "            while (buf[i] >= '0' && buf[i] <= '9') { v = v * 10 + (buf[i] - '0'); i++; }\n"
            "            arr[sz++] = v * sign;\n"
            "        } else { i++; }\n"
            "    }\n"
            "    int retSz = 0; int* retColSz = NULL;\n"
            "    int** res = findLeaves(build(arr, sz), &retSz, &retColSz);\n"
            "    printf(\"[\");\n"
            "    for (int j = 0; j < retSz; j++) {\n"
            "        printf(\"[\");\n"
            "        for (int k = 0; k < retColSz[j]; k++) {\n"
            "            if (k > 0) printf(\",\");\n"
            "            printf(\"%d\", res[j][k]);\n"
            "        }\n"
            "        printf(\"]\");\n"
            "        if (j + 1 < retSz) printf(\",\");\n"
            "    }\n"
            "    printf(\"]\\n\");\n"
            "    return 0;\n"
            "}\n"
        )
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
