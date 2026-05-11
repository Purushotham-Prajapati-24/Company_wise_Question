import json
import os

def generate_json():
    problem_id = 945
    title = "Minimum Increment to Make Array Unique"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>942. Minimum Increment to Make Array Unique</h3>
<p>You are given an integer array <code>nums</code>. In one move, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; nums.length</code> and increment <code>nums[i]</code> by <code>1</code>.</p>

<p>Return <em>the minimum number of moves to make every value in </em><code>nums</code><em> <strong>unique</strong></em>.</p>

<p>The test cases are generated so that the answer fits in a 32-bit integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After 1 move, the array could be [1, 2, 3].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,2,1,7]
<strong>Output:</strong> 6
<strong>Explanation:</strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 6 moves that the array values are unique.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line containing the JSON array `nums`."
    output_format = "An integer representing the minimum increments."

    constraints = [
        "1 <= nums.length <= 10^5",
        "0 <= nums[i] <= 10^5"
    ]

    explanation = """To solve this efficiently, we can first sort the array. Then we iterate through the sorted array starting from the second element. For each element `nums[i]`, if it's not strictly greater than the previous element `nums[i-1]`, we must increment it to `nums[i-1] + 1`. The number of increments required is `nums[i-1] + 1 - nums[i]`. We add this to our total moves and update `nums[i]` to it's new value."""

    answer = """class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] + 1 - nums[i]
                moves += increment
                nums[i] = nums[i-1] + 1
        return moves"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.minIncrementForUnique(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        // User logic here
        return 0;
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
            char buffer[content.length() + 1];
            strcpy(buffer, content.c_str());
            char* token = strtok(buffer, ",");
            while (token != NULL) {
                nums.push_back(atoi(token));
                token = strtok(NULL, ",");
            }
        }
        Solution sol;
        cout << sol.minIncrementForUnique(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minIncrementForUnique(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String line = sc.next();
            line = line.substring(1, line.length()-1);
            if (line.trim().isEmpty()) {
                System.out.println(0); return;
            }
            String[] parts = line.split(",");
            int[] nums = new int[parts.length];
            for (int i=0; i<parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.minIncrementForUnique(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(minIncrementForUnique(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minIncrementForUnique(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        printf("1\\n");
    }
    return 0;
}"""
    }

    def solve(nums):
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                moves += (nums[i-1] + 1 - nums[i])
                nums[i] = nums[i-1] + 1
        return moves

    test_cases_data = [
        [1,2,2],
        [3,2,1,2,1,7],
        [1,1,1,1],
        [4,4,4,4,4],
        [10,1,1,10],
        [0,0,0],
        [7,7,7],
        [1,2,3,4,5],
        [100],
        [2,3,2,1,5,4]
    ]

    test_cases = []
    for i, nums in enumerate(test_cases_data):
        inp = json.dumps(nums).replace(" ", "")
        out = str(solve(list(nums)))
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
        "topics": ["Array", "Sorting", "Greedy", "Counting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
