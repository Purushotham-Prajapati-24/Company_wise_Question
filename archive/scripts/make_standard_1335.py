import json
import os

def generate_json():
    problem_id = 1335
    title = "Minimum Difficulty of a Job Schedule"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1335. Minimum Difficulty of a Job Schedule</h3>
<p>You want to schedule a list of jobs in <code>d</code> days. Jobs are dependent (i.e To work on the <code>i-th</code> job, you have to finish all the jobs <code>j</code> where <code>j &lt; i</code>).</p>

<p>You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the <code>d</code> days. The difficulty of a day is the maximum difficulty of a job done in that day.</p>

<p>Given an array of integers <code>jobDifficulty</code> and an integer <code>d</code>. Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return <strong>-1</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/untitled.png" style="width: 365px; height: 370px;">
<pre><strong>Input:</strong> jobDifficulty = [6,5,4,3,2,1], d = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> jobDifficulty = [9,9,9], d = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> If you finish a job per day you will still have 3 days but you have 4 jobs to do. You cannot find a schedule for the given jobs.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> jobDifficulty = [1,1,1], d = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The schedule is one job per day. total difficulty will be 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= jobDifficulty.length &lt;= 300</code></li>
	<li><code>0 &lt;= jobDifficulty[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= d &lt;= 10</code></li>
</ul>"""

    input_format = "A list of integers `jobDifficulty` and an integer `d` provided as `[jobDifficulty, d]` in JSON."
    output_format = "An integer representing the minimum difficulty."

    constraints = [
        "1 <= jobDifficulty.length <= 300",
        "1 <= d <= 10",
        "0 <= jobDifficulty[i] <= 1000"
    ]

    explanation = """To find the minimum difficulty of a job schedule:
1. This is a classic dynamic programming problem. Let `dp[i][j]` be the minimum difficulty to finish the first `j` jobs in `i` days.
2. Initialize `dp` with infinity, except `dp[0][0] = 0`.
3. For each day `day` from 1 to `d`:
   - For each end job `j` from `day` up to `n`:
     - Maintain a running maximum `max_diff` for the current day's jobs.
     - For each start job `k` from `j` down to `day`:
       - `max_diff = max(max_diff, jobDifficulty[k-1])`
       - `dp[day][j] = min(dp[day][j], dp[day-1][k-1] + max_diff)`
4. If `n < d`, return -1.
5. The result is `dp[d][n]`."""

    answer = """class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        # dp[i][j] = min diff for first j jobs in i days
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        
        for k in range(1, d + 1):
            for i in range(k, n + 1):
                max_d = 0
                for j in range(i, k - 1, -1):
                    max_d = max(max_d, jobDifficulty[j - 1])
                    if dp[k - 1][j - 1] != float('inf'):
                        dp[k][i] = min(dp[k][i], dp[k - 1][j - 1] + max_d)
                        
        return dp[d][n] if dp[d][n] != float('inf') else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        jobDifficulty, d = json.loads(raw)
        sol = Solution()
        print(sol.minDifficulty(jobDifficulty, d))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> jd = j[0].get<vector<int>>();
        int d = j[1];
        Solution sol;
        cout << sol.minDifficulty(jd, d) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int[] jd = mapper.convertValue(data[0], int[].class);
            int d = (Integer) data[1];
            System.out.println(new Solution().minDifficulty(jd, d));
        }
    }
}""",
        "javascript": """var minDifficulty = function(jobDifficulty, d) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [jd, d] = JSON.parse(input);
    console.log(minDifficulty(jd, d));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int minDifficulty(int* jobDifficulty, int jobDifficultySize, int d){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array/int parsing
    return 0;
}"""
    }

    def solve(jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d: return -1
        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0
        for k in range(1, d + 1):
            for i in range(k, n + 1):
                max_d = 0
                for j in range(i, k - 1, -1):
                    max_d = max(max_d, jobDifficulty[j - 1])
                    if dp[k - 1][j - 1] != float('inf'):
                        dp[k][i] = min(dp[k][i], dp[k - 1][j - 1] + max_d)
        return int(dp[d][n]) if dp[d][n] != float('inf') else -1

    test_cases_data = [
        [[6,5,4,3,2,1], 2], # Sample 1
        [[9,9,9], 4],       # Sample 2
        [[1,1,1], 3],       # Sample 3
        [[7,1,7,1,7,1], 3], # Alternating
        [[11,111,22,222,33,333,44,444], 6], # Medium
        [[1], 1],           # Single job
        [[1,2,3,4,5], 1],    # One day max
        # Stress tests
        [[100]*300, 10],
        [[i for i in range(300)], 10],
        [[0]*10, 10]         # All zero difficulty
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
