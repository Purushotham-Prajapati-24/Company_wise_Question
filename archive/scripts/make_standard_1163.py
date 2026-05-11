import json
import os

def generate_json():
    problem_id = 1163
    title = "Last Substring in Lexicographical Order"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1163. Last Substring in Lexicographical Order</h3>
<p>Given a string <code>s</code>, return <em>the last substring of</em> <code>s</code> <em>in lexicographical order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "abab"
<strong>Output:</strong> "bab"
<strong>Explanation:</strong> The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically largest substring is "bab".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> "tcode"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>5</sup></code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
"""

    input_format = "A string `s` provided as `[s]` in JSON."
    output_format = "A string representing the lexicographically largest substring."

    constraints = [
        "1 <= s.length <= 4 * 10^5",
        "s contains only lowercase English letters"
    ]

    explanation = """To find the lexicographically largest substring:
1. The largest substring will always be a suffix of the original string.
2. Use two pointers `i` and `j` starting at `0` and `1`.
3. Use a variable `k = 0` to compare `s[i+k]` and `s[j+k]`.
4. If `s[i+k] == s[j+k]`, increment `k`.
5. If `s[i+k] < s[j+k]`, it means the suffix starting at `j` is better than one starting at `i`. Update `i = max(i + k + 1, j)` and set `j = i + 1`, reset `k = 0`.
6. If `s[i+k] > s[j+k]`, it means suffix starting at `i` is better. Update `j = j + k + 1` and reset `k = 0`.
7. Continue until `j` reaches the end of the string.
8. The result is the substring starting from index `i` to the end."""

    answer = """class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            if s[i + k] < s[j + k]:
                i = max(i + k + 1, j)
                j = i + 1
            else:
                j += k + 1
            k = 0
        return s[i:]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def lastSubstring(self, s: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        data = json.loads(raw)
        if isinstance(data, list): s = data[0]
        else: s = data
        sol = Solution()
        print(sol.lastSubstring(s))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string lastSubstring(string s) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        string s;
        if (j.is_array()) s = j[0].get<string>();
        else s = j.get<string>();
        Solution sol;
        cout << sol.lastSubstring(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String lastSubstring(String s) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            String s;
            if (raw instanceof List) s = (String)((List)raw).get(0);
            else s = (String)raw;
            System.out.println(new Solution().lastSubstring(s));
        }
    }
}""",
        "javascript": """var lastSubstring = function(s) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let data = JSON.parse(input);
    const s = Array.isArray(data) ? data[0] : data;
    console.log(lastSubstring(s));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* lastSubstring(char* s) {
    // User logic here
    return s;
}

int main() {
    static char buf[400005 * 2];
    if (fgets(buf, sizeof(buf), stdin)) {
        char* p = strchr(buf, '\"');
        if (p) {
            p++;
            char* end = strrchr(p, '\"');
            if (end) *end = '\\0';
            printf("%s\\n", lastSubstring(p));
        } else {
            // handle raw string or other formats
            char* start = strchr(buf, '[');
            if (start) {
                char* s_start = strchr(start, '\"');
                if (s_start) {
                    s_start++;
                    char* s_end = strchr(s_start, '\"');
                    if (s_end) {
                        *s_end = '\\0';
                        printf("%s\\n", lastSubstring(s_start));
                    }
                }
            }
        }
    }
    return 0;
}"""
    }

    def solve(s):
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            if s[i + k] < s[j + k]:
                i = max(i + k + 1, j)
                j = i + 1
            else:
                j += k + 1
            k = 0
        return s[i:]

    test_cases_data = [
        ["abab"],      # Sample 1
        ["leetcode"],  # Sample 2
        ["aaaaa"],
        ["zzzzzzz"],
        ["a"],
        ["abacaba"],
        ["ba"],
        # Stress tests
        ["a"*100000],
        ["z"*100000 + "y"],
        ["abcdefghijklmnopqrstuvwxyz"*4000]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps([t]).replace(" ", "")
        out = f"\"{solve(t).replace('\"', '\\\"')}\""
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 512, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Two Pointers", "String"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
