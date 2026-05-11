import json
import os

def generate_json():
    problem_id = 1007
    title = "Minimum Domino Rotations For Equal Row"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1007. Minimum Domino Rotations For Equal Row</h3>
<p>In a row of dominoes, <code>tops[i]</code> and <code>bottoms[i]</code> represent the top and bottom halves of the <code>i<sup>th</sup></code> domino. (A domino is a tile with two numbers from 1-6 - one on each half of the tile.)</p>

<p>We may rotate the <code>i<sup>th</sup></code> domino, so that <code>tops[i]</code> and <code>bottoms[i]</code> swap values.</p>

<p>Return the minimum number of rotations so that all the values in <code>tops</code> are the same, or all the values in <code>bottoms</code> are the same.</p>

<p>If it cannot be done, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/03/08/domino.png" style="width: 421px; height: 161px;" />
<pre><strong>Input:</strong> tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations, each domino is as follows: [2,5], [1,2], [2,6], [4,2], [2,3], [2,2].
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 
In this case, it is not possible to make every value in the top row or bottom row equal to 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>2 &lt;= tops.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>bottoms.length == tops.length</code></li>
    <li><code>1 &lt;= tops[i], bottoms[i] &lt;= 6</code></li>
</ul>"""

    input_format = "Two JSON arrays `tops` and `bottoms` on two separate lines."
    output_format = "An integer representing the minimum rotations or -1."

    constraints = [
        "2 <= tops.length <= 20000",
        "bottoms.length == tops.length",
        "1 <= tops[i], bottoms[i] <= 6"
    ]

    explanation = """To make all values in a row equal to X, X must be a value present in the first domino (either tops[0] or bottoms[0]). 
There are at most two candidate values. For each candidate, we calculate the minimum rotations needed to make the top row all that value or the bottom row all that value.
If a domino contains neither candidate, that candidate is invalid. We return the minimum of all valid rotation counts, or -1 if none exist."""

    answer = """class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def check(x):
            rot_a = rot_b = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rot_a += 1
                elif bottoms[i] != x:
                    rot_b += 1
            return min(rot_a, rot_b)
        
        res = min(check(tops[0]), check(bottoms[0]))
        return res if res != float('inf') else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    if len(input_data) >= 2:
        tops = json.loads(input_data[0])
        bottoms = json.loads(input_data[1])
        sol = Solution()
        print(sol.minDominoRotations(tops, bottoms))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        // User logic here
        return -1;
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
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        vector<int> tops = parseArray(line1);
        vector<int> bottoms = parseArray(line2);
        Solution sol;
        cout << sol.minDominoRotations(tops, bottoms) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        // User logic here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[] tops = parse(sc.nextLine());
            int[] bottoms = parse(sc.nextLine());
            System.out.println(new Solution().minDominoRotations(tops, bottoms));
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
        "javascript": """var minDominoRotations = function(tops, bottoms) {
    // User logic here
    return -1;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    console.log(minDominoRotations(JSON.parse(input[0]), JSON.parse(input[1])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minDominoRotations(int* tops, int topsSize, int* bottoms, int bottomsSize) {
    // User logic here
    return -1;
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
    int s1, s2;
    int* tops = parseArray(&s1);
    int* bottoms = parseArray(&s2);
    printf("%d\\n", minDominoRotations(tops, s1, bottoms, s2));
    free(tops); free(bottoms);
    return 0;
}"""
    }

    def solve(tops, bottoms):
        def check(x):
            rot_a = rot_b = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x: return 10**9
                if tops[i] != x: rot_a += 1
                if bottoms[i] != x: rot_b += 1
            return min(rot_a, rot_b)
        res = min(check(tops[0]), check(bottoms[0]))
        return res if res < 10**9 else -1

    test_cases_data = [
        ([2,1,2,4,2,2], [5,2,6,2,3,2]), # LC Sample 1
        ([3,5,1,2,3], [3,6,3,3,4]),     # LC Sample 2
        ([1,1,1,1,1,1], [1,1,1,1,1,1]), # All same
        ([1,2,3,4,5,6], [1,1,1,1,1,1]), # bottoms all same
        ([1,1,1,1,1,1], [1,2,3,4,5,6]), # tops all same
        ([1,2,1,2,1,2], [2,1,2,1,2,1]), # Alternating
        ([1,2,3,4,5,6], [6,5,4,3,2,1]), # Impossible
        # Stress tests (last 3): No spaces in input strings
        ([1]*1000 + [2]*1000, [2]*1000 + [1]*1000), 
        ([1]*2000, [6]*2000),
        ([1,2]*500, [2,1]*500)
    ]

    test_cases = []
    for i, (t, b) in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "") + "\n" + json.dumps(b).replace(" ", "")
        out = str(solve(t, b))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Greedy"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
