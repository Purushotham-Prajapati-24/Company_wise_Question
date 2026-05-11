import json
import os

def generate_json():
    problem_id = 698
    title = "Partition to K Equal Sum Subsets"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>698. Partition to K Equal Sum Subsets</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if it is possible to divide this array into <code>k</code> non-empty subsets whose sums are all equal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,3,5,2,1], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= k &lt;= nums.length &lt;= 16</code></li>
    <li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
    <li>The frequency of each element is in the range <code>[1, 4]</code>.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `nums`.\nLine 2: Integer `k`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= k <= nums.length <= 16",
        "1 <= nums[i] <= 10000"
    ]

    explanation = """First check if the total sum is divisible by k. The target sum is total/k. Sort the array in reverse order for pruning. Use backtracking to try placing each number into one of the k buckets. If placing a number exceeds the target, skip it. If it perfectly matches without leading to a valid overall solution, and the bucket was empty, further pruning can be applied."""

    answer = """class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        nums.sort(reverse=True)
        sums = [0] * k
        
        def dfs(i):
            if i == len(nums): return True
            for j in range(k):
                if sums[j] + nums[i] <= target:
                    sums[j] += nums[i]
                    if dfs(i + 1): return True
                    sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False
            
        return dfs(0)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums = json.loads(raw[0])
        k = int(raw[1])
        sol = Solution()
        print("true" if sol.canPartitionKSubsets(nums, k) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        // User logic here
        return false;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            int val = 0;
            while (isdigit(input[i])) { val = val * 10 + (input[i]-'0'); i++; }
            res.push_back(val);
        } else i++;
    }
    return res;
}

int main() {
    string n_str, k_str;
    if (getline(cin, n_str) && getline(cin, k_str)) {
        vector<int> nums = parseArray(n_str);
        int k = stoi(k_str);
        Solution sol;
        cout << (sol.canPartitionKSubsets(nums, k) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String n_str = sc.nextLine().trim();
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                int[] nums = parseArray(n_str);
                Solution sol = new Solution();
                System.out.println(sol.canPartitionKSubsets(nums, k) ? "true" : "false");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canPartitionKSubsets = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(canPartitionKSubsets(nums, k) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool canPartitionKSubsets(int* nums, int numsSize, int k) {
    // User logic here
    return false;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
            int val, off = 0;
            sscanf(input+i, "%d%n", &val, &off);
            if (!off) { i++; continue; }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
            res[size++] = val;
            i += off;
        } else i++;
    }
    *outSize = size;
    return res;
}

int main() {
    char n_str[50000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int numsSize;
        int* nums = parseArray(n_str, &numsSize);
        int k;
        if (scanf("%d", &k) == 1) {
            printf("%s\\n", canPartitionKSubsets(nums, numsSize, k) ? "true" : "false");
        }
        free(nums);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(nums, k):
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        nums.sort(reverse=True)
        sums = [0] * k
        def dfs(i):
            if i == len(nums): return True
            for j in range(k):
                if sums[j] + nums[i] <= target:
                    sums[j] += nums[i]
                    if dfs(i + 1): return True
                    sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False
        return dfs(0)

    test_cases_data = [
        ([4,3,2,3,5,2,1], 4),
        ([1,2,3,4], 3),
        ([2,2,2,2,3,4,5], 4),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 16),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 4),
        ([10,10,10,10,10,10,10,10], 4),
        ([2,2,2,2], 2),
        ([85,35,40,64,86,45,63,16,5364,5364,5364,5364,5364], 5),
        ([3,3,3,3,4], 4),
        ([12,12,12,12,12,12], 3)
    ]

    test_cases = []
    for i, (nums, k) in enumerate(test_cases_data):
        inp = json.dumps(nums) + "\\n" + str(k)
        out = "true" if solve(nums, k) else "false"
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
        "topics": ["Array", "Dynamic Programming", "Backtracking", "Bit Manipulation", "Memoization", "Bitmask"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
