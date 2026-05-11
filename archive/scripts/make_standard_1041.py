import json
import os

def generate_json():
    problem_id = 1041
    title = "Robot Bounded In Circle"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1041. Robot Bounded In Circle</h3>
<p>On an infinite 2D plane, a robot initially stands at <code>(0, 0)</code> and faces north. The robot can receive one of three instructions:</p>

<ul>
	<li><code>"G"</code>: go straight 1 unit;</li>
	<li><code>"L"</code>: turn 90 degrees to the left;</li>
	<li><code>"R"</code>: turn 90 degrees to the right.</li>
</ul>

<p>The robot performs the <code>instructions</code> given in order, and repeats them forever.</p>

<p>Return <code>true</code> if and only if there exists a circle in the plane such that the robot never leaves the circle.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> instructions = "GGLLGG"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> instructions = "GG"
<strong>Output:</strong> false
<strong>Explanation:</strong> The robot moves north indefinitely.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> instructions = "GL"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves from (0,0) -&gt; (0,1) -&gt; (-1,1) -&gt; (-1,0) -&gt; (0,0), and repeated instructions keep it in this square.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= instructions.length &lt;= 100</code></li>
	<li><code>instructions[i]</code> is <code>'G'</code>, <code>'L'</code> or <code>'R'</code>.</li>
</ul>"""

    input_format = "A single string `instructions`."
    output_format = "`true` if the robot is bounded by a circle, otherwise `false`."

    constraints = [
        "1 <= instructions.length <= 100",
        "instructions[i] is 'G', 'L' or 'R'"
    ]

    explanation = """After executing the sequence once, the robot is bounded if:
1. It is back at the origin (0, 0).
2. It is NOT facing north. (If it's facing any other direction, it will return to (0,0) after 2 or 4 repetitions)."""

    answer = """class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1 # north
        for i in instructions:
            if i == 'G':
                x, y = x + dx, y + dy
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)"""

    boilerplate = {
        "python": """import sys

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip().strip('"')
    if raw:
        sol = Solution()
        print("true" if sol.isRobotBounded(raw) else "false")""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isRobotBounded(string instructions) {
        // User logic here
        return false;
    }
};

int main() {
    string instructions;
    if (cin >> instructions) {
        if (instructions[0] == '"') instructions = instructions.substr(1, instructions.length() - 2);
        Solution sol;
        cout << (sol.isRobotBounded(instructions) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isRobotBounded(String instructions) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next().replace("\\"", "");
            System.out.println(new Solution().isRobotBounded(s));
        }
    }
}""",
        "javascript": """var isRobotBounded = function(instructions) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().replace(/\\"/g, "");
if (input) {
    console.log(isRobotBounded(input));
}""",
        "c": """#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isRobotBounded(char* instructions) {
    // User logic here
    return false;
}

int main() {
    char s[200];
    if (scanf("%s", s) == 1) {
        char *p = s;
        if (*p == '"') {
            p++;
            s[strlen(s)-1] = '\\0';
        }
        printf("%s\\n", isRobotBounded(p) ? "true" : "false");
    }
    return 0;
}"""
    }

    def solve(instructions):
        x, y = 0, 0
        dx, dy = 0, 1
        for i in instructions:
            if i == 'G': x, y = x + dx, y + dy
            elif i == 'L': dx, dy = -dy, dx
            else: dx, dy = dy, -dx
        return (x == 0 and y == 0) or (dx, dy) != (0, 1)

    test_cases_data = ["GGLLGG", "GG", "GL", "G", "LLLL", "RRRR", "GLGLG", "GR", "GGLR", "GGLL"]
    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = f'"{t}"'
        out = "true" if solve(t) else "false"
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "String", "Simulation"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
