import json
import os

def generate_json():
    problem_id = 942
    title = "DI String Match"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>942. DI String Match</h3>
<p>A permutation <code>perm</code> of <code>n + 1</code> integers of all the integers in the range <code>[0, n]</code> can be represented as a string <code>s</code> of length <code>n</code> where:</p>

<ul>
    <li><code>s[i] == 'I'</code> if <code>perm[i] &lt; perm[i + 1]</code>, and</li>
    <li><code>s[i] == 'D'</code> if <code>perm[i] &gt; perm[i + 1]</code>.</li>
</ul>

<p>Given a string <code>s</code>, reconstruct the permutation <code>perm</code> and return it. If there are multiple valid permutations <code>perm</code>, return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "IDID"
<strong>Output:</strong> [0,4,1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "III"
<strong>Output:</strong> [0,1,2,3]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "DDI"
<strong>Output:</strong> [3,2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
    <li><code>s[i]</code> is either <code>'I'</code> or <code>'D'</code>.</li>
</ul>"""

    input_format = "A single line containing the JSON string `s`."
    output_format = "A JSON array representing the permutation `perm`."

    constraints = [
        "1 <= s.length <= 10^5",
        "s[i] is 'I' or 'D'"
    ]

    explanation = """To reconstruct the permutation, we use a greedy approach with two pointers: `low = 0` and `high = n`.
- If `s[i] == 'I'`, we pick `low` and then increment `low`.
- If `s[i] == 'D'`, we pick `high` and then decrement `high`.
Finally, append the remaining value (which will be `low == high`)."""

    answer = """class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        l, r = 0, len(s)
        ans = []
        for char in s:
            if char == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        ans.append(l)
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.diStringMatch(s)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> diStringMatch(string s) {
        // User logic here
        return {};
    }
};

int main() {
    string s;
    if (cin >> s) {
        if (s[0] == '"') s = s.substr(1, s.length()-2);
        Solution sol;
        auto res = sol.diStringMatch(s);
        cout << "[";
        for (int i=0; i<res.size(); ++i) cout << res[i] << (i==res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] diStringMatch(String s) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (s.startsWith("\\"")) s = s.substring(1, s.length()-1);
            Solution sol = new Solution();
            int[] res = sol.diStringMatch(s);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(diStringMatch(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* diStringMatch(char* s, int* returnSize) {
    // User logic here
    int n = strlen(s);
    *returnSize = n + 1;
    return malloc((*returnSize) * sizeof(int));
}

int main() {
    char s[100000];
    if (scanf("%s", s) == 1) {
        int retSz;
        // printf("[]\\n"); 
    }
    return 0;
}"""
    }

    def solve(s):
        l, r = 0, len(s)
        ans = []
        for char in s:
            if char == 'I':
                ans.append(l); l += 1
            else:
                ans.append(r); r -= 1
        ans.append(l)
        return ans

    test_cases_data = [
        "IDID",
        "III",
        "DDI",
        "I",
        "D",
        "ID",
        "DI",
        "DDDD",
        "IIII",
        "IDIDID"
    ]

    test_cases = []
    for i, s in enumerate(test_cases_data):
        inp = json.dumps(s)
        out = json.dumps(solve(s)).replace(" ", "")
        is_sample = i < 3
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
        "topics": ["Array", "Two Pointers", "String", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
