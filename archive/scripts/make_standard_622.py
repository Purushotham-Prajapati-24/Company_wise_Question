import json
import os

def generate_json():
    problem_id = 622
    title = "Design Circular Queue"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>622. Design Circular Queue</h3>
<p>Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".</p>

<p>One of the benefits of a circular queue is that you can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, you cannot insert the next element even if there is space in front of the queue. But using the circular queue, we can use the space to store new values.</p>

<p>Implementation the <code>MyCircularQueue</code> class:</p>

<ul>
	<li><code>MyCircularQueue(k)</code> Initializes the object with the size of the queue to be <code>k</code>.</li>
	<li><code>int Front()</code> Gets the front item from the queue. If the queue is empty, return <code>-1</code>.</li>
	<li><code>int Rear()</code> Gets the last item from the queue. If the queue is empty, return <code>-1</code>.</li>
	<li><code>boolean enQueue(int value)</code> Inserts an element into the circular queue. Return <code>true</code> if the operation is successful.</li>
	<li><code>boolean deQueue()</code> Deletes an element from the circular queue. Return <code>true</code> if the operation is successful.</li>
	<li><code>boolean isEmpty()</code> Checks whether the circular queue is empty or not.</li>
	<li><code>boolean isFull()</code> Checks whether the circular queue is full or not.</li>
</ul>

<p>You must solve the problem without using the built-in queue data structure in your programming language.&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
<strong>Output:</strong>
[null, true, true, true, false, 3, true, true, true, 4]

<strong>Explanation:</strong>
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False (is full)
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>0 &lt;= value &lt;= 1000</code></li>
	<li>At most <code>3000</code> calls will be made to <code>enQueue</code>, <code>deQueue</code>, <code>Front</code>, <code>Rear</code>, <code>isEmpty</code>, and <code>isFull</code>.</li>
</ul>"""

    input_format = "Two lines: 1) space-separated commands 2) space-separated arguments (comma-separated within each bracketed group)."
    output_format = "A single line containing space-separated results."
    
    constraints = [
        "1 <= k <= 1000",
        "At most 3000 calls.",
        "No built-in queue structure allowed.",
        "O(1) per operation.",
        "O(K) extra space."
    ]
    
    explanation = """A circular queue is implemented using a fixed-size array and modular arithmetic:
1. **The Core Structure**:
   - An array `queue` of size $k$.
   - Integers `head`, `tail`, and `size`.
2. **Operations**:
   - `isEmpty`: Check if `size == 0`.
   - `isFull`: Check if `size == k`.
   - `enQueue`: If not full, update `tail = (tail + 1) % k`, put value at `tail`, increment `size`. (Initial `tail` can be -1).
   - `deQueue`: If not empty, update `head = (head + 1) % k`, decrement `size`.
   - `Front`: If not empty, return `queue[head]`.
   - `Rear`: If not empty, return `queue[tail]`.
3. **Complexity**:
   - Time Complexity: O(1) for each operation.
   - Space Complexity: O(K) where K is the size of the buffer."""
    
    answer = """class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.size = 0
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k"""

    boilerplate = {
        "python": "import sys\n\nclass MyCircularQueue:\n    def __init__(self, k): pass\n    def enQueue(self, value): pass\n    def deQueue(self): pass\n    def Front(self): pass\n    def Rear(self): pass\n    def isEmpty(self): pass\n    def isFull(self): pass\n\nif __name__ == '__main__':\n    # Parsing commands... helper logic here\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nclass MyCircularQueue {\npublic:\n    MyCircularQueue(int k) {}\n    bool enQueue(int value) { return false; }\n    bool deQueue() { return false; }\n    int Front() { return -1; }\n    int Rear() { return -1; }\n    bool isEmpty() { return true; }\n    bool isFull() { return true; }\n};",
        "java": "class MyCircularQueue {\n    public MyCircularQueue(int k) {}\n    public boolean enQueue(int value) { return false; }\n    public boolean deQueue() { return false; }\n    public int Front() { return -1; }\n    public int Rear() { return -1; }\n    public boolean isEmpty() { return false; }\n    public boolean isFull() { return false; }\n}",
        "javascript": "var MyCircularQueue = function(k) {};",
        "c": "typedef struct {} MyCircularQueue;"
    }

    test_cases = [
        {"input": "MyCircularQueue enQueue enQueue enQueue enQueue Rear isFull deQueue enQueue Rear\\n3 1 2 3 4 - - - 4 -", "expected_output": "null true true true false 3 true true true 4", "is_sample": True},
        {"input": "MyCircularQueue enQueue enQueue Front Rear deQueue Front Rear\\n2 5 3 - - - - -", "expected_output": "null true true 5 3 true 3 3", "is_sample": True},
        {"input": "MyCircularQueue isEmpty isFull\\n1 - -", "expected_output": "null true false", "is_sample": False},
        {"input": "MyCircularQueue enQueue enQueue deQueue enQueue deQueue enQueue deQueue Front\\n1 1 2 - 3 - 4 - -", "expected_output": "null true false true true true true true -1", "is_sample": False},
        {"input": "MyCircularQueue enQueue enQueue deQueue Front\\n2 1 2 - -", "expected_output": "null true true true 2", "is_sample": False},
        {"input": "MyCircularQueue isFull enQueue deQueue isEmpty\\n1 - 10 - -", "expected_output": "null false true true true", "is_sample": False},
        {"input": "MyCircularQueue Front Rear deQueue enQueue Front Rear\\n3 - - - 100 100 100", "expected_output": "null -1 -1 false true 100 100", "is_sample": False},
        # Stress cases
        {"input": "MyCircularQueue " + " ".join(["enQueue"] * 1000) + "\\n1000 " + " ".join([str(i) for i in range(1000)]), "expected_output": "null " + " ".join(["true"] * 1000), "is_sample": False},
        {"input": "MyCircularQueue " + " ".join(["enQueue", "deQueue"] * 1500) + "\\n10 " + " ".join(["1", "-"] * 1500), "expected_output": "null " + " ".join(["true", "true"] * 1500), "is_sample": False},
        {"input": "MyCircularQueue enQueue isFull\\n1 1 -", "expected_output": "null true true", "is_sample": False}
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
        "topics": ["Array", "Queue", "Design"],
        "companyIndex": 0
    }

    output_path = "601-800/622_Design_Circular_Queue.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
