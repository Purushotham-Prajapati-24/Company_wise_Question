import json
import os

def generate_json():
    problem_id = 430
    title = "Flatten a Multilevel Doubly Linked List"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>430. Flatten a Multilevel Doubly Linked List</h3>
<p>You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional <strong>child pointer</strong>. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure.</p>

<p>Given the <code>head</code> of the first level of the list, <strong>flatten</strong> the list so that all the nodes appear in a single-level, doubly linked list. Let <code>curr</code> be a node with a child list. The nodes in the child list should appear after <code>curr</code> and before <code>curr.next</code> in the flattened list.</p>

<p>Return <em>the </em><code>head</code><em> of the flattened list. The nodes in the list must have all of their child pointers set to </em><code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg" style="width: 701px; height: 171px;" />
<pre><strong>Input:</strong> head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
<strong>Output:</strong> [1,2,3,7,8,11,12,9,10,4,5,6]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/09/flatten2.1jpg" style="width: 440px; height: 158px;" />
<pre><strong>Input:</strong> head = [1,2,null,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of Nodes will not exceed <code>1000</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A JSON array representing the multilevel doubly linked list in level-order traversal format."
    output_format = "A JSON array representing the flattened doubly linked list."
    
    constraints = [
        "The number of nodes will not exceed 1000.",
        "1 <= Node.val <= 10^5"
    ]
    
    explanation = """Perform a depth-first traversal of the multilevel list. When a node has a child, insert the child sublist recursively between the current node and its next node. Ensure all pointers (prev, next, child) are correctly updated to form a single doubly linked list."""
    
    answer = """class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        curr = head
        while curr:
            if curr.child:
                nxt = curr.next
                child = curr.child
                # Flatten child
                self.flatten(child)
                
                # Connect curr to child head
                curr.next = child
                child.prev = curr
                curr.child = None
                
                # Connect child tail to nxt
                temp = child
                while temp.next:
                    temp = temp.next
                if nxt:
                    temp.next = nxt
                    nxt.prev = temp
            curr = curr.next
        return head"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Node:\n    def __init__(self, val, prev=None, next=None, child=None):\n        self.val = val\n        self.prev = prev\n        self.next = next\n        self.child = child\n\ndef build_multilevel(data):\n    if not data: return None\n    nodes = []\n    for v in data:\n        nodes.append(Node(v) if v is not None else None)\n    \n    head = nodes[0]\n    for i in range(len(nodes)-1):\n        if nodes[i] and nodes[i+1]:\n            nodes[i].next = nodes[i+1]\n            nodes[i+1].prev = nodes[i]\n    if len(nodes) > 3 and nodes[0] and nodes[3]: nodes[0].child = nodes[3]\n    return head\n\nclass Solution:\n    def flatten(self, head: 'Node') -> 'Node':\n        # User logic here\n        return head\n\nif __name__ == '__main__':\n    raw = sys.stdin.read().strip()\n    if raw:\n        data = json.loads(raw)\n        print(\"[]\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Node {\npublic:\n    int val;\n    Node* prev;\n    Node* next;\n    Node* child;\n};\n\nclass Solution {\npublic:\n    Node* flatten(Node* head) {\n        // User logic here\n        return head;\n    }\n};\n\nint main() {\n    string input;\n    getline(cin, input);\n    cout << \"[]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Node {\n    public int val;\n    public Node prev;\n    public Node next;\n    public Node child;\n}\n\nclass Solution {\n    public Node flatten(Node head) {\n        // User logic here\n        return head;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            System.out.println(\"[]\");\n        }\n    }\n}",
        "javascript": "function Node(val,prev,next,child) {\n    this.val = val;\n    this.prev = prev;\n    this.next = next;\n    this.child = child;\n}\n\nvar flatten = function(head) {\n    // User logic here\n    return head;\n};\n\nconst fs = require('fs');\nconst raw = fs.readFileSync(0, 'utf8').trim();\nif (raw) {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct Node {\n    int val;\n    struct Node* prev;\n    struct Node* next;\n    struct Node* child;\n};\n\nstruct Node* flatten(struct Node* head) {\n    // User logic here\n    return head;\n}\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]", "expected_output": "[1,2,3,7,8,11,12,9,10,4,5,6]", "is_sample": True},
        {"input": "[1,2,null,3]", "expected_output": "[1,3,2]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": True},
        {"input": "[1,null,2]", "expected_output": "[1,2]", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "[1,2,3]", "is_sample": False},
        {"input": "[ 1, 2, null, 3 ]", "expected_output": "[1,3,2]", "is_sample": False},
        {"input": "[1,2,3,null,null,4,5,null,6]", "expected_output": "[1,2,3,4,6,5]", "is_sample": False},
        {"input": "[10,20,null,30]", "expected_output": "[10,30,20]", "is_sample": False},
        {"input": "[1,null,2,null,3,null,4]", "expected_output": "[1,2,3,4]", "is_sample": False},
        {"input": "[5,6,7,8,9,10]", "expected_output": "[5,6,7,8,9,10]", "is_sample": False}
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
        "topics": ["Linked List", "Doubly Linked List", "DFS"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
