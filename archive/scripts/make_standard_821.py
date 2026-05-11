import json
import os

def generate_json():
    problem_id = 821
    title = "Shortest Distance to a Character"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>821. Shortest Distance to a Character</h3>
<p>Given a string <code>s</code> and a character <code>c</code> that occurs in <code>s</code>, return <em>an array of integers </em><code>answer</code><em> where </em><code>answer.length == s.length</code><em> and </em><code>answer[i]</code><em> is the <strong>distance</strong> from index </em><code>i</code><em> to the <strong>closest</strong> occurrence of character </em><code>c</code><em> in </em><code>s</code>.</p>

<p>The <strong>distance</strong> between two indices <code>i</code> and <code>j</code> is <code>abs(i - j)</code>, where <code>abs</code> is the absolute value function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "loveleetcode", c = "e"
<strong>Output:</strong> [3,2,1,0,1,0,0,1,2,2,1,0]
<strong>Explanation:</strong> The character 'e' appears at indices 3, 5, 6, and 11.
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 4 is at index 3 or 5, so the distance is abs(4 - 3) = 1 or abs(4 - 5) = 1.
The distance for index 6 is 0 because s[6] is 'e'.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaab", c = "b"
<strong>Output:</strong> [3,2,1,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
    <li><code>s[i]</code> and <code>c</code> are lowercase English letters.</li>
    <li>It is guaranteed that <code>c</code> occurs at least once in <code>s</code>.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: string `s`\nLine 2: character `c`"
    output_format = "A JSON array of integers representing the distances."

    constraints = [
        "1 <= s.length <= 10000",
        "c exists in s"
    ]

    explanation = """To find the shortest distance to a character, we can perform two passes over the string. In the first pass (left-to-right), we record the distance to the last seen occurrence of `c`. In the second pass (right-to-left), we do the same and take the minimum of the two distances."""

    answer = """class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [0] * n
        pos = -float('inf')
        for i in range(n):
            if s[i] == c: pos = i
            res[i] = i - pos
        pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c: pos = i
            res[i] = min(res[i], pos - i)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        s = raw[0].strip().strip('"')
        c = raw[1].strip().strip('"')
        sol = Solution()
        print(json.dumps(sol.shortestToChar(s, c)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        // User logic here
        return {};
    }
};

int main() {
    string s; char c;
    if (cin >> s >> c) {
        if (s.front() == '"') s = s.substr(1, s.length()-2);
        Solution sol;
        vector<int> res = sol.shortestToChar(s, c);
        cout << "[";
        for (int i=0; i<res.size(); i++) cout << res[i] << (i+1==res.size()?"":",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] shortestToChar(String s, char c) {
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
            if (sc.hasNext()) {
                char c = sc.next().charAt(0);
                Solution sol = new Solution();
                int[] res = sol.shortestToChar(s, c);
                System.out.print("[");
                for (int i=0; i<res.length; i++) System.out.print(res[i] + (i+1==res.length?"":","));
                System.out.println("]");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    let s = input[0].trim();
    if (s.startsWith('"')) s = JSON.parse(s);
    let c = input[1].trim();
    if (c.startsWith('"')) c = JSON.parse(c);
    console.log(JSON.stringify(shortestToChar(s, c)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* shortestToChar(char* s, char c, int* returnSize) {
    // User logic here
    return NULL;
}

int main() {
    char s[10001], c;
    if (scanf("%s %c", s, &c) == 2) {
        int outSz;
        int* res = shortestToChar(s, c, &outSz);
        printf("[");
        for (int i=0; i<outSz; i++) printf("%d%s", res[i], i+1==outSz?"":",");
        printf("]\\n");
    }
    return 0;
}"""
    }

    def solve(s, c):
        n = len(s)
        res = [0] * n
        pos = -100000
        for i in range(n):
            if s[i] == c: pos = i
            res[i] = i - pos
        pos = 100000
        for i in range(n - 1, -1, -1):
            if s[i] == c: pos = i
            res[i] = min(res[i], pos - i)
        return res

    test_cases_data = [
        ("loveleetcode", "e"),
        ("aaab", "b"),
        ("a", "a"),
        ("abracadabra", "a"),
        ("z", "z"),
        ("baaaaa", "b"),
        ("aaaaa", "a"),
        ("hello world", "l"),
        ("abcde fghij", " "),
        ("aaaaaaaaaa", "a")
    ]

    test_cases = []
    for i, (s, c) in enumerate(test_cases_data):
        inp = json.dumps(s).replace(" ", "") + "\n" + json.dumps(c).replace(" ", "")
        out = json.dumps(solve(s, c)).replace(" ", "")
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
        "topics": ["Array", "Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
