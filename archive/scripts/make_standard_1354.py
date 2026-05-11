import json
import os

def generate_json():
    problem_id = 1354
    title = "Construct Target Array With Multiple Sums"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1354. Construct Target Array With Multiple Sums</h3>
<p>You are given an array <code>target</code> of n integers. From a starting array <code>arr</code> consisting of <code>n</code> 1's, you may perform the following procedure:</p>

<ul>
	<li>let <code>x</code> be the sum of all elements currently in your array.</li>
	<li>choose index <code>i</code>, such that <code>0 &lt;= i &lt; n</code> and set the value of <code>arr</code> at index <code>i</code> to <code>x</code>.</li>
	<li>you may repeat this procedure as many times as needed.</li>
</ul>

<p>Return <code>true</code> <em>if it is possible to construct the</em> <code>target</code> <em>array from</em> <code>arr</code><em>, otherwise, return</em> <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> target = [9,3,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Start with [1, 1, 1] 
[1, 1, 1], sum = 3, choose index 1, replace with 3 ==> [1, 3, 1]
[1, 3, 1], sum = 5, choose index 2, replace with 5 ==> [1, 3, 5]
[1, 3, 5], sum = 9, choose index 0, replace with 9 ==> [9, 3, 5] Done
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> target = [1,1,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Impossible to create target array from [1,1,1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> target = [8,5]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= target[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A list of integers `target` as a JSON array."
    output_format = "A boolean value `true` or `false`."

    constraints = [
        "1 <= target.length <= 5 * 10^4",
        "1 <= target[i] <= 10^9"
    ]

    explanation = """To determine if the target array is constructible:
1. Work backwards from the `target` array to the starting array of all ones.
2. In each step, the largest element in the `target` must have been the sum of the elements in the previous step.
3. Use a max-priority queue to keep track of the largest element.
4. Let `total_sum` be the sum of all elements in the current `target`.
5. For the largest element `max_val`:
   - Let `others_sum = total_sum - max_val`.
   - The previous value of the element that is currently `max_val` would be `max_val - others_sum`.
   - If `others_sum == 1`, return `true` (special case like `[8, 1]`).
   - If `others_sum == 0` or `max_val <= others_sum` or `max_val % others_sum == 0`, it might be impossible unless `others_sum == 1`.
   - Use modulo to speed up: `prev_val = max_val % others_sum`. If `prev_val == 0`, set it to `others_sum` (but only if we need to continue; actually, if `max_val % others_sum == 0` and `others_sum > 1`, it's impossible).
6. Repeat until all elements in the priority queue are 1."""

    answer = """import heapq

class Solution:
    def isPossible(self, target: list[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        pq = [-x for x in target]
        heapq.heapify(pq)
        
        while -pq[0] > 1:
            max_val = -heapq.heappop(pq)
            others_sum = total_sum - max_val
            
            if others_sum == 1:
                return True
            if max_val <= others_sum or others_sum == 0 or max_val % others_sum == 0:
                return False
            
            new_val = max_val % others_sum
            total_sum = others_sum + new_val
            heapq.heappush(pq, -new_val)
            
        return True"""

    boilerplate = {
        "python": """import sys
import json
import heapq

class Solution:
    def isPossible(self, target: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        target = json.loads(raw)
        sol = Solution()
        print(str(sol.isPossible(target)).lower())""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <numeric>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool isPossible(vector<int>& target) {
        // User logic here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> target = json::parse(line);
        Solution sol;
        cout << (sol.isPossible(target) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public boolean isPossible(int[] target) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            int[] target = mapper.readValue(sc.nextLine(), int[].class);
            System.out.println(new Solution().isPossible(target));
        }
    }
}""",
        "javascript": """var isPossible = function(target) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(isPossible(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPossible(int* target, int targetSize){
    // User logic here
    return false;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    import heapq
    def solve(target):
        if len(target) == 1: return target[0] == 1
        s = sum(target)
        pq = [-x for x in target]
        heapq.heapify(pq)
        while -pq[0] > 1:
            v = -heapq.heappop(pq)
            others = s - v
            if others == 1: return True
            if v <= others or others == 0 or v % others == 0: return False
            new_v = v % others
            s = others + new_v
            heapq.heappush(pq, -new_v)
        return True

    test_cases_data = [
        [9,3,5],         # Sample 1
        [1,1,1,2],       # Sample 2
        [8,5],           # Sample 3
        [1],             # Single 1
        [2],             # Single 2
        [1, 1000000000], # Large diff
        [1, 2, 4, 8],    # Powers of 2 (fail)
        # Stress tests
        [1]*50000,
        [2, 2, 2],
        [7, 13]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t)).lower()
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Heap (Priority Queue)"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
