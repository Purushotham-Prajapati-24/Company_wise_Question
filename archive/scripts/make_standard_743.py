import json
import os
import heapq

def generate_json():
    problem_id = 743
    title = "Network Delay Time"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>743. Network Delay Time</h3>
<p>You are given a network of <code>n</code> nodes, labeled from <code>1</code> to <code>n</code>. You are also given <code>times</code>, a list of travel times as directed edges <code>times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)</code>, where <code>u<sub>i</sub></code> is the source node, <code>v<sub>i</sub></code> is the target node, and <code>w<sub>i</sub></code> is the time it takes for a signal to travel from source to target.</p>
<p>We will send a signal from a given node <code>k</code>. Return <i>the <b>minimum</b> time it takes for all the </i><code>n</code><i> nodes to receive the signal</i>. If it is impossible for all the <code>n</code> nodes to receive the signal, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="width: 217px; height: 239px;" />
<pre><strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= times.length &lt;= 6000</code></li>
	<li><code>times[i].length == 3</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>0 &lt;= w<sub>i</sub> &lt;= 100</code></li>
	<li>All the pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are <b>unique</b>. (i.e., no multiple edges.)</li>
</ul>
"""

    input_format = "A JSON dictionary with 'times', 'n', and 'k'."
    output_format = "An integer (minimum time) or -1."
    
    constraints = [
        "1 <= n <= 100",
        "1 <= k <= n",
        "1 <= times.length <= 6000",
        "Directed edges with weights 0-100."
    ]
    
    explanation = """To find the network delay time:
1. **Represent Graph**: Use an adjacency list: `graph[u] = [(v, w), ...]`.
2. **Dijkstra's Algorithm**:
   - Use a min-priority queue (min-heap) to explore the shortest path to each node.
   - Initialize `distances` map with infinity for all nodes except `k` (distance 0).
   - In each step, extract node with minimum distance, and relax its neighbors.
3. **Analyze Result**:
   - The time all nodes receive the signal is `max(distances.values())`.
   - If any node's distance is still infinity, return -1.
4. **Complexity**:
   - Time: O(E log V) where E is number of edges and V is number of nodes.
   - Space: O(E + V).

Complexity:
- Time: O(E log V).
- Space: O(E + V).
"""
    
    answer = """import heapq
import collections
def networkDelayTime(times, n, k):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    pq = [(0, k)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist: continue
        dist[node] = d
        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(pq, (d + weight, neighbor))
                
    return max(dist.values()) if len(dist) == n else -1"""

    boilerplate = {
        "python": "import sys\\nimport json\\nimport heapq\\nimport collections\\n\\ndef networkDelayTime(times, n, k):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    input_data = json.loads(sys.stdin.read().strip())\\n    print(networkDelayTime(input_data['times'], input_data['n'], input_data['k']))",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <queue>\\n#include <unordered_map>\\nusing namespace std;\\n\\nint networkDelayTime(vector<vector<int>>& times, int n, int k) { return -1; }",
        "java": "class Solution { public int networkDelayTime(int[][] times, int n, int k) { } }",
        "javascript": "var networkDelayTime = function(times, n, k) { };",
        "c": "int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k) { }"
    }

    test_cases = [
        {"input": '{"times": [[2,1,1],[2,3,1],[3,4,1]], "n": 4, "k": 2}', "expected_output": "2", "is_sample": True},
        {"input": '{"times": [[1,2,1]], "n": 2, "k": 1}', "expected_output": "1", "is_sample": True},
        {"input": '{"times": [[1,2,1]], "n": 2, "k": 2}', "expected_output": "-1", "is_sample": True},
        {"input": '{"times": [[1,2,1], [2,3,2], [1,3,2]], "n": 3, "k": 1}', "expected_output": "2", "is_sample": False},
        {"input": '{"times": [[1,2,1], [2,1,3]], "n": 2, "k": 1}', "expected_output": "1", "is_sample": False},
        {"input": '{"times": [[1,2,1], [2,3,1], [3,4,1]], "n": 5, "k": 1}', "expected_output": "-1", "is_sample": False},
        {"input": '{"times": [[1,2,0], [2,3,0]], "n": 3, "k": 1}', "expected_output": "0", "is_sample": False},
        {"input": '{"times": [[1,2,10], [1,3,5], [3,2,3]], "n": 3, "k": 1}', "expected_output": "8", "is_sample": False},
        # Stress cases
        {"input": json.dumps({"times": [[i, i+1, 1] for i in range(1, 100)], "n": 100, "k": 1}), "expected_output": "99", "is_sample": False},
        {"input": json.dumps({"times": [], "n": 100, "k": 1}), "expected_output": "-1", "is_sample": False}
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
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph", "Heap (Priority Queue)", "Shortest Path"],
        "companyIndex": 0
    }

    output_path = "601-800/743_Network_Delay_Time.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
