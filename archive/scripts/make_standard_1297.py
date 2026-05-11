import json
import os

def generate_json():
    problem_id = 1297
    title = "Maximum Number of Occurrences of a Substring"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1297. Maximum Number of Occurrences of a Substring</h3>
<p>Given a string <code>s</code>, return the maximum number of occurrences of <strong>any</strong> substring under the following rules:</p>

<ul>
	<li>The number of unique characters in the substring must be less than or equal to <code>maxLetters</code>.</li>
	<li>The substring size must be between <code>minSize</code> and <code>maxSize</code> inclusive.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring "aab" has 2 occurrences in the text. It satisfies the conditions: 2 unique letters and size 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring "aaa" occurs 2 times in the string. It can overlap.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= maxLetters &lt;= 26</code></li>
	<li><code>1 &lt;= minSize &lt;= maxSize &lt;= s.length</code></li>
	<li><code>minSize &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A string `s`, integers `maxLetters`, `minSize`, and `maxSize` provided as `[s, maxLetters, minSize, maxSize]` in JSON."
    output_format = "An integer representing the maximum occurrences."

    constraints = [
        "1 <= s.length <= 10^5",
        "1 <= maxLetters <= 26",
        "1 <= minSize <= maxSize <= s.length",
        "minSize <= 100"
    ]

    explanation = """To find the maximum number of occurrences of a substring:
1. Observe that if any substring of length between `minSize` and `maxSize` satisfies the `maxLetters` constraint, then its prefix of length exactly `minSize` also satisfies the same constraint and will occur at least as many times.
2. Therefore, we only need to consider substrings of length exactly `minSize`.
3. Iterate through the string `s` from index 0 to `len(s) - minSize`.
4. For each substring of length `minSize`:
   - Check if the number of unique characters is <= `maxLetters`.
   - If it satisfies the condition, increment its count in a frequency map.
5. The result is the maximum value in the frequency map."""

    answer = """import collections

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                count[sub] += 1
        return max(count.values()) if count else 0"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s, maxLetters, minSize, maxSize = json.loads(raw)
        sol = Solution()
        print(sol.maxFreq(s, maxLetters, minSize, maxSize))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        string s = j[0];
        int maxL = j[1];
        int minS = j[2];
        int maxS = j[3];
        Solution sol;
        cout << sol.maxFreq(s, maxL, minS, maxS) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
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
            String s = (String) data[0];
            int maxLetters = (Integer) data[1];
            int minSize = (Integer) data[2];
            int maxSize = (Integer) data[3];
            System.out.println(new Solution().maxFreq(s, maxLetters, minSize, maxSize));
        }
    }
}""",
        "javascript": """var maxFreq = function(s, maxLetters, minSize, maxSize) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [s, maxLetters, minSize, maxSize] = JSON.parse(input);
    console.log(maxFreq(s, maxLetters, minSize, maxSize));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxFreq(char * s, int maxLetters, int minSize, int maxSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for string/int parsing
    return 0;
}"""
    }

    import collections
    def solve(s, maxLetters, minSize, maxSize):
        count = collections.defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                count[sub] += 1
        return max(count.values()) if count else 0

    test_cases_data = [
        ["aababcaab", 2, 3, 4],    # Sample 1
        ["aaaa", 1, 3, 3],         # Sample 2
        ["abcde", 2, 3, 3],        # Unique > maxLetters
        ["aababcaab", 1, 2, 2],    # Smaller minSize
        ["abc", 3, 1, 3],          # maxSize variations
        ["", 2, 2, 2],             # Empty string (not possible per constraints but for safety)
        ["abcdefg", 7, 1, 7],      # Max unique
        # Stress tests
        ["a" * 10000, 1, 100, 100],
        ["ab" * 5000, 2, 2, 2],
        ["abcdefghij" * 1000, 10, 10, 10]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2], t[3])) if t[0] else "0"
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Hash Table", "Sliding Window"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
