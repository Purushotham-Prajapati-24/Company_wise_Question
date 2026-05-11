import json
import os

def generate_json():
    problem_id = 647
    title = "Palindromic Substrings"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>647. Palindromic Substrings</h3>
<p>Given a string <code>s</code>, return <em>the number of <strong>palindromic substrings</strong> in it</em>.</p>

<p>A string is a <strong>palindrome</strong> when it reads the same backward as forward.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three palindromic strings: "a", "b", "c".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaa"
<strong>Output:</strong> 6
<strong>Explanation:</strong> Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 1000</code></li>
    <li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line: a JSON string `s`."
    output_format = "An integer: the count of palindromic substrings."

    constraints = [
        "1 <= s.length <= 1000",
        "s consists of lowercase English letters"
    ]

    explanation = """Use the expand-around-center technique. For each index, expand outward for both odd-length and even-length palindromes. Count all valid palindromes found. Time: O(n^2), Space: O(1)."""

    answer = """class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def countSubstrings(self, s: str) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(sol.countSubstrings(s))""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        // User logic here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        cout << sol.countSubstrings(input) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int countSubstrings(String s) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() >= 2 && raw.startsWith("\\""))
                raw = raw.substring(1, raw.length() - 1);
            Solution sol = new Solution();
            System.out.println(sol.countSubstrings(raw));
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const s = JSON.parse(input);
    console.log(countSubstrings(s));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int countSubstrings(char* s) {
    // User logic here
    return 0;
}

int main() {
    char input[2000];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char s[2000];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(s, input + 1, len - 2);
            s[len - 2] = '\\0';
        } else {
            strcpy(s, input);
        }
        printf("%d\\n", countSubstrings(s));
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"abc"', "expected_output": "3", "is_sample": True},
        {"input": '"aaa"', "expected_output": "6", "is_sample": True},
        {"input": '"a"', "expected_output": "1", "is_sample": False},
        {"input": '"ab"', "expected_output": "2", "is_sample": False},
        {"input": '"aa"', "expected_output": "3", "is_sample": False},
        {"input": '"abba"', "expected_output": "6", "is_sample": False},
        {"input": '"racecar"', "expected_output": "10", "is_sample": False},
        {"input": '"' + "a" * 1000 + '"', "expected_output": str(1000 * 1001 // 2), "is_sample": False},
        {"input": '"' + "ab" * 500 + '"', "expected_output": "1000", "is_sample": False},
        {"input": '"' + "abcba" * 200 + '"', "expected_output": str(sum(1 for i in range(1000) for j in range(i, 1000) if ("abcba" * 200)[i:j+1] == ("abcba" * 200)[i:j+1][::-1])), "is_sample": False}
    ]
    # Compute last test case properly
    s = "abcba" * 200
    n = len(s)
    count = 0
    for center in range(2 * n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    test_cases[9]["expected_output"] = str(count)

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
        "topics": ["String", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
