import json
import os

def generate_json():
    problem_id = 232
    title = "Implement Queue using Stacks"
    difficulty = "EASY"
    marks = 5
    
    html_description = """<h3>232. Implement Queue using Stacks</h3>
<p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyQueue</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the back of the queue.</li>
	<li><code>int pop()</code> Removes the element from the front of the queue and returns it.</li>
	<li><code>int peek()</code> Returns the element at the front of the queue.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the queue is empty, <code>false</code> otherwise.</li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 1, 1, false]

<strong>Explanation</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code> calls will be made to <code>push</code>, <code>pop</code>, <code>peek</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>peek</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Can you implement the queue such that each operation is <strong>amortized</strong> <code>O(1)</code> time complexity? In other words, performing <code>n</code> operations will take <code>O(n)</code> time even if one of those operations may take longer.
"""

    input_format = "Two lines: first, an array of operation names; second, an array of arrays containing operation arguments."
    output_format = "An array of results (null, integers, or booleans)."
    
    constraints = [
        "1 <= x <= 9",
        "At most 100 calls total.",
        "Pop and Peek are always valid.",
        "Must use exactly two stacks logic."
    ]
    
    explanation = """To implement a queue using two stacks (in_stack and out_stack):
1. **Push**: Always push the new element onto the `in_stack`.
2. **Pop / Peek**:
   - If the `out_stack` is empty, move all elements from the `in_stack` to the `out_stack`. This reverses the order so that the oldest element (FIFO) is now on top.
   - Pop/peek from the `out_stack`.
3. **Empty**: Both stacks must be empty.
4. **Complexity**:
   - Amortized O(1) for all operations because each element is pushed once and popped once from each stack.
   - Space: O(N) where N is the number of elements."""
    
    answer = """class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek() # Ensure out_stack is ready
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass MyQueue:\n    def __init__(self):\n        # Initialize your stacks here\n        pass\n\n    def push(self, x: int) -> None:\n        # User logic\n        pass\n\n    def pop(self) -> int:\n        # User logic\n        return 0\n\n    def peek(self) -> int:\n        # User logic\n        return 0\n\n    def empty(self) -> bool:\n        # User logic\n        return True\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        ops = json.loads(lines[0])\n        args = json.loads(lines[1])\n        obj = None\n        output = []\n        for op, arg in zip(ops, args):\n            if op == \"MyQueue\": \n                obj = MyQueue()\n                output.append(None)\n            elif op == \"push\":\n                obj.push(arg[0])\n                output.append(None)\n            elif op == \"pop\":\n                output.append(obj.pop())\n            elif op == \"peek\":\n                output.append(obj.peek())\n            elif op == \"empty\":\n                output.append(obj.empty())\n        print(json.dumps(output).lower().replace('null', 'null'))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <stack>\n\nusing namespace std;\n\nclass MyQueue {\npublic:\n    MyQueue() {}\n    void push(int x) {}\n    int pop() { return 0; }\n    int peek() { return 0; }\n    bool empty() { return true; }\n};\n\nstring trim(string s) {\n    size_t first = s.find_first_not_of(\" \\t\\n\\r\");\n    size_t last = s.find_last_not_of(\" \\t\\n\\r\");\n    return (first == string::npos || last == string::npos) ? \"\" : s.substr(first, last - first + 1);\n}\n\nvector<string> parseOps(string line) {\n    vector<string> ops;\n    size_t start = line.find('[');\n    size_t end = line.find_last_of(']');\n    if (start == string::npos || end == string::npos) return ops;\n    string content = line.substr(start + 1, end - start - 1);\n    stringstream ss(content);\n    string op;\n    while (getline(ss, op, ',')) {\n        size_t s = op.find('\"');\n        size_t e = op.find_last_of('\"');\n        if (s != string::npos && e != string::npos) ops.push_back(op.substr(s + 1, e - s - 1));\n    }\n    return ops;\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        vector<string> ops = parseOps(line1);\n        // Simplified arg parsing for this problem (only ints)\n        size_t s = line2.find('['), e = line2.find_last_of(']');\n        string content = line2.substr(s + 1, e - s - 1);\n        vector<int> args;\n        stringstream ss(content);\n        string argStr;\n        while (getline(ss, argStr, ']')) {\n            size_t subS = argStr.find('[');\n            if (subS != string::npos) {\n                string val = argStr.substr(subS + 1);\n                if (!trim(val).empty()) args.push_back(stoi(val));\n                else args.push_back(0); // placeholder\n            }\n            if (ss.peek() == ',') ss.ignore();\n        }\n        \n        MyQueue* obj = nullptr;\n        cout << \"[\";\n        int argIdx = 0;\n        for (int i = 0; i < ops.size(); i++) {\n            if (ops[i] == \"MyQueue\") {\n                obj = new MyQueue();\n                cout << \"null\"; argIdx++;\n            } else if (ops[i] == \"push\") {\n                obj->push(args[argIdx++]);\n                cout << \"null\";\n            } else if (ops[i] == \"pop\") {\n                cout << obj->pop(); argIdx++;\n            } else if (ops[i] == \"peek\") {\n                cout << obj->peek(); argIdx++;\n            } else if (ops[i] == \"empty\") {\n                cout << (obj->empty() ? \"true\" : \"false\"); argIdx++;\n            }\n            if (i < ops.size() - 1) cout << \", \";\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\nclass MyQueue {\n    public MyQueue() {}\n    public void push(int x) {}\n    public int pop() { return 0; }\n    public int peek() { return 0; }\n    public boolean empty() { return true; }\n}\n\npublic class Solution {\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 == null || line2 == null) return;\n        \n        String[] ops = line1.replaceAll(\"\\\\[|\\\\]|\\\"\", \"\").split(\",\\\\s*\");\n        String[] argStrings = line2.substring(1, line2.length() - 1).split(\"(?<=\\\\]),\\\\s*(?=\\\\[)\");\n        \n        MyQueue obj = null;\n        List<String> output = new ArrayList<>();\n        for (int i = 0; i < ops.length; i++) {\n            String op = ops[i].trim();\n            if (op.equals(\"MyQueue\")) {\n                obj = new MyQueue();\n                output.add(\"null\");\n            } else if (op.equals(\"push\")) {\n                int val = Integer.parseInt(argStrings[i].replaceAll(\"\\\\[|\\\\]\", \"\").trim());\n                obj.push(val);\n                output.add(\"null\");\n            } else if (op.equals(\"pop\")) {\n                output.add(String.valueOf(obj.pop()));\n            } else if (op.equals(\"peek\")) {\n                output.add(String.valueOf(obj.peek()));\n            } else if (op.equals(\"empty\")) {\n                output.add(String.valueOf(obj.empty()));\n            }\n        }\n        System.out.println(\"[\" + String.join(\", \", output) + \"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nvar MyQueue = function() {\n    // User logic\n};\nMyQueue.prototype.push = function(x) {};\nMyQueue.prototype.pop = function() { return 0; };\nMyQueue.prototype.peek = function() { return 0; };\nMyQueue.prototype.empty = function() { return true; };\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const ops = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    let output = [];\n    for (let i = 0; i < ops.length; i++) {\n        if (ops[i] === \"MyQueue\") {\n            obj = new MyQueue();\n            output.push(null);\n        } else if (ops[i] === \"push\") {\n            obj.push(args[i][0]);\n            output.push(null);\n        } else if (ops[i] === \"pop\") {\n            output.push(obj.pop());\n        } else if (ops[i] === \"peek\") {\n            output.push(obj.peek());\n        } else if (ops[i] === \"empty\") {\n            output.push(obj.empty());\n        }\n    }\n    console.log(JSON.stringify(output));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\ntypedef struct {\n    // User logic\n} MyQueue;\n\nMyQueue* myQueueCreate() {\n    return (MyQueue*)malloc(sizeof(MyQueue));\n}\n\nvoid myQueuePush(MyQueue* obj, int x) {}\nint myQueuePop(MyQueue* obj) { return 0; }\nint myQueuePeek(MyQueue* obj) { return 0; }\nbool myQueueEmpty(MyQueue* obj) { return true; }\nvoid myQueueFree(MyQueue* obj) { free(obj); }\n\nint main() {\n    char line1[1000], line2[1000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        // Extremely simplified parser for C\n        char* op = strtok(line1, \"\\\"[], \");\n        char* argLine = line2;\n        MyQueue* obj = NULL;\n        printf(\"[\");\n        bool first = true;\n        while (op) {\n            if (!first) printf(\", \");\n            first = false;\n            if (strcmp(op, \"MyQueue\") == 0) {\n                obj = myQueueCreate();\n                printf(\"null\");\n            } else if (strcmp(op, \"push\") == 0) {\n                while (*argLine && !(*argLine >= '0' && *argLine <= '9')) argLine++;\n                if (*argLine) {\n                    myQueuePush(obj, atoi(argLine));\n                    while (*argLine && (*argLine >= '0' && *argLine <= '9')) argLine++;\n                }\n                printf(\"null\");\n            } else if (strcmp(op, \"pop\") == 0) {\n                printf(\"%d\", myQueuePop(obj));\n            } else if (strcmp(op, \"peek\") == 0) {\n                printf(\"%d\", myQueuePeek(obj));\n            } else if (strcmp(op, \"empty\") == 0) {\n                printf(\"%s\", myQueueEmpty(obj) ? \"true\" : \"false\");\n            }\n            op = strtok(NULL, \"\\\"[], \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["MyQueue", "push", "push", "peek", "pop", "empty"]\\n[[], [1], [2], [], [], []]', "expected_output": "[null, null, null, 1, 1, false]", "is_sample": True},
        {"input": '["MyQueue", "empty"]\\n[[], []]', "expected_output": "[null, true]", "is_sample": True},
        {"input": '["MyQueue", "push", "pop", "empty"]\\n[[], [5], [], []]', "expected_output": "[null, null, 5, true]", "is_sample": False},
        {"input": '["MyQueue", "push", "push", "push", "pop", "peek", "pop", "peek"]\\n[[], [1], [2], [3], [], [], [], []]', "expected_output": "[null, null, null, null, 1, 2, 2, 3]", "is_sample": False},
        {"input": '["MyQueue", "push", "peek", "push", "peek"]\\n[[], [1], [], [2], []]', "expected_output": "[null, null, 1, null, 1]", "is_sample": False},
        {"input": '["MyQueue", "push", "pop", "push", "pop"]\\n[[], [8], [], [9], []]', "expected_output": "[null, null, 8, null, 9]", "is_sample": False},
        {"input": '["MyQueue", "push", "push", "empty", "pop", "pop", "empty"]\\n[[], [1], [2], [], [], [], []]', "expected_output": "[null, null, null, false, 1, 2, true]", "is_sample": False},
        # Stress Tests (Up to 100 calls)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_mq(ops, vals):
        q = []
        res = []
        for op, val in zip(ops, vals):
            if op == 'MyQueue': res.append(None)
            elif op == 'push': q.append(val[0]); res.append(None)
            elif op == 'pop': res.append(q.pop(0))
            elif op == 'peek': res.append(q[0])
            elif op == 'empty': res.append(len(q) == 0)
        return res

    # Stress 8: 100 push, then 100 pop
    ops8 = ["MyQueue"] + ["push"] * 50 + ["pop"] * 50
    vals8 = [[]] + [[i] for i in range(50)] + [[]] * 50
    test_cases[7] = {"input": json.dumps(ops8) + "\\n" + json.dumps(vals8), "expected_output": json.dumps(_solve_mq(ops8, vals8)).lower(), "is_sample": False}
    # Stress 9: Mixed 100 calls
    ops9 = ["MyQueue"] + ["push", "push", "peek", "pop", "push", "empty", "pop"] * 14
    vals9 = [[]] + [[1], [2], [], [], [3], [], []] * 14
    test_cases[8] = {"input": json.dumps(ops9[:100]) + "\\n" + json.dumps(vals9[:100]), "expected_output": json.dumps(_solve_mq(ops9[:100], vals9[:100])).lower(), "is_sample": False}
    # Stress 10: Empty/Push toggle
    ops10 = ["MyQueue"] + ["empty", "push", "empty", "pop"] * 24
    vals10 = [[]] + [[], [1], [], []] * 24
    test_cases[9] = {"input": json.dumps(ops10[:100]) + "\\n" + json.dumps(vals10[:100]), "expected_output": json.dumps(_solve_mq(ops10[:100], vals10[:100])).lower(), "is_sample": False}

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

    output_path = "201-400/232_Implement_Queue_using_Stacks.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
