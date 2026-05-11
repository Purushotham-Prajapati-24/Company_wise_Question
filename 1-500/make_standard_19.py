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
</ul>"""

    input_format = "Line 1: The 'head' array (e.g., [1,2,3,4,5]).\nLine 2: The 'n' integer."
    output_format = "A list representing the resulting linked list."
    
    constraints = [
        "1 <= sz <= 30",
        "0 <= Node.val <= 100",
        "1 <= n <= sz"
    ]
    
    explanation = """Use two pointers, 'fast' and 'slow'.
Move 'fast' pointer n steps forward.
Then move both pointers until 'fast' reaches the end.
'slow' will be pointing to the node before the one to be removed."""
    
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
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef removeNthFromEnd(head, n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        head_list = [int(x) for x in input_data[0].replace('[','').replace(']','').replace(',',' ').split()]\n        n = int(input_data[1].replace('[','').replace(']','').split('=')[-1].strip())\n        dummy = ListNode(0)\n        curr = dummy\n        for val in head_list:\n            curr.next = ListNode(val)\n            curr = curr.next\n        res = removeNthFromEnd(dummy.next, n)\n        out = []\n        while res:\n            out.append(res.val)\n            res = res.next\n        print(json.dumps(out).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* removeNthFromEnd(ListNode* head, int n) {\n    // User logic\n    return head;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n        stringstream ss(line);\n        ListNode dummy(0);\n        ListNode* curr = &dummy;\n        int val; while (ss >> val) { curr->next = new ListNode(val); curr = curr->next; }\n        int n = 0;\n        if (getline(cin, line)) {\n            string clean = \"\";\n            for(char c : line) if(isdigit(c)) clean += c;\n            if(!clean.empty()) n = stoi(clean);\n        }\n        ListNode* res = removeNthFromEnd(dummy.next, n);\n        cout << \"[\";\n        while (res) {\n            cout << res->val;\n            if (res->next) cout << \", \";\n            res = res->next;\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode removeNthFromEnd(ListNode head, int n) {\n        // User logic\n        return head;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine();\n        String[] parts = line1.replaceAll(\"[\\\\\\\\[\\\\\\\\],]\", \" \").trim().split(\"\\\\\\\\s+\");\n        ListNode dummy = new ListNode(0);\n        ListNode curr = dummy;\n        for (String p : parts) if(!p.isEmpty()) { curr.next = new ListNode(Integer.parseInt(p)); curr = curr.next; }\n        if (!sc.hasNextLine()) return;\n        String line2 = sc.nextLine().replaceAll(\"[^0-9]\", \"\");\n        int n = Integer.parseInt(line2);\n        ListNode res = removeNthFromEnd(dummy.next, n);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction removeNthFromEnd(head, n) {\n    // User logic\n    return head;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const head_arr = input[0].replace(/[\\\\[\\\\],]/g, ' ').trim().split(/\\\\s+/).filter(x => x !== '').map(Number);\n    const n = parseInt(input[1].replace(/[^0-9]/g, ''), 10);\n    let dummy = new ListNode(0);\n    let curr = dummy;\n    for (let val of head_arr) { curr.next = new ListNode(val); curr = curr.next; }\n    let res = removeNthFromEnd(dummy.next, n);\n    let out = [];\n    while (res) { out.push(res.val); res = res.next; }\n    console.log(JSON.stringify(out).split(',').join(', '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* removeNthFromEnd(struct ListNode* head, int n) {\n    // User logic\n    return head;\n}\n\nint main() {\n    char line[10000];\n    if (fgets(line, sizeof(line), stdin)) {\n        struct ListNode dummy;\n        dummy.next = NULL;\n        struct ListNode* curr = &dummy;\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                curr->next = malloc(sizeof(struct ListNode));\n                curr->next->val = atoi(p);\n                curr->next->next = NULL;\n                curr = curr->next;\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n        int n = 0;\n        if (fgets(line, sizeof(line), stdin)) {\n            char* q = line;\n            while (*q && !isdigit(*q)) q++;\n            if (*q) n = atoi(q);\n        }\n        struct ListNode* res = removeNthFromEnd(dummy.next, n);\n        printf(\"[\");\n        while (res) {\n            printf(\"%d\", res->val);\n            if (res->next) printf(\", \");\n            res = res->next;\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4,5]\n2", "expected_output": "[1, 2, 3, 5]", "is_sample": True},
        {"input": "[1]\n1", "expected_output": "[]", "is_sample": True},
        {"input": "[1,2]\n1", "expected_output": "[1]", "is_sample": True},
        {"input": "[1,2]\n2", "expected_output": "[2]", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10\n10", "expected_output": "[2, 3, 4, 5, 6, 7, 8, 9, 10]", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10\n1", "expected_output": "[1, 2, 3, 4, 5, 6, 7, 8, 9]", "is_sample": False},
        {"input": "1 2 3 4 5 6 7 8 9 10\n5", "expected_output": "[1, 2, 3, 4, 5, 7, 8, 9, 10]", "is_sample": False},
        {"input": "10 20 30 40 50\n3", "expected_output": "[10, 20, 40, 50]", "is_sample": False},
        {"input": "5 4 3 2 1\n4", "expected_output": "[5, 3, 2, 1]", "is_sample": False},
        {"input": "1 1 1 1 1\n3", "expected_output": "[1, 1, 1, 1]", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_title": title,
        "difficulty": difficulty,
        "marks": marks,
        "question_text": html_description,
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
