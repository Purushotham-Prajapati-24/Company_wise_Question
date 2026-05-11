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
        "python": "import sys\nimport json\nimport collections\n\nclass TreeNode:\n    def __init__(self, x):\n        self.val = x\n        self.left = None\n        self.right = None\n\nclass Codec:\n    def serialize(self, root):\n        # User logic here\n        pass\n\n    def deserialize(self, data):\n        # User logic here\n        pass\n\ndef build_tree(vals):\n    if not vals or vals[0] == 'null': return None\n    root = TreeNode(int(vals[0]))\n    queue = collections.deque([root]); i = 1\n    while queue and i < len(vals):\n        node = queue.popleft()\n        if i < len(vals) and vals[i] != 'null':\n            node.left = TreeNode(int(vals[i])); queue.append(node.left)\n        i += 1\n        if i < len(vals) and vals[i] != 'null':\n            node.right = TreeNode(int(vals[i])); queue.append(node.right)\n        i += 1\n    return root\n\ndef tree_to_list(root):\n    if not root: return []\n    result, queue = [], collections.deque([root])\n    while queue:\n        node = queue.popleft()\n        if node:\n            result.append(node.val); queue.append(node.left); queue.append(node.right)\n        else:\n            result.append(None)\n    while result and result[-1] is None: result.pop()\n    return result\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        vals = line.split()\n        root = build_tree(vals)\n        codec = Codec()\n        serialized = codec.serialize(root)\n        deserialized = codec.deserialize(serialized)\n        print(json.dumps(tree_to_list(deserialized)))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <queue>\n#include <sstream>\nusing namespace std;\n\nstruct TreeNode {\n    int val;\n    TreeNode *left, *right;\n    TreeNode(int x) : val(x), left(NULL), right(NULL) {}\n};\n\nclass Codec {\npublic:\n    string serialize(TreeNode* root) {\n        // User logic here\n        return \"\";\n    }\n    TreeNode* deserialize(string data) {\n        // User logic here\n        return NULL;\n    }\n};\n\nint main() {\n    // Stub: returns empty list\n    cout << \"[]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Codec {\n    public String serialize(TreeNode root) {\n        // User logic here\n        return \"\";\n    }\n    public TreeNode deserialize(String data) {\n        // User logic here\n        return null;\n    }\n    public static void main(String[] args) {\n        System.out.println(\"[]\");\n    }\n}",
        "javascript": "const fs = require('fs');\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\n\nfunction serialize(root) {\n    // User logic here\n    return \"\";\n}\nfunction deserialize(data) {\n    // User logic here\n    return null;\n}\n\nconsole.log(\"[]\");",
        "c": "#include <stdio.h>\n\nstruct TreeNode {\n    int val;\n    struct TreeNode *left, *right;\n};\n\nchar* serialize(struct TreeNode* root) {\n    // User logic here\n    return (char*)\"\";\n}\n\nstruct TreeNode* deserialize(char* data) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
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
