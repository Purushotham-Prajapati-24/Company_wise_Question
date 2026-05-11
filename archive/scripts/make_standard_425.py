import json
import os

def generate_json():
    problem_id = 425
    title = "Word Squares"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>425. Word Squares</h3>
<p>Given an array of <strong>unique</strong> strings <code>words</code>, return <em>all the </em><strong>word squares</strong><em> that can be formed from </em><code>words</code>. You can return the answer in <strong>any order</strong>.</p>

<p>A sequence of strings forms a <strong>word square</strong> if the <code>k<sup>th</sup></code> row and column read the same string, where <code>0 &lt;= k &lt; max(numRows, numColumns)</code>.</p>

<ul>
	<li>For example, the sequence <code>["ball","area","lead","lady"]</code> forms a word square because each word reads the same horizontally and vertically.</li>
</ul>

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["area","lead","wall","lady","ball"]
<strong>Output:</strong> [["ball","area","lead","lady"],["wall","area","lead","lady"]]
<strong>Explanation:</strong>
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["abat","baba","atan","atal"]
<strong>Output:</strong> [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
<strong>Explanation:</strong>
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 4</code></li>
	<li>All <code>words[i]</code> have the same length.</li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li>All <code>words[i]</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A JSON array of unique strings `words`."
    output_format = "A JSON array of arrays of strings representing all possible word squares."
    
    constraints = [
        "1 <= words.length <= 1000",
        "1 <= words[i].length <= 4",
        "All words have the same length.",
        "Words consist of lowercase English letters.",
        "All words are unique."
    ]
    
    explanation = """A word square of size N x N must satisfy square[i][j] == square[j][i].
This means if we have already chosen the first 'i' rows, the next row (row 'i') must start with a prefix formed by the characters at square[0][i], square[1][i], ..., square[i-1][i].
We can use a Trie or a hash map to quickly look up all words that start with a given prefix to efficiently build the square row by row using backtracking."""
    
    answer = """class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        prefixes = {}
        for w in words:
            for i in range(n):
                prefix = w[:i]
                if prefix not in prefixes:
                    prefixes[prefix] = []
                prefixes[prefix].append(w)
        
        results = []
        
        def backtrack(step, current_square):
            if step == n:
                results.append(list(current_square))
                return
            
            prefix = "".join([word[step] for word in current_square])
            if prefix not in prefixes:
                return
            
            for candidate in prefixes[prefix]:
                current_square.append(candidate)
                backtrack(step + 1, current_square)
                current_square.pop()
        
        for word in words:
            backtrack(1, [word])
            
        return results"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        # User Logic Here
        pass

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        try:
            words = json.loads(raw_input)
            sol = Solution()
            result = sol.wordSquares(words)
            print(json.dumps(result).replace(" ", ""))
        except:
            pass""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        // User Logic Here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> words;
        int i = 0;
        while (i < line.length()) {
            if (line[i] == '\"') {
                int j = i + 1;
                while (j < line.length() && line[j] != '\"') j++;
                words.push_back(line.substr(i + 1, j - i - 1));
                i = j;
            }
            i++;
        }
        Solution sol;
        vector<vector<string>> res = sol.wordSquares(words);
        cout << "[";
        for (int k = 0; k < res.size(); k++) {
            if (k > 0) cout << ",";
            cout << "[";
            for (int l = 0; l < res[k].size(); l++) {
                if (l > 0) cout << ",";
                cout << "\\\"" << res[k][l] << "\\\"";
            }
            cout << "]";
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<List<String>> wordSquares(String[] words) {
        // User Logic Here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            List<String> wordList = new ArrayList<>();
            int i = 0;
            while (i < line.length()) {
                if (line.charAt(i) == '\"') {
                    int j = i + 1;
                    while (j < line.length() && line.charAt(j) != '\"') j++;
                    wordList.add(line.substring(i + 1, j));
                    i = j;
                }
                i++;
            }
            Solution sol = new Solution();
            List<List<String>> res = sol.wordSquares(wordList.toArray(new String[0]));
            StringBuilder sb = new StringBuilder();
            sb.append(\"[\");
            for (int k = 0; k < res.size(); k++) {
                if (k > 0) sb.append(\",\");
                sb.append(\"[\");
                for (int l = 0; l < res.get(k).size(); l++) {
                    if (l > 0) sb.append(\",\");
                    sb.append(\"\\\"\").append(res.get(k).get(l)).append(\"\\\"\");
                }
                sb.append(\"]\");
            }
            sb.append(\"]\");
            System.out.println(sb.toString());
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} words
 * @return {string[][]}
 */
var wordSquares = function(words) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const words = JSON.parse(input);
    const result = wordSquares(words);
    console.log(JSON.stringify(result).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** wordSquares(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    // User Logic Here
    *returnSize = 0;
    return NULL;
}

int main() {
    char line[100000];
    if (fgets(line, sizeof(line), stdin)) {
        char* words[1000];
        int wordsSize = 0;
        int i = 0;
        while (line[i]) {
            if (line[i] == '\"') {
                int j = i + 1;
                while (line[j] && line[j] != '\"') j++;
                line[j] = '\\0';
                words[wordsSize++] = line + i + 1;
                i = j;
            }
            i++;
        }
        int returnSize = 0;
        int* returnColumnSizes = NULL;
        char*** res = wordSquares(words, wordsSize, &returnSize, &returnColumnSizes);
        printf(\"[\");
        for (int k = 0; k < returnSize; k++) {
            if (k > 0) printf(\",\");
            printf(\"[\");
            for (int l = 0; l < returnColumnSizes[k]; l++) {
                if (l > 0) printf(\",\");
                printf(\"\\\"%s\\\"\", res[k][l]);
            }
            printf(\"]\");
        }
        printf(\"]\\n\");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '["area","lead","wall","lady","ball"]', "expected_output": '[["ball","area","lead","lady"],["wall","area","lead","lady"]]', "is_sample": True},
        {"input": '["abat","baba","atan","atal"]', "expected_output": '[["baba","abat","baba","atan"],["baba","abat","baba","atal"]]', "is_sample": True},
        {"input": '["a"]', "expected_output": '[["a"]]', "is_sample": False},
        {"input": '["ab", "ba"]', "expected_output": '[["ab","ba"],["ba","ab"]]', "is_sample": False},
        {"input": '["abcd","bcde","cdef","defg"]', "expected_output": '[]', "is_sample": False},
        {"input": '["wall","area","lead","lady","ball","abcd"]', "expected_output": '[["ball","area","lead","lady"],["wall","area","lead","lady"]]', "is_sample": False},
        {"input": '["ball",  "area",  "lead", "lady"]', "expected_output": '[["ball","area","lead","lady"]]', "is_sample": False}, # anomalous spaces
        {"input": '[ "a", "b" ]', "expected_output": '[["a"],["b"]]', "is_sample": False}, # anomalous spaces
        # Stress
        {"input": '["poll","oils","lily","lays"]', "expected_output": '[["poll","oils","lily","lays"]]', "is_sample": False},
        {"input": '[]', "expected_output": '[]', "is_sample": False}
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
        "topics": ["Trie", "Backtracking"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
