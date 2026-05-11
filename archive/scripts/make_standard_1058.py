import json
import os

def generate_json():
    problem_id = 1058
    title = "Campus Bikes II"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1058. Campus Bikes II</h3>
<p>On a campus represented as a 2D grid, there are <code>N</code> workers and <code>M</code> bikes, with <code>N &lt;= M</code>. Each worker and bike is a 2D coordinate on this grid.</p>

<p>Our goal is to assign a bike to each worker such that the <strong>sum of Manhattan distances</strong> between each worker and their assigned bike is <strong>minimized</strong>.</p>

<p>The Manhattan distance between two points <code>P1 = (x1, y1)</code> and <code>P2 = (x2, y2)</code> is <code>Manhattan(P1, P2) = |x1 - x2| + |y1 - y2|</code>.</p>

<p>Return the minimum possible sum of Manhattan distances.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/06/1261_example_1_v2.png" style="width: 264px; height: 164px;" />
<pre>
<strong>Input:</strong> workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
We assign bike 0 to worker 0 (distance 3) and bike 1 to worker 1 (distance 3). The total distance is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/06/1261_example_2_v2.png" style="width: 264px; height: 264px;" />
<pre>
<strong>Input:</strong> workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
We assign bike 0 to worker 0 (distance 1), bike 2 to worker 1 (distance 1), and bike 1 to worker 2 (distance 2). The total distance is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= workers.length &lt;= bikes.length &lt;= 10</code></li>
	<li><code>0 &lt;= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] &lt; 1000</code></li>
	<li>All worker and bike locations are distinct.</li>
</ul>
"""

    input_format = "Two 2D arrays `workers` and `bikes` provided as `[workers, bikes]` in JSON."
    output_format = "An integer representing the minimum sum of Manhattan distances."

    constraints = [
        "1 <= n <= m <= 10",
        "0 <= coordinates < 1000"
    ]

    explanation = """To find the minimum sum of Manhattan distances:
1. Since the number of workers and bikes is small (up to 10), we can use DP with bitmasking.
2. Define `dp[mask]` as the minimum distance for assigning bikes to the first `popcount(mask)` workers, using the bikes indicated by `mask`.
3. Base case: `dp[0] = 0`.
4. Transitions: For each mask, if `popcount(mask) < n`, the next worker is `w = popcount(mask)`. For each unused bike `b`, update `dp[mask | (1 << b)] = min(dp[mask | (1 << b)], dp[mask] + dist(workers[w], bikes[b]))`.
5. The answer is the minimum value in `dp` among masks with `popcount(mask) == n`."""

    answer = """class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        n, m = len(workers), len(bikes)
        # dp[mask] is min sum of distances for popcount(mask) workers
        dp = [float('inf')] * (1 << m)
        dp[0] = 0
        
        for mask in range(1 << m):
            w_idx = bin(mask).count('1')
            if w_idx >= n:
                continue
            
            for b_idx in range(m):
                if not (mask & (1 << b_idx)):
                    new_mask = mask | (1 << b_idx)
                    dist = abs(workers[w_idx][0] - bikes[b_idx][0]) + abs(workers[w_idx][1] - bikes[b_idx][1])
                    dp[new_mask] = min(dp[new_mask], dp[mask] + dist)
        
        ans = float('inf')
        for mask in range(1 << m):
            if bin(mask).count('1') == n:
                ans = min(ans, dp[mask])
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        # User logic here
        return 0

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
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<vector<int>> workers = j[0].get<vector<vector<int>>>();
        vector<vector<int>> bikes = j[1].get<vector<vector<int>>>();
        Solution sol;
        cout << sol.assignBikes(workers, bikes) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int assignBikes(int[][] workers, int[][] bikes) {
        // User logic here
        return 0;
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
            System.out.println(new Solution().assignBikes(workers, bikes));
        }
    }
}""",
        "javascript": """var assignBikes = function(workers, bikes) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [workers, bikes] = JSON.parse(input);
    console.log(assignBikes(workers, bikes));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int assignBikes(int** workers, int workersSize, int* workersColSize, int** bikes, int bikesSize, int* bikesColSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int w_cap = 12, w_size = 0;
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
    int b_cap = 12, b_size = 0;
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
    printf("%d\\n", assignBikes(workers, w_size, w_cols, bikes, b_size, b_cols));
    return 0;
}"""
    }

    def solve(workers, bikes):
        n, m = len(workers), len(bikes)
        dp = [float('inf')] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            w_idx = bin(mask).count('1')
            if w_idx >= n: continue
            for b_idx in range(m):
                if not (mask & (1 << b_idx)):
                    new_mask = mask | (1 << b_idx)
                    dist = abs(workers[w_idx][0] - bikes[b_idx][0]) + abs(workers[w_idx][1] - bikes[b_idx][1])
                    dp[new_mask] = min(dp[new_mask], dp[mask] + dist)
        ans = float('inf')
        for mask in range(1 << m):
            if bin(mask).count('1') == n: ans = min(ans, dp[mask])
        return ans

    test_cases_data = [
        [[[0,0],[2,1]], [[1,2],[3,3]]], # Sample 1
        [[[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]], # Sample 2
        [[[0,0]], [[1,1]]],
        [[[1,1]], [[0,0]]],
        [[[1,1]], [[1,1]]],
        [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]]],
        [[[0,0],[1,1]], [[1,0],[0,1],[2,2]]],
        # Stress tests
        [[[i, 0] for i in range(10)], [[0, i] for i in range(10)]],
        [[[0, 0] for _ in range(10)], [[i, i] for i in range(10)]],
        [[[5,5]]*10, [[i,j] for i in range(3) for j in range(4)][:10]]
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
        "topics": ["Array", "Dynamic Programming", "Bitmask"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
