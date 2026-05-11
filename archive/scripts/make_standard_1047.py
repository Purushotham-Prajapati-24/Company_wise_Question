import json
import os

def generate_json():
    problem_id = 1047
    title = "Remove All Adjacent Duplicates In String"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1047. Remove All Adjacent Duplicates In String</h3>
<p>You are given a string <code>s</code> consisting of lowercase English letters. A <strong>duplicate removal</strong> consists of choosing two <strong>adjacent</strong> and <strong>equal</strong> letters and removing them.</p>

<p>We repeatedly make <strong>duplicate removals</strong> on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It can be proven that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abbaca"
<strong>Output:</strong> "ca"
<strong>Explanation:</strong> 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "azxxzy"
<strong>Output:</strong> "ay"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single string `s` representing the input string."
    output_format = "A string after all adjacent duplicate removals."

    constraints = [
        "1 <= s.length <= 100000",
        "s consists of lowercase English letters"
    ]

    explanation = """Use a stack to build the result. Iterate through the string, if the current character is the same as the top of the stack, pop the stack. Otherwise, push the character onto the stack."""

    answer = """class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)"""

    boilerplate = {
        "python": """import sys

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip().strip('"')
    if raw:
        sol = Solution()
        print(f'"{sol.removeDuplicates(raw)}"')""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string removeDuplicates(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string s;
    if (cin >> s) {
        if (s[0] == '"') s = s.substr(1, s.length() - 2);
        Solution sol;
        cout << "\\"" << sol.removeDuplicates(s) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String removeDuplicates(String s) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next().replace("\\"", "");
            System.out.println("\\"" + new Solution().removeDuplicates(s) + "\\"");
        }
    }
}""",
        "javascript": """var removeDuplicates = function(s) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().replace(/\\"/g, "");
if (input) {
    console.log(`"${removeDuplicates(input)}"`);
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* removeDuplicates(char* s) {
    // User logic here
    return "";
}

int main() {
    char s[100005];
    if (scanf("%s", s) == 1) {
        char *p = s;
        if (*p == '"') {
            p++;
            s[strlen(s)-1] = '\\0';
        }
        printf("\\"%s\\"\\n", removeDuplicates(p));
    }
    return 0;
}"""
    }

    def solve(s):
        stack = []
        for char in s:
            if stack and stack[-1] == char: stack.pop()
            else: stack.append(char)
        return "".join(stack)

    test_cases_data = ["abbaca", "azxxzy", "aab", "baac", "abcde", "aaaaa", "abccba", 
                      "a" * 10, "ab" * 5, "aabbcc"]
    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = f'"{t}"'
        out = f'"{solve(t)}"'
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Stack"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
