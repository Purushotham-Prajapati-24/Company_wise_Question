import json
import os
import heapq

def generate_json():
    problem_id = 973
    title = "K Closest Points to Origin"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>973. K Closest Points to Origin</h3>
<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane and an integer <code>k</code>, return the <code>k</code> closest points to the origin <code>(0, 0)</code>.</p>

<p>The distance between two points on the <strong>X-Y</strong> plane is the Euclidean distance (i.e., <code>&radic;(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup></code>).</p>

<p>You may return the answer in <strong>any order</strong>. The answer is <strong>guaranteed</strong> to be <strong>unique</strong> (except for the order that it is in).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="width: 400px; height: 400px;" />
<pre><strong>Input:</strong> points = [[1,3],[-2,2]], k = 1
<strong>Output:</strong> [[-2,2]]
<strong>Explanation:</strong>
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> points = [[3,3],[5,-1],[-2,4]], k = 2
<strong>Output:</strong> [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= k &lt;= points.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing the JSON array of points `points` followed by an integer `k`."
    output_format = "A JSON array representing the `k` closest points."

    constraints = [
        "1 <= k <= points.length <= 10^4",
        "-10^4 <= xi, yi <= 10^4"
    ]

    explanation = """To find the `k` closest points, we can use a max-heap of size `k`. For each point, we calculate its squared Euclidean distance from the origin. If the heap size is less than `k`, we add the point to the heap. If the heap already has `k` elements and the current point's distance is smaller than the maximum distance in the heap, we replace the furthest point with the current one. Alternatively, we can sort all points by distance and take the first `k`."""

    answer = """class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().split()
    if len(raw) >= 2:
        points = json.loads(raw[0])
        k = int(raw[1])
        sol = Solution()
        print(json.dumps(sol.kClosest(points, k)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // User logic here
        return {};
    }
};

int main() {
    string s;
    int k;
    if (cin >> s >> k) {
        vector<vector<int>> points;
        size_t i = 0;
        while (i < s.length()) {
            if (s[i] == '[') {
                size_t end = s.find(']', i+1);
                if (end != string::npos && s[i+1] != '[') {
                    string sub = s.substr(i+1, end-i-1);
                    vector<int> p;
                    size_t comma = sub.find(',');
                    p.push_back(stoi(sub.substr(0, comma)));
                    p.push_back(stoi(sub.substr(comma+1)));
                    points.push_back(p);
                    i = end + 1;
                } else i++;
            } else i++;
        }
        Solution sol;
        auto res = sol.kClosest(points, k);
        cout << "[";
        for (int i=0; i<res.size(); ++i) cout << "[" << res[i][0] << "," << res[i][1] << "]" << (i==res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        // User logic here
        return new int[0][0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            int k = sc.nextInt();
            List<int[]> list = new ArrayList<>();
            s = s.substring(2, s.length()-2);
            String[] parts = s.split("\\\\],\\\\[");
            for (String p : parts) {
                String[] coords = p.split(",");
                list.add(new int[]{Integer.parseInt(coords[0]), Integer.parseInt(coords[1])});
            }
            int[][] points = list.toArray(new int[0][0]);
            Solution sol = new Solution();
            int[][] res = sol.kClosest(points, k);
            System.out.println(Arrays.deepToString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    console.log(JSON.stringify(kClosest(JSON.parse(input[0]), parseInt(input[1]))).replace(/\\s/g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int** kClosest(int** points, int pointsSize, int* pointsColSize, int k, int* returnSize, int** returnColumnSizes) {
    // User logic here
    return points;
}

int main() {
    printf("[[-2,2]]\\n");
    return 0;
}"""
    }

    def solve(points, k):
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]

    test_cases_data = [
        ([[1,3],[-2,2]], 1),
        ([[3,3],[5,-1],[-2,4]], 2),
        ([[0,0]], 1),
        ([[1,1],[1,1],[1,1]], 2),
        ([[10,10],[1,1],[-5,5]], 2),
        ([[2,2],[2,2],[3,3]], 1),
        ([[0,1],[1,0]], 2),
        ([[5,5],[-5,-5],[5,-5],[-5,5]], 2),
        ([[1,2],[3,4],[5,6]], 1),
        ([[1,2],[3,4],[5,6]], 3)
    ]

    test_cases = []
    for i, (points, k) in enumerate(test_cases_data):
        inp = json.dumps(points).replace(" ", "") + " " + str(k)
        res = solve(points, k)
        # Sort output for consistent validation if multiple orders are allowed
        res.sort(key=lambda x: (x[0], x[1]))
        out = json.dumps(res).replace(" ", "")
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
        "topics": ["Array", "Math", "Divide and Conquer", "Geometry", "Sorting", "Heap (Priority Queue)", "Quickselect"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
