import json
import os

def generate_json():
    problem_id = 724
    title = "Find Pivot Index"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>724. Find Pivot Index</h3>
<p>Given an array of integers <code>nums</code>, calculate the <strong>pivot index</strong> of this array.</p>

<p>The <strong>pivot index</strong> is the index where the sum of all the numbers <strong>strictly</strong> to the left of the index is equal to the sum of all the numbers <strong>strictly</strong> to the index's right.</p>

<p>If the index is on the left edge of the array, then the left sum is <code>0</code> because there are no elements to the left. This also applies to the right edge of the array.</p>

<p>Return <em>the <strong>leftmost pivot index</strong></em>. If no such index exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,7,3,6,5,6]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no index that satisfies the conditions in the problem statement.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [2,1,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `nums`."
    output_format = "An integer representing the pivot index, or `-1` if it doesn't exist."

    constraints = [
        "1 <= nums.length <= 10^4",
        "-1000 <= nums[i] <= 1000"
    ]

    explanation = """First, calculate the total sum of the array. Then iterate through the array while keeping a running sum of the numbers seen so far (left sum). For each element, check if the left sum is equal to the total sum minus the left sum minus the current element. If so, return the current index."""

    answer = """class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, val in enumerate(nums):
            if leftSum == total - leftSum - val:
                return i
            leftSum += val
        return -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.pivotIndex(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        // User logic here
        return -1;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '-' || isdigit(input[i])) {
            int sign = 1, val = 0;
            if (input[i] == '-') { sign = -1; i++; }
            while (i < input.length() && isdigit(input[i])) {
                val = val * 10 + (input[i] - '0');
                i++;
            }
            res.push_back(val * sign);
        } else i++;
    }
    return res;
}

int main() {
    string n_str;
    if (getline(cin, n_str)) {
        vector<int> nums = parseArray(n_str);
        Solution sol;
        cout << sol.pivotIndex(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int pivotIndex(int[] nums) {
        // User logic here
        return -1;
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
            int[] nums = parseArray(n_str);
            Solution sol = new Solution();
            System.out.println(sol.pivotIndex(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(pivotIndex(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int pivotIndex(int* nums, int numsSize) {
    // User logic here
    return -1;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '-' || isdigit(input[i])) {
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
    char n_str[200000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int numsSize;
        int* nums = parseArray(n_str, &numsSize);
        printf("%d\\n", pivotIndex(nums, numsSize));
        free(nums);
    }
    return 0;
}"""
    }

    def solve(nums):
        total = sum(nums)
        left = 0
        for i, val in enumerate(nums):
            if left == total - left - val:
                return i
            left += val
        return -1

    test_cases_data = [
        [1,7,3,6,5,6],
        [1,2,3],
        [2,1,-1],
        [-1,-1,-1,-1,-1,0],
        [-1,-1,0,-1,-1],
        [0],
        [-1000,-1000,-1000],
        [x for x in range(-500, 501)] + [0],
        [0]*10000,
        [1]*4999 + [0] + [1]*4999
    ]

    test_cases = []
    for i, nums in enumerate(test_cases_data):
        inp = json.dumps(nums)
        out = str(solve(nums))
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
        "topics": ["Array", "Prefix Sum"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
