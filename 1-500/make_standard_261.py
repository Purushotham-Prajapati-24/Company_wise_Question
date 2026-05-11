import json
import os

def generate_json():
    problem_id = 261
    title = "Graph Valid Tree"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>261. Graph Valid Tree</h3>
<p>You have a graph of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given an integer <code>n</code> and a list of <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an undirected edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the graph.</p>

<p>Return <code>true</code> <em>if the edges of the given graph make up a valid tree, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg" style="width: 222px; height: 302px;" />
<pre><strong>Input:</strong> n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg" style="width: 382px; height: 222px;" />
<pre><strong>Input:</strong> n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>0 &lt;= edges.length &lt;= 5000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no self-loops or repeated edges.</li>
</ul>"""

    input_format = "First line: Two space-separated integers N and E. Next E lines: space-separated integers u v, denoting an edge."
    output_format = "A boolean (true/false)."
    
    constraints = [
        "1 <= n <= 2000",
        "0 <= edges.length <= 5000",
        "A valid tree must be connected and acyclic (|E| = n-1)."
    ]
    
    explanation = """To check if a graph is a valid tree:
1. **The Tree Condition**: A graph is a tree if and only if:
   - It is connected.
   - It contains no cycles.
   - For $n$ nodes, it must have exactly $n - 1$ edges.
2. **Algorithm**:
   - First, check if `len(edges) == n - 1`. If not, return `false`.
   - Then, check if the graph is connected using BFS, DFS, or Union-Find.
   - For connectivity, perform a traversal starting from node 0 and count how many unique nodes were visited.
   - If count equals $n$, the graph is connected (and since $|E| = n-1$, it must be acyclic).
