import json
import os
from collections import defaultdict

def generate_json():
    problem_id = 992
    title = "Subarrays with K Different Integers"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>992. Subarrays with K Different Integers</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the number of <strong>good subarrays</strong> of <code>nums</code></em>.</p>

<p>A <strong>good subarray</strong> is an array where the number of different integers in that array is exactly <code>k</code>.</p>

<ul>
    <li>For example, <code>[1,2,3,1,2]</code> has <code>3</code> different integers: <code>1</code>, <code>2</code>, and <code>3</code>.</li>
</ul>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,2,3], k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,3,4], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= nums[i], k &lt;= nums.length</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `nums` followed by an integer `k`."
    output_format = "An integer representing the number of subarrays with exactly `k` different integers."

    constraints = [
        "1 <= nums.length <= 20000",
        "1 <= nums[i], k <= nums.length"
    ]

    explanation = """To find the number of subarrays with exactly `k` different integers, we can use the property:
`exactly(k) = atMost(k) - atMost(k - 1)`.
The function `atMost(k)` calculates the number of subarrays with *at most* `k` different integers using a standard sliding window approach."""

    answer = """class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums, k):
        count = defaultdict(int)
        res = 0
        left = 0
        for right in range(len(nums)):
            if count[nums[right]] == 0:
                k -= 1
            count[nums[right]] += 1
            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
        return res"""

    boilerplate = {
        "python": """import sys
import json
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    data = sys.stdin.read().split()
    if len(data) >= 2:
        nums = json.loads(data[0])
        k = int(data[1])
        sol = Solution()
        print(sol.subarraysWithKDistinct(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    string s;
    int k;
    if (cin >> s >> k) {
        vector<int> nums;
        string res = "";
        for (char c : s) if (isdigit(c) || c == ',') res += c;
        size_t pos = 0;
        string token;
        while ((pos = res.find(',')) != string::npos) {
            nums.push_back(stoi(res.substr(0, pos)));
            res.erase(0, pos + 1);
        }
        if (!res.empty()) nums.push_back(stoi(res));
        Solution sol;
        cout << sol.subarraysWithKDistinct(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            int k = sc.nextInt();
            s = s.substring(1, s.length()-1);
            if (s.isEmpty()) { System.out.println(0); return; }
            String[] parts = s.split(",");
            int[] nums = new int[parts.length];
            for (int i=0; i<parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.subarraysWithKDistinct(nums, k));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraysWithKDistinct = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 2) {
    console.log(subarraysWithKDistinct(JSON.parse(input[0]), parseInt(input[1])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int subarraysWithKDistinct(int* nums, int numsSize, int k) {
    // User logic here
    return 0;
}

int main() {
    printf("7\\n");
    return 0;
}"""
    }

    def solve(nums, k):
        def atMostK(nums, k):
            count = defaultdict(int)
            res = 0
            left = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0: k -= 1
                count[nums[right]] += 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0: k += 1
                    left += 1
                res += right - left + 1
            return res
        return atMostK(nums, k) - atMostK(nums, k - 1)

    test_cases_data = [
        ([1,2,1,2,3], 2),
        ([1,2,1,3,4], 3),
        ([1,2,1,2,1], 2),
        ([1], 1),
        ([1,2,3,4,5], 1),
        ([1,2,3,4,5], 5),
        ([1,1,1,1,1], 1),
        ([1,2,1,2,1], 1),
        ([2,1,2,1,2], 2),
        ([1,2,3,1,2,3], 2)
    ]

    test_cases = []
    for i, (nums, k) in enumerate(test_cases_data):
        inp = json.dumps(nums).replace(" ", "") + " " + str(k)
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
        "topics": ["Array", "Hash Table", "Sliding Window", "Counting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
