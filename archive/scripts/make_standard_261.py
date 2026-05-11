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
        "python": "import sys\n\ndef validTree(n: int, edges: list[list[int]]) -> bool:\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data: sys.exit()\n    n = int(data[0])\n    e = int(data[1])\n    edges = []\n    idx = 2\n    for _ in range(e):\n        edges.append([int(data[idx]), int(data[idx+1])])\n        idx += 2\n    print(\"true\" if validTree(n, edges) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nbool validTree(int n, vector<vector<int>>& edges) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int n, e;\n    if (cin >> n >> e) {\n        vector<vector<int>> edges(e, vector<int>(2));\n        for (int i = 0; i < e; i++) {\n            cin >> edges[i][0] >> edges[i][1];\n        }\n        cout << (validTree(n, edges) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean validTree(int n, int[][] edges) {\n        // User logic\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            int e = sc.nextInt();\n            int[][] edges = new int[e][2];\n            for (int i = 0; i < e; i++) {\n                edges[i][0] = sc.nextInt();\n                edges[i][1] = sc.nextInt();\n            }\n            System.out.println(new Solution().validTree(n, edges) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction validTree(n, edges) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let n = parseInt(input[0]);\n    let e = parseInt(input[1]);\n    let edges = [];\n    let idx = 2;\n    for (let i = 0; i < e; i++) {\n        edges.push([parseInt(input[idx++]), parseInt(input[idx++])]);\n    }\n    console.log(validTree(n, edges) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nbool validTree(int n, int** edges, int edgesSize, int* edgesColSize) {\n    // User logic\n    return false;\n}\n\nint main() {\n    int n, e;\n    if (scanf(\"%d %d\", &n, &e) == 2) {\n        int** edges = (int**)malloc((e > 0 ? e : 1) * sizeof(int*));\n        int* cols = (int*)malloc((e > 0 ? e : 1) * sizeof(int));\n        for (int i = 0; i < e; i++) {\n            edges[i] = (int*)malloc(2 * sizeof(int));\n            scanf(\"%d %d\", &edges[i][0], &edges[i][1]);\n            cols[i] = 2;\n        }\n        printf(\"%s\\n\", validTree(n, edges, e, cols) ? \"true\" : \"false\");\n        for (int i = 0; i < e; i++) free(edges[i]);\n        free(edges);\n        free(cols);\n    }\n    return 0;\n}"
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
