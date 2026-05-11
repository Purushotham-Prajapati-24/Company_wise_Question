import json
import os

def generate_json():
    problem_id = 817
    title = "Linked List Components"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>817. Linked List Components</h3>
<p>You are given the <code>head</code> of a linked list containing unique integer values and an integer array <code>nums</code> that is a subset of the linked list's values.</p>

<p>Return <em>the number of connected components in </em><code>nums</code><em>, where two values are connected if they appear <b>consecutively</b> in the linked list.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> head = [0,1,2,3], nums = [0,1,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 0 and 1 are connected, so [0, 1] forms one component. 3 is not connected to 0 or 1, so [3] forms another component.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> head = [0,1,2,3,4], nums = [0,3,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 0 and 1 are connected, 3 and 4 are connected. So [0, 1] and [3, 4] are the two connected components.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the linked list is <code>n</code>.</li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt; n</code></li>
	<li>All the values <code>Node.val</code> are <b>unique</b>.</li>
	<li><code>1 &lt;= nums.length &lt;= n</code></li>
	<li><code>0 &lt;= nums[i] &lt; n</code></li>
	<li>All the values in <code>nums</code> are <b>unique</b>.</li>
</ul>"""

    input_format = "Two lines: 1) space-separated values of the linked list 2) space-separated values of nums subset."
    output_format = "A single integer representing the number of connected components."
    
    constraints = [
        "1 <= n <= 10,000",
        "Subset values are unique and exist in the linked list.",
        "O(N + M) time complexity.",
        "O(M) space complexity."
    ]
    
    explanation = """To find the number of connected components in the subset `nums`:
1. **The Hash Set Optimization**:
   - Searching for a value in the `nums` array takes O(M) time. By converting `nums` into a Hash Set (O(M) space), we can check for existence in O(1).
2. **Component Logic**:
   - A connected component is a sequence of one or more adjacent nodes in the linked list that all belong to `nums`.
   - We traverse the linked list node by node.
   - We count a "component" starting when we encounter a node whose value is in `nums`, but whose *next* node is either `None` or not in `nums`.
   - Alternatively: Increment the count if `current_node.val` is in `nums` AND (`current_node.next` is `None` OR `current_node.next.val` is NOT in `nums`).
3. **Complexity**:
   - Time Complexity: O(N + M) to iterate through the linked list (N nodes) and build the set from nums (M elements).
   - Space Complexity: O(M) to store the hash set of `nums`."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numComponents(head: ListNode, nums: list[int]) -> int:
    num_set = set(nums)
    count = 0
    curr = head
    
    while curr:
        # If current is in nums AND (is last node OR next is NOT in nums)
        if curr.val in num_set and (not curr.next or curr.next.val not in num_set):
            count += 1
        curr = curr.next
        
    return count"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef build_list(arr):\n    if not arr: return None\n    head = ListNode(int(arr[0]))\n    curr = head\n    for i in range(1, len(arr)):\n        curr.next = ListNode(int(arr[i]))\n        curr = curr.next\n    return head\n\ndef numComponents(head, nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if lines:\n        list_vals = lines[0].strip().split()\n        head = build_list(list_vals)\n        nums_vals = list(map(int, lines[1].strip().split()))\n        print(numComponents(head, nums_vals))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nstruct ListNode {\n    int val;\n    ListNode *next;\n    ListNode(int x) : val(x), next(NULL) {}\n};\n\nint numComponents(ListNode* head, vector<int>& nums) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class Solution {\n    public int numComponents(ListNode head, int[] nums) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function numComponents(head, nums) {\n    // User logic\n}",
        "c": "struct ListNode {\n    int val;\n    struct ListNode *next;\n};\n\nint numComponents(struct ListNode* head, int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "0 1 2 3\\n0 1 3", "expected_output": "2", "is_sample": True},
        {"input": "0 1 2 3 4\\n0 3 1 4", "expected_output": "2", "is_sample": True},
        {"input": "0 1 2\\n1", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4 5\\n1 2 3 4 5", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4 5\\n1 3 5", "expected_output": "3", "is_sample": False},
        {"input": "99\\n99", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4\\n1 4", "expected_output": "2", "is_sample": False},
        {"input": "0 1 2 3 4\\n0 2 4", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n" + " ".join([str(i) for i in range(0, 10000, 2)]), "expected_output": "5000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(10000)]) + "\\n" + " ".join([str(i) for i in range(10000)]), "expected_output": "1", "is_sample": False}
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
        "topics": ["Linked List", "Hash Table"],
        "companyIndex": 0
    }

    output_path = "801-1000/817_Linked_List_Components.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
