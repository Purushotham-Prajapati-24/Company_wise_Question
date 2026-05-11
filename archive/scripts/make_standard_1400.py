import json
import os

def generate_json():
    problem_id = 1400
    title = "Construct K Palindrome Strings"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1400. Construct K Palindrome Strings</h3>
<p>Given a string <code>s</code> and an integer <code>k</code>, return <code>true</code> <em>if you can use all the characters in </em><code>s</code><em> to construct </em><code>k</code><em> palindrome strings or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "annabelle", k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anblelbna" + "e", "anellena" + "b"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "leetcode", k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to construct 3 palindromes using all the characters of s.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "true", k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> The only possible solution is to put each character in a separate palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A string `s` and an integer `k` provided as `[s, k]` in JSON."
    output_format = "A boolean value `true` or `false`."

    constraints = [
        "1 <= s.length <= 10^5",
        "1 <= k <= 10^5"
    ]

    explanation = """To determine if it's possible to construct `k` palindrome strings from `s`:
1. The first condition is that the total number of characters in `s` must be at least `k`. If `len(s) < k`, return `false` because we need at least one character for each palindrome.
2. Every palindrome string can have at most one character with an odd frequency (the middle element).
3. Therefore, if the number of characters with odd frequencies in `s` is `odd_count`, then we need at least `odd_count` palindromes to accommodate them.
4. If `odd_count > k`, return `false`.
5. Otherwise, we can always distribute the characters to form `k` palindromes. Return `true`."""

    answer = """import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        count = collections.Counter(s)
        odd_count = 0
        for char in count:
            if count[char] % 2 != 0:
                odd_count += 1
                
        return odd_count <= k"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s, k = json.loads(raw)
        sol = Solution()
        print(str(sol.canConstruct(s, k)).lower())""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool canConstruct(string s, int k) {
        // User logic here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        string s = j[0];
        int k = j[1];
        Solution sol;
        cout << (sol.canConstruct(s, k) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public boolean canConstruct(String s, int k) {
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
            System.out.println(new Solution().canConstruct((String)data[0], (Integer)data[1]));
        }
    }
}""",
        "javascript": """var canConstruct = function(s, k) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [s, k] = JSON.parse(input);
    console.log(canConstruct(s, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool canConstruct(char * s, int k){
    // User logic here
    return false;
}

int main() {
    // Boilerplate for string/int parsing
    return 0;
}"""
    }

    import collections
    def solve(s, k):
        if len(s) < k: return False
        count = collections.Counter(s)
        odd_count = sum(1 for char in count if count[char] % 2 != 0)
        return odd_count <= k

    test_cases_data = [
        ["annabelle", 2],      # Sample 1
        ["leetcode", 3],       # Sample 2
        ["true", 4],           # Sample 3
        ["a", 1],              # Single
        ["aa", 1],             # Even
        ["aa", 2],             # Split
        ["abcdefg", 1],        # One long
        # Stress tests
        ["a" * 100000, 1],
        ["a" * 100000, 100000],
        ["abcde" * 20000, 5]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1])).lower()
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Hash Table", "String", "Greedy"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
