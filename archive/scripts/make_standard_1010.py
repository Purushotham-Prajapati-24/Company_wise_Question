import json
import os

def generate_json():
    problem_id = 1010
    title = "Pairs of Songs With Total Durations Divisible by 60"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1010. Pairs of Songs With Total Durations Divisible by 60</h3>
<p>You are given a list of songs where the <code>i<sup>th</sup></code> song has a duration of <code>time[i]</code> seconds.</p>

<p>Return <em>the number of pairs of songs for which their total duration in seconds is divisible by <code>60</code></em>. Formally, we want the number of indices <code>i</code>, <code>j</code> such that <code>i &lt; j</code> with <code>(time[i] + time[j]) % 60 == 0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> time = [30,20,150,100,40]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> time = [60,60,60]
<strong>Output:</strong> 3
<strong>Explanation:</strong> All three pairs have a total duration of 120, which is divisible by 60.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= time.length &lt;= 6 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `time`."
    output_format = "An integer representing the number of valid pairs."

    constraints = [
        "1 <= time.length <= 60000",
        "1 <= time[i] <= 500"
    ]

    explanation = """We use a frequency array of size 60 to store the count of song durations with each remainder when divided by 60. 
For each song with duration `t`, the remainder is `r = t % 60`. 
The required remainder for a pair is `target = (60 - r) % 60`. 
We add the count of songs with remainder `target` to our result and then increment the count for remainder `r`."""

    answer = """class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        remainders = [0] * 60
        count = 0
        for t in time:
            r = t % 60
            target = (60 - r) % 60
            count += remainders[target]
            remainders[r] += 1
        return count"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        time = json.loads(raw)
        sol = Solution()
        print(sol.numPairsDivisibleBy60(time))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string s) {
    vector<int> res;
    string temp = "";
    for (char c : s) {
        if (isdigit(c)) temp += c;
        else if (temp != "") {
            res.push_back(stoi(temp));
            temp = "";
        }
    }
    if (temp != "") res.push_back(stoi(temp));
    return res;
}

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> time = parseArray(line);
        Solution sol;
        cout << sol.numPairsDivisibleBy60(time) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[] time = parse(sc.nextLine());
            System.out.println(new Solution().numPairsDivisibleBy60(time));
        }
    }
    private static int[] parse(String s) {
        s = s.replaceAll("[\\[\\] ]", "");
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i]);
        return res;
    }
}""",
        "javascript": """var numPairsDivisibleBy60 = function(time) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(numPairsDivisibleBy60(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int numPairsDivisibleBy60(int* time, int timeSize) {
    // User logic here
    return 0;
}

int* parseArray(int* size) {
    char c;
    while (scanf(" %c", &c) == 1 && c != '[');
    int capacity = 100, s = 0;
    int* arr = malloc(capacity * sizeof(int));
    int val;
    while (scanf("%d", &val) == 1) {
        if (s == capacity) { capacity *= 2; arr = realloc(arr, capacity * sizeof(int)); }
        arr[s++] = val;
        while (scanf(" %c", &c) == 1 && (c == ' ' || c == ','));
        if (c == ']') break;
        ungetc(c, stdin);
    }
    *size = s;
    return arr;
}

int main() {
    int size;
    int* time = parseArray(&size);
    printf("%d\\n", numPairsDivisibleBy60(time, size));
    free(time);
    return 0;
}"""
    }

    def solve(time):
        remainders = [0] * 60
        res = 0
        for t in time:
            r = t % 60
            res += remainders[(60 - r) % 60]
            remainders[r] += 1
        return res

    test_cases_data = [
        [30, 20, 150, 100, 40], # LC Sample 1
        [60, 60, 60],           # LC Sample 2
        [30, 30, 30, 30],       # Multiple pairs
        [0, 60, 120, 180],      # Multiple of 60
        [1, 59, 2, 58, 3, 57],    # Multiple valid pairs
        [1, 2, 3, 4, 5],        # No valid pairs
        [30] * 100,             # Large number of identical remainders
        # Stress tests (last 3)
        [60] * 1000,
        [30] * 2000,
        list(range(1, 501)) * 40
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Counting"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
