import json
import os

def generate_json():
    problem_id = 557
    title = "Reverse Words in a String III"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>557. Reverse Words in a String III</h3>
<p>Given a string <code>s</code>, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "Let's take LeetCode contest"
<strong>Output:</strong> "s'teL ekat edoCteeL tsetnoc"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "Mr Ding"
<strong>Output:</strong> "rM gniD"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>s</code> contains printable ASCII characters.</li>
    <li><code>s</code> does not contain any leading or trailing spaces.</li>
    <li>There is <strong>at least one</strong> word in <code>s</code>.</li>
    <li>All the words in <code>s</code> are separated by a single space.</li>
</ul>"""

    input_format = "A single line: a JSON string `s`."
    output_format = "A JSON string with each word reversed."

    constraints = [
        "1 <= s.length <= 5 * 10^4",
        "s contains printable ASCII characters",
        "s does not contain any leading or trailing spaces",
        "All words are separated by a single space"
    ]

    explanation = """Split the string by spaces, reverse each word individually, then join them back together with spaces."""

    answer = """class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def reverseWords(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.reverseWords(s)))""",
        "cpp": """#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        string result = sol.reverseWords(input);
        cout << "\\"" << result << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String reverseWords(String s) {
        // User logic here
        return "";
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
            System.out.println("\\"" + sol.reverseWords(raw) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const s = JSON.parse(input);
    console.log(JSON.stringify(reverseWords(s)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverseWords(char* s) {
    // User logic here
    char* result = (char*)malloc(strlen(s) + 1);
    strcpy(result, s);
    return result;
}

int main() {
    char raw[100000];
    if (fgets(raw, sizeof(raw), stdin)) {
        raw[strcspn(raw, "\\n")] = 0;
        char s[100000];
        int len = strlen(raw);
        if (len >= 2 && raw[0] == '"') {
            strncpy(s, raw + 1, len - 2);
            s[len - 2] = '\\0';
        } else {
            strcpy(s, raw);
        }
        char* result = reverseWords(s);
        printf("\\"%s\\"\\n", result);
        free(result);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": '"Let\'s take LeetCode contest"', "expected_output": '"s\'teL ekat edoCteeL tsetnoc"', "is_sample": True},
        {"input": '"Mr Ding"', "expected_output": '"rM gniD"', "is_sample": True},

        # Five Diverse Cases
        {"input": '"hello"', "expected_output": '"olleh"', "is_sample": False},
        {"input": '"a"', "expected_output": '"a"', "is_sample": False},
        {"input": '"abcde fghij"', "expected_output": '"edcba jihgf"', "is_sample": False},
        {"input": '"God Ding"', "expected_output": '"doG gniD"', "is_sample": False},
        {"input": '"I love you"', "expected_output": '"I evol uoy"', "is_sample": False},

        # Three Stress Test Cases
        {"input": '"' + ' '.join(['a' * 100] * 490) + '"', "expected_output": '"' + ' '.join(['a' * 100] * 490) + '"', "is_sample": False},
        {"input": '"' + ' '.join(['abcde'] * 9999) + '"', "expected_output": '"' + ' '.join(['edcba'] * 9999) + '"', "is_sample": False},
        {"input": '"' + 'z' * 50000 + '"', "expected_output": '"' + 'z' * 50000 + '"', "is_sample": False}
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
