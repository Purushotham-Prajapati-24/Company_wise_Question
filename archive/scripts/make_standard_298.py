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
        "python": "import sys\nimport collections\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\n\nclass Solution:\n    def longestConsecutive(self, root) -> int:\n        # User logic here\n        pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == 'null': return None\n    root = TreeNode(int(vals[0]))\n    queue = collections.deque([root]); i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != 'null':\n            node.left = TreeNode(int(vals[i])); queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != 'null':\n            node.right = TreeNode(int(vals[i])); queue.append(node.right)\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        vals = line.split()\n        root = build_tree(vals)\n        print(Solution().longestConsecutive(root))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    int longestConsecutive(TreeNode* root) {\n        // User logic here\n        return 0;\n    }\n};\n\nTreeNode* buildTree(vector<string>& vals) {\n    if (vals.empty() || vals[0] == \"null\") return NULL;\n    TreeNode* root = new TreeNode(stoi(vals[0]));\n    queue<TreeNode*> q; q.push(root); int i = 1;\n    while (!q.empty() && i < (int)vals.size()) {\n        TreeNode* node = q.front(); q.pop();\n        if (i < (int)vals.size() && vals[i] != \"null\") {\n            node->left = new TreeNode(stoi(vals[i])); q.push(node->left);\n        } i++;\n        if (i < (int)vals.size() && vals[i] != \"null\") {\n            node->right = new TreeNode(stoi(vals[i])); q.push(node->right);\n        } i++;\n    }\n    return root;\n}\n\nint main() {\n    vector<string> vals;\n    string tok;\n    while (cin >> tok) vals.push_back(tok);\n    TreeNode* root = buildTree(vals);\n    cout << Solution().longestConsecutive(root) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    static class TreeNode {\n        int val; TreeNode left, right;\n        TreeNode(int x) { val = x; }\n    }\n    public int longestConsecutive(TreeNode root) {\n        // User logic here\n        return 0;\n    }\n    static TreeNode buildTree(String[] vals) {\n        if (vals.length == 0 || vals[0].equals(\"null\")) return null;\n        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));\n        Queue<TreeNode> q = new LinkedList<>(); q.add(root); int i = 1;\n        while (!q.isEmpty() && i < vals.length) {\n            TreeNode node = q.poll();\n            if (i < vals.length && !vals[i].equals(\"null\")) { node.left = new TreeNode(Integer.parseInt(vals[i])); q.add(node.left); } i++;\n            if (i < vals.length && !vals[i].equals(\"null\")) { node.right = new TreeNode(Integer.parseInt(vals[i])); q.add(node.right); } i++;\n        }\n        return root;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String[] vals = sc.useDelimiter(\"\\\\A\").next().trim().split(\"\\\\s+\");\n        System.out.println(new Solution().longestConsecutive(buildTree(vals)));\n    }\n}",
        "javascript": "const fs = require('fs');\nconst vals = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n\nfunction TreeNode(val) { this.val = val; this.left = this.right = null; }\nfunction buildTree(vals) {\n    if (!vals.length || vals[0] === 'null') return null;\n    const root = new TreeNode(parseInt(vals[0]));\n    const queue = [root]; let i = 1;\n    while (queue.length && i < vals.length) {\n        const node = queue.shift();\n        if (i < vals.length && vals[i] !== 'null') { node.left = new TreeNode(parseInt(vals[i])); queue.push(node.left); } i++;\n        if (i < vals.length && vals[i] !== 'null') { node.right = new TreeNode(parseInt(vals[i])); queue.push(node.right); } i++;\n    }\n    return root;\n}\n\nfunction longestConsecutive(root) {\n    // User logic here\n    return 0;\n}\nconsole.log(longestConsecutive(buildTree(vals)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nint longestConsecutive(struct TreeNode* root) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    // Stub: tree construction in C left as exercise\n    printf(\"0\\n\");\n    return 0;\n}"
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
