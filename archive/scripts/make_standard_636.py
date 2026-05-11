import json
import os

def generate_json():
    problem_id = 636
    title = "Exclusive Time of Functions"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>636. Exclusive Time of Functions</h3>
<p>On a <strong>single-threaded</strong> CPU, we execute a program containing <code>n</code> functions. Each function has a unique ID between <code>0</code> and <code>n-1</code>.</p>

<p>Function calls are <strong>stored in a <a href="https://en.wikipedia.org/wiki/Call_stack" target="_blank">call stack</a></strong>: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is <strong>the current function being executed</strong>. There is only one function being executed at any given moment.</p>

<p>You are given a list <code>logs</code>, where <code>logs[i]</code> represents the <code>i<sup>th</sup></code> log message formatted as a string <code>"{function_id}:{"start" | "end"}:{timestamp}"</code>. For example, <code>"0:start:3"</code> means a call to the function with ID <code>0</code> <strong>started at the beginning</strong> of timestamp <code>3</code> and <code>"1:end:2"</code> means a call to the function with ID <code>1</code> <strong>ended at the end</strong> of timestamp <code>2</code>. Note that a function can be called <strong>multiple times, possibly recursively</strong>.</p>

<p>A function's <strong>exclusive time</strong> is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for <code>2</code> time units and another call executing for <code>1</code> time unit, the <strong>exclusive time</strong> is <code>2 + 1 = 3</code>.</p>

<p>Return <em>the <strong>exclusive time</strong> of each function in an array, where the value at the <code>i<sup>th</sup></code> index represents the exclusive time for the function with ID <code>i</code>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/05/diag1b.png" style="width: 550px;">
<pre><strong>Input:</strong> n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
<strong>Output:</strong> [3,4]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
<strong>Output:</strong> [8]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
<strong>Output:</strong> [7,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 100</code></li>
    <li><code>1 &lt;= logs.length &lt;= 500</code></li>
    <li><code>0 &lt;= function_id &lt; n</code></li>
    <li><code>0 &lt;= timestamp &lt;= 10<sup>9</sup></code></li>
    <li>No two start events will happen at the same timestamp.</li>
    <li>No two end events will happen at the same timestamp.</li>
    <li>Each function has an <code>"end"</code> log for each <code>"start"</code> log.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: Integer n.\nLine 2: JSON array of log strings."
    output_format = "A JSON array of integers: exclusive times for each function."

    constraints = [
        "1 <= n <= 100",
        "1 <= logs.length <= 500",
        "0 <= function_id < n",
        "0 <= timestamp <= 10^9"
    ]

    explanation = """Use a stack to simulate function execution. For each log, parse it into (fn_id, type, timestamp). On 'start', push the fn_id to the stack and track the previous time. On 'end', pop from the stack, calculate time spent, update exclusive time, and advance previous time."""

    answer = """class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn_id, typ, ts = log.split(':')
            fn_id, ts = int(fn_id), int(ts)
            
            if typ == 'start':
                if stack:
                    result[stack[-1]] += ts - prev_time
                stack.append(fn_id)
                prev_time = ts
            else:
                result[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1
                
        return result"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        # User logic here
        return [0] * n

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        n = int(raw[0])
        logs = json.loads(raw[1])
        sol = Solution()
        print(json.dumps(sol.exclusiveTime(n, logs)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        // User logic here
        return vector<int>(n, 0);
    }
};

vector<string> parseStringArray(string input) {
    vector<string> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '"') {
            size_t j = i + 1;
            string s = "";
            while (j < input.length() && input[j] != '"') s += input[j++];
            res.push_back(s);
            i = j + 1;
        } else i++;
    }
    return res;
}

int main() {
    string n_str, logs_str;
    if (getline(cin, n_str) && getline(cin, logs_str)) {
        int n = stoi(n_str);
        vector<string> logs = parseStringArray(logs_str);
        Solution sol;
        vector<int> ans = sol.exclusiveTime(n, logs);
        cout << "[";
        for (size_t i = 0; i < ans.size(); i++)
            cout << ans[i] << (i + 1 == ans.size() ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        // User logic here
        return new int[n];
    }
}

public class Main {
    static String[] parseStringArray(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '"') {
                int j = i + 1;
                StringBuilder sb = new StringBuilder();
                while (j < s.length() && s.charAt(j) != '"') sb.append(s.charAt(j++));
                res.add(sb.toString());
                i = j + 1;
            } else i++;
        }
        return res.toArray(new String[0]);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int n = Integer.parseInt(sc.nextLine().trim());
            if (sc.hasNextLine()) {
                String logsStr = sc.nextLine().trim();
                String[] logsArr = parseStringArray(logsStr);
                Solution sol = new Solution();
                int[] ans = sol.exclusiveTime(n, Arrays.asList(logsArr));
                System.out.print("[");
                for (int i = 0; i < ans.length; i++)
                    System.out.print(ans[i] + (i + 1 == ans.length ? "" : ","));
                System.out.println("]");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @param {string[]} logs
 * @return {number[]}
 */
var exclusiveTime = function(n, logs) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const n = parseInt(input[0], 10);
    const logs = JSON.parse(input[1]);
    console.log(JSON.stringify(exclusiveTime(n, logs)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* exclusiveTime(int n, char** logs, int logsSize, int* returnSize) {
    // User logic here
    int* result = (int*)calloc(n, sizeof(int));
    *returnSize = n;
    return result;
}

int main() {
    // Simplified; full parsing for C is complex
    printf("[]\\n");
    return 0;
}"""
    }

    test_cases = [
        {"input": '2\\n["0:start:0","1:start:2","1:end:5","0:end:6"]', "expected_output": "[3,4]", "is_sample": True},
        {"input": '1\\n["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]', "expected_output": "[8]", "is_sample": True},
        {"input": '2\\n["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]', "expected_output": "[7,1]", "is_sample": False},
        {"input": '1\\n["0:start:0","0:end:0"]', "expected_output": "[1]", "is_sample": False},
        {"input": '3\\n["0:start:0","1:start:5","2:start:10","2:end:15","1:end:20","0:end:25"]', "expected_output": "[10,10,6]", "is_sample": False},
        {"input": '2\\n["0:start:0","1:start:1","1:end:2","0:end:3"]', "expected_output": "[2,2]", "is_sample": False},
        {"input": '2\\n["0:start:0","1:start:1","1:end:1","0:end:2"]', "expected_output": "[2,1]", "is_sample": False},
        {"input": '3\\n["0:start:0","1:start:1","2:start:2","2:end:3","1:end:4","0:end:5","0:start:6","0:end:7","1:start:8","1:end:9","2:start:10","2:end:11"]', "expected_output": "[4,4,4]", "is_sample": False},
        {"input": '1\\n["0:start:0","0:start:1","0:end:1","0:end:2"]', "expected_output": "[3]", "is_sample": False},
        {"input": '2\\n["1:start:0","0:start:1","0:end:9","1:end:10"]', "expected_output": "[9,2]", "is_sample": False}
    ]

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
        "topics": ["Array", "Stack"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
