import json
import os

def generate_json():
    problem_id = 2382
    title = "Maximum Segment Sum After Removals"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>2382. Maximum Segment Sum After Removals</h3>
<p>You are given two <strong>0-indexed</strong> integer arrays <code>nums</code> and <code>removeQueries</code>, both of length <code>n</code>. For the <code>i<sup>th</sup></code> query, the element in <code>nums</code> at the index <code>removeQueries[i]</code> is removed, splitting <code>nums</code> into different segments.</p>

<p>A <strong>segment</strong> is a contiguous sequence of <strong>positive</strong> integers in <code>nums</code>. A <strong>segment sum</strong> is the sum of every element in a segment.</p>

<p>Return <em>an integer array </em><code>answer</code><em> of length </em><code>n</code><em>, where </em><code>answer[i]</code><em> is the <strong>maximum</strong> segment sum after applying the </em><code>i<sup>th</sup></code> <em>removal.</em></p>

<p><strong>Note:</strong> The value at <code>removeQueries[i]</code> is removed from <code>nums</code> but the index <code>removeQueries[i]</code> is still counted for the next removal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
<strong>Output:</strong> [14,7,2,2,0]
<strong>Explanation:</strong> Using 0 to indicate a removed element, the state is as follows:
Query 1: At index 0, 1 is removed. nums becomes [0,2,5,6,1]. Maximum segment sum is 14 (sum of [2,5,6,1]).
Query 2: At index 3, 6 is removed. nums becomes [0,2,5,0,1]. Maximum segment sum is 7 (sum of [2,5]).
Query 3: At index 2, 5 is removed. nums becomes [0,2,0,0,1]. Maximum segment sum is 2 (sum of [2]).
Query 4: At index 4, 1 is removed. nums becomes [0,2,0,0,0]. Maximum segment sum is 2 (sum of [2]).
Query 5: At index 1, 2 is removed. nums becomes [0,0,0,0,0]. Maximum segment sum is 0.
So, we return [14,7,2,2,0].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,11,1], removeQueries = [3,2,1,0]
<strong>Output:</strong> [16,5,3,0]
<strong>Explanation:</strong> Using 0 to indicate a removed element, the state is as follows:
Query 1: At index 3, 1 is removed. nums becomes [3,2,11,0]. Maximum segment sum is 16 (sum of [3,2,11]).
Query 2: At index 2, 11 is removed. nums becomes [3,2,0,0]. Maximum segment sum is 5 (sum of [3,2]).
Query 3: At index 1, 2 is removed. nums becomes [3,0,0,0]. Maximum segment sum is 3 (sum of [3]).
Query 4: At index 0, 3 is removed. nums becomes [0,0,0,0]. Maximum segment sum is 0.
So, we return [16,5,3,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length == removeQueries.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= removeQueries[i] &lt;= n - 1</code></li>
	<li><code>removeQueries</code> contains all numbers from <code>0</code> to <code>n - 1</code>.</li>
</ul>
"""

    input_format = "Two integer arrays `nums` and `removeQueries` provided as `[nums, removeQueries]` in JSON."
    output_format = "An array of 64-bit integers representing the maximum segment sum after each query."

    constraints = [
        "1 <= n <= 10^5",
        "1 <= nums[i] <= 10^9",
        "removeQueries is a permutation of indices"
    ]

    explanation = """To solve this efficiently:
1. Since we are removing elements, it's easier to think about this in reverse: start with all elements removed and add them back one by one in the reverse order of `removeQueries`.
2. As we add an element back, use a Disjoint Set Union (DSU) to merge adjacent elements that were also added back.
3. Keep track of the sum of each connected component (segment).
4. Maintain a variable `max_sum` that updates as components merge.
5. Store the `max_sum` before each addition back (which corresponds to the state after the removal in the forward direction).
6. Reverse the final answer array before returning."""

    answer = """class DSU:
    def __init__(self, n, nums):
        self.parent = list(range(n))
        self.sums = [nums[i] for i in range(n)]
        self.max_sum = 0
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.sums[root_j] += self.sums[root_i]
        self.max_sum = max(self.max_sum, self.sums[root_j])

class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(nums)
        dsu = DSU(n, nums)
        active = [False] * n
        res = [0] * n
        current_max = 0
        
        for i in range(n - 1, -1, -1):
            res[i] = current_max
            idx = removeQueries[i]
            active[idx] = True
            dsu.max_sum = max(dsu.max_sum, nums[idx])
            if idx > 0 and active[idx-1]:
                dsu.union(idx, idx-1)
            if idx < n - 1 and active[idx+1]:
                dsu.union(idx, idx+1)
            current_max = dsu.max_sum
            
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums, queries = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.maximumSegmentSum(nums, queries)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> nums = j[0].get<vector<int>>();
        vector<int> queries = j[1].get<vector<int>>();
        Solution sol;
        vector<long long> res = sol.maximumSegmentSum(nums, queries);
        json out = res;
        cout << out.dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public long[] maximumSegmentSum(int[] nums, int[] removeQueries) {
        // User logic here
        return new long[0];
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int[] nums = mapper.convertValue(data[0], int[].class);
            int[] queries = mapper.convertValue(data[1], int[].class);
            long[] res = new Solution().maximumSegmentSum(nums, queries);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var maximumSegmentSum = function(nums, removeQueries) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [nums, queries] = JSON.parse(input);
    console.log(JSON.stringify(maximumSegmentSum(nums, queries)).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

long long* maximumSegmentSum(int* nums, int numsSize, int* removeQueries, int removeQueriesSize, int* returnSize) {
    // User logic here
    return NULL;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap1 = 1024, s1 = 0;
    int* nums = malloc(cap1 * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s1 >= cap1) { cap1 *= 2; nums = realloc(nums, cap1 * sizeof(int)); }
        scanf("%d", &nums[s1++]);
    }
    while ((c = getchar()) != EOF && c != '[');
    int cap2 = 1024, s2 = 0;
    int* queries = malloc(cap2 * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s2 >= cap2) { cap2 *= 2; queries = realloc(queries, cap2 * sizeof(int)); }
        scanf("%d", &queries[s2++]);
    }
    int retSize;
    long long* res = maximumSegmentSum(nums, s1, queries, s2, &retSize);
    printf("[");
    for (int i=0; i<retSize; i++) {
        printf("%lld", res[i]);
        if (i < retSize - 1) printf(",");
    }
    printf("]\\n");
    free(nums); free(queries); free(res);
    return 0;
}"""
    }

    def solve(nums, queries):
        n = len(nums)
        parent = list(range(n))
        sums = [nums[i] for i in range(n)]
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]
        
        mx = 0
        def union(i, j):
            nonlocal mx
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                sums[root_j] += sums[root_i]
            mx = max(mx, sums[root_j])

        active = [False] * n
        res = [0] * n
        for i in range(n-1, -1, -1):
            res[i] = mx
            idx = queries[i]
            active[idx] = True
            mx = max(mx, nums[idx])
            if idx > 0 and active[idx-1]: union(idx, idx-1)
            if idx < n-1 and active[idx+1]: union(idx, idx+1)
        return res

    test_cases_data = [
        [[1,2,5,6,1], [0,3,2,4,1]],   # Sample 1
        [[3,2,11,1], [3,2,1,0]],      # Sample 2
        [[1], [0]],                   # Minimal
        [[5,5,5], [1,0,2]],           # Equal
        [[1,3,5], [1,2,0]],
        [[10,20], [0,1]],
        [[10,20], [1,0]],
        # Stress tests
        [[10**9]*1000, list(range(1000))],
        [[i+1 for i in range(10000)], list(range(9999,-1,-1))],
        [[1]*40000, [i for i in range(40000)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Union Find", "Prefix Sum", "Ordered Set"], "companyIndex": 0
    }

    output_path = f"2301-2500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
