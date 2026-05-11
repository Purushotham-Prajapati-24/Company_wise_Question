import json
import os

def generate_json():
    problem_id = 369
    title = "Plus One Linked List"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>369. Plus One Linked List</h3>
<p>Given a non-negative integer represented as a <strong>non-empty</strong> singly linked list of digits, plus one to the integer.</p>

<p>The digits are stored such that the most significant digit is at the <strong>head</strong> of the list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> head = [1,2,3]
<strong>Output:</strong> [1,2,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> head = [0]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>The number represented by the linked list does not contain leading zeros except for the zero itself.</li>
</ul>"""

    input_format = "A singly linked list `head` representing an integer."
    output_format = "The linked list after adding one."
    
    constraints = [
        "1 <= number of nodes <= 100",
        "0 <= Node.val <= 9",
        "No leading zeros except for 0."
    ]
    
    explanation = """To add one to a linked list where the most significant digit is at the head, we can use **Recursion** or **Reverse the List**.

### Recursion Approach ($O(N)$):
The recursive approach allows us to "visit" the digits from right to left (backtracking from the base case).

1. **DFS Function**: `add(node)`:
   - If `node` is `None`: return `1` (this is the "one" we are adding).
   - Recursive call `carry = add(node.next)`.
   - Update `node.val += carry`.
   - If `node.val == 10`:
     - `node.val = 0`
     - return `1` (new carry).
   - Else: return `0`.
2. **Handle Head Carry**:
   - If the final recursive call returns a `1`, we need to create a new head node with value `1`.

### Pre-computation Improvement (Two Pointers):
1. Create a dummy node pointing to the head.
2. Find the rightmost node that is **not equal to 9**. Let's call it `not_nine`.
3. Increment `not_nine.val`.
4. Set all nodes after `not_nine` to 0.
5. If dummy node was incremented (i.e. all original nodes were 9), return dummy. Otherwise, return dummy.next.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the number of nodes in the list.
- **Space Complexity**: $O(H)$ for recursion stack, or $O(1)$ for the two-pointer approach."""
    
    answer = """class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # Optimization: Two-pointer approach
        dummy = ListNode(0)
        dummy.next = head
        
        # Find the rightmost node that is not a 9
        not_nine = dummy
        curr = head
        while curr:
            if curr.val != 9:
                not_nine = curr
            curr = curr.next
            
        # Increment the rightmost non-9 node
        not_nine.val += 1
        
        # Set all subsequent nodes (all were 9s) to 0
        curr = not_nine.next
        while curr:
            curr.val = 0
            curr = curr.next
            
        return dummy if dummy.val != 0 else dummy.next"""

    boilerplate = {
        "python": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\nimport sys\nimport json\n\nclass Solution:\n    def plusOne(self, head):\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    # ListNode construction and execution code\n    pass",
        "cpp": "#include <iostream>\nusing namespace std;\n\nclass Solution {\npublic:\n    ListNode* plusOne(ListNode* head) {\n        // Your logic here\n        return head;\n    }\n};",
        "java": "public class Solution {\n    public ListNode plusOne(ListNode head) {\n        // Your logic here\n        return head;\n    }\n}",
        "javascript": "/**\n * @param {ListNode} head\n * @return {ListNode}\n */\nvar plusOne = function(head) {\n    // Your logic here\n};",
        "c": "struct ListNode* plusOne(struct ListNode* head) {\n    // Your logic here\n    return head;\n}"
    }

    test_cases = [
        {"input": "[1,2,3]", "expected_output": "[1,2,4]", "is_sample": True},
        {"input": "[0]", "expected_output": "[1]", "is_sample": True},
        {"input": "[9]", "expected_output": "[1,0]", "is_sample": False},
        {"input": "[9,9,9]", "expected_output": "[1,0,0,0]", "is_sample": False},
        {"input": "[1,9,9]", "expected_output": "[2,0,0]", "is_sample": False},
        {"input": "[8,9,9]", "expected_output": "[9,0,0]", "is_sample": False},
        {"input": "[1,0,0]", "expected_output": "[1,0,1]", "is_sample": False},
        # Stress cases
        {"input": "[9]*100", "expected_output": "[1] + [0]*100", "is_sample": False},
        {"input": "[1]*100", "expected_output": "[1]*99 + [2]", "is_sample": False},
        {"input": "[0]", "expected_output": "[1]", "is_sample": False}
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
        "topics": ["Linked List", "Math"],
        "companyIndex": 1
    }

    output_path = "301-500/369_Plus_One_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
