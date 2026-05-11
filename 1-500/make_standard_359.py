import json
import os

def generate_json():
    problem_id = 359
    title = "Logger Rate Limiter"
    difficulty = "Easy"
    marks = 10

    html_description = """<h3>359. Logger Rate Limiter</h3>
<p>Design a logger system that receives a stream of messages along with their timestamps. Each <strong>unique</strong> message should only be printed <strong>at most every 10 seconds</strong> (i.e. a message printed at timestamp <code>t</code> will prevent other identical messages from being printed until timestamp <code>t + 10</code>).</p>
<p>All messages will come in chronological order. Several messages may arrive at the same timestamp.</p>
<p>Implement the <code>Logger</code> class:</p>
<ul>
\t<li><code>Logger()</code> Initializes the <code>logger</code> object.</li>
\t<li><code>bool shouldPrintMessage(int timestamp, string message)</code> Returns <code>true</code> if the <code>message</code> should be printed in the given <code>timestamp</code>, otherwise returns <code>false</code>.</li>
</ul>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
<strong>Output</strong>
[null, true, true, false, false, false, true]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>0 &lt;= timestamp &lt;= 10<sup>9</sup></code></li>
\t<li>Every <code>timestamp</code> will be passed in non-decreasing order (chronological).</li>
\t<li><code>1 &lt;= message.length &lt;= 30</code></li>
\t<li>At most <code>10<sup>4</sup></code> calls will be made to <code>shouldPrintMessage</code>.</li>
</ul>"""

    input_format = (
        "Each line: `timestamp message` (int and string, space-separated).\n"
        "Output `true` or `false` per line."
    )
    output_format = "One `true` or `false` per line for each `shouldPrintMessage` call."

    constraints = [
        "0 <= timestamp <= 10^9",
        "Timestamps are in non-decreasing order",
        "1 <= message.length <= 30",
        "At most 10^4 calls to shouldPrintMessage"
    ]

    explanation = """Use a **hash map** from message → last print timestamp.

### Algorithm for `shouldPrintMessage(ts, msg)`:
1. If `msg` not in map OR `map[msg] + 10 <= ts`:
   - Update `map[msg] = ts`.
   - Return `True`.
2. Otherwise return `False`.

### Complexity:
- **Time**: O(1) per call (hash map lookup).
- **Space**: O(M) — number of unique messages."""

    answer = """class Logger:
    def __init__(self):
        self.last_print = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_print or self.last_print[message] + 10 <= timestamp:
            self.last_print[message] = timestamp
            return True
        return False"""
    boilerplate = {
        "python": "import sys\nimport re\n\nclass Logger:\n    def __init__(self):\n        # User logic here\n        pass\n    def shouldPrintMessage(self, timestamp, message):\n        # User logic here\n        return True\n\nif __name__ == '__main__':\n    obj = Logger()\n    input_data = sys.stdin.read().splitlines()\n    for line in input_data:\n        parts = re.findall(r'(\\d+)\\s+(.+)', line)\n        if parts:\n            ts, msg = parts[0]\n            print(str(obj.shouldPrintMessage(int(ts), msg)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <sstream>\nusing namespace std;\n\nclass Logger {\npublic:\n    Logger() {}\n    bool shouldPrintMessage(int timestamp, string message) {\n        // User logic here\n        return true;\n    }\n};\n\nint main() {\n    Logger obj;\n    string line;\n    while (getline(cin, line)) {\n        stringstream ss(line);\n        int ts;\n        string msg;\n        if (ss >> ts >> msg) {\n            cout << (obj.shouldPrintMessage(ts, msg) ? \"true\" : \"false\") << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    static class Logger {\n        public Logger() {}\n        public boolean shouldPrintMessage(int timestamp, String message) {\n            // User logic here\n            return true;\n        }\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Logger obj = new Logger();\n        while (sc.hasNext()) {\n            int ts = sc.nextInt();\n            String msg = sc.next();\n            System.out.println(obj.shouldPrintMessage(ts, msg));\n        }\n    }\n}",
        "javascript": "\"use strict\";\nconst fs = require('fs');\nclass Logger {\n    constructor() {}\n    shouldPrintMessage(timestamp, message) {\n        // User logic here\n        return true;\n    }\n}\nfunction main() {\n    const obj = new Logger();\n    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n    input.forEach(line => {\n        const match = line.match(/(\\d+)\\s+(.+)/);\n        if (match) {\n            console.log(obj.shouldPrintMessage(parseInt(match[1]), match[2]));\n        }\n    });\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\n// User logic here\nbool shouldPrintMessage(int timestamp, char* message) {\n    return true;\n}\n\nint main() {\n    int ts; char msg[100];\n    while (scanf(\"%d %s\", &ts, msg) != EOF) {\n        printf(\"%s\\n\", shouldPrintMessage(ts, msg) ? \"true\" : \"false\");\n    }\n    return 0;\n}"
    }

    # Precompute stress test outputs
    def simulate_logger(ops):
        last = {}
        res = []
        for ts, msg in ops:
            if msg not in last or last[msg] + 10 <= ts:
                last[msg] = ts
                res.append("true")
            else:
                res.append("false")
        return res

    # Stress 1: 10000 unique messages, all at t=0
    ops1 = [(0, f"msg{i}") for i in range(10000)]
    res1 = simulate_logger(ops1)

    # Stress 2: same message repeated many times, spacing 1
    ops2 = [(i, "foo") for i in range(10000)]
    res2 = simulate_logger(ops2)

    # Stress 3: alternating two messages at every timestamp
    ops3 = [(i, "a" if i % 2 == 0 else "b") for i in range(10000)]
    res3 = simulate_logger(ops3)

    test_cases = [
        # 2 sample cases
        {
            "input": "1 foo\n2 bar\n3 foo\n8 bar\n10 foo\n11 foo",
            "expected_output": "true\ntrue\nfalse\nfalse\nfalse\ntrue",
            "is_sample": True
        },
        {
            "input": "0 hello\n5 hello\n10 hello\n11 hello",
            "expected_output": "true\nfalse\ntrue\nfalse",
            "is_sample": True
        },
        # 5 diverse cases
        {
            "input": "0 a\n10 a\n20 a",
            "expected_output": "true\ntrue\ntrue",
            "is_sample": False
        },
        {
            "input": "0 x\n9 x",
            "expected_output": "true\nfalse",
            "is_sample": False
        },
        {
            "input": "0 cat\n0 dog\n0 cat",
            "expected_output": "true\ntrue\nfalse",
            "is_sample": False
        },
        {
            "input": "1000000000 big",
            "expected_output": "true",
            "is_sample": False
        },
        {
            "input": "1 a\n2 b\n3 c\n4 d\n5 e\n11 a\n12 b",
            "expected_output": "true\ntrue\ntrue\ntrue\ntrue\ntrue\ntrue",
            "is_sample": False
        },
        # 3 stress cases (precomputed)
        {
            "input": "\n".join(f"{ts} {msg}" for ts, msg in ops1),
            "expected_output": "\n".join(res1),
            "is_sample": False
        },
        {
            "input": "\n".join(f"{ts} {msg}" for ts, msg in ops2),
            "expected_output": "\n".join(res2),
            "is_sample": False
        },
        {
            "input": "\n".join(f"{ts} {msg}" for ts, msg in ops3),
            "expected_output": "\n".join(res3),
            "is_sample": False
        },
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
        "topics": ["Hash Table", "Design"],
        "companyIndex": 1
    }

    output_path = "301-500/359_Logger_Rate_Limiter.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
