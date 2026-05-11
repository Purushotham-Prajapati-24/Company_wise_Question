import json
import os

def generate_json():
    problem_id = 323
    title = "Number of Connected Components in an Undirected Graph"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>323. Number of Connected Components in an Undirected Graph</h3>
<p>You have a graph of <code>n</code> nodes. You are given an integer <code>n</code> and an array <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the graph.</p>

<p>Return <em>the number of connected components in the graph</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg" style="width: 222px; height: 222px;" />
<pre><strong>Input:</strong> n = 5, edges = [[0,1],[1,2],[3,4]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg" style="width: 222px; height: 222px;" />
<pre><strong>Input:</strong> n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= edges.length &lt;= 5000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub> &lt; b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
</ul>"""

    input_format = "Two lines. Line 1: an integer `n`. Line 2: a 2D array of integers `edges`."
    output_format = "An integer representing the count of connected components."
    
    constraints = [
        "1 <= n <= 2000",
        "1 <= edges.length <= 5000",
        "0 <= ai < bi < n"
    ]
    
    explanation = """To count the number of connected components in an undirected graph, we can use Union-Find or Depth-First Search (DFS).

### Union-Find Approach:
1. **Disjoint Set Union (DSU)**:
   - Initialize a parent array where each node is its own parent.
   - For each edge `(u, v)` in `edges`, perform a `union(u, v)`.
   - If two nodes are unioned that were not already in the same component, we reduce the total count of components (initially `n`).
2. **Operations**:
   - `find(idx)`: Returns the representative (root) of the component containing `idx` with path compression.
   - `union(u, v)`: Merges the components containing `u` and `v` using union by rank (to keep the tree flat).
3. **Complexity Analysis**:
   - **Time Complexity**: $O(V + E \alpha(V))$, where $V$ is the number of nodes, $E$ is the number of edges, and $\alpha$ is the inverse Ackermann function (nearly $O(1)$).
   - **Space Complexity**: $O(V)$ to store the parent and rank arrays."""
    
    answer = """class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n
        components = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            nonlocal components
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                elif rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                components -= 1
                return True
            return False
            
        for u, v in edges:
            union(u, v)
        return components"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef countComponents(n: int, edges: list[list[int]]) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    n_match = re.search(r'(?:n\\s*=\\s*)?(\\d+)', raw_input)\n    n = int(n_match.group(1)) if n_match else 0\n    edges_match = re.search(r'\\[\\s*\\[.*\\]\\s*\\]', raw_input, re.DOTALL)\n    edges = json.loads(edges_match.group(0)) if edges_match else []\n    print(countComponents(n, edges))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\nusing namespace std;\n\nint countComponents(int n, vector<vector<int>>& edges) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    \n    regex re_n(\"(?:n\\\\s*=\\\\s*)?(\\\\d+)\");\n    smatch m_n;\n    int n = 0;\n    if (regex_search(input, m_n, re_n)) n = stoi(m_n[1]);\n    \n    regex re_edges(\"\\\\[\\\\s*\\\\[.*\\\\]\\\\s*\\\\]\");\n    smatch m_edges;\n    vector<vector<int>> edges;\n    if (regex_search(input, m_edges, re_edges)) {\n        string edges_str = m_edges.str();\n        regex re_pair(\"\\\\[\\\\s*(\\\\d+)\\\\s*,\\\\s*(\\\\d+)\\\\s*\\\\]\");\n        auto it = sregex_iterator(edges_str.begin(), edges_str.end(), re_pair);\n        for (; it != sregex_iterator(); ++it) {\n            edges.push_back({stoi((*it)[1]), stoi((*it)[2])});\n        }\n    }\n    cout << countComponents(n, edges) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int countComponents(int n, int[][] edges) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while(sc.hasNext()) sb.append(sc.next()).append(\" \");\n        String input = sb.toString();\n        \n        Matcher mN = Pattern.compile(\"(?:n\\\\s*=\\\\s*)?(\\\\d+)\").matcher(input);\n        int n = mN.find() ? Integer.parseInt(mN.group(1)) : 0;\n        \n        Matcher mEdges = Pattern.compile(\"\\\\[\\\\s*\\\\[.*\\\\]\\\\s*\\\\]\").matcher(input);\n        List<int[]> edgesList = new ArrayList<>();\n        if (mEdges.find()) {\n            Matcher mPair = Pattern.compile(\"\\\\[\\\\s*(\\\\d+)\\\\s*,\\\\s*(\\\\d+)\\\\s*\\\\]\").matcher(mEdges.group());\n            while(mPair.find()) {\n                edgesList.add(new int[]{Integer.parseInt(mPair.group(1)), Integer.parseInt(mPair.group(2))});\n            }\n        }\n        System.out.println(new Solution().countComponents(n, edgesList.toArray(new int[0][])));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction countComponents(n, edges) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst nMatch = input.match(/(?:n\\s*=\\s*)?(\\d+)/);\nconst n = nMatch ? parseInt(nMatch[1]) : 0;\nconst edgesMatch = input.match(/\\[\\s*\\[.*\\]\\s*\\]/s);\nconst edges = edgesMatch ? JSON.parse(edgesMatch[0]) : [];\nconsole.log(countComponents(n, edges));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint countComponents(int n, int** edges, int edgesSize, int* edgesColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int n, m;\n    if (scanf(\"%d %d\", &n, &m) != 2) return 0;\n    int** edges = malloc(sizeof(int*) * m);\n    int* colSize = malloc(sizeof(int) * m);\n    for(int i=0; i<m; i++) {\n        edges[i] = malloc(sizeof(int) * 2);\n        scanf(\"%d %d\", &edges[i][0], &edges[i][1]);\n        colSize[i] = 2;\n    }\n    printf(\"%d\\n\", countComponents(n, edges, m, colSize));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5\\n[[0,1],[1,2],[3,4]]", "expected_output": "2", "is_sample": True},
        {"input": "5\\n[[0,1],[1,2],[2,3],[3,4]]", "expected_output": "1", "is_sample": True},
        {"input": "2\\n[[0,1]]", "expected_output": "1", "is_sample": False},
        {"input": "3\\n[]", "expected_output": "3", "is_sample": False},
        {"input": "4\\n[[0,1],[2,3]]", "expected_output": "2", "is_sample": False},
        {"input": "10\\n[[0,1],[1,2],[2,3],[4,5],[5,6],[7,8]]", "expected_output": "4", "is_sample": False},
        {"input": "5\\n[[0,1],[0,2],[0,3],[0,4]]", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": "2000\\n[]", "expected_output": "2000", "is_sample": False},
        {"input": "2000\\n" + json.dumps([[i, i+1] for i in range(1999)]), "expected_output": "1", "is_sample": False},
        {"input": "2000\\n" + json.dumps([[2*i, 2*i+1] for i in range(1000)]), "expected_output": "1000", "is_sample": False}
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
        "topics": ["Union Find", "Graph", "DFS", "BFS"],
        "companyIndex": 1
    }

    output_path = "301-500/323_Number_of_Connected_Components_in_an_Undirected_Graph.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
