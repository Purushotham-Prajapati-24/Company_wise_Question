import json
import os

def generate_json():
    problem_id = 844
    title = "Backspace String Compare"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>844. Backspace String Compare</h3>
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if they are equal when both are typed into empty text editors</em>. <code>'#'</code> means a backspace character.</p>

<p>Note that after backspacing an empty text, the text will continue empty.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ab#c", t = "ad#c"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "ac".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "ab##", t = "c#d#"
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become "".
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "a#c", t = "b"
<strong>Output:</strong> false
<strong>Explanation:</strong> s becomes "c" while t becomes "b".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length, t.length &lt;= 200</code></li>
    <li><code>s</code> and <code>t</code> consist of lowercase English letters and <code>'#'</code> characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it in <code>O(n)</code> time and <code>O(1)</code> space?</p>"""

    input_format = "Two lines:\nLine 1: string `s`\nLine 2: string `t`"
    output_format = "A boolean string 'true' or 'false'."

    constraints = [
        "1 <= s.length, t.length <= 200",
        "Characters are lowercase letters or '#'"
    ]

    explanation = """To compare the strings, we can simulate the typing process using a stack. For each character, if it's not '#', push it onto the stack. If it is '#', pop from the stack if it's not empty. Finally, compare the resulting strings. Alternatively, use a two-pointer approach from the end of the strings for O(1) space."""

    answer = """class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        s = raw[0].strip().strip('"')
        t = raw[1].strip().strip('"')
        sol = Solution()
        print('true' if sol.backspaceCompare(s, t) else 'false')""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        // User logic here
        return false;
    }
};

int main() {
    string s, t;
    if (cin >> s >> t) {
        if (s.front() == '"') s = s.substr(1, s.length()-2);
        if (t.front() == '"') t = t.substr(1, t.length()-2);
        Solution sol;
        cout << (sol.backspaceCompare(s, t) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean backspaceCompare(String s, String t) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (s.startsWith("\\"")) s = s.substring(1, s.length()-1);
            if (sc.hasNext()) {
                String t = sc.next();
                if (t.startsWith("\\"")) t = t.substring(1, t.length()-1);
                Solution sol = new Solution();
                System.out.println(sol.backspaceCompare(s, t));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    let s = input[0].trim();
    if (s.startsWith('"')) s = JSON.parse(s);
    let t = input[1].trim();
    if (t.startsWith('"')) t = JSON.parse(t);
    console.log(backspaceCompare(s, t));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool backspaceCompare(char* s, char* t) {
    // User logic here
    return false;
}

int main() {
    char s[201], t[201];
    if (scanf("%s %s", s, t) == 2) {
        printf("%s\\n", backspaceCompare(s, t) ? "true" : "false");
    }
    return 0;
}"""
    }

    def solve(s, t):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)

    test_cases_data = [
        ("ab#c", "ad#c"),
        ("ab##", "c#d#"),
        ("a#c", "b"),
        ("a##c", "#a#c"),
        ("xywrrmp", "xywrrmu#p"),
        ("bxj##tw", "bxj###tw"),
        ("nzp#o#g", "b#nzp#o#g"),
        ("##", "##"),
        ("abc", "abc"),
        ("a", "b")
    ]

    test_cases = []
    for i, (s, t) in enumerate(test_cases_data):
        inp = json.dumps(s).replace(" ", "") + "\n" + json.dumps(t).replace(" ", "")
        out = "true" if solve(s, t) else "false"
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
        "topics": ["Two Pointers", "String", "Stack", "Simulation"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
