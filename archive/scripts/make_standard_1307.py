import json
import os

def generate_json():
    problem_id = 1307
    title = "Verbal Arithmetic Puzzle"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1307. Verbal Arithmetic Puzzle</h3>
<p>Given an equation, represented by <code>words</code> on the left side and the <code>result</code> on the right side.</p>

<p>You need to check if the equation is solvable under the following rules:</p>

<ul>
	<li>Each character is decoded as one digit (0-9).</li>
	<li>No two characters can map to the same digit.</li>
	<li>Each <code>words[i]</code> and <code>result</code> cannot start with 0 if its length is greater than 1.</li>
	<li>Sum of the values of the words on the left side equals the value of <code>result</code> on the right side.</li>
	<li>Return <code>true</code> if the equation is solvable, otherwise return <code>false</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["SEND","MORE"], result = "MONEY"
<strong>Output:</strong> true
<strong>Explanation:</strong> Map 'S'->9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->2.
'SEND' + 'MORE' = 9567 + 1085 = 10652 = 'MONEY'
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
<strong>Output:</strong> true
<strong>Explanation:</strong> Map 'S'->6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->3, 'Y'->4.
'SIX' + 'SEVEN' + 'SEVEN' = 650 + 68782 + 68782 = 138214 = 'TWENTY'
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> words = ["LEET","CODE"], result = "POINT"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= words.length &lt;= 8</code></li>
	<li><code>1 &lt;= words[i].length, result.length &lt;= 7</code></li>
	<li><code>words[i], result</code> contain only uppercase English letters.</li>
	<li>The number of different characters used in the equation is at most <code>10</code>.</li>
</ul>"""

    input_format = "A list of `words` and a `result` string provided as `[words, result]` in JSON."
    output_format = "A boolean value `true` or `false`."

    constraints = [
        "2 <= words.length <= 8",
        "1 <= words[i].length, result.length <= 7",
        "At most 10 different characters"
    ]

    explanation = """To solve the verbal arithmetic puzzle:
1. Identify all unique characters in the words and result.
2. Use backtracking to assign a unique digit (0-9) to each character.
3. Optimize the backtracking:
   - Instead of assigning all digits and then checking the sum, solve the equation column by column starting from the rightmost (unit's place).
   - At each column `j`:
     - Assign digits to unmapped characters in `words[i][-j]` and `result[-j]`.
     - Check if the sum of characters in the current column (including carry) matches the digit assigned to `result[-j]`.
     - If yes, proceed to the next column `j+1`.
4. Ensure that no character that is the first letter of a word (with length > 1) is assigned the digit 0."""

    answer = """class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        all_words = words + [result]
        max_len = max(len(w) for w in all_words)
        if len(result) < max_len: return False
        
        char_to_digit = {}
        digit_to_char = [None] * 10
        leading_chars = {w[0] for w in all_words if len(w) > 1}
        
        def backtrack(col, row, carry):
            if col == len(result):
                return carry == 0
            
            if row == len(words):
                res_char = result[-(col + 1)]
                target = (carry % 10)
                if res_char in char_to_digit:
                    if char_to_digit[res_char] == target:
                        return backtrack(col + 1, 0, carry // 10)
                    else:
                        return False
                else:
                    if digit_to_char[target] is None:
                        if target == 0 and res_char in leading_chars:
                            return False
                        char_to_digit[res_char] = target
                        digit_to_char[target] = res_char
                        if backtrack(col + 1, 0, carry // 10):
                            return True
                        digit_to_char[target] = None
                        del char_to_digit[res_char]
                    return False
            
            word = words[row]
            if col >= len(word):
                return backtrack(col, row + 1, carry)
            
            char = word[-(col + 1)]
            if char in char_to_digit:
                return backtrack(col, row + 1, carry + char_to_digit[char])
            else:
                for d in range(10):
                    if digit_to_char[d] is None:
                        if d == 0 and char in leading_chars:
                            continue
                        char_to_digit[char] = d
                        digit_to_char[d] = char
                        if backtrack(col, row + 1, carry + d):
                            return True
                        digit_to_char[d] = None
                        del char_to_digit[char]
                return False
                
        return backtrack(0, 0, 0)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        words, result = json.loads(raw)
        sol = Solution()
        print(str(sol.isSolvable(words, result)).lower())""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool isSolvable(vector<string>& words, string result) {
        // User logic here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<string> words = j[0].get<vector<string>>();
        string result = j[1];
        Solution sol;
        cout << (sol.isSolvable(words, result) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public boolean isSolvable(String[] words, String result) {
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
            String[] words = mapper.convertValue(data[0], String[].class);
            String result = (String) data[1];
            System.out.println(new Solution().isSolvable(words, result));
        }
    }
}""",
        "javascript": """var isSolvable = function(words, result) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [words, result] = JSON.parse(input);
    console.log(isSolvable(words, result));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isSolvable(char ** words, int wordsSize, char * result){
    // User logic here
    return false;
}

int main() {
    // Boilerplate for string/array parsing
    return 0;
}"""
    }

    def solve(words, result):
        all_words = words + [result]
        max_len = max(len(w) for w in all_words)
        if len(result) < max_len: return False
        char_to_digit = {}
        digit_to_char = [None] * 10
        leading_chars = {w[0] for w in all_words if len(w) > 1}
        def backtrack(col, row, carry):
            if col == len(result): return carry == 0
            if row == len(words):
                res_char = result[-(col + 1)]
                target = (carry % 10)
                if res_char in char_to_digit:
                    if char_to_digit[res_char] == target: return backtrack(col + 1, 0, carry // 10)
                    else: return False
                else:
                    if digit_to_char[target] is None:
                        if target == 0 and res_char in leading_chars: return False
                        char_to_digit[res_char] = target
                        digit_to_char[target] = res_char
                        if backtrack(col + 1, 0, carry // 10): return True
                        digit_to_char[target] = None
                        del char_to_digit[res_char]
                    return False
            word = words[row]
            if col >= len(word): return backtrack(col, row + 1, carry)
            char = word[-(col + 1)]
            if char in char_to_digit: return backtrack(col, row + 1, carry + char_to_digit[char])
            else:
                for d in range(10):
                    if digit_to_char[d] is None:
                        if d == 0 and char in leading_chars: continue
                        char_to_digit[char] = d
                        digit_to_char[d] = char
                        if backtrack(col, row + 1, carry + d): return True
                        digit_to_char[d] = None
                        del char_to_digit[char]
                return False
        return backtrack(0, 0, 0)

    test_cases_data = [
        [["SEND","MORE"], "MONEY"],     # Sample 1
        [["SIX","SEVEN","SEVEN"], "TWENTY"], # Sample 2
        [["LEET","CODE"], "POINT"],     # Sample 3
        [["A","B"], "C"],               # Simple single
        [["A","A"], "AA"],              # Carry to next
        [["THAT","IS","WHY"], "THEY"],  # Medium
        [["THIS","IS","TOO"], "FUNNY"], # Large
        # Stress tests
        [["A","B","C","D","E","F","G","H"], "ABCDEFGH"], # Many words
        [["AB","CD","EF"], "GHIJ"],     # Many chars
        [["I","LIKE","LEET"], "CODE"]
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
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Math", "String", "Backtracking"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
