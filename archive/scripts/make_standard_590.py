import json
import os

def generate_json():
    problem_id = 590
    title = "N-ary Tree Postorder Traversal"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>590. N-ary Tree Postorder Traversal</h3>
<p>Given the <code>root</code> of an n-ary tree, return <em>the postorder traversal of its nodes' values</em>.</p>

<p>N-ary tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" />
<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [5,6,3,2,4,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 100%; max-width: 296px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The height of the n-ary tree is less than or equal to <code>1000</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Recursive solution is trivial, can you do it iteratively?
"""

    input_format = "A single line containing space-separated level-order values with 'null' as sibling separators."
    output_format = "A single line of space-separated integers representing the postorder traversal."
    
    constraints = [
        "0 <= nodes <= 10^4",
        "0 <= val <= 10^4",
        "Tree height <= 1000",
        "O(N) time complexity.",
        "O(H) extra space."
    ]
    
    explanation = """To perform postorder traversal on an N-ary tree:
1. **The Postorder Rule**:
   - Recursively visit all children of a node from left to right.
   - After visiting all children, visit the node itself.
2. **Recursive Strategy**:
   - Define a function `dfs(node)`:
     - For each `child` in `node.children`:
       - `dfs(child)`
     - Add `node.val` to the result list.
3. **Iterative Strategy (Follow-up)**:
   - Use a stack to perform a pre-order traversal (Root -> Right Child -> Left Child).
   - Reverse the resulting list to get postorder (Left Child -> Right Child -> Root).
4. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(H) representing the recursion depth or O(N) for result storage."""
    
    answer = """class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def postorder(root: Node) -> list[int]:
    if not root: return []
    res = []
    def dfs(node):
        for child in node.children:
            dfs(child)
        res.append(node.val)
    dfs(root)
    return res"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass Node:\n    def __init__(self, val=None, children=None):\n        self.val = val\n        self.children = children if children is not None else []\n\ndef build_tree(vals):\n    if not vals or vals[0] == 'null': return None\n    root = Node(int(vals[0]))\n    queue = deque([root])\n    i = 2 # skip root and first null\n    while queue and i < len(vals):\n        parent = queue.popleft()\n        while i < len(vals) and vals[i] != 'null':\n            child = Node(int(vals[i]))\n            parent.children.append(child)\n            queue.append(child)\n            i += 1\n        i += 1 # skip null separator\n    return root\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        vals = line.split()\n        root = build_tree(vals)\n        # postorder(root) logic here\n        pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass Node {\npublic:\n    int val;\n    vector<Node*> children;\n    Node() {}\n    Node(int _val) : val(_val) {}\n    Node(int _val, vector<Node*> _children) : val(_val), children(_children) {}\n};\n\nvector<int> postorder(Node* root) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\nclass Node {\n    public int val;\n    public List<Node> children;\n    public Node() {}\n    public Node(int _val) { val = _val; }\n    public Node(int _val, List<Node> _children) { val = _val; children = _children; }\n}\n\npublic class Solution {\n    public List<Integer> postorder(Node root) {\n        // User logic\n        return new ArrayList<>();\n    }\n}",
        "javascript": "function postorder(root) {\n    // User logic\n}",
        "c": "struct Node {\n    int val;\n    int numChildren;\n    struct Node** children;\n};\n\nint* postorder(struct Node* root, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 null 3 2 4 null 5 6", "expected_output": "5 6 3 2 4 1", "is_sample": True},
        {"input": "1 null 2 3 4 5 null null 6 7 null 8 null 9 10 null null 11 null 12 null 13 null null 14", "expected_output": "2 6 14 11 7 3 12 8 4 13 9 10 5 1", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "", "expected_output": "", "is_sample": False},
        {"input": "1 null 2", "expected_output": "2 1", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "3 2 1", "is_sample": False},
        {"input": "1 null 2 3 4", "expected_output": "2 3 4 1", "is_sample": False},
        # Stress cases
        {"input": "1 null " + " ".join([str(i) for i in range(2, 5001)]) + " null", "expected_output": " ".join([str(i) for i in range(2, 5001)]) + " 1", "is_sample": False},
        {"input": "1 null 2 null 3 null 4 null 5", "expected_output": "5 4 3 2 1", "is_sample": False},
        {"input": "0 null 1", "expected_output": "1 0", "is_sample": False}
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
        "topics": ["Tree", "DFS", "Multi-ary Tree"],
        "companyIndex": 0
    }

    output_path = "401-600/590_N-ary_Tree_Postorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
