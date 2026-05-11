import json
import os

def generate_json():
    problem_id = 680
    title = "Valid Palindrome II"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>680. Valid Palindrome II</h3>
<p>Given a string <code>s</code>, return <code>true</code> <em>if the</em> <code>s</code> <em>can be palindrome after deleting <strong>at most one</strong> character from it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aba"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abca"
<strong>Output:</strong> true
<strong>Explanation:</strong> You could delete the character 'c'.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
    <li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line: a JSON string `s`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= s.length <= 10^5",
        "s consists of lowercase English letters"
    ]

    explanation = """Use two pointers from both ends. If characters match, move inward. If they don't, try skipping either the left or right character and check if the remaining substring is a palindrome."""

    answer = """class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]: return False
                left += 1; right -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1; right -= 1
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print("true" if sol.validPalindrome(s) else "false")""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        // User logic here
        return false;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        cout << (sol.validPalindrome(input) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean validPalindrome(String s) {
        // User logic here
        return false;
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
            System.out.println(sol.validPalindrome(raw) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const s = JSON.parse(input);
    console.log(validPalindrome(s) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool validPalindrome(char* s) {
    // User logic here
    return false;
}

int main() {
    char input[200100];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char s[200100];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(s, input + 1, len - 2);
            s[len - 2] = '\\0';
        } else {
            strcpy(s, input);
        }
        printf("%s\\n", validPalindrome(s) ? "true" : "false");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"aba"', "expected_output": "true", "is_sample": True},
        {"input": '"abca"', "expected_output": "true", "is_sample": True},
        {"input": '"abc"', "expected_output": "false", "is_sample": False},
        {"input": '"a"', "expected_output": "true", "is_sample": False},
        {"input": '"aa"', "expected_output": "true", "is_sample": False},
        {"input": '"ab"', "expected_output": "true", "is_sample": False},
        {"input": '"racecar"', "expected_output": "true", "is_sample": False},
        {"input": '"deeee"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "a" * 49999 + "b" + "a" * 49999 + '"', "expected_output": "true", "is_sample": False},
        {"input": '"' + "a" * 49999 + "bc" + "a" * 49998 + '"', "expected_output": "false", "is_sample": False}
    ]

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
        "topics": ["Two Pointers", "String", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
