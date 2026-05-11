import json
import os

def generate_json():
    problem_id = 548
    title = "Split Array with Equal Sum"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>548. Split Array with Equal Sum</h3>
<p>Given an integer array <code>nums</code> of length <code>n</code>, return <code>true</code> if there exists a triplet <code>(i, j, k)</code> such that:</p>
<ul>
    <li><code>0 &lt; i</code></li>
    <li><code>i + 1 &lt; j</code></li>
    <li><code>j + 1 &lt; k &lt; n - 1</code></li>
    <li>The sum of the four subarrays <code>nums[0..i-1]</code>, <code>nums[i+1..j-1]</code>, <code>nums[j+1..k-1]</code>, and <code>nums[k+1..n-1]</code> are all equal.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,2,1,2,1]
<strong>Output:</strong> true
<strong>Explanation:</strong>
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1,2,1,2,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 2000</code></li>
    <li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "A single line: a JSON array of integers `nums`."
    output_format = "A boolean value: `true` or `false`."

    constraints = [
        "1 <= nums.length <= 2000",
        "-10^6 <= nums[i] <= 10^6"
    ]

    explanation = """Build prefix sums. Fix j (the middle split). For all valid i < j, store the sum of nums[0..i-1] in a set. Then for all valid k > j, check if sum of nums[k+1..n-1] equals sum of nums[j+1..k-1] and also equals some value in the set. This is O(n^2) average."""

    answer = """class Solution:
    def splitArray(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def rsum(l, r):
            return prefix[r + 1] - prefix[l]

        for j in range(3, n - 3):
            seen = set()
            for i in range(1, j - 1):
                if rsum(0, i - 1) == rsum(i + 1, j - 1):
                    seen.add(rsum(0, i - 1))
            for k in range(j + 2, n - 1):
                if rsum(j + 1, k - 1) == rsum(k + 1, n - 1):
                    if rsum(j + 1, k - 1) in seen:
                        return True
        return False"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def splitArray(self, nums: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print("true" if sol.splitArray(nums) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool splitArray(vector<int>& nums) {
        // User logic here
        return false;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<int> nums;
        size_t p = 0;
        while (p < input.length()) {
            if (input[p] == '-' || isdigit(input[p])) {
                size_t next;
                nums.push_back(stoi(input.substr(p), &next));
                p += next;
            } else p++;
        }
        Solution sol;
        cout << (sol.splitArray(nums) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean splitArray(int[] nums) {
        // User logic here
        return false;
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
            Solution sol = new Solution();
            System.out.println(sol.splitArray(nums) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {boolean}
 */
var splitArray = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(splitArray(nums) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool splitArray(int* nums, int numsSize) {
    // User logic here
    return false;
}

int main() {
    char input[100000];
    if (fgets(input, sizeof(input), stdin)) {
        int cap = 10, size = 0, i = 0;
        int* nums = (int*)malloc(cap * sizeof(int));
        while (input[i] && input[i] != '\\n') {
            if (input[i] == '-' || isdigit(input[i])) {
                int val, off = 0;
                sscanf(input + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                if (size == cap) { cap *= 2; nums = realloc(nums, cap * sizeof(int)); }
                nums[size++] = val;
                i += off;
            } else i++;
        }
        printf("%s\\n", splitArray(nums, size) ? "true" : "false");
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[1,2,1,2,1,2,1]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,1,2,1,2,1,2]", "expected_output": "false", "is_sample": True},

        # Five Diverse Cases
        {"input": "[1,1,1,1,1,1,1]", "expected_output": "true", "is_sample": False},
        {"input": "[0,0,0,0,0,0,0]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "false", "is_sample": False},
        {"input": "[3,0,2,3,0,2,3,0,2,3]", "expected_output": "true", "is_sample": False},
        {"input": "[1,1,1,1,1,1,1,1,1,1]", "expected_output": "false", "is_sample": False},

        # Three Stress Test Cases
        {"input": "[" + ",".join(["1"] * 2000) + "]", "expected_output": "false", "is_sample": False},
        {"input": "[" + ",".join(["0"] * 2000) + "]", "expected_output": "true", "is_sample": False},
        {"input": "[" + ",".join([str(i % 4) for i in range(2000)]) + "]", "expected_output": "false", "is_sample": False}
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
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
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
