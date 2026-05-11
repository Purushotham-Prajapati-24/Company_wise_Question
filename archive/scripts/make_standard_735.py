import json
import os

def generate_json():
    problem_id = 735
    title = "Asteroid Collision"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>735. Asteroid Collision</h3>
<p>We are given an array <code>asteroids</code> of integers representing asteroids in a row.</p>

<p>For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.</p>

<p>Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> asteroids = [5,10,-5]
<strong>Output:</strong> [5,10]
<strong>Explanation:</strong> The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> asteroids = [8,-8]
<strong>Output:</strong> []
<strong>Explanation:</strong> The 8 and -8 collide exploding each other.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> asteroids = [10,2,-5]
<strong>Output:</strong> [10]
<strong>Explanation:</strong> The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>2 &lt;= asteroids.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-1000 &lt;= asteroids[i] &lt;= 1000</code></li>
    <li><code>asteroids[i] != 0</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `asteroids`."
    output_format = "A JSON array of integers."

    constraints = [
        "2 <= asteroids.length <= 10^4",
        "-1000 <= asteroids[i] <= 1000",
        "asteroids[i] != 0"
    ]

    explanation = """Use a stack to track moving asteroids. Iterate through the asteroids. If an asteroid is moving right (positive), push it to the stack. If it's moving left (negative), it could collide with asteroids moving right. Pop from the stack as long as the top asteroid is moving right and is smaller than the current left-moving asteroid. Handle identical sizes by popping but not pushing the negative asteroid."""

    answer = """class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        asteroids = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.asteroidCollision(asteroids)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        // User logic here
        return {};
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '-' || isdigit(input[i])) {
            int sign = 1, val = 0;
            if (input[i] == '-') { sign = -1; i++; }
            while (i < input.length() && isdigit(input[i])) {
                val = val * 10 + (input[i] - '0');
                i++;
            }
            res.push_back(val * sign);
        } else i++;
    }
    return res;
}

int main() {
    string n_str;
    if (getline(cin, n_str)) {
        vector<int> asteroids = parseArray(n_str);
        Solution sol;
        vector<int> res = sol.asteroidCollision(asteroids);
        cout << "[";
        for (size_t i = 0; i < res.size(); ++i) {
            cout << res[i] << (i + 1 == res.size() ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String n_str = sc.nextLine().trim();
            int[] asteroids = parseArray(n_str);
            Solution sol = new Solution();
            int[] res = sol.asteroidCollision(asteroids);
            System.out.print("[");
            for (int i = 0; i < res.length; i++) {
                System.out.print(res[i] + (i + 1 == res.length ? "" : ","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const asteroids = JSON.parse(input);
    console.log(JSON.stringify(asteroidCollision(asteroids)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '-' || isdigit(input[i])) {
            int val, off = 0;
            sscanf(input+i, "%d%n", &val, &off);
            if (!off) { i++; continue; }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
            res[size++] = val;
            i += off;
        } else i++;
    }
    *outSize = size;
    return res;
}

int main() {
    char n_str[200000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int asteroidsSize;
        int* asteroids = parseArray(n_str, &asteroidsSize);
        int returnSize = 0;
        int* res = asteroidCollision(asteroids, asteroidsSize, &returnSize);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("%d%s", res[i], i == returnSize - 1 ? "" : ",");
        }
        printf("]\\n");
        free(asteroids);
        if(res) free(res);
    }
    return 0;
}"""
    }

    def solve(asteroids):
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack

    test_cases_data = [
        [5,10,-5],
        [8,-8],
        [10,2,-5],
        [-2,-1,1,2],
        [1,2,3,-4,5,-6],
        [-2,1,1,-1],
        [-2,2,1,-2],
        [x for x in range(1, 5001)] + [-5001],
        [x for x in range(1000, 0, -1)] + [-x for x in range(1, 1001)],
        [-10]*5000 + [10]*5000
    ]

    test_cases = []
    for i, asteroids in enumerate(test_cases_data):
        inp = json.dumps(asteroids)
        out = json.dumps(solve(asteroids)).replace(" ", "")
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
        "topics": ["Array", "Stack", "Simulation"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
