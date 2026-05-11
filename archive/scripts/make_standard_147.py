import json
import os

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate_json():
    problem_id = 147
    title = "Insertion Sort List"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>147. Insertion Sort List</h3>
<p>Given the <code>head</code> of a singly linked list, sort the list using <strong>insertion sort</strong>, and return <em>the sorted list's head</em>.</p>
<p>The steps of the <strong>insertion sort</strong> algorithm:</p>
<ol>
	<li>Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.</li>
	<li>At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.</li>
	<li>It repeats until no input elements remain.</li>
</ol>
<p>The following is a graphical example explaining the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" style="height: 180px; width: 300px;" />

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg" style="width: 422px; height: 222px;" />
<pre><strong>Input:</strong> head = [4,2,1,3]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg" style="width: 542px; height: 222px;" />
<pre><strong>Input:</strong> head = [-1,5,3,4,0]
<strong>Output:</strong> [-1,0,3,4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the linked list."
    output_format = "A bracketed array of integers representing the sorted list."
    
    constraints = [
        "1 <= Number of nodes <= 5000",
        "-5000 <= Node.val <= 5000",
        "Algorithm must implement Insertion Sort mechanism.",
        "O(n^2) time complexity is expected for this specific algorithm."
    ]
    
    explanation = """Insertion Sort on a Linked List works by building a sorted list one node at a time:
1. **Dummy Node**: Create a `dummy` node to act as the head of the sorted list. This simplifies insertions at the very beginning.
2. **Iteration**: Traverse the original list node by node. For each node `curr`:
   - Start from the `dummy` node and find the first node `prev` such that `prev.next.val >= curr.val`.
   - Insert `curr` between `prev` and `prev.next`.
3. **Pointers Management**: Carefully update pointers to disconnect `curr` from its original position and reconnect it in the sorted sequence.
4. **Complexity**:
   - Time Complexity: O(n²) in the worst case (reverse sorted list).
   - Space Complexity: O(1) as we are rearranging existing nodes."""
    
    answer = """class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        dummy = ListNode(0)
        curr = head
        
        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
            
        return dummy.next"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef insertionSortList(head):\n    # User logic here\n    pass\n\ndef solve():\n    line = sys.stdin.read().split()\n    if not line: return\n    nodes = [ListNode(int(x)) for x in line]\n    for i in range(len(nodes)-1):\n        nodes[i].next = nodes[i+1]\n    \n    sorted_head = insertionSortList(nodes[0])\n    res = []\n    curr = sorted_head\n    while curr:\n        res.append(curr.val)\n        curr = curr.next\n    print(json.dumps(res))\n\nif __name__ == '__main__':\n    solve()",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nstruct ListNode {\n    int val; ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nListNode* insertionSortList(ListNode* head) {\n    // User logic\n    return NULL;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val; ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Main {\n    public static ListNode insertionSortList(ListNode head) {\n        // User logic\n        return null;\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "function ListNode(val, next) {\n    this.val = (val===undefined ? 0 : val);\n    this.next = (next===undefined ? null : next);\n}\n/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar insertionSortList = function(head) {\n    // User logic\n};",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct ListNode {\n    int val; struct ListNode *next;\n};\n\nstruct ListNode* insertionSortList(struct ListNode* head) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "4 2 1 3", "expected_output": "[1, 2, 3, 4]", "is_sample": True},
        {"input": "-1 5 3 4 0", "expected_output": "[-1, 0, 3, 4, 5]", "is_sample": True},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "2 1", "expected_output": "[1, 2]", "is_sample": False},
        {"input": "1 2 3", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "3 2 1", "expected_output": "[1, 2, 3]", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "[1, 2, 3, 4, 5]", "is_sample": False},
        # Stress Tests
        {"input": " ".join([str(i) for i in range(5000, 0, -1)]), "expected_output": json.dumps(list(range(1, 5001))), "is_sample": False},
        {"input": " ".join(["0"] * 5000), "expected_output": json.dumps([0] * 5000), "is_sample": False},
        {"input": " ".join([str(i % 100) for i in range(5000)]), "expected_output": json.dumps(sorted([i % 100 for i in range(5000)])), "is_sample": False}
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Linked List", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/147_Insertion_Sort_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
