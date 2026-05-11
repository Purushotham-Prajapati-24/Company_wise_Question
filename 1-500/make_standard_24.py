import json
import os

def generate_json():
    problem_id = 24
    title = "Swap Nodes in Pairs"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>24. Swap Nodes in Pairs</h3>
<p>Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [2,1,4,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> head = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the list is in the range <code>[0, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>"""

    input_format = "A list of integers representing the linked list."
    output_format = "A list of integers representing the modified linked list."
    
    constraints = [
        "The number of nodes in the list is in the range [0, 100].",
        "0 <= Node.val <= 100"
    ]
    
    explanation = """Use a dummy node to simplify edge cases.
Iterate through the list in pairs.
For each pair, perform the swap by adjusting the pointers of the current pair and the preceding node."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef swapPairs(head):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if not data or data == '[]':\n        print(\"[]\")\n        sys.exit()\n    \n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    \n    dummy = ListNode()\n    curr = dummy\n    for n in nums: curr.next = ListNode(n); curr = curr.next\n    \n    res = swapPairs(dummy.next)\n    out = []\n    while res: out.append(res.val); res = res.next\n    print(json.dumps(out).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* swapPairs(ListNode* head) {\n    // User logic\n    return nullptr;\n}\n\nint main() {\n    string line;\n    if (!getline(cin, line)) return 0;\n    for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n    stringstream ss(line);\n    string part;\n    ListNode dummy(0);\n    ListNode* curr = &dummy;\n    while (ss >> part) {\n        if (part == \"head\" || part == \"=\") continue;\n        curr->next = new ListNode(stoi(part));\n        curr = curr->next;\n    }\n    \n    ListNode* res = swapPairs(dummy.next);\n    cout << \"[\";\n    while (res) {\n        cout << res->val;\n        if (res->next) cout << \", \";\n        res = res->next;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode swapPairs(ListNode head) {\n        // User logic\n        return null;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line = sc.nextLine().replaceAll(\"[\\\\[\\\\]=,head]\", \" \").trim();\n        String[] parts = line.split(\"\\\\s+\");\n        ListNode dummy = new ListNode(0);\n        ListNode curr = dummy;\n        for (String p : parts) if (!p.isEmpty()) { curr.next = new ListNode(Integer.parseInt(p)); curr = curr.next; }\n        \n        ListNode res = swapPairs(dummy.next);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction swapPairs(head) {\n    // User logic\n    return null;\n}\n\nconst data = fs.readFileSync(0, 'utf-8').trim();\nif (!data || data === '[]') { console.log(\"[]\"); process.exit(0); }\nconst nums = data.match(/-?\\d+/g).map(Number);\n\nlet dummy = new ListNode(0);\nlet curr = dummy;\nfor (let n of nums) { curr.next = new ListNode(n); curr = curr.next; }\n\nlet res = swapPairs(dummy.next);\nlet out = [];\nwhile (res) { out.push(res.val); res = res.next; }\nconsole.log(JSON.stringify(out).split(',').join(', '));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* swapPairs(struct ListNode* head) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    char line[10000];\n    if (!fgets(line, sizeof(line), stdin)) return 0;\n    struct ListNode dummy; dummy.next = NULL;\n    struct ListNode* curr = &dummy;\n    char* p = line;\n    while (*p) {\n        while (*p && !isdigit(*p) && *p != '-') p++;\n        if (*p) {\n            curr->next = malloc(sizeof(struct ListNode));\n            curr->next->val = atoi(p);\n            curr->next->next = NULL;\n            curr = curr->next;\n            if (*p == '-') p++;\n            while (*p && isdigit(*p)) p++;\n        }\n    }\n    struct ListNode* res = swapPairs(dummy.next);\n    printf(\"[\");\n    while (res) {\n        printf(\"%d\", res->val);\n        if (res->next) printf(\", \");\n        res = res->next;\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4]", "expected_output": "[2, 1, 4, 3]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1]", "is_sample": True},
        {"input": "[1,2]", "expected_output": "[2, 1]", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "[2, 1, 3]", "is_sample": False},
        {"input": "[1,2,3,4,5,6]", "expected_output": "[2, 1, 4, 3, 6, 5]", "is_sample": False},
        {"input": "[1,1,1,1]", "expected_output": "[1, 1, 1, 1]", "is_sample": False},
        {"input": "[10,20,30,40,50]", "expected_output": "[20, 10, 40, 30, 50]", "is_sample": False},
        {"input": "[-1,-2,-3,-4]", "expected_output": "[-2, -1, -4, -3]", "is_sample": False},
        {"input": "[0,0,0]", "expected_output": "[0, 0, 0]", "is_sample": False}
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
        "topics": ["Linked List", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/24_Swap_Nodes_in_Pairs.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
