import json
import os

def generate_json():
    problem_id = 657
    title = "Robot Return to Origin"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>657. Robot Return to Origin</h3>
<p>There is a robot starting at the position <code>(0, 0)</code>, the origin, on a 2D plane. Given a string <code>moves</code> that represents the move sequence of the robot where <code>moves[i]</code> represents its <code>i<sup>th</sup></code> move. Valid moves are <code>'R'</code> (right), <code>'L'</code> (left), <code>'U'</code> (up), and <code>'D'</code> (down).</p>

<p>Return <code>true</code> <em>if the robot returns to the origin after it finishes all of its moves, or</em> <code>false</code> <em>otherwise</em>.</p>

<p><strong>Note:</strong> The way that the robot is "facing" is irrelevant. <code>'R'</code> will always make the robot move to the right. Also, <code>'R'</code> and <code>'L'</code> are opposite, as are <code>'U'</code> and <code>'D'</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> moves = "UD"
<strong>Output:</strong> true
<strong>Explanation:</strong> The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> moves = "LL"
<strong>Output:</strong> false
<strong>Explanation:</strong> The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= moves.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>moves</code> only contains the characters <code>'U'</code>, <code>'D'</code>, <code>'L'</code> and <code>'R'</code>.</li>
</ul>"""

    input_format = "A single line: a JSON string `moves`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= moves.length <= 2 * 10^4",
        "moves only contains 'U', 'D', 'L', 'R'"
    ]

    explanation = """Count the occurrences of each direction. The robot returns to origin if count('U') == count('D') and count('L') == count('R')."""

    answer = """class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        moves = json.loads(raw)
        sol = Solution()
        print("true" if sol.judgeCircle(moves) else "false")""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool judgeCircle(string moves) {
        // User logic here
        return false;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        cout << (sol.judgeCircle(input) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean judgeCircle(String moves) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() >= 2 && raw.startsWith("\\""))
                raw = raw.substring(1, raw.length() - 1);
            Solution sol = new Solution();
            System.out.println(sol.judgeCircle(raw) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const moves = JSON.parse(input);
    console.log(judgeCircle(moves) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool judgeCircle(char* moves) {
    // User logic here
    return false;
}

int main() {
    char input[50000];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char moves[50000];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(moves, input + 1, len - 2);
            moves[len - 2] = '\\0';
        } else {
            strcpy(moves, input);
        }
        printf("%s\\n", judgeCircle(moves) ? "true" : "false");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"UD"', "expected_output": "true", "is_sample": True},
        {"input": '"LL"', "expected_output": "false", "is_sample": True},
        {"input": '"UDLR"', "expected_output": "true", "is_sample": False},
        {"input": '"UUDDLLRR"', "expected_output": "true", "is_sample": False},
        {"input": '"UUDDLLRRU"', "expected_output": "false", "is_sample": False},
        {"input": '"UUUU"', "expected_output": "false", "is_sample": False},
        {"input": '"RRLLUD"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "UDLR" * 5000 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "U" * 10000 + "D" * 9999 + '"', "expected_output": "false", "is_sample": False},
        {"input": '"' + "UDLR" * 4999 + "UDL" + '"', "expected_output": "false", "is_sample": False}
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
        "topics": ["String", "Simulation"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
