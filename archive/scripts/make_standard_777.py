import json
import os

def generate_json():
    problem_id = 777
    title = "Swap Adjacent in LR String"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>777. Swap Adjacent in LR String</h3>
<p>In a string composed of <code>'L'</code>, <code>'R'</code>, and <code>'X'</code> characters, like <code>"RXXLRXRXL"</code>, a move consists of either replacing one occurrence of <code>"XL"</code> with <code>"LX"</code>, or replacing one occurrence of <code>"RX"</code> with <code>"XR"</code>. Given the starting string <code>start</code> and the ending string <code>end</code>, return <code>true</code> if and only if there exists a sequence of moves to transform one string to the other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> start = "RXXLRXRXL", end = "XRLXXRRLX"
<strong>Output:</strong> true
<strong>Explanation:</strong>
We can transform start to end following these steps:
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> start = "X", end = "L"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= start.length&nbsp;&lt;= 10<sup>4</sup></code></li>
    <li><code>start.length == end.length</code></li>
    <li>Both <code>start</code> and <code>end</code> will only consist of characters in <code>'L'</code>, <code>'R'</code>, and&nbsp;<code>'X'</code>.</li>
</ul>"""

    input_format = "Two lines of input.\nLine 1: string `start`\nLine 2: string `end`"
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= start.length <= 10^4",
        "start.length == end.length",
        "Both strings consist of 'L', 'R', and 'X' only"
    ]

    explanation = """First, without the 'X's, the sequence of 'L's and 'R's in both strings must be identical. An 'L' can only move left (swap with an 'X' to its left), so its index in `start` must be >= its index in `end`. An 'R' can only move right, so its index in `start` must be <= its index in `end`."""

    answer = """class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        p1, p2 = 0, 0
        while p1 < len(start) and p2 < len(end):
            while p1 < len(start) and start[p1] == 'X':
                p1 += 1
            while p2 < len(end) and end[p2] == 'X':
                p2 += 1
                
            if p1 == len(start) or p2 == len(end):
                return p1 == len(start) and p2 == len(end)
                
            if start[p1] != end[p2]:
                return False
                
            if start[p1] == 'L' and p1 < p2:
                return False
            if start[p1] == 'R' and p1 > p2:
                return False
                
            p1 += 1
            p2 += 1
            
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        start = json.loads(lines[0]) if lines[0].startswith('"') else lines[0]
        end = json.loads(lines[1]) if lines[1].startswith('"') else lines[1]
        
        if type(start) == str and start.startswith('"'): start = start[1:-1]
        if type(end) == str and end.startswith('"'): end = end[1:-1]
            
        sol = Solution()
        print("true" if sol.canTransform(start, end) else "false")""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool canTransform(string start, string end) {
        // User logic here
        return false;
    }
};

int main() {
    string start, end;
    if (cin >> start >> end) {
        if (start.front() == '"') start = start.substr(1, start.length() - 2);
        if (end.front() == '"') end = end.substr(1, end.length() - 2);
        Solution sol;
        cout << (sol.canTransform(start, end) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean canTransform(String start, String end) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String start = sc.next();
            if (sc.hasNext()) {
                String end = sc.next();
                if (start.startsWith("\\"")) start = start.substring(1, start.length() - 1);
                if (end.startsWith("\\"")) end = end.substring(1, end.length() - 1);
                Solution sol = new Solution();
                System.out.println(sol.canTransform(start, end) ? "true" : "false");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} start
 * @param {string} end
 * @return {boolean}
 */
var canTransform = function(start, end) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    let start = input[0];
    let end = input[1];
    if (start.startsWith('"')) start = JSON.parse(start);
    if (end.startsWith('"')) end = JSON.parse(end);
    console.log(canTransform(start, end) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool canTransform(char* start, char* end) {
    // User logic here
    return false;
}

int main() {
    char start[10005], end[10005];
    if (scanf("%10004s %10004s", start, end) == 2) {
        char *s = start, *e = end;
        int sl = strlen(start), el = strlen(end);
        if (sl >= 2 && start[0] == '"') { start[sl-1] = '\\0'; s = start + 1; }
        if (el >= 2 && end[0] == '"') { end[el-1] = '\\0'; e = end + 1; }
        printf("%s\\n", canTransform(s, e) ? "true" : "false");
    }
    return 0;
}"""
    }

    def solve(start, end):
        if start.replace("X", "") != end.replace("X", ""):
            return False
        p1, p2 = 0, 0
        while p1 < len(start) and p2 < len(end):
            while p1 < len(start) and start[p1] == 'X':
                p1 += 1
            while p2 < len(end) and end[p2] == 'X':
                p2 += 1
            if p1 == len(start) or p2 == len(end):
                return p1 == len(start) and p2 == len(end)
            if start[p1] != end[p2]:
                return False
            if start[p1] == 'L' and p1 < p2:
                return False
            if start[p1] == 'R' and p1 > p2:
                return False
            p1 += 1
            p2 += 1
        return True

    test_cases_data = [
        ("RXXLRXRXL", "XRLXXRRLX"),
        ("X", "L"),
        ("XXRXXLXXXX", "XXXXRXXLXX"),
        ("RXXL", "XRLX"),
        ("XRR", "RX"),
        ("L", "X"),
        ("RL", "LR"),
        ("XXXXXLXXXX", "LXXXXXXXXX"),
        ("RX", "XR"),
        ("XXXXXL", "LXXXXX")
    ]

    test_cases = []
    for i, (s, e) in enumerate(test_cases_data):
        inp = json.dumps(s) + "\\n" + json.dumps(e)
        out = "true" if solve(s, e) else "false"
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
