import json
import os

def generate_json():
    problem_id = 720
    title = "Longest Word in Dictionary"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>720. Longest Word in Dictionary</h3>
<p>Given an array of strings <code>words</code> representing an English Dictionary, return <em>the longest word in</em> <code>words</code> <em>that can be built one character at a time by other words in</em> <code>words</code>.</p>

<p>If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.</p>

<p>Note that the word should be built from left to right with each additional character being added to the end of the previous word.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["w","wo","wor","worl","world"]
<strong>Output:</strong> "world"
<strong>Explanation:</strong> The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["a","banana","app","appl","ap","apply","apple"]
<strong>Output:</strong> "apple"
<strong>Explanation:</strong> Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= words.length &lt;= 1000</code></li>
    <li><code>1 &lt;= words[i].length &lt;= 30</code></li>
    <li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line: JSON array of strings `words`."
    output_format = "A JSON string: the longest word."

    constraints = [
        "1 <= words.length <= 1000",
        "1 <= words[i].length <= 30",
        "words[i] consists of lowercase English letters"
    ]

    explanation = """Sort the words array lexicographically so that shorter prefixes naturally come first and alphabetical ties are already resolved. Use a set to keep track of words that can be built. Iterate over the sorted words; if a word has length 1 or its prefix (length - 1) is in the set, add it to the set and update the longest word found."""

    answer = """class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        built = set([""])
        longest = ""
        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def longestWord(self, words: list[str]) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        words = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.longestWord(words)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestWord(vector<string>& words) {
        // User logic here
        return "";
    }
};

vector<string> parseStringArray(string input) {
    vector<string> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '"') {
            size_t j = i + 1;
            string s = "";
            while (j < input.length() && input[j] != '"') s += input[j++];
            res.push_back(s);
            i = j + 1;
        } else i++;
    }
    return res;
}

int main() {
    string input;
    if (getline(cin, input)) {
        vector<string> words = parseStringArray(input);
        Solution sol;
        cout << "\\"" << sol.longestWord(words) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String longestWord(String[] words) {
        // User logic here
        return "";
    }
}

public class Main {
    static String[] parseStringArray(String raw) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < raw.length()) {
            if (raw.charAt(i) == '"') {
                int j = i + 1;
                StringBuilder sb = new StringBuilder();
                while (j < raw.length() && raw.charAt(j) != '"') sb.append(raw.charAt(j++));
                res.add(sb.toString());
                i = j + 1;
            } else i++;
        }
        return res.toArray(new String[0]);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            String[] words = parseStringArray(input);
            Solution sol = new Solution();
            System.out.println("\\"" + sol.longestWord(words) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} words
 * @return {string}
 */
var longestWord = function(words) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const words = JSON.parse(input);
    console.log(JSON.stringify(longestWord(words)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* longestWord(char** words, int wordsSize) {
    // User logic here
    char* res = (char*)malloc(1);
    res[0] = '\\0';
    return res;
}

int main() {
    char input[50000];
    if (fgets(input, sizeof(input), stdin)) {
        int cap = 100, size = 0, i = 0;
        char** words = (char**)malloc(cap * sizeof(char*));
        while (input[i]) {
            if (input[i] == '"') {
                int j = i + 1;
                while (input[j] && input[j] != '"') j++;
                if (size == cap) { cap *= 2; words = realloc(words, cap * sizeof(char*)); }
                words[size] = (char*)malloc(j - i);
                strncpy(words[size], input + i + 1, j - i - 1);
                words[size][j - i - 1] = '\\0';
                size++;
                i = j + 1;
            } else i++;
        }
        char* res = longestWord(words, size);
        printf("\\"%s\\"\\n", res);
        free(res);
        for(int k=0; k<size; k++) free(words[k]);
        free(words);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(words):
        words.sort()
        built = set([""])
        longest = ""
        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest

    test_cases_data = [
        ["w","wo","wor","worl","world"],
        ["a","banana","app","appl","ap","apply","apple"],
        ["a","b","c","d","e"],
        ["abcd","abc","ab","a"],
        ["m","mo","mon","monk","monkey","e","el","ele","elep","eleph","elepha","elephan","elephant"],
        ["a","ab","abc","abcd","z","zy","zyx","zyxw","zyxwv"],
        ["ogz","og","o","x","xy","xyz"],
        ["a"] * 1000,
        ["a" * i for i in range(1, 31)] * 30,
        ["b","ba","ban","bana","banan","banana","a","an","ant","ante","antel","antelo","antelop","antelope"]
    ]

    test_cases = []
    for i, words in enumerate(test_cases_data):
        inp = json.dumps(words)
        out = json.dumps(solve(words))
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
        "topics": ["Array", "Hash Table", "String", "Trie", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
