import json
import os

def generate_json():
    problem_id = 847
    title = "Shortest Path Visiting All Nodes"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>847. Shortest Path Visiting All Nodes</h3>
<p>You have an undirected, connected graph of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given an array <code>graph</code> where <code>graph[i]</code> is a list of all the nodes connected with node <code>i</code> by an edge.</p>

<p>Return <em>the length of the shortest path that visits every node</em>. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg" style="width: 222px; height: 183px;" />
<pre>
<strong>Input:</strong> graph = [[1,2,3],[0],[0],[0]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible path is [1,0,2,0,3].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg" style="width: 382px; height: 181px;" />
<pre>
<strong>Input:</strong> graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible path is [0,1,4,2,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt; n</code></li>
	<li><code>graph[i]</code> does not contain <code>i</code>.</li>
	<li>If <code>graph[a]</code> contains <code>b</code>, then <code>graph[b]</code> contains <code>a</code>.</li>
	<li>The input graph is always connected.</li>
</ul>"""

    input_format = "An integer n, followed by n lines. Each line i starts with a count c_i, followed by c_i neighbors of node i."
    output_format = "An integer representing the shortest path length."
    
    constraints = ["1 <= n <= 12", "Graph is connected and undirected.", "Shortest path visiting all nodes."]
    
    explanation = """HARD problem on ."""
    
    answer = """from collections import deque
def shortestPathLength(graph):
    n = len(graph)
    if n == 1: return 0
    q = deque([(i, 1 << i, 0) for i in range(n)])
    visited = {(i, 1 << i) for i in range(n)}
    target = (1 << n) - 1
    
    while q:
        node, mask, dist = q.popleft()
        if mask == target: return dist
        for neighbor in graph[node]:
            new_mask = mask | (1 << neighbor)
            if (neighbor, new_mask) not in visited:
                visited.add((neighbor, new_mask))
                q.append((neighbor, new_mask, dist + 1))
    return -1"""

    boilerplate = {
        "python": "import sys\n\ndef shortestPathLength(graph):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    graph = input_data[0] if len(input_data) > 0 else \"\"\n    print(shortestPathLength(graph))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint shortestPathLength(string graph) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string graph; cin >> graph;\n    cout << shortestPathLength(graph) << endl;\n    return 0;\n}",
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
