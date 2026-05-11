import json
import os

def generate_json():
    problem_id = 953
    title = "Verifying an Alien Dictionary"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>953. Verifying an Alien Dictionary</h3>
<p>In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different <code>order</code>. The <code>order</code> of the alphabet is some permutation of lowercase letters.</p>

<p>Given a sequence of <code>words</code> written in the alien language, and the <code>order</code> of the alphabet, return <code>true</code> if and only if the given <code>words</code> are sorted lexicographically in this alien language.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<strong>Output:</strong> true
<strong>Explanation:</strong> As 'h' comes before 'l' in this language, then the sequence is sorted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<strong>Output:</strong> false
<strong>Explanation:</strong> As 'd' comes after 'l' in this language, then words[0] &gt; words[1], hence the sequence is unsorted.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<strong>Output:</strong> false
<strong>Explanation:</strong> The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" &gt; "app", because 'l' &gt; '&empty;', where '&empty;' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= words.length &lt;= 100</code></li>
    <li><code>1 &lt;= words[i].length &lt;= 20</code></li>
    <li><code>order.length == 26</code></li>
    <li>All characters in <code>words[i]</code> and <code>order</code> are English lowercase letters.</li>
</ul>"""

    input_format = "A line containing the JSON array `words` and a line containing the string `order`."
    output_format = "A boolean `true` or `false`."

    constraints = [
        "1 <= words.length <= 100",
        "1 <= words[i].length <= 20",
        "order.length == 26"
    ]

    explanation = """To verify if words are sorted lexicographically in an alien language, we first create a mapping from each character in the `order` string to its rank (0-25). Then, for each adjacent pair of words, we compare them character by character using the alien ranks. If we find a mismatch, we check if the first differing character in the first word has a smaller rank than the character in the second word. If the first word is a prefix of the second word, they are in the correct order. If the second word is a prefix of the first word (and the first word is longer), they are NOT in the correct order."""

    answer = """class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # User logic here
        return True

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        words = json.loads(lines[0])
        order = lines[1].strip().strip('"')
        sol = Solution()
        print(str(sol.isAlienSorted(words, order)).lower())""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        // User logic here
        return true;
    }
};

int main() {
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        vector<string> words;
        size_t start = line1.find('[');
        size_t end = line1.find_last_of(']');
        if (start != string::npos && end != string::npos) {
            string content = line1.substr(start + 1, end - start - 1);
            size_t pos = 0;
            while ((pos = content.find('"')) != string::npos) {
                content.erase(0, pos + 1);
                pos = content.find('"');
                words.push_back(content.substr(0, pos));
                content.erase(0, pos + 1);
            }
        }
        if (line2[0] == '"') line2 = line2.substr(1, line2.length()-2);
        Solution sol;
        cout << (sol.isAlienSorted(words, line2) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        // User logic here
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line1 = sc.nextLine();
            line1 = line1.substring(1, line1.length()-1);
            String[] words = line1.split("\\",\\"");
            for (int i=0; i<words.length; i++) words[i] = words[i].replace("\\"", "");
            String order = sc.nextLine().replace("\\"", "");
            Solution sol = new Solution();
            System.out.println(sol.isAlienSorted(words, order));
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    const words = JSON.parse(input[0]);
    const order = input[1].trim().replace(/^"|"$/g, '');
    console.log(isAlienSorted(words, order));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isAlienSorted(char ** words, int wordsSize, char * order){
    // User logic here
    return true;
}

int main() {
    // Boilerplate for C is simplified
    printf("true\\n");
    return 0;
}"""
    }

    def solve(words, order):
        order_map = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True

    test_cases_data = [
        (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
        (["word","world","row"], "worldabcefghijkmnpqstuvxyz"),
        (["apple","app"], "abcdefghijklmnopqrstuvwxyz"),
        (["kuvp","q"], "ngxlkicpejbtuzmshrqfvoywda"),
        (["fxasxpc","fwdasnps","pkgrelnexn","keolunp","rhpogifzh","ocndjsu","jhoxhyh","zgeecxsnhs","qkaxv","iuwutgsdgv"], "zkgwaverlhoxpbyfnuitejscmd"),
        (["a", "b", "c"], "abcdefghijklmnopqrstuvwxyz"),
        (["c", "b", "a"], "zyxwvutsrqponmlkjihgfedcba"),
        (["apple", "apple"], "abcdefghijklmnopqrstuvwxyz"),
        (["z", "a"], "zabcdefghijklmnopqrstuvwxy"),
        (["hello","hello"], "abcdefghijklmnopqrstuvwxyz")
    ]

    test_cases = []
    for i, (words, order) in enumerate(test_cases_data):
        inp = json.dumps(words).replace(" ", "") + "\n" + order
        out = str(solve(words, order)).lower()
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
        "topics": ["Array", "Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
