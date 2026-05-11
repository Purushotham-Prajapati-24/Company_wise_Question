import json
import os

def generate_json():
    problem_id = 251
    title = "Flatten 2D Vector"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>251. Flatten 2D Vector</h3>
<p>Design an iterator to flatten a 2D vector. It should support the <code>next</code> and <code>hasNext</code> operations.</p>

<p>Implement the <code>Vector2D</code> class:</p>

<ul>
	<li><code>Vector2D(int[][] v)</code> initializes the object with the 2D vector <code>v</code>.</li>
	<li><code>next()</code> returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all calls to <code>next</code> are valid.</li>
	<li><code>hasNext()</code> returns <code>true</code> if there are still some elements in the 2D vector, and <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [], [4]]], [], [], [], [], [], [], []]
<strong>Output</strong>
[null, 1, 2, 3, true, true, 4, false]

<strong>Explanation</strong>
Vector2D vector2D = new Vector2D([[1, 2], [3], [], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= v.length &lt;= 250</code></li>
	<li><code>0 &lt;= v[i].length &lt;= 500</code></li>
	<li><code>-500 &lt;= v[i][j] &lt;= 500</code></li>
	<li>At most <code>10<sup>5</sup></code> calls will be made to <code>next</code> and <code>hasNext</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> As an added challenge, try only using $O(1)$ additional space beyond the input vector.
"""

    input_format = "First line: Number of operations N. Next N lines: operation names. Next line: Number of rows R for the initial 2D vector. Next R lines: An integer C (row length), followed by C space-separated integers."
    output_format = "An array of results (null, integers, or booleans)."
    
    constraints = [
        "v.length <= 250",
        "v[i].length <= 500",
        "At most 10^5 calls total.",
        "Must handle empty inner lists efficiently."
    ]
    
    explanation = """To implement an efficient 2D iterator:
1. **Pointers**: Maintain two pointers: `row` and `col`.
2. **Advance Strategy**: In `hasNext()`, move the `row` pointer forward whenever `col` reaches the end of the current row, skipping any empty rows until a valid element is found or the end of the 2D vector is reached.
3. **Operations**:
   - `hasNext()`: Returns `true` if `row` is within the vector bounds after skipping empty rows.
   - `next()`: Calls `hasNext()` to ensure pointers are ready, returns `v[row][col]`, and increments `col`.
4. **Complexity**:
   - `next()` / `hasNext()`: Amortized O(1).
   - Space: O(1) additional space (not counting the input)."""
    
    answer = """class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.v = v
        self.row = 0
        self.col = 0

    def next(self) -> int:
        self.hasNext() # Ensure we are on a valid element
        val = self.v[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self) -> bool:
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass Vector2D:\n    def __init__(self, v: list[list[int]]):\n        # User logic here\n        pass\n\n    def next(self) -> int:\n        # User logic here\n        return 0\n\n    def hasNext(self) -> bool:\n        # User logic here\n        return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Find the first array (operations) and the second array (parameters)\n    parts = re.findall(r'\\[.*?\\]', raw_input, re.DOTALL)\n    if len(parts) >= 2:\n        ops = json.loads(parts[0])\n        params = json.loads(parts[1])\n        \n        obj = None\n        res = []\n        for op, param in zip(ops, params):\n            if op == 'Vector2D':\n                obj = Vector2D(param[0])\n                res.append(None)\n            elif op == 'next':\n                res.append(obj.next())\n            elif op == 'hasNext':\n                res.append(obj.hasNext())\n        print(json.dumps(res).replace('None', 'null').replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <sstream>\n\nusing namespace std;\n\nclass Vector2D {\npublic:\n    Vector2D(vector<vector<int>>& v) {\n        // User logic\n    }\n    \n    int next() {\n        // User logic\n        return 0;\n    }\n    \n    bool hasNext() {\n        // User logic\n        return false;\n    }\n};\n\nvector<string> parseOps(string s) {\n    vector<string> res;\n    regex re_word(\"\\\\\"(\\\\w+)\\\\\"\");\n    auto b = sregex_iterator(s.begin(), s.end(), re_word);\n    auto e = sregex_iterator();\n    for (auto i = b; i != e; ++i) res.push_back((*i)[1]);\n    return res;\n}\n\nvector<vector<int>> parse2D(string s) {\n    vector<vector<int>> res;\n    size_t start = s.find(\"[[\");\n    if (start == string::npos) return res;\n    size_t end = s.find(\"]]\", start);\n    string inner = s.substr(start + 1, end - start);\n    // Simple nested bracket parser\n    int depth = 0;\n    string current;\n    for (char c : inner) {\n        if (c == '[') { depth++; current = \"\"; }\n        else if (c == ']') {\n            depth--;\n            vector<int> row;\n            regex re_num(\"-?\\\\d+\");\n            auto b = sregex_iterator(current.begin(), current.end(), re_num);\n            auto e = sregex_iterator();\n            for (auto i = b; i != e; ++i) row.push_back(stoi(i->str()));\n            res.push_back(row);\n        }\n        else current += c;\n    }\n    return res;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    size_t first_bracket = input.find('[');\n    size_t second_bracket = input.find('[', first_bracket + 1);\n    \n    vector<string> ops = parseOps(input.substr(0, second_bracket));\n    vector<vector<int>> v = parse2D(input.substr(second_bracket));\n    \n    Vector2D* obj = nullptr;\n    cout << \"[\";\n    for (size_t i = 0; i < ops.size(); ++i) {\n        if (ops[i] == \"Vector2D\") {\n            obj = new Vector2D(v);\n            cout << \"null\";\n        } else if (ops[i] == \"next\") {\n            cout << obj->next();\n        } else if (ops[i] == \"hasNext\") {\n            cout << (obj->hasNext() ? \"true\" : \"false\");\n        }\n        if (i < ops.size() - 1) cout << \",\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class Vector2D {\n        public Vector2D(int[][] v) {\n            // User logic\n        }\n        \n        public int next() {\n            return 0;\n        }\n        \n        public boolean hasNext() {\n            return false;\n        }\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        // Extract ops\n        List<String> ops = new ArrayList<>();\n        Matcher m_op = Pattern.compile(\"\\\\\"(\\\\w+)\\\\\"\").matcher(input.substring(0, input.indexOf(\"[\", 1)));\n        while (m_op.find()) ops.add(m_op.group(1));\n        \n        // Extract initial 2D vector (simplified logic for lethal parsing)\n        List<List<Integer>> list2D = new ArrayList<>();\n        int start2D = input.indexOf(\"[[\");\n        int end2D = input.indexOf(\"]]\", start2D) + 1;\n        String inner = input.substring(start2D + 1, end2D);\n        Matcher m_row = Pattern.compile(\"\\\\[([^\\\\]]*)\\\\]\").matcher(inner);\n        while (m_row.find()) {\n            List<Integer> row = new ArrayList<>();\n            Matcher m_num = Pattern.compile(\"-?\\\\d+\").matcher(m_row.group(1));\n            while (m_num.find()) row.add(Integer.parseInt(m_num.group()));\n            list2D.add(row);\n        }\n        \n        int[][] v = new int[list2D.size()][];\n        for (int i = 0; i < list2D.size(); i++) {\n            v[i] = new int[list2D.get(i).size()];\n            for (int j = 0; j < v[i].length; j++) v[i][j] = list2D.get(i).get(j);\n        }\n        \n        Vector2D obj = null;\n        System.out.print(\"[\");\n        for (int i = 0; i < ops.size(); i++) {\n            if (ops.get(i).equals(\"Vector2D\")) {\n                obj = new Vector2D(v);\n                System.out.print(\"null\");\n            } else if (ops.get(i).equals(\"next\")) {\n                System.out.print(obj.next());\n            } else if (ops.get(i).equals(\"hasNext\")) {\n                System.out.print(obj.hasNext() ? \"true\" : \"false\");\n            }\n            if (i < ops.size() - 1) System.out.print(\",\");\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass Vector2D {\n    constructor(v) {\n        // User logic\n    }\n    \n    next() {\n        return 0;\n    }\n    \n    hasNext() {\n        return false;\n    }\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst parts = input.match(/\\[.*\\]/s);\nif (parts) {\n    // This is a bit tricky due to nested arrays, but for simplicity:\n    const all = JSON.parse(input.substring(input.indexOf('[')));\n    const ops = all[0]; // Wait, example format says [\"Vector2D\", ...] and [[...], [], ...]\n    // Let's assume input matches the example: two top-level arrays\n    // Using regex to find the two top-level arrays is safer\n    const match = input.match(/\\[.*?\\]/g); // This might fail on nested\n    // Let's just use the full input as a single array of [ops, params] if possible\n    // Or parse manually.\n    try {\n        const full = JSON.parse('[' + input.replace(/\\s+/g, '').replace(/\\],\\[/g, '],[') + ']');\n        // Actually, let's just stick to a simpler approach\n        const raw = input.trim();\n        const ops = JSON.parse(raw.substring(0, raw.indexOf(']') + 1));\n        const params = JSON.parse(raw.substring(raw.indexOf('[', raw.indexOf(']'))));\n        \n        let obj = null;\n        let res = [];\n        for (let i = 0; i < ops.length; i++) {\n            if (ops[i] === 'Vector2D') {\n                obj = new Vector2D(params[i][0]);\n                res.push(null);\n            } else if (ops[i] === 'next') {\n                res.push(obj.next());\n            } else if (ops[i] === 'hasNext') {\n                res.push(obj.hasNext());\n            }\n        }\n        console.log(JSON.stringify(res));\n    } catch(e) {}\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n#include <ctype.h>\n\ntypedef struct {\n    // User logic\n} Vector2D;\n\nVector2D* vectorCreate(int** v, int vSize, int* vColSizes) {\n    Vector2D* obj = (Vector2D*)malloc(sizeof(Vector2D));\n    return obj;\n}\n\nint vectorNext(Vector2D* obj) {\n    return 0;\n}\n\nbool vectorHasNext(Vector2D* obj) {\n    return false;\n}\n\nvoid vectorFree(Vector2D* obj) {\n    free(obj);\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    // Parse operations\n    char ops[100][20];\n    int opCount = 0;\n    char* p = buffer;\n    while (*p && *p != ']') {\n        if (*p == '\"') {\n            char* start = ++p;\n            while (*p && *p != '\"') p++;\n            strncpy(ops[opCount], start, p - start);\n            ops[opCount][p - start] = '\\0';\n            opCount++;\n        }\n        p++;\n    }\n    \n    // Move to params\n    while (*p && *p != '[') p++;\n    p++; // Skip first [\n    \n    int** v = NULL;\n    int vSize = 0;\n    int* vColSizes = NULL;\n    \n    // The first param is the 2D vector [[1,2],[3],[],[4]]\n    if (*p == '[') {\n        v = (int**)malloc(250 * sizeof(int*));\n        vColSizes = (int*)malloc(250 * sizeof(int));\n        p++; // Skip [\n        while (*p && *p != ']') {\n            if (*p == '[') {\n                p++;\n                int row[500];\n                int colCount = 0;\n                while (*p && *p != ']') {\n                    if (isdigit(*p) || *p == '-') {\n                        row[colCount++] = strtol(p, &p, 10);\n                    } else p++;\n                }\n                vColSizes[vSize] = colCount;\n                v[vSize] = (int*)malloc(colCount * sizeof(int));\n                for (int i = 0; i < colCount; i++) v[vSize][i] = row[i];\n                vSize++;\n            }\n            p++;\n        }\n    }\n    \n    Vector2D* obj = NULL;\n    printf(\"[\");\n    for (int i = 0; i < opCount; i++) {\n        if (strcmp(ops[i], \"Vector2D\") == 0) {\n            obj = vectorCreate(v, vSize, vColSizes);\n            printf(\"null\");\n        } else if (strcmp(ops[i], \"next\") == 0) {\n            printf(\"%d\", vectorNext(obj));\n        } else if (strcmp(ops[i], \"hasNext\") == 0) {\n            printf(\"%s\", vectorHasNext(obj) ? \"true\" : \"false\");\n        }\n        if (i < opCount - 1) printf(\",\");\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }\n    \n    int next() {\n        return 0;\n    }\n    \n    bool hasNext() {\n        return false;\n    }\n};\n\nint main() {\n    int n;\n    if (!(cin >> n)) return 0;\n    vector<string> ops(n);\n    for (int i = 0; i < n; i++) cin >> ops[i];\n    \n    int r;\n    cin >> r;\n    vector<vector<int>> v(r);\n    for (int i = 0; i < r; i++) {\n        int c;\n        cin >> c;\n        v[i].resize(c);\n        for (int j = 0; j < c; j++) cin >> v[i][j];\n    }\n    \n    Vector2D* obj = nullptr;\n    cout << \"[\";\n    for (int i = 0; i < n; i++) {\n        if (ops[i] == \"Vector2D\") {\n            obj = new Vector2D(v);\n            cout << \"null\";\n        } else if (ops[i] == \"next\") {\n            cout << obj->next();\n        } else if (ops[i] == \"hasNext\") {\n            cout << (obj->hasNext() ? \"true\" : \"false\");\n        }\n        if (i < n - 1) cout << \",\";\n    }\n    cout << \"]\\n\";\n    delete obj;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    static class Vector2D {\n        public Vector2D(int[][] v) {\n            // User logic\n        }\n        \n        public int next() {\n            return 0;\n        }\n        \n        public boolean hasNext() {\n            return false;\n        }\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int n = sc.nextInt();\n        String[] ops = new String[n];\n        for (int i = 0; i < n; i++) ops[i] = sc.next();\n        \n        int r = sc.nextInt();\n        int[][] v = new int[r][];\n        for (int i = 0; i < r; i++) {\n            int c = sc.nextInt();\n            v[i] = new int[c];\n            for (int j = 0; j < c; j++) v[i][j] = sc.nextInt();\n        }\n        \n        Vector2D obj = null;\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < n; i++) {\n            if (ops[i].equals(\"Vector2D\")) {\n                obj = new Vector2D(v);\n                sb.append(\"null\");\n            } else if (ops[i].equals(\"next\")) {\n                sb.append(obj.next());\n            } else if (ops[i].equals(\"hasNext\")) {\n                sb.append(obj.hasNext() ? \"true\" : \"false\");\n            }\n            if (i < n - 1) sb.append(\",\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass Vector2D {\n    constructor(v) {\n        // User logic\n    }\n    \n    next() {\n        return 0;\n    }\n    \n    hasNext() {\n        return false;\n    }\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let ptr = 0;\n    let n = parseInt(input[ptr++]);\n    let ops = [];\n    for (let i = 0; i < n; i++) ops.push(input[ptr++]);\n    \n    let r = parseInt(input[ptr++]);\n    let v = [];\n    for (let i = 0; i < r; i++) {\n        let c = parseInt(input[ptr++]);\n        let row = [];\n        for (let j = 0; j < c; j++) row.push(parseInt(input[ptr++]));\n        v.push(row);\n    }\n    \n    let obj = null;\n    let res = [];\n    for (let op of ops) {\n        if (op === 'Vector2D') {\n            obj = new Vector2D(v);\n            res.push(null);\n        } else if (op === 'next') {\n            res.push(obj.next());\n        } else if (op === 'hasNext') {\n            res.push(obj.hasNext());\n        }\n    }\n    console.log(JSON.stringify(res));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\ntypedef struct {\n    // User logic\n} Vector2D;\n\nVector2D* vectorCreate(int** v, int vSize, int* vColSizes) {\n    Vector2D* obj = (Vector2D*)malloc(sizeof(Vector2D));\n    return obj;\n}\n\nint vectorNext(Vector2D* obj) {\n    return 0;\n}\n\nbool vectorHasNext(Vector2D* obj) {\n    return false;\n}\n\nvoid vectorFree(Vector2D* obj) {\n    free(obj);\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) != 1) return 0;\n    char** ops = (char**)malloc(n * sizeof(char*));\n    for (int i = 0; i < n; i++) {\n        ops[i] = (char*)malloc(20 * sizeof(char));\n        scanf(\"%s\", ops[i]);\n    }\n    \n    int r;\n    scanf(\"%d\", &r);\n    int** v = (int**)malloc(r * sizeof(int*));\n    int* vColSizes = (int*)malloc(r * sizeof(int));\n    for (int i = 0; i < r; i++) {\n        scanf(\"%d\", &vColSizes[i]);\n        if (vColSizes[i] > 0) {\n            v[i] = (int*)malloc(vColSizes[i] * sizeof(int));\n            for (int j = 0; j < vColSizes[i]; j++) scanf(\"%d\", &v[i][j]);\n        } else {\n            v[i] = NULL;\n        }\n    }\n    \n    Vector2D* obj = NULL;\n    printf(\"[\");\n    for (int i = 0; i < n; i++) {\n        if (strcmp(ops[i], \"Vector2D\") == 0) {\n            obj = vectorCreate(v, r, vColSizes);\n            printf(\"null\");\n        } else if (strcmp(ops[i], \"next\") == 0) {\n            printf(\"%d\", vectorNext(obj));\n        } else if (strcmp(ops[i], \"hasNext\") == 0) {\n            printf(\"%s\", vectorHasNext(obj) ? \"true\" : \"false\");\n        }\n        if (i < n - 1) printf(\",\");\n    }\n    printf(\"]\\n\");\n    \n    if (obj) vectorFree(obj);\n    for (int i = 0; i < n; i++) free(ops[i]);\n    free(ops);\n    for (int i = 0; i < r; i++) free(v[i]);\n    free(v);\n    free(vColSizes);\n    \n    return 0;\n}"
    }

    def create_tc(ops, v):
        res = []
        res.append(str(len(ops)))
        res.extend(ops)
        res.append(str(len(v)))
        for row in v:
            res.append(str(len(row)))
            res.extend(map(str, row))
        return " ".join(res)

    def _solve_v2d(ops, v):
        row, col = 0, 0
        def hasNext():
            nonlocal row, col
            while row < len(v):
                if col < len(v[row]): return True
                row += 1; col = 0
            return False
        def next():
            hasNext()
            nonlocal col
            val = v[row][col]
            col += 1
            return val
        res = [None]
        for op in ops[1:]:
            if op == 'next': res.append(next())
            elif op == 'hasNext': res.append(hasNext())
        return res

    test_cases = [
        {"input": create_tc(["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"], [[1, 2], [3], [], [4]]), "expected_output": "[null,1,2,3,true,true,4,false]", "is_sample": True},
        {"input": create_tc(["Vector2D", "hasNext"], [[]]), "expected_output": "[null,false]", "is_sample": True},
        {"input": create_tc(["Vector2D", "hasNext"], [[], [], []]), "expected_output": "[null,false]", "is_sample": False},
        {"input": create_tc(["Vector2D", "next", "next"], [[1], [2]]), "expected_output": "[null,1,2]", "is_sample": False},
        {"input": create_tc(["Vector2D", "next", "hasNext"], [[1]]), "expected_output": "[null,1,false]", "is_sample": False},
        {"input": create_tc(["Vector2D", "hasNext", "next"], [[0]]), "expected_output": "[null,true,0]", "is_sample": False},
    ]

    # Stress 6: 250 rows of 400 elements
    v6 = [list(range(400)) for _ in range(250)]
    ops6 = ["Vector2D"] + ["next"] * 10
    test_cases.append({"input": create_tc(ops6, v6), "expected_output": json.dumps(_solve_v2d(ops6, v6)).replace(' ', ''), "is_sample": False})
    
    # Stress 7: Lots of empty rows
    v7 = [[]] * 200 + [[1]] + [[]] * 49
    ops7 = ["Vector2D", "hasNext", "next", "hasNext"]
    test_cases.append({"input": create_tc(ops7, v7), "expected_output": json.dumps(_solve_v2d(ops7, v7)).replace(' ', '').replace('True', 'true').replace('False', 'false'), "is_sample": False})
    
    # Stress 8: Mixed
    v8 = [[1], [], [2], [3, 4], [], [], [5]]
    ops8 = ["Vector2D", "next", "hasNext", "next", "next", "next", "hasNext", "next", "hasNext"]
    test_cases.append({"input": create_tc(ops8, v8), "expected_output": json.dumps(_solve_v2d(ops8, v8)).replace(' ', '').replace('True', 'true').replace('False', 'false'), "is_sample": False})
    
    v9 = [[], [1, 2], [], [3], []]
    ops9 = ["Vector2D", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    test_cases.append({"input": create_tc(ops9, v9), "expected_output": json.dumps(_solve_v2d(ops9, v9)).replace(' ', '').replace('True', 'true').replace('False', 'false'), "is_sample": False})

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
        "topics": ["Design", "Array", "Two Pointers", "Iterator"],
        "companyIndex": 0
    }

    output_path = "201-400/251_Flatten_2D_Vector.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
