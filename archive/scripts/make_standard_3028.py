import json
import os

def generate_json():
    problem_id = 3028
    title = "Ant on the Boundary"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>3028. Ant on the Boundary</h3>
<p>An ant is at the boundary of a 1D grid. At each step, it moves a certain distance to the left or right.</p>

<p>You are given an array of <strong>non-zero</strong> integers <code>nums</code>. The ant starts at position <code>0</code> and moves <code>nums[i]</code> distance in the <code>i<sup>th</sup></code> step. The sign of <code>nums[i]</code> indicates the direction: positive means moving to the right, and negative means moving to the left.</p>

<p>Return <em>the number of times the ant <strong>returns</strong> to the boundary.</em></p>

<p><strong>Note:</strong> The boundary is at position <code>0</code>. The actual return to the boundary happens when the ant's total displacement is zero.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,-5]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After the first step, the ant is at 2. After the second step, the ant is at 5. After the third step, the ant is at 0. So it returns to the boundary 1 time.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,-3,-4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> After the first step, the ant is at 3. After the second step, it's at 5. After the third step, it's at 2. After the fourth step, it's at -2. The ant never returns to the boundary.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>
"""

    input_format = "An array of integers `nums` provided as `[nums]` in JSON."
    output_format = "An integer representing the count of returns to position 0."

    constraints = [
        "1 <= nums.length <= 100",
        "-10 <= nums[i] <= 10",
        "nums[i] != 0"
    ]

    explanation = """To count returns to the boundary:
1. Maintain a variable `pos` initialized to 0.
2. Maintain a counter `returns` initialized to 0.
3. Iterate through each move `x` in `nums`:
   - Add `x` to `pos`.
   - If `pos` becomes 0, increment `returns`.
4. Return `returns`."""

    answer = """class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        pos = 0
        returns = 0
        for x in nums:
            pos += x
            if pos == 0:
                returns += 1
        return returns"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        if isinstance(nums[0], list): nums = nums[0]
        sol = Solution()
        print(sol.returnToBoundaryCount(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> nums;
        if (j.is_array() && j.size() > 0 && j[0].is_array()) nums = j[0].get<vector<int>>();
        else nums = j.get<vector<int>>();
        Solution sol;
        cout << sol.returnToBoundaryCount(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int returnToBoundaryCount(int[] nums) {
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
            int[] nums;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                nums = mapper.convertValue(((List)raw).get(0), int[].class);
            } else {
                nums = mapper.convertValue(raw, int[].class);
            }
            System.out.println(new Solution().returnToBoundaryCount(nums));
        }
    }
}""",
        "javascript": """var returnToBoundaryCount = function(nums) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let nums = JSON.parse(input);
    if (Array.isArray(nums[0])) nums = nums[0];
    console.log(returnToBoundaryCount(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int returnToBoundaryCount(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* nums = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; nums = realloc(nums, cap * sizeof(int)); }
        scanf("%d", &nums[s++]);
    }
    printf("%d\\n", returnToBoundaryCount(nums, s));
    free(nums);
    return 0;
}"""
    }

    def solve(nums):
        pos = 0
        ans = 0
        for x in nums:
            pos += x
            if pos == 0: ans += 1
        return ans

    test_cases_data = [
        [[2,3,-5]],       # Sample 1
        [[3,2,-3,-4]],    # Sample 2
        [[1,-1,1,-1]],    # Oscillating
        [[10,-10]],       # Large step
        [[-10,10]],       # Other side
        [[1,1,1,1,1]],    # No returns
        [[2,2,-2,-2,2,2,-1,-1,-1,-1]],
        # Stress tests
        [[1 if i%2==0 else -1 for i in range(100)]],
        [[10 if i%2==0 else -10 for i in range(100)]],
        [[5]*100]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Simulation"], "companyIndex": 0
    }

    output_path = f"3001-3200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
