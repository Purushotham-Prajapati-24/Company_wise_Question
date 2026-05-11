import json
import os

def generate_json():
    problem_id = 685
    title = "Redundant Connection II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>685. Redundant Connection II</h3>
<p>In this problem, a rooted tree is a <b>directed</b> graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.</p>

<p>The given input is a directed graph that started as a rooted tree with <code>n</code> nodes (with distinct values <code>1, 2, ..., n</code>), with one additional directed edge added. The added edge has two different vertices chosen from <code>1</code> to <code>n</code>, and was not an edge that already existed.</p>

<p>The graph is represented as a 2D-array of <code>edges</code>. Each element of <code>edges</code> is a pair <code>[u<sub>i</sub>, v<sub>i</sub>]</code> that represents a <b>directed</b> edge connecting node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code>, where <code>u<sub>i</sub></code> is a parent of child <code>v<sub>i</sub></code>.</p>

<p>Return <em>an edge that can be removed so that the resulting graph is a rooted tree of n nodes</em>. If there are multiple answers, return the answer that occurs last in the input.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg" style="width: 222px; height: 222px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> [2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg" style="width: 222px; height: 382px;" />
<pre>
<strong>Input:</strong> edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
<strong>Output:</strong> [4,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
</ul>"""

    input_format = "An array of directed edges."
    output_format = "An array [u, v] representing the redundant edge."
    
    constraints = ["n == edges.length", "3 <= n <= 1000", "1 <= ui", "vi <= n"]
    
    explanation = """HARD problem on ."""
    
    answer = """def findRedundantDirectedConnection(edges):
    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])
        return parent[i]

    n = len(edges)
    parent = list(range(n + 1))
    candidate1, candidate2 = None, None
    node_parent = {}
    
    for i, (u, v) in enumerate(edges):
        if v in node_parent:
            candidate1 = node_parent[v]
            candidate2 = i
            break
        node_parent[v] = i

    for i, (u, v) in enumerate(edges):
        if i == candidate2: continue
        root_u = find(parent, u)
        if root_u == v:
            if candidate1 is None: return [u, v]
            return edges[candidate1]
        parent[v] = root_u
        
    return edges[candidate2]"""

    boilerplate = {
        "python": "import sys\n\ndef find(parent, i):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    parent = input_data[0] if len(input_data) > 0 else \"\"\n    i = input_data[1] if len(input_data) > 1 else \"\"\n    print(find(parent, i))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint find(string parent, string i) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string parent; cin >> parent;\n    string i; cin >> i;\n    cout << find(parent, i) << endl;\n    return 0;\n}",
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
