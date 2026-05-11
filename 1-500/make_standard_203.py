import json
import os

def generate_json():
    problem_id = 203
    title = "Remove Linked List Elements"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>203. Remove Linked List Elements</h3>
<p>Given the <code>head</code> of a linked list and an integer <code>val</code>, remove all the nodes of the linked list that have <code>Node.val == val</code>, and return <em>the new head</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 133px;" />
<pre>
<strong>Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong>Output:</strong> [1,2,3,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [], val = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [7,7,7,7], val = 7
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 50</code></li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for the linked list. Line 2: the value to remove."
    output_format = "Space-separated integers representing the modified linked list."
    
    constraints = [
        "Nodes: [0, 10^4]",
        "Node.val: [1, 50]",
        "val: [0, 50]",
        "O(N) time and O(1) space expected."
    ]
    
    explanation = """To remove elements from a linked list:
1. **Use a Dummy Node**:
   - Create a `dummy` node that points to the origin `head`. This simplifies handling cases where the head node itself needs to be removed.
2. **One-Pass Iteration**:
   - Use a `current` pointer starting at `dummy`.
   - While `current.next` exists:
     - Check if `current.next.val` is equal to the target `val`.
     - If it is, skip the node by setting `current.next = current.next.next`.
     - Otherwise, move `current` to the next node (`current = current.next`).
3. **Return New Head**:
   - Return `dummy.next`, which is the head of the modified list.
4. **Complexity**:
   - Time Complexity: O(N) because we visit each node once.
   - Space Complexity: O(1) as we only use a few extra pointers."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    return dummy.next"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef removeElements(head, val):\n    # User logic here\n    return head\n\ndef build_list(nodes):\n    if not nodes: return None\n    head = ListNode(int(nodes[0]))\n    curr = head\n    for i in range(1, len(nodes)):\n        curr.next = ListNode(int(nodes[i]))\n        curr = curr.next\n    return head\n\ndef print_list(head):\n    res = []\n    while head:\n        res.append(str(head.val))\n        head = head.next\n    print(\" \".join(res))\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 1:\n        nodes = lines[0].split()\n        target = int(lines[1]) if len(lines) >= 2 else 0\n        print_list(removeElements(build_list(nodes), target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* buildList(vector<int>& nums) {\n    if (nums.empty()) return NULL;\n    ListNode* head = new ListNode(nums[0]);\n    ListNode* curr = head;\n    for (size_t i = 1; i < nums.size(); i++) {\n        curr->next = new ListNode(nums[i]);\n        curr = curr->next;\n    }\n    return head;\n}\n\nvoid printList(ListNode* head) {\n    while (head) {\n        cout << head->val << (head->next ? \" \" : \"\");\n        head = head->next;\n    }\n    cout << endl;\n}\n\nListNode* removeElements(ListNode* head, int val) {\n    // User logic here\n    return head;\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        stringstream ss(line1);\n        int num;\n        vector<int> nums;\n        while (ss >> num) nums.push_back(num);\n        int val = stoi(line2);\n        printList(removeElements(buildList(nums), val));\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public ListNode removeElements(ListNode head, int val) {\n        // User logic here\n        return head;\n    }\n\n    public static ListNode buildList(String[] nodes) {\n        if (nodes.length == 0 || (nodes.length == 1 && nodes[0].isEmpty())) return null;\n        ListNode head = new ListNode(Integer.parseInt(nodes[0]));\n        ListNode curr = head;\n        for (int i = 1; i < nodes.length; i++) {\n            curr.next = new ListNode(Integer.parseInt(nodes[i]));\n            curr = curr.next;\n        }\n        return head;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null && line2 != null) {\n            String[] nodes = line1.trim().split(\"\\\\s+\");\n            int val = Integer.parseInt(line2.trim());\n            ListNode head = new Solution().removeElements(buildList(nodes), val);\n            while (head != null) {\n                System.out.print(head.val + (head.next != null ? \" \" : \"\"));\n                head = head.next;\n            }\n            System.out.println();\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction buildList(nodes) {\n    if (nodes.length === 0 || (nodes.length === 1 && nodes[0] === '')) return null;\n    let head = new ListNode(parseInt(nodes[0]));\n    let curr = head;\n    for (let i = 1; i < nodes.length; i++) {\n        curr.next = new ListNode(parseInt(nodes[i]));\n        curr = curr.next;\n    }\n    return head;\n}\n\nfunction removeElements(head, val) {\n    // User logic here\n    return head;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\r?\\n/);\nif (input.length >= 2) {\n    let nodes = input[0].trim().split(/\\\\s+/);\n    let val = parseInt(input[1].trim());\n    let head = removeElements(buildList(nodes), val);\n    let res = [];\n    while (head) {\n        res.push(head.val);\n        head = head.next;\n    }\n    console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* buildList(char* line) {\n    char* token = strtok(line, \" \\t\\r\\n\");\n    if (!token) return NULL;\n    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));\n    head->val = atoi(token);\n    head->next = NULL;\n    struct ListNode* curr = head;\n    while ((token = strtok(NULL, \" \\t\\r\\n\"))) {\n        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n        curr->next->val = atoi(token);\n        curr->next->next = NULL;\n        curr = curr->next;\n    }\n    return head;\n}\n\nstruct ListNode* removeElements(struct ListNode* head, int val) {\n    // User logic here\n    return head;\n}\n\nint main() {\n    char line1[100000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        struct ListNode* head = removeElements(buildList(line1), atoi(line2));\n        while (head) {\n            printf(\"%d%s\", head->val, head->next ? \" \" : \"\");\n            head = head->next;\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 6 3 4 5 6\\n6", "expected_output": "1 2 3 4 5", "is_sample": True},
        {"input": "\\n1", "expected_output": "", "is_sample": True},
        {"input": "7 7 7 7\\n7", "expected_output": "", "is_sample": True},
        {"input": "1 2 3 4\\n5", "expected_output": "1 2 3 4", "is_sample": False},
        {"input": "1 2 3\\n1", "expected_output": "2 3", "is_sample": False},
        {"input": "1 2 3\\n3", "expected_output": "1 2", "is_sample": False},
        {"input": "1 1 2 2\\n1", "expected_output": "2 2", "is_sample": False},
        # Stress cases
        {"input": " ".join(["42"]*10000) + "\\n42", "expected_output": "", "is_sample": False},
        {"input": " ".join([str(i%10 + 1) for i in range(10000)]) + "\\n5", "expected_output": "...", "is_sample": False},
        {"input": "1 2 3\\n2", "expected_output": "1 3", "is_sample": False}
    ]
    
    # Stress case 9 expected output
    s9_res = [str(i%10 + 1) for i in range(10000) if (i%10 + 1) != 5]
    test_cases[8]["expected_output"] = " ".join(s9_res)

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

    output_path = "1-200/203_Remove_Linked_List_Elements.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
