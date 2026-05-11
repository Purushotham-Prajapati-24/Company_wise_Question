import json
import os

def generate_json():
    problem_id = 1283
    title = "Find the Smallest Divisor Given a Threshold"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1283. Find the Smallest Divisor Given a Threshold</h3>
<p>Given an array of integers <code>nums</code> and an integer <code>threshold</code>, we will choose a positive integer <code>divisor</code>, divide all the array by it, and sum the division's result. Find the <strong>smallest</strong> <code>divisor</code> such that the result mentioned above is less than or equal to <code>threshold</code>.</p>

<p>Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: <code>7/3 = 3</code> and <code>10/2 = 5</code>).</p>

<p>The test cases are generated so that there will be an answer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,5,9], threshold = 6
<strong>Output:</strong> 5
<strong>Explanation:</strong> We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3). If the divisor is 5 the sum will be 5 (1+1+1+2). 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [44,22,33,11,1], threshold = 5
<strong>Output:</strong> 44
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>nums.length &lt;= threshold &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "A list of integers `nums` and an integer `threshold` provided as `[nums, threshold]` in JSON."
    output_format = "An integer representing the smallest divisor."

    constraints = [
        "1 <= nums.length <= 5 * 10^4",
        "1 <= nums[i] <= 10^6",
        "nums.length <= threshold <= 10^6"
    ]

    explanation = """To find the smallest divisor:
1. The smallest possible divisor is 1, and the largest can be the maximum element in `nums`.
2. This suggests using Binary Search over the range `[1, max(nums)]`.
3. For a chosen `mid` divisor:
   - Calculate the sum of `ceil(nums[i] / mid)`.
   - `ceil(a / b)` can be calculated as `(a + b - 1) // b`.
   - If `sum <= threshold`, then `mid` is a potential candidate. Try smaller divisors: `high = mid - 1`.
   - Otherwise, `mid` is too small. Try larger divisors: `low = mid + 1`.
4. The smallest divisor satisfying the condition will be `low` at the end of the search."""

    answer = """import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2
            total = sum((x + mid - 1) // mid for x in nums)
            if total <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low"""

    boilerplate = {
        "python": """import sys
import json
import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums, threshold = json.loads(raw)
        sol = Solution()
        print(sol.smallestDivisor(nums, threshold))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> nums = j[0].get<vector<int>>();
        int threshold = j[1];
        Solution sol;
        cout << sol.smallestDivisor(nums, threshold) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int[] nums = mapper.convertValue(data[0], int[].class);
            int threshold = (Integer) data[1];
            System.out.println(new Solution().smallestDivisor(nums, threshold));
        }
    }
}""",
        "javascript": """var smallestDivisor = function(nums, threshold) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    const [nums, threshold] = JSON.parse(input);
    console.log(smallestDivisor(nums, threshold));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int smallestDivisor(int* nums, int numsSize, int threshold){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(nums, threshold):
        low, high = 1, max(nums)
        while low <= high:
            mid = (low + high) // 2
            total = sum((x + mid - 1) // mid for x in nums)
            if total <= threshold: high = mid - 1
            else: low = mid + 1
        return low

    test_cases_data = [
        [[1,2,5,9], 6],         # Sample 1
        [[44,22,33,11,1], 5],   # Sample 2
        [[1,1,1], 3],           # Exact
        [[1,1,1], 10],          # Min divisor 1
        [[1000000], 1],          # Large single
        [[1,1000000], 2],        # Max split
        [[1,2,3,4,5], 15],       # Threshold = sum
        # Stress tests
        [[1000000]*1000, 1000],
        [[1]*50000, 50000],
        [[i for i in range(1, 50000)], 1000000]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Binary Search"], "companyIndex": 0
    }

    output_path = f"1101-1300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
