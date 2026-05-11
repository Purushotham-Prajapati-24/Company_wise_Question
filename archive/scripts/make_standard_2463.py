import json
import os

def generate_json():
    problem_id = 2463
    title = "Minimum Total Distance Traveled"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>2463. Minimum Total Distance Traveled</h3>
<p>There are some robots and factories on a 1D line. You are given an integer array <code>robot</code> where <code>robot[i]</code> is the position of the <code>i<sup>th</sup></code> robot. You are also given a 2D integer array <code>factory</code> where <code>factory[j] = [position<sub>j</sub>, limit<sub>j</sub>]</code> indicates that the <code>j<sup>th</sup></code> factory is at <code>position<sub>j</sub></code> and can repair at most <code>limit<sub>j</sub></code> robots.</p>

<p>The positions of each robot are <strong>unique</strong>. The positions of each factory are also <strong>unique</strong>. Note that a robot can be at the same position as a factory initially.</p>

<p>All the robots are initially broken; they keep moving in one direction. The goal is to repair all the robots such that the total distance traveled by all the robots is <strong>minimized</strong>.</p>

<p>Return <em>the minimum total distance traveled by all the robots.</em> The test cases are generated such that all the robots can be repaired.</p>

<p><strong>Note:</strong> All robots move at the same speed. When a robot reaches a factory, it may be repaired, provided the factory has not reached its limit. If a robot is repaired, it stops moving.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/15/example1.jpg" style="width: 500px; height: 172px;" />
<pre>
<strong>Input:</strong> robot = [0,4,6], factory = [[2,2],[6,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory at position 2.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory at position 2.
- The third robot at position 6 will be repaired at the second factory at position 6, as it is already at the same position.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that 4 is the minimum total distance.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/15/example-2.jpg" style="width: 500px; height: 176px;" />
<pre>
<strong>Input:</strong> robot = [1,-1], factory = [[-2,1],[2,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> As shown in the figure:
- The first robot at position 1 moves in the negative direction. It will be repaired at the first factory at position -2.
- The second robot at position -1 moves in the positive direction. It will be repaired at the second factory at position 2.
The total distance is |-2 - 1| + |2 - (-1)| = 6.
It should be noted that the first robot could have also moved to the second factory and the second robot move to the first factory. In this case, the total distance would be |2 - 1| + |-2 - (-1)| = 2, which is the minimum total distance.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= robot.length, factory.length &lt;= 100</code></li>
	<li><code>factory[j].length == 2</code></li>
	<li><code>-10<sup>9</sup> &lt;= robot[i], position<sub>j</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= limit<sub>j</sub> &lt;= robot.length</code></li>
	<li>The input will be generated such that all the robots can be repaired.</li>
</ul>
"""

    input_format = "An array of integers `robot` and a 2D array `factory` provided as `[robot, factory]` in JSON."
    output_format = "A long integer representing the minimum total distance."

    constraints = [
        "1 <= robot.length, factory.length <= 100",
        "robot[i] and factory position up to 10^9",
        "All robots can be repaired"
    ]

    explanation = """To minimize the total distance:
1. Sort both the robots and the factories by their positions. Sorting ensures that robots don't "cross" each other on their way to factories in an optimal assignment.
2. Use dynamic programming `dp[i][j]` representing the minimum distance to repair the first `i` robots using a subset of the first `j` factories.
3. For the `j`-th factory, we can choose to repair `k` robots (where `0 <= k <= limit_j`). If we repair `k` robots at factory `j`, the cost is `sum(dist(robot[m], factory[j]))` for `m` from `i-k` to `i-1` plus `dp[i-k][j-1]`.
4. Transition: `dp[i][j] = min(dp[i-k][j-1] + dist_cost(k robots at factory j))`.
5. Base cases: `dp[0][j] = 0`, others infinity.
6. Final answer: `dp[len(robot)][len(factory)]`."""

    answer = """class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1): dp[0][j] = 0
        
        for j in range(1, n + 1):
            pos, limit = factory[j-1]
            for i in range(m + 1):
                dp[i][j] = dp[i][j-1]
                dist = 0
                for k in range(1, min(i, limit) + 1):
                    dist += abs(robot[i-k] - pos)
                    if dp[i-k][j-1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i-k][j-1] + dist)
        return dp[m][n]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        robot, factory = json.loads(raw)
        sol = Solution()
        print(sol.minimumTotalDistance(robot, factory))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> robot = j[0].get<vector<int>>();
        vector<vector<int>> factory = j[1].get<vector<vector<int>>>();
        Solution sol;
        cout << sol.minimumTotalDistance(robot, factory) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
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
            List<Integer> robot = mapper.convertValue(data[0], List.class);
            int[][] factory = mapper.convertValue(data[1], int[][].class);
            System.out.println(new Solution().minimumTotalDistance(robot, factory));
        }
    }
}""",
        "javascript": """var minimumTotalDistance = function(robot, factory) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [robot, factory] = JSON.parse(input);
    console.log(minimumTotalDistance(robot, factory).toString());
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

long long minimumTotalDistance(int* robot, int robotSize, int** factory, int factorySize, int* factoryColSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int r_cap = 100, r_size = 0;
    int* robot = malloc(r_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (r_size >= r_cap) { r_cap *= 2; robot = realloc(robot, r_cap * sizeof(int)); }
        scanf("%d", &robot[r_size++]);
    }
    while ((c = getchar()) != EOF && c != '[');
    int f_cap = 100, f_size = 0;
    int** factory = malloc(f_cap * sizeof(int*));
    int* colSizes = malloc(f_cap * sizeof(int));
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
        if (f_size >= f_cap) { f_cap *= 2; factory = realloc(factory, f_cap * sizeof(int*)); colSizes = realloc(colSizes, f_cap * sizeof(int)); }
        factory[f_size] = row;
        colSizes[f_size++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    printf("%lld\\n", minimumTotalDistance(robot, r_size, factory, f_size, colSizes));
    return 0;
}"""
    }

    def solve(robot, factory):
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1): dp[0][j] = 0
        for j in range(1, n + 1):
            pos, limit = factory[j-1]
            for i in range(m + 1):
                dp[i][j] = dp[i][j-1]
                dist = 0
                for k in range(1, min(i, limit) + 1):
                    dist += abs(robot[i-k] - pos)
                    if dp[i-k][j-1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i-k][j-1] + dist)
        return dp[m][n]

    test_cases_data = [
        [[0,4,6], [[2,2],[6,2]]],              # Sample 1
        [[1,-1], [[-2,1],[2,1]]],              # Sample 2
        [[10,20], [[15,2]]],                  # One factory
        [[1,2,3], [[1,1],[2,1],[3,1]]],       # Exact match
        [[10,100], [[1,1],[200,1]]],          # Far apart
        [[1,2,3,4], [[0,4]]],
        [[5], [[10,1]]],
        # Stress tests
        [[i*10 for i in range(100)], [[i*10 + 5, 1] for i in range(100)]],
        [[i for i in range(100)], [[1000, 100]]],
        [[10**9, -10**9], [[0, 2]]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0].copy(), [f.copy() for f in t[1]]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Sorting"], "companyIndex": 0
    }

    output_path = f"2401-2600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
