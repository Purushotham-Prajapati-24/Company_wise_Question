import json
import os

def generate_json():
    problem_id = 1044
    title = "Longest Duplicate Substring"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1044. Longest Duplicate Substring</h3>
<p>Given a string <code>s</code>, consider all <em>duplicated substrings</em>: (contiguous) substrings of <code>s</code> that occur 2 or more times. The occurrences may overlap.</p>

<p>Return <strong>any</strong> duplicated substring that has the longest possible length. If <code>s</code> does not have a duplicated substring, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "banana"
<strong>Output:</strong> "ana"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> ""
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>2 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
    <li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single string `s` representing the input string."
    output_format = "A string which is the longest duplicated substring."

    constraints = [
        "2 <= s.length <= 30000",
        "s consists of lowercase English letters"
    ]

    explanation = """To find the longest duplicate substring efficiently:
1. Binary search the length of the duplicate substring (from 1 to N-1).
2. For a fixed length `L`, use Rabin-Karp (Rolling Hash) to check if any duplicate substring of length `L` exists in O(N).
3. If hashes match, verify the actual strings to avoid collisions.
The time complexity is O(N log N)."""

    answer = """class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def check(length):
            h = 0
            for i in range(length):
                h = (h * 26 + ord(s[i]) - 97) % (2**63 - 1)
            seen = {h}
            power = pow(26, length, 2**63 - 1)
            for i in range(length, len(s)):
                h = (h * 26 + ord(s[i]) - 97 - (ord(s[i-length]) - 97) * power) % (2**63 - 1)
                if h in seen:
                    return s[i-length+1 : i+1]
                seen.add(h)
            return ""

        res, left, right = "", 1, len(s) - 1
        while left <= right:
            mid = (left + right) // 2
            candidate = check(mid)
            if candidate:
                res = candidate
                left = mid + 1
            else:
                right = mid - 1
        return res"""

    boilerplate = {
        "python": """import sys

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip().strip('"')
    if raw:
        sol = Solution()
        print(f'"{sol.longestDupSubstring(raw)}"')""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    string longestDupSubstring(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string s;
    if (cin >> s) {
        if (s[0] == '"') s = s.substr(1, s.length() - 2);
        Solution sol;
        cout << "\\"" << sol.longestDupSubstring(s) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String longestDupSubstring(String s) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next().replace("\\"", "");
            System.out.println("\\"" + new Solution().longestDupSubstring(s) + "\\"");
        }
    }
}""",
        "javascript": """var longestDupSubstring = function(s) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().replace(/\\"/g, "");
if (input) {
    console.log(`"${longestDupSubstring(input)}"`);
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* longestDupSubstring(char* s) {
    // User logic here
    return "";
}

int main() {
    char s[40000];
    if (scanf("%s", s) == 1) {
        char *p = s;
        if (*p == '"') {
            p++;
            s[strlen(s)-1] = '\\0';
        }
        printf("\\"%s\\"\\n", longestDupSubstring(p));
    }
    return 0;
}"""
    }

    def solve(s):
        def check(length):
            h = 0
            for i in range(length):
                h = (h * 26 + ord(s[i]) - 97) % (2**63 - 1)
            seen = {h}
            power = pow(26, length, 2**63 - 1)
            for i in range(length, len(s)):
                h = (h * 26 + ord(s[i]) - 97 - (ord(s[i-length]) - 97) * power) % (2**63 - 1)
                if h in seen:
                    return s[i-length+1 : i+1]
                seen.add(h)
            return ""
        res, left, right = "", 1, len(s) - 1
        while left <= right:
            mid = (left + right) // 2
            cand = check(mid)
            if cand: res = cand; left = mid + 1
            else: right = mid - 1
        return res

    test_cases_data = [
        "banana", "abcd", "aaaaa", "abcdeabcde", "missing", "racecar", "zabcabc",
        # Stress tests (last 3)
        "a" * 100,
        "abc" * 33,
        "abacaba" * 10
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = f'"{t}"'
        out = f'"{solve(t)}"'
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 512, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Binary Search", "Rolling Hash", "Suffix Array"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
