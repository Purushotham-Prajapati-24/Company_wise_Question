import json
import os

def generate_json():
    problem_id = 1312
    title = "Minimum Insertion Steps to Make a String Palindrome"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1312. Minimum Insertion Steps to Make a String Palindrome</h3>
<p>Given a string <code>s</code>. In one step you can insert any character at any position of the string.</p>

<p>Return <em>the minimum number of steps</em> to make <code>s</code>&nbsp;palindrome.</p>

<p>A&nbsp;<b>Palindrome String</b>&nbsp;is one that reads the same backward as forward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "zzazz"
<strong>Output:</strong> 0
<strong>Explanation:</strong> The string "zzazz" is already palindrome we don't need any insertions.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "mbadm"
<strong>Output:</strong> 2
<strong>Explanation:</strong> String can be "mbdadbm" or "mdbabdm".
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Inserting 5 characters yields "leetcodocteel".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A string `s` enclosed in quotes as a JSON string."
    output_format = "An integer representing the minimum steps."

    constraints = [
        "1 <= s.length <= 500",
        "s consists of lowercase English letters"
    ]

    explanation = """To find the minimum insertions to make a string a palindrome:
1. This is equivalent to finding the length of the Longest Palindromic Subsequence (LPS).
2. The number of insertions needed is `len(s) - LPS(s)`.
3. To find LPS(s):
   - Let `reverse_s = s[::-1]`.
   - The LPS(s) is equal to the Longest Common Subsequence (LCS) of `s` and `reverse_s`.
4. To find LCS(s, reverse_s):
   - Use dynamic programming where `dp[i][j]` is the length of LCS of `s[0:i]` and `reverse_s[0:j]`.
   - `dp[i][j] = 1 + dp[i-1][j-1]` if `s[i-1] == reverse_s[j-1]`.
   - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` otherwise.
5. The result is `len(s) - dp[n][n]`."""

    answer = """class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n - dp[n][n]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minInsertions(self, s: str) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(sol.minInsertions(s))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minInsertions(string s) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        string s = json::parse(line);
        Solution sol;
        cout << sol.minInsertions(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minInsertions(String s) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String s = mapper.readValue(sc.nextLine(), String.class);
            System.out.println(new Solution().minInsertions(s));
        }
    }
}""",
        "javascript": """var minInsertions = function(s) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(minInsertions(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minInsertions(char * s){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    def solve(s):
        n = len(s)
        t = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n - dp[n][n]

    test_cases_data = [
        "zzazz",        # Sample 1
        "mbadm",        # Sample 2
        "leetcode",     # Sample 3
        "a",            # Single
        "ab",           # Two diff
        "aba",          # Palindrome
        "abcde",        # Distinct
        # Stress tests
        "a" * 250 + "b" + "a" * 249,
        "abcdef" * 80,
        "g" * 500
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Dynamic Programming"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
