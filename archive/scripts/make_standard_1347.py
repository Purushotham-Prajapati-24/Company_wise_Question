import json
import os

def generate_json():
    problem_id = 1347
    title = "Minimum Number of Steps to Make Two Strings Anagram"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1347. Minimum Number of Steps to Make Two Strings Anagram</h3>
<p>You are given two strings of the same length <code>s</code> and <code>t</code>. In one step you can choose <strong>any character</strong> of <code>t</code> and replace it with <strong>another character</strong>.</p>

<p>Return <em>the minimum number of steps</em> to make <code>t</code> an anagram of <code>s</code>.</p>

<p>An <strong>Anagram</strong> of a string is a string that contains the same characters with a different (or the same) ordering.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "bab", t = "aba"
<strong>Output:</strong> 1
<strong>Explanation:</strong> Replace the first 'a' in t with b, t = "bba" which is anagram of s.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "leetcode", t = "practice"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Replace 'p', 'r', 'a', 'i', 'c' from t with proper characters to make t anagram of s.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "mangaar"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "anagram" and "mangaar" are anagrams. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s.length == t.length</code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters only.</li>
</ul>"""

    input_format = "Two strings `s` and `t` provided as `[s, t]` in JSON."
    output_format = "An integer representing the minimum steps."

    constraints = [
        "1 <= s.length <= 5 * 10^4",
        "s.length == t.length",
        "Lowercase English letters only"
    ]

    explanation = """To make `t` an anagram of `s`:
1. Count the frequency of each character in both strings `s` and `t`.
2. For each unique character in `s`, compare its count in `s` with its count in `t`.
3. If `count_s[char] > count_t[char]`, then we need `count_s[char] - count_t[char]` more occurrences of this character in `t`.
4. The total number of steps is the sum of these differences for all characters.
5. Alternatively, since the strings have the same length, the sum of positive differences (needs) will equal the sum of negative differences (surplus)."""

    answer = """import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        
        res = 0
        for char in count_s:
            if count_s[char] > count_t[char]:
                res += count_s[char] - count_t[char]
        return res"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s, t = json.loads(raw)
        sol = Solution()
        print(sol.minSteps(s, t))""",
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
    int minSteps(string s, string t) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        string s = j[0];
        string t = j[1];
        Solution sol;
        cout << sol.minSteps(s, t) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minSteps(String s, String t) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            System.out.println(new Solution().minSteps((String)data[0], (String)data[1]));
        }
    }
}""",
        "javascript": """var minSteps = function(s, t) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [s, t] = JSON.parse(input);
    console.log(minSteps(s, t));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minSteps(char * s, char * t){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    import collections
    def solve(s, t):
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        res = 0
        for char in count_s:
            if count_s[char] > count_t[char]:
                res += count_s[char] - count_t[char]
        return res

    test_cases_data = [
        ["bab", "aba"],               # Sample 1
        ["leetcode", "practice"],      # Sample 2
        ["anagram", "mangaar"],        # Sample 3
        ["a", "b"],                    # Single
        ["aa", "bb"],                  # Double
        ["abc", "def"],                # All diff
        ["", ""],                      # Empty (not per constraints but handled)
        # Stress tests
        ["a" * 10000, "b" * 10000],
        ["a" * 5000 + "b" * 5000, "b" * 5000 + "a" * 5000],
        ["abcdefghijklmnopqrstuvwxyz" * 100, "zyxwvutsrqponmlkjihgfedcba" * 100]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1])) if t[0] or t[1] else "0"
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Hash Table", "String"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
