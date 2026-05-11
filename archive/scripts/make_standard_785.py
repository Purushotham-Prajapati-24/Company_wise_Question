import json
import os

def generate_json():
    problem_id = 785
    title = "Is Graph Bipartite?"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>785. Is Graph Bipartite?</h3>
<p>There is an <strong>undirected</strong> graph with <code>n</code> nodes, where each node is numbered between <code>0</code> and <code>n - 1</code>. You are given a 2D array <code>graph</code>, where <code>graph[u]</code> is an array of nodes that node <code>u</code> is adjacent to. More formally, for each <code>v</code> in <code>graph[u]</code>, there is an undirected edge between node <code>u</code> and node <code>v</code>. The graph has the following properties:</p>

<ul>
    <li>There are no self-edges (<code>graph[u]</code> does not contain <code>u</code>).</li>
    <li>There are no parallel edges (<code>graph[u]</code> does not contain duplicate values).</li>
    <li>If <code>v</code> is in <code>graph[u]</code>, then <code>u</code> is in <code>graph[v]</code> (the graph is undirected).</li>
    <li>The graph may not be connected, meaning there may be two nodes <code>u</code> and <code>v</code> such that there is no path between them.</li>
</ul>

<p>A graph is <strong>bipartite</strong> if the nodes can be partitioned into two independent sets <code>A</code> and <code>B</code> such that every edge in the graph connects a node in set <code>A</code> and a node in set <code>B</code>.</p>

<p>Return <code>true</code><em> if and only if it is <strong>bipartite</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> graph = [[1,3],[0,2],[1,3],[0,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can partition the nodes into two sets: {0, 2} and {1, 3}.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>graph.length == n</code></li>
    <li><code>1 &lt;= n &lt;= 100</code></li>
    <li><code>0 &lt;= graph[u].length &lt; n</code></li>
    <li><code>0 &lt;= graph[u][i] &lt; n</code></li>
    <li><code>graph[u]</code> does not contain <code>u</code>.</li>
    <li>All the values of <code>graph[u]</code> are <strong>unique</strong>.</li>
    <li>The graph is undirected; if <code>v</code> is in <code>graph[u]</code>, then <code>u</code> is in <code>graph[v]</code>.</li>
</ul>"""

    input_format = "A single line containing the 2D JSON array `graph`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= graph.length <= 100",
        "0 <= graph[u].length < n",
        "0 <= graph[u][i] < n",
        "graph[u] does not contain u",
        "All the values of graph[u] are unique",
        "The graph is undirected"
    ]

    explanation = """We can use graph coloring with BFS or DFS. Assign colors 0 and 1 to alternating levels. If we ever try to color a node with a color that conflicts with its currently assigned color, the graph is not bipartite. Return false in that case. If we successfully color all components, return true."""

    answer = """import collections

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    curr = stack.pop()
                    for nei in graph[curr]:
                        if nei not in color:
                            color[nei] = color[curr] ^ 1
                            stack.append(nei)
                        elif color[nei] == color[curr]:
                            return False
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        graph = json.loads(raw)
        sol = Solution()
        print("true" if sol.isBipartite(graph) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        // User logic here
        return false;
    }
};

vector<vector<int>> parse2DArray(string input) {
    vector<vector<int>> res;
    size_t i = 1;
    while (i < input.length() - 1) {
        if (input[i] == '[') {
            vector<int> row;
            i++;
            while (input[i] != ']') {
                if (isdigit(input[i])) {
                    int val = 0;
                    while (isdigit(input[i])) { val = val * 10 + (input[i] - '0'); i++; }
                    row.push_back(val);
                } else {
                    i++;
                }
            }
            res.push_back(row);
            i++;
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string input;
    if (cin >> input) {
        vector<vector<int>> graph = parse2DArray(input);
        Solution sol;
        cout << (sol.isBipartite(graph) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[][] parse2DArray(String raw) {
        raw = raw.trim();
        if (raw.length() < 2) return new int[0][0];
        raw = raw.substring(1, raw.length() - 1).trim();
        if (raw.isEmpty()) return new int[0][0];
        
        List<int[]> resList = new ArrayList<>();
        int i = 0;
        while (i < raw.length()) {
            if (raw.charAt(i) == '[') {
                int j = i;
                while (raw.charAt(j) != ']') j++;
                String rowStr = raw.substring(i + 1, j);
                if (rowStr.trim().isEmpty()) {
                    resList.add(new int[0]);
                } else {
                    String[] parts = rowStr.split(",");
                    int[] row = new int[parts.length];
                    for (int k = 0; k < parts.length; k++) {
                        row[k] = Integer.parseInt(parts[k].trim());
                    }
                    resList.add(row);
                }
                i = j + 1;
            } else {
                i++;
            }
        }
        int[][] res = new int[resList.size()][];
        for (int k = 0; k < resList.size(); k++) res[k] = resList.get(k);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String input = sc.next();
            int[][] graph = parse2DArray(input);
            Solution sol = new Solution();
            System.out.println(sol.isBipartite(graph) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function(graph) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(isBipartite(JSON.parse(input)) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool isBipartite(int** graph, int graphSize, int* graphColSize) {
    // User logic here
    return false;
}

int** parse2DArray(char* input, int* outSize, int** outColSizes) {
    int cap = 10, size = 0, i = 0;
    int** res = (int**)malloc(cap * sizeof(int*));
    int* cols = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '[') {
            i++;
            if (input[i] == '[') continue;
            int rcap = 10, csize = 0;
            int* row = (int*)malloc(rcap * sizeof(int));
            while (input[i] && input[i] != ']') {
                if (isdigit(input[i])) {
                    int val, off = 0;
                    sscanf(input+i, "%d%n", &val, &off);
                    if (!off) { i++; continue; }
                    if (csize == rcap) { rcap *= 2; row = realloc(row, rcap * sizeof(int)); }
                    row[csize++] = val;
                    i += off;
                } else {
                    i++;
                }
            }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int*)); cols = realloc(cols, cap * sizeof(int)); }
            res[size] = row;
            cols[size++] = csize;
        }
        i++;
    }
    *outSize = size;
    *outColSizes = cols;
    return res;
}

int main() {
    char input[100000];
    if (scanf("%99999s", input) == 1) {
        int sz;
        int* colsz;
        int** graph = parse2DArray(input, &sz, &colsz);
        printf("%s\\n", isBipartite(graph, sz, colsz) ? "true" : "false");
        for(int i=0; i<sz; i++) free(graph[i]);
        free(graph);
        free(colsz);
    }
    return 0;
}"""
    }

    def solve(graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    curr = stack.pop()
                    for nei in graph[curr]:
                        if nei not in color:
                            color[nei] = color[curr] ^ 1
                            stack.append(nei)
                        elif color[nei] == color[curr]:
                            return False
        return True

    test_cases_data = [
        [[1,2,3],[0,2],[0,1,3],[0,2]],
        [[1,3],[0,2],[1,3],[0,2]],
        [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]],
        [[1],[0,3],[3],[1,2]],
        [[1,4],[0,2],[1,3],[2,4],[0,3]],
        [[2,4],[2,3,4],[0,1],[1],[0,1]],
        [[1],[0],[4],[4],[2,3]],
        [[1],[0]],
        [[],[],[],[]],
        [[4],[],[4],[4],[0,2,3]]
    ]

    test_cases = []
    for i, graph in enumerate(test_cases_data):
        inp = json.dumps(graph).replace(" ", "")
        out = "true" if solve(graph) else "false"
        is_sample = i < 2
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_').replace('?', '')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
