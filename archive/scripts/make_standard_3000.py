import json
import os

def generate_json():
    problem_id = 3000
    title = "Maximum Area of Longest Diagonal Rectangle"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>3000. Maximum Area of Longest Diagonal Rectangle</h3>
<p>You are given a 2D integer array <code>dimensions</code> where <code>dimensions[i] = [length<sub>i</sub>, width<sub>i</sub>]</code>.</p>

<p>Return <em>the <strong>area</strong> of the rectangle having the <strong>longest</strong> diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the <strong>maximum</strong> area.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dimensions = [[9,3],[8,6]]
<strong>Output:</strong> 48
<strong>Explanation:</strong> 
For index 0, length = 9, width = 3. Diagonal length = sqrt(9<sup>2</sup> + 3<sup>2</sup>) = sqrt(81 + 9) = sqrt(90).
For index 1, length = 8, width = 6. Diagonal length = sqrt(8<sup>2</sup> + 6<sup>2</sup>) = sqrt(64 + 36) = sqrt(100).
The longest diagonal is at index 1, and its area is 8 * 6 = 48.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dimensions = [[3,4],[4,3]]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Length of diagonal is the same for both which is sqrt(3<sup>2</sup> + 4<sup>2</sup>) = 5. Area of both rectangles are 3 * 4 = 12. So output is 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= dimensions.length &lt;= 100</code></li>
	<li><code>dimensions[i].length == 2</code></li>
	<li><code>1 &lt;= length<sub>i</sub>, width<sub>i</sub> &lt;= 100</code></li>
</ul>
"""

    input_format = "A 2D array of integers `dimensions` provided as `[dimensions]` in JSON."
    output_format = "An integer representing the maximum area of rectangles with the longest diagonal."

    constraints = [
        "1 <= dimensions.length <= 100",
        "1 <= length, width <= 100"
    ]

    explanation = """To find the area:
1. For each rectangle `[l, w]`, calculating the squared diagonal length `d^2 = l^2 + w^2` is sufficient (to avoid floating point issues).
2. Keep track of the maximum `d^2` found so far and the corresponding maximum area.
3. If current `l^2 + w^2` is greater than `max_d2`, update both `max_d2` and `max_area`.
4. If current `l^2 + w^2` is equal to `max_d2`, update `max_area = max(max_area, l * w)`.
5. Return `max_area`."""

    answer = """class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_d2 = 0
        max_area = 0
        for l, w in dimensions:
            d2 = l*l + w*w
            if d2 > max_d2:
                max_d2 = d2
                max_area = l * w
            elif d2 == max_d2:
                max_area = max(max_area, l * w)
        return max_area"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        dimensions = json.loads(raw)
        if isinstance(dimensions[0][0], list): dimensions = dimensions[0]
        sol = Solution()
        print(sol.areaOfMaxDiagonal(dimensions))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<vector<int>> dimensions;
        if (j.is_array() && j.size() > 0 && j[0].is_array() && j[0][0].is_array()) dimensions = j[0].get<vector<vector<int>>>();
        else dimensions = j.get<vector<vector<int>>>();
        Solution sol;
        cout << sol.areaOfMaxDiagonal(dimensions) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
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
            int[][] dimensions;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List && ((List)((List)raw).get(0)).get(0) instanceof List) {
                dimensions = mapper.convertValue(((List)raw).get(0), int[][].class);
            } else {
                dimensions = mapper.convertValue(raw, int[][].class);
            }
            System.out.println(new Solution().areaOfMaxDiagonal(dimensions));
        }
    }
}""",
        "javascript": """var areaOfMaxDiagonal = function(dimensions) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let dimensions = JSON.parse(input);
    if (Array.isArray(dimensions[0]) && Array.isArray(dimensions[0][0])) dimensions = dimensions[0];
    console.log(areaOfMaxDiagonal(dimensions));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int f_cap = 128, f_size = 0;
    int** dimensions = malloc(f_cap * sizeof(int*));
    int* colSizes = malloc(f_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && c != '[' && c != ']');
        if (c == EOF || c == ']') break;
        int row_cap = 2, row_size = 0;
        int* row = malloc(row_cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (row_size >= row_cap) { row_cap *= 2; row = realloc(row, row_cap * sizeof(int)); }
            scanf("%d", &row[row_size++]);
        }
        if (f_size >= f_cap) { f_cap *= 2; dimensions = realloc(dimensions, f_cap * sizeof(int*)); colSizes = realloc(colSizes, f_cap * sizeof(int)); }
        dimensions[f_size] = row;
        colSizes[f_size++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    printf("%d\\n", areaOfMaxDiagonal(dimensions, f_size, colSizes));
    return 0;
}"""
    }

    def solve(dimensions):
        max_d2 = 0
        max_area = 0
        for l, w in dimensions:
            d2 = l*l + w*w
            if d2 > max_d2:
                max_d2 = d2
                max_area = l * w
            elif d2 == max_d2:
                max_area = max(max_area, l * w)
        return max_area

    test_cases_data = [
        [[9,3],[8,6]],     # Sample 1
        [[3,4],[4,3]],     # Sample 2
        [[1,1],[1,1]],
        [[10,1],[1,10]],
        [[2,2],[1,3]],     # 4+4=8 vs 1+9=10
        [[100,100]],
        [[1,1],[2,2],[3,3]],
        # Stress tests
        [[i, 101-i] for i in range(1, 101)],
        [[100, i] for i in range(1, 101)],
        [[i, i] for i in range(1, 101)]
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
        "topics": ["Array", "Math"], "companyIndex": 0
    }

    output_path = f"2801-3000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
