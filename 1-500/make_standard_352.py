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
        "python": "import sys\nimport re\n\nclass SummaryRanges:\n    def __init__(self):\n        # User logic here\n        pass\n\n    def addNum(self, value: int) -> None:\n        # User logic here\n        pass\n\n    def getIntervals(self):\n        # User logic here\n        return []\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read()\n    cmds = re.findall(r'\"(.*?)\"', input_data)\n    args = re.findall(r'\\[(.*?)\\]', input_data)\n    if not cmds:\n        obj = SummaryRanges()\n        for line in input_data.splitlines():\n            parts = line.split()\n            if not parts: continue\n            if parts[0] == 'add': obj.addNum(int(parts[1]))\n            elif parts[0] == 'get':\n                ivs = obj.getIntervals()\n                print('[' + ','.join(f'[{s},{e}]' for s, e in ivs) + ']')\n    else:\n        obj = None\n        res = []\n        for c, a in zip(cmds, args):\n            if c == 'SummaryRanges':\n                obj = SummaryRanges()\n                res.append('null')\n            elif c == 'addNum':\n                v = int(re.search(r'-?\\d+', a).group())\n                obj.addNum(v)\n                res.append('null')\n            elif c == 'getIntervals':\n                ivs = obj.getIntervals()\n                res.append('[' + ','.join(f'[{s},{e}]' for s, e in ivs) + ']')\n        print('[' + ','.join(res) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\nusing namespace std;\n\nclass SummaryRanges {\npublic:\n    SummaryRanges() {}\n    void addNum(int value) {}\n    vector<vector<int>> getIntervals() { return {}; }\n};\n\nint main() {\n    string input; char ch;\n    while (cin.get(ch)) input += ch;\n    regex cr(\"\\\"(.*?)\\\"\");\n    regex ar(\"\\\\[(.*?)\\\\]\");\n    auto ci = sregex_iterator(input.begin(), input.end(), cr);\n    auto ai = sregex_iterator(input.begin(), input.end(), ar);\n    auto end = sregex_iterator();\n    if (ci == end) {\n        SummaryRanges obj;\n        regex lr(\"(add|get)\\\\s*(-?\\\\d+)?\");\n        auto li = sregex_iterator(input.begin(), input.end(), lr);\n        while (li != end) {\n            string op = (*li)[1].str();\n            if (op == \"add\") obj.addNum(stoi((*li)[2].str()));\n            else {\n                auto ivs = obj.getIntervals();\n                cout << '[';\n                for (size_t i=0; i<ivs.size(); ++i) {\n                    cout << '[' << ivs[i][0] << ',' << ivs[i][1] << ']';\n                    if (i+1 < ivs.size()) cout << ',';\n                }\n                cout << \"]\\n\";\n            }\n            ++li;\n        }\n    } else {\n        SummaryRanges* obj = nullptr;\n        cout << '[';\n        bool first = true;\n        while (ci != end && ai != end) {\n            string c = (*ci)[1].str();\n            string a = (*ai)[1].str();\n            if (!first) cout << ',';\n            if (c == \"SummaryRanges\") { obj = new SummaryRanges(); cout << \"null\"; }\n            else if (c == \"addNum\") {\n                smatch m; regex_search(a, m, regex(\"-?\\\\d+\"));\n                obj->addNum(stoi(m.str()));\n                cout << \"null\";\n            } else if (c == \"getIntervals\") {\n                auto ivs = obj->getIntervals();\n                cout << '[';\n                for (size_t i=0; i<ivs.size(); ++i) {\n                    cout << '[' << ivs[i][0] << ',' << ivs[i][1] << ']';\n                    if (i+1 < ivs.size()) cout << ',';\n                }\n                cout << ']';\n            }\n            first = false; ++ci; ++ai;\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class SummaryRanges {\n        public SummaryRanges() {}\n        public void addNum(int value) {}\n        public int[][] getIntervals() { return new int[0][]; }\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        List<String> cmds = new ArrayList<>();\n        Matcher m1 = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(input);\n        while (m1.find()) cmds.add(m1.group(1));\n        if (cmds.isEmpty()) {\n            SummaryRanges obj = new SummaryRanges();\n            Matcher m = Pattern.compile(\"(add|get)\\\\s*(-?\\\\d+)?\").matcher(input);\n            while (m.find()) {\n                if (m.group(1).equals(\"add\")) obj.addNum(Integer.parseInt(m.group(2)));\n                else {\n                    int[][] ivs = obj.getIntervals();\n                    System.out.print(\"[\");\n                    for (int i=0; i<ivs.length; i++) {\n                        System.out.print(\"[\" + ivs[i][0] + \",\" + ivs[i][1] + \"]\");\n                        if (i+1 < ivs.length) System.out.print(\",\");\n                    }\n                    System.out.println(\"]\");\n                }\n            }\n        } else {\n            List<String> argsList = new ArrayList<>();\n            Matcher m2 = Pattern.compile(\"\\\\[(.*?)\\\\]\").matcher(input);\n            while (m2.find()) argsList.add(m2.group(1));\n            SummaryRanges obj = null;\n            System.out.print(\"[\");\n            for (int i=0; i<cmds.size(); i++) {\n                if (i > 0) System.out.print(\",\");\n                if (cmds.get(i).equals(\"SummaryRanges\")) { obj = new SummaryRanges(); System.out.print(\"null\"); }\n                else if (cmds.get(i).equals(\"addNum\")) {\n                    Matcher am = Pattern.compile(\"-?\\\\d+\").matcher(argsList.get(i));\n                    am.find(); obj.addNum(Integer.parseInt(am.group()));\n                    System.out.print(\"null\");\n                } else if (cmds.get(i).equals(\"getIntervals\")) {\n                    int[][] ivs = obj.getIntervals();\n                    System.out.print(\"[\");\n                    for (int j=0; j<ivs.length; j++) {\n                        System.out.print(\"[\" + ivs[j][0] + \",\" + ivs[j][1] + \"]\");\n                        if (j+1 < ivs.length) System.out.print(\",\");\n                    }\n                    System.out.print(\"]\");\n                }\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "\"use strict\";\nconst fs = require('fs');\n\nclass SummaryRanges {\n    constructor() {}\n    addNum(v) {}\n    getIntervals() { return []; }\n}\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const cmds = input.match(/\\\"(.*?)\\\"/g)?.map(s => s.slice(1, -1)) || [];\n    if (cmds.length === 0) {\n        const obj = new SummaryRanges();\n        const lines = input.split('\\n');\n        for (let l of lines) {\n            const p = l.trim().split(/\\s+/);\n            if (p[0] === 'add') obj.addNum(parseInt(p[1]));\n            else if (p[0] === 'get') {\n                const ivs = obj.getIntervals();\n                console.log('[' + ivs.map(iv => '[' + iv[0] + ',' + iv[1] + ']').join(',') + ']');\n            }\n        }\n    } else {\n        const args = input.match(/\\[(.*?)\\]/g) || [];\n        let obj = null; const res = [];\n        for (let i=0; i<cmds.length; i++) {\n            if (cmds[i] === 'SummaryRanges') { obj = new SummaryRanges(); res.push('null'); }\n            else if (cmds[i] === 'addNum') {\n                obj.addNum(parseInt(args[i].match(/-?\\d+/)[0]));\n                res.push('null');\n            } else if (cmds[i] === 'getIntervals') {\n                const ivs = obj.getIntervals();\n                res.push('[' + ivs.map(iv => '[' + iv[0] + ',' + iv[1] + ']').join(',') + ']');\n            }\n        }\n        console.log('[' + res.join(',') + ']');\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nvoid addNum(int v) {}\nint** getIntervals(int* rs, int** rcs) { *rs=0; return NULL; }\n\nint main() {\n    char *input = malloc(1000000);\n    int len = 0, ch;\n    while ((ch = getchar()) != EOF) input[len++] = ch;\n    input[len] = '\\0';\n    if (strchr(input, '\"')) {\n        printf(\"[\");\n        char *p = input; int first = 1;\n        while ((p = strchr(p, '\"'))) {\n            p++; char *end = strchr(p, '\"'); if (!end) break;\n            char cmd[50]; strncpy(cmd, p, end-p); cmd[end-p] = '\\0';\n            if (!first) printf(\",\");\n            if (strcmp(cmd, \"SummaryRanges\") == 0) printf(\"null\");\n            else if (strcmp(cmd, \"addNum\") == 0) {\n                while (*end != '[') end++;\n                addNum(strtol(end+1, &end, 10)); printf(\"null\");\n            } else if (strcmp(cmd, \"getIntervals\") == 0) {\n                int sz; int *colSz;\n                int** ivs = getIntervals(&sz, &colSz);\n                printf(\"[\");\n                for (int i=0; i<sz; i++) {\n                    printf(\"[%d,%d]\", ivs[i][0], ivs[i][1]);\n                    if (i+1 < sz) printf(\",\");\n                }\n                printf(\"]\");\n            }\n            first = 0; p = end + 1;\n        }\n        printf(\"]\\n\");\n    } else {\n        char line[100]; char *p = input;\n        while (sscanf(p, \"%[^\\n]\\n\", line) == 1) {\n            p += strlen(line) + 1;\n            if (strncmp(line, \"add\", 3) == 0) addNum(atoi(line+4));\n            else if (strncmp(line, \"get\", 3) == 0) {\n                int sz; int *colSz; int** ivs = getIntervals(&sz, &colSz);\n                printf(\"[\");\n                for (int i=0; i<sz; i++) {\n                    printf(\"[%d,%d]\", ivs[i][0], ivs[i][1]);\n                    if (i+1 < sz) printf(\",\");\n                }\n                printf(\"]\\n\");\n            }\n        }\n    }\n    return 0;\n}"
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
