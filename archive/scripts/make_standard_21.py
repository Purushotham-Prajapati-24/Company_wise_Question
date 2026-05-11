import json
import os

def generate_json():
    problem_id = 21
    title = "Merge Two Sorted Lists"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>21. Merge Two Sorted Lists</h3>
<p>You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.</p>

<p>Merge the two lists into one <strong>sorted</strong> list. The list should be made by splicing together the nodes of the first two lists.</p>

<p>Return <em>the head of the merged linked list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>Input:</strong> list1 = [1,2,4], list2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [], list2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in both lists is in the range <code>[0, 50]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>Both <code>list1</code> and <code>list2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>
"""

    input_format = "Line 1: Space-separated integers for the first sorted list.\nLine 2: Space-separated integers for the second sorted list."
    output_format = "A list of integers representing the merged sorted list."
    
    constraints = [
        "0 <= nodes in both lists <= 50",
        "-100 <= Node.val <= 100",
        "Both lists are sorted in non-decreasing order."
    ]
    
    explanation = """To merge two sorted linked lists into one sorted list:
1. Initialize a 'dummy' node to act as the head of the merged list and a 'curr' pointer.
2. Iterate while both lists have remaining nodes:
   - Compare the current values of both lists.
   - Attach the node with the smaller value to 'curr.next'.
   - Move the pointer of the selected list forward.
   - Move the 'curr' pointer forward.
3. If one list reaches the end before the other, attach the remaining part of the non-empty list to 'curr.next'.
4. Return 'dummy.next' as the head of the merged sorted list.

