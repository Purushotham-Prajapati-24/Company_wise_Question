import json
import os

def generate_json():
    problem_id = 761
    title = "Special Binary String"
    difficulty = "HARD"
    marks = 15

    html_description = """<h3>761. Special Binary String</h3>
<p>Special binary strings are binary strings with the following two properties:</p>

<ul>
    <li>The number of <code>0</code>'s is equal to the number of <code>1</code>'s.</li>
    <li>Every prefix of the binary string has at least as many <code>1</code>'s as <code>0</code>'s.</li>
</ul>

<p>You are given a special binary string <code>s</code>.</p>

<p>A move consists of choosing two consecutive, non-empty, special substrings of <code>s</code>, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.</p>

<p>Return <em>the lexicographically largest resulting string possible after applying the mentioned operations on the string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "11011000"
<strong>Output:</strong> "11100100"
<strong>Explanation:</strong> The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "10"
<strong>Output:</strong> "10"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 50</code></li>
    <li><code>s[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
    <li><code>s</code> is a special binary string.</li>
</ul>"""

    input_format = "A single line containing the string `s`."
    output_format = "A string representing the lexicographically largest special binary string."

    constraints = [
        "1 <= s.length <= 50",
        "s[i] is either '0' or '1'",
        "s is a special binary string"
    ]

    explanation = """A special binary string can be viewed as valid parentheses where '1' is '(' and '0' is ')'. We can split the string into multiple valid top-level special substrings. For each substring, the outermost characters must be '1' and '0'. We recursively sort the inner string. Finally, we sort all the top-level substrings in descending (lexicographical) order and concatenate them."""

    answer = """class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        res.sort(reverse=True)
        return "".join(res)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        if raw.startswith('"') and raw.endswith('"'):
            s = json.loads(raw)
        else:
            s = raw
        sol = Solution()
        print(sol.makeLargestSpecial(s))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string makeLargestSpecial(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string s;
    if (cin >> s) {
        if (s.length() >= 2 && s.front() == '"' && s.back() == '"') {
            s = s.substr(1, s.length() - 2);
        }
        Solution sol;
        cout << sol.makeLargestSpecial(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String makeLargestSpecial(String s) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (s.length() >= 2 && s.startsWith("\\"") && s.endsWith("\\"")) {
                s = s.substring(1, s.length() - 1);
            }
            Solution sol = new Solution();
            System.out.println(sol.makeLargestSpecial(s));
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {string}
 */
var makeLargestSpecial = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let s = input;
    if (s.startsWith('"') && s.endsWith('"')) {
        s = JSON.parse(s);
    }
    console.log(makeLargestSpecial(s));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* makeLargestSpecial(char* s) {
    // User logic here
    char* res = (char*)malloc(51);
    res[0] = '\\0';
    return res;
}

int main() {
    char s[200];
    if (scanf("%s", s) == 1) {
        char* str = s;
        int len = strlen(s);
        if (len >= 2 && s[0] == '"' && s[len-1] == '"') {
            s[len-1] = '\\0';
            str = s + 1;
        }
        char* res = makeLargestSpecial(str);
        printf("%s\\n", res);
        free(res);
    }
    return 0;
}"""
    }

    def solve(s):
        count = 0
        i = 0
        res = []
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                res.append('1' + solve(s[i + 1:j]) + '0')
                i = j + 1
        res.sort(reverse=True)
        return "".join(res)

    test_cases_data = [
        "11011000",
        "10",
        "101010",
        "1100",
        "11100010",
        "110100111000110100",
        "101100101100",
        "11111111110000000000",
        "101010101010101010101010101010",
        "11011011000010101100"
    ]

    test_cases = []
    for i, s in enumerate(test_cases_data):
        inp = json.dumps(s)
        out = solve(s)
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
        "topics": ["String", "Recursion"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
