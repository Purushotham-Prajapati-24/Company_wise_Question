import json
import os

def generate_json():
    problem_id = 713
    title = "Subarray Product Less Than K"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>713. Subarray Product Less Than K</h3>
<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than </em><code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [10,5,2,6], k = 100
<strong>Output:</strong> 8
<strong>Explanation:</strong> The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
    <li><code>0 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `nums`.\nLine 2: Integer `k`."
    output_format = "An integer: the number of valid subarrays."

    constraints = [
        "1 <= nums.length <= 3 * 10^4",
        "1 <= nums[i] <= 1000",
        "0 <= k <= 10^6"
    ]

    explanation = """Use a sliding window. Keep a running product of elements inside the window. If the product becomes >= k, increment the left pointer to shrink the window until the product is < k. The number of valid subarrays ending at the right pointer is right - left + 1."""

    answer = """class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums = json.loads(raw[0])
        k = int(raw[1])
        sol = Solution()
        print(sol.numSubarrayProductLessThanK(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        // User logic here
        return 0;
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
        cout << sol.numSubarrayProductLessThanK(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        // User logic here
        return 0;
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
                System.out.println(sol.numSubarrayProductLessThanK(nums, k));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(numSubarrayProductLessThanK(nums, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {
    // User logic here
    return 0;
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
    char n_str[500000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int numsSize;
        int* nums = parseArray(n_str, &numsSize);
        int k;
        if (scanf("%d", &k) == 1) {
            printf("%d\\n", numSubarrayProductLessThanK(nums, numsSize, k));
        }
        free(nums);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(nums, k):
        if k <= 1: return 0
        prod = 1
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    test_cases_data = [
        ([10,5,2,6], 100),
        ([1,2,3], 0),
        ([1,1,1], 1),
        ([5,4,3,2,1], 50),
        ([1,1,1,1,1], 5),
        ([1000,1000,1000], 100),
        ([2,2,2,2,2], 16),
        ([2] * 20000, 20),
        ([1] * 30000, 10),
        ([10,20,30,40,50], 1000)
    ]

    test_cases = []
    for i, (nums, k) in enumerate(test_cases_data):
        inp = json.dumps(nums) + "\\n" + str(k)
        out = str(solve(nums, k))
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
        "topics": ["Array", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
