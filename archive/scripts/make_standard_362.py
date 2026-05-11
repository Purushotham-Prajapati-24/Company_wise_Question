import json
import os

def generate_json():
    problem_id = 362
    title = "Design Hit Counter"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>362. Design Hit Counter</h3>
<p>Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past <code>300</code> seconds).</p>

<p>Implement the <code>HitCounter</code> class:</p>
<ul>
    <li><code>HitCounter()</code> Initializes the hit counter object.</li>
    <li><code>void hit(int timestamp)</code> Records a hit that happened at <code>timestamp</code> (in seconds). Multiple hits can happen at the same <code>timestamp</code>.</li>
    <li><code>int getHits(int timestamp)</code> Returns the number of hits in the past 300 seconds from <code>timestamp</code> (i.e., the range <code>[timestamp - 299, timestamp]</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
<strong>Output:</strong>
[null, null, null, null, 3, null, 4, 3]
<strong>Explanation:</strong>
HitCounter counter = new HitCounter();
counter.hit(1);       // hit at timestamp 1
counter.hit(2);       // hit at timestamp 2
counter.hit(3);       // hit at timestamp 3
counter.getHits(4);   // get hits at timestamp 4, should return 3.
counter.hit(300);     // hit at timestamp 300
counter.getHits(300); // get hits at timestamp 300, should return 4.
counter.getHits(301); // get hits at timestamp 301, should return 3 (hit at timestamp 1 is outdated).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= timestamp &lt;= 2 * 10<sup>9</sup></code></li>
	<li>All the calls are being made to the system in chronological order (i.e., <code>timestamp</code> is monotonically increasing).</li>
	<li>At most <code>300</code> calls will be made to <code>hit</code> and <code>getHits</code>. (Note: Many platforms use 10^4 as the limit)</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the number of hits per second is very large? Does your design scale?</p>"""

    input_format = "Calls to `hit(timestamp)` and `getHits(timestamp)`."
    output_format = "Integers representing hit counts."
    
    constraints = [
        "1 <= timestamp <= 2 * 10^9",
        "Chronological order guaranteed."
    ]
    
    explanation = """To design a hit counter that handles hits in a rolling 300-second window, we can use a **Circular Buffer** or a **Queue**.

### Approach 1: Deque (Queue)
- Store each hit timestamp in a deque.
- `hit(timestamp)`: Append `timestamp`.
- `getHits(timestamp)`: Remove all timestamps from the front of the deque that are $\le timestamp - 300$. Return the remaining length.
- **Pros**: Simple.
- **Cons**: Memory can grow if many hits occur in 300s.

### Approach 2: Circular Buffer (Scalable)
- Use two arrays of size 300: `times` and `hits`.
  - `times[i]` stores the timestamp.
  - `hits[i]` stores the number of hits at that timestamp.
- Use `timestamp % 300` as the index.
- `hit(timestamp)`: 
  - If `times[index] == timestamp`, increment `hits[index]`.
  - If `times[index] != timestamp` (it's an old timestamp), reset `times[index] = timestamp` and `hits[index] = 1`.
- `getHits(timestamp)`: Iterate through the `times` array. If `timestamp - times[i] < 300`, sum up `hits[i]`.
- **Pros**: Constant memory $O(300)$, handles massive concurrent hits at the same timestamp efficiently.

### Complexity Analysis:
- **Time Complexity**: 
  - `hit()`: $O(1)$.
  - `getHits()`: $O(300) = O(1)$.
- **Space Complexity**: $O(300) = O(1)$."""
    
    answer = """class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total"""

    boilerplate = {
        "python": (
            "import sys\n\n"
            "class HitCounter:\n"
            "    def __init__(self):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def hit(self, timestamp: int) -> None:\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def getHits(self, timestamp: int) -> int:\n"
            "        # User logic here\n"
            "        return 0\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().strip().splitlines()\n"
            "    obj = HitCounter()\n"
            "    for line in lines:\n"
            "        if not line.strip(): continue\n"
            "        parts = line.strip().split()\n"
            "        if parts[0] == 'hit':\n"
            "            obj.hit(int(parts[1]))\n"
            "        elif parts[0] == 'get':\n"
            "            print(obj.getHits(int(parts[1])))\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <deque>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "class HitCounter {\n"
            "public:\n"
            "    HitCounter() {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    void hit(int timestamp) {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    int getHits(int timestamp) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    HitCounter obj;\n"
            "    string op;\n"
            "    int ts;\n"
            "    while (cin >> op >> ts) {\n"
            "        if (op == \"hit\") obj.hit(ts);\n"
            "        else if (op == \"get\") cout << obj.getHits(ts) << \"\\n\";\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    static class HitCounter {\n"
            "        public HitCounter() {\n"
            "            // User logic here\n"
            "        }\n"
            "        \n"
            "        public void hit(int timestamp) {\n"
            "            // User logic here\n"
            "        }\n"
            "        \n"
            "        public int getHits(int timestamp) {\n"
            "            // User logic here\n"
            "            return 0;\n"
            "        }\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        HitCounter obj = new HitCounter();\n"
            "        while (sc.hasNext()) {\n"
            "            String op = sc.next();\n"
            "            int ts = sc.nextInt();\n"
            "            if (op.equals(\"hit\")) obj.hit(ts);\n"
            "            else if (op.equals(\"get\")) System.out.println(obj.getHits(ts));\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "class HitCounter {\n"
            "    constructor() {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    hit(timestamp) {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    getHits(timestamp) {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n"
            "}\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n"
            "    const obj = new HitCounter();\n"
            "    for (const line of input) {\n"
            "        if (!line.trim()) continue;\n"
            "        const [op, ts] = line.trim().split(/\\s+/);\n"
            "        if (op === 'hit') obj.hit(parseInt(ts));\n"
            "        else if (op === 'get') console.log(obj.getHits(parseInt(ts)));\n"
            "    }\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "#include <stdlib.h>\n\n"
            "typedef struct {\n"
            "    int times[300];\n"
            "    int hits[300];\n"
            "} HitCounter;\n\n"
            "void hitCreate(HitCounter* obj) {\n"
            "    // User logic here\n"
            "}\n\n"
            "void hit(HitCounter* obj, int timestamp) {\n"
            "    // User logic here\n"
            "}\n\n"
            "int getHits(HitCounter* obj, int timestamp) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "int main() {\n"
            "    HitCounter obj;\n"
            "    hitCreate(&obj);\n"
            "    char op[10];\n"
            "    int ts;\n"
            "    while (scanf(\"%s %d\", op, &ts) == 2) {\n"
            "        if (strcmp(op, \"hit\") == 0) hit(&obj, ts);\n"
            "        else if (strcmp(op, \"get\") == 0) printf(\"%d\\n\", getHits(&obj, ts));\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
    }

    test_cases = [
        {"input": "hit 1\nhit 2\nhit 3\nget 4\nhit 300\nget 300\nget 301", "expected_output": "3\n4\n3", "is_sample": True},
        {"input": "hit 1\nhit 1\nget 1", "expected_output": "2", "is_sample": False},
        {"input": "hit 300\nget 600", "expected_output": "0", "is_sample": False},
        {"input": "hit 1\nget 300", "expected_output": "1", "is_sample": False},
        {"input": "get 1000", "expected_output": "0", "is_sample": False},
        {"input": "hit 1\nhit 2\nhit 3\nget 301", "expected_output": "0", "is_sample": False},
        {"input": "hit 1\nhit 301\nget 301", "expected_output": "1", "is_sample": False},
        {"input": "hit 100\nget 399", "expected_output": "1", "is_sample": False},
        {"input": "\n".join(f"hit {i}" for i in range(1, 301)) + "\nget 300", "expected_output": "300", "is_sample": False},
        {"input": "\n".join(f"hit {i}" for i in range(1, 301)) + "\nget 400", "expected_output": "100", "is_sample": False},
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
        "topics": ["Array", "Hash Table", "Design", "Queue"],
        "companyIndex": 1
    }

    output_path = "301-500/362_Design_Hit_Counter.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
