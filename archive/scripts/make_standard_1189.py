import json
import os

def generate_json():
    problem_id = 1189
    title = "Maximum Number of Balloons"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1189. Maximum Number of Balloons</h3>
<p>Given a string <code>text</code>, you want to use the characters of <code>text</code> to form as many instances of the word <strong>"balloon"</strong> as possible.</p>

<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> text = "nlaebolko"
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> text = "loonbalxballpoon"
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> text = "leetcode"
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code> consists of lower case English letters only.</li>
</ul>"""

    input_format = "A string `text` enclosed in quotes as a JSON string."
    output_format = "An integer representing the number of instances."

    constraints = [
        "1 <= text.length <= 10^4",
        "text consists of lower case English letters only"
    ]

    explanation = """To find the maximum number of "balloon" instances:
1. Count the frequency of each char in the text.
2. The word "balloon" contains: 'b':1, 'a':1, 'l':2, 'o':2, 'n':1.
3. Calculate how many "balloon"s can be formed for each character specifically:
   - For 'b', 'a', 'n': `count // 1`
   - For 'l', 'o': `count // 2`
4. The result is the minimum of these values."""

    answer = """class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = collections.Counter(text)
        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        text = json.loads(raw)
        sol = Solution()
        print(sol.maxNumberOfBalloons(text))""",
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
    int maxNumberOfBalloons(string text) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        string text = json::parse(line);
        Solution sol;
        cout << sol.maxNumberOfBalloons(text) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maxNumberOfBalloons(String text) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String text = mapper.readValue(sc.nextLine(), String.class);
            System.out.println(new Solution().maxNumberOfBalloons(text));
        }
    }
}""",
        "javascript": """var maxNumberOfBalloons = function(text) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(maxNumberOfBalloons(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxNumberOfBalloons(char * text){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    import collections
    def solve(text):
        counts = collections.Counter(text)
        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])

    test_cases_data = [
        "nlaebolko",        # Sample 1
        "loonbalxballpoon", # Sample 2
        "leetcode",         # Sample 3
        "balloon",          # Exactly one
        "ballnnnn",         # Missing o, a
        "baaaaallllloooonn", # Extra a, l, o, n
        "abcdefghijklmnopqrstuvwxyz", # One of each
        # Stress tests
        "balloon" * 1000,
        "b" * 10000,
        "a" * 2000 + "b" * 2000 + "l" * 2000 + "o" * 2000 + "n" * 2000
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
        "topics": ["Hash Table", "String", "Counting"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
