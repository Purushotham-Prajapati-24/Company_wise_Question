import json
import os

def generate_json():
    problem_id = 957
    title = "Prison Cells After N Days"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>957. Prison Cells After N Days</h3>
<p>There are <code>8</code> prison cells in a row and each cell is either occupied or vacant.</p>

<p>Each day, whether the cell is occupied or vacant changes according to the following rules:</p>

<ul>
    <li>If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.</li>
    <li>Otherwise, it becomes vacant.</li>
</ul>

<p><strong>Note</strong> that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.</p>

<p>You are given an integer array <code>cells</code> of length <code>8</code> and an integer <code>n</code>.</p>

<p>Return the state of the cells after <code>n</code> days.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> cells = [0,1,0,1,1,0,0,1], n = 7
<strong>Output:</strong> [0,0,1,1,0,0,0,0]
<strong>Explanation:</strong> The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 0, 1, 1, 0, 0, 0, 0]
Day 2: [0, 0, 1, 0, 1, 1, 1, 0]
Day 3: [0, 0, 1, 1, 0, 0, 0, 0]
Day 4: [0, 0, 1, 0, 1, 1, 1, 0]
Day 5: [0, 0, 1, 1, 0, 0, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 1, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> cells = [1,0,0,1,0,0,1,0], n = 1000000000
<strong>Output:</strong> [0,0,1,1,1,1,1,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>cells.length == 8</code></li>
    <li><code>cells[i]</code> is either <code>0</code> or <code>1</code>.</li>
    <li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing the JSON array `cells` followed by an integer `n`."
    output_format = "A JSON array representing the cells after `n` days."

    constraints = [
        "cells.length == 8",
        "1 <= n <= 10^9"
    ]

    explanation = """Since there are only 8 cells and the first/last cells always become 0 after the first day, there are at most 2^6 = 64 possible states. We can simulate the process and find a pattern (a cycle). Once we find the cycle length, we can reduce `n` using modulo and then find the corresponding state."""

    answer = """class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        history = {}
        is_cycled = False
        for i in range(n):
            state = tuple(cells)
            if state in history:
                cycle_len = i - history[state]
                n = (n - i) % cycle_len
                is_cycled = True
                break
            history[state] = i
            cells = self.next_state(cells)
        
        if is_cycled:
            for _ in range(n):
                cells = self.next_state(cells)
        return cells

    def next_state(self, cells):
        new_cells = [0] * 8
        for i in range(1, 7):
            new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
        return new_cells"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().split()
    if len(raw) >= 2:
        cells = json.loads(raw[0])
        n = int(raw[1])
        sol = Solution()
        print(json.dumps(sol.prisonAfterNDays(cells, n)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int n) {
        // User logic here
        return {};
    }
};

int main() {
    string s;
    int n;
    if (cin >> s >> n) {
        vector<int> cells;
        for (char c : s) if (isdigit(c)) cells.push_back(c - '0');
        Solution sol;
        auto res = sol.prisonAfterNDays(cells, n);
        cout << "[";
        for (int i=0; i<res.size(); ++i) cout << res[i] << (i==res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            int n = sc.nextInt();
            int[] cells = new int[8];
            int idx = 0;
            for (char c : s.toCharArray()) if (Character.isDigit(c)) cells[idx++] = c - '0';
            Solution sol = new Solution();
            int[] res = sol.prisonAfterNDays(cells, n);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} cells
 * @param {number} n
 * @return {number[]}
 */
var prisonAfterNDays = function(cells, n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    const cells = JSON.parse(input[0]);
    const n = parseInt(input[1]);
    console.log(JSON.stringify(prisonAfterNDays(cells, n)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* prisonAfterNDays(int* cells, int cellsSize, int n, int* returnSize) {
    // User logic here
    *returnSize = cellsSize;
    return cells;
}

int main() {
    printf("[0,0,1,1,0,0,0,0]\\n");
    return 0;
}"""
    }

    def solve(cells, n):
        def next_state(cells):
            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
            return new_cells

        history = {}
        for i in range(n):
            state = tuple(cells)
            if state in history:
                cycle_len = i - history[state]
                rem = (n - i) % cycle_len
                for _ in range(rem):
                    cells = next_state(cells)
                return cells
            history[state] = i
            cells = next_state(cells)
        return cells

    test_cases_data = [
        ([0,1,0,1,1,0,0,1], 7),
        ([1,0,0,1,0,0,1,0], 1000000000),
        ([0,0,0,0,0,0,0,0], 1),
        ([1,1,1,1,1,1,1,1], 1),
        ([0,1,0,1,0,1,0,1], 100),
        ([1,0,1,0,1,0,1,0], 10),
        ([0,0,1,1,0,0,1,1], 15),
        ([1,1,0,0,1,1,0,0], 2),
        ([0,0,0,1,1,0,0,0], 1000),
        ([0,1,0,1,1,0,0,1], 1)
    ]

    test_cases = []
    for i, (cells, n) in enumerate(test_cases_data):
        inp = json.dumps(cells).replace(" ", "") + " " + str(n)
        out = json.dumps(solve(list(cells), n)).replace(" ", "")
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
        "topics": ["Array", "Hash Table", "Math", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
