import json
import os

def generate_json():
    problem_id = 684
    title = "Redundant Connection"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>684. Redundant Connection</h3>
<p>In this problem, a tree is an <b>undirected graph</b> that is connected and has no cycles.</p>

<p>You are given a graph that started as a tree with <code>n</code> nodes labeled from <code>1</code> to <code>n</code>, with one additional edge added. The added edge has two different vertices chosen from <code>1</code> to <code>n</code>, and was not an edge that already existed.</p>

<p>The graph is represented as an array <code>edges</code> of length <code>n</code> where <code>edges[i] = [ai, bi]</code> indicates that there is an edge between nodes <code>ai</code> and <code>bi</code> in the graph.</p>

<p>Return <em>an edge that can be removed so that the resulting graph is a tree of n nodes</em>. If there are multiple answers, return the answer that occurs last in the input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> [2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
<strong>Output:</strong> [1,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= ai &lt; bi &lt;= edges.length</code></li>
	<li><code>ai != bi</code></li>
	<li>There are no repeated edges.</li>
	<li>The given graph is connected.</li>
</ul>"""

    input_format = "Each line contains a space-separated pair of integers (u v) representing an edge."
    output_format = "Two space-separated integers representing the redundant edge."
    
    constraints = [
        "3 <= n <= 1000",
        "n == edges.length (exactly one redundant edge).",
        "O(N \u03b1(N)) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To find the redundant edge in a graph that was originally a tree:
1. **The Principle (Union-Find)**:
   - A tree with $n$ nodes has exactly $n-1$ edges and no cycles.
   - Adding one more edge creates exactly one cycle.
   - We process edges one by one and use a Disjoint Set Union (DSU) to keep track of connected components.
2. **Implementation**:
   - For each edge $(u, v)$:
     - Check if $u$ and $v$ are already in the same component using `find(u)` and `find(v)`.
     - If `find(u) == find(v)`, this edge forms a cycle and is the redundant one.
     - Otherwise, `union(u, v)` to merge components.
   - Since we need the *last* such edge in the input, the first one that forms a cycle is the answer (because only one edge was added to the tree).
3. **Complexity**:
   - Time Complexity: O(N \u03b1(N)), where \u03b1 is the inverse Ackermann function (nearly constant).
   - Space Complexity: O(N) to store the `parent` and `rank` arrays."""
    
    answer = """class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return []"""

    boilerplate = {
        "python": "import sys\n\nclass DSU:\n    # Implement find and union\n    pass\n\ndef findRedundantConnection(edges):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    edges = [list(map(int, line.split())) for line in lines if line.strip()]\n    res = findRedundantConnection(edges)\n    print(f'{res[0]} {res[1]}')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <numeric>\n\nusing namespace std;\n\nclass DSU {\npublic:\n    DSU(int n);\n    int find(int x);\n    bool combine(int x, int y);\n};",
        "java": "public class Solution {\n    public int[] findRedundantConnection(int[][] edges) {\n        // User logic\n        return new int[]{0, 0};\n    }\n}",
        "javascript": "function findRedundantConnection(edges) {\n    // User logic\n}",
        "c": "int* findRedundantConnection(int** edges, int edgesSize, int* edgesColSize, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 2\\n1 3\\n2 3", "expected_output": "2 3", "is_sample": True},
        {"input": "1 2\\n2 3\\n3 4\\n1 4\\n1 5", "expected_output": "1 4", "is_sample": True},
        {"input": "1 2\\n2 3\\n3 1", "expected_output": "3 1", "is_sample": False},
        {"input": "1 2\\n1 3\\n1 4\\n3 4", "expected_output": "3 4", "is_sample": False},
        {"input": "1 2\\n2 3\\n3 4\\n4 5\\n5 1", "expected_output": "5 1", "is_sample": False},
        {"input": "1 2\\n2 3\\n1 4\\n4 5\\n5 6\\n1 6", "expected_output": "1 6", "is_sample": False},
        {"input": "1 2\\n1 3\\n3 4\\n2 4\\n4 5", "expected_output": "2 4", "is_sample": False},
        {"input": "2 1\\n3 1\\n4 2\\n1 4", "expected_output": "1 4", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"{i} {i+1}" for i in range(1, 1000)]) + "\\n1000 1", "expected_output": "1000 1", "is_sample": False},
        {"input": "\\n".join([f"1 {i}" for i in range(2, 1001)]) + "\\n1000 2", "expected_output": "1000 2", "is_sample": False}
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
        "topics": ["Tree", "Graph", "DFS", "BFS", "Union Find"],
        "companyIndex": 0
    }

    output_path = "601-800/684_Redundant_Connection.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
