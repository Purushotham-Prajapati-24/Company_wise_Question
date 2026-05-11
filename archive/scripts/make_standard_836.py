import json
import os

def generate_json():
    problem_id = 836
    title = "Rectangle Overlap"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>836. Rectangle Overlap</h3>
<p>An axis-aligned rectangle is represented as a list <code>[x1, y1, x2, y2]</code>, where <code>(x1, y1)</code> is the coordinate of its bottom-left corner, and <code>(x2, y2)</code> is the coordinate of its top-right corner. Its edges are parallel to the X and Y axes.</p>

<p>Two rectangles overlap if the area of their intersection is <strong>positive</strong>. To be clear, two rectangles that only touch at the corner or edges do not overlap.</p>

<p>Given two axis-aligned rectangles <code>rec1</code> and <code>rec2</code>, return <code>true</code><em> if they overlap, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rec1 = [0,0,2,2], rec2 = [1,1,3,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rec1 = [0,0,1,1], rec2 = [1,0,2,1]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rec1 = [0,0,1,1], rec2 = [2,2,3,3]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>rec1.length == 4</code></li>
    <li><code>rec2.length == 4</code></li>
    <li><code>-10<sup>9</sup> &lt;= rec1[i], rec2[i] &lt;= 10<sup>9</sup></code></li>
    <li><code>rec1</code> and <code>rec2</code> represent a valid rectangle with a non-zero area (i.e., <code>x1 &lt; x2</code> and <code>y1 &lt; y2</code>).</li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `rec1`\nLine 2: JSON array `rec2`"
    output_format = "A boolean string 'true' or 'false'."

    constraints = [
        "-10^9 <= rec1[i], rec2[i] <= 10^9"
    ]

    explanation = """To overlap, one rectangle must not be completely to the left, right, top, or bottom of the other. The overlap condition is: `max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])` and `max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])`."""

    answer = """class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and
                min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]))"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        rec1 = json.loads(raw[0].strip())
        rec2 = json.loads(raw[1].strip())
        sol = Solution()
        print('true' if sol.isRectangleOverlap(rec1, rec2) else 'false')""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        // User logic here
        return false;
    }
};

vector<int> parseArray(string s) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (isdigit(s[i]) || s[i] == '-') {
            int val, off=0;
            auto sub = s.substr(i);
            sscanf(sub.c_str(), "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string s1, s2;
    if (cin >> s1 >> s2) {
        auto r1 = parseArray(s1);
        auto r2 = parseArray(s2);
        Solution sol;
        cout << (sol.isRectangleOverlap(r1, r2) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[] parseArray(String s) {
        s = s.substring(1, s.length()-1);
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i=0; i<parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[] r1 = parseArray(sc.next());
            if (sc.hasNext()) {
                int[] r2 = parseArray(sc.next());
                Solution sol = new Solution();
                System.out.println(sol.isRectangleOverlap(r1, r2));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    console.log(isRectangleOverlap(JSON.parse(input[0]), JSON.parse(input[1])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size) {
    // User logic here
    return false;
}

int main() {
    int r1[4], r2[4];
    if (scanf("[%d,%d,%d,%d] [%d,%d,%d,%d]", &r1[0], &r1[1], &r1[2], &r1[3], &r2[0], &r2[1], &r2[2], &r2[3]) == 8) {
        printf("%s\\n", isRectangleOverlap(r1, 4, r2, 4) ? "true" : "false");
    }
    return 0;
}"""
    }

    def solve(rec1, rec2):
        return (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and
                min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]))

    test_cases_data = [
        ([0,0,2,2], [1,1,3,3]),
        ([0,0,1,1], [1,0,2,1]),
        ([0,0,1,1], [2,2,3,3]),
        ([0,0,10,10], [1,1,2,2]),
        ([0,0,1,1], [0,0,1,1]),
        ([-1,-1,1,1], [0,0,2,2]),
        ([0,0,1,1], [0,2,1,3]),
        ([0,0,1,1], [0.5,0.5,1.5,1.5]),
        ([0,0,1,1], [1,1,2,2]),
        ([0,0,2,2], [2,0,3,3])
    ]

    test_cases = []
    for i, (r1, r2) in enumerate(test_cases_data):
        inp = json.dumps(r1).replace(" ", "") + "\n" + json.dumps(r2).replace(" ", "")
        out = "true" if solve(r1, r2) else "false"
        is_sample = i < 3
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
        "topics": ["Math", "Geometry"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
