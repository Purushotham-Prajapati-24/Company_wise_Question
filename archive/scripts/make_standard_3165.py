import json
import os

def generate_json():
    problem_id = 3165
    title = "Maximum Sum of Subsequence With Non-adjacent Elements"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>3165. Maximum Sum of Subsequence With Non-adjacent Elements</h3>
<p>You are given an array <code>nums</code> consisting of integers. You are also given a 2D array <code>queries</code> where <code>queries[i] = [pos<sub>i</sub>, x<sub>i</sub>]</code>.</p>

<p>For each query, first set <code>nums[pos<sub>i</sub>] = x<sub>i</sub></code>, then calculate the maximum possible <strong>sum</strong> of a <strong>subsequence</strong> of <code>nums</code> such that no two elements in the subsequence are <strong>adjacent</strong>.</p>

<p>Return the <strong>sum</strong> of the answers to all queries. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,9], queries = [[1,-2],[0,-3]]
<strong>Output:</strong> 21
<strong>Explanation:</strong>
After the 1st query, nums = [3,-2,9]. The maximum sum of a subsequence with non-adjacent elements is 3 + 9 = 12.
After the 2nd query, nums = [-3,-2,9]. The maximum sum of a subsequence with non-adjacent elements is 9.
The sum of answers is 12 + 9 = 21.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,-1], queries = [[0,-5]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
After the 1st query, nums = [-5,-1]. The maximum sum of a subsequence with non-adjacent elements is 0 (empty subsequence).
The sum of answers is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i] == [pos<sub>i</sub>, x<sub>i</sub>]</code></li>
	<li><code>0 &lt;= pos<sub>i</sub> &lt;= nums.length - 1</code></li>
	<li><code>-10<sup>5</sup> &lt;= x<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "An array of integers `nums` and a 2D array `queries` provided as `[nums, queries]` in JSON."
    output_format = "An integer representing the sum of maximum subsequence sums modulo 10^9 + 7."

    constraints = [
        "1 <= nums.length, queries.length <= 5 * 10^4",
        "-10^5 <= nums[i], x_i <= 10^5"
    ]

    explanation = """To solve this problem with updates:
1. This is a classic "House Robber" problem with point updates.
2. For a static array, we use DP. For dynamic updates, we use a segment tree.
3. Each node in the segment tree represents a range `[L, R]`.
4. We store four values for each node:
   - `f00`: max sum in `[L, R]` excluding both `L` and `R`.
   - `f01`: max sum in `[L, R]` excluding `L` but possibly including `R`.
   - `f10`: max sum in `[L, R]` including `L` but possibly excluding `R`.
   - `f11`: max sum in `[L, R]` possibly including both `L` and `R` (but `L` and `R` can't be included if they are adjacent).
5. Merge children `node.left` and `node.right`:
   - `node.f00 = max(left.f00 + right.f10, left.f01 + right.f00)`
   - `node.f01 = max(left.f00 + right.f11, left.f01 + right.f01)`
   - `node.f10 = max(left.f10 + right.f10, left.f11 + right.f00)`
   - `node.f11 = max(left.f10 + right.f11, left.f11 + right.f01)`
6. For a leaf node representing `nums[i]`:
   - `f11 = max(0, nums[i])`, others 0 (or appropriately handled).
7. The answer to each query is `root.f11`.
8. Final result is the sum of these answers modulo 10^9 + 7."""

    answer = """class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        # segment tree nodes: f00, f01, f10, f11
        tree = [[0]*4 for _ in range(4 * n)]
        
        def push_up(v):
            l, r = 2*v, 2*v+1
            tree[v][0] = max(tree[l][0] + tree[r][2], tree[l][1] + tree[r][0])
            tree[v][1] = max(tree[l][0] + tree[r][3], tree[l][1] + tree[r][1])
            tree[v][2] = max(tree[l][2] + tree[r][2], tree[l][3] + tree[r][0])
            tree[v][3] = max(tree[l][2] + tree[r][3], tree[l][3] + tree[r][1])

        def build(v, tl, tr):
            if tl == tr:
                tree[v][3] = max(0, nums[tl])
                return
            tm = (tl + tr) // 2
            build(2*v, tl, tm)
            build(2*v+1, tm+1, tr)
            push_up(v)

        def update(v, tl, tr, pos, val):
            if tl == tr:
                tree[v][3] = max(0, val)
                return
            tm = (tl + tr) // 2
            if pos <= tm: update(2*v, tl, tm, pos, val)
            else: update(2*v+1, tm+1, tr, pos, val)
            push_up(v)

        build(1, 0, n - 1)
        res = 0
        MOD = 10**9 + 7
        for pos, val in queries:
            update(1, 0, n - 1, pos, val)
            res = (res + tree[1][3]) % MOD
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums, queries = json.loads(raw)
        sol = Solution()
        print(sol.maximumSumSubsequence(nums, queries))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumSumSubsequence(vector<int>& nums, vector<vector<int>>& queries) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<int> nums = j[0].get<vector<int>>();
        vector<vector<int>> queries = j[1].get<vector<vector<int>>>();
        Solution sol;
        cout << sol.maximumSumSubsequence(nums, queries) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maximumSumSubsequence(int[] nums, int[][] queries) {
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
            int[][] queries = mapper.convertValue(data[1], int[][].class);
            System.out.println(new Solution().maximumSumSubsequence(nums, queries));
        }
    }
}""",
        "javascript": """var maximumSumSubsequence = function(nums, queries) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [nums, queries] = JSON.parse(input);
    console.log(maximumSumSubsequence(nums, queries));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int maximumSumSubsequence(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int h_cap = 128, h_size = 0;
    int* nums = malloc(h_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (h_size >= h_cap) { h_cap *= 2; nums = realloc(nums, h_cap * sizeof(int)); }
        scanf("%d", &nums[h_size++]);
    }
    while ((c = getchar()) != EOF && c != '[');
    int q_cap = 128, q_size = 0;
    int** queries = malloc(q_cap * sizeof(int*));
    int* colSizes = malloc(q_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && c != '[' && c != ']');
        if (c == EOF || c == ']') break;
        int row_cap = 2, row_size = 0;
        int* row = malloc(row_cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (row_size >= row_cap) { row_cap *= 2; row = realloc(row, row_cap * sizeof(int)); }
            scanf("%d", &row[row_size++]);
        }
        if (q_size >= q_cap) { q_cap *= 2; queries = realloc(queries, q_cap * sizeof(int*)); colSizes = realloc(colSizes, q_cap * sizeof(int)); }
        queries[q_size] = row;
        colSizes[q_size++] = row_size;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    printf("%d\\n", maximumSumSubsequence(nums, h_size, queries, q_size, colSizes));
    return 0;
}"""
    }

    def solve(nums, queries):
        n = len(nums)
        tree = [[0]*4 for _ in range(4 * n)]
        def push_up(v):
            l, r = 2*v, 2*v+1
            tree[v][0] = max(tree[l][0] + tree[r][2], tree[l][1] + tree[r][0])
            tree[v][1] = max(tree[l][0] + tree[r][3], tree[l][1] + tree[r][1])
            tree[v][2] = max(tree[l][2] + tree[r][2], tree[l][3] + tree[r][0])
            tree[v][3] = max(tree[l][2] + tree[r][3], tree[l][3] + tree[r][1])
        def build(v, tl, tr):
            if tl == tr:
                tree[v][3] = max(0, nums[tl])
                return
            tm = (tl + tr) // 2
            build(2*v, tl, tm)
            build(2*v+1, tm+1, tr)
            push_up(v)
        def update(v, tl, tr, pos, val):
            if tl == tr:
                tree[v][3] = max(0, val)
                return
            tm = (tl + tr) // 2
            if pos <= tm: update(2*v, tl, tm, pos, val)
            else: update(2*v+1, tm+1, tr, pos, val)
            push_up(v)
        build(1, 0, n - 1)
        res = 0
        MOD = 10**9 + 7
        for pos, val in queries:
            update(1, 0, n - 1, pos, val)
            res = (res + tree[1][3]) % MOD
        return res

    test_cases_data = [
        [[3,5,9], [[1,-2],[0,-3]]], # Sample 1
        [[0,-1], [[0,-5]]],        # Sample 2
        [[1,2,3], [[0,10],[2,10]]], 
        [[10,10,10,10], [[1,0]]],
        [[-1,-2,-3], [[0,1],[2,1]]],
        [[0,0,0], [[1,5]]],
        [[5], [[0,-5],[0,10]]],
        # Stress tests
        [[i for i in range(1000)], [[999, 0]]*100],
        [[10**5 if i%2==0 else -10**5 for i in range(1000)], [[500, 0]]*100],
        [[0]*1000, [[i, i] for i in range(1000)]]
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
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 512, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Segment Tree"], "companyIndex": 0
    }

    output_path = f"3001-3200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
