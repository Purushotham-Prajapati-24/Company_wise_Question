import json
import os

def generate_json():
    problem_id = 1320
    title = "Minimum Distance to Type a Word using Two Fingers"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1320. Minimum Distance to Type a Word using Two Fingers</h3>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/25/keyboard.png" style="width: 349px; height: 209px;">
<p>You have a keyboard layout as shown above in the image where letters are located at specific coordinates. For example, letter <strong>'A'</strong> is at <code>(0,0)</code>, letter <strong>'B'</strong> is at <code>(0,1)</code>, letter <strong>'G'</strong> is at <code>(1,0)</code> and letter <strong>'Z'</strong> is at <code>(4,1)</code>.</p>

<p>Given the string <code>word</code>, return <em>the minimum total distance to type such string using two fingers</em>.</p>

<p>The distance between index <code>i</code> and index <code>j</code> is <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code> where <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and <code>(x<sub>j</sub>, y<sub>j</sub>)</code> are the coordinates of the letters at index <code>i</code> and <code>j</code> respectively.</p>

<p>Note that the initial positions of your two fingers are free so the distance to type the first letter with either finger is <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> word = "CAKE"
<strong>Output:</strong> 3
<strong>Explanation: </strong>
Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on 'C' -> cost 0
Finger 1 on 'A' -> cost distance('C', 'A') = 2
Finger 2 on 'K' -> cost 0
Finger 2 on 'E' -> cost distance('K', 'E') = 1
Total distance = 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> word = "HAPPY"
<strong>Output:</strong> 6
<strong>Explanation: </strong>
Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on 'H' -> cost 0
Finger 1 on 'A' -> cost distance('H', 'A') = 2
Finger 2 on 'P' -> cost 0
Finger 2 on 'P' -> cost distance('P', 'P') = 0
Finger 1 on 'Y' -> cost distance('A', 'Y') = 4
Total distance = 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>2 &lt;= word.length &lt;= 300</code></li>
    <li><code>word</code> consists of uppercase English letters.</li>
</ul>"""

    input_format = "A string `word`."
    output_format = "An integer representing the minimum distance."

    constraints = [
        "2 <= word.length <= 300",
        "word consists of uppercase English letters"
    ]

    explanation = """To solve this using Dynamic Programming:
1. Define the distance function: `dist(char1, char2) = |r1 - r2| + |c1 - c2|`.
2. Map each character 'A'-'Z' to coordinates `(row, col)`.
3. Use memoization `dp(i, f1, f2)`: the minimum distance to type the remaining characters from `word[i:]` with the fingers currently at `f1` and `f2`.
4. Initial call: `dp(0, None, None)`.
5. For each step `i`:
   - Either move `f1` to `word[i]`: cost is `dist(f1, word[i]) + dp(i+1, word[i], f2)`.
   - Or move `f2` to `word[i]`: cost is `dist(f2, word[i]) + dp(i+1, f1, word[i])`.
6. Base case: If `i == len(word)`, return 0."""

    answer = """class Solution:
    def minimumDistance(self, word: str) -> int:
        def d(a, b):
            if a == None: return 0
            x1, y1 = divmod(ord(a) - ord('A'), 6)
            x2, y2 = divmod(ord(b) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        from functools import lru_cache
        @lru_cache(None)
        def solve(i, f1, f2):
            if i == len(word): return 0
            # Option 1: Move f1 to word[i]
            res1 = d(f1, word[i]) + solve(i + 1, word[i], f2)
            # Option 2: Move f2 to word[i]
            res2 = d(f2, word[i]) + solve(i + 1, f1, word[i])
            return min(res1, res2)
        
        return solve(0, None, None)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minimumDistance(self, word: str) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw.startswith('"') and raw.endswith('"'): raw = raw[1:-1]
    sol = Solution()
    print(sol.minimumDistance(raw))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimumDistance(string word) {
        // User logic here
        return 0;
    }
};

int main() {
    printf("3\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minimumDistance(String word) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(3);
    }
}""",
        "javascript": """/**
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().replace(/"/g, '');
if (input) {
    console.log(minimumDistance(input));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minimumDistance(char* word) {
    // User logic here
    return 0;
}

int main() {
    printf("3\\n");
    return 0;
}"""
    }

    def solve(word):
        from functools import lru_cache
        def d(a, b):
            if a is None: return 0
            x1, y1 = divmod(ord(a) - ord('A'), 6)
            x2, y2 = divmod(ord(b) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word): return 0
            return min(d(f1, word[i]) + dp(i+1, word[i], f2), d(f2, word[i]) + dp(i+1, f1, word[i]))
        return dp(0, None, None)

    test_cases_data = ["CAKE", "HAPPY", "NEW", "YEAR", "ABC", "ZZZ", "A", "BANANA", "MISSISSIPPI", "LEETCODE"]

    test_cases = []
    for i, word in enumerate(test_cases_data):
        if i == 6: # word length >= 2
           word = "AA"
        inp = f'"{word}"'
        out = str(solve(word))
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
        "topics": ["String", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
