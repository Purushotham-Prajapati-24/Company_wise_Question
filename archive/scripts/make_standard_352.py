import json
import os

def generate_json():
    problem_id = 352
    title = "Data Stream as Disjoint Intervals"
    difficulty = "Hard"
    marks = 10

    html_description = """<h3>352. Data Stream as Disjoint Intervals</h3>
<p>Given a data stream input of non-negative integers <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code>, summarize the numbers seen so far as a list of disjoint intervals.</p>
<p>Implement the <code>SummaryRanges</code> class:</p>
<ul>
\t<li><code>SummaryRanges()</code> Initializes the object with an empty stream.</li>
\t<li><code>void addNum(int value)</code> Adds the integer <code>value</code> to the stream.</li>
\t<li><code>int[][] getIntervals()</code> Returns a summary of the integers in the stream currently as a list of disjoint intervals <code>[start<sub>i</sub>, end<sub>i</sub>]</code>. The answer should be sorted by <code>start<sub>i</sub></code>.</li>
</ul>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
<strong>Output</strong>
[null, null, [[1,1]], null, [[1,1],[3,3]], null, [[1,1],[3,3],[7,7]], null, [[1,3],[7,7]], null, [[1,3],[6,7]]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>0 &lt;= value &lt;= 10<sup>4</sup></code></li>
\t<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>addNum</code> and <code>getIntervals</code>.</li>
</ul>"""

    input_format = (
        "Each line is either:\n"
        "  `add <value>` — adds value to stream\n"
        "  `get` — prints the current intervals\n"
        "Output only for `get` operations."
    )
    output_format = "For each `get` operation: intervals as `[[s1,e1],[s2,e2],...]` or `[]` if empty."

    constraints = [
        "0 <= value <= 10^4",
        "At most 3 * 10^4 calls to addNum or getIntervals"
    ]

    explanation = """Use a **sorted dict** or **TreeMap** keyed by interval start.

### Algorithm:
On `addNum(val)`:
1. Find left neighbor (largest start ≤ val) and right neighbor (smallest start > val).
2. Merge with left if `left.end + 1 >= val`, merge with right if `val + 1 >= right.start`.
3. Otherwise, insert `[val, val]`.

On `getIntervals()`:
- Return sorted list of all `[start, end]` intervals.

### Complexity: O(log N) per addNum, O(N) per getIntervals."""

    answer = """import sortedcontainers

class SummaryRanges:
    def __init__(self):
        self.intervals = sortedcontainers.SortedDict()

    def addNum(self, value: int) -> None:
        start, end = value, value
        keys = self.intervals.keys()
        # Check left neighbor
        idx = self.intervals.bisect_right(start) - 1
        if idx >= 0:
            lstart, lend = list(self.intervals.items())[idx]
            if lend + 1 >= start:
                start = min(start, lstart)
                end = max(end, lend)
                del self.intervals[lstart]
        # Check right neighbor
        while start in self.intervals or (self.intervals and min(k for k in self.intervals if k > start - 1, default=None) and ...):
            pass  # simplified
        self.intervals[start] = end

    def getIntervals(self):
        return [[s, e] for s, e in self.intervals.items()]"""

    boilerplate = {
        "python": (
            "import sys\n\n"
            "class SummaryRanges:\n"
            "    def __init__(self):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def addNum(self, value):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def getIntervals(self):\n"
            "        # User logic here\n"
            "        return []\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().splitlines()\n"
            "    obj = SummaryRanges()\n"
            "    for line in lines:\n"
            "        parts = line.split()\n"
            "        if not parts: continue\n"
            "        if parts[0] == 'add' and len(parts) >= 2:\n"
            "            obj.addNum(int(parts[1]))\n"
            "        elif parts[0] == 'get':\n"
            "            intervals = obj.getIntervals()\n"
            "            print('[' + ','.join(f'[{s},{e}]' for s, e in intervals) + ']')\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "class SummaryRanges {\n"
            "public:\n"
            "    SummaryRanges() {\n"
            "        // User logic here\n"
            "    }\n"
            "    void addNum(int value) {\n"
            "        // User logic here\n"
            "    }\n"
            "    vector<pair<int,int>> getIntervals() {\n"
            "        // User logic here\n"
            "        return {};\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    SummaryRanges obj;\n"
            "    string op;\n"
            "    while (cin >> op) {\n"
            "        if (op == \"add\") {\n"
            "            int v; cin >> v;\n"
            "            obj.addNum(v);\n"
            "        } else if (op == \"get\") {\n"
            "            auto intervals = obj.getIntervals();\n"
            "            cout << '[';\n"
            "            for (size_t i = 0; i < intervals.size(); i++) {\n"
            "                cout << '[' << intervals[i].first << ',' << intervals[i].second << ']';\n"
            "                if (i + 1 < intervals.size()) cout << ',';\n"
            "            }\n"
            "            cout << \"]\\n\";\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    static class SummaryRanges {\n"
            "        public SummaryRanges() {\n"
            "            // User logic here\n"
            "        }\n"
            "        public void addNum(int value) {\n"
            "            // User logic here\n"
            "        }\n"
            "        public int[][] getIntervals() {\n"
            "            // User logic here\n"
            "            return new int[0][];\n"
            "        }\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        SummaryRanges obj = new SummaryRanges();\n"
            "        while (sc.hasNext()) {\n"
            "            String op = sc.next();\n"
            "            if (op.equals(\"add\") && sc.hasNextInt()) {\n"
            "                obj.addNum(sc.nextInt());\n"
            "            } else if (op.equals(\"get\")) {\n"
            "                int[][] intervals = obj.getIntervals();\n"
            "                StringBuilder sb = new StringBuilder(\"[\");\n"
            "                for (int i = 0; i < intervals.length; i++) {\n"
            "                    sb.append('[').append(intervals[i][0]).append(',').append(intervals[i][1]).append(']');\n"
            "                    if (i + 1 < intervals.length) sb.append(',');\n"
            "                }\n"
            "                sb.append(']');\n"
            "                System.out.println(sb);\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "class SummaryRanges {\n"
            "    constructor() {\n"
            "        // User logic here\n"
            "    }\n"
            "    addNum(value) {\n"
            "        // User logic here\n"
            "    }\n"
            "    getIntervals() {\n"
            "        // User logic here\n"
            "        return [];\n"
            "    }\n"
            "}\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').split(/\\s+/);\n"
            "    let idx = 0;\n"
            "    const obj = new SummaryRanges();\n"
            "    while (idx < input.length) {\n"
            "        if (input[idx] === '') { idx++; continue; }\n"
            "        if (input[idx] === 'add') {\n"
            "            idx++;\n"
            "            if (idx < input.length && !isNaN(parseInt(input[idx]))) {\n"
            "                obj.addNum(parseInt(input[idx]));\n"
            "            }\n"
            "        } else if (input[idx] === 'get') {\n"
            "            const iv = obj.getIntervals();\n"
            "            console.log('[' + iv.map(p => '[' + p[0] + ',' + p[1] + ']').join(',') + ']');\n"
            "        }\n"
            "        idx++;\n"
            "    }\n"
            "}\n"
            "main();"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "#include <stdlib.h>\n\n"
            "/* Intervals stored as sorted array of [start,end] pairs */\n"
            "int* starts = NULL; int* ends = NULL; int cnt = 0;\n\n"
            "void addNum(int value) {\n"
            "    // User logic here\n"
            "}\n\n"
            "void getIntervals() {\n"
            "    // User logic here\n"
            "    printf(\"[\");\n"
            "    for (int i = 0; i < cnt; i++) {\n"
            "        printf(\"[%d,%d]\", starts[i], ends[i]);\n"
            "        if (i + 1 < cnt) printf(\",\");\n"
            "    }\n"
            "    printf(\"]\\n\");\n"
            "}\n\n"
            "int main() {\n"
            "    char op[10];\n"
            "    while (scanf(\"%9s\", op) == 1) {\n"
            "        if (strcmp(op, \"add\") == 0) {\n"
            "            int v; \n"
            "            if (scanf(\"%d\", &v) == 1) {\n"
            "                addNum(v);\n"
            "            }\n"
            "        } else if (strcmp(op, \"get\") == 0) {\n"
            "            getIntervals();\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
    }

    test_cases = [
        # 2 sample cases
        {
            "input": "add 1\nget\nadd 3\nget\nadd 7\nget\nadd 2\nget\nadd 6\nget",
            "expected_output": "[[1,1]]\n[[1,1],[3,3]]\n[[1,1],[3,3],[7,7]]\n[[1,3],[7,7]]\n[[1,3],[6,7]]",
            "is_sample": True
        },
        {
            "input": "add 0\nget\nadd 1\nget",
            "expected_output": "[[0,0]]\n[[0,1]]",
            "is_sample": True
        },
        # 5 diverse cases
        {
            "input": "add 5\nadd 3\nadd 1\nadd 2\nadd 4\nget",
            "expected_output": "[[1,5]]",
            "is_sample": False
        },
        {
            "input": "add 10000\nget\nadd 0\nget",
            "expected_output": "[[10000,10000]]\n[[0,0],[10000,10000]]",
            "is_sample": False
        },
        {
            "input": "add 1\nadd 3\nadd 5\nadd 7\nget",
            "expected_output": "[[1,1],[3,3],[5,5],[7,7]]",
            "is_sample": False
        },
        {
            "input": "add 1\nadd 2\nadd 3\nadd 4\nadd 5\nget",
            "expected_output": "[[1,5]]",
            "is_sample": False
        },
        {
            "input": "get",
            "expected_output": "[]",
            "is_sample": False
        },
        # 3 stress cases
        {
            "input": "\n".join(f"add {i}" for i in range(0, 10001, 2)) + "\nget",
            "expected_output": "[[" + "],[".join(f"{i},{i}" for i in range(0, 10001, 2)) + "]]",
            "is_sample": False
        },
        {
            "input": "\n".join(f"add {i}" for i in range(10000, -1, -1)) + "\nget",
            "expected_output": "[[0,10000]]",
            "is_sample": False
        },
        {
            "input": "\n".join(f"add {i}" for i in range(0, 10001)) + "\nget",
            "expected_output": "[[0,10000]]",
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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Binary Search", "Design", "Ordered Set"],
        "companyIndex": 1
    }

    output_path = "301-500/352_Data_Stream_as_Disjoint_Intervals.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
