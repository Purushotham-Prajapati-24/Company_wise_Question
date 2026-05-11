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
        "python": "import sys\nimport json\n\nclass Solution:\n    def countComponents(self, n: int, edges: list[list[int]]) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        lines = raw_input.split('\\n')\n        if len(lines) >= 2:\n            n = json.loads(lines[0])\n            edges = json.loads(lines[1])\n            sol = Solution()\n            print(json.dumps(sol.countComponents(n, edges)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nclass Solution {\npublic:\n    int countComponents(int n, vector<vector<int>>& edges) {\n        // Your logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        int n = stoi(line1);\n        vector<vector<int>> edges;\n        int n_len = line2.length();\n        for (int i = 0; i < n_len; ++i) {\n            if (line2[i] == '[') {\n                int start = i;\n                int open = 1;\n                while (open > 0 && ++i < n_len) {\n                    if (line2[i] == '[') open++;\n                    else if (line2[i] == ']') open--;\n                }\n                if (start > 0) {\n                    string inner = line2.substr(start + 1, i - start - 1);\n                    vector<int> row;\n                    stringstream ss(inner);\n                    string item;\n                    while (getline(ss, item, ',')) {\n                        row.push_back(stoi(item));\n                    }\n                    edges.push_back(row);\n                }\n            }\n        }\n        Solution sol;\n        cout << sol.countComponents(n, edges) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int countComponents(int n, int[][] edges) {\n        // Your logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            int n = Integer.parseInt(scanner.nextLine().trim());\n            if (scanner.hasNextLine()) {\n                String line2 = scanner.nextLine().trim();\n                List<int[]> edgesList = new ArrayList<>();\n                int len = line2.length();\n                for (int i = 0; i < len; i++) {\n                    if (line2.charAt(i) == '[') {\n                        int start = i;\n                        int open = 1;\n                        while (open > 0 && ++i < len) {\n                            if (line2.charAt(i) == '[') open++;\n                            else if (line2.charAt(i) == ']') open--;\n                        }\n                        if (start > 0) {\n                            String inner = line2.substring(start + 1, i);\n                            if (!inner.isEmpty()) {\n                                String[] parts = inner.split(\",\");\n                                int[] row = new int[parts.length];\n                                for (int j = 0; j < parts.length; j++) {\n                                    row[j] = Integer.parseInt(parts[j].trim());\n                                }\n                                edgesList.add(row);\n                            }\n                        }\n                    }\n                }\n                int[][] edges = edgesList.toArray(new int[0][]);\n                Solution sol = new Solution();\n                System.out.println(sol.countComponents(n, edges));\n            }\n        }\n    }\n}",
        "javascript": "/**\n * @param {number} n\n * @param {number[][]} edges\n * @return {number}\n */\nvar countComponents = function(n, edges) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const n = JSON.parse(input[0]);\n    const edges = JSON.parse(input[1]);\n    console.log(JSON.stringify(countComponents(n, edges)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint countComponents(int n, int** edges, int edgesSize, int* edgesColSize) {\n    // Your logic here\n    return 0;\n}\n\nint main() {\n    char line1[100];\n    char line2[200000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        int n = atoi(line1);\n        int capacity = 100;\n        int** edges = malloc(capacity * sizeof(int*));\n        int* colSize = malloc(capacity * sizeof(int));\n        int size = 0;\n        char* ptr = line2;\n        while (*ptr && *ptr != '[') ptr++;\n        if (*ptr == '[') ptr++;\n        while (*ptr) {\n            if (*ptr == '[') {\n                ptr++;\n                int rowCap = 10;\n                int* row = malloc(rowCap * sizeof(int));\n                int rowSize = 0;\n                while (*ptr && *ptr != ']') {\n                    int val;\n                    int charsRead;\n                    if (sscanf(ptr, \"%d%n\", &val, &charsRead) == 1) {\n                        if (rowSize >= rowCap) {\n                            rowCap *= 2;\n                            row = realloc(row, rowCap * sizeof(int));\n                        }\n                        row[rowSize++] = val;\n                        ptr += charsRead;\n                    } else if (*ptr == ',') {\n                        ptr++;\n                    } else {\n                        ptr++;\n                    }\n                }\n                if (size >= capacity) {\n                    capacity *= 2;\n                    edges = realloc(edges, capacity * sizeof(int*));\n                    colSize = realloc(colSize, capacity * sizeof(int));\n                }\n                edges[size] = row;\n                colSize[size] = rowSize;\n                size++;\n            }\n            ptr++;\n        }\n        int result = countComponents(n, edges, size, colSize);\n        printf(\"%d\\n\", result);\n        for (int i = 0; i < size; i++) free(edges[i]);\n        free(edges);\n        free(colSize);\n    }\n    return 0;\n}"
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
