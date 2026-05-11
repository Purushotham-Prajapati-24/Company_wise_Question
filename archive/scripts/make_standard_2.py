import json
import os

def generate_json():
    problem_id = 2
    title = "Add Two Numbers"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>2. Add Two Numbers</h3>
<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>
"""

    input_format = "Line 1: Space-separated integers for the first linked list.\nLine 2: Space-separated integers for the second linked list."
    output_format = "A list of integers representing the sum in reverse order."
    
    constraints = [
        "1 <= nodes in each list <= 100",
        "0 <= Node.val <= 9",
        "No leading zeros (except for 0 itself)."
    ]
    
    explanation = """To add two numbers represented as linked lists in reverse order:
1. Initialize a dummy node to simplify list construction and a 'curr' pointer.
2. Maintain a 'carry' variable initialized to 0.
3. Iterate through both lists until both are exhausted and carry becomes 0.
4. In each step:
   - Extract values from the current nodes of l1 and l2 (if they exist, else 0).
   - Compute the sum: total = val1 + val2 + carry.
   - Update carry: carry = total // 10.
   - Create a new node with value (total % 10) and link it to the current node.
   - Move the pointers of l1, l2, and curr forward.
5. Return the 'next' of the dummy node as the resulting list head.

This approach ensures we handle numbers of different lengths and trailing carries efficiently in O(max(M, N)) time and space, where M and N are lengths of the input lists."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum_val = val1 + val2 + carry
        carry = sum_val // 10
        curr.next = ListNode(sum_val % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef addTwoNumbers(l1, l2):\n    # User logic here\n    pass\n\ndef build_list(nums):\n    dummy = ListNode(0)\n    curr = dummy\n    for n in nums:\n        curr.next = ListNode(n)\n        curr = curr.next\n    return dummy.next\n\ndef print_list(node):\n    res = []\n    while node:\n        res.append(str(node.val))\n        node = node.next\n    print(\"[\" + \", \".join(res) + \"]\")\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 2:\n        nums1 = [int(x) for x in data[0].strip().split()] if data[0].strip() else []\n        nums2 = [int(x) for x in data[1].strip().split()] if data[1].strip() else []\n        l1 = build_list(nums1)\n        l2 = build_list(nums2)\n        print_list(addTwoNumbers(l1, l2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\n#include <string>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n    // User logic\n    return nullptr;\n}\n\nListNode* build_list(const string& line) {\n    istringstream iss(line);\n    int num;\n    ListNode dummy(0);\n    ListNode* curr = &dummy;\n    while (iss >> num) {\n        curr->next = new ListNode(num);\n        curr = curr->next;\n    }\n    return dummy.next;\n}\n\nvoid print_list(ListNode* node) {\n    cout << \"[\";\n    bool first = true;\n    while (node) {\n        if (!first) cout << \", \";\n        cout << node->val;\n        first = false;\n        node = node->next;\n    }\n    cout << \"]\" << endl;\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        ListNode* l1 = build_list(line1);\n        ListNode* l2 = build_list(line2);\n        ListNode* res = addTwoNumbers(l1, l2);\n        print_list(res);\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        // User logic\n        return null;\n    }\n\n    public static ListNode buildList(String line) {\n        line = line.trim();\n        if (line.isEmpty()) return null;\n        String[] parts = line.split(\"\\\\s+\");\n        ListNode dummy = new ListNode(0);\n        ListNode curr = dummy;\n        for (String p : parts) {\n            curr.next = new ListNode(Integer.parseInt(p));\n            curr = curr.next;\n        }\n        return dummy.next;\n    }\n\n    public static void printList(ListNode node) {\n        System.out.print(\"[\");\n        boolean first = true;\n        while (node != null) {\n            if (!first) System.out.print(\", \");\n            System.out.print(node.val);\n            first = false;\n            node = node.next;\n        }\n        System.out.println(\"]\");\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String l1Str = sc.nextLine();\n            String l2Str = sc.hasNextLine() ? sc.nextLine() : \"\";\n            ListNode l1 = buildList(l1Str);\n            ListNode l2 = buildList(l2Str);\n            ListNode res = addTwoNumbers(l1, l2);\n            printList(res);\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction addTwoNumbers(l1, l2) {\n    // User logic\n    return null;\n}\n\nfunction buildList(parts) {\n    let dummy = new ListNode(0);\n    let curr = dummy;\n    for (const p of parts) {\n        if (p) {\n            curr.next = new ListNode(parseInt(p));\n            curr = curr.next;\n        }\n    }\n    return dummy.next;\n}\n\nfunction printList(node) {\n    let res = [];\n    while (node) {\n        res.push(node.val);\n        node = node.next;\n    }\n    console.log(\"[\" + res.join(\", \") + \"]\");\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (input.length >= 2) {\n    const l1 = buildList(input[0].trim().split(/\\s+/));\n    const l2 = buildList(input[1].trim().split(/\\s+/));\n    const res = addTwoNumbers(l1, l2);\n    printList(res);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {\n    // User logic\n    return NULL;\n}\n\nstruct ListNode* buildList(char* line) {\n    struct ListNode dummy;\n    dummy.next = NULL;\n    struct ListNode* curr = &dummy;\n    char* pt = line;\n    while (*pt != '\\0') {\n        if (isdigit(*pt) || (*pt == '-' && isdigit(*(pt+1)))) {\n            struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));\n            node->val = atoi(pt);\n            node->next = NULL;\n            curr->next = node;\n            curr = node;\n            while (*pt != '\\0' && (isdigit(*pt) || *pt == '-')) pt++;\n        } else { pt++; }\n    }\n    return dummy.next;\n}\n\nvoid printList(struct ListNode* node) {\n    printf(\"[\");\n    int first = 1;\n    while (node) {\n        if (!first) printf(\", \");\n        printf(\"%d\", node->val);\n        first = 0;\n        node = node->next;\n    }\n    printf(\"]\\n\");\n}\n\nint main() {\n    char line1[100000];\n    char line2[100000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        struct ListNode* l1 = buildList(line1);\n        struct ListNode* l2 = buildList(line2);\n        struct ListNode* res = addTwoNumbers(l1, l2);\n        printList(res);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "2 4 3\n5 6 4", "expected_output": "[7, 0, 8]", "is_sample": True},
        {"input": "0\n0", "expected_output": "[0]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "9 9 9 9 9 9 9\n9 9 9 9", "expected_output": "[8, 9, 9, 9, 0, 0, 0, 1]", "is_sample": False},
        {"input": "1 8\n0", "expected_output": "[1, 8]", "is_sample": False},
        {"input": "5\n5", "expected_output": "[0, 1]", "is_sample": False},
        {"input": "2 4\n5 6", "expected_output": "[7, 0, 1]", "is_sample": False},
        {"input": "1 2 3\n4 5 6", "expected_output": "[5, 7, 9]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["9"] * 100) + "\n" + " ".join(["9"] * 100), "expected_output": "[" + ", ".join(["8"] + ["9"]*99 + ["1"]) + "]", "is_sample": False},
        {"input": " ".join(["9"] * 100) + "\n1", "expected_output": "[" + ", ".join(["0"] + ["0"]*99 + ["1"]) + "]", "is_sample": False},
        {"input": " ".join(["1"] * 100) + "\n" + " ".join(["1"] * 100), "expected_output": "[" + ", ".join(["2"] * 100) + "]", "is_sample": False}
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
        "topics": ["Linked List", "Math", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/2_Add_Two_Numbers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
