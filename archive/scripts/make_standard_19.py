import json
import os

def generate_json():
    problem_id = 19
    title = "Remove Nth Node From End of List"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>19. Remove Nth Node From End of List</h3>
<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do this in one pass?"""

    input_format = "Line 1: Space-separated integers for the linked list 'head'.\nLine 2: An integer 'n'."
    output_format = "A string representing the resulting linked list."
    
    constraints = [
        "1 <= sz <= 30",
        "0 <= Node.val <= 100",
        "1 <= n <= sz"
    ]
    
    explanation = """To remove the Nth node from the end of a linked list in one pass:
1. Use the 'Two-Pointer' technique with a 'fast' and a 'slow' pointer.
2. Initialize a dummy node pointing to the head to handle cases like removing the head itself.
3. Advance the 'fast' pointer `n + 1` steps forward.
4. Advance both 'fast' and 'slow' pointers together until 'fast' reaches the end (None).
5. At this point, 'slow' will be pointing to the node *before* the Nth node from the end.
6. Bypass the Nth node by setting `slow.next = slow.next.next`.
7. Return `dummy.next` as the new head.

Time Complexity: O(L) where L is the length of the list.
Space Complexity: O(1)."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef removeNthFromEnd(head, n):\n    # User logic here\n    pass\n\ndef to_list(node):\n    res = []\n    while node:\n        res.append(node.val)\n        node = node.next\n    return res\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    head_data = input_data[0].strip() if len(input_data) > 0 else \"\"\n    n_data = input_data[1].strip() if len(input_data) > 1 else \"\"\n    \n    head_list = [int(x.strip('[],')) for x in head_data.split() if x.strip('[],')]\n    n = int(n_data) if n_data else 0\n    \n    dummy = ListNode(0)\n    curr = dummy\n    for val in head_list:\n        curr.next = ListNode(val)\n        curr = curr.next\n        \n    res_node = removeNthFromEnd(dummy.next, n)\n    print(json.dumps(to_list(res_node)).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* removeNthFromEnd(ListNode* head, int n) {\n    // User logic\n    return head;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        ListNode dummy(0);\n        ListNode* curr = &dummy;\n        while (ss >> val) {\n            curr->next = new ListNode(val);\n            curr = curr->next;\n        }\n        int n = 0;\n        if (getline(cin, line)) {\n            stringstream ss2(line);\n            ss2 >> n;\n        }\n        ListNode* res = removeNthFromEnd(dummy.next, n);\n        cout << \"[\";\n        while (res) {\n            cout << res->val;\n            if (res->next) cout << \", \";\n            res = res->next;\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode removeNthFromEnd(ListNode head, int n) {\n        // User logic\n        return head;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line1 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        String line2 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        \n        ListNode dummy = new ListNode(0);\n        ListNode curr = dummy;\n        if (!line1.isEmpty()) {\n            String[] parts = line1.split(\"\\\\s+\");\n            for (String part : parts) {\n                curr.next = new ListNode(Integer.parseInt(part));\n                curr = curr.next;\n            }\n        }\n        int n = line2.isEmpty() ? 0 : Integer.parseInt(line2);\n        \n        ListNode res = removeNthFromEnd(dummy.next, n);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction removeNthFromEnd(head, n) {\n    // User logic\n    return head;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const head_arr = input[0].trim() === '' ? [] : input[0].trim().split(/\\s+/).map(Number);\n    const n = parseInt(input[1].trim(), 10);\n    \n    let dummy = new ListNode(0);\n    let curr = dummy;\n    for (let val of head_arr) {\n        curr.next = new ListNode(val);\n        curr = curr.next;\n    }\n    \n    let res = removeNthFromEnd(dummy.next, n);\n    let out = [];\n    while (res) {\n        out.push(res.val);\n        res = res.next;\n    }\n    console.log(JSON.stringify(out).replace(/,/g, \", \"));\n} else {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* removeNthFromEnd(struct ListNode* head, int n) {\n    // User logic\n    return head;\n}\n\nint main() {\n    char line1[20000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin)) {\n        struct ListNode dummy;\n        dummy.next = NULL;\n        struct ListNode* curr = &dummy;\n        \n        char* token = strtok(line1, \" \\r\\n\");\n        while (token != NULL) {\n            curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n            curr->next->val = atoi(token);\n            curr->next->next = NULL;\n            curr = curr->next;\n            token = strtok(NULL, \" \\r\\n\");\n        }\n        \n        int n = 0;\n        if (fgets(line2, sizeof(line2), stdin)) {\n            n = atoi(line2);\n        }\n        \n        struct ListNode* res = removeNthFromEnd(dummy.next, n);\n        printf(\"[\");\n        while (res != NULL) {\n            printf(\"%d\", res->val);\n            if (res->next != NULL) printf(\", \");\n            res = res->next;\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3 4 5\n2", "expected_output": "[1, 2, 3, 5]", "is_sample": True},
        {"input": "1\n1", "expected_output": "[]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1 2\n1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2\n2", "expected_output": "[2]", "is_sample": False},
        {"input": "1 2 3\n3", "expected_output": "[2, 3]", "is_sample": False},
        {"input": "1 2 3\n1", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "1 2 3 4 5 6\n4", "expected_output": "[1, 2, 4, 5, 6]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(30)]) + "\n30", "expected_output": str([i for i in range(1, 30)]), "is_sample": False},
        {"input": " ".join([str(i) for i in range(30)]) + "\n1", "expected_output": str([i for i in range(29)]), "is_sample": False},
        {"input": " ".join([str(i) for i in range(30)]) + "\n15", "expected_output": str([i for i in range(15)] + [i for i in range(16, 30)]), "is_sample": False}
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
        "topics": ["Linked List", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/19_Remove_Nth_Node_From_End_of_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
