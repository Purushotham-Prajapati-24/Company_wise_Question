import json
import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generate_json():
    problem_id = 142
    title = "Linked List Cycle II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>142. Linked List Cycle II</h3>
<p>Given the <code>head</code> of a linked list, return <em>the node where the cycle begins. If there is no cycle, return </em><code>null</code>.</p>
<p>There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the&nbsp;<code>next</code>&nbsp;pointer. Internally, <code>pos</code>&nbsp;is used to denote the index of the node that&nbsp;tail's&nbsp;<code>next</code>&nbsp;pointer is connected to (<strong>0-indexed</strong>). It is <code>-1</code> if there is no cycle. <strong>Note that&nbsp;<code>pos</code>&nbsp;is not passed as a parameter</strong>.</p>
<p><strong>Do not modify</strong> the linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="height: 145px; width: 450px;" />
<pre><strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> tail connects to node index 1
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the second node.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 105px; width: 201px;" />
<pre><strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> tail connects to node index 0
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the first node.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 65px; width: 65px;" />
<pre><strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> no cycle
<strong>Explanation:</strong> There is no cycle in the linked list.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>pos</code> is <code>-1</code> or a <strong>valid index</strong> in the linked-list.</li>
</ul>"""

    input_format = "Two lines. Line 1: Space-separated integers representing nodes. Line 2: Integer 'pos' for cycle entry index (-1 if no cycle)."
    output_format = "A string: 'tail connects to node index X' or 'no cycle'."
    
    constraints = [
        "0 <= Number of nodes <= 10^4",
        "-10^5 <= Node.val <= 10^5",
        "pos is -1 or a valid index.",
        "Constant extra space (O(1)) required for best performance."
    ]
    
    explanation = """To find the entry point of a cycle in a linked list using O(1) space, we use Floyd's Cycle-Finding Algorithm (Tortoise and Hare):
1. **Detecting Cycle**: 
   - Initialize two pointers, `slow` and `fast`, at the `head`.
   - Move `slow` by one step and `fast` by two steps.
   - If they meet, a cycle exists. If `fast` reaches `null`, no cycle exists.
2. **Finding Cycle Entry**:
   - Once a meeting point is found, reset one pointer (e.g., `slow`) to the `head`.
   - Move both pointers one step at a time.
   - The point where they meet again is the start of the cycle.
3. **Mathematical Proof**:
   - Let $L_1$ be distance from head to entry, $L_2$ from entry to meeting point, $C$ be cycle length.
   - Fast distance = $L_1 + L_2 + nC$
   - Slow distance = $L_1 + L_2$
   - $2(L_1 + L_2) = L_1 + L_2 + nC \implies L_1 + L_2 = nC$. This means distance from head to entry ($L_1$) is equal to distance from meeting point to entry ($nC - L_2$).
4. **Complexity**:
   - Time Complexity: O(n)
   - Space Complexity: O(1)"""
    
    answer = """class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Phase 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Phase 2: Find entry
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, x):\n        self.val = x\n        self.next = None\n\ndef detectCycle(head):\n    # User logic here\n    pass\n\ndef solve():\n    lines = sys.stdin.read().splitlines()\n    if not lines: return\n    arr = [int(x) for x in lines[0].split()]\n    if not arr: print('no cycle'); return\n    pos = int(lines[1])\n    \n    nodes = [ListNode(x) for x in arr]\n    for i in range(len(nodes) - 1):\n        nodes[i].next = nodes[i+1]\n    if pos != -1:\n        nodes[-1].next = nodes[pos]\n        \n    res = detectCycle(nodes[0])\n    if not res: print('no cycle')\n    else:\n        for i in range(len(nodes)):\n            if nodes[i] == res:\n                print(f'tail connects to node index {i}')\n                return\n\nif __name__ == '__main__':\n    solve()",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode *detectCycle(ListNode *head) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    // Parsing logic here\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val; ListNode next;\n    ListNode(int x) { val = x; next = null; }\n}\n\npublic class Main {\n    public static ListNode detectCycle(ListNode head) {\n        // User logic\n        return null;\n    }\n    public static void main(String[] args) {\n        // Parsing logic here\n    }\n}",
        "javascript": "function ListNode(val) {\n    this.val = val;\n    this.next = null;\n}\n\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar detectCycle = function(head) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nstruct ListNode *detectCycle(struct ListNode *head) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "3 2 0 -4\n1", "expected_output": "tail connects to node index 1", "is_sample": True},
        {"input": "1 2\n0", "expected_output": "tail connects to node index 0", "is_sample": True},
        {"input": "1\n-1", "expected_output": "no cycle", "is_sample": False},
        {"input": "1 2 3\n-1", "expected_output": "no cycle", "is_sample": False},
        {"input": "1 2 3\n0", "expected_output": "tail connects to node index 0", "is_sample": False},
        {"input": "1 2 3 4 5\n2", "expected_output": "tail connects to node index 2", "is_sample": False},
        {"input": "100 200 300\n1", "expected_output": "tail connects to node index 1", "is_sample": False},
        # Stress Tests
        {"input": " ".join([str(i) for i in range(10000)]) + "\n-1", "expected_output": "no cycle", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\n0", "expected_output": "tail connects to node index 0", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\n5000", "expected_output": "tail connects to node index 5000", "is_sample": False}
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

    output_path = "1-200/142_Linked_List_Cycle_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
