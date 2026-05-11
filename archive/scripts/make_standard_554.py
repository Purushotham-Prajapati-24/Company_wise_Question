import json
import os

def generate_json():
    problem_id = 554
    title = "Brick Wall"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>554. Brick Wall</h3>
<p>There is a rectangular brick wall in front of you with <code>n</code> rows of bricks. The <code>i<sup>th</sup></code> row has some number of bricks each of the same height but they can be of different widths. The total width of each row is the same.</p>

<p>Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.</p>

<p>Given the 2D array <code>wall</code> that contains the width of each brick in each row from left to right, return <em>the minimum number of crossed bricks</em> after drawing such a vertical line.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> wall = [[1],[1],[1]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == wall.length</code></li>
    <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
    <li><code>1 &lt;= wall[i].length &lt;= 10<sup>4</sup></code></li>
    <li><code>1 &lt;= sum(wall[i].length) &lt;= 2 * 10<sup>4</sup></code></li>
    <li>The sum of the widths in each row is the same.</li>
    <li><code>1 &lt;= wall[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single line: a JSON 2D array of integers `wall`."
    output_format = "An integer: the minimum number of crossed bricks."

    constraints = [
        "n == wall.length",
        "1 <= n <= 10^4",
        "1 <= wall[i].length <= 10^4",
        "The sum of widths in each row is the same"
    ]

    explanation = """For each row, track the prefix sums of brick widths (up to but not including the last brick, to avoid counting the edge). Use a hash map to count how many rows share the same prefix sum position. The best cut line passes through the maximum such count, and the answer is n minus this count."""

    answer = """from collections import Counter
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edge_count = Counter()
        for row in wall:
            prefix = 0
            for brick in row[:-1]:
                prefix += brick
                edge_count[prefix] += 1
        if not edge_count:
            return len(wall)
        return len(wall) - max(edge_count.values())"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        wall = json.loads(raw)
        sol = Solution()
        print(sol.leastBricks(wall))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        // User logic here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<vector<int>> wall;
        vector<int> row;
        int depth = 0;
        size_t p = 0;
        while (p < input.length()) {
            if (input[p] == '[') { depth++; p++; }
            else if (input[p] == ']') {
                depth--;
                if (depth == 1) { wall.push_back(row); row.clear(); }
                p++;
            } else if (isdigit(input[p])) {
                size_t next;
                row.push_back(stoi(input.substr(p), &next));
                p += next;
            } else p++;
        }
        Solution sol;
        cout << sol.leastBricks(wall) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            List<List<Integer>> wall = new ArrayList<>();
            List<Integer> row = new ArrayList<>();
            int depth = 0;
            int i = 0;
            while (i < raw.length()) {
                char c = raw.charAt(i);
                if (c == '[') { depth++; i++; }
                else if (c == ']') {
                    depth--;
                    if (depth == 1) { wall.add(new ArrayList<>(row)); row.clear(); }
                    i++;
                } else if (Character.isDigit(c)) {
                    int end = i;
                    while (end < raw.length() && Character.isDigit(raw.charAt(end))) end++;
                    row.add(Integer.parseInt(raw.substring(i, end)));
                    i = end;
                } else i++;
            }
            Solution sol = new Solution();
            System.out.println(sol.leastBricks(wall));
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function(wall) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const wall = JSON.parse(input);
    console.log(leastBricks(wall));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int leastBricks(int** wall, int wallSize, int* wallColSize) {
    // User logic here
    return 0;
}

int main() {
    char input[1000000];
    if (fgets(input, sizeof(input), stdin)) {
        int nums[200000], ncount = 0;
        int rowSizes[10000], nrows = 0;
        int rowCount = 0;
        int depth = 0, i = 0;
        while (input[i]) {
            if (input[i] == '[') { depth++; if (depth == 2) rowCount = 0; i++; }
            else if (input[i] == ']') {
                depth--;
                if (depth == 1) rowSizes[nrows++] = rowCount;
                i++;
            } else if (isdigit(input[i])) {
                int val, off = 0;
                sscanf(input + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                nums[ncount++] = val;
                rowCount++;
                i += off;
            } else i++;
        }
        int** wall = (int**)malloc(nrows * sizeof(int*));
        int idx = 0;
        for (int r = 0; r < nrows; r++) {
            wall[r] = (int*)malloc(rowSizes[r] * sizeof(int));
            for (int c = 0; c < rowSizes[r]; c++) wall[r][c] = nums[idx++];
        }
        printf("%d\\n", leastBricks(wall, nrows, rowSizes));
        for (int r = 0; r < nrows; r++) free(wall[r]);
        free(wall);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1],[1],[1]]", "expected_output": "3", "is_sample": True},

        # Five Diverse Cases
        {"input": "[[1,1],[1,1]]", "expected_output": "0", "is_sample": False},
        {"input": "[[2,2],[1,1,2]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,2,3],[2,1,3],[3,3]]", "expected_output": "1", "is_sample": False},
        {"input": "[[4],[4],[4],[4]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1,3,2],[2,2,2],[1,1,4]]", "expected_output": "1", "is_sample": False},

        # Three Stress Test Cases
        {"input": "[[" + ",".join(["1"] * 1000) + "]] " * 9999, "expected_output": "0", "is_sample": False},
        {"input": "[[2,2],[1,1,2],[4]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,1,1,1],[2,2],[1,1,2],[4]]", "expected_output": "0", "is_sample": False}
    ]

    # Fix test case 7 (stress)
    test_cases[7] = {"input": "[[2,2],[1,1,2],[4]]", "expected_output": "1", "is_sample": False}
    test_cases[8] = {"input": "[[1,1,1,1],[2,1,1],[1,3],[4]]", "expected_output": "1", "is_sample": False}
    test_cases[9] = {"input": "[[1,2,1],[1,1,1,1],[3,1]]", "expected_output": "0", "is_sample": False}

    # rebuild clean
    test_cases = [
        {"input": "[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1],[1],[1]]", "expected_output": "3", "is_sample": True},
        {"input": "[[1,1],[1,1]]", "expected_output": "0", "is_sample": False},
        {"input": "[[2,2],[1,1,2]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,2,3],[2,1,3],[3,3]]", "expected_output": "1", "is_sample": False},
        {"input": "[[4],[4],[4],[4]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1,3,2],[2,2,2],[1,1,4]]", "expected_output": "1", "is_sample": False},
        {"input": "[[2,2],[1,1,2],[4]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,2,1],[1,1,1,1],[3,1],[2,2]]", "expected_output": "0", "is_sample": False},
        {"input": "[[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5]]", "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
