import json
import os

def generate_json():
    problem_id = 809
    title = "Expressive Words"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>809. Expressive Words</h3>
<p>Sometimes people repeat letters to represent extra feeling. For example, "hello" -> "heeellooo", "hi" -> "hiiii". In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".</p>

<p>You are given a string <code>s</code> and an array of query strings <code>words</code>. A query word is <strong>stretchy</strong> if it can be made to be equal to <code>s</code> by any number of applications of the following extension operation: choose a group consisting of characters <code>c</code>, and add some number of characters <code>c</code> to the group so that the size of the group is <strong>three or more</strong>.</p>

<p>For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". Note that we cannot get "hello" from "helo" by extending "ll" because "ll" is not size 3 or more (in "helo", "l" is size 1).</p>

<p>Return <em>the number of query strings that are <strong>stretchy</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "heeellooo", words = ["hello", "hi", "helo"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We cannot extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "zzzzzyyyyy", words = ["zzyy", "zy", "zyy"]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 100</code></li>
    <li><code>1 &lt;= words.length &lt;= 100</code></li>
    <li><code>1 &lt;= words[i].length &lt;= 100</code></li>
    <li><code>s</code> and all <code>words[i]</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: string `s`\nLine 2: JSON array of strings `words`"
    output_format = "An integer representing the count of stretchy words."

    constraints = [
        "1 <= s.length <= 100",
        "1 <= words.length <= 100",
        "1 <= words[i].length <= 100",
        "All characters are lowercase English letters"
    ]

    explanation = """To determine if a word matches a target string `s`, we can shrink both into a sequence of (character, count) pairs. For each group, the character must match. If the count in `s` is smaller than the count in the word, it's impossible. If the count in `s` is larger than the count in the word, but less than 3, it's also impossible because you can only extend to a group of size 3 or more."""

    answer = """class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        def get_groups(word):
            if not word: return []
            res = []
            char = word[0]
            count = 0
            for c in word:
                if c == char:
                    count += 1
                else:
                    res.append((char, count))
                    char = c
                    count = 1
            res.append((char, count))
            return res
        
        s_groups = get_groups(s)
        ans = 0
        for w in words:
            w_groups = get_groups(w)
            if len(s_groups) != len(w_groups):
                continue
            is_stretchy = True
            for i in range(len(s_groups)):
                sc, sn = s_groups[i]
                wc, wn = w_groups[i]
                if sc != wc or sn < wn or (sn > wn and sn < 3):
                    is_stretchy = False
                    break
            if is_stretchy:
                ans += 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        s = raw[0].strip().strip('"')
        words = json.loads(raw[1].strip())
        sol = Solution()
        print(sol.expressiveWords(s, words))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int expressiveWords(string s, vector<string>& words) {
        // User logic here
        return 0;
    }
};

int main() {
    string s, arrStr;
    if (cin >> s >> arrStr) {
        if (s.front() == '"') s = s.substr(1, s.length()-2);
        // Basic parser for string array
        vector<string> words;
        size_t i = 1;
        while (i < arrStr.length()-1) {
            if (arrStr[i] == '"') {
                i++; size_t start = i;
                while (arrStr[i] != '"') i++;
                words.push_back(arrStr.substr(start, i - start));
                i++;
            } else i++;
        }
        Solution sol;
        cout << sol.expressiveWords(s, words) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int expressiveWords(String s, String[] words) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine().trim();
            if (s.startsWith("\\"")) s = s.substring(1, s.length()-1);
            if (sc.hasNextLine()) {
                String arrStr = sc.nextLine().trim();
                arrStr = arrStr.substring(1, arrStr.length()-1);
                String[] words;
                if (arrStr.isEmpty()) words = new String[0];
                else {
                    String[] parts = arrStr.split(",");
                    words = new String[parts.length];
                    for (int i=0; i<parts.length; i++) {
                        String p = parts[i].trim();
                        words[i] = p.substring(1, p.length()-1);
                    }
                }
                Solution sol = new Solution();
                System.out.println(sol.expressiveWords(s, words));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var expressiveWords = function(s, words) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    let s = input[0].trim();
    if (s.startsWith('"')) s = JSON.parse(s);
    let words = JSON.parse(input[1].trim());
    console.log(expressiveWords(s, words));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int expressiveWords(char* s, char** words, int wordsSize) {
    // User logic here
    return 0;
}

int main() {
    char s[102], arrStr[20000];
    if (scanf("%s %s", s, arrStr) == 2) {
        char *ptr_s = s;
        if (s[0] == '"') {
            s[strlen(s)-1] = '\\0';
            ptr_s = s + 1;
        }
        int cap = 100, sz = 0;
        char** words = malloc(cap * sizeof(char*));
        size_t i = 1;
        while (arrStr[i] && arrStr[i+1]) {
            if (arrStr[i] == '"') {
                i++; size_t start = i;
                while (arrStr[i] != '"') i++;
                int len = i - start;
                words[sz] = malloc(len + 1);
                strncpy(words[sz], arrStr + start, len);
                words[sz][len] = '\\0';
                sz++; i++;
            } else i++;
        }
        printf("%d\\n", expressiveWords(ptr_s, words, sz));
    }
    return 0;
}"""
    }

    def solve(s, words):
        def get_groups(word):
            if not word: return []
            res = []
            char = word[0]
            count = 0
            for c in word:
                if c == char:
                    count += 1
                else:
                    res.append((char, count))
                    char = c
                    count = 1
            res.append((char, count))
            return res
        s_g = get_groups(s)
        ans = 0
        for w in words:
            w_g = get_groups(w)
            if len(s_g) != len(w_g): continue
            match = True
            for i in range(len(s_g)):
                if s_g[i][0] != w_g[i][0] or s_g[i][1] < w_g[i][1] or (s_g[i][1] > w_g[i][1] and s_g[i][1] < 3):
                    match = False; break
            if match: ans += 1
        return ans

    test_cases_data = [
        ("heeellooo", ["hello", "hi", "helo"]),
        ("zzzzzyyyyy", ["zzyy", "zy", "zyy"]),
        ("abcd", ["abcd", "abc"]),
        ("aaa", ["a", "aa", "aaa"]),
        ("aaabbb", ["ab", "aa", "bbb"]),
        ("sassss", ["sa", "sas"]),
        ("heeello", ["hello"]),
        ("helllo", ["hello"]),
        ("hheellloo", ["hello"]),
        ("aaa", ["aaaa"])
    ]

    test_cases = []
    for i, (s, words) in enumerate(test_cases_data):
        inp = json.dumps(s).replace(" ", "") + "\n" + json.dumps(words).replace(" ", "")
        out = str(solve(s, words))
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

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
