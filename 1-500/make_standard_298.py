import json
import os


def generate_json():
    problem_id = 298
    title = "Binary Tree Longest Consecutive Sequence"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>298. Binary Tree Longest Consecutive Sequence</h3>
<p>Given the <code>root</code> of a binary tree, return <em>the length of the longest <strong>consecutive sequence path</strong></em>.</p>

<p>A <strong>consecutive sequence path</strong> is a path where the values <strong>increase by one</strong> along the path.</p>

<p>Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://raw.githubusercontent.com/doocs/leetcode/main/solution/0200-0299/0298.Binary%20Tree%20Longest%20Consecutive%20Sequence/images/consec1-1-tree.jpg" style="width: 222px; height: 242px;" />
<pre><strong>Input:</strong> root = [1,null,3,2,4,null,null,null,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Longest consecutive sequence path is 3-4-5, so return 3.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://raw.githubusercontent.com/doocs/leetcode/main/solution/0200-0299/0298.Binary%20Tree%20Longest%20Consecutive%20Sequence/images/consec1-2-tree.jpg" style="width: 222px; height: 242px;" />
<pre><strong>Input:</strong> root = [2,null,3,2,null,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
	<li><code>-3 * 10<sup>4</sup> &lt;= Node.val &lt;= 3 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A serialized string representation of the tree (LeetCode format)."
    output_format = "The length of the longest consecutive sequence path."
    
    constraints = ["1 <= number of nodes <= 3 * 10^4\\n", "-3 * 10^4 <= Node.val <= 3 * 10^4\\n", "O(N) time complexity required.\\n", "O(H) space complexity required (Recursion stack)."]
    
    explanation = """To find the longest consecutive sequence path in a binary tree:
1. **DFS Traversal**: Use depth-first search starting from the root.
2. **Track Length**: Pass the parent's value and current sequence length to each child.
   - If the current node's value equals `parent_val + 1`, increment `curr_len`.
   - Otherwise, reset `curr_len = 1`.
3. **Update Max**: At each node, update the global maximum with `curr_len`.
4. **Complexity**:
   - Time: O(N) — each node is visited once.
   - Space: O(H) — recursion stack depth equals tree height."""
    
    answer = """class Solution:
    def longestConsecutive(self, root) -> int:
        if not root: return 0
        max_len = [0]

        def dfs(node, parent_val, curr_len):
            if not node: return
            if node.val == parent_val + 1:
                curr_len += 1
            else:
                curr_len = 1
            max_len[0] = max(max_len[0], curr_len)
            dfs(node.left, node.val, curr_len)
            dfs(node.right, node.val, curr_len)

        dfs(root, root.val - 1, 0)
        return max_len[0]"""

    boilerplate = {
        "python": "import sys\nimport collections\nimport re\nimport json\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data or data == '[]': return None\n    vals = data.strip('[]').split(',')\n    if not vals or not vals[0].strip() or vals[0].strip() == 'null': return None\n    \n    root = TreeNode(int(vals[0].strip()))\n    queue = collections.deque([root])\n    i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i].strip() != 'null' and vals[i].strip() != '':\n            node.left = TreeNode(int(vals[i].strip()))\n            queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i].strip() != 'null' and vals[i].strip() != '':\n            node.right = TreeNode(int(vals[i].strip()))\n            queue.append(node.right)\n        i += 1\n    return root\n\nclass Solution:\n    def longestConsecutive(self, root) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    match = re.search(r'\\[.*\\]', raw_input)\n    if match:\n        root = build_tree(match.group(0))\n        print(Solution().longestConsecutive(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <regex>\n#include <sstream>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    int longestConsecutive(TreeNode* root) {\n        // User logic\n        return 0;\n    }\n};\n\nTreeNode* buildTree(string data) {\n    if (data == \"[]\" || data == \"\") return NULL;\n    data = data.substr(1, data.length() - 2);\n    stringstream ss(data);\n    string item;\n    vector<string> vals;\n    while (getline(ss, item, ',')) vals.push_back(item);\n    if (vals.empty() || vals[0] == \"null\") return NULL;\n\n    TreeNode* root = new TreeNode(stoi(vals[0]));\n    queue<TreeNode*> q;\n    q.push(root);\n    int i = 1;\n    while (!q.empty() && i < vals.size()) {\n        TreeNode* curr = q.front(); q.pop();\n        if (i < vals.size() && vals[i] != \"null\" && !vals[i].empty()) {\n            curr->left = new TreeNode(stoi(vals[i]));\n            q.push(curr->left);\n        }\n        i++;\n        if (i < vals.size() && vals[i] != \"null\" && !vals[i].empty()) {\n            curr->right = new TreeNode(stoi(vals[i]));\n            q.push(curr->right);\n        }\n        i++;\n    }\n    return root;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line;\n    smatch m;\n    if (regex_search(input, m, regex(R\"(\\[.*\\])\"))) {\n        TreeNode* root = buildTree(m.str());\n        cout << Solution().longestConsecutive(root) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public int longestConsecutive(TreeNode root) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        Matcher m = Pattern.compile(\"\\\\[.*\\\\]\").matcher(input);\n        if (m.find()) {\n            TreeNode root = buildTree(m.group());\n            System.out.println(new Solution().longestConsecutive(root));\n        }\n    }\n\n    static TreeNode buildTree(String data) {\n        if (data.equals(\"[]\")) return null;\n        String[] vals = data.substring(1, data.length() - 1).split(\",\");\n        if (vals[0].trim().isEmpty() || vals[0].trim().equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(vals[0].trim()));\n        Queue<TreeNode> q = new LinkedList<>();\n        q.add(root);\n        int i = 1;\n        while (!q.isEmpty() && i < vals.length) {\n            TreeNode curr = q.poll();\n            if (i < vals.length && !vals[i].trim().equals(\"null\")) {\n                curr.left = new TreeNode(Integer.parseInt(vals[i].trim()));\n                q.add(curr.left);\n            }\n            i++;\n            if (i < vals.length && !vals[i].trim().equals(\"null\")) {\n                curr.right = new TreeNode(Integer.parseInt(vals[i].trim()));\n                q.add(curr.right);\n            }\n            i++;\n        }\n        return root;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass TreeNode {\n    constructor(val) {\n        this.val = val;\n        this.left = this.right = null;\n    }\n}\n\nfunction buildTree(data) {\n    if (!data || data === '[]') return null;\n    const vals = data.slice(1, -1).split(',').map(s => s.trim());\n    if (vals[0] === 'null' || vals[0] === '') return null;\n    const root = new TreeNode(parseInt(vals[0]));\n    const q = [root];\n    let i = 1;\n    while (q.length > 0 && i < vals.length) {\n        const curr = q.shift();\n        if (i < vals.length && vals[i] !== 'null') {\n            curr.left = new TreeNode(parseInt(vals[i]));\n            q.push(curr.left);\n        }\n        i++;\n        if (i < vals.length && vals[i] !== 'null') {\n            curr.right = new TreeNode(parseInt(vals[i]));\n            q.push(curr.right);\n        }\n        i++;\n    }\n    return root;\n}\n\nfunction longestConsecutive(root) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst match = input.match(/\\[.*\\]/);\nif (match) {\n    const root = buildTree(match[0]);\n    console.log(longestConsecutive(root));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nint longestConsecutive(struct TreeNode* root) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    printf(\"0\\n\");\n    return 0;\n}"
    }

    test_cases = [{"input": "[1,null,3,2,4,null,null,null,5]", "expected_output": "3", "is_sample": True},
        {"input": "[2,null,3,2,null,1]", "expected_output": "2", "is_sample": True},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3,4,5]", "expected_output": "2", "is_sample": False},
        {"input": "[1,null,2,null,3,null,4,null,5]", "expected_output": "5", "is_sample": False},
        {"input": "[5,4,3,2,1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,null,3,null,4,null,5]", "expected_output": "5", "is_sample": False},
        {"input": "[1,3,2,4,5,null,null,null,null,null,6]", "expected_output": "2", "is_sample": False},
        {"input": "[1,1,1,1,1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "2", "is_sample": False}]

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
        "companyIndex": 0
    }

    output_path = f"201-400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
