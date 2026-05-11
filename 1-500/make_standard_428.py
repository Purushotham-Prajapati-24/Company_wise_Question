import json
import os

def generate_json():
    problem_id = 428
    title = "Serialize and Deserialize N-ary Tree"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>428. Serialize and Deserialize N-ary Tree</h3>
<p>Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.</p>

<p>Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.</p>

<p>For example, you may serialize the following 3-ary tree</p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;">
<p>as <code>[1 [3[5 6] 2 4]]</code>. You do not necessarily need to follow this format.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The height of the n-ary tree is less than or equal to <code>1000</code>.</li>
	<li>Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.</li>
</ul>"""

    input_format = "A JSON array representing the level-order traversal of an N-ary tree."
    output_format = "A JSON array representing the level-order traversal of the reconstructed tree."
    
    constraints = [
        "0 <= number of nodes <= 10,000",
        "0 <= Node.val <= 10,000",
        "Tree height <= 1000"
    ]
    
    explanation = """To serialize an N-ary tree, we can use a pre-order traversal where each node's value is followed by its number of children. During deserialization, we can recursively reconstruct each node by reading its value and then its children count, repeating the process for each child."""
    
    answer = """class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root: return ""
        res = []
        def dfs(node):
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
        dfs(root)
        return ",".join(res)
	
    def deserialize(self, data: str) -> 'Node':
        if not data: return None
        items = data.split(",")
        it = iter(items)
        def dfs():
            try:
                val = next(it)
                count = int(next(it))
                node = Node(int(val), [])
                for _ in range(count):
                    node.children.append(dfs())
                return node
            except StopIteration:
                return None
        return dfs()"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Node(object):\n    def __init__(self, val=None, children=None):\n        self.val = val\n        self.children = children if children is not None else []\n\nclass Codec:\n    def serialize(self, root: 'Node') -> str:\n        # User logic here\n        return \"\"\n\n    def deserialize(self, data: str) -> 'Node':\n        # User logic here\n        return None\n\ndef build_tree(data):\n    if not data: return None\n    root = Node(data[0], [])\n    queue = [root]\n    i = 2\n    while queue and i < len(data):\n        node = queue.pop(0)\n        while i < len(data) and data[i] is not None:\n            child = Node(data[i], [])\n            node.children.append(child)\n            queue.append(child)\n            i += 1\n        i += 1\n    return root\n\ndef tree_to_list(root):\n    if not root: return []\n    res = [root.val, None]\n    queue = [root]\n    while queue:\n        node = queue.pop(0)\n        if node.children:\n            for child in node.children:\n                res.append(child.val)\n                queue.append(child)\n            res.append(None)\n    while res and res[-1] is None: res.pop()\n    return res\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        root = build_tree(data)\n        codec = Codec()\n        serialized = codec.serialize(root)\n        deserialized = codec.deserialize(serialized)\n        print(json.dumps(tree_to_list(deserialized)).replace(\" \", \"\"))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nclass Node {\npublic:\n    int val;\n    vector<Node*> children;\n    Node() {}\n    Node(int _val) : val(_val) {}\n};\n\nclass Codec {\npublic:\n    string serialize(Node* root) {\n        // User logic here\n        return \"\";\n    }\n    Node* deserialize(string data) {\n        // User logic here\n        return NULL;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        cout << \"[]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Node {\n    public int val;\n    public List<Node> children;\n    public Node() {}\n    public Node(int _val) { val = _val; }\n}\n\nclass Codec {\n    public String serialize(Node root) {\n        // User logic here\n        return \"\";\n    }\n    public Node deserialize(String data) {\n        // User logic here\n        return null;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        // I/O logic here\n    }\n}",
        "javascript": "function Node(val, children) {\n    this.val = val;\n    this.children = children;\n}\n\nclass Codec {\n    serialize(root) {\n        // User logic here\n    }\n    deserialize(data) {\n        // User logic here\n    }\n}\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct Node {\n    int val;\n    int childrenCount;\n    struct Node** children;\n};\n\nchar* serialize(struct Node* root) {\n    // User logic here\n    return NULL;\n}\n\nstruct Node* deserialize(char* data) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,null,3,2,4,null,5,6]", "expected_output": "[1,null,3,2,4,null,5,6]", "is_sample": True},
        {"input": "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]", "expected_output": "[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,null,2,null,3,null,4,null,5]", "expected_output": "[1,null,2,null,3,null,4,null,5]", "is_sample": False},
        {"input": "[ 1, null, 2 ]", "expected_output": "[1,null,2]", "is_sample": False}, # Spaces
        {"input": "[10,null,20,30,40]", "expected_output": "[10,null,20,30,40]", "is_sample": False},
        {"input": "[1,null,3,2,null,null,4,null,5,6]", "expected_output": "[1,null,3,2,null,null,4,null,5,6]", "is_sample": False},
        # Stress
        {"input": "[1,null,2,3,4,5,6,7,8,9,10,null,11,12,13,null,14,15]", "expected_output": "[1,null,2,3,4,5,6,7,8,9,10,null,11,12,13,null,14,15]", "is_sample": False},
        {"input": "[100,null,null]", "expected_output": "[100]", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Design"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Serialize_and_Deserialize_N-ary_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
