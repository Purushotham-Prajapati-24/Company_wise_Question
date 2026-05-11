import json
import os

def generate_json():
    problem_id = 876
    title = "Middle of the Linked List"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>876. Middle of the Linked List</h3>
<p>Given the <code>head</code> of a singly linked list, return <em>the middle node of the linked list</em>.</p>

<p>If there are two middle nodes, return <strong>the second middle</strong> node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>
"""

    input_format = "A linked list head in JSON format."
    output_format = "The middle node (sublist)."
    
    constraints = [
        "1 <= Number of nodes <= 100",
        "1 <= Node.val <= 100"
    ]
    
    explanation = """To find the middle node of a singly linked list in a single pass:
1. **The Fast & Slow Pointer Technique**:
   - Initialize two pointers `slow` and `fast` both pointing to the `head`.
2. **Move Pointers**:
   - For each step:
     - Move `slow` one node forward (`slow = slow.next`).
     - Move `fast` two nodes forward (`fast = fast.next.next`).
3. **Logic**:
   - When `fast` reaches the end of the list (either `fast` is `null` or `fast.next` is `null`), `slow` will be pointing exactly at the middle node.
   - For an odd-length list, `slow` is exactly in the middle.
   - For an even-length list, `slow` is at the second of the two middle nodes.

Complexity:
- Time: O(N) where N is the length of the list.
- Space: O(1)."""
    
    answer = """def middleNode(head: 'ListNode') -> 'ListNode':
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef middleNode(head):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    # List deserialization code goes here\n    pass",
        "cpp": "#include <iostream>\n\nusing namespace std;\ntypedef struct ListNode {\n    int val;\n    ListNode *next;\n} ListNode;",
        "java": "class Solution {\n    public ListNode middleNode(ListNode head) {\n        return head;\n    }\n}",
        "javascript": "var middleNode = function(head) {\n    return head;\n};",
        "c": "struct ListNode* middleNode(struct ListNode* head){\n    return head;\n}"
    }

    test_cases = [
        {"input": "[1,2,3,4,5]", "expected_output": "[3,4,5]", "is_sample": True},
        {"input": "[1,2,3,4,5,6]", "expected_output": "[4,5,6]", "is_sample": True},
        # Diverse cases
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1,2]", "expected_output": "[2]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10]", "expected_output": "[6,7,8,9,10]", "is_sample": False},
        {"input": "[10, 20, 30]", "expected_output": "[20, 30]", "is_sample": False},
        {"input": "[1, 2, 3, 4, 5, 6, 7]", "expected_output": "[4, 5, 6, 7]", "is_sample": False},
        {"input": "[5, 4, 3, 2, 1]", "expected_output": "[3, 2, 1]", "is_sample": False},
        # Stress cases
        {"input": "[Node values don't matter]", "expected_output": "Check logic", "is_sample": False},
        {"input": "[1-100 sequence]", "expected_output": "51-100", "is_sample": False}
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

    output_path = "801-1000/876_Middle_of_the_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
