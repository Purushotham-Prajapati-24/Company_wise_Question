import json
import os
from collections import deque

def generate_json():
    problem_id = 675
    title = "Cut Off Trees for Golf Event"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>675. Cut Off Trees for Golf Event</h3>
<p>You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an <code>m x n</code> matrix. In this matrix:</p>

<ul>
    <li><code>0</code> means the cell cannot be walked through.</li>
    <li><code>1</code> represents an empty cell that can be walked through.</li>
    <li>A number greater than <code>1</code> represents a tree in a cell that can be walked through, and this number is the tree's height.</li>
</ul>

<p>In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.</p>

<p>You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes <code>1</code> (an empty cell).</p>

<p>Starting from the point <code>(0, 0)</code>, return <em>the minimum steps you need to walk to cut off all the trees</em>. If you cannot cut off all the trees, return <code>-1</code>.</p>

<p><strong>Note:</strong> The input is generated such that no two trees have the same height, and there is at least one tree needs to be cut off.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> forest = [[1,2,3],[0,0,4],[7,6,5]]
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> forest = [[1,2,3],[0,0,0],[7,6,5]]
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> forest = [[2,3,4],[0,0,5],[8,7,6]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You can follow the same path in Example 1 to cut off all the trees. Note that you can cut off the first tree at (0, 0) before making any steps.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>m == forest.length</code></li>
    <li><code>n == forest[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 50</code></li>
    <li><code>0 &lt;= forest[i][j] &lt;= 10<sup>9</sup></code></li>
    <li>Heights of all trees are <strong>distinct</strong>.</li>
</ul>"""

    input_format = "A single line: a JSON 2D array `forest`."
    output_format = "An integer: minimum steps to cut all trees, or -1."

    constraints = [
        "1 <= m, n <= 50",
        "0 <= forest[i][j] <= 10^9",
        "All tree heights are distinct"
    ]

    explanation = """Sort all trees by height. Starting at (0,0), BFS to each tree in sorted order. If any tree is unreachable, return -1. Accumulate total steps."""

    answer = """from collections import deque
class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        m, n = len(forest), len(forest[0])
        
        def bfs(sr, sc, er, ec):
            if sr == er and sc == ec: return 0
            q = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            while q:
                r, c, dist = q.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0 and (nr, nc) not in visited:
                        if nr == er and nc == ec: return dist + 1
                        visited.add((nr, nc))
                        q.append((nr, nc, dist + 1))
            return -1
        
        trees = sorted((forest[r][c], r, c) for r in range(m) for c in range(n) if forest[r][c] > 1)
        sr, sc = 0, 0
        total = 0
        for _, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)
            if steps == -1: return -1
            total += steps
            sr, sc = tr, tc
        return total"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        forest = json.loads(raw)
        sol = Solution()
        print(sol.cutOffTree(forest))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int cutOffTree(vector<vector<int>>& forest) {
        // User logic here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<vector<int>> forest;
        vector<int> cur;
        bool inRow = false;
        int depth = 0;
        string num = "";
        for (char c : input) {
            if (c == '[') {
                depth++;
                if (depth == 2) { inRow = true; cur.clear(); }
            } else if (c == ']') {
                if (depth == 2 && inRow) {
                    if (!num.empty()) { cur.push_back(stoi(num)); num = ""; }
                    forest.push_back(cur);
                    inRow = false;
                }
                depth--;
            } else if (isdigit(c) && depth == 2) {
                num += c;
            } else if (c == ',' && depth == 2 && !num.empty()) {
                cur.push_back(stoi(num)); num = "";
            }
        }
        Solution sol;
        cout << sol.cutOffTree(forest) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int cutOffTree(List<List<Integer>> forest) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            List<List<Integer>> forest = new ArrayList<>();
            raw = raw.substring(1, raw.length() - 1);
            int depth = 0;
            StringBuilder sb = new StringBuilder();
            for (char c : raw.toCharArray()) {
                if (c == '[') { depth++; if (depth > 0) sb.append(c); }
                else if (c == ']') { if (depth > 0) sb.append(c); depth--;
                    if (depth == 0) {
                        String inner = sb.toString().substring(1, sb.length()-1);
                        List<Integer> row = new ArrayList<>();
                        if (!inner.isEmpty())
                            for (String p : inner.split(",")) row.add(Integer.parseInt(p.trim()));
                        forest.add(row);
                        sb = new StringBuilder();
                    }
                } else if (depth > 0) sb.append(c);
            }
            Solution sol = new Solution();
            System.out.println(sol.cutOffTree(forest));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const forest = JSON.parse(input);
    console.log(cutOffTree(forest));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int cutOffTree(int** forest, int forestSize, int* forestColSize) {
    // User logic here
    return 0;
}

int main() {
    // Complex parsing for 2D arrays; use Python/Java/JS/C++ for this problem
    printf("-1\\n");
    return 0;
}"""
    }

    # Helper to compute BFS steps
    def bfs_steps(forest, sr, sc, er, ec):
        m, n = len(forest), len(forest[0])
        if sr == er and sc == ec: return 0
        q = deque([(sr, sc, 0)])
        visited = {(sr, sc)}
        while q:
            r, c, dist = q.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0 and (nr, nc) not in visited:
                    if nr == er and nc == ec: return dist + 1
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))
        return -1

    def solve(forest):
        m, n = len(forest), len(forest[0])
        trees = sorted((forest[r][c], r, c) for r in range(m) for c in range(n) if forest[r][c] > 1)
        sr, sc = 0, 0
        total = 0
        for _, tr, tc in trees:
            steps = bfs_steps(forest, sr, sc, tr, tc)
            if steps == -1: return -1
            total += steps
            sr, sc = tr, tc
        return total

    test_cases_data = [
        [[1,2,3],[0,0,4],[7,6,5]],
        [[1,2,3],[0,0,0],[7,6,5]],
        [[2,3,4],[0,0,5],[8,7,6]],
        [[54581641,64080174,24346381,69107959],[86374198,61363882,68671278,23708228],[11317, 1,49965779,5298264],[42249, 1,72020160,9874]],
        [[1,2],[3,4]],
        [[1,3,2],[4,5,6],[7,8,9]],
        [[0,0,0],[0,1,0],[0,0,0]],
        [[4,3],[2,1]],
        [[1,1,1],[1,1,1],[1,1,1]],
        [[4,2,3],[0,3,0],[7,0,5]],
    ]

    test_cases = []
    for i, f in enumerate(test_cases_data):
        inp = json.dumps(f)
        out = str(solve(f))
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
        "metadata": {"time_limit_ms": 3000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Breadth-First Search", "Heap (Priority Queue)", "Matrix"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
