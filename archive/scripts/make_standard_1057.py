import json
import os

def generate_json():
    problem_id = 1057
    title = "Campus Bikes"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1057. Campus Bikes</h3>
<p>On a campus represented as a 2D grid, there are <code>N</code> workers and <code>M</code> bikes, with <code>N &lt;= M</code>. Each worker and bike is a 2D coordinate on this grid.</p>

<p>Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest <strong>Manhattan distance</strong> between each other, and assign the bike to that worker. If there are multiple pairs with the same shortest Manhattan distance, we choose the pair with the <strong>smallest worker index</strong>; if there is still a tie, we choose the pair with the <strong>smallest bike index</strong>. We repeat this process until each worker has a bike assigned.</p>

<p>The Manhattan distance between two points <code>P1 = (x1, y1)</code> and <code>P2 = (x2, y2)</code> is <code>Manhattan(P1, P2) = |x1 - x2| + |y1 - y2|</code>.</p>

<p>Return a vector <code>ans</code> of length <code>N</code>, where <code>ans[i]</code> is the index (0-indexed) of the bike that the <code>i<sup>th</sup></code> worker is assigned to.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/06/1261_example_1_v2.png" style="width: 264px; height: 164px;" />
<pre>
<strong>Input:</strong> workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> 
Worker 1 grabs Bike 0 as they are closest (distance 1), and Bike 0 is the smallest index. Worker 0 then grabs Bike 1 (distance 4). As there are only 2 workers and 2 bikes, we are done.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/06/1261_example_2_v2.png" style="width: 264px; height: 264px;" />
<pre>
<strong>Input:</strong> workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
<strong>Output:</strong> [0,2,1]
<strong>Explanation:</strong> 
Worker 0 grabs Bike 0 at distance 1. Since there are multiple pairs with distance 1, worker 0 with bike 0 is the smallest worker index.
Worker 1 grabs Bike 2 at distance 1.
Worker 2 grabs Bike 1 at distance 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] &lt; 1000</code></li>
	<li><code>1 &lt;= workers.length &lt;= bikes.length &lt;= 1000</code></li>
	<li>All worker and bike locations are distinct.</li>
</ul>
"""

    input_format = "Two 2D arrays `workers` and `bikes` provided as `[workers, bikes]` in JSON."
    output_format = "An array of integers representing the bike index for each worker."

    constraints = [
        "0 <= x, y < 1000",
        "1 <= workers.length <= bikes.length <= 1000",
        "All locations are distinct"
    ]

    explanation = """To assign bikes to workers:
1. Calculate all possible (distance, worker_index, bike_index) triplets for all workers and bikes.
2. Sort these triplets primarily by distance, secondarily by worker_index, and tertiarily by bike_index.
3. Use a boolean array `worker_assigned` and `bike_used` to keep track of assignments.
4. Iterate through the sorted triplets and assign the bike if both the worker and bike are available.
5. Store the bike index for each worker in an array and return it."""

    answer = """class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
        n, m = len(workers), len(bikes)
        all_triplets = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                all_triplets.append((dist, i, j))
        
        all_triplets.sort()
        
        ans = [0] * n
        worker_used = [False] * n
        bike_used = [False] * m
        count = 0
        
        for d, w, b in all_triplets:
            if not worker_used[w] and not bike_used[b]:
                ans[w] = b
                worker_used[w] = True
                bike_used[b] = True
                count += 1
                if count == n:
                    break
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        workers, bikes = json.loads(raw)
        sol = Solution()
        print(sol.assignBikes(workers, bikes))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<vector<int>> workers = j[0].get<vector<vector<int>>>();
        vector<vector<int>> bikes = j[1].get<vector<vector<int>>>();
        Solution sol;
        vector<int> res = sol.assignBikes(workers, bikes);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
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
            int[][] workers = mapper.convertValue(data[0], int[][].class);
            int[][] bikes = mapper.convertValue(data[1], int[][].class);
            int[] res = new Solution().assignBikes(workers, bikes);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var assignBikes = function(workers, bikes) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [workers, bikes] = JSON.parse(input);
    const res = assignBikes(workers, bikes);
    console.log(JSON.stringify(res));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* assignBikes(int** workers, int workersSize, int* workersColSize, int** bikes, int bikesSize, int* bikesColSize, int* returnSize) {
    // User logic here
    *returnSize = workersSize;
    return (int*)malloc(workersSize * sizeof(int));
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int w_cap = 128, w_size = 0;
    int** workers = malloc(w_cap * sizeof(int*));
    int* w_cols = malloc(w_cap * sizeof(int));
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
        if (w_size >= w_cap) { w_cap *= 2; workers = realloc(workers, w_cap * sizeof(int*)); w_cols = realloc(w_cols, w_cap * sizeof(int)); }
        workers[w_size] = row;
        w_cols[w_size++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    
    while ((c = getchar()) != EOF && c != '[');
    int b_cap = 128, b_size = 0;
    int** bikes = malloc(b_cap * sizeof(int*));
    int* b_cols = malloc(b_cap * sizeof(int));
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
        if (b_size >= b_cap) { b_cap *= 2; bikes = realloc(bikes, b_cap * sizeof(int*)); b_cols = realloc(b_cols, b_cap * sizeof(int)); }
        bikes[b_size] = row;
        b_cols[b_size++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    
    int rs;
    int* res = assignBikes(workers, w_size, w_cols, bikes, b_size, b_cols, &rs);
    printf("[");
    for (int i = 0; i < rs; i++) printf("%d%s", res[i], i == rs - 1 ? "" : ",");
    printf("]\\n");
    return 0;
}"""
    }

    def solve(workers, bikes):
        n, m = len(workers), len(bikes)
        all_triplets = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                all_triplets.append((dist, i, j))
        all_triplets.sort()
        ans = [0] * n
        worker_used = [False] * n
        bike_used = [False] * m
        count = 0
        for d, w, b in all_triplets:
            if not worker_used[w] and not bike_used[b]:
                ans[w] = b
                worker_used[w] = True
                bike_used[b] = True
                count += 1
                if count == n: break
        return ans

    test_cases_data = [
        [[[0,0],[2,1]], [[1,2],[3,3]]], # Sample 1
        [[[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]], # Sample 2
        [[[0,0],[0,1]], [[0,2],[0,3]]],
        [[[0,0]], [[10,10],[1,1]]],
        [[[1,1],[2,2]], [[1,1],[2,2]]], # Exact overlap
        [[[1,2],[3,4]], [[5,6],[7,8]]],
        [[[0,0],[10,10]], [[0,0],[10,10]]],
        # Stress tests
        [[[i, 0] for i in range(100)], [[0, i] for i in range(100)]],
        [[[0, 0] for _ in range(10)], [[i, j] for i in range(10) for j in range(10)]],
        [[[i, i] for i in range(50)], [[i, i+1] for i in range(100)]]
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
        "topics": ["Array", "Greedy", "Sorting"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
