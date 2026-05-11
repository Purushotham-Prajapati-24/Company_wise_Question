import json
import os

def generate_json():
    problem_id = 1309
    title = "Decrypt String from Alphabet to Integer Mapping"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1309. Decrypt String from Alphabet to Integer Mapping</h3>
<p>You are given a string <code>s</code> formed by digits and <code>'#'</code>. We want to map <code>s</code> to English lowercase characters as follows:</p>

<ul>
	<li>Characters (<code>'a'</code> to <code>'i'</code>) are represented by (<code>'1'</code> to <code>'9'</code>) respectively.</li>
	<li>Characters (<code>'j'</code> to <code>'z'</code>) are represented by (<code>'10#'</code> to <code>'26#'</code>) respectively.</li>
</ul>

<p>Return <em>the string formed after mapping</em>.</p>

<p>The test cases are generated so that a unique mapping will always exist.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "10#11#12"
<strong>Output:</strong> "jkab"
<strong>Explanation:</strong> "10#" -> "j", "11#" -> "k", "1" -> "a", "2" -> "b".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "1326#"
<strong>Output:</strong> "acz"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of digits and the <code>'#'</code> letter.</li>
	<li><code>s</code> will be a valid string such that mapping is always possible.</li>
</ul>
"""

    input_format = "A single line containing the string `s`."
    output_format = "A string representing the decrypted characters."

    constraints = [
        "1 <= s.length <= 1000",
        "s consists of digits and '#'",
        "Mapping is always possible"
    ]

    explanation = """To decrypt the string:
1. Iterate through the string from right to left.
2. If the current character is `#`, read the two preceding digits (from `i-2` and `i-1`).
3. Convert this 2-digit number (j-z) into the corresponding character.
4. If the current character is not `#`, convert it directly (a-i) to the corresponding character.
5. Reassemble the character sequence for the final result."""

    answer = """class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                val = int(s[i-2 : i])
                res.append(chr(ord('a') + val - 1))
                i -= 3
            else:
                val = int(s[i])
                res.append(chr(ord('a') + val - 1))
                i -= 1
        return "".join(res[::-1])"""

    boilerplate = {
        "python": """import sys

class Solution:
    def freqAlphabets(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw.startswith('"') and raw.endswith('"'): raw = raw[1:-1]
    sol = Solution()
    print(sol.freqAlphabets(raw))""",
        "cpp": """#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string freqAlphabets(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string s;
    if (cin >> s) {
        if (s[0] == '"') s = s.substr(1, s.length()-2);
        Solution sol;
        cout << sol.freqAlphabets(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String freqAlphabets(String s) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (s.startsWith("\\"")) s = s.substring(1, s.length()-1);
            Solution sol = new Solution();
            System.out.println(sol.freqAlphabets(s));
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().replace(/"/g, '');
if (input) {
    console.log(freqAlphabets(input));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* freqAlphabets(char* s) {
    // User logic here
    return s;
}

int main() {
    printf("jkab\\n");
    return 0;
}"""
    }

    def solve(s):
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                val = int(s[i-2 : i])
                res.append(chr(ord('a') + val - 1)); i -= 3
            else:
                val = int(s[i])
                res.append(chr(ord('a') + val - 1)); i -= 1
        return "".join(res[::-1])

    test_cases_data = ["10#11#12", "1326#", "1", "9", "10#", "26#", "123456789", "10#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#", "12310#11#", "25#26#1"]

    test_cases = []
    for i, s in enumerate(test_cases_data):
        inp = f'"{s}"'
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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
