import json
import os

def generate_json():
    problem_id = 1255
    title = "Maximum Score Words Formed by Letters"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1255. Maximum Score Words Formed by Letters</h3>
<p>Given a list of <code>words</code>, list of single <code>letters</code> (might be repeating) and <code>score</code> of every character.</p>

<p>Return the maximum score of <strong>any</strong> valid set of words formed by using the given letters (<code>words[i]</code> cannot be used two or more times).</p>

<p>It is not necessary to use all characters in <code>letters</code> and each letter can only be used once. Score of letters <code>'a'</code>, <code>'b'</code>, <code>'c'</code>, ... , <code>'z'</code> is given by <code>score[0]</code>, <code>score[1]</code>, ... , <code>score[25]</code> respectively.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
<strong>Output:</strong> 23
<strong>Explanation:</strong>
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a total score of 23.
Words "dad" and "dog" only get a score of 21.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
<strong>Output:</strong> 27
<strong>Explanation:</strong>
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a total score of 27.
Word "xxxz" only get a score of 25.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Letter "e" can only be used once.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= words.length &lt;= 14</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 15</code></li>
	<li><code>1 &lt;= letters.length &lt;= 100</code></li>
	<li><code>letters[i].length == 1</code></li>
	<li><code>score.length == 26</code></li>
	<li><code>0 &lt;= score[i] &lt;= 10</code></li>
	<li><code>words[i]</code>, <code>letters[i]</code> contains only lower case English letters.</li>
</ul>"""

    input_format = "A list of `words`, a list of `letters`, and a `score` array provided as `[words, letters, score]` in JSON."
    output_format = "An integer representing the maximum score."

    constraints = [
        "1 <= words.length <= 14",
        "1 <= letters.length <= 100",
        "score.length == 26"
    ]

    explanation = """To find the maximum score:
1. Since the number of words is very small (<= 14), we can explore all possible subsets of words using backtracking.
2. For each word in the current subset, check if it can be formed using the remaining letters.
3. Keep track of character counts in a frequency map or array.
4. For each word choice:
   - Try including it if the required character counts are available.
   - Recurse to the next word.
   - Backtrack by restoring the character counts.
5. Also explore the case where the current word is skipped.
6. The maximum score found during the recursion is the final result."""

    answer = """import collections

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        count = collections.Counter(letters)
        
        def backtrack(i):
            if i == len(words):
                return 0
            
            # Skip current word
            res = backtrack(i + 1)
            
            # Try to include current word
            word = words[i]
            word_count = collections.Counter(word)
            can_form = True
            current_score = 0
            for char, c in word_count.items():
                if count[char] < c:
                    can_form = False
                current_score += score[ord(char) - ord('a')] * c
            
            if can_form:
                for char, c in word_count.items():
                    count[char] -= c
                res = max(res, current_score + backtrack(i + 1))
                # Backtrack
                for char, c in word_count.items():
                    count[char] += c
            
            return res
            
        return backtrack(0)"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        words, letters, score = json.loads(raw)
        sol = Solution()
        print(sol.maxScoreWords(words, letters, score))""",
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
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<string> w = j[0].get<vector<string>>();
        string l_str = j[1].get<string>(); // handle char array if provided as string
        vector<char> l;
        for(char c : l_str) if(c >= 'a' && c <= 'z') l.push_back(c);
        if(j[1].is_array()) {
            l.clear();
            for(auto& v : j[1]) l.push_back(v.get<string>()[0]);
        }
        vector<int> s = j[2].get<vector<int>>();
        Solution sol;
        cout << sol.maxScoreWords(w, l, s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
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
            String[] w = mapper.convertValue(data[0], String[].class);
            List<String> lList = mapper.convertValue(data[1], List.class);
            char[] l = new char[lList.size()];
            for(int i=0; i<lList.size(); i++) l[i] = lList.get(i).charAt(0);
            int[] s = mapper.convertValue(data[2], int[].class);
            System.out.println(new Solution().maxScoreWords(w, l, s));
        }
    }
}""",
        "javascript": """var maxScoreWords = function(words, letters, score) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [w, l, s] = JSON.parse(input);
    console.log(maxScoreWords(w, l, s));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxScoreWords(char ** words, int wordsSize, char * letters, int lettersSize, int * score, int scoreSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    import collections
    def solve(words, letters, score):
        count = collections.Counter(letters)
        def backtrack(i):
            if i == len(words): return 0
            res = backtrack(i + 1)
            word = words[i]
            word_count = collections.Counter(word)
            can_form = True
            current_score = 0
            for char, c in word_count.items():
                if count[char] < c: can_form = False
                current_score += score[ord(char) - ord('a')] * c
            if can_form:
                for char, c in word_count.items(): count[char] -= c
                res = max(res, current_score + backtrack(i + 1))
                for char, c in word_count.items(): count[char] += c
            return res
        return backtrack(0)

    test_cases_data = [
        [["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]], # Sample 1
        [["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]], # Sample 2
        [["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]], # Sample 3
        [["a"], ["a"], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], # Simple
        [["a", "a"], ["a"], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], # Duplicate word
        [["abc"], ["a","b","c"], [1,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], # Exactly match
        [["abcdefghijklmnopqrstuvwxyz"], ["a"], [1]*26], # Missing letters
        # Stress tests
        [["a"]*14, ["a"]*10, [1]*26], # 14 words max
        ["a" + str(i) for i in range(14)], # (Wait, lowercase only)
        [["a"]*14, ["a"]*100, [10]*26], # Max score
        [["abcdefghijklmno"], ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"], [1]*26]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "String", "Dynamic Programming", "Backtracking", "Bit Manipulation"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
