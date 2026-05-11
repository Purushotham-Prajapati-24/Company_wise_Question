import json
import os

def generate_json():
    problem_id = 437
    title = "Path Sum III"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>437. Path Sum III</h3>
<p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>the number of paths where the sum of the node values along the path equals</em>&nbsp;<code>targetSum</code>.</p>

<p>The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg" style="width: 450px; height: 386px;" />
<pre><strong>Input:</strong> root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
<strong>Output:</strong> 3
<strong>Explanation:</strong> The paths that sum to 8 are: [5,3], [5,2,1], [-3,11]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 1000]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>"""

    input_format = "Two lines: root (JSON array) and targetSum (integer)."
    output_format = "An integer representing the number of paths."
    
    constraints = [
        "0 <= number of nodes <= 1000",
        "-10^9 <= Node.val <= 10^9",
        "-1000 <= targetSum <= 1000"
    ]
    
    explanation = """To find the number of paths that sum to `targetSum`, we can use a prefix sum approach with DFS. At each node, we maintain the current path sum from root to node. The number of paths ending at the current node that sum to `targetSum` is the frequency of `(current_sum - targetSum)` in our prefix sum hash map."""
    
    answer = """from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix_sums[curr_sum - targetSum]
            
            prefix_sums[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1
            
            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        return dfs(root, 0)"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import defaultdict\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data: return None\n    root = TreeNode(data[0])\n    queue = [root]\n    i = 1\n    while queue and i < len(data):\n        node = queue.pop(0)\n        if i < len(data) and data[i] is not None:\n            node.left = TreeNode(data[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and data[i] is not None:\n            node.right = TreeNode(data[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\nclass Solution:\n    def pathSum(self, root: TreeNode, targetSum: int) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        root_data = json.loads(lines[0].strip())\n        targetSum = int(lines[1].strip())\n        root = build_tree(root_data)\n        sol = Solution()\n        print(sol.pathSum(root, targetSum))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <unordered_map>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    int pathSum(TreeNode* root, int targetSum) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string rootLine;\n    int target;\n    if (getline(cin, rootLine) && cin >> target) {\n        cout << 0 << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\nclass Solution {\n    public int pathSum(TreeNode root, int targetSum) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        // I/O logic here\n    }\n}",
        "javascript": "function TreeNode(val, left, right) {\n    this.val = val;\n    this.left = left;\n    this.right = right;\n}\n\nvar pathSum = function(root, targetSum) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    console.log(0);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nint pathSum(struct TreeNode* root, int targetSum) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[10,5,-3,3,2,null,11,3,-2,null,1]\\n8", "expected_output": "3", "is_sample": True},
        {"input": "[5,4,8,11,null,13,4,7,2,null,null,5,1]\\n22", "expected_output": "3", "is_sample": True},
        {"input": "[]\\n0", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3]\\n5", "expected_output": "0", "is_sample": False},
        {"input": "[1,-1,1,-1,1,-1]\\n0", "expected_output": "7", "is_sample": False},
        {"input": "[ 10, 5, -3 ]\\n15", "expected_output": "1", "is_sample": False}, # Spaces
        {"input": "[1,null,2,null,3,null,4]\\n3", "expected_output": "2", "is_sample": False},
        {"input": "[1000000000,1000000000,null,1000000000,null,1000000000]\\n0", "expected_output": "0", "is_sample": False},
        # Stress
        {"input": json.dumps([1]*100) + "\\n1", "expected_output": "100", "is_sample": False},
        {"input": json.dumps([0]*50) + "\\n0", "expected_output": "1275", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Prefix Sum"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Path_Sum_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
