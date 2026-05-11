import json
import os

def generate_json():
    problem_id = 1473
    title = "Paint House III"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1473. Paint House III</h3>
<p>There is a row of <code>m</code> houses in a small city, each house must be painted with one of the <code>n</code> colors (labeled from 1 to <code>n</code>), some houses that have been painted last summer should not be painted again.</p>

<p>A neighborhood is a maximal group of continuous houses painted with the same color.</p>

<ul>
	<li>For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].</li>
</ul>

<p>Given an array <code>houses</code>, an <code>m x n</code> matrix <code>cost</code> and an integer <code>target</code> where:</p>

<ul>
	<li><code>houses[i]</code>: is the color of the house <code>i</code>, and <code>0</code> if the house is not painted yet.</li>
	<li><code>cost[i][j]</code>: is the cost of painting house <code>i</code> with the color <code>j + 1</code>.</li>
</ul>

<p>Return <em>the minimum cost of painting all the remaining houses such that there are exactly</em> <code>target</code> <em>neighborhoods</em>. If it is not possible, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
<strong>Output:</strong> 9
<strong>Explanation:</strong> Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
<strong>Output:</strong> 11
<strong>Explanation:</strong> Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the unpainted houses (11 + 0 + 0 + 0 + 0) = 11.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
<strong>Output:</strong> -1
<strong>Explanation:</strong> Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] which is different from target = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == houses.length</code></li>
	<li><code>n == cost[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= target &lt;= m</code></li>
	<li><code>0 &lt;= houses[i] &lt;= n</code></li>
	<li><code>1 &lt;= cost[i][j] &lt;= 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "Five parameters: `houses` (array), `cost` (2D array), `m` (int), `n` (int), `target` (int)."
    output_format = "Integer representing the minimum cost or -1."

    constraints = [
        "1 <= m <= 100",
        "1 <= n <= 20",
        "1 <= target <= m"
    ]

    explanation = """To find the minimum cost to paint houses with exactly `target` neighborhoods:
1. Use 3D Dynamic Programming `dp[i][j][k]`: minimum cost to paint the first `i` houses with `j` neighborhoods and the `i`-th house having color `k`.
2. Transition: 
   - If house `i` is already painted (say color `c`), move from `dp[i-1][j']][k']` to `dp[i][j][c]`.
   - If house `i` is unpainted, iterate through all colors `k` from 1 to `n`. 
   - Increase `j` if the new color `k` is different from the previous color `k'`.
3. Base case: `dp[0][0][0] = 0`, all others infinity.
4. Final answer: `min(dp[m][target][k])` for all `k` from 1 to `n`."""

    answer = """class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        dp = {} # (idx, target, prev_color)
        
        def solve(idx, t, prev_color):
            if t > target: return float('inf')
            if idx == m:
                return 0 if t == target else float('inf')
            if (idx, t, prev_color) in dp:
                return dp[(idx, t, prev_color)]
                
            res = float('inf')
            if houses[idx] != 0:
                new_t = t + (1 if houses[idx] != prev_color else 0)
                res = solve(idx + 1, new_t, houses[idx])
            else:
                for color in range(1, n + 1):
                    new_t = t + (1 if color != prev_color else 0)
                    res = min(res, cost[idx][color-1] + solve(idx + 1, new_t, color))
            
            dp[(idx, t, prev_color)] = res
            return res
            
        ans = solve(0, 0, 0)
        return ans if ans != float('inf') else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        data = json.loads(raw)
        houses, cost, m, n, target = data
        sol = Solution()
        print(sol.minCost(houses, cost, m, n, target))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        // User logic here
        return -1;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<int> houses = j[0].get<vector<int>>();
        vector<vector<int>> cost = j[1].get<vector<vector<int>>>();
        int m = j[2], n = j[3], target = j[4];
        Solution sol;
        cout << sol.minCost(houses, cost, m, n, target) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
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
            int[] houses = mapper.convertValue(data[0], int[].class);
            int[][] cost = mapper.convertValue(data[1], int[][].class);
            int m = (Integer) data[2], n = (Integer) data[3], target = (Integer) data[4];
            System.out.println(new Solution().minCost(houses, cost, m, n, target));
        }
    }
}""",
        "javascript": """var minCost = function(houses, cost, m, n, target) {
    // User logic here
    return -1;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [houses, cost, m, n, target] = JSON.parse(input);
    console.log(minCost(houses, cost, m, n, target));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int minCost(int* houses, int housesSize, int** cost, int costSize, int* costColSize, int m, int n, int target) {
    // User logic here
    return -1;
}

int main() {
    int c;
    // Parsing houses array
    while ((c = getchar()) != EOF && c != '[');
    int h_cap = 100, h_size = 0;
    int* houses = malloc(h_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (h_size >= h_cap) { h_cap *= 2; houses = realloc(houses, h_cap * sizeof(int)); }
        scanf("%d", &houses[h_size++]);
    }
    
    // Parsing cost matrix
    while ((c = getchar()) != EOF && c != '[');
    int c_cap = 100, c_size = 0;
    int** cost = malloc(c_cap * sizeof(int*));
    int* colSizes = malloc(c_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && c != '[' && c != ']');
        if (c == EOF || c == ']') break;
        int r_cap = 10, r_size = 0;
        int* row = malloc(r_cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (r_size >= r_cap) { r_cap *= 2; row = realloc(row, r_cap * sizeof(int)); }
            scanf("%d", &row[r_size++]);
        }
        if (c_size >= c_cap) {
            c_cap *= 2;
            cost = realloc(cost, c_cap * sizeof(int*));
            colSizes = realloc(colSizes, c_cap * sizeof(int));
        }
        cost[c_size] = row;
        colSizes[c_size++] = r_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    
    int m, n, target;
    while ((c = getchar()) != EOF && c != ','); scanf("%d", &m);
    while ((c = getchar()) != EOF && c != ','); scanf("%d", &n);
    while ((c = getchar()) != EOF && c != ','); scanf("%d", &target);
    
    printf("%d\\n", minCost(houses, h_size, cost, c_size, colSizes, m, n, target));
    
    for (int i=0; i<c_size; i++) free(cost[i]);
    free(cost); free(colSizes); free(houses);
    return 0;
}"""
    }

    def solve(houses, cost, m, n, target):
        memo = {}
        def dp(i, target_count, prev_color):
            if target_count < 0: return float('inf')
            if i == m:
                return 0 if target_count == 0 else float('inf')
            state = (i, target_count, prev_color)
            if state in memo: return memo[state]
            
            res = float('inf')
            if houses[i] != 0:
                new_target = target_count - (1 if houses[i] != prev_color else 0)
                res = dp(i + 1, new_target, houses[i])
            else:
                for color in range(1, n + 1):
                    new_target = target_count - (1 if color != prev_color else 0)
                    res = min(res, cost[i][color-1] + dp(i + 1, new_target, color))
            
            memo[state] = res
            return res
            
        ans = dp(0, target, 0)
        return ans if ans != float('inf') else -1

    test_cases_data = [
        [[0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3], # Sample 1
        [[0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3], # Sample 2
        [[3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3], # Sample 3
        [[0,0], [[1,2],[3,4]], 2, 2, 1], # Simple Case
        [[1,1,1], [[10,10],[10,10],[10,10]], 3, 2, 1], # All same
        [[1,2,3], [[1,1,1],[1,1,1],[1,1,1]], 3, 3, 2], # Impossible target
        [[0,0,0], [[5,5],[5,5],[5,5]], 3, 2, 2],
        # Stress tests
        [[0]*100, [[1]*20]*100, 100, 20, 50],
        [[i%21 for i in range(100)], [[10]*20]*100, 100, 20, 10],
        [[0]*100, [[10000]*20]*100, 100, 20, 100]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2], t[3], t[4]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Matrix"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
