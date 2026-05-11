import json
import os

def generate_json():
    problem_id = 445
    title = "Add Two Numbers II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>445. Add Two Numbers II</h3>
<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg" style="width: 523px; height: 199px;" />
<pre><strong>Input:</strong> l1 = [7,2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,8,0,7]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [8,0,7]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it without reversing the input lists?</p>"""

    input_format = "Two lines: l1 (JSON array) and l2 (JSON array)."
    output_format = "A JSON array representing the sum linked list."
    
    constraints = [
        "1 <= number of nodes <= 100",
        "0 <= Node.val <= 9",
        "No leading zeros."
    ]
    
    explanation = """To add two numbers represented by linked lists where the most significant digit comes first, we can use two stacks to store the digits of each list. We then pop values from the stacks to add them from least significant to most significant, keeping track of the carry and building the result list from back to front."""
    
    answer = """class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        dummy = None
        carry = 0
        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            
            node = ListNode(total % 10)
            node.next = dummy
            dummy = node
            
        return dummy"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef build_list(data):\n    if not data: return None\n    dummy = ListNode(0)\n    curr = dummy\n    for v in data:\n        curr.next = ListNode(v)\n        curr = curr.next\n    return dummy.next\n\ndef list_to_array(head):\n    res = []\n    while head:\n        res.append(head.val)\n        head = head.next\n    return res\n\nclass Solution:\n    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:\n        # User logic here\n        return None\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        l1 = build_list(json.loads(input_data[0]))\n        l2 = build_list(json.loads(input_data[1]))\n        sol = Solution()\n        res = sol.addTwoNumbers(l1, l2)\n        print(json.dumps(list_to_array(res)).replace(\" \", \"\"))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nclass Solution {\npublic:\n    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {\n        // User logic here\n        return NULL;\n    }\n};\n\nListNode* buildList(string s) {\n    s.erase(remove(s.begin(), s.end(), '['), s.end());\n    s.erase(remove(s.begin(), s.end(), ']'), s.end());\n    s.erase(remove(s.begin(), s.end(), ' '), s.end());\n    if (s.empty()) return NULL;\n    stringstream ss(s);\n    string item;\n    ListNode *dummy = new ListNode(0), *curr = dummy;\n    while (getline(ss, item, ',')) {\n        curr->next = new ListNode(stoi(item));\n        curr = curr->next;\n    }\n    return dummy->next;\n}\n\nvoid printList(ListNode* head) {\n    cout << \"[\";\n    while (head) {\n        cout << head->val << (head->next ? \",\" : \"\");\n        head = head->next;\n    }\n    cout << \"]\" << endl;\n}\n\nint main() {\n    string s1, s2;\n    if (getline(cin, s1) && getline(cin, s2)) {\n        Solution sol;\n        printList(sol.addTwoNumbers(buildList(s1), buildList(s2)));\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\nclass Solution {\n    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {\n        // User logic here\n        return null;\n    }\n}\n\npublic class Main {\n    private static ListNode buildList(String s) {\n        s = s.replace(\"[\", \"\").replace(\"]\", \"\").replace(\" \", \"\");\n        if (s.isEmpty()) return null;\n        String[] parts = s.split(\",\");\n        ListNode dummy = new ListNode(0), curr = dummy;\n        for (String p : parts) {\n            curr.next = new ListNode(Integer.parseInt(p));\n            curr = curr.next;\n        }\n        return dummy.next;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            ListNode l1 = buildList(sc.nextLine());\n            ListNode l2 = sc.hasNextLine() ? buildList(sc.nextLine()) : null;\n            ListNode res = new Solution().addTwoNumbers(l1, l2);\n            StringBuilder sb = new StringBuilder(\"[\");\n            while (res != null) {\n                sb.append(res.val).append(res.next != null ? \",\" : \"\");\n                res = res.next;\n            }\n            System.out.println(sb.append(\"]\").toString());\n        }\n    }\n}",
        "javascript": "function ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val);\n    this.next = (next===undefined ? null : next);\n}\n\nvar addTwoNumbers = function(l1, l2) {\n    // User logic here\n};\n\nconst fs = require('fs');\nfunction buildList(arr) {\n    let dummy = new ListNode(0), curr = dummy;\n    for (let v of arr) {\n        curr.next = new ListNode(v);\n        curr = curr.next;\n    }\n    return dummy.next;\n}\nfunction toArray(head) {\n    let res = [];\n    while (head) { res.push(head.val); head = head.next; }\n    return res;\n}\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const l1 = buildList(JSON.parse(input[0]));\n    const l2 = buildList(JSON.parse(input[1]));\n    console.log(JSON.stringify(toArray(addTwoNumbers(l1, l2))).replace(/\\s/g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[7,2,4,3]\\n[5,6,4]", "expected_output": "[7,8,0,7]", "is_sample": True},
        {"input": "[2,4,3]\\n[5,6,4]", "expected_output": "[8,0,7]", "is_sample": True},
        {"input": "[0]\\n[0]", "expected_output": "[0]", "is_sample": True},
        {"input": "[ 7, 2, 4, 3 ]\\n[ 5, 6, 4 ]", "expected_output": "[7,8,0,7]", "is_sample": False}, # Spaces
        {"input": "[9,9,9]\\n[1]", "expected_output": "[1,0,0,0]", "is_sample": False},
        {"input": "[1,2,3]\\n[9,8,7]", "expected_output": "[1,1,1,0]", "is_sample": False},
        {"input": "[5]\\n[5]", "expected_output": "[1,0]", "is_sample": False},
        {"input": "[1]\\n[9,9]", "expected_output": "[1,0,0]", "is_sample": False},
        # Stress
        {"input": json.dumps([9]*100) + "\\n[1]", "expected_output": "[1]" + str([0]*100).replace(" ", "").replace("[0,", "").replace(" ", ""), "is_sample": False},
        {"input": "[1,0,0]\\n[1]", "expected_output": "[1,0,1]", "is_sample": False}
    ]
    # Correcting expected output for stress case 9
    test_cases[8]["expected_output"] = "[1," + ",".join(["0"]*100) + "]"

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
        "topics": ["Linked List", "Math", "Stack"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Add_Two_Numbers_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
