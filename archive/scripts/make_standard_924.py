import json
import os

def generate_json():
    problem_id = 924
    title = "Minimize Malware Spread"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>924. Minimize Malware Spread</h3>
<p>You are given a network of <code>n</code> nodes represented as an <code>n x n</code> adjacency matrix <code>graph</code>, where <code>graph[i][j] == 1</code> if nodes <code>i</code> and <code>j</code> are directly connected, and <code>0</code> otherwise.</p>

<p>Some nodes <code>initial</code> are initially infected with malware. When two nodes are directly connected, and at least one of them is infected with malware, both nodes will be infected with malware. This spread of malware will continue until no more nodes can be infected.</p>

<p>Suppose <code>M(initial)</code> is the final number of nodes infected with malware in the entire network after the spread of malware stops.</p>

<p>We will remove <strong>exactly one node</strong> from <code>initial</code>. Return the node that, if removed, would minimize <code>M(initial)</code>. If multiple nodes could be removed to minimize <code>M(initial)</code>, return such a node with the smallest index.</p>

<p>Note that if a node was removed from the <code>initial</code> list of infected nodes, it might still be infected later due to the malware spread.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == graph.length</code></li>
    <li><code>n == graph[i].length</code></li>
    <li><code>2 &lt;= n &lt;= 300</code></li>
    <li><code>graph[i][j]</code> is <code>0</code> or <code>1</code>.</li>
    <li><code>graph[i][j] == graph[j][i]</code></li>
    <li><code>graph[i][i] == 1</code></li>
    <li><code>1 &lt;= initial.length &lt;= n</code></li>
    <li><code>0 &lt;= initial[i] &lt;= n - 1</code></li>
    <li>All the integers in <code>initial</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A line with the JSON matrix `graph` and a second line with the JSON array `initial`."
    output_format = "An integer representing the node index to remove."

    constraints = [
        "2 <= n <= 300",
        "1 <= initial.length <= n"
    ]

    explanation = """The problem can be solved by finding the connected components of the graph. For each component, we count how many nodes are initially infected.
- If a component has exactly ONE initially infected node, removing that node would save all nodes in that component from malware.
- If a component has more than one initially infected node, removing one of them doesn't change the outcome for that component (it will still be fully infected by the other nodes).
We choose the node that saves the largest component. If there is a tie, or if no component has exactly one infected node, we return the smallest index among the initial infected nodes."""

    answer = """class Solution:
    def minMalwareSpread(self, graph: list[list[int]], initial: list[int]) -> int:
        n = len(graph)
        parent = list(range(n))
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j]:
                    union(i, j)
        
        from collections import Counter
        size = Counter(find(i) for i in range(n))
        infected_count = Counter(find(i) for i in initial)
        
        ans = -1
        max_size = -1
        initial.sort()
        
        for u in initial:
            root = find(u)
            if infected_count[root] == 1:
                if size[root] > max_size:
                    max_size = size[root]
                    ans = u
        
        return ans if ans != -1 else initial[0]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minMalwareSpread(self, graph: list[list[int]], initial: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        graph = json.loads(raw[0])
        initial = json.loads(raw[1])
        sol = Solution()
        print(sol.minMalwareSpread(graph, initial))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int minMalwareSpread(vector<vector<int>>& graph, vector<int>& initial) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parseMatrix(string s) {
    auto res = vector<vector<int>>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (s[i] == '[') {
            size_t end = s.find(']', i);
            string sub = s.substr(i + 1, end - i - 1);
            auto row = vector<int>();
            char buffer[sub.length() + 1];
            strcpy(buffer, sub.c_str());
            char* token = strtok(buffer, ",");
            while (token != NULL) {
                row.push_back(atoi(token));
                token = strtok(NULL, ",");
            }
            res.push_back(row);
            i = end + 1;
        } else i++;
    }
    return res;
}

vector<int> parseArray(string s) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (isdigit(s[i])) {
            int val = 0; int off=0;
            sscanf(s.c_str()+i, "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string gLine, iLine;
    if (getline(cin, gLine) && getline(cin, iLine)) {
        auto graph = parseMatrix(gLine);
        auto initial = parseArray(iLine);
        Solution sol;
        cout << sol.minMalwareSpread(graph, initial) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minMalwareSpread(int[][] graph, int[] initial) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[][] parseMatrix(String s) {
        s = s.substring(2, s.length() - 2);
        String[] rows = s.split("\\\\],\\\\[");
        int n = rows.length;
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] cells = rows[i].split(",");
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(cells[j].trim());
            }
        }
        return board;
    }
    static int[] parseArray(String s) {
        s = s.substring(1, s.length()-1);
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i=0; i<parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[][] graph = parseMatrix(sc.nextLine());
            int[] initial = parseArray(sc.nextLine());
            Solution sol = new Solution();
            System.out.println(sol.minMalwareSpread(graph, initial));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} graph
 * @param {number[]} initial
 * @return {number}
 */
var minMalwareSpread = function(graph, initial) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\n|\\r\\n/);
if (input.length >= 2) {
    console.log(minMalwareSpread(JSON.parse(input[0]), JSON.parse(input[1])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minMalwareSpread(int** graph, int graphSize, int* graphColSize, int* initial, int initialSize) {
    // User logic here
    return 0;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        printf("0\\n");
    }
    return 0;
}"""
    }

    def solve(graph, initial):
        n = len(graph)
        parent = list(range(n))
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j: parent[root_i] = root_j
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j]: union(i, j)
        from collections import Counter
        size = Counter(find(i) for i in range(n))
        infected_count = Counter(find(i) for i in initial)
        ans = -1
        max_size = -1
        initial.sort()
        for u in initial:
            root = find(u)
            if infected_count[root] == 1:
                if size[root] > max_size:
                    max_size = size[root]
                    ans = u
        return ans if ans != -1 else initial[0]

    test_cases_data = [
        ([[1,1,0],[1,1,0],[0,0,1]], [0,1]),
        ([[1,0,0],[0,1,0],[0,0,1]], [0,2]),
        ([[1,1,1],[1,1,1],[1,1,1]], [1,2]),
        ([[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], [0,3]),
        ([[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]], [0,1]),
        ([[1,0,0,0],[0,1,1,1],[0,1,1,1],[0,1,1,1]], [0,1,2]),
        ([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,1,1]], [0,2,3]),
        ([[1,0,0,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]], [1,3]),
        ([[1,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0],[0,0,0,1,0],[0,0,0,0,1]], [0,3,4]),
        ([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]], [0,1,2,3,4])
    ]

    test_cases = []
    for i, (graph, initial) in enumerate(test_cases_data):
        inp = f"{json.dumps(graph).replace(' ', '')}\n{json.dumps(initial).replace(' ', '')}"
        out = str(solve(graph, initial))
        is_sample = i < 3
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
        "topics": ["Array", "Graph", "Union Find", "Breadth-First Search", "Depth-First Search"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
