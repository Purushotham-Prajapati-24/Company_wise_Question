import json
import os

def generate_json():
    problem_id = 426
    title = "Convert Binary Search Tree to Sorted Doubly Linked List"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>426. Convert Binary Search Tree to Sorted Doubly Linked List</h3>
<p>Convert a <strong>Binary Search Tree</strong> to a sorted <strong>Circular Doubly Linked List</strong> in place.</p>

<p>You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.</p>

<p>We want to do the transformation <strong>in place</strong>. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0426.Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List/images/bstdlloriginalbst.png" style="width: 282px; height: 161px;" />
<pre><strong>Input:</strong> root = [4,2,5,1,3]
<strong>Output:</strong> [1,2,3,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A JSON array representing the level-order traversal of the BST."
    output_format = "A JSON array representing the values of the sorted circular doubly linked list (starting from the head, ending at the tail)."
    
    constraints = [
        "0 <= number of nodes <= 2000",
        "-1000 <= Node.val <= 1000",
        "Conversion must be in-place."
    ]
    
    explanation = """Perform an in-order traversal of the BST. Use a 'last' pointer to keep track of the previously visited node. As you visit each node, link it with 'last' in both directions. After the traversal, link the first node and the last node to make the doubly linked list circular."""
    
    answer = """class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        first, last = None, None
        
        def inorder(node):
            nonlocal first, last
            if node:
                inorder(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                inorder(node.right)
        
        inorder(root)
        last.right = first
        first.left = last
        return first"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef build_tree(data):\n    if not data: return None\n    root = Node(data[0])\n    queue = [root]\n    i = 1\n    while queue and i < len(data):\n        node = queue.pop(0)\n        if i < len(data) and data[i] is not None:\n            node.left = Node(data[i])\n            queue.append(node.left)\n        i += 1\n        if i < len(data) and i < len(data) and data[i] is not None:\n            node.right = Node(data[i])\n            queue.append(node.right)\n        i += 1\n    return root\n\nclass Solution:\n    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        root = build_tree(data)\n        sol = Solution()\n        head = sol.treeToDoublyList(root)\n        res = []\n        if head:\n            curr = head\n            while True:\n                res.append(curr.val)\n                curr = curr.right\n                if curr == head: break\n        print(json.dumps(res).replace(\" \", \"\"))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <algorithm>\n\nusing namespace std;\n\nclass Node {\npublic:\n    int val;\n    Node* left;\n    Node* right;\n    Node(int _val) : val(_val), left(NULL), right(NULL) {}\n};\n\nclass Solution {\npublic:\n    Node* treeToDoublyList(Node* root) {\n        // User logic here\n        return NULL;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<string> data;\n        string temp = \"\";\n        bool inArr = false;\n        for (char c : line) {\n            if (c == '[') inArr = true;\n            else if (c == ']') {\n                if (!temp.empty()) data.push_back(temp);\n                temp = \"\";\n                inArr = false;\n            } else if (c == ',') {\n                if (!temp.empty()) data.push_back(temp);\n                temp = \"\";\n            } else if (c != ' ') {\n                temp += c;\n            }\n        }\n        if (data.empty()) {\n            cout << \"[]\" << endl;\n            return 0;\n        }\n        Node* root = new Node(stoi(data[0]));\n        queue<Node*> q;\n        q.push(root);\n        int i = 1;\n        while (!q.empty() && i < data.size()) {\n            Node* curr = q.front(); q.pop();\n            if (i < data.size() && data[i] != \"null\") {\n                curr->left = new Node(stoi(data[i]));\n                q.push(curr->left);\n            }\n            i++;\n            if (i < data.size() && data[i] != \"null\") {\n                curr->right = new Node(stoi(data[i]));\n                q.push(curr->right);\n            }\n            i++;\n        }\n        Solution sol;\n        Node* head = sol.treeToDoublyList(root);\n        cout << \"[\";\n        if (head) {\n            Node* curr = head;\n            bool first = true;\n            do {\n                if (!first) cout << \",\";\n                cout << curr->val;\n                first = false;\n                curr = curr->right;\n            } while (curr != head);\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Node {\n    public int val;\n    public Node left;\n    public Node right;\n    public Node(int _val) { val = _val; }\n}\n\nclass Solution {\n    public Node treeToDoublyList(Node root) {\n        // User logic here\n        return null;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            if (line.equals(\"[]\")) {\n                System.out.println(\"[]\");\n                return;\n            }\n            line = line.substring(1, line.length() - 1);\n            String[] parts = line.split(\",\");\n            List<String> data = new ArrayList<>();\n            for (String p : parts) data.add(p.trim());\n            if (data.get(0).isEmpty()) {\n                System.out.println(\"[]\");\n                return;\n            }\n            Node root = new Node(Integer.parseInt(data.get(0)));\n            Queue<Node> q = new LinkedList<>();\n            q.add(root);\n            int i = 1;\n            while (!q.isEmpty() && i < data.size()) {\n                Node curr = q.poll();\n                if (i < data.size() && !data.get(i).equals(\"null\")) {\n                    curr.left = new Node(Integer.parseInt(data.get(i)));\n                    q.add(curr.left);\n                }\n                i++;\n                if (i < data.size() && !data.get(i).equals(\"null\")) {\n                    curr.right = new Node(Integer.parseInt(data.get(i)));\n                    q.add(curr.right);\n                }\n                i++;\n            }\n            Solution sol = new Solution();\n            Node head = sol.treeToDoublyList(root);\n            System.out.print(\"[\");\n            if (head != null) {\n                Node curr = head;\n                boolean first = true;\n                do {\n                    if (!first) System.out.print(\",\");\n                    System.out.print(curr.val);\n                    first = false;\n                    curr = curr.right;\n                } while (curr != head);\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "function Node(val, left, right) {\n    this.val = val;\n    this.left = left;\n    this.right = right;\n}\n\n/**\n * @param {Node} root\n * @return {Node}\n */\nvar treeToDoublyList = function(root) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const data = JSON.parse(input);\n    if (!data.length) {\n        console.log(\"[]\");\n    } else {\n        const buildTree = (arr) => {\n            if (!arr.length) return null;\n            let root = new Node(arr[0]);\n            let q = [root];\n            let i = 1;\n            while (q.length && i < arr.length) {\n                let node = q.shift();\n                if (i < arr.length && arr[i] !== null) {\n                    node.left = new Node(arr[i]);\n                    q.push(node.left);\n                }\n                i++;\n                if (i < arr.length && arr[i] !== null) {\n                    node.right = new Node(arr[i]);\n                    q.push(node.right);\n                }\n                i++;\n            }\n            return root;\n        };\n        const root = buildTree(data);\n        const head = treeToDoublyList(root);\n        let res = [];\n        if (head) {\n            let curr = head;\n            while (true) {\n                res.push(curr.val);\n                curr = curr.right;\n                if (curr === head) break;\n            }\n        }\n        console.log(JSON.stringify(res).replace(/ /g, ''));\n    }\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct Node {\n    int val;\n    struct Node* left;\n    struct Node* right;\n};\n\nstruct Node* treeToDoublyList(struct Node* root) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    char line[10000];\n    if (fgets(line, sizeof(line), stdin)) {\n        printf(\"[]\\\\n\"); \n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[4,2,5,1,3]", "expected_output": "[1,2,3,4,5]", "is_sample": True},
        {"input": "[2,1,3]", "expected_output": "[1,2,3]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[5,3,7,2,4,6,8]", "expected_output": "[2,3,4,5,6,7,8]", "is_sample": False},
        {"input": "[ 4, 2, 5, 1, 3 ]", "expected_output": "[1,2,3,4,5]", "is_sample": False}, # Spaces
        {"input": "[10, 5, 15]", "expected_output": "[5,10,15]", "is_sample": False},
        {"input": "[5, null, 10]", "expected_output": "[5,10]", "is_sample": False},
        # Stress
        {"input": "[100,50,150,25,75,125,175]", "expected_output": "[25,50,75,100,125,150,175]", "is_sample": False},
        {"input": "[10,null,20,null,30]", "expected_output": "[10,20,30]", "is_sample": False}
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
        "topics": ["Tree", "BST", "Linked List"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Convert_BST_to_Sorted_Doubly_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
