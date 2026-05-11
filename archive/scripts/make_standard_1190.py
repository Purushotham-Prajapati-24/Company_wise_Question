import json
import os

def generate_json():
    problem_id = 1190
    title = "Reverse Substrings Between Each Pair of Parentheses"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1190. Reverse Substrings Between Each Pair of Parentheses</h3>
<p>You are given a string <code>s</code> that consists of lower case English letters and brackets. </p>

<p>Reverse the strings in each pair of matching parentheses, starting from the innermost one.</p>

<p>Your result should <strong>not</strong> contain any brackets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "(abcd)"
<strong>Output:</strong> "dcba"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(u(love)i)"
<strong>Output:</strong> "iloveu"
<strong>Explanation:</strong> The substring "love" is reversed first, then the whole string is reversed.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(ed(et(oc))el)"
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong> First, we reverse the substring "oc", then "etco", and finally, the whole string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> only contains lower case English letters and parentheses.</li>
	<li>It's guaranteed that all parentheses are balanced.</li>
</ul>"""

    input_format = "A string `s` enclosed in quotes as a JSON string."
    output_format = "A string representing the processed result."

    constraints = [
        "1 <= s.length <= 2000",
        "s contains only lower case English letters and parentheses"
    ]

    explanation = """To reverse substrings between parentheses:
1. Use a stack to track the indices of opening parentheses.
2. Iterate through the string.
3. If the character is `(`, push the current index to the stack.
4. If the character is `)`, pop the last index from the stack and reverse the substring between that index and the current one.
5. After processing all parentheses, remove all `(` and `)` from the string to get the final result."""

    answer = """class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = list(s)
        for i, c in enumerate(res):
            if c == '(':
                stack.append(i)
            elif c == ')':
                start = stack.pop()
                res[start+1:i] = res[start+1:i][::-1]
        return "".join(c for c in res if c not in "()")"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(sol.reverseParentheses(s))""",
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
    string reverseParentheses(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        string s = json::parse(line);
        Solution sol;
        cout << sol.reverseParentheses(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String reverseParentheses(String s) {
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
            System.out.println(new Solution().reverseParentheses(s));
        }
    }
}""",
        "javascript": """var reverseParentheses = function(s) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(reverseParentheses(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * reverseParentheses(char * s){
    // User logic here
    return "";
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    def solve(s):
        stack = []
        res = list(s)
        for i, c in enumerate(res):
            if c == '(':
                stack.append(i)
            elif c == ')':
                start = stack.pop()
                res[start+1:i] = res[start+1:i][::-1]
        return "".join(c for c in res if c not in "()")

    test_cases_data = [
        "(abcd)",             # Sample 1
        "(u(love)i)",         # Sample 2
        "(ed(et(oc))el)",     # Sample 3
        "a(bcdef)g",          # Middle
        "((a))",              # Double
        "a(b)c(d)e",          # Sequential
        "((((abcd))))",       # Nested
        # Stress tests
        "a" * 200,
        "(" * 100 + "a" * 100 + ")" * 100,
        "a" * 100 + "(((b)))" + "c" * 100
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
        "topics": ["Stack", "String"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
