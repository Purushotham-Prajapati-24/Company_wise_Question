import json
import os

def generate_json():
    problem_id = 346
    title = "Moving Average from Data Stream"
    difficulty = "Easy"
    marks = 10

    html_description = """<h3>346. Moving Average from Data Stream</h3>
<p>Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.</p>
<p>Implement the <code>MovingAverage</code> class:</p>
<ul>
\t<li><code>MovingAverage(int size)</code> Initializes the object with the size of the window <code>size</code>.</li>
\t<li><code>double next(int val)</code> Returns the moving average of the last <code>size</code> values of the stream.</li>
</ul>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
<strong>Output</strong>
[null, 1.0, 5.5, 4.666..., 6.0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= size &lt;= 1000</code></li>
\t<li><code>-10<sup>5</sup> &lt;= val &lt;= 10<sup>5</sup></code></li>
\t<li>At most <code>10<sup>4</sup></code> calls will be made to <code>next</code>.</li>
</ul>"""

    input_format = (
        "Line 1: window size `size` (integer).\n"
        "Each subsequent line: an integer `val` to add to the stream.\n"
        "Output one moving average per `next` call."
    )
    output_format = "One floating-point number (rounded to 5 decimal places) per line for each `next` call."

    constraints = [
        "1 <= size <= 1000",
        "-10^5 <= val <= 10^5",
        "At most 10^4 calls to next"
    ]

    explanation = """A **sliding window** with a deque (or circular buffer) is the key.

### Algorithm:
1. Maintain a queue of at most `size` elements and a running `window_sum`.
2. On each `next(val)`:
   - Append `val` to the queue and add to `window_sum`.
   - If queue length exceeds `size`, pop the oldest element and subtract from `window_sum`.
   - Return `window_sum / len(queue)`.

### Complexity:
- **Time**: O(1) per `next` call.
- **Space**: O(size) for the window."""

    answer = """from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()
        return self.window_sum / len(self.queue)"""

    boilerplate = {
        "python": (
            "import sys\n\n"
            "class MovingAverage:\n"
            "    def __init__(self, size):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def next(self, val):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "if __name__ == '__main__':\n"
            "    input_data = sys.stdin.read().splitlines()\n"
            "    if len(input_data) > 0:\n"
            "        size = int(input_data[0].strip())\n"
            "        obj = MovingAverage(size)\n"
            "        for val_str in input_data[1:]:\n"
            "            if val_str.strip():\n"
            "                val = int(val_str.strip())\n"
            "                print(round(obj.next(val), 5))"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n"
            "#include <iomanip>\n"
            "using namespace std;\n\n"
            "class MovingAverage {\n"
            "public:\n"
            "    MovingAverage(int size) {\n"
            "        // User logic here\n"
            "    }\n"
            "    double next(int val) {\n"
            "        // User logic here\n"
            "        return 0.0;\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    int size;\n"
            "    if (cin >> size) {\n"
            "        MovingAverage obj(size);\n"
            "        int val;\n"
            "        cout << fixed << setprecision(5);\n"
            "        while (cin >> val) {\n"
            "            cout << obj.next(val) << endl;\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "java": (
            "import java.util.*;\n\n"
            "class MovingAverage {\n"
            "    public MovingAverage(int size) {\n"
            "        // User logic here\n"
            "    }\n"
            "    public double next(int val) {\n"
            "        // User logic here\n"
            "        return 0.0;\n"
            "    }\n"
            "}\n\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextInt()) {\n"
            "            int size = sc.nextInt();\n"
            "            MovingAverage obj = new MovingAverage(size);\n"
            "            while (sc.hasNextInt()) {\n"
            "                System.out.printf(\"%.5f%n\", obj.next(sc.nextInt()));\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "class MovingAverage {\n"
            "    constructor(size) {\n"
            "        // User logic here\n"
            "    }\n"
            "    next(val) {\n"
            "        // User logic here\n"
            "        return 0.0;\n"
            "    }\n"
            "}\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').split(/\\s+/);\n"
            "    if (input.length > 0 && input[0] !== '') {\n"
            "        let idx = 0;\n"
            "        const size = parseInt(input[idx++]);\n"
            "        const obj = new MovingAverage(size);\n"
            "        while (idx < input.length) {\n"
            "            if (input[idx] === '') { idx++; continue; }\n"
            "            const val = parseInt(input[idx++]);\n"
            "            if (!isNaN(val)) {\n"
            "                process.stdout.write(obj.next(val).toFixed(5) + '\\n');\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
            "main();"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n\n"
            "typedef struct {\n"
            "    // User definition here\n"
            "} MovingAverage;\n\n"
            "MovingAverage* movingAverageCreate(int size) {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "double movingAverageNext(MovingAverage* obj, int val) {\n"
            "    // User logic here\n"
            "    return 0.0;\n"
            "}\n\n"
            "int main() {\n"
            "    int size;\n"
            "    if (scanf(\"%d\", &size) == 1) {\n"
            "        MovingAverage* obj = movingAverageCreate(size);\n"
            "        int val;\n"
            "        while (scanf(\"%d\", &val) == 1) {\n"
            "            printf(\"%.5f\\n\", movingAverageNext(obj, val));\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    }

    # Helper to simulate MovingAverage
    from collections import deque
    def simulate(size, vals):
        q, s = deque(), 0
        results = []
        for v in vals:
            q.append(v); s += v
            if len(q) > size: s -= q.popleft()
            results.append(round(s / len(q), 5))
        return results

    def fmt_output(results):
        return "\n".join(str(r) for r in results)

    # Stress: 10000 calls
    import random
    random.seed(7)
    stress_vals_1 = [random.randint(-100000, 100000) for _ in range(10000)]
    stress_res_1 = simulate(500, stress_vals_1)
    stress_vals_2 = [random.randint(0, 100) for _ in range(10000)]
    stress_res_2 = simulate(1000, stress_vals_2)
    stress_vals_3 = list(range(1, 10001))  # 1..10000
    stress_res_3 = simulate(3, stress_vals_3)

    def make_input(size, vals):
        return str(size) + "\n" + "\n".join(str(v) for v in vals)

    test_cases = [
        # 2 sample cases
        {
            "input": "3\n1\n10\n3\n5",
            "expected_output": "1.0\n5.5\n4.66667\n6.0",
            "is_sample": True
        },
        {
            "input": "1\n4\n7\n2",
            "expected_output": "4.0\n7.0\n2.0",
            "is_sample": True
        },
        # 5 diverse cases
        {
            "input": "2\n10\n20\n30",
            "expected_output": "10.0\n15.0\n25.0",
            "is_sample": False
        },
        {
            "input": "5\n1\n2\n3\n4\n5\n6",
            "expected_output": "1.0\n1.5\n2.0\n2.5\n3.0\n4.0",
            "is_sample": False
        },
        {
            "input": "3\n-3\n-6\n-9",
            "expected_output": "-3.0\n-4.5\n-6.0",
            "is_sample": False
        },
        {
            "input": "1000\n" + "\n".join(["100000"] * 100),
            "expected_output": "\n".join(["100000.0"] * 100),
            "is_sample": False
        },
        {
            "input": "3\n0\n0\n0",
            "expected_output": "0.0\n0.0\n0.0",
            "is_sample": False
        },
        # 3 stress cases (precomputed)
        {
            "input": make_input(500, stress_vals_1),
            "expected_output": fmt_output(stress_res_1),
            "is_sample": False
        },
        {
            "input": make_input(1000, stress_vals_2),
            "expected_output": fmt_output(stress_res_2),
            "is_sample": False
        },
        {
            "input": make_input(3, stress_vals_3),
            "expected_output": fmt_output(stress_res_3),
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
        "topics": ["Array", "Design", "Queue", "Sliding Window"],
        "companyIndex": 1
    }

    output_path = "301-500/346_Moving_Average_from_Data_Stream.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
