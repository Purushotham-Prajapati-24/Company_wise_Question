import json
import os

def generate_json():
    problem_id = 716
    title = "Max Stack"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>716. Max Stack</h3>
<p>Design a max stack data structure that supports the stack operations and can fully retrieve the maximum element in the stack.</p>
<p>Implement the <code>MaxStack</code> class:</p>
<ul>
	<li><code>MaxStack()</code> Initializes the stack object.</li>
	<li><code>void push(int x)</code> Pushes element <code>x</code> onto the stack.</li>
	<li><code>int pop()</code> Removes the element on top of the stack and returns it.</li>
	<li><code>int top()</code> Gets the element on the top of the stack without removing it.</li>
	<li><code>int peekMax()</code> Retrieves the maximum element in the stack without removing it.</li>
	<li><code>int popMax()</code> Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the <strong>top-most</strong> one.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
<strong>Output</strong>
[null, null, null, null, 5, 5, 1, 5, 1, 5]

<strong>Explanation</strong>
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top element is 5, the maximum element is 5
stk.push(1);   // [5, 1] the top element is 1, the maximum element is 5
stk.push(5);   // [5, 1, 5] the top element is 5, the maximum element is 5
stk.top();     // return 5, [5, 1, 5] the top element is 5, the maximum element is 5
stk.popMax();  // return 5, [5, 1] the top element is 1, the maximum element is 5
stk.top();     // return 1, [5, 1] the top element is 1, the maximum element is 5
stk.peekMax(); // return 5, [5, 1] the top element is 1, the maximum element is 5
stk.pop();     // return 1, [5] the top element is 5, the maximum element is 5
stk.top();     // return 5, [5] the top element is 5, the maximum element is 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-10<sup>7</sup> <= x <= 10<sup>7</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, <code>peekMax</code>, and <code>popMax</code>.</li>
	<li>There will be <strong>at least one element</strong> in the stack when <code>pop</code>, <code>top</code>, <code>peekMax</code>, or <code>popMax</code> is called.</li>
</ul>"""

    input_format = "A list of operations and a list of arguments."
    output_format = "A list of results (null for void, integer for retrieval)."
    
    constraints = ["-10^7 <= x <= 10^7", "10^4 operations", "Stack not empty during pop/top/max operations"]
    
    explanation = """HARD problem on ."""
    
    answer = """import heapq
class MaxStack:
    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set()
        self.id_counter = 0

    def push(self, x):
        heapq.heappush(self.heap, (-x, -self.id_counter))
        self.stack.append((x, self.id_counter))
        self.id_counter += 1

    def _clean_stack(self):
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()

    def _clean_heap(self):
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)

    def pop(self):
        self._clean_stack()
        x, item_id = self.stack.pop()
        self.removed.add(item_id)
        return x

    def top(self):
        self._clean_stack()
        return self.stack[-1][0]

    def peekMax(self):
        self._clean_heap()
        return -self.heap[0][0]

    def popMax(self):
        self._clean_heap()
        x_neg, id_neg = heapq.heappop(self.heap)
        self.removed.add(-id_neg)
        return -x_neg"""

    boilerplate = {
        "python": "import sys\n\ndef popMax():\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    print(popMax())",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint popMax() {\n    // User logic\n    return 0;\n}\n\nint main() {\n    cout << popMax() << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": '["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]\\n[[], [5], [1], [5], [], [], [], [], [], []]', "expected_output": "[null, null, null, null, 5, 5, 1, 5, 1, 5]", "is_sample": True},
        {"input": '["MaxStack", "push", "peekMax", "popMax"]\\n[[], [5], [], []]', "expected_output": "[null, null, 5, 5]", "is_sample": True},
        {"input": '["MaxStack", "push", "push", "popMax", "popMax"]\\n[[], [1], [2], [], []]', "expected_output": "[null, null, null, 2, 1]", "is_sample": False}, # Correction: popMax returns val.
        {"input": '["MaxStack", "push", "push", "push", "popMax", "popMax", "popMax"]\\n[[], [10], [5], [10], [], [], []]', "expected_output": "[null, null, null, null, 10, 10, 5]", "is_sample": False},
        {"input": '["MaxStack", "push", "push", "push", "pop", "peekMax", "popMax"]\\n[[], [7], [2], [9], [], [], []]', "expected_output": "[null, null, null, null, 9, 7, 7]", "is_sample": False},
        {"input": '["MaxStack", "push", "push", "top", "peekMax"]\\n[[], [1], [2], [], []]', "expected_output": "[null, null, null, 2, 2]", "is_sample": False},
        {"input": '["MaxStack", "push", "push", "push", "popMax", "peekMax"]\\n[[], [1], [2], [3], [], []]', "expected_output": "[null, null, null, null, 3, 2]", "is_sample": False},
        {"input": '["MaxStack", "push", "push", "push", "popMax", "pop", "top"]\\n[[], [5], [1], [2], [], [], []]', "expected_output": "[null, null, null, null, 5, 2, 1]", "is_sample": False},
        {"input": '["MaxStack", "push", "popMax", "push", "popMax"]\\n[[], [100], [], [200], []]', "expected_output": "[null, null, 100, null, 200]", "is_sample": False},
        {"input": '["MaxStack", "push", "push", "push", "popMax", "pop", "pop"]\\n[[], [1], [1], [1], [], [], []]', "expected_output": "[null, null, null, null, 1, 1, 1]", "is_sample": False}]

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = "1-1000/716_Max_Stack.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
