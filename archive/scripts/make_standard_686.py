import json
import os

def generate_json():
    problem_id = 686
    title = "Repeated String Match"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>686. Repeated String Match</h3>
<p>Given two strings <code>a</code> and <code>b</code>, return the minimum number of times you should repeat string <code>a</code> such that string <code>b</code> is a substring of it. If it is not possible for <code>b</code> to be a substring of <code>a</code> after repeating, return <code>-1</code>.</p>

<p><strong>Note:</strong> string <code>"abc"</code> repeated 0 times is <code>""</code>. string <code>"abc"</code> repeated 1 time is <code>"abc"</code>. string <code>"abc"</code> repeated 2 times is <code>"abcabc"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "abcd", b = "cdabcdab"
<strong>Output:</strong> 3
<strong>Explanation:</strong> We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "a", b = "aa"
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= a.length &lt;= 10<sup>4</sup></code></li>
    <li><code>1 &lt;= b.length &lt;= 10<sup>4</sup></code></li>
    <li><code>a</code> and <code>b</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON string `a`.\nLine 2: JSON string `b`."
    output_format = "An integer: minimum repeats or -1."

    constraints = [
        "1 <= a.length <= 10^4",
        "1 <= b.length <= 10^4",
        "a and b consist of lowercase English letters"
    ]

    explanation = """We need to repeat `a` at least ceil(len(b)/len(a)) times to have enough characters. Then check if b is a substring; if not, try one more repetition. If still not found, return -1 (b has characters not in a)."""

    answer = """import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = math.ceil(len(b) / len(a))
        if b in a * times:
            return times
        if b in a * (times + 1):
            return times + 1
        return -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        a = json.loads(raw[0])
        b = json.loads(raw[1])
        sol = Solution()
        print(sol.repeatedStringMatch(a, b))""",
        "cpp": """#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        // User logic here
        return -1;
    }
};

string stripQuotes(string s) {
    if (s.length() >= 2 && s[0] == '"')
        return s.substr(1, s.length() - 2);
    return s;
}

int main() {
    string a_str, b_str;
    if (getline(cin, a_str) && getline(cin, b_str)) {
        Solution sol;
        cout << sol.repeatedStringMatch(stripQuotes(a_str), stripQuotes(b_str)) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int repeatedStringMatch(String a, String b) {
        // User logic here
        return -1;
    }
}

public class Main {
    static String stripQuotes(String s) {
        if (s.length() >= 2 && s.startsWith("\\""))
            return s.substring(1, s.length() - 1);
        return s;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String a = stripQuotes(sc.nextLine().trim());
            if (sc.hasNextLine()) {
                String b = stripQuotes(sc.nextLine().trim());
                Solution sol = new Solution();
                System.out.println(sol.repeatedStringMatch(a, b));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var repeatedStringMatch = function(a, b) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const a = JSON.parse(input[0]);
    const b = JSON.parse(input[1]);
    console.log(repeatedStringMatch(a, b));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int repeatedStringMatch(char* a, char* b) {
    // User logic here
    return -1;
}

int main() {
    char a_raw[20010], b_raw[20010];
    if (fgets(a_raw, sizeof(a_raw), stdin) && fgets(b_raw, sizeof(b_raw), stdin)) {
        int alen = strlen(a_raw), blen = strlen(b_raw);
        a_raw[strcspn(a_raw, "\\n")] = 0;
        b_raw[strcspn(b_raw, "\\n")] = 0;
        char a[20010], b[20010];
        if (a_raw[0] == '"') { strncpy(a, a_raw+1, alen-2); a[alen-2]=0; } else strcpy(a, a_raw);
        if (b_raw[0] == '"') { strncpy(b, b_raw+1, blen-2); b[blen-2]=0; } else strcpy(b, b_raw);
        printf("%d\\n", repeatedStringMatch(a, b));
    }
    return 0;
}"""
    }

    # Compute expected outputs
    import math
    def solve(a, b):
        times = math.ceil(len(b) / len(a))
        if b in a * times: return times
        if b in a * (times + 1): return times + 1
        return -1

    test_cases_data = [
        ("abcd", "cdabcdab"),
        ("a", "aa"),
        ("abc", "wxyz"),
        ("ab", "ababababab"),
        ("abc", "abc"),
        ("abcd", "abcdabcd"),
        ("a", "a"),
        ("ba", "bababababab"),
        ("abc", "c"),
        ("abc", "cabcabca")
    ]

    test_cases = []
    for i, (a, b) in enumerate(test_cases_data):
        inp = json.dumps(a) + "\\n" + json.dumps(b)
        out = str(solve(a, b))
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
        "topics": ["String", "String Matching"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
