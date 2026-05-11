import json
import os

def generate_json():
    problem_id = 802
    title = "Find Eventual Safe States"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>802. Find Eventual Safe States</h3>
<p>There is a directed graph of <code>n</code> nodes with each node labeled from <code>0</code> to <code>n - 1</code>. The graph is represented by a <strong>0-indexed</strong> 2D integer array <code>graph</code> where <code>graph[i]</code> is an integer array of nodes adjacent to node <code>i</code>, meaning there is an edge from node <code>i</code> to each node in <code>graph[i]</code>.</p>

<p>A node is a <strong>terminal node</strong> if there are no outgoing edges. A node is a <strong>safe node</strong> if every possible path starting from that node leads to a <strong>terminal node</strong> (or another safe node).</p>

<p>Return <em>an array containing all the <strong>safe nodes</strong> of the graph</em>. The answer should be sorted in <strong>ascending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="Nodes 5 and 6 are terminal nodes. All paths starting at nodes 2, 4, 5, and 6 lead to either node 5 or 6." src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" style="width: 347px; height: 225px;" />
<pre>
<strong>Input:</strong> graph = [[1,2],[2,3],[5],[0],[5],[],[]]
<strong>Output:</strong> [2,4,5,6]
<strong>Explanation:</strong> The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
<strong>Output:</strong> [4]
<strong>Explanation:</strong>
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= graph[i].length &lt;= n</code></li>
	<li><code>0 &lt;= graph[i][j] &lt;= n - 1</code></li>
	<li><code>graph[i]</code> is sorted in a strictly increasing order.</li>
	<li>The graph may contain self-loops.</li>
	<li>The number of edges in the graph will be in the range <code>[1, 2 * 10<sup>4</sup>]</code>.</li>
</ul>"""

    input_format = "An integer n, followed by n lines. Each line i starts with a count c_i, followed by c_i neighbors of node i."
    output_format = "A list of sorted safe node IDs."
    
    constraints = ["1 <= n <= 10", "000", "Edges <= 20", "000", "Result must be sorted."]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """from collections import deque
def eventualSafeNodes(graph):
    n = len(graph)
    out_degree = [len(x) for x in graph]
    rev_graph = [[] for _ in range(n)]
    for i, neighbors in enumerate(graph):
        for v in neighbors:
            rev_graph[v].append(i)
    
    q = deque([i for i in range(n) if out_degree[i] == 0])
    safe = [False] * n
    while q:
        u = q.popleft()
        safe[u] = True
        for v in rev_graph[u]:
            out_degree[v] -= 1
            if out_degree[v] == 0:
                q.append(v)
    return [i for i in range(n) if safe[i]]"""

    boilerplate = {
        "python": "import sys\n\ndef eventualSafeNodes(graph):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    graph = input_data[0] if len(input_data) > 0 else \"\"\n    print(eventualSafeNodes(graph))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint eventualSafeNodes(string graph) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string graph; cin >> graph;\n    cout << eventualSafeNodes(graph) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = []

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
