import json
import os

def generate_json():
    problem_id = 781
    title = "Rabbits in Forest"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>781. Rabbits in Forest</h3>
<p>There is a forest with an unknown number of rabbits. We asked n rabbits <strong>"How many rabbits have the same color as you?"</strong> and collected the answers in an integer array <code>answers</code> where <code>answers[i]</code> is the answer of the <code>i<sup>th</sup></code> rabbit.</p>

<p>Given the array <code>answers</code>, return <em>the minimum number of rabbits that could be in the forest</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> answers = [1,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> answers = [10,10,10]
<strong>Output:</strong> 11
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= answers.length &lt;= 1000</code></li>
    <li><code>0 &lt;= answers[i] &lt; 1000</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `answers`."
    output_format = "An integer representing the minimum total number of rabbits."

    constraints = [
        "1 <= answers.length <= 1000",
        "0 <= answers[i] < 1000"
    ]

    explanation = """If a rabbit answers `x`, then there's a group of `x + 1` rabbits with the same color. If `y` rabbits answer `x`, they can be grouped into ceil(y / (x + 1)) different colors. Thus the minimal amount of rabbits in the forest is sum of ceil(y / (x + 1)) * (x + 1) for every answer `x` over all unique answers."""

    answer = """import collections
import math

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = collections.Counter(answers)
        return sum(math.ceil(v / (k + 1)) * (k + 1) for k, v in count.items())"""

    boilerplate = {
        "python": """import sys
import json
import collections
import math

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        answers = json.loads(raw)
        sol = Solution()
        print(sol.numRabbits(answers))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution {
public:
    int numRabbits(vector<int>& answers) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string s) {
    vector<int> res;
    int i = 1;
    while(i < s.length() - 1) {
        if(isdigit(s[i])) {
            int val = 0;
            while(isdigit(s[i])) val = val * 10 + (s[i++] - '0');
            res.push_back(val);
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string s;
    if (cin >> s) {
        vector<int> answers = parseArray(s);
        Solution sol;
        cout << sol.numRabbits(answers) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numRabbits(int[] answers) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String raw = sc.next();
            raw = raw.substring(1, raw.length() - 1);
            if (raw.isEmpty()) {
                Solution sol = new Solution();
                System.out.println(sol.numRabbits(new int[0]));
                return;
            }
            String[] parts = raw.split(",");
            int[] answers = new int[parts.length];
            for (int i = 0; i < parts.length; i++) answers[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.numRabbits(answers));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function(answers) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(numRabbits(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int numRabbits(int* answers, int answersSize) {
    // User logic here
    return 0;
}

int main() {
    int cap = 1000;
    int* answers = (int*)malloc(cap * sizeof(int));
    int size = 0;
    char c;
    while ((c = getchar()) != EOF) {
        if (c == '[') continue;
        if (c == ']') break;
        if (c >= '0' && c <= '9') {
            ungetc(c, stdin);
            int val;
            scanf("%d", &val);
            if(size == cap) { cap *= 2; answers = realloc(answers, cap * sizeof(int)); }
            answers[size++] = val;
        }
    }
    printf("%d\\n", numRabbits(answers, size));
    free(answers);
    return 0;
}"""
    }

    import math
    import collections
    def solve(answers):
        count = collections.Counter(answers)
        return sum(math.ceil(v / (k + 1)) * (k + 1) for k, v in count.items())

    test_cases_data = [
        [1,1,2],
        [10,10,10],
        [0,0,1,1,1],
        [1]*10,
        [2,2,2,2,2],
        [0,0,0,0,0],
        [999,999,999],
        [1,2,3,4,5],
        [5,5,5,5,5,5,5],
        [2,1,2,2,2,2,2,2,1,1]
    ]

    test_cases = []
    for i, answers in enumerate(test_cases_data):
        inp = json.dumps(answers).replace(" ", "")
        out = str(solve(answers))
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
        "topics": ["Hash Table", "Math", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