3. **Complexity**:
   - Time: O(N + E).
   - Space: O(N + E) for adjacency list."""
    
    answer = """class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
                
        dfs(0)
        return len(visited) == n"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef validTree(n: int, edges: list[list[int]]) -> bool:\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Extract n\n    n_match = re.search(r'n\\s*=\\s*(\\d+)', raw_input)\n    if n_match:\n        n = int(n_match.group(1))\n    else:\n        nums = re.findall(r'\\d+', raw_input)\n        n = int(nums[0]) if nums else 0\n    \n    # Extract edges\n    edges = []\n    # Find all pairs in brackets [u, v]\n    matches = re.findall(r'\\[\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\]', raw_input)\n    for m in matches:\n        edges.append([int(m[0]), int(m[1])])\n        \n    print(\"true\" if validTree(n, edges) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nbool validTree(int n, vector<vector<int>>& edges) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    int n = 0;\n    smatch m;\n    if (regex_search(input, m, regex(\"n\\\\s*=\\\\s*(\\\\d+)\"))) {\n        n = stoi(m[1].str());\n    } else {\n        regex re_num(\"\\\\d+\");\n        auto it = sregex_iterator(input.begin(), input.end(), re_num);\n        if (it != sregex_iterator()) n = stoi(it->str());\n    }\n    \n    vector<vector<int>> edges;\n    regex re_edge(\"\\\\[\\\\s*(\\\\d+)\\\\s*,\\\\s*(\\\\d+)\\\\s*\\\\]\");\n    auto b = sregex_iterator(input.begin(), input.end(), re_edge);\n    auto e = sregex_iterator();\n    for (auto i = b; i != e; ++i) {\n        edges.push_back({stoi((*i)[1]), stoi((*i)[2])});\n    }\n    \n    cout << (validTree(n, edges) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public boolean validTree(int n, int[][] edges) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        int n = 0;\n        Matcher mn = Pattern.compile(\"n\\\\s*=\\\\s*(\\\\d+)\").matcher(input);\n        if (mn.find()) {\n            n = Integer.parseInt(mn.group(1));\n        } else {\n            Matcher mNum = Pattern.compile(\"\\\\d+\").matcher(input);\n            if (mNum.find()) n = Integer.parseInt(mNum.group());\n        }\n        \n        List<int[]> edgeList = new ArrayList<>();\n        Matcher me = Pattern.compile(\"\\\\[\\\\s*(\\\\d+)\\\\s*,\\\\s*(\\\\d+)\\\\s*\\\\]\").matcher(input);\n        while (me.find()) {\n            edgeList.add(new int[]{Integer.parseInt(me.group(1)), Integer.parseInt(me.group(2))});\n        }\n        \n        int[][] edges = edgeList.toArray(new int[0][]);\n        System.out.println(new Solution().validTree(n, edges) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction validTree(n, edges) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nlet n = 0;\nconst nMatch = input.match(/n\\s*=\\s*(\\d+)/);\nif (nMatch) {\n    n = parseInt(nMatch[1]);\n} else {\n    const nums = input.match(/\\d+/g);\n    if (nums) n = parseInt(nums[0]);\n}\n\nconst edges = [];\nconst edgeMatches = input.matchAll(/\\[\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\]/g);\nfor (const m of edgeMatches) {\n    edges.push([parseInt(m[1]), parseInt(m[2])]);\n}\n\nconsole.log(validTree(n, edges) ? \"true\" : \"false\");",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n#include <ctype.h>\n\nbool validTree(int n, int** edges, int edgesSize, int* edgesColSize) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    int n = 0;\n    char* nLabel = strstr(buffer, \"n\");\n    if (nLabel) {\n        char* p = nLabel;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) n = strtol(p, NULL, 10);\n    } else {\n        char* p = buffer;\n        while (*p && !isdigit(*p)) p++;\n        if (*p) n = strtol(p, NULL, 10);\n    }\n    \n    int** edges = (int**)malloc(6000 * sizeof(int*));\n    int* cols = (int*)malloc(6000 * sizeof(int));\n    int count = 0;\n    \n    char* p = buffer;\n    while (*p) {\n        if (*p == '[') {\n            p++;\n            while (*p && isspace(*p)) p++;\n            if (isdigit(*p)) {\n                edges[count] = (int*)malloc(2 * sizeof(int));\n                edges[count][0] = strtol(p, &p, 10);\n                while (*p && !isdigit(*p)) p++;\n                if (*p) {\n                    edges[count][1] = strtol(p, &p, 10);\n                    cols[count] = 2;\n                    count++;\n                }\n            }\n        } else p++;\n    }\n    \n    printf(\"%s\\n\", validTree(n, edges, count, cols) ? \"true\" : \"false\");\n    return 0;\n}"
    }

    def create_tc(n, edges):
        res = [f"{n} {len(edges)}"]
        for u, v in edges:
            res.append(f"{u} {v}")
        return "\\n".join(res)

    test_cases = [
        {"input": create_tc(5, [[0,1],[0,2],[0,3],[1,4]]), "expected_output": "true", "is_sample": True},
        {"input": create_tc(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]), "expected_output": "false", "is_sample": True},
        {"input": create_tc(1, []), "expected_output": "true", "is_sample": False},
        {"input": create_tc(2, []), "expected_output": "false", "is_sample": False},
        {"input": create_tc(4, [[0,1],[2,3]]), "expected_output": "false", "is_sample": False},
        {"input": create_tc(3, [[0,1],[0,2],[1,2]]), "expected_output": "false", "is_sample": False},
        {"input": create_tc(4, [[0,1],[1,2],[2,3]]), "expected_output": "true", "is_sample": False},
    ]
    
    def _solve_vt(n, edges):
        if len(edges) != n - 1: return False
        adj = [[] for _ in range(n)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        vst = {0}
        q = [0]
        while q:
            curr = q.pop()
            for nb in adj[curr]:
                if nb not in vst: vst.add(nb); q.append(nb)
        return len(vst) == n if n > 0 else True

    # Stress 8: 2000 nodes, star graph
    e8 = [[0, i] for i in range(1, 2000)]
    test_cases.append({"input": create_tc(2000, e8), "expected_output": "true", "is_sample": False})
    # Stress 9: 2000 nodes, line graph
    e9 = [[i, i+1] for i in range(1999)]
    test_cases.append({"input": create_tc(2000, e9), "expected_output": "true", "is_sample": False})
    # Stress 10: 2000 nodes, cycle of 1999 + 1 isolated
    e10 = [[i, (i+1)%1999] for i in range(1999)]
    test_cases.append({"input": create_tc(2000, e10), "expected_output": "false", "is_sample": False})

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
        "topics": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
        "companyIndex": 0
    }

    output_path = "201-400/261_Graph_Valid_Tree.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
