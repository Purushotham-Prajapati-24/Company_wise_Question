import json
import os

def generate_json():
    problem_id = 305
    title = "Number of Islands II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>305. Number of Islands II</h3>
<p>You are given an empty 2D binary grid <code>grid</code> of size <code>m x n</code>. The grid represents a map where <code>0</code> is water and <code>1</code> is land. Initially, all cells are water.</p>

<p>We may perform an <code>addLand</code> operation which turns the water at <code>(row, col)</code> into a land. You are given an array <code>positions</code> where <code>positions[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> is the position of the <code>i</code><sup>th</sup> operation.</p>

<p>Return <em>an array of integers</em> <code>answer</code> <em>where</em> <code>answer[i]</code> <em>is the number of islands after the </em><code>i</code><sup>th</sup><em> operation.</em></p>

<p>An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
<strong>Output:</strong> [1,1,2,3]
<strong>Explanation:</strong>
Operation #1: addLand(0, 0) turns the water at (0, 0) into a land. [1]
Operation #2: addLand(0, 1) turns the water at (0, 1) into a land. [1]
Operation #3: addLand(1, 2) turns the water at (1, 2) into a land. [1, 2]
Operation #4: addLand(2, 1) turns the water at (2, 1) into a land. [1, 2, 3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> m = 1, n = 1, positions = [[0,0]]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= m, n, positions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>positions[i].length == 2</code></li>
	<li><code>0 &lt;= r<sub>i</sub> &lt; m</code></li>
	<li><code>0 &lt;= c<sub>i</sub> &lt; n</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you solve it in <code>O(k log(mn))</code>, where <code>k</code> is the length of <code>positions</code>?"""

    input_format = "Integers `m`, `n`, and a 2D array `positions`."
    output_format = "A list of integers representing the island counts after each operation."
    
    constraints = [
        "1 <= m, n <= 10,000",
        "1 <= m * n <= 10,000",
        "1 <= positions.length <= 10,000",
        "O(K log(MN)) time complexity is expected."
    ]
    
    explanation = """To track the number of islands dynamically:
1. **Union-Find (DSU)**: This structure is perfect for merging disjoint sets efficiently.
2. **Setup**:
   - `parent` array of size `m * n` initialized with -1 (indicating water).
   - `count` to track current number of islands.
3. **Execution for each `(r, c)`**:
   - Convert 2D coordinates to 1D: `idx = r * n + c`.
   - If the cell is already land (handles duplicate positions), append current `count`.
   - Mark the cell as land (`parent[idx] = idx`) and increment `count`.
   - Check 4 neighbors. For each neighbor that is land:
     - Use `find()` to check if they belong to different components.
     - If different, `union()` them and decrement `count`.
4. **Optimizations**:
   - **Path Compression** in `find()` to flatten the tree.
   - **Union by Rank** to keep the tree balanced.
5. **Complexity Analysis**:
   - Time: O(K * α(N)) where K is the number of positions and α is the inverse Ackermann function (nearly constant).
   - Space: O(M * N) for the DSU parent array."""
    
    answer = """class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.count = 0

    def add(self, i):
        if self.parent[i] == -1:
            self.parent[i] = i
            self.count += 1
            return True
        return False

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        res = []
        for r, c in positions:
            idx = r * n + c
            if uf.add(idx):
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        n_idx = nr * n + nc
                        if uf.parent[n_idx] != -1:
                            uf.union(idx, n_idx)
            res.append(uf.count)
        return res"""
    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef numIslands2(m, n, positions):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    # Lethal extraction for m, n, positions\n    m_val = re.search(r'm\\s*=\\s*(\\d+)', raw_input)\n    n_val = re.search(r'n\\s*=\\s*(\\d+)', raw_input)\n    pos_match = re.search(r'positions\\s*=\\s*(\\[.*\\])', raw_input, re.DOTALL)\n    \n    m = int(m_val.group(1)) if m_val else int(re.findall(r'\\d+', raw_input)[0])\n    n = int(n_val.group(1)) if n_val else int(re.findall(r'\\d+', raw_input)[1])\n    \n    if pos_match: \n        positions = json.loads(pos_match.group(1))\n    else:\n        # fallback: find the first occurrence of a nested list [[...]]\n        arr_match = re.search(r'\\[\\s*\\[.*\\]\\s*\\]', raw_input, re.DOTALL)\n        positions = json.loads(arr_match.group(0)) if arr_match else []\n        \n    result = numIslands2(m, n, positions)\n    print(json.dumps(result))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nvector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line;\n    \n    int m_val = 0, n_val = 0;\n    regex m_re(\"m\\\\s*=\\\\s*(\\\\d+)\"), n_re(\"n\\\\s*=\\\\s*(\\\\d+)\");\n    smatch match;\n    if (regex_search(input, match, m_re)) m_val = stoi(match[1]);\n    if (regex_search(input, match, n_re)) n_val = stoi(match[1]);\n    \n    regex pos_re(\"\\\\[\\\\s*\\\\[.*\\\\]\\\\s*\\\\]\");\n    vector<vector<int>> positions;\n    if (regex_search(input, match, pos_re)) {\n        string s = match[0];\n        regex pair_re(\"\\\\[(\\\\d+)\\\\s*,\\\\s*(\\\\d+)\\\\]\");\n        auto it = sregex_iterator(s.begin(), s.end(), pair_re);\n        auto end = sregex_iterator();\n        for (; it != end; ++it) {\n            positions.push_back({stoi((*it)[1]), stoi((*it)[2])});\n        }\n    }\n    \n    vector<int> res = numIslands2(m_val, n_val, positions);\n    cout << \"[\";\n    for (int j = 0; j < (int)res.size(); j++) {\n        if (j) cout << \",\";\n        cout << res[j];\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public List<Integer> numIslands2(int m, int n, int[][] positions) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb_in = new StringBuilder();\n        while(sc.hasNextLine()) sb_in.append(sc.nextLine());\n        String input = sb_in.toString();\n        \n        int m_val = 0, n_val = 0;\n        Matcher mm = Pattern.compile(\"m\\\\s*=\\\\s*(\\\\d+)\").matcher(input);\n        if (mm.find()) m_val = Integer.parseInt(mm.group(1));\n        Matcher nm = Pattern.compile(\"n\\\\s*=\\\\s*(\\\\d+)\").matcher(input);\n        if (nm.find()) n_val = Integer.parseInt(nm.group(1));\n        \n        List<int[]> posList = new ArrayList<>();\n        Matcher pm = Pattern.compile(\"\\\\[\\\\s*(\\\\d+)\\\\s*,\\\\s*(\\\\d+)\\\\s*\\\\]\").matcher(input);\n        while (pm.find()) {\n            posList.add(new int[]{Integer.parseInt(pm.group(1)), Integer.parseInt(pm.group(2))});\n        }\n        \n        int[][] positions = posList.toArray(new int[0][]);\n        List<Integer> res = new Solution().numIslands2(m_val, n_val, positions);\n        System.out.println(res.toString().replace(\" \", \"\"));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction numIslands2(m, n, positions) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst mMatch = input.match(/m\\s*=\\s*(\\d+)/);\nconst nMatch = input.match(/n\\s*=\\s*(\\d+)/);\nconst posMatch = input.match(/positions\\s*=\\s*(\\[.*\\])/s) || input.match(/\\[\\s*\\[.*\\]\\s*\\]/s);\n\nconst m = mMatch ? parseInt(mMatch[1]) : parseInt(input.split(/[^0-9]+/)[0]);\nconst n = nMatch ? parseInt(nMatch[1]) : parseInt(input.split(/[^0-9]+/)[1]);\nconst positions = posMatch ? JSON.parse(posMatch[1] || posMatch[0]) : [];\n\nconsole.log(JSON.stringify(numIslands2(m, n, positions)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint* numIslands2(int m, int n, int** positions, int positionsSize, int* returnSize) {\n    // User logic here\n    *returnSize = positionsSize;\n    return (int*)calloc(positionsSize, sizeof(int));\n}\n\nint main() {\n    char buf[65536];\n    int len = 0, c;\n    while ((c = getchar()) != EOF && len < 65535) buf[len++] = c;\n    buf[len] = '\\0';\n\n    int m = 0, n = 0;\n    char *pm = strstr(buf, \"m\"); if(pm) while(*pm && !isdigit(*pm)) pm++; if(pm) m = atoi(pm);\n    char *pn = strstr(buf, \"n\"); if(pn) while(*pn && !isdigit(*pn)) pn++; if(pn) n = atoi(pn);\n\n    int* rs = malloc(10005 * sizeof(int));\n    int* cs = malloc(10005 * sizeof(int));\n    int sz = 0;\n    char *p = strstr(buf, \"[[\");\n    if (p) {\n        while (*p && sz < 10000) {\n            if (*p == '[') {\n                p++; while(*p && !isdigit(*p) && *p != '-') p++;\n                if (isdigit(*p) || *p == '-') {\n                    rs[sz] = strtol(p, &p, 10);\n                    while(*p && !isdigit(*p) && *p != '-') p++;\n                    cs[sz] = strtol(p, &p, 10);\n                    sz++;\n                }\n            } else p++;\n        }\n    }\n\n    int** ptrs = malloc(sz * sizeof(int*));\n    for (int i = 0; i < sz; i++) {\n        ptrs[i] = malloc(2 * sizeof(int));\n        ptrs[i][0] = rs[i]; ptrs[i][1] = cs[i];\n    }\n    int returnSize = 0;\n    int* res = numIslands2(m, n, ptrs, sz, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        if (i) printf(\",\");\n        printf(\"%d\", res[i]);\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    } 

    test_cases = [
        {"input": "3\n3\n[[0,0],[0,1],[1,2],[2,1]]", "expected_output": "[1,1,2,3]", "is_sample": True},
        {"input": "1\n1\n[[0,0]]", "expected_output": "[1]", "is_sample": True},
        {"input": "3\n3\n[[0,0],[0,0]]", "expected_output": "[1,1]", "is_sample": False},
        {"input": "2\n2\n[[0,0],[1,1],[0,1]]", "expected_output": "[1,2,1]", "is_sample": False},
        {"input": "3\n3\n[[0,0],[1,1],[2,2]]", "expected_output": "[1,2,3]", "is_sample": False},
        {"input": "3\n3\n[[0,0],[0,2],[2,0],[2,2],[1,1]]", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "3\n3\n[[1,1],[0,1],[1,0],[1,2],[2,1]]", "expected_output": "[1,1,1,1,1]", "is_sample": False},
        {"input": "4\n4\n[[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0]]", "expected_output": "[1,1,1,1,1,1,1,1,1,1]", "is_sample": False},
        {"input": "2\n3\n[[0,0],[0,2],[1,1],[0,1],[1,0],[1,2]]", "expected_output": "[1,2,3,2,2,1]", "is_sample": False},
        {"input": "5\n5\n[[0,0],[4,4],[0,4],[4,0],[2,2]]", "expected_output": "[1,2,3,4,5]", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Union Find"],
        "companyIndex": 0
    }

    output_path = "201-400/305_Number_of_Islands_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
