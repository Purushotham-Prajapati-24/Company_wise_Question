import json
import os

def generate_json():
    problem_id = 2597
    title = "The Number of Beautiful Subsets"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>2597. The Number of Beautiful Subsets</h3>
<p>You are given an array <code>nums</code> of positive integers and a <strong>positive</strong> integer <code>k</code>.</p>

<p>A subset of <code>nums</code> is <strong>beautiful</strong> if it does not contain two integers with an absolute difference equal to <code>k</code>.</p>

<p>Return <em>the number of <strong>non-empty</strong> beautiful subsets of the array</em> <code>nums</code>.</p>

<p>A <strong>subset</strong> of <code>nums</code> is an array that can be obtained by deleting some (possibly none) elements from <code>nums</code>. Two subsets are different if and only if the chosen indices to delete are different.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,6], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 1000</code></li>
</ul>
"""

    input_format = "An array of integers `nums` and an integer `k` provided as `[nums, k]` in JSON."
    output_format = "An integer representing the number of non-empty beautiful subsets."

    constraints = [
        "1 <= nums.length <= 20",
        "1 <= nums[i], k <= 1000"
    ]

    explanation = """To find the number of beautiful subsets:
1. A subset is beautiful if no two elements differ by exactly `k`.
2. Since `nums.length` is small (up to 20), we can use backtracking (recursion) to explore all possible subsets.
3. At each step `i`, we have two choices:
   - Include `nums[i]` in the subset: This is only allowed if no element already in the subset is `nums[i] - k` or `nums[i] + k`.
   - Exclude `nums[i]` from the subset.
4. Keep track of the counts of elements in the current subset using a hash map or frequency array.
5. Subtract 1 from the total count at the end to exclude the empty subset."""

    answer = """class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        self.count = 0
        n = len(nums)
        freq = {}
        
        def backtrack(idx):
            if idx == n:
                self.count += 1
                return
                
            # Option 1: Exclude nums[idx]
            backtrack(idx + 1)
            
            # Option 2: Include nums[idx]
            val = nums[idx]
            if val - k not in freq and val + k not in freq:
                freq[val] = freq.get(val, 0) + 1
                backtrack(idx + 1)
                freq[val] -= 1
                if freq[val] == 0: del freq[val]
                
        backtrack(0)
        return self.count - 1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums, k = json.loads(raw)
        sol = Solution()
        print(sol.beautifulSubsets(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> nums = j[0].get<vector<int>>();
        int k = j[1];
        Solution sol;
        cout << sol.beautifulSubsets(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int beautifulSubsets(int[] nums, int k) {
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
            int[] nums = mapper.convertValue(data[0], int[].class);
            int k = (Integer) data[1];
            System.out.println(new Solution().beautifulSubsets(nums, k));
        }
    }
}""",
        "javascript": """var beautifulSubsets = function(nums, k) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [nums, k] = JSON.parse(input);
    console.log(beautifulSubsets(nums, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int beautifulSubsets(int* nums, int numsSize, int k) {
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
    while ((c = getchar()) != EOF && c != ',');
    int k;
    if (scanf("%d", &k) == 1) {
        printf("%d\\n", beautifulSubsets(nums, s, k));
    }
    free(nums);
    return 0;
}"""
    }

    def solve(nums, k):
        n = len(nums)
        ans = 0
        def bt(idx, freq):
            nonlocal ans
            if idx == n:
                ans += 1
                return
            bt(idx + 1, freq)
            val = nums[idx]
            if freq.get(val - k, 0) == 0 and freq.get(val + k, 0) == 0:
                freq[val] = freq.get(val, 0) + 1
                bt(idx + 1, freq)
                freq[val] -= 1
        bt(0, {})
        return ans - 1

    test_cases_data = [
        [[2,4,6], 2],     # Sample 1
        [[1], 1],         # Sample 2
        [[1,2,3], 1],     # all pairs distance 1
        [[1,1,1], 1],     # duplicates
        [[10,20,30], 5],  # no diff k
        [[1,3,5,7,9], 2], # arithmetic prog
        [[1,4,7,10], 3],
        # Stress tests (limit is 20)
        [[i for i in range(1, 21)], 1],
        [[i for i in range(1, 21)], 10],
        [[1]*20, 1]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Backtracking", "Dynamic Programming", "Hash Table"], "companyIndex": 0
    }

    output_path = f"2401-2600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
