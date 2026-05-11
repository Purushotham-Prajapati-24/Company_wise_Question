import json
import os

def generate_json():
    problem_id = 917
    title = "Reverse Only Letters"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>917. Reverse Only Letters</h3>
<p>Given a string <code>s</code>, reverse the string where all characters that are not English letters remain in the same position and all English letters (lowercase or uppercase) should be reversed.</p>

<p>Return <code>s</code><em> after reversing it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ab-cd"
<strong>Output:</strong> "dc-ba"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a-bC-dEf-ghIj"
<strong>Output:</strong> "j-Ih-gfE-dCba"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "Test1ng-Leet=code-Q!"
<strong>Output:</strong> "Qedo1ct-eeLg=ntse-T!"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 100</code></li>
    <li><code>s</code> consists of characters with ASCII values in the range <code>[33, 122]</code>.</li>
    <li><code>s</code> does not contain <code>'\"'</code> or <code>'\\'</code>.</li>
</ul>"""

    input_format = "A single string s (JSON string)."
    output_format = "A single string representing the modified s."

    constraints = [
        "1 <= s.length <= 100",
        "ASCII values in [33, 122]",
        "No double quotes or backslashes"
    ]

    explanation = """We use a two-pointer approach starting from both ends of the string. At each step, if both pointers point to a letter, we swap them and move both. If the left pointer is not pointing to a letter, we increment it. If the right pointer is not pointing to a letter, we decrement it. We continue until the pointers meet."""

    answer = """class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        l, r = 0, len(s_list) - 1
        while l < r:
            if not s_list[l].isalpha():
                l += 1
            elif not s_list[r].isalpha():
                r -= 1
            else:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
        return "".join(s_list)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # User logic here
        return s

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.reverseOnlyLetters(s)))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    string reverseOnlyLetters(string s) {
        // User logic here
        return s;
    }
};

int main() {
    string input;
    if (cin >> input) {
        if (input[0] == '"') input = input.substr(1, input.length()-2);
        Solution sol;
        cout << "\\"" << sol.reverseOnlyLetters(input) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String reverseOnlyLetters(String s) {
        // User logic here
        return s;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (s.startsWith("\\"")) s = s.substring(1, s.length()-1);
            Solution sol = new Solution();
            System.out.println("\\"" + sol.reverseOnlyLetters(s) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(reverseOnlyLetters(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* reverseOnlyLetters(char* s) {
    // User logic here
    return s;
}

int main() {
    char input[200];
    if (scanf("%s", input) == 1) {
        char* s = input;
        if (s[0] == '"') {
            s++;
            s[strlen(s)-1] = '\\0';
        }
        printf("\\"%s\\"\\n", reverseOnlyLetters(s));
    }
    return 0;
}"""
    }

    def solve(s):
        s_list = list(s)
        l, r = 0, len(s_list) - 1
        while l < r:
            if not s_list[l].isalpha(): l += 1
            elif not s_list[r].isalpha(): r -= 1
            else:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1; r -= 1
        return "".join(s_list)

    test_cases_data = [
        "ab-cd",
        "a-bC-dEf-ghIj",
        "Test1ng-Leet=code-Q!",
        "7_28_",
        "---",
        "a",
        "ab",
        "abc",
        "a-b-c-d",
        "z$y#x!w"
    ]

    test_cases = []
    for i, s in enumerate(test_cases_data):
        inp = json.dumps(s)
        out = json.dumps(solve(s))
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
