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
</ul>
"""

    input_format = "A single line containing space-separated integers for the linked list 'head'."
    output_format = "A list of integers representing the modified linked list."
    
    constraints = [
        "0 <= number of nodes <= 100",
        "0 <= Node.val <= 100"
    ]
    
    explanation = """To swap every two adjacent nodes in a linked list:
1. Use a 'dummy' node that points to the head of the list. This simplifies handling the swapping of the first pair.
2. Initialize a pointer `prev` at the dummy node.
3. Iterate while there are at least two nodes (`prev.next` and `prev.next.next`) remaining:
   - Identify the two nodes to swap: `first = prev.next` and `second = prev.next.next`.
   - Update `prev.next` to point to `second`.
   - Update `first.next` to point to `second.next` (the node after the pair).
   - Update `second.next` to point to `first`, completing the swap.
   - Move the `prev` pointer to `first` to process the next pair of nodes.
4. Return `dummy.next` as the new head.

Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(1) as only a few pointers are used."""
    
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
        
        # Swapping
        first.next = second.next
        second.next = first
        prev.next = second
        
        # Move forward
        prev = first
    return dummy.next"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef swapPairs(head):\n    # User logic here\n    pass\n\ndef to_list(node):\n    res = []\n    while node:\n        res.append(node.val)\n        node = node.next\n    return res\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    head_list = [int(x) for x in data.split() if x]\n    dummy = ListNode(0)\n    curr = dummy\n    for val in head_list:\n        curr.next = ListNode(val)\n        curr = curr.next\n    res_node = swapPairs(dummy.next)\n    print(json.dumps(to_list(res_node)).replace(',', ', '))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode() : val(0), next(nullptr) {}\n    ListNode(int x) : val(x), next(nullptr) {}\n    ListNode(int x, ListNode *next) : val(x), next(next) {}\n};\n\nListNode* swapPairs(ListNode* head) {\n    // User logic\n    return nullptr;\n}\n\nint main() {\n    string line;\n    ListNode dummy(0);\n    ListNode* curr = &dummy;\n    if (getline(cin, line)) {\n        stringstream ss(line);\n        int val;\n        while (ss >> val) {\n            curr->next = new ListNode(val);\n            curr = curr->next;\n        }\n    }\n    \n    ListNode* res = swapPairs(dummy.next);\n    cout << \"[\";\n    while (res) {\n        cout << res->val;\n        if (res->next) cout << \", \";\n        res = res->next;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode() {}\n    ListNode(int val) { this.val = val; }\n    ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n}\n\npublic class Main {\n    public static ListNode swapPairs(ListNode head) {\n        // User logic\n        return null;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line = sc.hasNextLine() ? sc.nextLine().trim() : \"\";\n        \n        ListNode dummy = new ListNode(0);\n        ListNode curr = dummy;\n        if (!line.isEmpty()) {\n            String[] parts = line.split(\"\\\\s+\");\n            for (String part : parts) {\n                curr.next = new ListNode(Integer.parseInt(part));\n                curr = curr.next;\n            }\n        }\n        \n        ListNode res = swapPairs(dummy.next);\n        System.out.print(\"[\");\n        while (res != null) {\n            System.out.print(res.val);\n            if (res.next != null) System.out.print(\", \");\n            res = res.next;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction swapPairs(head) {\n    // User logic\n    return null;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nlet arr = [];\nif (input.length > 0 && input[0].trim() !== '') arr = input[0].trim().split(/\\s+/).map(Number);\n\nlet dummy = new ListNode(0);\nlet curr = dummy;\nfor (let val of arr) {\n    curr.next = new ListNode(val);\n    curr = curr.next;\n}\n\nlet res = swapPairs(dummy.next);\nlet out = [];\nwhile (res) {\n    out.push(res.val);\n    res = res.next;\n}\nconsole.log(JSON.stringify(out).replace(/,/g, \", \"));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* swapPairs(struct ListNode* head) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    char line[20000];\n    \n    struct ListNode dummy; dummy.next = NULL;\n    struct ListNode* curr = &dummy;\n    \n    if (fgets(line, sizeof(line), stdin)) {\n        char* token = strtok(line, \" \\r\\n\");\n        while (token != NULL) {\n            curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n            curr->next->val = atoi(token);\n            curr->next->next = NULL;\n            curr = curr->next;\n            token = strtok(NULL, \" \\r\\n\");\n        }\n    }\n    \n    struct ListNode* res = swapPairs(dummy.next);\n    printf(\"[\");\n    while (res != NULL) {\n        printf(\"%d\", res->val);\n        if (res->next != NULL) printf(\", \");\n        res = res->next;\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    def _swap_ref(nums):
        res = list(nums)
        for i in range(0, len(res) - 1, 2):
            res[i], res[i+1] = res[i+1], res[i]
        return res

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3 4", "expected_output": str(_swap_ref([1,2,3,4])), "is_sample": True},
        {"input": "", "expected_output": "[]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[2, 1, 3]", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "[2, 1, 4, 3, 5]", "is_sample": False},
        {"input": "1 1", "expected_output": "[1, 1]", "is_sample": False},
        {"input": "10 20 30 40", "expected_output": "[20, 10, 40, 30]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(1, 101)]), "expected_output": str(_swap_ref(range(1, 101))), "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 100)]), "expected_output": str(_swap_ref(range(1, 100))), "is_sample": False},
        {"input": " ".join(["100"]*100), "expected_output": str(_swap_ref([100]*100)), "is_sample": False}
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

    output_path = "1-200/24_Swap_Nodes_in_Pairs.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
