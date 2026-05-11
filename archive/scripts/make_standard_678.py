import json
import os

def generate_json():
    problem_id = 678
    title = "Valid Parenthesis String"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>678. Valid Parenthesis String</h3>
<p>Given a string <code>s</code> containing only three types of characters: <code>'('</code>, <code>')'</code> and <code>'*'</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is <strong>valid</strong></em>.</p>

<p>The following rules define a <strong>valid</strong> string:</p>

<ul>
    <li>Any left parenthesis <code>'('</code> must have a corresponding right parenthesis <code>')'</code>.</li>
    <li>Any right parenthesis <code>')'</code> must have a corresponding left parenthesis <code>'('</code>.</li>
    <li>Left parenthesis <code>'('</code> must go before the corresponding right parenthesis <code>')'</code>.</li>
    <li><code>'*'</code> could be treated as a single right parenthesis <code>')'</code> or a single left parenthesis <code>'('</code> or an empty string <code>""</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 100</code></li>
    <li><code>s[i]</code> is <code>'('</code>, <code>')'</code> or <code>'*'</code>.</li>
</ul>"""

    input_format = "A single line: a JSON string `s`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= s.length <= 100",
        "s[i] is '(', ')' or '*'"
    ]

    explanation = """Track the range of possible open-paren counts [lo, hi]. On '(', both lo and hi increase. On ')', both decrease. On '*', lo decreases (treat as ')') and hi increases (treat as '('). Clamp lo to 0 (can't go negative). If hi < 0 at any point, return false. At end, return lo == 0."""

    answer = """class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1; hi += 1
            elif c == ')':
                lo -= 1; hi -= 1
            else:  # '*'
                lo -= 1; hi += 1
            if hi < 0: return False
            lo = max(lo, 0)
        return lo == 0"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def checkValidString(self, s: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print("true" if sol.checkValidString(s) else "false")""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
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
        cout << (sol.checkValidString(input) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean checkValidString(String s) {
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
            System.out.println(sol.checkValidString(raw) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const s = JSON.parse(input);
    console.log(checkValidString(s) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool checkValidString(char* s) {
    // User logic here
    return false;
}

int main() {
    char input[200];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char s[200];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(s, input + 1, len - 2);
            s[len - 2] = '\\0';
        } else {
            strcpy(s, input);
        }
        printf("%s\\n", checkValidString(s) ? "true" : "false");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"()"', "expected_output": "true", "is_sample": True},
        {"input": '"(*)"', "expected_output": "true", "is_sample": True},
        {"input": '"(*))"', "expected_output": "true", "is_sample": True},
        {"input": '"(((*"', "expected_output": "false", "is_sample": False},
        {"input": '"*"', "expected_output": "true", "is_sample": False},
        {"input": '"***"', "expected_output": "true", "is_sample": False},
        {"input": '"(**)"', "expected_output": "true", "is_sample": False},
        {"input": '")("', "expected_output": "false", "is_sample": False},
        {"input": '"' + "(" * 50 + "*" * 50 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "(" * 51 + "*" * 50 + '"', "expected_output": "false", "is_sample": False}
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
        "topics": ["String", "Dynamic Programming", "Stack", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
