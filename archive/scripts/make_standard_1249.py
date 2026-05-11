import json
import os

def generate_json():
    problem_id = 1249
    title = "Minimum Remove to Make Valid Parentheses"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1249. Minimum Remove to Make Valid Parentheses</h3>
<p>Given a string s of <code>'('</code> , <code>')'</code> and lowercase English characters. </p>

<p>Your task is to remove the minimum number of parentheses ( <code>'('</code> or <code>')'</code>, in any positions ) so that the resulting parentheses string is valid and return <strong>any</strong> valid string.</p>

<p>Formally, a <em>parentheses string</em> is valid if and only if:</p>
<ul>
	<li>It is the empty string, contains only lowercase characters, or</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "lee(t(c)o)de)"
<strong>Output:</strong> "lee(t(c)o)de"
<strong>Explanation:</strong> "lee(t(c)ode" , "lee(t(c)o)de" are also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a)b(c)d"
<strong>Output:</strong> "ab(c)d"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "))(("
<strong>Output:</strong> ""
<strong>Explanation:</strong> An empty string is also valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either<code>'('</code> , <code>')'</code>, or lowercase English letter<code>.</code></li>
</ul>"""

    input_format = "A string `s` enclosed in quotes as a JSON string."
    output_format = "A string representing any valid result."

    constraints = [
        "1 <= s.length <= 10^5",
        "s contains '(', ')', and lowercase English letters"
    ]

    explanation = """To make the string valid with minimum removals:
1. Use a stack to track the indices of opening parentheses `(`.
2. Iterate through the string:
   - If `s[i]` is `(`, push its index to the stack.
   - If `s[i]` is `)`, and the stack is not empty, pop the top index (matching pair).
   - If `s[i]` is `)` and the stack is empty, this `)` is invalid and should be removed. Mark its index.
3. After the loop, any indices remaining on the stack correspond to opening parentheses `(` that have no matching `)`. These are also invalid.
4. Construct the final string by skipping all marked invalid indices."""

    answer = """class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = "" # Mark for removal
        while stack:
            s_list[stack.pop()] = "" # Mark for removal
        return "".join(s_list)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(sol.minRemoveToMakeValid(s))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        string s = json::parse(line);
        Solution sol;
        cout << sol.minRemoveToMakeValid(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String minRemoveToMakeValid(String s) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String s = mapper.readValue(sc.nextLine(), String.class);
            System.out.println(new Solution().minRemoveToMakeValid(s));
        }
    }
}""",
        "javascript": """var minRemoveToMakeValid = function(s) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(minRemoveToMakeValid(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * minRemoveToMakeValid(char * s){
    // User logic here
    return "";
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    def solve(s):
        s_list = list(s)
        stack = []
        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack: stack.pop()
                else: s_list[i] = ""
        while stack:
            s_list[stack.pop()] = ""
        return "".join(s_list)

    test_cases_data = [
        "lee(t(c)o)de)",   # Sample 1
        "a)b(c)d",         # Sample 2
        "))((",            # Sample 3
        "()()",            # Valid
        "(((",             # All open
        ")))",             # All close
        "abc(d)ef",        # Valid middle
        # Stress tests
        "(a" * 1000 + "b" * 1000 + ")c" * 1000,
        "(" * 500 + ")" * 500 + "a" * 500,
        "a" * 10000        # Large text
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = solve(t)
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Stack"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
