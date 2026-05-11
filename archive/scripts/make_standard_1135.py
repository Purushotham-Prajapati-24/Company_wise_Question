import json
import os

def generate_json():
    problem_id = 1135
    title = "Connecting Cities With Minimum Cost"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1135. Connecting Cities With Minimum Cost</h3>
<p>There are <code>n</code> cities labeled from 1 to <code>n</code>. You are given <code>connections</code>, where each <code>connections[i] = [u, v, cost]</code> represents the cost to connect city <code>u</code> and city <code>v</code> together. (A connection is bidirectional: connecting <code>u</code> and <code>v</code> is the same as connecting <code>v</code> and <code>u</code>.)</p>

<p>Return the minimum cost to connect all <code>n</code> cities such that there is at least one path between each pair of cities. If it is impossible to connect all <code>n</code> cities, return <code>-1</code>.</p>

<p>The minimum cost is the sum of the costs of the connections used.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/20/1314_ex2.png" style="width: 161px; height: 141px;" />
<pre>
<strong>Input:</strong> n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Choosing any two connections will connect all cities so we choose the ones with minimum cost.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/20/1314_ex1.png" style="width: 136px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 4, connections = [[1,2,3],[3,4,4]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no way to connect all cities even if all connections are used.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= connections.length &lt;= 10<sup>4</sup></code></li>
	<li><code>connections[i].length == 3</code></li>
	<li><code>1 &lt;= u, v &lt;= n</code></li>
	<li><code>u != v</code></li>
	<li><code>0 &lt;= cost &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "An integer `n` and a 2D array `connections` provided as `[n, connections]` in JSON."
    output_format = "An integer representing the minimum cost, or -1."

    constraints = [
        "1 <= n <= 10^4",
        "1 <= connections.length <= 10^4",
        "1 <= u, v <= n, u != v",
        "0 <= cost <= 10^5"
    ]

    explanation = """This is a Minimum Spanning Tree (MST) problem.
1. Use Kruskal's algorithm: sort all connections by cost.
2. Use Union-Find (Disjoint Set Union) to manage components of cities.
3. Iterate through sorted connections and add each connection if it connects two different components.
4. Keep track of the total cost and the number of edges added.
5. If we add `n - 1` edges, return the total cost. Otherwise, return -1."""

    answer = """class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        parent = list(range(n + 1))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
        
        connections.sort(key=lambda x: x[2])
        total_cost = 0
        edges_count = 0
        for u, v, cost in connections:
            if union(u, v):
                total_cost += cost
                edges_count += 1
                if edges_count == n - 1:
                    return total_cost
        return total_cost if n == 1 and edges_count == 0 else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        data = json.loads(raw)
        n, connections = data
        sol = Solution()
        print(sol.minimumCost(n, connections))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumCost(int n, vector<vector<int>>& connections) {
        // User logic here
        return -1;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        int n = j[0].get<int>();
        vector<vector<int>> connections = j[1].get<vector<vector<int>>>();
        Solution sol;
        cout << sol.minimumCost(n, connections) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minimumCost(int n, int[][] connections) {
        // User logic here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (int)data[0];
            int[][] connections = mapper.convertValue(data[1], int[][].class);
            System.out.println(new Solution().minimumCost(n, connections));
        }
    }
}""",
        "javascript": """var minimumCost = function(n, connections) {
    // User logic here
    return -1;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, connections] = JSON.parse(input);
    console.log(minimumCost(n, connections));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int minimumCost(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    // User logic here
    return -1;
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int** conn = malloc(cap * sizeof(int*));
    int* cols = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && c != '[' && c != ']');
        if (c == EOF || c == ']') break;
        int row_cap = 3, row_size = 0;
        int* row = malloc(row_cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (row_size >= row_cap) { row_cap *= 2; row = realloc(row, row_cap * sizeof(int)); }
            scanf("%d", &row[row_size++]);
        }
        if (s >= cap) { cap *= 2; conn = realloc(conn, cap * sizeof(int*)); cols = realloc(cols, cap * sizeof(int)); }
        conn[s] = row;
        cols[s++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    printf("%d\\n", minimumCost(n, conn, s, cols));
    return 0;
}"""
    }

    def solve(n, connections):
        parent = list(range(n + 1))
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
        connections.sort(key=lambda x: x[2])
        ans = 0
        cnt = 0
        for u, v, cost in connections:
            if union(u, v):
                ans += cost
                cnt += 1
                if cnt == n - 1: return ans
        return ans if n == 1 else -1

    test_cases_data = [
        [3, [[1,2,5],[1,3,6],[2,3,1]]], # Sample 1
        [4, [[1,2,3],[3,4,4]]],        # Sample 2
        [1, []],
        [2, [[1,2,100]]],
        [2, []],
        [5, [[1,2,1],[2,3,2],[3,4,3],[4,5,4]]],
        [5, [[1,5,10],[1,2,1],[2,3,1],[3,4,1]]],
        # Stress tests
        [100, [[i, i+1, 1] for i in range(1, 100)]],
        [100, []],
        [1000, [[i, i+1, 5] for i in range(1, 1000)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 512, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Tree", "Graph", "Union Find", "Minimum Spanning Tree"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
