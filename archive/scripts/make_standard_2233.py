import json
import os

def generate_json():
    problem_id = 2233
    title = "Maximum Product After K Increments"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>2233. Maximum Product After K Increments</h3>
<p>You are given an array of non-negative integers <code>nums</code> and an integer <code>k</code>. In one operation, you may choose any element from <code>nums</code> and <strong>increment</strong> it by <code>1</code>.</p>

<p>Return <em>the <strong>maximum product</strong> of</em> <code>nums</code> <em>after at most</em> <code>k</code> <em>operations.</em> Since the answer may be very large, return it <b>modulo</b> <code>10<sup>9</sup> + 7</code>. Note that you should maximize the product before taking the modulo.&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,4], k = 5
<strong>Output:</strong> 20
<strong>Explanation:</strong> Increment the first number 5 times.
Now nums = [5, 4], and the product is 5 * 4 = 20.
It can be shown that 20 is the maximum product possible, so we return 20.
Note that there may be other ways to increment nums to have the maximum product.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,3,3,2], k = 2
<strong>Output:</strong> 216
<strong>Explanation:</strong> Increment the second number 1 time and the fourth number 1 time.
Now nums = [6, 4, 3, 3], and the product is 6 * 4 * 3 * 3 = 216.
It can be shown that 216 is the maximum product possible, so we return 216.
Note that there may be other ways to increment nums to have the maximum product.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], k &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "An array of non-negative integers `nums` and an integer `k` provided as `[nums, k]` in JSON."
    output_format = "An integer representing the maximum product modulo 10^9 + 7."

    constraints = [
        "1 <= nums.length <= 10^5",
        "0 <= nums[i], k <= 10^5"
    ]

    explanation = """To maximize the product after k increments:
1. Always increment the smallest current number in the array. This is because increasing a smaller number contributes more to the overall product increase than increasing a larger one.
2. Use a min-priority queue (min-heap) to efficiently find and increment the smallest element `k` times.
3. After `k` operations, calculate the product of all elements in the heap.
4. Return the product modulo 10^9 + 7."""

    answer = """import heapq
class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums) + 1)
        
        MOD = 10**9 + 7
        res = 1
        for x in nums:
            res = (res * x) % MOD
        return res"""

    boilerplate = {
        "python": """import heapq
import sys
import json

class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums, k = json.loads(raw)
        sol = Solution()
        print(sol.maximumProduct(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> nums = j[0].get<vector<int>>();
        int k = j[1];
        Solution sol;
        cout << sol.maximumProduct(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maximumProduct(int[] nums, int k) {
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
            int k = (Integer) data[1];
            System.out.println(new Solution().maximumProduct(nums, k));
        }
    }
}""",
        "javascript": """var maximumProduct = function(nums, k) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [nums, k] = JSON.parse(input);
    console.log(maximumProduct(nums, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int maximumProduct(int* nums, int numsSize, int k) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 1024, s = 0;
    int* nums = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; nums = realloc(nums, cap * sizeof(int)); }
        scanf("%d", &nums[s++]);
    }
    while ((c = getchar()) != EOF && c != ',');
    int k;
    if (scanf("%d", &k) == 1) {
        printf("%d\\n", maximumProduct(nums, s, k));
    }
    free(nums);
    return 0;
}"""
    }

    def solve(nums, k):
        import heapq
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums) + 1)
        MOD = 10**9 + 7
        res = 1
        for x in nums: res = (res * x) % MOD
        return res

    test_cases_data = [
        [[0,4], 5],      # Sample 1
        [[6,3,3,2], 2],  # Sample 2
        [[1,2,3,4], 1],  # Small
        [[0,0,0], 10],   # Modulo 0s
        [[10,20,30], 0], # Zero k
        [[1], 10],       # Single element
        [[5,5,5], 3],    # Equality
        # Stress tests
        [[0]*100000, 100000],
        [[100000]*100000, 100000],
        [[i%10 for i in range(100000)], 50000]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0].copy(), t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Greedy", "Heap (Priority Queue)"], "companyIndex": 0
    }

    output_path = f"2101-2300/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
