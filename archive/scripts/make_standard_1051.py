import json
import os

def generate_json():
    problem_id = 1051
    title = "Height Checker"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1051. Height Checker</h3>
<p>A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in <strong>non-decreasing order</strong> by height. Let this ordering be represented by the integer array <code>expected</code> where <code>expected[i]</code> is the expected height of the <code>i<sup>th</sup></code> student in line.</p>

<p>You are given an integer array <code>heights</code> representing the <strong>current order</strong> that the students are standing in. Each <code>heights[i]</code> is the height of the <code>i<sup>th</sup></code> student in line (<strong>0-indexed</strong>).</p>

<p>Return <em>the <strong>number of indices</strong> where </em><code>heights[i] != expected[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> heights = [1,1,4,2,1,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> heights = [5,1,2,3,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> heights = [1,2,3,4,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 100</code></li>
	<li><code>1 &lt;= heights[i] &lt;= 100</code></li>
</ul>
"""

    input_format = "An array of integers `heights` provided as `[heights]` or a single array in JSON."
    output_format = "An integer representing the number of mismatched indices."

    constraints = [
        "1 <= heights.length <= 100",
        "1 <= heights[i] <= 100"
    ]

    explanation = """To count mismatched indices:
1. Create a sorted copy of the `heights` array and call it `expected`.
2. Compare each element of `heights` with `expected` at the same index.
3. If they are different, increment the count.
4. Return the total count."""

    answer = """class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        heights = json.loads(raw)
        if isinstance(heights[0], list): heights = heights[0]
        sol = Solution()
        print(sol.heightChecker(heights))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> heights;
        if (j.is_array() && j.size() > 0 && j[0].is_array()) heights = j[0].get<vector<int>>();
        else heights = j.get<vector<int>>();
        Solution sol;
        cout << sol.heightChecker(heights) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int heightChecker(int[] heights) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            int[] heights;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                heights = mapper.convertValue(((List)raw).get(0), int[].class);
            } else {
                heights = mapper.convertValue(raw, int[].class);
            }
            System.out.println(new Solution().heightChecker(heights));
        }
    }
}""",
        "javascript": """var heightChecker = function(heights) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let heights = JSON.parse(input);
    if (Array.isArray(heights[0])) heights = heights[0];
    console.log(heightChecker(heights));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int heightChecker(int* heights, int heightsSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* heights = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; heights = realloc(heights, cap * sizeof(int)); }
        scanf("%d", &heights[s++]);
    }
    printf("%d\\n", heightChecker(heights, s));
    free(heights);
    return 0;
}"""
    }

    def solve(heights):
        expected = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != expected[i])

    test_cases_data = [
        [[1,1,4,2,1,3]],   # Sample 1
        [[5,1,2,3,4]],     # Sample 2
        [[1,2,3,4,5]],     # Sample 3
        [[1,1,1]],
        [[3,3,3,1,1]],
        [[100, 1, 100, 1]],
        [[50]],
        # Stress tests
        [[1]*100],
        [list(range(100, 0, -1))],
        [list(range(1, 101))]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Sorting", "Counting Sort"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
