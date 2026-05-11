import json
import os

def generate_json():
    problem_id = 1229
    title = "Meeting Scheduler"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1229. Meeting Scheduler</h3>
<p>Given the availability time slots arrays <code>slots1</code> and <code>slots2</code> of two people and a meeting duration <code>duration</code>, return the <strong>earliest</strong> time slot that works for both of them and is of duration <code>duration</code>.</p>

<p>If there is no common time slot that satisfies the requirements, return an <strong>empty array</strong>.</p>

<p>The format of a time slot is an array of two elements <code>[start, end]</code> representing an inclusive time range from <code>start</code> to <code>end</code>. </p>

<p>It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots <code>[start1, end1]</code> and <code>[start2, end2]</code> of the same person, either <code>start1 > end2</code> or <code>start2 > end1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
<strong>Output:</strong> [60,68]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= slots1.length, slots2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>slots1[i].length, slots2[i].length == 2</code></li>
	<li><code>slots1[i][0], slots1[i][1], slots2[i][0], slots2[i][1] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= duration &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "Two matrices `slots1` and `slots2`, and an integer `duration` provided as `[slots1, slots2, duration]` in JSON."
    output_format = "A JSON array `[start, end]` or empty array `[]`."

    constraints = [
        "1 <= slots1.length, slots2.length <= 10^4",
        "Slots are disjoint and sorted",
        "1 <= duration <= 10^6"
    ]

    explanation = """To find the earliest common slot:
1. Sort both `slots1` and `slots2` by start time (if not already sorted).
2. Use two pointers `i` and `j` to iterate through the slots of both people.
3. For each pair of slots `slots1[i]` and `slots2[j]`:
   - Calculate the common intersection: `start = max(slots1[i][0], slots2[j][0])` and `end = min(slots1[i][1], slots2[j][1])`.
   - If `end - start >= duration`, return `[start, start + duration]`.
   - If `slots1[i][1] < slots2[j][1]`, increment `i` (move to next slot for person 1).
   - Otherwise, increment `j` (move to next slot for person 2).
4. If no common slot is found, return `[]`."""

    answer = """class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        slots1, slots2, duration = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.minAvailableDuration(slots1, slots2, duration)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<vector<int>> s1 = j[0].get<vector<vector<int>>>();
        vector<vector<int>> s2 = j[1].get<vector<vector<int>>>();
        int d = j[2];
        Solution sol;
        vector<int> res = sol.minAvailableDuration(s1, s2, d);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int[][] s1 = mapper.convertValue(data[0], int[][].class);
            int[][] s2 = mapper.convertValue(data[1], int[][].class);
            int d = (Integer) data[2];
            List<Integer> res = new Solution().minAvailableDuration(s1, s2, d);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var minAvailableDuration = function(slots1, slots2, duration) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [s1, s2, d] = JSON.parse(input);
    const res = minAvailableDuration(s1, s2, d);
    console.log(JSON.stringify(res).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* minAvailableDuration(int** slots1, int slots1Size, int* slots1ColSize, int** slots2, int slots2Size, int* slots2ColSize, int duration, int* returnSize){
    // User logic here
    return NULL;
}

int main() {
    // Boilerplate for matrix parsing
    return 0;
}"""
    }

    def solve(slots1, slots2, duration):
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []

    test_cases_data = [
        [[[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8],  # Sample 1
        [[[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12], # Sample 2
        [[[10,60]], [[12,17],[20,50]], 8],                   # Overlap within
        [[[0,10]], [[10,20]], 1],                             # Edge touch
        [[[10,20]], [[10,20]], 10],                           # Exact match
        [[[10,20]], [[30,40]], 5],                             # Disjoint
        [[[0,1000000000]], [[0,1000000000]], 1000000],        # Large range
        # Stress tests
        [[[i*2, i*2+1] for i in range(1000)], [[i*2+0.5, i*2+1.5] for i in range(1000)], 0.5], # Lots of small overlaps
        [[[i*10, i*10+5] for i in range(100)], [[i*10+6, i*10+11] for i in range(100)], 1], # No overlaps
        [[[0, 1000000000]], [[0, 1000000000]], 1000000000]    # One max duration
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1], t[2])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Two Pointers", "Sorting"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
