import json
import os

def generate_json():
    problem_id = 589
    title = "N-ary Tree Preorder Traversal"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>589. N-ary Tree Preorder Traversal</h3>
<p>Given the <code>root</code> of an n-ary tree, return <em>the preorder traversal of its nodes' values</em>.</p>

<p>N-ary tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" />
<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [1,3,5,6,2,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 100%; max-width: 296px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>The height of the n-ary tree is less than or equal to <code>1000</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>"""

    input_format = "A single line containing space-separated level-order values with 'null' as sibling separators."
    output_format = "A single line of space-separated integers representing the preorder traversal."
    
    constraints = [
        "0 <= nodes <= 10^4",
        "Max depth 1000.",
        "O(N) time complexity.",
        "O(H) extra space."
    ]
    
    explanation = """To perform a Preorder traversal (Root -> Children) on an N-ary tree:
1. **Iterative Strategy (using a Stack)**:
   - Root is visited first.
   - Then children are visited from left to right.
   - To achieve this using a stack (LIFO):
     - Push the root onto the stack.
     - While stack is not empty:
       - Pop the `node`.
       - Add `node.val` to the result.
       - Push all children of `node` onto the stack in **reverse order** (right to left). 
       - This ensures the left-most child is popped first in the next iteration.
2. **Complexity**:
   - Time Complexity: O(N) as each node is visited once.
   - Space Complexity: O(H) where H is the height of the tree for the stack."""
    
    answer = """class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def preorder(root: Node) -> list[int]:
    if not root: return []
    res = []
    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        # Push children in reverse to process left to right
        for child in reversed(curr.children):
            stack.append(child)
    return res"""

    boilerplate = {
        "python": "import sys\nfrom collections import deque\n\nclass Node:\n    def __init__(self, val=None, children=None):\n        self.val = val\n        self.children = children if children is not None else []\n\ndef build_tree(vals):\n    if not vals or vals[0] == 'null': return None\n    root = Node(int(vals[0]))\n    queue = deque([root])\n    i = 2\n    while queue and i < len(vals):\n        parent = queue.popleft()\n        while i < len(vals) and vals[i] != 'null':\n            child = Node(int(vals[i]))\n            parent.children.append(child)\n            queue.append(child)\n            i += 1\n        i += 1\n    return root\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        vals = line.split()\n        root = build_tree(vals)\n        # preorder(root) logic here\n        pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <algorithm>\n\nusing namespace std;\n\nclass Node {\npublic:\n    int val;\n    vector<Node*> children;\n    Node() {}\n    Node(int _val) : val(_val) {}\n    Node(int _val, vector<Node*> _children) : val(_val), children(_children) {}\n};\n\nvector<int> preorder(Node* root) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\nclass Node {\n    public int val;\n    public List<Node> children;\n    public Node() {}\n    public Node(int _val) { val = _val; }\n    public Node(int _val, List<Node> _children) { val = _val; children = _children; }\n}\n\npublic class Solution {\n    public List<Integer> preorder(Node root) {\n        // User logic\n        return new ArrayList<>();\n    }\n}",
        "javascript": "function preorder(root) {\n    // User logic\n}",
        "c": "int* preorder(struct Node* root, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 null 3 2 4 null 5 6", "expected_output": "1 3 5 6 2 4", "is_sample": True},
        {"input": "1 null 2 3 4 5 null null 6 7 null 8 null 9 10 null null 11 null 12 null 13 null null 14", "expected_output": "1 2 3 6 7 11 14 4 8 12 5 9 13 10", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 null 2", "expected_output": "1 2", "is_sample": False},
        {"input": "1 null 2 3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1 null 2 null 3", "expected_output": "1 2 3", "is_sample": False},
        # Stress cases
        {"input": "1 null " + " ".join([str(i) for i in range(2, 1001)]) + " null", "expected_output": "1 " + " ".join([str(i) for i in range(2, 1001)]), "is_sample": False},
        {"input": " ".join([str(i) if i % 2 == 0 else "null" for i in range(2000)]), "expected_output": " ".join([str(i*2) for i in range(1000)]), "is_sample": False},
        {"input": "100", "expected_output": "100", "is_sample": False}
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
        "topics": ["Tree", "Stack", "Preorder Traversal"],
        "companyIndex": 0
    }

    output_path = "401-600/589_N-ary_Tree_Preorder_Traversal.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
