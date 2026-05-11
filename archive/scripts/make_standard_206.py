import json
import os

def generate_json():
    problem_id = 206
    title = "Reverse Linked List"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>206. Reverse Linked List</h3>
<p>Given the <code>head</code> of a singly linked list, reverse the list, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> A linked list can be reversed either iteratively or recursively. Could you implement both?"""

    input_format = "A single line containing space-separated integers for the linked list."
    output_format = "Space-separated integers representing the reversed linked list."
    
    constraints = [
        "Nodes: [0, 5000]",
        "Node.val: [-5000, 5000]",
        "O(N) time, O(1) space expected for iterative version."
    ]
    
    explanation = """To reverse a singly linked list iteratively:
1. **Initialize Poínters**:
   - `prev` as `None` (representing the new end of the list).
   - `curr` as `head` (the node being processed).
2. **Logic**:
   - While `curr` is not `None`:
     - Temporarily store the next node: `nxt = curr.next`.
     - Reverse the connection: `curr.next = prev`.
     - Move `prev` forward: `prev = curr`.
     - Move `curr` forward: `curr = nxt`.
3. **Return Head**:
   - When the loop ends, `prev` will be pointing to the new head of the reversed list.
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of nodes.
   - Space Complexity: O(1) as we only use three pointers."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef reverseList(head):\n    # User logic here\n    return head\n\ndef build_list(nodes):\n    if not nodes: return None\n    head = ListNode(int(nodes[0]))\n    curr = head\n    for i in range(1, len(nodes)):\n        curr.next = ListNode(int(nodes[i]))\n        curr = curr.next\n    return head\n\ndef print_list(head):\n    res = []\n    while head:\n        res.append(str(head.val))\n        head = head.next\n    print(\" \".join(res))\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print_list(reverseList(build_list(data)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* buildList(vector<int>& nums) {\n    if (nums.empty()) return NULL;\n    ListNode* head = new ListNode(nums[0]);\n    ListNode* curr = head;\n    for (size_t i = 1; i < nums.size(); i++) {\n        curr->next = new ListNode(nums[i]);\n        curr = curr->next;\n    }\n    return head;\n}\n\nvoid printList(ListNode* head) {\n    while (head) {\n        cout << head->val << (head->next ? \" \" : \"\");\n        head = head->next;\n    }\n    cout << endl;\n}\n\nListNode* reverseList(ListNode* head) {\n    // User logic\n    return head;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int num;\n        vector<int> nums;\n        while (ss >> num) nums.push_back(num);\n        printList(reverseList(buildList(nums)));\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public ListNode reverseList(ListNode head) {\n        // User logic\n        return head;\n    }\n\n    public static ListNode buildList(String[] nodes) {\n        if (nodes.length == 0 || (nodes.length == 1 && nodes[0].isEmpty())) return null;\n        ListNode head = new ListNode(Integer.parseInt(nodes[0]));\n        ListNode curr = head;\n        for (int i = 1; i < nodes.length; i++) {\n            curr.next = new ListNode(Integer.parseInt(nodes[i]));\n            curr = curr.next;\n        }\n        return head;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            String[] nodes = line.trim().split(\"\\\\s+\");\n            ListNode head = new Solution().reverseList(buildList(nodes));\n            while (head != null) {\n                System.out.print(head.val + (head.next != null ? \" \" : \"\"));\n                head = head.next;\n            }\n            System.out.println();\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction buildList(nodes) {\n    if (nodes.length === 0 || (nodes.length === 1 && nodes[0] === '')) return null;\n    let head = new ListNode(parseInt(nodes[0]));\n    let curr = head;\n    for (let i = 1; i < nodes.length; i++) {\n        curr.next = new ListNode(parseInt(nodes[i]));\n        curr = curr.next;\n    }\n    return head;\n}\n\nfunction reverseList(head) {\n    // User logic\n    return head;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let head = reverseList(buildList(input));\n    let res = [];\n    while (head) {\n        res.push(head.val);\n        head = head.next;\n    }\n    console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* buildList(char* line) {\n    char* token = strtok(line, \" \\t\\r\\n\");\n    if (!token) return NULL;\n    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));\n    head->val = atoi(token);\n    head->next = NULL;\n    struct ListNode* curr = head;\n    while ((token = strtok(NULL, \" \\t\\r\\n\"))) {\n        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n        curr->next->val = atoi(token);\n        curr->next->next = NULL;\n        curr = curr->next;\n    }\n    return head;\n}\n\nstruct ListNode* reverseList(struct ListNode* head) {\n    // User logic\n    return head;\n}\n\nint main() {\n    char line[100000];\n    if (fgets(line, sizeof(line), stdin)) {\n        struct ListNode* head = reverseList(buildList(line));\n        while (head) {\n            printf(\"%d%s\", head->val, head->next ? \" \" : \"\");\n            head = head->next;\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 4 5", "expected_output": "5 4 3 2 1", "is_sample": True},
        {"input": "1 2", "expected_output": "2 1", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "100 200 300 400", "expected_output": "400 300 200 100", "is_sample": False},
        {"input": "-5 -4 -3", "expected_output": "-3 -4 -5", "is_sample": False},
        {"input": "0 1 0", "expected_output": "0 1 0", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(5000)]), "expected_output": " ".join([str(i) for i in range(4999, -1, -1)]), "is_sample": False},
        {"input": " ".join(["42"]*5000), "expected_output": " ".join(["42"]*5000), "is_sample": False},
        {"input": "1 " + " ".join(["0"]*4998) + " 2", "expected_output": "2 " + " ".join(["0"]*4998) + " 1", "is_sample": False}
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
        "topics": ["Linked List", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/206_Reverse_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
