import json
import os

def generate_json():
    problem_id = 225
    title = "Implement Stack using Queues"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>225. Implement Stack using Queues</h3>
<p>Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (<code>push</code>, <code>top</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyStack</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the top of the stack.</li>
	<li><code>int pop()</code> Removes the element on the top of the stack and returns it.</li>
	<li><code>int top()</code> Returns the element on the top of the stack.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the stack is empty, <code>false</code> otherwise.</li>
</ul>

<p><b>Notes:</b></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a queue, which means that only <code>push to back</code>, <code>peek/pop from front</code>, <code>size</code> and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 2, 2, false]

<strong>Explanation</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>top</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you implement the stack using only one queue?</p>"""

    input_format = "Two lines: first, an array of operation names; second, an array of arrays containing operation arguments."
    output_format = "An array of results (null, integers, or booleans)."
    
    constraints = [
        "1 <= x <= 9",
        "At most 100 calls total.",
        "Pop and Top calls are always valid.",
        "Only queue operations allowed."
    ]
    
    explanation = """To implement a LIFO Stack using a FIFO Queue:
1. **Push Strategy (O(N))**:
   - Add the new element to the queue.
   - Rotate the queue: Pop the `size - 1` pre-existing elements and push them back. 
   - This places the newest element at the front of the queue, effectively simulating a stack top.
2. **Pop/Top Strategy (O(1))**:
   - Since the newest element is at the front, `top` is `queue.peek()` and `pop` is `queue.pop()`.
3. **Complexity**:
   - Push: O(N) where N is the number of elements in the stack.
   - Pop/Top: O(1).
   - Space: O(N)."""
    
    answer = """from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate the queue to bring the new element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass MyStack:\n    def __init__(self):\n        self.q = deque()\n    def push(self, x):\n        pass\n    def pop(self):\n        pass\n    def top(self):\n        pass\n    def empty(self):\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if not lines: sys.exit()\n    ops = json.loads(lines[0])\n    vals = json.loads(lines[1])\n    res = []\n    obj = None\n    for op, val in zip(ops, vals):\n        if op == 'MyStack':\n            obj = MyStack()\n            res.append(None)\n        elif op == 'push':\n            obj.push(val[0])\n            res.append(None)\n        elif op == 'pop':\n            res.append(obj.pop())\n        elif op == 'top':\n            res.append(obj.top())\n        elif op == 'empty':\n            res.append(obj.empty())\n    print(json.dumps(res).lower().replace('false', 'false').replace('true', 'true'))",
        "cpp": "class MyStack { /* logic */ };",
        "java": "class MyStack { /* logic */ }",
        "javascript": "var MyStack = function() { /* logic */ };",
        "c": "typedef struct { /* logic */ } MyStack;"
    }

    test_cases = [
        {"input": '["MyStack", "push", "push", "top", "pop", "empty"]\\n[[], [1], [2], [], [], []]', "expected_output": "[null, null, null, 2, 2, false]", "is_sample": True},
        {"input": '["MyStack", "push", "empty"]\\n[[], [1], []]', "expected_output": "[null, null, false]", "is_sample": True},
        {"input": '["MyStack", "empty"]\\n[[], []]', "expected_output": "[null, true]", "is_sample": False},
        {"input": '["MyStack", "push", "push", "push", "pop", "pop", "pop"]\\n[[], [10], [20], [30], [], [], []]', "expected_output": "[null, null, null, null, 30, 20, 10]", "is_sample": False},
        {"input": '["MyStack", "push", "top", "push", "top"]\\n[[], [1], [], [2], []]', "expected_output": "[null, null, 1, null, 2]", "is_sample": False},
        {"input": '["MyStack", "push", "push", "push", "empty", "pop", "pop", "pop", "empty"]\\n[[], [1], [2], [3], [], [], [], [], []]', "expected_output": "[null, null, null, null, false, 3, 2, 1, true]", "is_sample": False},
        {"input": '["MyStack", "push", "pop", "push", "pop"]\\n[[], [5], [], [10], []]', "expected_output": "[null, null, 5, null, 10]", "is_sample": False},
        # Stress Tests (100 calls)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(ops, vals):
        from collections import deque
        q = deque()
        res = []
        for op, val in zip(ops, vals):
            if op == 'MyStack': res.append(None)
            elif op == 'push':
                q.append(val[0])
                for _ in range(len(q)-1): q.append(q.popleft())
                res.append(None)
            elif op == 'pop': res.append(q.popleft())
            elif op == 'top': res.append(q[0])
            elif op == 'empty': res.append(not q)
        return res

    # Stress 8: 100 pushes
    ops8 = ["MyStack"] + ["push"]*99
    vals8 = [[]] + [[i] for i in range(99)]
    test_cases[7] = {"input": json.dumps(ops8) + "\\n" + json.dumps(vals8), "expected_output": json.dumps(_solve(ops8, vals8)).lower().replace('null', 'null'), "is_sample": False}
    # Stress 9: Alternate push/pop
    ops9 = ["MyStack"] + ["push", "pop"]*49
    vals9 = [[]]
    for i in range(49): vals9.extend([[i], []])
    test_cases[8] = {"input": json.dumps(ops9) + "\\n" + json.dumps(vals9), "expected_output": json.dumps(_solve(ops9, vals9)).lower(), "is_sample": False}
    # Stress 10: Mixed pattern
    ops10 = ["MyStack"] + ["push", "push", "top", "pop"]*24 + ["empty"]
    vals10 = [[]]
    for i in range(24): vals10.extend([[i], [i+100], [], []])
    vals10.append([])
    test_cases[9] = {"input": json.dumps(ops10) + "\\n" + json.dumps(vals10), "expected_output": json.dumps(_solve(ops10, vals10)).lower(), "is_sample": False}

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
        "topics": ["Stack", "Design", "Queue"],
        "companyIndex": 0
    }

    output_path = "201-400/225_Implement_Stack_using_Queues.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
