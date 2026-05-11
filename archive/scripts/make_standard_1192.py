import json
import os

def generate_json():
    problem_id = 1192
    title = "Critical Connections in a Network"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1192. Critical Connections in a Network</h3>
<p>There are <code>n</code> servers numbered from <code>0</code> to <code>n - 1</code> connected by undirected server-to-server <code>connections</code> forming a network where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a connection between servers <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Any server can reach other servers directly or indirectly through the network.</p>

<p>A <em>critical connection</em> is a connection that, if removed, will make some servers unable to reach some other server.</p>

<p>Return all critical connections in the network in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png" style="width: 198px; height: 191px;">
<pre><strong>Input:</strong> n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>Output:</strong> [[1,3]]
<strong>Explanation:</strong> [[3,1]] is also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2, connections = [[0,1]]
<strong>Output:</strong> [[0,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n - 1 &lt;= connections.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated connections.</li>
</ul>"""

    input_format = "An integer `n` and a JSON matrix `connections` provided as `[n, connections]` in JSON."
    output_format = "A JSON matrix representing all critical connections."

    constraints = [
        "2 <= n <= 10^5",
        "n - 1 <= connections.length <= 10^5",
        "0 <= a, b <= n - 1"
    ]

    explanation = """To find critical connections (bridges) in an undirected graph:
1. Use Tarjan's bridge-finding algorithm or a similar DFS-based approach.
2. Maintain `discovery_time` and `low_link_value` for each node.
3. During DFS, for an edge `(u, v)`:
   - If `v` is the parent of `u`, skip.
   - If `v` is already visited, update `low_link[u] = min(low_link[u], discovery[v])`.
   - If `v` is not visited, recursively call DFS for `v`.
   - After return, update `low_link[u] = min(low_link[u], low_link[v])`.
   - If `low_link[v] > discovery[u]`, the edge `(u, v)` is a bridge.
4. Return all identified bridges."""

    answer = """import collections

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        discovery = [-1] * n
        low = [-1] * n
        res = []
        
        def dfs(u, p, t):
            discovery[u] = low[u] = t
            for v in adj[u]:
                if v == p: continue
                if discovery[v] == -1:
                    dfs(v, u, t + 1)
                    low[u] = min(low[u], low[v])
                    if low[v] > discovery[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], discovery[v])
                    
        dfs(0, -1, 0)
        return res"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        data = json.loads(raw)
        n = data[0]
        connections = data[1]
        sol = Solution()
        print(json.dumps(sol.criticalConnections(n, connections)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0];
        vector<vector<int>> connections = j[1].get<vector<vector<int>>>();
        Solution sol;
        vector<vector<int>> res = sol.criticalConnections(n, connections);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (Integer) data[0];
            List<List<Integer>> connections = mapper.convertValue(data[1], List.class);
            List<List<Integer>> res = new Solution().criticalConnections(n, connections);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var criticalConnections = function(n, connections) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, connections] = JSON.parse(input);
    const res = criticalConnections(n, connections);
    console.log(JSON.stringify(res).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int** criticalConnections(int n, int** connections, int connectionsSize, int* connectionsColSize, int* returnSize, int** returnColumnSizes){
    // User logic here
    return NULL;
}

int main() {
    // Boilerplate for graph parsing
    return 0;
}"""
    }

    import collections
    def solve(n, connections):
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        discovery = [-1] * n
        low = [-1] * n
        res = []
        def dfs(u, p, t):
            discovery[u] = low[u] = t
            for v in adj[u]:
                if v == p: continue
                if discovery[v] == -1:
                    dfs(v, u, t + 1)
                    low[u] = min(low[u], low[v])
                    if low[v] > discovery[u]:
                        res.append(sorted([u, v]))
                else:
                    low[u] = min(low[u], discovery[v])
        dfs(0, -1, 0)
        return sorted(res)

    test_cases_data = [
        [4, [[0,1],[1,2],[2,0],[1,3]]], # Sample 1
        [2, [[0,1]]],                   # Sample 2
        [3, [[0,1],[1,2],[0,2]]],       # Triangle no critical
        [3, [[0,1],[1,2]]],             # Line two critical
        [5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]], # Complex no critical
        [6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]], # Two triangles connected by bridge
        [4, [[0,1],[1,2],[2,3]]],       # Simple path
        # Stress tests
        [1000, [[i, i+1] for i in range(999)]], # Large line
        [100, [[0, i] for i in range(1, 100)]], # Large star
        [100, [[i, (i+1)%100] for i in range(100)]] # Large circle
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Graph", "DFS", "Tarjan's Bridge Algorithm"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
