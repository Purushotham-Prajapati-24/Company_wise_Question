import json
import os
from collections import defaultdict
import heapq

def generate_json():
    problem_id = 787
    title = "Cheapest Flights Within K Stops"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>787. Cheapest Flights Within K Stops</h3>
<p>There are <code>n</code> cities connected by some number of flights. You are given an array <code>flights</code> where <code>flights[i] = [from<sub>i</sub>, to<sub>i</sub>, price<sub>i</sub>]</code> indicates that there is a flight from city <code>from<sub>i</sub></code> to city <code>to<sub>i</sub></code> with cost <code>price<sub>i</sub></code>.</p>

<p>You are also given three integers <code>src</code>, <code>dst</code>, and <code>k</code>, return <em><strong>the cheapest price</strong> from </em><code>src</code><em> to </em><code>dst</code><em> with at most </em><code>k</code><em> stops. </em>If there is no such route, return<em> </em><code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
<strong>Output:</strong> 700
<strong>Explanation:</strong>
The optimal path with at most 1 stop from city 0 to 3 is 0 -&gt; 1 -&gt; 3 with cost 100 + 600 = 700.
Note that the path 0 -&gt; 1 -&gt; 2 -&gt; 3 is cheaper but has 2 stops.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
<strong>Output:</strong> 200
<strong>Explanation:</strong>
The optimal path with at most 1 stop from city 0 to 2 is 0 -&gt; 1 -&gt; 2 with cost 100 + 100 = 200.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 100</code></li>
    <li><code>0 &lt;= flights.length &lt;= (n * (n - 1) / 2)</code></li>
    <li><code>flights[i].length == 3</code></li>
    <li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub> &lt; n</code></li>
    <li><code>from<sub>i</sub> != to<sub>i</sub></code></li>
    <li><code>1 &lt;= price<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
    <li>There will not be any multiple flights between two cities.</li>
    <li><code>0 &lt;= src, dst, k &lt; n</code></li>
    <li><code>src != dst</code></li>
</ul>"""

    input_format = "Five lines:\nLine 1: integer `n`\nLine 2: 2D JSON array `flights`\nLine 3: integer `src`\nLine 4: integer `dst`\nLine 5: integer `k`"
    output_format = "An integer representing the cheapest price."

    constraints = [
        "1 <= n <= 100",
        "0 <= flights.length <= (n * (n - 1) / 2)",
        "0 <= src, dst, k < n"
    ]

    explanation = """We can use Dijkstra's Algorithm or Bellman-Ford. Given K stops means at most K+1 edges. A simple Bellman-Ford algorithm that relaxes all edges K+1 times is very efficient and simple to implement for this problem. We maintain an array of minimum costs and iterate K+1 times."""

    answer = """class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        
        for _ in range(k + 1):
            tmpPrices = list(prices)
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
            
        return prices[dst] if prices[dst] != float('inf') else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 5:
        n = int(raw[0])
        flights = json.loads(raw[1])
        src = int(raw[2])
        dst = int(raw[3])
        k = int(raw[4])
        sol = Solution()
        print(sol.findCheapestPrice(n, flights, src, dst, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // User logic here
        return -1;
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
    int n, src, dst, k;
    string arr_str;
    if (cin >> n >> arr_str >> src >> dst >> k) {
        vector<vector<int>> flights = parse2DArray(arr_str);
        Solution sol;
        cout << sol.findCheapestPrice(n, flights, src, dst, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // User logic here
        return -1;
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
                if (rowStr.trim().isEmpty()) { resList.add(new int[0]); } else {
                    String[] parts = rowStr.split(",");
                    int[] row = new int[parts.length];
                    for (int o = 0; o < parts.length; o++) row[o] = Integer.parseInt(parts[o].trim());
                    resList.add(row);
                }
                i = j + 1;
            } else i++;
        }
        int[][] res = new int[resList.size()][];
        for (int k = 0; k < resList.size(); k++) res[k] = resList.get(k);
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            String f_str = sc.next();
            int src = sc.nextInt();
            int dst = sc.nextInt();
            int k = sc.nextInt();
            int[][] flights = parse2DArray(f_str);
            Solution sol = new Solution();
            System.out.println(sol.findCheapestPrice(n, flights, src, dst, k));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 5) {
    let n = parseInt(input[0]);
    let flights = JSON.parse(input[1]);
    let src = parseInt(input[2]);
    let dst = parseInt(input[3]);
    let k = parseInt(input[4]);
    console.log(findCheapestPrice(n, flights, src, dst, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int k) {
    // User logic here
    return -1;
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
    int n, src, dst, k;
    char arr_str[100000];
    if (scanf("%d %99999s %d %d %d", &n, arr_str, &src, &dst, &k) == 5) {
        int sz;
        int* colsz;
        int** flights = parse2DArray(arr_str, &sz, &colsz);
        printf("%d\\n", findCheapestPrice(n, flights, sz, colsz, src, dst, k));
        for(int i=0; i<sz; i++) free(flights[i]);
        free(flights);
        free(colsz);
    }
    return 0;
}"""
    }

    def solve(n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            tmpPrices = list(prices)
            for s, d, p in flights:
                if prices[s] != float('inf') and prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float('inf') else -1

    test_cases_data = [
        (4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1),
        (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),
        (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0),
        (5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2),
        (3, [[0,1,2],[1,2,1],[2,0,10]], 1, 0, 1),
        (10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 6, 0, 7),
        (2, [[0,1,10]], 0, 1, 0),
        (2, [[0,1,10]], 1, 0, 0),
        (4, [[0,1,1],[1,2,1],[2,3,1]], 0, 3, 1),
        (4, [[0,1,1],[1,2,1],[2,3,1]], 0, 3, 2)
    ]

    test_cases = []
    for i, (n, flights, src, dst, k) in enumerate(test_cases_data):
        inp = f"{n}\n{json.dumps(flights).replace(' ', '')}\n{src}\n{dst}\n{k}"
        out = str(solve(n, flights, src, dst, k))
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
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph", "Dynamic Programming", "Shortest Path"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
