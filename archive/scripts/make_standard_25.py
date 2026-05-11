import json
import os

def generate_json():
    problem_id = 25
    title = "Reverse Nodes in k-Group"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>25. Reverse Nodes in k-Group</h3>
<p>Given the <code>head</code> of a linked list, reverse the nodes of the list <code>k</code> at a time, and return the modified list.</p>

<p><code>k</code> is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of <code>k</code> then left-out nodes, in the end, should remain as it is.</p>

<p>You may not alter the values in the list&#39;s nodes, only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [2,1,4,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 3
<strong>Output:</strong> [3,2,1,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Can you solve the problem in <code>O(1)</code> extra memory space?"""

    input_format = "Line 1: Space-separated integers for the linked list 'head'.\nLine 2: An integer 'k'."
    output_format = "A list of integers representing the modified linked list."
    
    constraints = [
        "1 <= k <= n <= 5000",
        "0 <= Node.val <= 1000"
    ]
    
    explanation = """To reverse nodes in groups of k in a linked list using O(1) space:
1. Initialize a 'dummy' node pointing to the head for easier management of the list's beginning.
2. Use a pointer `prev_group_tail` initially at the dummy node to track the end of the previously processed group.
3. In each iteration:
   - Determine if there are at least `k` nodes remaining following `prev_group_tail`. If fewer than `k` nodes exist, the remaining nodes stay in their current order.
   - Store the start node of the current group (`group_start = prev_group_tail.next`) and the `k-th` node (`kth`).
   - Store the node following the current group (`next_part = kth.next`).
   - Reverse the nodes in the current group by reorienting their `next` pointers.
   - Connect `prev_group_tail.next` to the new head of the group (the former `kth` node).
   - Connect the new tail of the group (the former `group_start`) to `next_part`.
   - Update `prev_group_tail` to the new tail of the group to prepare for the next possible group.
4. Return `dummy.next` as the new modified head.

Time Complexity: O(N) where N is the total number of nodes.
Space Complexity: O(1) as swaps are done in-place."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if not head or k == 1:
        return head
    
    dummy = ListNode(0, head)
    prev_group_tail = dummy
    
    while True:
        # Check if k nodes exist
        kth = prev_group_tail
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        
        # Start of group and next part of list
        group_start = prev_group_tail.next
        next_part = kth.next
        
        # Reverse the group
        prev, curr = next_part, group_start
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Connect to the overall list
        prev_group_tail.next = kth
        prev_group_tail = group_start"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef reverseKGroup(head, k):\n    # User logic here\n    pass\n\ndef to_list(node):\n    res = []\n    while node:\n        res.append(node.val)\n        node = node.next\n    return res\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    head_data = input_data[0].strip() if len(input_data) > 0 else \"\"\n    k_data = input_data[1].strip() if len(input_data) > 1 else \"\"\n    head_list = [int(x) for x in head_data.split() if x]\n    k = int(k_data) if k_data else 1\n    \n    dummy = ListNode(0)\n    curr = dummy\n    for val in head_list:\n        curr.next = ListNode(val)\n        curr = curr.next\n    \n    res_node = reverseKGroup(dummy.next, k)\n    print(json.dumps(to_list(res_node)).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* reverseKGroup(ListNode* head, int k) {\n    // User logic\n    return head;\n}\n\nint main() {\n    string line;\n    ListNode dummy(0);\n    ListNode* curr = &dummy;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        while (ss >> val) {\n            curr->next = new ListNode(val);\n            curr = curr->next;\n        }\n    }\n    int k = 1;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        ss >> k;\n    }\n    \n    ListNode* res = reverseKGroup(dummy.next, k);\n    cout << \"[\";\n    while (res) {\n        cout << res->val;\n        if (res->next) cout << \", \";\n        res = res->next;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode reverseKGroup(ListNode head, int k) {\n        // User logic\n        return head;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line1 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        String line2 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        \n        ListNode dummy = new ListNode(0);\n        ListNode curr = dummy;\n        if (!line1.isEmpty()) {\n            String[] parts = line1.split(\"\\\\s+\");\n            for (String part : parts) {\n                curr.next = new ListNode(Integer.parseInt(part));\n                curr = curr.next;\n            }\n        }\n        \n        int k = 1;\n        if (!line2.isEmpty()) k = Integer.parseInt(line2);\n        \n        ListNode res = reverseKGroup(dummy.next, k);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction reverseKGroup(head, k) {\n    // User logic\n    return head;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nlet arr = [];\nlet k = 1;\nif (input.length > 0 && input[0].trim() !== '') arr = input[0].trim().split(/\\s+/).map(Number);\nif (input.length > 1 && input[1].trim() !== '') k = parseInt(input[1].trim());\n\nlet dummy = new ListNode(0);\nlet curr = dummy;\nfor (let val of arr) {\n    curr.next = new ListNode(val);\n    curr = curr.next;\n}\n\nlet res = reverseKGroup(dummy.next, k);\nlet out = [];\nwhile (res) {\n    out.push(res.val);\n    res = res.next;\n}\nconsole.log(JSON.stringify(out).replace(/,/g, \", \"));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* reverseKGroup(struct ListNode* head, int k) {\n    // User logic\n    return head;\n}\n\nint main() {\n    char line[20000];\n    \n    struct ListNode dummy; dummy.next = NULL;\n    struct ListNode* curr = &dummy;\n    \n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \" \\r\\n\");\n        while (token != NULL) {\n            curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n            curr->next->val = atoi(token);\n            curr->next->next = NULL;\n            curr = curr->next;\n            token = strtok(NULL, \" \\r\\n\");\n        }\n    }\n    \n    int k = 1;\n    if (fgets(line, sizeof(line), stdin)) {\n        k = atoi(line);\n    }\n    \n    struct ListNode* res = reverseKGroup(dummy.next, k);\n    printf(\"[\");\n    while (res != NULL) {\n        printf(\"%d\", res->val);\n        if (res->next != NULL) printf(\", \");\n        res = res->next;\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    def _reverse_ref(nums, k):
        res = list(nums)
        for i in range(0, len(res), k):
            if i + k <= len(res):
                res[i:i+k] = res[i:i+k][::-1]
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3 4 5\n2", "expected_output": str(_reverse_ref([1,2,3,4,5], 2)), "is_sample": True},
        {"input": "1 2 3 4 5\n3", "expected_output": str(_reverse_ref([1,2,3,4,5], 3)), "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1 2 3 4 5\n1", "expected_output": "[1, 2, 3, 4, 5]", "is_sample": False},
        {"input": "1 2 3 4 5\n5", "expected_output": "[5, 4, 3, 2, 1]", "is_sample": False},
        {"input": "1 2\n2", "expected_output": "[2, 1]", "is_sample": False},
        {"input": "1 2 3\n2", "expected_output": "[2, 1, 3]", "is_sample": False},
        {"input": "1 2 3 4 5 6\n3", "expected_output": "[3, 2, 1, 6, 5, 4]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\n2", "expected_output": str(_reverse_ref(range(1, 101), 2)), "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\n100", "expected_output": str(_reverse_ref(range(1, 101), 100)), "is_sample": False},
        {"input": " ".join(["0"]*100) + "\n10", "expected_output": str([0]*100), "is_sample": False}
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

    output_path = "1-200/25_Reverse_Nodes_in_k-Group.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
