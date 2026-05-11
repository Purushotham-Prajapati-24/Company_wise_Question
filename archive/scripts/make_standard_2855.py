import json
import os

def generate_json():
    problem_id = 2855
    title = "Minimum Right Shifts to Sort the Array"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>2855. Minimum Right Shifts to Sort the Array</h3>
<p>You are given a <strong>0-indexed</strong> array <code>nums</code> of length <code>n</code> containing <strong>distinct</strong> positive integers. Return <em>the <strong>minimum</strong> number of <strong>right shifts</strong> required to sort </em><code>nums</code><em> and </em><code>-1</code><em> if this is not possible.</em></p>

<p>A <strong>right shift</strong> is defined as shifting the element at index <code>i</code> to index <code>(i + 1) % n</code>, for all indices.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
After 1 right shift, nums = [2,3,4,5,1].
After 2 right shifts, nums = [1,2,3,4,5].
Since nums is now sorted, we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> nums is already sorted, so we return 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It's impossible to sort the array using right shifts.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> contains distinct integers.</li>
</ul>
"""

    input_format = "An array of integers `nums` provided as `[nums]` or single array in JSON."
    output_format = "An integer representing the minimum right shifts."

    constraints = [
        "1 <= nums.length <= 100",
        "1 <= nums[i] <= 100",
        "Distinct integers"
    ]

    explanation = """To find the minimum right shifts:
1. A right shift on a circular array is equivalent to rotating it.
2. An array can be sorted by rotation if it has at most one "drop" (i.e., an index `i` such that `nums[i] > nums[i+1]`).
3. If the array is already sorted, return 0.
4. If there is exactly one drop at index `idx` and the last element `nums[n-1]` is less than the first element `nums[0]`, then it can be sorted.
5. The number of right shifts required is `n - 1 - idx`."""

    answer = """class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        if nums == sorted_nums: return 0
        
        for k in range(1, n):
            # Shift k times
            shifted = nums[n-k:] + nums[:n-k]
            if shifted == sorted_nums:
                return k
        return -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        if isinstance(nums[0], list): nums = nums[0]
        sol = Solution()
        print(sol.minimumRightShifts(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumRightShifts(vector<int>& nums) {
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
        cout << sol.minimumRightShifts(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int minimumRightShifts(List<Integer> nums) {
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
            List<Integer> nums;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                nums = (List<Integer>) ((List)raw).get(0);
            } else {
                nums = (List<Integer>) raw;
            }
            System.out.println(new Solution().minimumRightShifts(nums));
        }
    }
}""",
        "javascript": """var minimumRightShifts = function(nums) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let nums = JSON.parse(input);
    if (Array.isArray(nums[0])) nums = nums[0];
    console.log(minimumRightShifts(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int minimumRightShifts(int* nums, int numsSize) {
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
    printf("%d\\n", minimumRightShifts(nums, s));
    free(nums);
    return 0;
}"""
    }

    def solve(nums):
        n = len(nums)
        s = sorted(nums)
        if nums == s: return 0
        for i in range(1, n):
            shifted = nums[n-i:] + nums[:n-i]
            if shifted == s: return i
        return -1

    test_cases_data = [
        [[3,4,5,1,2]],     # Sample 1
        [[1,3,5]],         # Sample 2
        [[2,1,4]],         # Sample 3
        [[1]],             # Single
        [[10, 20, 30, 5, 6, 7]], 
        [[5, 1, 2]],
        [[1, 2, 5, 3, 4]], # Impossible
        # Stress tests
        [list(range(1, 101))],
        [list(range(50, 101)) + list(range(1, 50))],
        [[100] + list(range(1, 100))]
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
        "topics": ["Array", "Sorting"], "companyIndex": 0
    }

    output_path = f"2801-3000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
