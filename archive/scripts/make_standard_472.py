import json
import os

def generate_json():
    problem_id = 472
    title = "Concatenated Words"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>472. Concatenated Words</h3>
<p>Given an array of strings <code>words</code> (<strong>without duplicates</strong>), return <em>all the <strong>concatenated words</strong> in the given array of words</em>.</p>

<p>A <strong>concatenated word</strong> is defined as a string that is comprised entirely of at least two shorter words (or the same word more than once) in the given array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
<strong>Output:</strong> ["catsdogcats","dogcatsdog","ratcatdogcat"]
<strong>Explanation:</strong> "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["cat","dog","catdog"]
<strong>Output:</strong> ["catdog"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
	<li>Total length of all words in <code>words</code> does not exceed <code>10<sup>5</sup></code>.</li>
</ul>"""

    input_format = "Line 1: A JSON array of strings `words`."
    output_format = "A JSON array of strings representing the concatenated words."
    
    constraints = [
        "1 <= words.length <= 10^4",
        "1 <= words[i].length <= 30",
        "words[i] consists of only lowercase English letters.",
        "All words are unique."
    ]
    
    explanation = "Use a Set for fast lookup of words. For each word, check if it can be formed by concatenating two or more shorter words from the set using DFS or dynamic programming. To avoid self-concatenation infinite recursion, temporarily remove the word from the set or ensure the segments are strictly shorter."
    
    answer = """class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}

        def can_form(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or can_form(suffix):
                        memo[word] = True
                        return True
            memo[word] = False
            return False

        res = []
        for w in words:
            if can_form(w):
                res.append(w)
        return res"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # User Logic Here
        return []

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        words = json.loads(line)
        sol = Solution()
        # Sort output for consistency
        res = sol.findAllConcatenatedWordsInADict(words)
        print(json.dumps(sorted(res)))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        // User Logic Here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> words;
        int i = 0;
        while(i < line.length()){
            if(line[i] == '\"'){
                i++;
                string word = "";
                while(i < line.length() && line[i] != '\"'){
                    word += line[i++];
                }
                words.push_back(word);
            }
            i++;
        }
        Solution sol;
        vector<string> res = sol.findAllConcatenatedWordsInADict(words);
        sort(res.begin(), res.end());
        cout << "[";
        for(int j=0; j<res.size(); j++){
            cout << "\"" << res[j] << "\"" << (j == res.size()-1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        // User Logic Here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            line = line.substring(1, line.length() - 1);
            String[] words;
            if(line.isEmpty()) words = new String[0];
            else {
                words = line.split(",\\\\s*");
                for(int i=0; i<words.length; i++) words[i] = words[i].replace("\"", "").trim();
            }
            Solution sol = new Solution();
            List<String> res = sol.findAllConcatenatedWordsInADict(words);
            Collections.sort(res);
            System.out.println(Arrays.toString(res.toArray()).replace(", ", ","));
        }
    }
}""",
        "javascript": r"""/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const words = JSON.parse(input);
    const res = findAllConcatenatedWordsInADict(words);
    console.log(JSON.stringify(res.sort()));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** findAllConcatenatedWordsInADict(char** words, int wordsSize, int* returnSize) {
    // User Logic Here
    *returnSize = 0;
    return NULL;
}

int main() {
    // Manual parsing logic...
    printf("[]\n");
    return 0;
}"""
    }

    test_cases = [
        {"input": "[\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\"]", "expected_output": "[\"catsdogcats\", \"dogcatsdog\", \"ratcatdogcat\"]", "is_sample": True},
        {"input": "[\"cat\",\"dog\",\"catdog\"]", "expected_output": "[\"catdog\"]", "is_sample": True},
        {"input": "[\"a\",\"b\",\"ab\"]", "expected_output": "[\"ab\"]", "is_sample": False},
        {"input": "[\"a\",\"b\",\"c\",\"abc\"]", "expected_output": "[\"abc\"]", "is_sample": False},
        {"input": "[\"a\",\"aa\",\"aaa\"]", "expected_output": "[\"aa\", \"aaa\"]", "is_sample": False},
        {"input": "[\"a\",\"b\",\"c\",\"ab\",\"abc\",\"bc\"]", "expected_output": "[\"ab\", \"abc\", \"bc\"]", "is_sample": False},
        {"input": "[\"abc\"]", "expected_output": "[]", "is_sample": False},
        {"input": "[\"ba\",\"na\",\"bana\",\"banana\"]", "expected_output": "[\"bana\", \"banana\"]", "is_sample": False},
        {"input": "[\"prefix\",\"suffix\",\"prefixsuffix\"]", "expected_output": "[\"prefixsuffix\"]", "is_sample": False},
        {"input": "[\"x\",\"y\",\"z\",\"xyz\"]", "expected_output": "[\"xyz\"]", "is_sample": False}
    ]

    data = {
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "String", "Dynamic Programming", "DFS", "Trie"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Concatenated_Words.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
