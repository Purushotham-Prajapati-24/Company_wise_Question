import json
import os

def generate_json():
    problem_id = 853
    title = "Car Fleet"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>853. Car Fleet</h3>
<p>There are <code>n</code> cars at given miles away from the destination <code>target</code>, traveling at different constant speeds.</p>

<p>You are given two arrays: <code>position</code> and <code>speed</code>, both of integers and length <code>n</code>. <code>position[i]</code> is the position of the <code>i</code>-th car in miles and <code>speed[i]</code> is its speed in miles per hour. The destination is at <code>target</code> miles.</p>

<p>A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored - they are assumed to have the same position.</p>

<p>A <strong>car fleet</strong> is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.</p>

<p>If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.</p>

<p>Return <em>the <strong>number of car fleets</strong> that will arrive at the destination</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> target = 10, position = [3], speed = [3]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> target = 100, position = [0,2,4], speed = [4,2,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == position.length == speed.length</code></li>
    <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt; target &lt;= 10<sup>6</sup></code></li>
    <li><code>0 &lt;= position[i] &lt; target</code></li>
    <li>All the values in <code>position</code> are <strong>unique</strong>.</li>
    <li><code>0 &lt; speed[i] &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "Three lines:\nLine 1: integer `target`\nLine 2: JSON array `position`\nLine 3: JSON array `speed`"
    output_format = "An integer representing the number of car fleets."

    constraints = [
        "1 <= n <= 10^5",
        "0 < target <= 10^6"
    ]

    explanation = """First, sort the cars by their starting positions in descending order (from closest to the target to farthest). For each car, calculate the time it would take to reach the target at its current speed: `(target - position) / speed`. Iterate through the sorted cars and maintain a stack or simply keep track of the arrival time of the fleet currently ahead. If a car arrives at or earlier than the arrival time of the fleet ahead, it joins that fleet. Otherwise, it starts a new fleet."""

    answer = """class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        ans = 0
        curr_max_time = 0
        for t in times:
            if t > curr_max_time:
                ans += 1
                curr_max_time = t
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 3:
        target = int(raw[0].strip())
        position = json.loads(raw[1].strip())
        speed = json.loads(raw[2].strip())
        sol = Solution()
        print(sol.carFleet(target, position, speed))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < input.length() - 1) {
        if (isdigit(input[i]) || input[i] == '-') {
            int val = 0; int off=0;
            auto sub = input.substr(i);
            sscanf(sub.c_str(), "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    int target;
    string posStr, speedStr;
    if (cin >> target >> posStr >> speedStr) {
        auto pos = parseArray(posStr);
        auto speed = parseArray(speedStr);
        Solution sol;
        cout << sol.carFleet(target, pos, speed) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[] parseArray(String s) {
        s = s.substring(1, s.length()-1);
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i=0; i<parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int target = sc.nextInt();
            String posStr = sc.next();
            String speedStr = sc.next();
            int[] pos = parseArray(posStr);
            int[] speed = parseArray(speedStr);
            Solution sol = new Solution();
            System.out.println(sol.carFleet(target, pos, speed));
        }
    }
}""",
        "javascript": """/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 3) {
    let target = parseInt(input[0]);
    let position = JSON.parse(input[1]);
    let speed = JSON.parse(input[2]);
    console.log(carFleet(target, position, speed));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    // User logic here
    return 0;
}

int main() {
    int target;
    char posStr[100000], speedStr[100000];
    if (scanf("%d %99999s %99999s", &target, posStr, speedStr) == 3) {
        int sz = 0, cap = 100;
        int* posArray = malloc(cap * sizeof(int));
        char* token = strtok(posStr + 1, ",]");
        while (token != NULL) {
            if (sz == cap) posArray = realloc(posArray, (cap *= 2) * sizeof(int));
            posArray[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        int sz2 = 0, cap2 = sz;
        int* speedArray = malloc(cap2 * sizeof(int));
        char* token2 = strtok(speedStr + 1, ",]");
        while (token2 != NULL) {
            speedArray[sz2++] = atoi(token2);
            token2 = strtok(NULL, ",]");
        }
        printf("%d\\n", carFleet(target, posArray, sz, speedArray, sz2));
        free(posArray); free(speedArray);
    }
    return 0;
}"""
    }

    def solve(target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        ans = 0
        curr_max_time = 0
        for t in times:
            if t > curr_max_time:
                ans += 1
                curr_max_time = t
        return ans

    test_cases_data = [
        (12, [10,8,0,5,3], [2,4,1,1,3]),
        (10, [3], [3]),
        (100, [0,2,4], [4,2,1]),
        (10, [0,4,2], [2,1,3]),
        (10, [6,8], [3,2]),
        (10, [2,4], [3,2]),
        (31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,1,7,5,5,10]),
        (13, [10,2,5,7,4,6,11], [7,5,10,5,9,4,1]),
        (10, [3,5,7], [3,2,1]),
        (10, [0,1,2,3,4,5,6,7,8,9], [1,1,1,1,1,1,1,1,1,1])
    ]

    test_cases = []
    for i, (target, pos, speed) in enumerate(test_cases_data):
        inp = f"{target}\n{json.dumps(pos).replace(' ', '')}\n{json.dumps(speed).replace(' ', '')}"
        out = str(solve(target, pos, speed))
        is_sample = i < 3
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
        "topics": ["Array", "Stack", "Sorting", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
