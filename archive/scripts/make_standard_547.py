import json
import os

def generate_json():
    problem_id = 547
    title = "Number of Provinces"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>547. Number of Provinces</h3>
<p>There are <code>n</code> cities. Some of them are connected, while some are not. If city <code>a</code> is connected directly with city <code>b</code>, and city <code>b</code> is connected directly with city <code>c</code>, then city <code>a</code> is connected indirectly with city <code>c</code>.</p>

<p>A <strong>province</strong> is a group of directly or indirectly connected cities and no other cities outside of the group.</p>

<p>You are given an <code>n x n</code> matrix <code>isConnected</code> where <code>isConnected[i][j] = 1</code> if the <code>i<sup>th</sup></code> city and the <code>j<sup>th</sup></code> city are directly connected, and <code>isConnected[i][j] = 0</code> otherwise.</p>

<p>Return <em>the total number of <strong>provinces</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>Input:</strong> isConnected = [[1,1,0],[1,1,0],[0,0,1]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>Input:</strong> isConnected = [[1,0,0],[0,1,0],[0,0,1]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 200</code></li>
    <li><code>n == isConnected.length</code></li>
    <li><code>n == isConnected[i].length</code></li>
    <li><code>isConnected[i][j]</code> is <code>1</code> or <code>0</code>.</li>
    <li><code>isConnected[i][i] == 1</code></li>
    <li><code>isConnected[i][j] == isConnected[j][i]</code></li>
</ul>"""

    input_format = "A single line: a JSON 2D array of integers `isConnected`."
    output_format = "An integer: the number of provinces."

    constraints = [
        "1 <= n <= 200",
        "isConnected[i][j] is 1 or 0",
        "isConnected[i][i] == 1",
        "isConnected[i][j] == isConnected[j][i]"
    ]

    explanation = """Use DFS or Union-Find. Start from each unvisited city and mark all directly/indirectly connected cities as visited — that counts as one province. The answer is the number of times we start a new DFS."""

    answer = """class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        def dfs(city):
            for j in range(n):
                if isConnected[city][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1
        return provinces"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        isConnected = json.loads(raw)
        sol = Solution()
        print(sol.findCircleNum(isConnected))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        // User logic here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<vector<int>> grid;
        vector<int> row;
        int depth = 0;
        size_t p = 0;
        while (p < input.length()) {
            if (input[p] == '[') { depth++; p++; }
            else if (input[p] == ']') {
                depth--;
                if (depth == 1) { grid.push_back(row); row.clear(); }
                p++;
            } else if (isdigit(input[p])) {
                size_t next;
                row.push_back(stoi(input.substr(p), &next));
                p += next;
            } else p++;
        }
        Solution sol;
        cout << sol.findCircleNum(grid) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            // Parse 2D JSON array
            List<List<Integer>> grid = new ArrayList<>();
            List<Integer> row = new ArrayList<>();
            int depth = 0;
            for (int i = 0; i < raw.length(); i++) {
                char c = raw.charAt(i);
                if (c == '[') { depth++; }
                else if (c == ']') {
                    depth--;
                    if (depth == 1) { grid.add(new ArrayList<>(row)); row.clear(); }
                } else if (Character.isDigit(c)) {
                    int end = i;
                    while (end < raw.length() && Character.isDigit(raw.charAt(end))) end++;
                    row.add(Integer.parseInt(raw.substring(i, end)));
                    i = end - 1;
                }
            }
            int n = grid.size();
            int[][] mat = new int[n][n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) mat[i][j] = grid.get(i).get(j);
            Solution sol = new Solution();
            System.out.println(sol.findCircleNum(mat));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const isConnected = JSON.parse(input);
    console.log(findCircleNum(isConnected));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    // User logic here
    return 0;
}

int main() {
    char input[500000];
    if (fgets(input, sizeof(input), stdin)) {
        int nums[40000], ncount = 0, i = 0;
        while (input[i]) {
            if (isdigit(input[i])) {
                int val, off = 0;
                sscanf(input + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                nums[ncount++] = val;
                i += off;
            } else i++;
        }
        int n = 0;
        while (n * n < ncount) n++;
        int** grid = (int**)malloc(n * sizeof(int*));
        int* colSizes = (int*)malloc(n * sizeof(int));
        for (int r = 0; r < n; r++) {
            grid[r] = (int*)malloc(n * sizeof(int));
            colSizes[r] = n;
            for (int c = 0; c < n; c++) grid[r][c] = nums[r * n + c];
        }
        printf("%d\\n", findCircleNum(grid, n, colSizes));
        for (int r = 0; r < n; r++) free(grid[r]);
        free(grid); free(colSizes);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[[1,1,0],[1,1,0],[0,0,1]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1,0,0],[0,1,0],[0,0,1]]", "expected_output": "3", "is_sample": True},

        # Five Diverse Cases
        {"input": "[[1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,1],[1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1,1,1],[1,1,1],[1,1,1]]", "expected_output": "1", "is_sample": False},

        # Three Stress Test Cases (n=200 fully connected / fully disconnected)
        {"input": "[[" + "],[".join([",".join(["1"] * 200)] * 200) + "]]", "expected_output": "1", "is_sample": False},
        {"input": "[[" + "],[".join([",".join(["1" if i == j else "0" for j in range(200)]) for i in range(200)]) + "]]", "expected_output": "200", "is_sample": False},
        {"input": "[[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]", "expected_output": "2", "is_sample": False}
    ]

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

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
