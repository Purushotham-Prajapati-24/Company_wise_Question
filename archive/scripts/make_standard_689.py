import json
import os

def generate_json():
    problem_id = 689
    title = "Maximum Sum of 3 Non-Overlapping Subarrays"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>689. Maximum Sum of 3 Non-Overlapping Subarrays</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, find three non-overlapping subarrays of length <code>k</code> with maximum sum and return them.</p>

<p>Return the result as a list of indices representing the starting position of each interval (<strong>0-indexed</strong>). If there are multiple answers, return the lexicographically smallest one.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,2,6,7,5,1], k = 2
<strong>Output:</strong> [0,3,5]
<strong>Explanation:</strong> Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,2,1,2,1,2,1], k = 2
<strong>Output:</strong> [0,2,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= nums[i] &lt; 2<sup>16</sup></code></li>
    <li><code>1 &lt;= k &lt;= floor(nums.length / 3)</code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `nums`.\nLine 2: Integer `k`."
    output_format = "A JSON array of 3 integers: the starting indices of the 3 subarrays."

    constraints = [
        "1 <= nums.length <= 2 * 10^4",
        "1 <= nums[i] < 2^16",
        "1 <= k <= floor(nums.length / 3)"
    ]

    explanation = """Precompute sliding window sums of size k. Build left[i] = best start idx for window sum in [0..i], and right[i] = best start idx in [i..n-k]. Then iterate middle window from k to n-2k, using left[mid-1] and right[mid+k] to find max sum."""

    answer = """class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        sums = [sum(nums[:k])]
        for i in range(1, n - k + 1):
            sums.append(sums[-1] - nums[i-1] + nums[i+k-1])
        
        left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best
        
        right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best
        
        result = None
        for mid in range(k, n - 2*k + 1):
            l, r = left[mid - k], right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if result is None or total > sums[result[0]] + sums[result[1]] + sums[result[2]]:
                result = [l, mid, r]
        return result"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums = json.loads(raw[0])
        k = int(raw[1])
        sol = Solution()
        print(json.dumps(sol.maxSumOfThreeSubarrays(nums, k)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        // User logic here
        return {};
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
        vector<int> ans = sol.maxSumOfThreeSubarrays(nums, k);
        cout << "[" << ans[0] << "," << ans[1] << "," << ans[2] << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        // User logic here
        return new int[]{};
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
                int[] ans = sol.maxSumOfThreeSubarrays(nums, k);
                System.out.println("[" + ans[0] + "," + ans[1] + "," + ans[2] + "]");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(JSON.stringify(maxSumOfThreeSubarrays(nums, k)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* maxSumOfThreeSubarrays(int* nums, int numsSize, int k, int* returnSize) {
    // User logic here
    *returnSize = 3;
    int* res = (int*)malloc(3 * sizeof(int));
    res[0] = 0; res[1] = 0; res[2] = 0;
    return res;
}

int* parseArray(char* input, int* outSize) {
    int cap = 100, size = 0, i = 0;
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
    char n_str[500000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int numsSize;
        int* nums = parseArray(n_str, &numsSize);
        int k;
        if (scanf("%d", &k) == 1) {
            int returnSize;
            int* ans = maxSumOfThreeSubarrays(nums, numsSize, k, &returnSize);
            printf("[%d,%d,%d]\\n", ans[0], ans[1], ans[2]);
            free(ans);
        }
        free(nums);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(nums, k):
        n = len(nums)
        sums = [sum(nums[:k])]
        for i in range(1, n - k + 1):
            sums.append(sums[-1] - nums[i-1] + nums[i+k-1])
        left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]: best = i
            left[i] = best
        right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]: best = i
            right[i] = best
        result = None
        for mid in range(k, n - 2*k + 1):
            l, r = left[mid - k], right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if result is None or total > sums[result[0]] + sums[result[1]] + sums[result[2]]:
                result = [l, mid, r]
        return result

    test_cases_data = [
        ([1,2,1,2,6,7,5,1], 2),
        ([1,2,1,2,1,2,1,2,1], 2),
        ([1,2,3,4,5,6,7,8,9], 3),
        ([5,5,5,5,5,5,5,5,5], 3),
        ([1,1,1,1,1,1,1,1,1,1,1,1], 4),
        ([9,8,7,6,5,4,3,2,1], 3),
        ([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3], 5),
        ([1,2,3,4,5,6,7,8,9,10,11,12], 2),
        ([100,1,1,100,1,1,100,1,1,1], 1),
        ([4,4,4,4,4,4,4,4,4], 3)
    ]

    test_cases = []
    for i, (nums, k) in enumerate(test_cases_data):
        inp = json.dumps(nums) + "\\n" + str(k)
        out = json.dumps(solve(nums, k))
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
        "topics": ["Array", "Dynamic Programming", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
