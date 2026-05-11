import json
import os

def generate_json():
    problem_id = 2940
    title = "Find Building Where Alice and Bob Can Meet"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>2940. Find Building Where Alice and Bob Can Meet</h3>
<p>You are given a <strong>0-indexed</strong> array <code>heights</code> of positive integers, where <code>heights[i]</code> represents the height of the <code>i<sup>th</sup></code> building.</p>

<p>If a person is in building <code>i</code>, they can move to building <code>j</code> if and only if <code>i < j</code> and <code>heights[i] < heights[j]</code>.</p>

<p>You are also given another array <code>queries</code> where <code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>. On the <code>i<sup>th</sup></code> query, Alice is in building <code>a<sub>i</sub></code> while Bob is in building <code>b<sub>i</sub></code>.</p>

<p>Return <em>an array</em> <code>ans</code> <em>where</em> <code>ans[i]</code> <em>is the <strong>index of the leftmost building</strong> where Alice and Bob can meet, or</em> <code>-1</code> <em>if there is no such building.</em></p>

<p>Alice and Bob can move to building <code>j</code> if Alice can move to <code>j</code> and Bob can move to <code>j</code>.</p>

<p><strong>Note:</strong> In the <code>i<sup>th</sup></code> query, if <code>a<sub>i</sub> == b<sub>i</sub></code> or Alice can move directly to Bob's building or vice versa, they can also meet there.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
<strong>Output:</strong> [2,5,-1,5,2]
<strong>Explanation:</strong> In the first query, Alice is in building 0 and Bob is in building 1. They can meet in building 2 because heights[0] &lt; heights[2] and heights[1] &lt; heights[2]. 
In the second query, Alice is in building 0 and Bob is in building 3. They can meet in building 5 because heights[0] &lt; heights[5] and heights[3] &lt; heights[5]. 
In the third query, Alice is in building 2 and Bob is in building 4. Since heights[4] &lt; heights[2], Bob cannot move to Alice's building and Alice cannot move to Bob's building as they must move to a building with a greater index. Since index 2 and 4 are the only buildings Alice and Bob can move to, they cannot meet in any building.
In the fourth query, Alice is in building 3 and Bob is in building 4. They can meet in building 5 because heights[3] &lt; heights[5] and heights[4] &lt; heights[5].
In the fifth query, Alice and Bob are in building 2, so they can meet there. 
Output is [2,5,-1,5,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [5,3,8,2,6], queries = [[0,1],[0,3],[1,2],[1,1]]
<strong>Output:</strong> [2,2,2,1]
<strong>Explanation:</strong> In the first query, Alice is in 0 and Bob is in 1. Since heights[0] &gt; heights[1], they can only meet in a building with index greater than 1 whose height is greater than heights[0]. Building 2 has height 8, which is greater than heights[0] and heights[1], so they can meet there. 
In the second query, Alice is in 0 and Bob is in 3. Since heights[0] &gt; heights[3], they can only meet in a building with index greater than 3 whose height is greater than heights[0]. Building 2 is at index 2, which is less than index 3, so they cannot meet there. Building 4 has height 6, which is greater than heights[0] and heights[3], so they can meet there.
In the third query, Alice is in 1 and Bob is in 2. Since heights[2] &gt; heights[1], they can meet in building 2.
In the fourth query, Alice and Bob are in building 1, so they can meet there.
Output is [2,4,2,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= heights.length - 1</code></li>
</ul>
"""

    input_format = "An array of integers `heights` and a 2D array `queries` provided as `[heights, queries]` in JSON."
    output_format = "An array of integers representing the leftmost building for each query."

    constraints = [
        "1 <= heights.length <= 5 * 10^4",
        "1 <= heights[i] <= 10^9",
        "1 <= queries.length <= 5 * 10^4"
    ]

    explanation = """To find the leftmost building efficiently:
1. For each query `[a, b]`:
   - Let `i = min(a, b)` and `j = max(a, b)`.
   - If `i == j` or `heights[i] < heights[j]`, they can meet at `j`.
   - Otherwise, they need a building `k > j` such that `heights[k] > heights[i]` and `heights[k] > heights[j]`. Since `heights[i] >= heights[j]`, this is equivalent to `heights[k] > heights[i]`.
2. This is a range query problem. We can use a segment tree or a monotonic stack with binary search, or an offline approach with a priority queue.
3. Offline approach:
   - Group queries that need a building `k > j` by their index `j`.
   - Iterate through `heights` from left to right.
   - For each building `idx`, process all queries that were waiting at this `idx`.
   - Use a priority queue to store queries, prioritized by the height they need to exceed.
   - When we reach building `idx`, add all queries waiting at `idx-1` to the priority queue. Actually, the logic is: when we reach building `idx`, check if its height exceeds any waiting queries."""

    answer = """import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        ans = [-1] * len(queries)
        deferred = [[] for _ in range(n)]
        
        for q_idx, (a, b) in enumerate(queries):
            if a > b: a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[q_idx] = b
            else:
                deferred[b].append((heights[a], q_idx))
                
        pq = []
        for i in range(n):
            while pq and pq[0][0] < heights[i]:
                h, q_idx = heapq.heappop(pq)
                ans[q_idx] = i
            for h, q_idx in deferred[i]:
                heapq.heappush(pq, (h, q_idx))
        return ans"""

    boilerplate = {
        "python": """import sys
import json
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        heights, queries = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.leftmostBuildingQueries(heights, queries)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> heights = j[0].get<vector<int>>();
        vector<vector<int>> queries = j[1].get<vector<vector<int>>>();
        Solution sol;
        vector<int> res = sol.leftmostBuildingQueries(heights, queries);
        json out = res;
        cout << out.dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[] leftmostBuildingQueries(int[] heights, int[][] queries) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int[] heights = mapper.convertValue(data[0], int[].class);
            int[][] queries = mapper.convertValue(data[1], int[][].class);
            int[] res = new Solution().leftmostBuildingQueries(heights, queries);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var leftmostBuildingQueries = function(heights, queries) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [heights, queries] = JSON.parse(input);
    console.log(JSON.stringify(leftmostBuildingQueries(heights, queries)).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int* leftmostBuildingQueries(int* heights, int heightsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    // User logic here
    return NULL;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int h_cap = 128, h_size = 0;
    int* heights = malloc(h_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (h_size >= h_cap) { h_cap *= 2; heights = realloc(heights, h_cap * sizeof(int)); }
        scanf("%d", &heights[h_size++]);
    }
    while ((c = getchar()) != EOF && c != '[');
    int q_cap = 128, q_size = 0;
    int** queries = malloc(q_cap * sizeof(int*));
    int* colSizes = malloc(q_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && c != '[' && c != ']');
        if (c == EOF || c == ']') break;
        int row_cap = 2, row_size = 0;
        int* row = malloc(row_cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (row_size >= row_cap) { row_cap *= 2; row = realloc(row, row_cap * sizeof(int)); }
            scanf("%d", &row[row_size++]);
        }
        if (q_size >= q_cap) { q_cap *= 2; queries = realloc(queries, q_cap * sizeof(int*)); colSizes = realloc(colSizes, q_cap * sizeof(int)); }
        queries[q_size] = row;
        colSizes[q_size++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    int retSize;
    int* res = leftmostBuildingQueries(heights, h_size, queries, q_size, colSizes, &retSize);
    printf("[");
    for (int i=0; i<retSize; i++) {
        printf("%d", res[i]);
        if (i < retSize - 1) printf(",");
    }
    printf("]\\n");
    free(heights); for(int i=0; i<q_size; i++) free(queries[i]); free(queries); free(colSizes); free(res);
    return 0;
}"""
    }

    def solve(heights, queries):
        import heapq
        n = len(heights)
        ans = [-1] * len(queries)
        deferred = [[] for _ in range(n)]
        for q_idx, (a, b) in enumerate(queries):
            if a > b: a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[q_idx] = b
            else: deferred[b].append((heights[a], q_idx))
        pq = []
        for i in range(n):
            while pq and pq[0][0] < heights[i]:
                h, q_idx = heapq.heappop(pq)
                ans[q_idx] = i
            for h, q_idx in deferred[i]:
                heapq.heappush(pq, (h, q_idx))
        return ans

    test_cases_data = [
        [[6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]], # Sample 1
        [[5,3,8,2,6], [[0,1],[0,3],[1,2],[1,1]]],        # Sample 2
        [[1,2,3,4,5], [[0,4],[0,0],[1,3]]],
        [[5,4,3,2,1], [[0,4],[0,1],[4,4]]],
        [[1,1,1,1], [[0,1],[1,1],[2,3]]],
        [[10,10,10], [[0,2]]],
        [[1,5,2,6,3,7], [[0,2],[1,3],[2,4]]],
        # Stress tests
        [[1]*50000, [[0, 49999]]],
        [list(range(50000)), [[0, 49999]]],
        [list(range(50000, 0, -1)), [[0, 49999], [49999, 49999]]]
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
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 512, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Binary Search", "Stack", "Heap", "Segment Tree"], "companyIndex": 0
    }

    output_path = f"2801-3000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
