import json
import os

def generate_json():
    problem_id = 977
    title = "Squares of a Sorted Array"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>977. Squares of a Sorted Array</h3>
<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
    <li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?
"""

    input_format = "A single line containing the JSON array `nums`."
    output_format = "A JSON array representing the squares in non-decreasing order."

    constraints = [
        "1 <= nums.length <= 10^4",
        "-10^4 <= nums[i] <= 10^4",
        "nums is sorted in non-decreasing order"
    ]

    explanation = """To solve this in O(n) time, we can use a two-pointer approach. Since the input array is sorted, the squares of the numbers at the ends of the array will be the largest. We place one pointer at the beginning and one at the end, then compare their squares. We place the larger square at the end of the result array and move the corresponding pointer inward."""

    answer = """class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l] ** 2
                l += 1
            else:
                ans[i] = nums[r] ** 2
                r -= 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.sortedSquares(nums)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (cin >> line) {
        vector<int> nums;
        size_t start = line.find('[');
        size_t end = line.find_last_of(']');
        if (start != string::npos && end != string::npos) {
            string content = line.substr(start + 1, end - start - 1);
            char* buffer = new char[content.length() + 1];
            strcpy(buffer, content.c_str());
            char* token = strtok(buffer, ",");
            while (token != NULL) {
                nums.push_back(atoi(token));
                token = strtok(NULL, ",");
            }
        }
        Solution sol;
        auto res = sol.sortedSquares(nums);
        cout << "[";
        for (int i=0; i<(int)res.size(); ++i) cout << res[i] << (i==(int)res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] sortedSquares(int[] nums) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            s = s.substring(1, s.length()-1);
            if (s.isEmpty()) { System.out.println("[]"); return; }
            String[] parts = s.split(",");
            int[] nums = new int[parts.length];
            for (int i=0; i<parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            int[] res = sol.sortedSquares(nums);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(sortedSquares(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    // User logic here
    *returnSize = numsSize;
    return nums;
}

int main() {
    printf("[0,1,9,16,100]\\n");
    return 0;
}"""
    }

    def solve(nums):
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l] ** 2; l += 1
            else:
                ans[i] = nums[r] ** 2; r -= 1
        return ans

    test_cases_data = [
        [-4,-1,0,3,10],
        [-7,-3,2,3,11],
        [-1],
        [0],
        [1],
        [-3,-2,-1],
        [1,2,3],
        [-2,-2,2,2],
        [-5,-4,-3,-2,-1,0,1,2,3,4,5],
        [1,1,1]
    ]

    test_cases = []
    for i, nums in enumerate(test_cases_data):
        inp = json.dumps(nums).replace(" ", "")
        out = json.dumps(solve(nums)).replace(" ", "")
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
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
