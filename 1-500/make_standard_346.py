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
        "python": "import sys\nimport json\nimport re\n\nclass MovingAverage:\n    def __init__(self, size: int):\n        # User logic here\n        pass\n\n    def next(self, val: int) -> float:\n        # User logic here\n        return 0.0\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    # Lethal parsing: find all commands and all bracketed numbers\n    commands = re.findall(r'\"([^\"]*)\"', input_data)\n    val_groups = re.findall(r'\\[([^\\]]*)\\]', input_data)\n    \n    obj = None\n    res = []\n    for i in range(len(commands)):\n        cmd = commands[i]\n        # Extract numbers from the corresponding group\n        nums = [int(x) for x in re.findall(r'-?\\d+', val_groups[i])]\n        \n        if cmd == \"MovingAverage\":\n            obj = MovingAverage(nums[0])\n            res.append(None)\n        elif cmd == \"next\":\n            avg = obj.next(nums[0])\n            # Formatting to match float/int requirements\n            res.append(round(avg, 5))\n            \n    print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <iomanip>\n#include <algorithm>\nusing namespace std;\n\nclass MovingAverage {\npublic:\n    MovingAverage(int size) {\n        // User logic here\n    }\n\n    double next(int val) {\n        // User logic here\n        return 0.0;\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n\n    regex cmd_re(R\"(\"([^\"]*)\")\");\n    regex val_re(R\"(\\[([^\\]]*)\\])\");\n    \n    auto cmd_begin = sregex_iterator(input.begin(), input.end(), cmd_re);\n    auto val_begin = sregex_iterator(input.begin(), input.end(), val_re);\n    auto end = sregex_iterator();\n\n    MovingAverage* obj = nullptr;\n    cout << \"[\";\n    bool first = true;\n    \n    for (auto i = cmd_begin, j = val_begin; i != end && j != end; ++i, ++j) {\n        if (!first) cout << \",\";\n        first = false;\n        \n        string cmd = (*i)[1].str();\n        string val_str = (*j)[1].str();\n        smatch m;\n        regex num_re(R\"(-?\\d+)\");\n        regex_search(val_str, m, num_re);\n        int val = stoi(m.str());\n\n        if (cmd == \"MovingAverage\") {\n            obj = new MovingAverage(val);\n            cout << \"null\";\n        } else {\n            double res = obj->next(val);\n            if (res == (int)res) cout << (int)res << \".0\";\n            else cout << fixed << setprecision(5) << res;\n        }\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass MovingAverage {\n    public MovingAverage(int size) {\n        // User logic here\n    }\n\n    public double next(int val) {\n        // User logic here\n        return 0.0;\n    }\n}\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n\n        List<String> commands = new ArrayList<>();\n        Matcher m1 = Pattern.compile(\"\\\"([^\\\"]*)\\\"\").matcher(input);\n        while (m1.find()) commands.add(m1.group(1));\n\n        List<String> valGroups = new ArrayList<>();\n        Matcher m2 = Pattern.compile(\"\\\\[([^\\\\]]*)\\\\]\").matcher(input);\n        while (m2.find()) valGroups.add(m2.group(1));\n\n        MovingAverage obj = null;\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < commands.size(); i++) {\n            if (i > 0) sb.append(\",\");\n            String cmd = commands.get(i);\n            Matcher m3 = Pattern.compile(\"-?\\\\d+\").matcher(valGroups.get(i));\n            m3.find();\n            int val = Integer.parseInt(m3.group());\n\n            if (cmd.equals(\"MovingAverage\")) {\n                obj = new MovingAverage(val);\n                sb.append(\"null\");\n            } else {\n                double res = obj.next(val);\n                if (res == (long) res) sb.append((long) res).append(\".0\");\n                else sb.append(String.format(\"%.5f\", res));\n            }\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\nclass MovingAverage {\n    /**\n     * @param {number} size\n     */\n    constructor(size) {\n        // User logic here\n    }\n\n    /**\n     * @param {number} val\n     * @return {number}\n     */\n    next(val) {\n        // User logic here\n    }\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const commands = input.match(/\"([^\"]*)\"/g).map(s => s.slice(1, -1));\n    const args = input.match(/\\[([^\\]]*)\\]/g).map(s => JSON.parse(s));\n\n    let obj = null;\n    const res = commands.map((cmd, i) => {\n        if (cmd === \"MovingAverage\") {\n            obj = new MovingAverage(args[i][0]);\n            return null;\n        } else {\n            const val = obj.next(args[i][0]);\n            return Number(val.toFixed(5));\n        }\n    });\n    console.log(JSON.stringify(res).replace(/ /g, ''));\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\ntypedef struct {\n    // User logic here\n} MovingAverage;\n\nMovingAverage* movingAverageCreate(int size) {\n    // User logic here\n    return NULL;\n}\n\ndouble movingAverageNext(MovingAverage* obj, int val) {\n    // User logic here\n    return 0.0;\n}\n\nvoid movingAverageFree(MovingAverage* obj) {\n    // User logic here\n}\n\nint main() {\n    static char buffer[1000000];\n    int len = fread(buffer, 1, 999999, stdin); buffer[len] = '\\0';\n\n    printf(\"[\");\n    int first = 1;\n    char *ptr = buffer;\n    MovingAverage* obj = NULL;\n\n    // Crude parsing for C\n    char *cmd_ptr = buffer;\n    char *val_ptr = buffer;\n\n    while ((cmd_ptr = strchr(cmd_ptr, '\"')) != NULL) {\n        if (!first) printf(\",\");\n        first = 0;\n\n        cmd_ptr++;\n        char *cmd_end = strchr(cmd_ptr, '\"');\n        *cmd_end = '\\0';\n        char *cmd = cmd_ptr;\n        cmd_ptr = cmd_end + 1;\n\n        val_ptr = strchr(val_ptr, '[');\n        val_ptr++;\n        int val = atoi(val_ptr);\n        val_ptr = strchr(val_ptr, ']');\n\n        if (strcmp(cmd, \"MovingAverage\") == 0) {\n            obj = movingAverageCreate(val);\n            printf(\"null\");\n        } else {\n            double res = movingAverageNext(obj, val);\n            if (res == (int)res) printf(\"%d.0\", (int)res);\n            else printf(\"%.5f\", res);\n        }\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
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
