import json
import os

def generate_json():
    problem_id = 237
    title = "Delete Node in a Linked List"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>237. Delete Node in a Linked List</h3>
<p>There is a singly-linked list <code>head</code> and we want to delete a node <code>node</code> in it.</p>

<p>You are given the node to be deleted <code>node</code>. You will <strong>not be given access</strong> to the first node of <code>head</code>.</p>

<p>All the values of the linked list are <strong>unique</strong>, and it is guaranteed that the given node <code>node</code> is not the last node in the linked list.</p>

<p>Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:</p>

<ul>
	<li>The value of the given node should not exist in the linked list.</li>
	<li>The number of nodes in the linked list should decrease by one.</li>
	<li>All the values before <code>node</code> should be in the same order.</li>
	<li>All the values after <code>node</code> should be in the same order.</li>
</ul>

<p><strong>Custom testing:</strong></p>

<ul>
	<li>For the input, you should provide the entire linked list <code>head</code> and the node to be given <code>node</code>. <code>node</code> should not be the last node of the list and should be an actual node in the list.</li>
	<li>We will build the linked list and pass the node to your function.</li>
	<li>The output will be the entire list after calling your function.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/node1.jpg" style="width: 450px; height: 302px;" />
<pre><strong>Input:</strong> head = [4,5,1,9], node = 5
<strong>Output:</strong> [4,1,9]
<strong>Explanation: </strong>You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/node2.jpg" style="width: 450px; height: 302px;" />
<pre><strong>Input:</strong> head = [4,5,1,9], node = 1
<strong>Output:</strong> [4,5,9]
<strong>Explanation: </strong>You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the given list is in the range <code>[2, 1000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li>The value of each node in the list is <strong>unique</strong>.</li>
	<li>The <code>node</code> to be deleted is <strong>in the list</strong> and is <strong>not a tail</strong> node.</li>
</ul>"""

    input_format = "Two lines: first, an array representing the list; second, the value of the node to delete."
    output_format = "An array representing the updated list."
    
    constraints = [
        "2 <= count of nodes <= 1000",
        "-1000 <= Node.val <= 1000",
        "Target node value exists and is NOT the tail."
    ]
    
    explanation = """To delete a node in a linked list without access to the head or the previous node:
1. **The Trick**: Take the value from the *next* node and place it into the current `node`.
2. **Logic**: Then, update the current `node`'s `next` pointer to skip the *next* node (`node.next = node.next.next`).
3. **Complexity**:
   - Time: O(1).
   - Space: O(1)."""
    
    answer = """class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass ListNode:\n    def __init__(self, x):\n        self.val = x\n        self.next = None\n\ndef build_list(arr):\n    if not arr: return None\n    head = ListNode(arr[0])\n    curr = head\n    for val in arr[1:]: \n        curr.next = ListNode(val)\n        curr = curr.next\n    return head\n\ndef serialize_list(head):\n    res = []\n    while head: \n        res.append(head.val)\n        head = head.next\n    return res\n\ndef deleteNode(node):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        list_match = re.search(r'\\[.*?\\]', input_data[0])\n        list_str = list_match.group(0) if list_match else input_data[0]\n        list_str = list_str.replace('[', '').replace(']', '').replace(',', ' ')\n        vals = [int(x) for x in list_str.split()]\n        \n        num_match = re.findall(r'-?\\d+', input_data[1])\n        target_val = int(num_match[-1]) if num_match else 0\n        \n        head = build_list(vals)\n        curr = head\n        while curr and curr.val != target_val:\n            curr = curr.next\n        \n        if curr: deleteNode(curr)\n        print(json.dumps(serialize_list(head)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* buildList(vector<int>& vals) {\n    if (vals.empty()) return NULL;\n    ListNode* head = new ListNode(vals[0]);\n    ListNode* curr = head;\n    for (size_t i = 1; i < vals.size(); i++) {\n        curr->next = new ListNode(vals[i]);\n        curr = curr->next;\n    }\n    return head;\n}\n\nvoid printList(ListNode* head) {\n    cout << \"[\";\n    while (head) {\n        cout << head->val << (head->next ? \", \" : \"\");\n        head = head->next;\n    }\n    cout << \"]\" << endl;\n}\n\nvoid deleteNode(ListNode* node) {\n    // User logic here\n}\n\nint main() {\n    string line, targetLine;\n    if (getline(cin, line) && getline(cin, targetLine)) {\n        regex num_re(\"[-]?\\\\d+\");\n        vector<int> vals;\n        auto words_begin = sregex_iterator(line.begin(), line.end(), num_re);\n        auto words_end = sregex_iterator();\n        for (sregex_iterator i = words_begin; i != words_end; ++i) vals.push_back(stoi(i->str()));\n        \n        smatch m;\n        int targetVal = 0;\n        if (regex_search(targetLine, m, num_re)) targetVal = stoi(m.str());\n        \n        ListNode* head = buildList(vals);\n        ListNode* curr = head;\n        while (curr && curr->val != targetVal) curr = curr->next;\n        if (curr) deleteNode(curr);\n        printList(head);\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\nimport java.util.regex.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public void deleteNode(ListNode node) {\n        // User logic here\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null && line2 != null) {\n            List<Integer> vals = new ArrayList<>();\n            Matcher m = Pattern.compile(\"[-]?\\\\d+\").matcher(line1);\n            while (m.find()) vals.add(Integer.parseInt(m.group()));\n            \n            int targetVal = 0;\n            Matcher m2 = Pattern.compile(\"[-]?\\\\d+\").matcher(line2);\n            if (m2.find()) targetVal = Integer.parseInt(m2.group());\n            \n            ListNode head = buildList(vals);\n            ListNode curr = head;\n            while (curr != null && curr.val != targetVal) curr = curr.next;\n            if (curr != null) new Solution().deleteNode(curr);\n            printList(head);\n        }\n    }\n\n    static ListNode buildList(List<Integer> vals) {\n        if (vals.isEmpty()) return null;\n        ListNode head = new ListNode(vals.get(0));\n        ListNode curr = head;\n        for (int i = 1; i < vals.size(); i++) {\n            curr.next = new ListNode(vals.get(i));\n            curr = curr.next;\n        }\n        return head;\n    }\n\n    static void printList(ListNode head) {\n        List<Integer> res = new ArrayList<>();\n        while (head != null) {\n            res.add(head.val);\n            head = head.next;\n        }\n        System.out.println(res.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val) {\n    this.val = val;\n    this.next = null;\n}\n\nfunction buildList(arr) {\n    if (arr.length === 0) return null;\n    let head = new ListNode(arr[0]);\n    let curr = head;\n    for (let i = 1; i < arr.length; i++) {\n        curr.next = new ListNode(arr[i]);\n        curr = curr.next;\n    }\n    return head;\n}\n\nfunction serializeList(head) {\n    let res = [];\n    while (head) {\n        res.push(head.val);\n        head = head.next;\n    }\n    return res;\n}\n\nfunction deleteNode(node) {\n    // User logic here\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const listMatch = input[0].match(/\\[.*\\]/)?.[0] || input[0];\n    const arr = listMatch.replace(/[\\[\\]]/g, '').split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));\n    \n    const targetVal = parseInt(input[1].match(/[-]?\\d+/)?.[0]);\n    \n    let head = buildList(arr);\n    let curr = head;\n    while (curr && curr.val !== targetVal) curr = curr.next;\n    if (curr) deleteNode(curr);\n    console.log(JSON.stringify(serializeList(head)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nvoid deleteNode(struct ListNode* node) {\n    // User logic here\n}\n\nstruct ListNode* buildList(int* vals, int size) {\n    if (size == 0) return NULL;\n    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));\n    head->val = vals[0];\n    head->next = NULL;\n    struct ListNode* curr = head;\n    for (int i = 1; i < size; i++) {\n        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n        curr->next->val = vals[i];\n        curr->next->next = NULL;\n        curr = curr->next;\n    }\n    return head;\n}\n\nvoid printList(struct ListNode* head) {\n    printf(\"[\");\n    while (head) {\n        printf(\"%d%s\", head->val, head->next ? \", \" : \"\");\n        head = head->next;\n    }\n    printf(\"]\\n\");\n}\n\nint main() {\n    static char line[1000000];\n    char tLine[100];\n    if (fgets(line, sizeof(line), stdin) && fgets(tLine, sizeof(tLine), stdin)) {\n        int* vals = (int*)malloc(100000 * sizeof(int));\n        int size = 0;\n        char* p = line;\n        while (*p) {\n            if (isdigit(*p) || *p == '-') {\n                vals[size++] = strtol(p, &p, 10);\n            } else p++;\n        }\n        \n        char* tp = tLine; while (*tp && !isdigit(*tp) && *tp != '-') tp++;\n        int targetVal = atoi(tp);\n        \n        struct ListNode* head = buildList(vals, size);\n        struct ListNode* curr = head;\n        while (curr && curr->val != targetVal) curr = curr->next;\n        if (curr) deleteNode(curr);\n        printList(head);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[4,5,1,9]\\n5", "expected_output": "[4, 1, 9]", "is_sample": True},
        {"input": "[4,5,1,9]\\n1", "expected_output": "[4, 5, 9]", "is_sample": True},
        {"input": "[1,2,3,4]\\n1", "expected_output": "[2, 3, 4]", "is_sample": False},
        {"input": "[1,2,3,4]\\n3", "expected_output": "[1, 2, 4]", "is_sample": False},
        {"input": "[0,1]\\n0", "expected_output": "[1]", "is_sample": False},
        {"input": "[-100, 100, 50, 20]\\n-100", "expected_output": "[100, 50, 20]", "is_sample": False},
        {"input": "[1,3,2]\\n3", "expected_output": "[1, 2]", "is_sample": False},
        # Stress Tests (1000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_list(arr, val):
        return [x for x in arr if x != val]

    # Stress 8: 1000 nodes, delete head
    h8 = list(range(1000))
    test_cases[7] = {"input": json.dumps(h8) + "\\n0", "expected_output": json.dumps(_solve_list(h8, 0)), "is_sample": False}
    # Stress 9: 1000 nodes, delete almost tail
    h9 = list(range(1000))
    test_cases[8] = {"input": json.dumps(h9) + "\\n998", "expected_output": json.dumps(_solve_list(h9, 998)), "is_sample": False}
    # Stress 10: Mixed values
    h10 = [1000, -1000, 500, 2, 1, 0, -1]
    test_cases[9] = {"input": json.dumps(h10) + "\\n500", "expected_output": json.dumps(_solve_list(h10, 500)), "is_sample": False}

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
        "topics": ["Linked List"],
        "companyIndex": 0
    }

    output_path = "201-400/237_Delete_Node_in_a_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
