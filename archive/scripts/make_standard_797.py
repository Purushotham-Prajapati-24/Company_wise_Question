import json
import os

def generate_json():
    problem_id = 797
    title = "All Paths From Source to Target"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>797. All Paths From Source to Target</h3>
<p>Given a directed acyclic graph (<strong>DAG</strong>) of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>, find all possible paths from node <code>0</code> to node <code>n - 1</code> and return them in <strong>any order</strong>.</p>

<p>The graph is given as follows: <code>graph[i]</code> is a list of all nodes you can visit from node <code>i</code> (i.e., there is a directed edge from node <code>i</code> to node <code>graph[i][j]</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> graph = [[1,2],[3],[3],[]]
<strong>Output:</strong> [[0,1,3],[0,2,3]]
<strong>Explanation:</strong> There are two paths: 0 -&gt; 1 -&gt; 3 and 0 -&gt; 2 -&gt; 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>Output:</strong> [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == graph.length</code></li>
    <li><code>2 &lt;= n &lt;= 15</code></li>
    <li><code>0 &lt;= graph[i][j] &lt; n</code></li>
    <li><code>graph[i][j] != i</code> (i.e., there will be no self-loops).</li>
    <li>All the elements of <code>graph[i]</code> are <strong>unique</strong>.</li>
    <li>The input graph is <strong>guaranteed</strong> to be a <strong>DAG</strong>.</li>
</ul>"""

    input_format = "A single line containing the 2D JSON array `graph`."
    output_format = "A 2D JSON array containing all paths. The order of paths doesn't matter, but the internal nodes in each path must be in order."

    constraints = [
        "2 <= n <= 15",
        "0 <= graph[i][j] < n",
        "The graph is a DAG"
    ]

    explanation = """Since the graph is a DAG, we can use simple Backtracking/DFS to find all paths from 0 to n-1. We start at node 0 and explore each neighbor recursively until we reach the target node n-1."""

    answer = """class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        res = []
        
        def dfs(node, path):
            if node == target:
                res.append(list(path))
                return
            
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        
        dfs(0, [0])
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        graph = json.loads(raw)
        sol = Solution()
        res = sol.allPathsSourceTarget(graph)
        # Sort for consistent verification
        res.sort()
        print(json.dumps(res).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        // User logic here
        return {};
    }
};

vector<vector<int>> parse2DArray(string input) {
    auto res = vector<vector<int>>();
    size_t i = 1;
    while (i < input.length() - 1) {
        if (input[i] == '[') {
            vector<int> row; i++;
            while (input[i] != ']') {
                if (isdigit(input[i])) {
                    int val = 0;
                    while (isdigit(input[i])) val = val * 10 + (input[i++] - '0');
                    row.push_back(val);
                } else i++;
            }
            res.push_back(row); i++;
        } else i++;
    }
    return res;
}

int main() {
    string input;
    if (cin >> input) {
        auto graph = parse2DArray(input);
        Solution sol;
        auto res = sol.allPathsSourceTarget(graph);
        sort(res.begin(), res.end());
        cout << "[";
        for (int i=0; i<res.size(); ++i) {
            cout << "[";
            for (int j=0; j<res[i].size(); ++j) cout << res[i][j] << (j+1==res[i].size()?"":",");
            cout << "]" << (i+1==res.size()?"":",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    static int[][] parse2DArray(String raw) {
        raw = raw.trim();
        raw = raw.substring(1, raw.length()-1);
        if (raw.isEmpty()) return new int[0][0];
        List<int[]> resList = new ArrayList<>();
        int i = 0;
        while (i < raw.length()) {
            if (raw.charAt(i) == '[') {
                int j = i;
                while (raw.charAt(j) != ']') j++;
                String rowStr = raw.substring(i + 1, j).trim();
                if (rowStr.isEmpty()) resList.add(new int[0]);
                else {
                    String[] parts = rowStr.split(",");
                    int[] row = new int[parts.length];
                    for (int k=0; k<parts.length; k++) row[k] = Integer.parseInt(parts[k].trim());
                    resList.add(row);
                }
                i = j + 1;
            } else i++;
        }
        return resList.toArray(new int[0][]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[][] graph = parse2DArray(sc.next());
            Solution sol = new Solution();
            List<List<Integer>> res = sol.allPathsSourceTarget(graph);
            res.sort((a, b) -> {
                for (int i=0; i<Math.min(a.size(), b.size()); i++) if (!a.get(i).equals(b.get(i))) return a.get(i)-b.get(i);
                return a.size()-b.size();
            });
            System.out.print("[");
            for (int i=0; i<res.size(); i++) {
                System.out.print("[");
                for (int j=0; j<res.get(i).size(); j++) System.out.print(res.get(i).get(j) + (j+1==res.get(i).size()?"":","));
                System.out.print("]" + (i+1==res.size()?"":","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function(graph) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const res = allPathsSourceTarget(JSON.parse(input));
    res.sort((a, b) => a.join(',').localeCompare(b.join(',')));
    console.log(JSON.stringify(res).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int** allPathsSourceTarget(int** graph, int graphSize, int* graphColSize, int* returnSize, int** returnColumnSizes) {
    // User logic here
    return NULL;
}

int** parse2DArray(char* input, int* outSize, int** outColSizes) {
    int cap = 16, size = 0, i = 0;
    int** res = malloc(cap * sizeof(int*));
    int* cols = malloc(cap * sizeof(int));
    while (input[i]) {
        if (input[i] == '[') {
            i++; if (input[i] == '[') continue;
            int rcap = 16, csize = 0;
            int* row = malloc(rcap * sizeof(int));
            while (input[i] && input[i] != ']') {
                if (isdigit(input[i])) {
                    int val, off=0;
                    sscanf(input+i, "%d%n", &val, &off);
                    if (csize == rcap) row = realloc(row, (rcap *= 2) * sizeof(int));
                    row[csize++] = val; i += off;
                } else i++;
            }
            if (size == cap) { res = realloc(res, (cap *= 2) * sizeof(int*)); cols = realloc(cols, cap * sizeof(int)); }
            res[size] = row; cols[size++] = csize;
        }
        i++;
    }
    *outSize = size; *outColSizes = cols;
    return res;
}

int main() {
    char input[10000];
    if (scanf("%s", input) == 1) {
        int sz; int* colsz;
        int** graph = parse2DArray(input, &sz, &colsz);
        int retSz; int* retColSz;
        int** res = allPathsSourceTarget(graph, sz, colsz, &retSz, &retColSz);
        // C order simplification for standard print
        printf("[");
        for (int i=0; i<retSz; i++) {
            printf("[");
            for (int j=0; j<retColSz[i]; j++) printf("%d%s", res[i][j], j+1==retColSz[i]?"":",");
            printf("]%s", i+1==retSz?"":",");
        }
        printf("]\\n");
    }
    return 0;
}"""
    }

    def solve(graph):
        target = len(graph) - 1
        res = []
        def dfs(node, path):
            if node == target:
                res.append(list(path))
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        dfs(0, [0])
        res.sort()
        return res

    test_cases_data = [
        [[1,2],[3],[3],[]],
        [[4,3,1],[3,2,4],[3],[4],[]],
        [[1],[]],
        [[1,2,3],[2,3],[3],[]],
        [[1,4,3],[3],[2,4],[],[]],
        [[1,2,3,4],[],[],[],[]],
        [[1,2,3],[4],[4],[4],[]],
        [[1,2,3],[2,3],[3],[]],
        [[1,2],[2,3],[3,4],[4,5],[]],
        [[1,2,3,4,5,6,7,8,9,10,11,12,13,14],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    ]

    test_cases = []
    for i, graph in enumerate(test_cases_data):
        inp = json.dumps(graph).replace(" ", "")
        out = json.dumps(solve(graph)).replace(" ", "")
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
        "topics": ["Backtracking", "Depth-First Search", "Graph"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