Time Complexity: O(M + N) where M and N are lengths of both lists.
Space Complexity: O(1) as we are splicing nodes instead of creating new ones."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef mergeTwoLists(list1, list2):\n    # User logic here\n    pass\n\ndef to_list(node):\n    res = []\n    while node:\n        res.append(node.val)\n        node = node.next\n    return res\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    l1_data = input_data[0].strip() if len(input_data) > 0 else \"\"\n    l2_data = input_data[1].strip() if len(input_data) > 1 else \"\"\n    \n    l1_list = [int(x.strip('[],')) for x in l1_data.split() if x.strip('[],')]\n    l2_list = [int(x.strip('[],')) for x in l2_data.split() if x.strip('[],')]\n    \n    dummy1 = ListNode(0)\n    curr1 = dummy1\n    for val in l1_list:\n        curr1.next = ListNode(val)\n        curr1 = curr1.next\n        \n    dummy2 = ListNode(0)\n    curr2 = dummy2\n    for val in l2_list:\n        curr2.next = ListNode(val)\n        curr2 = curr2.next\n        \n    res_node = mergeTwoLists(dummy1.next, dummy2.next)\n    print(json.dumps(to_list(res_node)).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {\n    // User logic\n    return nullptr;\n}\n\nint main() {\n    string line;\n    ListNode dummy1(0);\n    ListNode* curr1 = &dummy1;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        while (ss >> val) {\n            curr1->next = new ListNode(val);\n            curr1 = curr1->next;\n        }\n    }\n    \n    ListNode dummy2(0);\n    ListNode* curr2 = &dummy2;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        while (ss >> val) {\n            curr2->next = new ListNode(val);\n            curr2 = curr2->next;\n        }\n    }\n    \n    ListNode* res = mergeTwoLists(dummy1.next, dummy2.next);\n    cout << \"[\";\n    while (res) {\n        cout << res->val;\n        if (res->next) cout << \", \";\n        res = res->next;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {\n        // User logic\n        return null;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line1 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        String line2 = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        \n        ListNode dummy1 = new ListNode(0);\n        ListNode curr1 = dummy1;\n        if (!line1.isEmpty()) {\n            String[] parts = line1.split(\"\\\\s+\");\n            for (String part : parts) {\n                curr1.next = new ListNode(Integer.parseInt(part));\n                curr1 = curr1.next;\n            }\n        }\n        \n        ListNode dummy2 = new ListNode(0);\n        ListNode curr2 = dummy2;\n        if (!line2.isEmpty()) {\n            String[] parts = line2.split(\"\\\\s+\");\n            for (String part : parts) {\n                curr2.next = new ListNode(Integer.parseInt(part));\n                curr2 = curr2.next;\n            }\n        }\n        \n        ListNode res = mergeTwoLists(dummy1.next, dummy2.next);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction mergeTwoLists(list1, list2) {\n    // User logic\n    return null;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nlet l1_arr = [];\nlet l2_arr = [];\nif (input.length > 0 && input[0].trim() !== '') l1_arr = input[0].trim().split(/\\s+/).map(Number);\nif (input.length > 1 && input[1].trim() !== '') l2_arr = input[1].trim().split(/\\s+/).map(Number);\n\nlet dummy1 = new ListNode(0);\nlet curr1 = dummy1;\nfor (let val of l1_arr) {\n    curr1.next = new ListNode(val);\n    curr1 = curr1.next;\n}\n\nlet dummy2 = new ListNode(0);\nlet curr2 = dummy2;\nfor (let val of l2_arr) {\n    curr2.next = new ListNode(val);\n    curr2 = curr2.next;\n}\n\nlet res = mergeTwoLists(dummy1.next, dummy2.next);\nlet out = [];\nwhile (res) {\n    out.push(res.val);\n    res = res.next;\n}\nconsole.log(JSON.stringify(out).replace(/,/g, \", \"));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    char line1[20000];\n    char line2[20000];\n    \n    struct ListNode dummy1; dummy1.next = NULL;\n    struct ListNode dummy2; dummy2.next = NULL;\n    struct ListNode* curr1 = &dummy1;\n    struct ListNode* curr2 = &dummy2;\n    \n    if (fgets(line1, sizeof(line1), stdin)) {\n        char* token = strtok(line1, \" \\r\\n\");\n        while (token != NULL) {\n            curr1->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n            curr1->next->val = atoi(token);\n            curr1->next->next = NULL;\n            curr1 = curr1->next;\n            token = strtok(NULL, \" \\r\\n\");\n        }\n    }\n    \n    if (fgets(line2, sizeof(line2), stdin)) {\n        char* token = strtok(line2, \" \\r\\n\");\n        while (token != NULL) {\n            curr2->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n            curr2->next->val = atoi(token);\n            curr2->next->next = NULL;\n            curr2 = curr2->next;\n            token = strtok(NULL, \" \\r\\n\");\n        }\n    }\n    \n    struct ListNode* res = mergeTwoLists(dummy1.next, dummy2.next);\n    printf(\"[\");\n    while (res != NULL) {\n        printf(\"%d\", res->val);\n        if (res->next != NULL) printf(\", \");\n        res = res->next;\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 4\n1 3 4", "expected_output": "[1, 1, 2, 3, 4, 4]", "is_sample": True},
        {"input": "\n", "expected_output": "[]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "\n0", "expected_output": "[0]", "is_sample": False},
        {"input": "1 3 5 7\n2 4 6 8", "expected_output": "[1, 2, 3, 4, 5, 6, 7, 8]", "is_sample": False},
        {"input": "1 1 1\n1 1 1", "expected_output": "[1, 1, 1, 1, 1, 1]", "is_sample": False},
        {"input": "10 20 30\n5 15 25", "expected_output": "[5, 10, 15, 20, 25, 30]", "is_sample": False},
        {"input": "1 2 3 4 5\n", "expected_output": "[1, 2, 3, 4, 5]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(-50, 0)]) + "\n" + " ".join([str(i) for i in range(0, 51)]), "expected_output": str([i for i in range(-50, 51)]), "is_sample": False},
        {"input": " ".join(["-100"]*25) + "\n" + " ".join(["100"]*25), "expected_output": str([-100]*25 + [100]*25), "is_sample": False},
        {"input": " ".join([str(i*2) for i in range(25)]) + "\n" + " ".join([str(i*2+1) for i in range(25)]), "expected_output": str([i for i in range(50)]), "is_sample": False}
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

    output_path = "1-200/21_Merge_Two_Sorted_Lists.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
