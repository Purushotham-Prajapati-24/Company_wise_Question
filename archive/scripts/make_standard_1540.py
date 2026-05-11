import json
import os

def generate_json():
    problem_id = 1540
    title = "Can Convert String in K Moves"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1540. Can Convert String in K Moves</h3>
<p>Given two strings <code>s</code> and <code>t</code>, your goal is to convert <code>s</code> into <code>t</code> in <code>k</code> moves or less.</p>

<p>During the <code>i<sup>th</sup></code> (<code>1 &lt;= i &lt;= k</code>) move you can:</p>

<ul>
	<li>Choose any index <code>j</code> (1-indexed) from <code>s</code>, such that <code>1 &lt;= j &lt;= s.length</code> and <code>j</code> has not been chosen in any previous move, and shift the character at that index <code>i</code> times.</li>
	<li>Do nothing.</li>
</ul>

<p>Shifting a character means replacing it with the next letter in the alphabet (wrapping around so <code>'z'</code> becomes <code>'a'</code>). Shifting a character by <code>i</code> means applying the shift operations <code>i</code> times.</p>

<p>Remember that any index <code>j</code> can be used at most once.</p>

<p>Return <code>true</code> if it&#39;s possible to convert <code>s</code> into <code>t</code> in <code>k</code> or less moves, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;input&quot;, t = &quot;ouput&quot;, k = 9
<strong>Output:</strong> true
<strong>Explanation:</strong> In the 6th move, we shift &#39;i&#39; at index 1 by 6 times to get &#39;o&#39;. In the 9th move, we shift &#39;n&#39; at index 2 by 9 times to get &#39;w&#39;. Then we get &quot;ouput&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;, t = &quot;bcd&quot;, k = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> We need to shift each character in s one time to get t. However, that would require using the same move number more than once, which is not allowed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;, t = &quot;bbb&quot;, k = 27
<strong>Output:</strong> true
<strong>Explanation:</strong> In the 1st move, we shift the first &#39;a&#39; 1 time to get &#39;b&#39;. In the 27th move, we shift the second &#39;a&#39; 27 times to get &#39;b&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= k &lt;= 10^9</code></li>
	<li><code>s</code>, <code>t</code> contain only lowercase English letters.</li>
</ul>
"""

    input_format = "Two strings `s` and `t` and an integer `k` provided as `[s, t, k]` in JSON."
    output_format = "A boolean value `true` or `false`."

    constraints = [
        "1 <= s.length, t.length <= 10^5",
        "0 <= k <= 10^9"
    ]

    explanation = """To determine if conversion is possible:
1. For each index `i`, calculate the required shift `diff = (t[i] - s[i] + 26) % 26`.
2. A shift of `0` requires no moves. 
3. For a shift `diff > 0`, it can first be achieved in move `diff`, and subsequently in moves `diff + 26`, `diff + 26 * 2`, etc.
4. Keep track of how many times each shift `diff` (1 to 25) is required. 
5. For each `diff`, the maximum move number needed is `diff + 26 * (count[diff] - 1)`.
6. If any such maximum move number exceeds `k`, return `false`. Otherwise, return `true`.
7. Also, if `len(s) != len(t)`, return `false` immediately."""

    answer = """class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        counts = [0] * 26
        for char_s, char_t in zip(s, t):
            diff = (ord(char_t) - ord(char_s) + 26) % 26
            if diff > 0:
                max_move = diff + 26 * counts[diff]
                if max_move > k:
                    return False
                counts[diff] += 1
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s, t, k = json.loads(raw)
        sol = Solution()
        print(str(sol.canConvertString(s, t, k)).lower())""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool canConvertString(string s, string t, int k) {
        // User logic here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        string s = j[0].get<string>();
        string t = j[1].get<string>();
        int k = j[2];
        Solution sol;
        cout << (sol.canConvertString(s, t, k) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public boolean canConvertString(String s, String t, int k) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            String s = (String) data[0];
            String t = (String) data[1];
            int k = (Integer) data[2];
            System.out.println(new Solution().canConvertString(s, t, k));
        }
    }
}""",
        "javascript": """var canConvertString = function(s, t, k) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [s, t, k] = JSON.parse(input);
    console.log(canConvertString(s, t, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool canConvertString(char * s, char * t, int k) {
    // User logic here
    return false;
}

char* read_json_string() {
    int c;
    while ((c = getchar()) != EOF && c != '"');
    if (c == EOF) return NULL;
    int cap = 128, len = 0;
    char* str = malloc(cap);
    while ((c = getchar()) != EOF && c != '"') {
        if (len + 1 >= cap) { cap *= 2; str = realloc(str, cap); }
        str[len++] = c;
    }
    str[len] = '\\0';
    return str;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    char* s = read_json_string();
    while ((c = getchar()) != EOF && c != ',');
    char* t = read_json_string();
    while ((c = getchar()) != EOF && c != ',');
    int k;
    if (scanf("%d", &k) == 1) {
        printf("%s\\n", canConvertString(s, t, k) ? "true" : "false");
    }
    free(s); free(t);
    return 0;
}"""
    }

    def solve(s, t, k):
        if len(s) != len(t): return False
        counts = [0] * 26
        for char_s, char_t in zip(s, t):
            diff = (ord(char_t) - ord(char_s) + 26) % 26
            if diff > 0:
                max_move = diff + 26 * counts[diff]
                if max_move > k:
                    return False
                counts[diff] += 1
        return True

    test_cases_data = [
        ["input", "ouput", 9],   # Sample 1
        ["abc", "bcd", 10],      # Sample 2
        ["aab", "bbb", 27],      # Sample 3
        ["", "", 0],              # Empty
        ["a", "z", 25],           # max single
        ["a", "z", 24],           # fail single
        ["aa", "zz", 51],         # duplicate diff
        # Stress tests
        ["a"*100000, "b"*100000, 10**9],
        ["abcdefghijklmnopqrstuvwxyz"*3000, "bcdefghijklmnopqrstuvwxyza"*3000, 10**6],
        ["a"*100000, "z"*100000, 10**5]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2])).lower()
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Hash Table", "Greedy"], "companyIndex": 0
    }

    output_path = f"1501-1700/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
