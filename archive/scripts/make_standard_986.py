import json
import os

def generate_json():
    problem_id = 986
    title = "Interval List Intersections"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>986. Interval List Intersections</h3>
<p>You are given two lists of closed intervals, <code>firstList</code> and <code>secondList</code>, where <code>firstList[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> and <code>secondList[j] = [start<sub>j</sub>, end<sub>j</sub>]</code>. Each list of intervals is pairwise <strong>disjoint</strong> and in <strong>sorted order</strong>.</p>

<p>Return <em>the intersection of these two interval lists</em>.</p>

<p>A <strong>closed interval</strong> <code>[a, b]</code> (with <code>a &lt;= b</code>) denotes the set of real numbers <code>x</code> with <code>a &lt;= x &lt;= b</code>.</p>

<p>The <strong>intersection</strong> of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of <code>[1, 3]</code> and <code>[2, 4]</code> is <code>[2, 3]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 700px; height: 194px;" />
<pre><strong>Input:</strong> firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
<strong>Output:</strong> [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> firstList = [[1,3],[5,9]], secondList = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>0 &lt;= firstList.length, secondList.length &lt;= 1000</code></li>
    <li><code>firstList.length + secondList.length &gt;= 1</code></li>
    <li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
    <li><code>end<sub>i</sub> &lt; start<sub>i+1</sub></code></li>
    <li><code>0 &lt;= start<sub>j</sub> &lt; end<sub>j</sub> &lt;= 10<sup>9</sup></code></li>
    <li><code>end<sub>j</sub> &lt; start<sub>j+1</sub></code></li>
</ul>"""

    input_format = "Two lines, each containing a JSON array of intervals."
    output_format = "A JSON array representing the intersection of the two lists."

    constraints = [
        "0 <= firstList.length, secondList.length <= 1000",
        "Disjoint and sorted lists"
    ]

    explanation = """To find the intersection, we use two pointers `i` and `j` to iterate through `firstList` and `secondList`. For each pair of intervals, the intersection exists if `max(start_i, start_j) <= min(end_i, end_j)`. If it does, we record the intersection `[max(start_i, start_j), min(end_i, end_j)]`. Then, we increment the pointer of the interval that ends earlier, as it cannot intersect with any subsequent interval in the other list."""

    answer = """class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # User logic here
        return []

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        l1 = json.loads(lines[0])
        l2 = json.loads(lines[1])
        sol = Solution()
        print(json.dumps(sol.intervalIntersection(l1, l2)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        // User logic here
        return {};
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
            if (!sub.empty()) {
                size_t comma = sub.find(',');
                row.push_back(atoi(sub.substr(0, comma).c_str()));
                row.push_back(atoi(sub.substr(comma + 1).c_str()));
            }
            if (!row.empty()) res.push_back(row);
            i = end + 1;
        } else i++;
    }
    return res;
}

int main() {
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        auto firstList = parseMatrix(line1);
        auto secondList = parseMatrix(line2);
        Solution sol;
        auto res = sol.intervalIntersection(firstList, secondList);
        cout << "[";
        for (int i=0; i<res.size(); ++i) cout << "[" << res[i][0] << "," << res[i][1] << "]" << (i==res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        // User logic here
        return new int[0][0];
    }
}

public class Main {
    static int[][] parseMatrix(String s) {
        if (s.equals("[]")) return new int[0][0];
        s = s.substring(2, s.length() - 2);
        String[] rows = s.split("\\\\],\\\\[");
        int[][] res = new int[rows.length][2];
        for (int i = 0; i < rows.length; i++) {
            String[] cells = rows[i].split(",");
            res[i][0] = Integer.parseInt(cells[0].trim());
            res[i][1] = Integer.parseInt(cells[1].trim());
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[][] l1 = parseMatrix(sc.nextLine());
            int[][] l2 = parseMatrix(sc.nextLine());
            Solution sol = new Solution();
            int[][] res = sol.intervalIntersection(l1, l2);
            System.out.println(Arrays.deepToString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function(firstList, secondList) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    console.log(JSON.stringify(intervalIntersection(JSON.parse(input[0]), JSON.parse(input[1]))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int** intervalIntersection(int** firstList, int firstListSize, int* firstListColSize, int** secondList, int secondListSize, int* secondListColSize, int* returnSize, int** returnColumnSizes) {
    // User logic here
    return NULL;
}

int main() {
    printf("[]\\n");
    return 0;
}"""
    }

    def solve(firstList, secondList):
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi: ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]: i += 1
            else: j += 1
        return ans

    test_cases_data = [
        ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]),
        ([[1,3],[5,9]], []),
        ([], [[4,8],[10,12]]),
        ([[1,7]], [[1,2],[3,4],[5,6]]),
        ([[1,2],[3,4],[5,6]], [[1,7]]),
        ([[0,4]], [[5,10]]),
        ([[1,2]], [[2,3]]),
        ([[1,10]], [[2,3],[5,7]]),
        ([[1,5],[8,10]], [[1,10]]),
        ([[1,3],[5,7],[9,12]], [[2,4],[6,8],[10,11]])
    ]

    test_cases = []
    for i, (l1, l2) in enumerate(test_cases_data):
        inp = json.dumps(l1).replace(" ", "") + "\n" + json.dumps(l2).replace(" ", "")
        out = json.dumps(solve(l1, l2)).replace(" ", "")
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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
