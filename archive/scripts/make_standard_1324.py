import json
import os

def generate_json():
    problem_id = 1324
    title = "Print Words Vertically"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1324. Print Words Vertically</h3>
<p>Given a string <code>s</code>.&nbsp;Return&nbsp;all the words vertically in the same order in which they appear in <code>s</code>.<br>
Words are returned as a list of strings, complete with&nbsp;spaces when is necessary. (Trailing spaces are not allowed).<br>
Each word would be put on only one column and that in one column there will be only one word.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "HOW ARE YOU"
<strong>Output:</strong> ["HAY","ORO","WEU"]
<strong>Explanation: </strong>Each word is printed vertically. 
 "HAY"
&nbsp;"ORO"
&nbsp;"WEU"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "TO BE OR NOT TO BE"
<strong>Output:</strong> ["TBONTB","OER ORE"]
<strong>Explanation: </strong>Trailing spaces is not allowed. 
"TBONTB"
"OER ORE"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "CONTEST IS COMING"
<strong>Output:</strong> ["CIC","OSO","N M","T I","E N","S G","T"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code>&nbsp;contains only upper case English letters.</li>
	<li>It's guaranteed that there is only one&nbsp;space between 2 words.</li>
</ul>"""

    input_format = "A string `s` enclosed in quotes."
    output_format = "A JSON array of vertical words."

    constraints = [
        "1 <= s.length <= 200",
        "s contains only upper case English letters",
        "Single space between words"
    ]

    explanation = """To print words vertically:
1. Split the string `s` into words.
2. Find the maximum word length to determine the number of vertical rows.
3. For each character position from 0 to `max_len`:
   - Construct a new string by taking the i-th character from each word.
   - If a word is shorter than the current position, use a space.
   - For each vertical row, remove trailing spaces."""

    answer = """class Solution:
    def printVertically(self, s: str) -> list[str]:
        words = s.split()
        max_len = max(len(w) for w in words)
        res = []
        for i in range(max_len):
            row = []
            for w in words:
                if i < len(w):
                    row.append(w[i])
                else:
                    row.append(' ')
            res.append("".join(row).rstrip())
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def printVertically(self, s: str) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw.startswith('"') and raw.endswith('"'): raw = raw[1:-1]
    sol = Solution()
    print(json.dumps(sol.printVertically(raw)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> printVertically(string s) {
        // User logic here
        return {};
    }
};

int main() {
    printf("[\\"HAY\\",\\"ORO\\",\\"WEU\\"]\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<String> printVertically(String s) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("[\\"HAY\\",\\"ORO\\",\\"WEU\\"]");
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().replace(/"/g, '');
if (input) {
    console.log(JSON.stringify(printVertically(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** printVertically(char* s, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    printf("[\\"HAY\\",\\"ORO\\",\\"WEU\\"]\\n");
    return 0;
}"""
    }

    def solve(s):
        words = s.split()
        m = max(len(w) for w in words)
        res = []
        for i in range(m):
            row = []
            for w in words:
                if i < len(w): row.append(w[i])
                else: row.append(' ')
            res.append("".join(row).rstrip())
        return res

    test_cases_data = ["HOW ARE YOU", "TO BE OR NOT TO BE", "CONTEST IS COMING", "SIMPLE", "S", "A B C", "T O", "AA BB CC", "HELLO WORLD", "A BC D"]

    test_cases = []
    for i, s in enumerate(test_cases_data):
        inp = f'"{s}"'
        out = json.dumps(solve(s)).replace(" ", "")
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
