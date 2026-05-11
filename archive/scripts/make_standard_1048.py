import json
import os

def generate_json():
    problem_id = 1048
    title = "Longest String Chain"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1048. Longest String Chain</h3>
<p>You are given an array of <code>words</code> where each word consists of lowercase English letters.</p>

<p>Word <code>A</code> is a <strong>predecessor</strong> of word <code>B</code> if and only if you can insert <strong>exactly one</strong> letter anywhere in word <code>A</code> (without changing the order of the other characters) to make it equal to word <code>B</code>.</p>

<ul>
	<li>For example, <code>"abc"</code> is a <strong>predecessor</strong> of <code>"abac"</code>, while <code>"cba"</code> is not a <strong>predecessor</strong> of <code>"bcad"</code>.</li>
</ul>

<p>A <strong>word chain</strong><em> </em>is a sequence of words <code>[word<sub>1</sub>, word<sub>2</sub>, ..., word<sub>k</sub>]</code> with <code>k &gt;= 1</code>, where <code>word<sub>1</sub></code> is a predecessor of <code>word<sub>2</sub></code>, <code>word<sub>2</sub></code> is a predecessor of <code>word<sub>3</sub></code>, and so on. A single word is trivially a word chain with <code>k = 1</code>.</p>

<p>Return <em>the <strong>length</strong> of the longest possible word chain with words chosen from the given list of </em><code>words</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["a","b","ba","bca","bda","bdca"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One of the longest word chains is ["a","ba","bda","bdca"].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
<strong>Output:</strong> 5
<strong>Explanation:</strong> All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["abcd","dbqca"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The trivial word chain ["abcd"] is one of the longest word chains. ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 16</code></li>
	<li><code>words[i]</code> only consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing the JSON array `words`."
    output_format = "An integer representing the length of the longest word chain."

    constraints = [
        "1 <= words.length <= 1000",
        "1 <= words[i].length <= 16",
        "words[i] only consists of lowercase English letters"
    ]

    explanation = """Sort the words by their lengths. 
Use a dynamic programming approach where `dp[word]` stores the length of the longest chain ending with `word`.
For each word, try removing one character at a time to find a potential predecessor. 
If the predecessor is in our list of words, `dp[word] = max(dp[word], dp[predecessor] + 1)`.
The answer is the maximum value in `dp`."""

    answer = """class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        dp = {}
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                if prev in dp:
                    dp[w] = max(dp[w], dp[prev] + 1)
        return max(dp.values())"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        words = json.loads(raw)
        sol = Solution()
        print(sol.longestStrChain(words))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestStrChain(vector<string>& words) {
        // User logic here
        return 0;
    }
};

vector<string> parseArray(string s) {
    vector<string> res;
    string current = "";
    bool inQuote = false;
    for (char c : s) {
        if (c == '"') {
            if (inQuote) {
                res.push_back(current);
                current = "";
                inQuote = false;
            } else {
                inQuote = true;
            }
        } else if (inQuote) {
            current += c;
        }
    }
    return res;
}

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> words = parseArray(line);
        Solution sol;
        cout << sol.longestStrChain(words) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int longestStrChain(String[] words) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String[] words = parse(sc.nextLine());
            System.out.println(new Solution().longestStrChain(words));
        }
    }
    private static String[] parse(String s) {
        s = s.trim();
        if (s.equals("[]")) return new String[0];
        s = s.substring(1, s.length() - 1);
        String[] parts = s.split(",");
        for (int i = 0; i < parts.length; i++) {
            parts[i] = parts[i].trim();
            parts[i] = parts[i].substring(1, parts[i].length() - 1);
        }
        return parts;
    }
}""",
        "javascript": """var longestStrChain = function(words) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(longestStrChain(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int longestStrChain(char** words, int wordsSize) {
    // User logic here
    return 0;
}

char** parseArray(int* size) {
    char c;
    while (scanf(" %c", &c) == 1 && c != '[');
    int capacity = 100, s = 0;
    char** arr = malloc(capacity * sizeof(char*));
    char temp[100];
    while (scanf(" %c", &c) == 1 && c == '"') {
        int i = 0;
        while (scanf("%c", &c) == 1 && c != '"') temp[i++] = c;
        temp[i] = '\\0';
        if (s == capacity) { capacity *= 2; arr = realloc(arr, capacity * sizeof(char*)); }
        arr[s++] = strdup(temp);
        while (scanf(" %c", &c) == 1 && (c == ' ' || c == ','));
        if (c == ']') break;
        ungetc(c, stdin);
    }
    *size = s;
    return arr;
}

int main() {
    int size;
    char** words = parseArray(&size);
    printf("%d\\n", longestStrChain(words, size));
    for (int i = 0; i < size; i++) free(words[i]);
    free(words);
    return 0;
}"""
    }

    def solve(words):
        words.sort(key=len)
        dp = {}
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                if prev in dp:
                    dp[w] = max(dp[w], dp[prev] + 1)
        return max(dp.values()) if dp else 0

    test_cases_data = [
        ["a","b","ba","bca","bda","bdca"], # LC Sample 1
        ["xbc","pcxbcf","xb","cxbc","pcxbc"], # LC Sample 2
        ["abcd","dbqca"],                   # LC Sample 3
        ["a","ab","abc"],
        ["ba","a"],
        ["qwer","qwe","qw","q"],
        ["a","b","c","d"],
        # Stress tests (last 3)
        ["a"] * 100,
        ["abcde", "abcd", "abc", "ab", "a"],
        [chr(97+i) for i in range(26)]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Two Pointers", "String", "Dynamic Programming"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
