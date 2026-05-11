import json
import os
from collections import deque

def generate_json():
    problem_id = 862
    title = "Shortest Subarray with Sum at Least K"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>862. Shortest Subarray with Sum at Least K</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the length of the shortest non-empty <strong>subarray</strong> of </em><code>nums</code><em> with a sum of at least </em><code>k</code>. If there is no such subarray, return <code>-1</code>.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2], k = 4
<strong>Output:</strong> -1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [2,-1,2], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
    <li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
    <li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `nums`\nLine 2: integer `k`"
    output_format = "An integer representing the length of the shortest subarray, or -1."

    constraints = [
        "1 <= nums.length <= 10^5",
        "-10^5 <= nums[i] <= 10^5",
        "1 <= k <= 10^9"
    ]

    explanation = """Since the array has negative numbers, a simple sliding window won't work. We use prefix sums and a monotonic deque. The prefix sum `P[i]` is the sum of `nums[0...i-1]`. We want to find `j > i` such that `P[j] - P[i] >= k` and `j - i` is minimized. The deque will store indices `i` such that `P[i]` is strictly increasing. When we process `P[j]`, we check the front of the deque for valid `i` and the back of the deque for maintaining monotonicity."""

    answer = """from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        res = n + 1
        dq = deque()
        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)
        return res if res <= n else -1"""

    boilerplate = {
        "python": """import sys
import json
from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        nums = json.loads(raw[0].strip())
        k = int(raw[1].strip())
        sol = Solution()
        print(sol.shortestSubarray(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        // User logic here
        return -1;
    }
};

vector<int> parseArray(string input) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < input.length() - 1) {
        if (isdigit(input[i]) || input[i] == '-') {
            int val = 0; int off=0;
            sscanf(input.c_str()+i, "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string numsStr; int k;
    if (cin >> numsStr >> k) {
        auto nums = parseArray(numsStr);
        Solution sol;
        cout << sol.shortestSubarray(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int shortestSubarray(int[] nums, int k) {
        // User logic here
        return -1;
    }
}

public class Main {
    static int[] parseArray(String s) {
        s = s.substring(1, s.length()-1);
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i=0; i<parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[] nums = parseArray(sc.next());
            int k = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.shortestSubarray(nums, k));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var shortestSubarray = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    let nums = JSON.parse(input[0]);
    let k = parseInt(input[1]);
    console.log(shortestSubarray(nums, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int shortestSubarray(int* nums, int numsSize, int k) {
    // User logic here
    return -1;
}

int main() {
    char input[100000]; int k;
    if (scanf("%s %d", input, &k) == 2) {
        int cap = 100, sz = 0;
        int* arr = malloc(cap * sizeof(int));
        char* token = strtok(input + 1, ",]");
        while (token != NULL) {
            if (sz == cap) arr = realloc(arr, (cap *= 2) * sizeof(int));
            arr[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%d\\n", shortestSubarray(arr, sz, k));
        free(arr);
    }
    return 0;
}"""
    }

    def solve(nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        res = n + 1
        dq = deque()
        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)
        return res if res <= n else -1

    test_cases_data = [
        ([1], 1),
        ([1, 2], 4),
        ([2, -1, 2], 3),
        ([1, 2, 3, 4, 5], 11),
        ([-1, -1, -1], 1),
        ([84, -37, 32, 40, 95], 167),
        ([1, 1, 1, 1, 1], 3),
        ([56, -21, 31, 35, 46, 20], 80),
        ([17, 85, 93, -45, -21], 150),
        ([1, 2, 3], 10)
    ]

    test_cases = []
    for i, (nums, k) in enumerate(test_cases_data):
        inp = f"{json.dumps(nums).replace(' ', '')}\n{k}"
        out = str(solve(nums, k))
        is_sample = i < 3
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
        "topics": ["Array", "Binary Search", "Queue", "Sliding Window", "Heap (Priority Queue)", "Prefix Sum", "Monotonic Queue"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
