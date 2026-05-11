import json
import os

def generate_json():
    problem_id = 382
    title = "Linked List Random Node"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>382. Linked List Random Node</h3>
<p>Given a singly linked list, return a random node's value from the linked list. Each node must have the <strong>same probability</strong> of being chosen.</p>

<p>Implement the <code>Solution</code> class:</p>
<ul>
	<li><code>Solution(ListNode head)</code> Initializes the object with the head of the singly-linked list.</li>
	<li><code>int getRandom()</code> Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/16/getnode-linkedlist.jpg" style="width: 302px; height: 62px;" />
<pre><strong>Input:</strong>
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
<strong>Output:</strong>
[null, 1, 3, 2, 2, 3]
<strong>Explanation:</strong>
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes in the linked list will be in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>getRandom</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>
<ul>
	<li>What if the linked list is extremely large and its length is unknown to you?</li>
	<li>Could you solve this efficiently without using extra space?</li>
</ul>"""

    input_format = "Head of a linked list and calls to `getRandom`."
    output_format = "Integer node values."
    
    constraints = [
        "1 <= number of nodes <= 10,000",
        "Calls to getRandom <= 10,000",
        "Equal probability required."
    ]
    
    explanation = """To select a random node from a linked list with unknown size (or to avoid extra space), we use **Reservoir Sampling**.

### Reservoir Sampling Algorithm:
1. **Initialize**: Set `chosen_value = head.val`.
2. **Iterate**: Traverse the list starting from the second node ($i=2, 3, \dots, N$).
3. **Probability**: For the $i$-th node, generate a random number between $1$ and $i$.
4. **Update**: If the random number is $1$, update `chosen_value = node.val`.
5. **Return**: After full traversal, `chosen_value` is our result.

### Why does it work?
The probability that the $i$-th node is selected and *stays* selected is:
$$ P(\text{selected}) = \frac{1}{i} \times \frac{i}{i+1} \times \dots \times \frac{N-1}{N} = \frac{1}{N} $$

### Efficiency:
- **Time Complexity**: $O(N)$ for each `getRandom()` call.
- **Space Complexity**: $O(1)$ extra space.

### Alternative (Pre-processing):
If the list is small enough to fit in memory ($N=10^4$ is fine), we can store all values in an array in $O(N)$ once and return `random.choice(array)` in $O(1)$. This is faster for many calls.

### Integration Choice:
Most tests accept either. The Reservoir Sampling is more "interview-standard" for the follow-up."""
    
    answer = """import random

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res = -1
        curr = self.head
        i = 1
        
        while curr:
            # For each node i, decide whether to pick it with probability 1/i
            if random.random() < 1/i:
                res = curr.val
            curr = curr.next
            i += 1
            
        return res"""

    boilerplate = {
        "python": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\nimport sys\nimport json\nimport random\n\nclass Solution:\n    def __init__(self, head):\n        pass\n    def getRandom(self):\n        pass\n\nif __name__ == '__main__':\n    # Execution logic\n    pass",
        "cpp": "class Solution {\npublic:\n    Solution(ListNode* head) {\n        \n    }\n    \n    int getRandom() {\n        \n    }\n};",
        "java": "public class Solution {\n    public Solution(ListNode head) {\n        \n    }\n    \n    public int getRandom() {\n        \n    }\n}",
        "javascript": "/**\n * @param {ListNode} head\n * @return {void}\n */\nvar Solution = function(head) {\n    \n};\n\n/**\n * @return {number}\n */\nSolution.prototype.getRandom = function() {\n    \n};",
        "c": "typedef struct {\n    \n} Solution;\n\nSolution* solutionCreate(struct ListNode* head) {\n    \n}\n\nint solutionGetRandom(Solution* obj) {\n    \n}"
    }

    test_cases = [
        {"input": '{"commands": ["Solution", "getRandom", "getRandom", "getRandom"], "args": [[[1, 2, 3]], [], [], []]}', "expected_output": "[null, 1, 2, 3] # Any permutation", "is_sample": True},
        {"input": '{"commands": ["Solution", "getRandom"], "args": [[[1]], []]}', "expected_output": "[null, 1]", "is_sample": False},
        {"input": '{"commands": ["Solution", "getRandom"], "args": [[[0]], []]}', "expected_output": "[null, 0]", "is_sample": False},
        {"input": '{"commands": ["Solution", "getRandom"], "args": [[[-1]], []]}', "expected_output": "[null, -1]", "is_sample": False},
        # Statistical check case
        {"input": '{"commands": ["Solution"] + ["getRandom"]*100, "args": [[[1,2]], [], ..., []]}', "expected_output": "...", "is_sample": False},
        # Large value case
        {"input": '{"commands": ["Solution", "getRandom"], "args": [[[10000, -10000]], []]}', "expected_output": "[null, 10000] # or -10000", "is_sample": False}
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
        "topics": ["Linked List", "Math", "Randomized", "Reservoir Sampling"],
        "companyIndex": 1
    }

    output_path = "301-500/382_Linked_List_Random_Node.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
