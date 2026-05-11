import json
import os

def generate_json():
    problem_id = 707
    title = "Design Linked List"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>707. Design Linked List</h3>
<p>Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: <code>val</code> and <code>next</code>. <code>val</code> is the value of the current node, and <code>next</code> is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute <code>prev</code> to indicate the previous node in the linked list. Assume all nodes in the linked list are <b>0-indexed</b>.</p>

<p>Implement the <code>MyLinkedList</code> class:</p>

<ul>
	<li><code>MyLinkedList()</code> Initializes the <code>MyLinkedList</code> object.</li>
	<li><code>int get(int index)</code> Get the value of the <code>index<sup>th</sup></code> node in the linked list. If the index is invalid, return <code>-1</code>.</li>
	<li><code>void addAtHead(int val)</code> Add a node of value <code>val</code> before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.</li>
	<li><code>void addAtTail(int val)</code> Append a node of value <code>val</code> as the last element of the linked list.</li>
	<li><code>void addAtIndex(int index, int val)</code> Add a node of value <code>val</code> before the <code>index<sup>th</sup></code> node in the linked list. If <code>index</code> equals the length of the linked list, the node will be appended to the end of the linked list. If <code>index</code> is greater than the length, the node <b>will not be inserted</b>.</li>
	<li><code>void deleteAtIndex(int index)</code> Delete the <code>index<sup>th</sup></code> node in the linked list, if the index is valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>Output:</strong>
[null, null, null, null, 2, null, 3]

<strong>Explanation:</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= index, val &lt;= 1000</code></li>
	<li>Please do not use any built-in LinkedList library.</li>
	<li>At most <code>2000</code> calls will be made to <code>get</code>, <code>addAtHead</code>, <code>addAtTail</code>, <code>addAtIndex</code> and <code>deleteAtIndex</code>.</li>
</ul>"""

    input_format = "Multiple lines: Each line is an operation (e.g., 'addAtHead 1', 'get 0', 'deleteAtIndex 5')."
    output_format = "A single integer for 'get' operations. No output for others."
    
    constraints = [
        "0 <= index, val <= 1000",
        "O(1) for addAtHead/Tail.",
        "O(N) for get/addAtIndex/deleteAtIndex.",
        "O(N) extra space."
    ]
    
    explanation = """To design a linked list from scratch:
1. **The Node Structure**:
   - `SinglyNode`: Contains `val` and `next`.
   - `DoublyNode`: Contains `val`, `next`, and `prev`.
2. **Efficiency Strategy**:
   - Maintain a `size` variable to handle index validation quickly.
   - Using a **Sentinel (Dummy) Head** simplifies insertion and deletion operations, as you don't have to handle the empty list or head-change cases separately.
3. **Operations**:
   - `addAtHead(val)`: Insert after dummy head.
   - `addAtTail(val)`: Iterate to the end (or maintain a `tail` pointer) and attach.
   - `addAtIndex(index, val)`: 
     - If `index > size`, return.
     - Find the predecessor (at `index-1`), insert new node between predecessor and current `index`-th node.
   - `deleteAtIndex(index)`:
     - Find the predecessor, point its `next` to the node after `index`.
4. **Complexity**:
   - `addAtHead`: O(1).
   - `addAtTail`: O(N) (or O(1) if tail is tracked).
   - `get/addAtIndex/deleteAtIndex`: O(N)."""
    
    answer = """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0) # Sentinel head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    # Define your node\n    pass\n\nclass MyLinkedList:\n    def __init__(self):\n        pass\n    def get(self, index):\n        pass\n    def addAtHead(self, val):\n        pass\n    def addAtTail(self, val):\n        pass\n    def addAtIndex(self, index, val):\n        pass\n    def deleteAtIndex(self, index):\n        pass\n\nif __name__ == '__main__':\n    # Parser and logic",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nclass MyLinkedList {\npublic:\n    MyLinkedList();\n    int get(int index);\n    void addAtHead(int val);\n    void addAtTail(int val);\n    void addAtIndex(int index, int val);\n    void deleteAtIndex(int index);\n};",
        "java": "public class MyLinkedList {\n    public int get(int index) {\n        // User logic\n        return -1;\n    }\n    public void addAtHead(int val) {}\n    public void addAtTail(int val) {}\n    public void addAtIndex(int index, int val) {}\n    public void deleteAtIndex(int index) {}\n}",
        "javascript": "var MyLinkedList = function() {\n    // User logic\n};\n\nMyLinkedList.prototype.get = function(index) {\n    // User logic\n};\n\nMyLinkedList.prototype.addAtHead = function(val) {\n    // User logic\n};\n\nMyLinkedList.prototype.addAtTail = function(val) {\n    // User logic\n};\n\nMyLinkedList.prototype.addAtIndex = function(index, val) {\n    // User logic\n};\n\nMyLinkedList.prototype.deleteAtIndex = function(index) {\n    // User logic\n};",
        "c": "typedef struct {\n    // User node fields\n} MyLinkedList;\n\nMyLinkedList* myLinkedListCreate();\nint myLinkedListGet(MyLinkedList* obj, int index);\nvoid myLinkedListAddAtHead(MyLinkedList* obj, int val);\nvoid myLinkedListAddAtTail(MyLinkedList* obj, int val);\nvoid myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val);\nvoid myLinkedListDeleteAtIndex(MyLinkedList* obj, int index);"
    }

    test_cases = [
        {"input": "addAtHead 1\\naddAtTail 3\\naddAtIndex 1 2\\nget 1\\ndeleteAtIndex 1\\nget 1", "expected_output": "2\\n3", "is_sample": True},
        {"input": "addAtHead 1\\naddAtTail 2\\naddAtTail 3\\nget 0\\nget 1\\nget 2\\nget 3", "expected_output": "1\\n2\\n3\\n-1", "is_sample": True},
        {"input": "get 0", "expected_output": "-1", "is_sample": False},
        {"input": "addAtTail 5\\nget 0", "expected_output": "5", "is_sample": False},
        {"input": "addAtHead 2\\ndeleteAtIndex 1\\nget 0", "expected_output": "2", "is_sample": False},
        {"input": "addAtHead 1\\naddAtTail 3\\naddAtIndex 1 2\\nget 1\\ndeleteAtIndex 0\\nget 0", "expected_output": "2\\n2", "is_sample": False},
        {"input": "addAtHead 7\\naddAtHead 2\\naddAtHead 1\\naddAtIndex 3 0\\ndeleteAtIndex 2\\naddAtHead 6\\naddAtTail 4\\nget 4\\naddAtHead 4\\naddAtIndex 5 0\\naddAtHead 6", "expected_output": "4", "is_sample": False},
        {"input": "addAtIndex 0 10\\naddAtIndex 0 20\\naddAtIndex 1 30\\nget 0", "expected_output": "20", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"addAtTail {i}" for i in range(1000)]) + "\\nget 500", "expected_output": "500", "is_sample": False},
        {"input": "\\n".join([f"addAtHead {i}" for i in range(1000)]) + "\\nget 0", "expected_output": "999", "is_sample": False}
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
        "topics": ["Linked List", "Design"],
        "companyIndex": 0
    }

    output_path = "601-800/707_Design_Linked_List.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
