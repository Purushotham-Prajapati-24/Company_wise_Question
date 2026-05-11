import json
import os

def generate_json():
    problem_id = 739
    title = "Daily Temperatures"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>739. Daily Temperatures</h3>
<p>Given an array of integers <code>temperatures</code> representing the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= temperatures.length &lt;= 10<sup>5</sup></code></li>
    <li><code>30 &lt;= temperatures[i] &lt;= 100</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `temperatures`."
    output_format = "A JSON array of integers representing the number of days to wait."

    constraints = [
        "1 <= temperatures.length <= 10^5",
        "30 <= temperatures[i] <= 100"
    ]

    explanation = """Use a monotonic decreasing stack to keep track of indices of temperatures. Iterate through the array. For each current temperature, while the stack is not empty and the current temperature is strictly greater than the temperature at the index on the top of the stack, pop the index from the stack and set the answer for that popped index to the difference between the current index and the popped index. Finally, push the current index onto the stack."""

    answer = """class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        temperatures = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.dailyTemperatures(temperatures)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // User logic here
        return {};
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            int val = 0;
            while (i < input.length() && isdigit(input[i])) {
                val = val * 10 + (input[i] - '0');
                i++;
            }
            res.push_back(val);
        } else i++;
    }
    return res;
}

int main() {
    string n_str;
    if (getline(cin, n_str)) {
        vector<int> temperatures = parseArray(n_str);
        Solution sol;
        vector<int> res = sol.dailyTemperatures(temperatures);
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
    public int[] dailyTemperatures(int[] temperatures) {
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
            int[] temperatures = parseArray(n_str);
            Solution sol = new Solution();
            int[] res = sol.dailyTemperatures(temperatures);
            System.out.print("[");
            for (int i = 0; i < res.length; i++) {
                System.out.print(res[i] + (i + 1 == res.length ? "" : ","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const temperatures = JSON.parse(input);
    console.log(JSON.stringify(dailyTemperatures(temperatures)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
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
    char n_str[2000000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int temperaturesSize;
        int* temperatures = parseArray(n_str, &temperaturesSize);
        int returnSize = 0;
        int* res = dailyTemperatures(temperatures, temperaturesSize, &returnSize);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("%d%s", res[i], i == returnSize - 1 ? "" : ",");
        }
        printf("]\\n");
        free(temperatures);
        if(res) free(res);
    }
    return 0;
}"""
    }

    def solve(temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans

    test_cases_data = [
        [73,74,75,71,69,72,76,73],
        [30,40,50,60],
        [30,60,90],
        [90,80,70,60],
        [100,100,100],
        [30],
        [30]*50000 + [31]*50000,
        [90,80,70,60,50,40,30,40,50,60,70,80,90],
        [x for x in range(100, 29, -1)] * 1000,
        [30] * 99999 + [100]
    ]

    test_cases = []
    for i, temperatures in enumerate(test_cases_data):
        inp = json.dumps(temperatures)
        out = json.dumps(solve(temperatures)).replace(" ", "")
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
        "topics": ["Array", "Stack", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
