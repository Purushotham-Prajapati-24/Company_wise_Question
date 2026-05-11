import json
import os

def generate_json():
    problem_id = 523
    title = "Continuous Subarray Sum"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>523. Continuous Subarray Sum</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if <code>nums</code> has a <strong>good subarray</strong> or <code>false</code> otherwise</em>.</p>

<p>A <strong>good subarray</strong> is a subarray where:</p>
<ul>
	<li>its length is <strong>at least two</strong>, and</li>
	<li>the sum of the elements of the subarray is a multiple of <code>k</code>.</li>
</ul>

<p><strong>Note</strong> that:</p>
<ul>
	<li>A <strong>subarray</strong> is a contiguous part of the array.</li>
	<li>An integer <code>x</code> is a multiple of <code>k</code> if there exists an integer <code>n</code> such that <code>x = n * k</code>. <code>0</code> is <strong>always</strong> a multiple of <code>k</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [23,2,4,6,7], k = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [23,2,6,4,7], k = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [23,2,6,4,7], k = 13
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "Two lines: Line 1: A JSON array of integers `nums`. Line 2: An integer `k`."
    output_format = "A boolean value: `true` or `false`."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "0 <= nums[i] <= 10^9",
        "1 <= k <= 2^31 - 1"
    ]
    
    explanation = """Use a hash map to store the first time we see each running sum modulo `k`. If we see the same modulo again, it means the elements between these two indices sum to a multiple of `k`. We initialize the map with `{0: -1}` to handle cases where the subarray starts from index 0. Check whether the difference between current index and the previously stored index is at least 2."""
    
    answer = """class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_mod = 0
        mod_seen = {0: -1}
        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
        return False"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums = json.loads(raw[0])
        k = int(raw[1].strip())
        sol = Solution()
        print("true" if sol.checkSubarraySum(nums, k) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        // User logic here
        return false;
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
            } else {
                p++;
            }
        }
        int k = stoi(k_str);
        Solution sol;
        cout << (sol.checkSubarraySum(nums, k) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() > 1) {
                raw = raw.substring(1, raw.length() - 1);
            }
            List<Integer> list = new ArrayList<>();
            if (!raw.isEmpty()) {
                String[] parts = raw.split(",");
                for (String p : parts) {
                    list.add(Integer.parseInt(p.trim()));
                }
            }
            int[] nums = new int[list.size()];
            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
            
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.checkSubarraySum(nums, k) ? "true" : "false");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkSubarraySum = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(checkSubarraySum(nums, k) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool checkSubarraySum(int* nums, int numsSize, int k) {
    // User logic here
    return false;
}

int main() {
    char input[1000000];
    if (fgets(input, sizeof(input), stdin)) {
        int capacity = 10;
        int* nums = (int*)malloc(capacity * sizeof(int));
        int size = 0;
        int i = 0;
        while (input[i] != '\\0' && input[i] != '\\n') {
            if (input[i] == '-' || isdigit(input[i])) {
                int val;
                int offset = 0;
                sscanf(input + i, "%d%n", &val, &offset);
                if (offset == 0) {
                    i++;
                    continue;
                }
                if (size == capacity) {
                    capacity *= 2;
                    nums = (int*)realloc(nums, capacity * sizeof(int));
                }
                nums[size++] = val;
                i += offset;
            } else {
                i++;
            }
        }
        
        int k;
        if (scanf("%d", &k) == 1) {
            if (checkSubarraySum(nums, size, k)) printf("true\\n");
            else printf("false\\n");
        }
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[23,2,4,6,7]\\n6", "expected_output": "true", "is_sample": True},
        {"input": "[23,2,6,4,7]\\n6", "expected_output": "true", "is_sample": True},
        
        # Five Diverse Cases
        {"input": "[23,2,6,4,7]\\n13", "expected_output": "false", "is_sample": False},
        {"input": "[5,0,0,0]\\n3", "expected_output": "true", "is_sample": False},
        {"input": "[2,4,3]\\n6", "expected_output": "true", "is_sample": False},
        {"input": "[1,0]\\n2", "expected_output": "false", "is_sample": False},
        {"input": "[0]\\n1", "expected_output": "false", "is_sample": False},
        
        # Three Stress Test Cases (strict JSON format boundaries)
        {"input": "[1,2,3,4,5,6,7,8,9,10]\\n55", "expected_output": "true", "is_sample": False},
        {"input": "[99999999,99999999]\\n2", "expected_output": "true", "is_sample": False},
        {"input": "[2000000000,1000000000,500000000]\\n1000000000", "expected_output": "true", "is_sample": False}
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Hash Table", "Math", "Prefix Sum"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
