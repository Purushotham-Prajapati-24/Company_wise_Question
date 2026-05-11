import json
import os

def generate_json():
    problem_id = 697
    title = "Degree of an Array"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>697. Degree of an Array</h3>
<p>Given a non-empty array of non-negative integers <code>nums</code>, the <b>degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>

<p>Your task is to find the smallest possible length of a (contiguous) subarray of <code>nums</code>, that has the same degree as <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2,3,1,4,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
The degree is 3 because the element 2 appears 3 times.
The subarray [2, 2, 3, 1, 4, 2] is the shortest contiguous subarray that has the same degree.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>nums.length</code> will be between 1 and 50,000.</li>
    <li><code>nums[i]</code> will be an integer between 0 and 49,999.</li>
</ul>"""

    input_format = "A single line: JSON array `nums`."
    output_format = "An integer: the shortest length of a valid subarray."

    constraints = [
        "1 <= nums.length <= 50,000",
        "0 <= nums[i] <= 49,999"
    ]

    explanation = """Find the frequency of each element in the array, along with its first and last occurrence indices. Calculate the degree (max frequency). For each element with that max frequency, find the subarray length (last index - first index + 1). Return the minimum of these lengths."""

    answer = """class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first, last, count = {}, {}, {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
            count[v] = count.get(v, 0) + 1
        
        degree = max(count.values())
        return min(last[v] - first[v] + 1 for v in count if count[v] == degree)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.findShortestSubArray(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
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
    string input;
    if (getline(cin, input)) {
        vector<int> nums = parseArray(input);
        Solution sol;
        cout << sol.findShortestSubArray(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int findShortestSubArray(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            if (input.length() > 1) input = input.substring(1, input.length() - 1);
            if (input.isEmpty()) return;
            String[] parts = input.split(",");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.findShortestSubArray(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(findShortestSubArray(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int findShortestSubArray(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int main() {
    char input[1000000];
    if (fgets(input, sizeof(input), stdin)) {
        int cap = 10, size = 0, i = 0;
        int* res = (int*)malloc(cap * sizeof(int));
        while (input[i] && input[i] != '\\n') {
            if (isdigit(input[i])) {
                int val, off = 0;
                sscanf(input + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
                res[size++] = val;
                i += off;
            } else i++;
        }
        printf("%d\\n", findShortestSubArray(res, size));
        free(res);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(nums):
        first, last, count = {}, {}, {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
            count[v] = count.get(v, 0) + 1
        degree = max(count.values()) if count else 0
        if not count: return 0
        return min(last[v] - first[v] + 1 for v in count if count[v] == degree)

    test_cases_data = [
        [1,2,2,3,1],
        [1,2,2,3,1,4,2],
        [1],
        [2,1],
        [1,2,3,4,5],
        [5,5,5,5,5],
        [1,1,2,2,2,1],
        [100,101,102,100,101,102],
        [1,2,3,2,1,4,5,4],
        [4,4,1,1,2,2,4,4]
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
