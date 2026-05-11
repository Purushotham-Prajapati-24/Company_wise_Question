import json
import os

def generate_json():
    problem_id = 1389
    title = "Create Target Array in the Given Order"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1389. Create Target Array in the Given Order</h3>
<p>Given two arrays of integers&nbsp;<code>nums</code> and <code>index</code>. Your task is to create <em>target</em> array under the following rules:</p>

<ul>
	<li>Initially <em>target</em> array is empty.</li>
	<li>From left to right read <code>nums[i]</code> and <code>index[i]</code>, insert at index <code>index[i]</code>&nbsp;the value <code>nums[i]</code>&nbsp;in <em>target</em> array.</li>
	<li>Repeat the previous step until there are no elements to read in <code>nums</code> and <code>index.</code></li>
</ul>

<p>Return the <em>target</em> array.</p>

<p>It is guaranteed that the insertion operations will be valid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,2,3,4], index = [0,1,2,2,1]
<strong>Output:</strong> [0,4,1,3,2]
<strong>Explanation:</strong>
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,0], index = [0,1,2,3,0]
<strong>Output:</strong> [0,1,2,3,4]
<strong>Explanation:</strong>
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], index = [0]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length, index.length &lt;= 100</code></li>
	<li><code>nums.length == index.length</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>0 &lt;= index[i] &lt;= i</code></li>
</ul>"""

    input_format = "Two integers arrays `nums` and `index` provided as `[nums, index]` in JSON."
    output_format = "A list of integers representing the target array."

    constraints = [
        "1 <= nums.length <= 100",
        "index.length == nums.length",
        "0 <= index[i] <= i"
    ]

    explanation = """To create the target array:
1. Initialize an empty list `target`.
2. Iterate through `nums` and `index` simultaneously.
3. For each pair `(num, idx)`, insert the value `num` into the `target` list at position `idx`.
4. In most languages, a dynamic array or list supports an `insert(index, value)` method that handles shifting the existing elements to the right.
5. Return the final `target` list."""

    answer = """class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums, index = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.createTargetArray(nums, index)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> nums = j[0].get<vector<int>>();
        vector<int> index = j[1].get<vector<int>>();
        Solution sol;
        vector<int> res = sol.createTargetArray(nums, index);
        // Output res
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
    }
}""",
        "javascript": """var createTargetArray = function(nums, index) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize){
    // User logic here
    return NULL;
}

int main() {
    return 0;
}"""
    }

    def solve(nums, index):
        res = []
        for n, i in zip(nums, index):
            res.insert(i, n)
        return res

    test_cases_data = [
        [[0,1,2,3,4], [0,1,2,2,1]], # Sample 1
        [[1,2,3,4,0], [0,1,2,3,0]], # Sample 2
        [[1], [0]],                 # Sample 3
        [[1,2,3], [0,0,0]],         # Reversal
        [[1,2,3], [0,1,2]],         # Sequential
        [[10,20,30,40], [0,1,1,0]], # Complex
        # Stress tests
        [[i for i in range(100)], [0 for _ in range(100)]],
        [[i for i in range(100)], [i for i in range(100)]],
        [[5]*100, [i for i in range(100)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Simulation"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
