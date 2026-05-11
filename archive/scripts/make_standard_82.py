import json
import os

def generate_json():
    problem_id = 82
    title = "Remove Duplicates from Sorted List II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>82. Remove Duplicates from Sorted List II</h3>
<p>Given the <code>head</code> of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return <em>the linked list <strong>sorted</strong> as well</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,3,4,4,5]
<strong>Output:</strong> [1,2,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="width: 500px; height: 205px;" />
<pre>
<strong>Input:</strong> head = [1,1,1,2,3]
<strong>Output:</strong> [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 300]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li>The list is guaranteed to be <strong>sorted</strong> in ascending order.</li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the sorted linked list."
    output_format = "A single line containing space-separated integers of the modified list (only distinct numbers)."
    
    constraints = [
        "0 <= number of nodes <= 300",
        "-100 <= Node.val <= 100",
        "The list is sorted in ascending order."
    ]
    
    explanation = """To remove all nodes that have duplicate numbers:
1. **Dummy Node & Predecessor**:
   - Use a `dummy` node pointing to the `head`. This handles cases where the head itself is a duplicate.
   - Use a `prev` pointer initialized to `dummy`.
2. **Iterate and Skip**:
   - Traverse the list with `head`.
   - While `head` has a next node and `head.val == head.next.val`:
     - Inner loop to skip all nodes with the same value (until `head.next` is different or None).
     - Link `prev.next` to the node *after* the last duplicate (`head.next`).
   - If no duplicate is detected for the current `head`, simply move `prev` to `head`.
   - Move `head` to its next node in each step.
3. **Complexity**:
   - Time Complexity: O(N) because each node is visited at most twice.
   - Space Complexity: O(1) as we only use a few pointers."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy = ListNode(0, head)
    prev = dummy
    
    while head:
        if head.next and head.val == head.next.val:
            # Skip all nodes with the same value
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
        
    return dummy.next"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef deleteDuplicates(head):\n    # User logic\n    pass\n\n# Helper to build/print list\ndef build_list(arr):\n    if not arr: return None\n    head = ListNode(arr[0])\n    curr = head\n    for i in range(1, len(arr)):\n        curr.next = ListNode(arr[i])\n        curr = curr.next\n    return head\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        nums = [int(x) for x in data]\n        res = deleteDuplicates(build_list(nums))\n        out = []\n        while res:\n            out.append(res.val)\n            res = res.next\n        print(*(out))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* deleteDuplicates(ListNode* head) {\n    // User logic\n    return head;\n}\n\nint main() {\n    int val;\n    ListNode *dummy = new ListNode(0), *curr = dummy;\n    while (cin >> val) {\n        curr->next = new ListNode(val);\n        curr = curr->next;\n    }\n    ListNode* res = deleteDuplicates(dummy->next);\n    while (res) {\n        cout << res->val << (res->next ? \" \" : \"\");\n        res = res->next;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static ListNode deleteDuplicates(ListNode head) {\n        // User logic\n        return head;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        ListNode dummy = new ListNode(0), curr = dummy;\n        while (sc.hasNextInt()) {\n            curr.next = new ListNode(sc.nextInt());\n            curr = curr.next;\n        }\n        ListNode res = deleteDuplicates(dummy.next);\n        while (res != null) {\n            System.out.print(res.val + (res.next != null ? \" \" : \"\"));\n            res = res.next;\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val)\n    this.next = (next===undefined ? null : next)\n}\n\nfunction deleteDuplicates(head) {\n    // User logic\n    return head;\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const nums = input.split(/\\s+/).map(Number);\n    let dummy = new ListNode(0), curr = dummy;\n    nums.forEach(n => {\n        curr.next = new ListNode(n);\n        curr = curr.next;\n    });\n    let res = deleteDuplicates(dummy.next);\n    const out = [];\n    while (res) {\n        out.push(res.val);\n        res = res.next;\n    }\n    console.log(out.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode* deleteDuplicates(struct ListNode* head) {\n    // User logic\n    return head;\n}\n\nint main() {\n    struct ListNode dummy = {0, NULL};\n    struct ListNode* curr = &dummy;\n    int val;\n    while (scanf(\"%d\", &val) == 1) {\n        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));\n        curr->next->val = val;\n        curr->next->next = NULL;\n        curr = curr->next;\n    }\n    struct ListNode* res = deleteDuplicates(dummy.next);\n    int first = 1;\n    while (res) {\n        if (!first) printf(\" \");\n        printf(\"%d\", res->val);\n        first = 0;\n        res = res->next;\n    }\n    printf(\"\\n\");\n    return 0;\n}"
    }

    def _solve(nums):
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        return [n for n in nums if counts[n] == 1]

    test_cases = [
        {"input": "1 2 3 3 4 4 5", "expected_output": " ".join(map(str, _solve([1,2,3,3,4,4,5]))), "is_sample": True},
        {"input": "1 1 1 2 3", "expected_output": " ".join(map(str, _solve([1,1,1,2,3]))), "is_sample": True},
        {"input": "1 1 2 2", "expected_output": "", "is_sample": False},
        {"input": "1 2 3", "expected_output": "1 2 3", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 1 1 1 1", "expected_output": "", "is_sample": False},
        {"input": "1 2 2 3 3 4", "expected_output": "1 4", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 300), "expected_output": "", "is_sample": False},
        {"input": " ".join([str(i//2) for i in range(300)]), "expected_output": "", "is_sample": False},
        {"input": " ".join(map(str, range(300))), "expected_output": " ".join(map(str, range(300))), "is_sample": False}
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

    output_path = "1-200/82_Remove_Duplicates_from_Sorted_List_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
