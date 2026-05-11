import json
import os

def generate_json():
    problem_id = 560
    title = "Subarray Sum Equals K"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>560. Subarray Sum Equals K</h3>
<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to</em> <code>k</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
    <li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>"""

    input_format = "Two lines: Line 1: A JSON array of integers `nums`. Line 2: An integer `k`."
    output_format = "An integer: the number of subarrays."

    constraints = [
        "1 <= nums.length <= 2 * 10^4",
        "-1000 <= nums[i] <= 1000",
        "-10^7 <= k <= 10^7"
    ]

    explanation = """Use a hash map to track prefix sums. For each element, compute the running prefix sum. If (prefix_sum - k) exists in the hash map, it means there's a subarray that sums to k. Initialize the map with {0: 1}."""

    answer = """from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1
        for num in nums:
            prefix += num
            count += freq[prefix - k]
            freq[prefix] += 1
        return count"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums = json.loads(raw[0])
        k = int(raw[1].strip())
        sol = Solution()
        print(sol.subarraySum(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    string n_str, k_str;
    if (getline(cin, n_str) && getline(cin, k_str)) {
        vector<int> nums;
        size_t p = 0;
        while (p < n_str.length()) {
            if (n_str[p] == '-' || isdigit(n_str[p])) {
                size_t next;
                nums.push_back(stoi(n_str.substr(p), &next));
                p += next;
            } else p++;
        }
        int k = stoi(k_str);
        Solution sol;
        cout << sol.subarraySum(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int subarraySum(int[] nums, int k) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
            List<Integer> list = new ArrayList<>();
            if (!raw.isEmpty()) {
                for (String p : raw.split(",")) list.add(Integer.parseInt(p.trim()));
            }
            int[] nums = new int[list.size()];
            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.subarraySum(nums, k));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(subarraySum(nums, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int subarraySum(int* nums, int numsSize, int k) {
    // User logic here
    return 0;
}

int main() {
    char n_str[200000], k_str[50];
    if (fgets(n_str, sizeof(n_str), stdin) && fgets(k_str, sizeof(k_str), stdin)) {
        int cap = 10, size = 0, i = 0;
        int* nums = (int*)malloc(cap * sizeof(int));
        while (n_str[i] && n_str[i] != '\\n') {
            if (n_str[i] == '-' || isdigit(n_str[i])) {
                int val, off = 0;
                sscanf(n_str + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                if (size == cap) { cap *= 2; nums = realloc(nums, cap * sizeof(int)); }
                nums[size++] = val;
                i += off;
            } else i++;
        }
        int k;
        sscanf(k_str, "%d", &k);
        printf("%d\\n", subarraySum(nums, size, k));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[1,1,1]\\n2", "expected_output": "2", "is_sample": True},
        {"input": "[1,2,3]\\n3", "expected_output": "2", "is_sample": True},

        # Five Diverse Cases
        {"input": "[1]\\n1", "expected_output": "1", "is_sample": False},
        {"input": "[-1,-1,1]\\n-1", "expected_output": "2", "is_sample": False},
        {"input": "[1,-1,1]\\n1", "expected_output": "3", "is_sample": False},
        {"input": "[0,0,0]\\n0", "expected_output": "6", "is_sample": False},
        {"input": "[3,4,7,2,-3,1,4,2]\\n7", "expected_output": "4", "is_sample": False},

        # Three Stress Test Cases (max bounds)
        {"input": "[" + ",".join(["1"] * 20000) + "]\\n1", "expected_output": "20000", "is_sample": False},
        {"input": "[" + ",".join(["1000"] * 20000) + "]\\n1000", "expected_output": "20000", "is_sample": False},
        {"input": "[" + ",".join(["-1000"] * 10000 + ["1000"] * 10000) + "]\\n0", "expected_output": str(10000 * 10001 // 2), "is_sample": False}
    ]

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
        "topics": ["Array", "Hash Table", "Prefix Sum"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
