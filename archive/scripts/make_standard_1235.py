import json
import os

def generate_json():
    problem_id = 1235
    title = "Maximum Profit in Job Scheduling"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1235. Maximum Profit in Job Scheduling</h3>
<p>We have <code>n</code> jobs, where every job is scheduled to be done from <code>startTime[i]</code> to <code>endTime[i]</code>, obtaining a profit of <code>profit[i]</code>.</p>

<p>You're given the <code>startTime</code>, <code>endTime</code> and <code>profit</code> arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time ranges.</p>

<p>If you choose a job that ends at time <code>X</code> you will be able to start another job that starts at time <code>X</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png" style="width: 380px; height: 154px;">
<pre><strong>Input:</strong> startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
<strong>Output:</strong> 120
<strong>Explanation:</strong> The subset chosen is the first and fourth job. 
Time range [1,3] and [3,6] , total profit is 50 + 70 = 120.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample2_1584.png" style="width: 441px; height: 154px;">
<pre><strong>Input:</strong> startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
<strong>Output:</strong> 150
<strong>Explanation:</strong> The subset chosen is the first, fourth and fifth job. 
Profit obtained: 20 + 70 + 60 = 150.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png" style="width: 380px; height: 154px;">
<pre><strong>Input:</strong> startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
<strong>Output:</strong> 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= startTime.length == endTime.length == profit.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= startTime[i] &lt;= endTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= profit[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Three arrays `startTime`, `endTime`, and `profit` provided as `[startTime, endTime, profit]` in JSON."
    output_format = "An integer representing the maximum profit."

    constraints = [
        "1 <= n <= 5 * 10^4",
        "1 <= time <= 10^9",
        "1 <= profit <= 10^4"
    ]

    explanation = """To find the maximum profit in job scheduling:
1. Combine `startTime`, `endTime`, and `profit` into a list of jobs.
2. Sort the jobs by their `endTime`.
3. Use dynamic programming where `dp[i]` is the maximum profit considering the first `i` jobs.
4. For each job `j`:
   - Find the latest previous job `k` that does not overlap with job `j` (i.e., `jobs[k].endTime <= jobs[j].startTime`). Use binary search for efficiency.
   - `dp[j] = max(dp[j-1], profit[j] + (dp[k] if k exists else 0))`.
5. The result is `dp[n]`.
6. To optimize binary search, use `bisect_right` on a sorted list of end times."""

    answer = """import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        # dp stores [endTime, maxProfit]
        dp = [[0, 0]]
        for s, e, p in jobs:
            # find the latest job that ends before or at s
            i = bisect.bisect_right(dp, [s, float('inf')]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]"""

    boilerplate = {
        "python": """import sys
import json
import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        startTime, endTime, profit = json.loads(raw)
        sol = Solution()
        print(sol.jobScheduling(startTime, endTime, profit))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> s = j[0].get<vector<int>>();
        vector<int> e = j[1].get<vector<int>>();
        vector<int> p = j[2].get<vector<int>>();
        Solution sol;
        cout << sol.jobScheduling(s, e, p) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
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
            int[] s = mapper.convertValue(data[0], int[].class);
            int[] e = mapper.convertValue(data[1], int[].class);
            int[] p = mapper.convertValue(data[2], int[].class);
            System.out.println(new Solution().jobScheduling(s, e, p));
        }
    }
}""",
        "javascript": """var jobScheduling = function(startTime, endTime, profit) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [s, e, p] = JSON.parse(input);
    console.log(jobScheduling(s, e, p));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int jobScheduling(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int* profit, int profitSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    import bisect
    def solve(startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect_right(dp, [s, float('inf')]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]

    test_cases_data = [
        [[1,2,3,3], [3,4,5,6], [50,10,40,70]], # Sample 1
        [[1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]], # Sample 2
        [[1,1,1], [2,3,4], [5,6,4]], # Sample 3
        [[1,2,3], [2,3,4], [10,10,10]], # Non-overlapping
        [[1,1,1], [4,4,4], [10,20,30]], # Total overlapping
        [[1,5,10], [10,15,20], [100,10,100]], # Middle job overlap
        [[1], [2], [100]], # Single job
        # Stress tests
        [[i for i in range(1000)], [i+1 for i in range(1000)], [1 for _ in range(1000)]], # All compatible
        [[i for i in range(1000)], [i+1000 for i in range(1000)], [1 for _ in range(1000)]], # Heavy overlap
        [[1]*1000, [10**9]*1000, [10**4 for _ in range(1000)]] # Many same starts
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1], t[2]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Binary Search", "Dynamic Programming", "Sorting"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
