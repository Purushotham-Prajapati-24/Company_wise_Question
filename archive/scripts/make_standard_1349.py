import json
import os

def generate_json():
    problem_id = 1349
    title = "Maximum Students Taking Exam"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1349. Maximum Students Taking Exam</h3>
<p>Given a <code>m * n</code> matrix <code>seats</code>&nbsp;that represent seats distributions&nbsp;in a classroom.&nbsp;If a seat&nbsp;is&nbsp;broken, it is denoted by <code>'#'</code> character otherwise it is denoted by a <code>'.'</code> character.</p>

<p>Students can see the screens of politics sitting&nbsp;in the <strong>front-left</strong>, <strong>front-right</strong> and <strong>directly left</strong> and <strong>directly right</strong> seat, relative to themselves. A student will only take a seat if they cannot see the screen of any other student.</p>

<p>Return the maximum number of students that can take the exam together&nbsp;under the given constraints.</p>

<p>Notice that students in the first row can only see the screens of students to their left and right.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/29/image.png" style="width: 339px; height: 252px;">
<pre><strong>Input:</strong> seats = [["#",".","#","#",".","#"],
&nbsp;               [".","#","#","#","#","."],
&nbsp;               ["#",".","#","#",".","#"]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Teacher can place 4 students in available seats so they don't cheat on the exam. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> seats = [[".","#"],
&nbsp;               ["#","#"],
&nbsp;               ["#","."],
&nbsp;               ["#","#"],
&nbsp;               [".","#"]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Place all students in available seats.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> seats = [["#",".",".",".","#"],
&nbsp;               [".","#",".","#","."],
&nbsp;               [".",".","#",".","."],
&nbsp;               [".","#",".","#","."],
&nbsp;               ["#",".",".",".","#"]]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Place students in [0,1], [0,3], [1,0], [1,2], [1,4], [3,0], [3,2], [3,4], [4,1], [4,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>seats.length == m</code></li>
	<li><code>seats[i].length == n</code></li>
	<li><code>1 &lt;= m &lt;= 8</code></li>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>"""

    input_format = "A 2D character array `seats` provided as a JSON array of arrays."
    output_format = "An integer representing the maximum students."

    constraints = [
        "1 <= m, n <= 8",
        "'.' for good seat, '#' for broken"
    ]

    explanation = """To find the maximum students:
1. Since the dimensions are small (at most 8x8), we can use Dynamic Programming with Bitmask.
2. Let `dp[row][mask]` be the maximum students that can be seated in the first `row` rows such that the `row`-th row has the seating configuration `mask`.
3. The configuration `mask` is a bitmask of length `n`, where the `i`-th bit is 1 if there's a student in the `i`-th seat of that row.
4. For each row `i`:
   - A mask is valid for row `i` if:
     - No two adjacent bits are set (students can see screens to their left and right).
     - No bit is set if the corresponding seat in `seats[i]` is broken.
   - For a valid mask `curr_mask` in row `i`:
     - It can be used with `prev_mask` in row `i-1` if:
       - No student in `curr_mask` is at `front-left` or `front-right` of a student in `prev_mask`.
       - This means `(curr_mask << 1) & prev_mask == 0` and `(curr_mask >> 1) & prev_mask == 0`.
5. Iterate through all rows and calculate the DP states.
6. The answer is the maximum value in the last row's DP table."""

    answer = """class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])
        # dp[row][mask] = max students for first 'row' rows with current row configuration 'mask'
        dp = [[-1] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0
        
        row_masks = []
        for i in range(m):
            mask = 0
            for j in range(n):
                if seats[i][j] == '.':
                    mask |= (1 << j)
            row_masks.append(mask)
            
        def is_valid_mask(mask, row_mask):
            if (mask & row_mask) != mask: return False
            if (mask & (mask << 1)) or (mask & (mask >> 1)): return False
            return True
            
        for i in range(1, m + 1):
            curr_row_mask = row_masks[i-1]
            for curr_mask in range(1 << n):
                if not is_valid_mask(curr_mask, curr_row_mask):
                    continue
                    
                bits_count = bin(curr_mask).count('1')
                for prev_mask in range(1 << n):
                    if dp[i-1][prev_mask] == -1:
                        continue
                        
                    if not ((curr_mask << 1) & prev_mask) and not ((curr_mask >> 1) & prev_mask):
                        dp[i][curr_mask] = max(dp[i][curr_mask], dp[i-1][prev_mask] + bits_count)
                        
        return max(dp[m])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        seats = json.loads(raw)
        sol = Solution()
        print(sol.maxStudents(seats))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxStudents(vector<vector<char>>& seats) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<char>> seats = json::parse(line);
        Solution sol;
        cout << sol.maxStudents(seats) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maxStudents(char[][] seats) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            char[][] seats = mapper.readValue(sc.nextLine(), char[][].class);
            System.out.println(new Solution().maxStudents(seats));
        }
    }
}""",
        "javascript": """var maxStudents = function(seats) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(maxStudents(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int maxStudents(char** seats, int seatsSize, int* seatsColSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    import collections
    def solve(seats):
        m, n = len(seats), len(seats[0])
        dp = [[-1] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0
        row_masks = []
        for i in range(m):
            mask = 0
            for j in range(n):
                if seats[i][j] == '.': mask |= (1 << j)
            row_masks.append(mask)
        def is_valid(mask, row_mask):
            return (mask & row_mask) == mask and not (mask & (mask << 1))
        for i in range(1, m + 1):
            for curr in range(1 << n):
                if not is_valid(curr, row_masks[i-1]): continue
                bits = bin(curr).count('1')
                for prev in range(1 << n):
                    if dp[i-1][prev] == -1: continue
                    if not ((curr << 1) & prev) and not ((curr >> 1) & prev):
                        dp[i][curr] = max(dp[i][curr], dp[i-1][prev] + bits)
        return max(dp[m])

    test_cases_data = [
        [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]], # Sample 1
        [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]], # Sample 2
        [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]], # Sample 3
        [[".",".",".",".",".",".",".","."]], # All good, 1 row
        [["#","#","#","#","#","#","#","#"]], # All broken
        [[".",".",".",".",".",".",".","."]] * 8, # All good, 8x8
        [[".","#",".","#",".","#",".","#"]] * 8, # Checkerboard
        # Stress tests
        [["."] * 8] * 8,
        [["#"] * 8] * 8,
        [[".", "#", ".", "#", ".", "#", ".", "#"], ["#", ".", "#", ".", "#", ".", "#", "."]] * 4
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Bit Manipulation", "Matrix"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
