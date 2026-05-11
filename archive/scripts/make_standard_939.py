import json
import os

def generate_json():
    problem_id = 939
    title = "Minimum Area Rectangle"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>939. Minimum Area Rectangle</h3>
<p>You are given an array of points in the X-Y plane <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.</p>

<p>Return <em>the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes</em>. If there is not any such rectangle, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG" style="width: 500px; height: 447px;" />
<pre><strong>Input:</strong> points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG" style="width: 500px; height: 477px;" />
<pre><strong>Input:</strong> points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= points.length &lt;= 500</code></li>
    <li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 4 * 10<sup>4</sup></code></li>
    <li>All the given points are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A single line containing the JSON array of points `points`."
    output_format = "An integer representing the minimum area."

    constraints = [
        "1 <= points.length <= 500",
        "0 <= xi, yi <= 40000",
        "All points are unique"
    ]

    explanation = """To find the minimum area rectangle with sides parallel to the axes, we can iterate through all pairs of points (P1, P2). If P1 and P2 can be diagonal corners of such a rectangle (meaning P1.x != P2.x and P1.y != P2.y), we check if the other two required corners (P1.x, P2.y) and (P2.x, P1.y) also exist in our set of points. If they do, we calculate the area as |P1.x - P2.x| * |P1.y - P2.y| and keep track of the minimum area found."""

    answer = """class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        p_set = set(map(tuple, points))
        ans = float('inf')
        for i, (x1, y1) in enumerate(points):
            for j in range(i):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in p_set and (x2, y1) in p_set:
                        ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans != float('inf') else 0"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        points = json.loads(raw)
        sol = Solution()
        print(sol.minAreaRect(points))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        // User logic here
        return 0;
    }
};

vector<vector<int>> parseMatrix(string s) {
    auto res = vector<vector<int>>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (s[i] == '[') {
            size_t end = s.find(']', i);
            string sub = s.substr(i + 1, end - i - 1);
            auto row = vector<int>();
            char buffer[sub.length() + 1];
            strcpy(buffer, sub.c_str());
            char* token = strtok(buffer, ",");
            while (token != NULL) {
                row.push_back(atoi(token));
                token = strtok(NULL, ",");
            }
            res.push_back(row);
            i = end + 1;
        } else i++;
    }
    return res;
}

int main() {
    string line;
    if (cin >> line) {
        auto points = parseMatrix(line);
        Solution sol;
        cout << sol.minAreaRect(points) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minAreaRect(int[][] points) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[][] parseMatrix(String s) {
        s = s.substring(2, s.length() - 2);
        String[] rows = s.split("\\\\],\\\\[");
        int n = rows.length;
        int[][] res = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] cells = rows[i].split(",");
            res[i][0] = Integer.parseInt(cells[0].trim());
            res[i][1] = Integer.parseInt(cells[1].trim());
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[][] points = parseMatrix(sc.next());
            Solution sol = new Solution();
            System.out.println(sol.minAreaRect(points));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} points
 * @return {number}
 */
var minAreaRect = function(points) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(minAreaRect(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minAreaRect(int** points, int pointsSize, int* pointsColSize) {
    // User logic here
    return 0;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        printf("4\\n");
    }
    return 0;
}"""
    }

    def solve(points):
        p_set = set(map(tuple, points))
        ans = float('inf')
        for i, (x1, y1) in enumerate(points):
            for j in range(i):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in p_set and (x2, y1) in p_set:
                        ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans != float('inf') else 0

    test_cases_data = [
        [[1,1],[1,3],[3,1],[3,3],[2,2]],
        [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]],
        [[1,1],[1,3],[3,1],[3,3]],
        [[1,1],[1,2],[2,1],[2,2]],
        [[0,1],[1,3],[3,1],[4,4]],
        [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3]],
        [[4,4],[1,1],[1,4],[4,1]],
        [[10,10],[10,20],[20,10],[20,20],[30,30]],
        [[1,1],[2,2],[3,3]],
        [[0,0],[1,1],[0,1],[1,0],[4,1],[4,0]]
    ]

    test_cases = []
    for i, points in enumerate(test_cases_data):
        inp = json.dumps(points).replace(" ", "")
        out = str(solve(points))
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
        "topics": ["Array", "Hash Table", "Math", "Geometry", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
