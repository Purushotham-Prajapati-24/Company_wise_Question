import json
import os

def generate_json():
    problem_id = 666
    title = "Path Sum IV"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>666. Path Sum IV</h3>
<p>If the depth of a tree is smaller than <code>5</code>, this tree can be represented by an array of three-digit integers. You are given an <strong>ascending</strong> array <code>nums</code> consisting of three-digit integers representing a binary tree with a depth smaller than <code>5</code>, where each integer represents a node where:</p>

<ul>
    <li>The <strong>hundreds digit</strong> represents the <strong>depth</strong> <code>d</code> of this node, where <code>1 &lt;= d &lt;= 4</code>.</li>
    <li>The <strong>tens digit</strong> represents the <strong>position</strong> <code>p</code> of this node in the level, where <code>1 &lt;= p &lt;= 8</code>, which is exactly the position in the complete binary tree numbering from left to right at that level.</li>
    <li>The <strong>units digit</strong> represents the <strong>value</strong> <code>v</code> of this node, where <code>0 &lt;= v &lt;= 9</code>.</li>
</ul>

<p>Return <em>the <strong>sum of paths</strong> from the root towards the leaves</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [113,215,221]
<strong>Output:</strong> 12
<strong>Explanation:</strong> The tree that the list represents is shown.
    3
   / \\
  5   1
The path sum is (3 + 5) + (3 + 1) = 12.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [113,221]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The tree that the list represents is shown.
    3
     \\
      1
The path sum is (3 + 1) = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 15</code></li>
    <li><code>110 &lt;= nums[i] &lt;= 489</code></li>
    <li><code>nums</code> represents a valid binary tree with depth less than <code>5</code>.</li>
    <li><code>nums</code> is sorted in <strong>ascending</strong> order.</li>
</ul>"""

    input_format = "A single line: a JSON array of integers `nums`."
    output_format = "An integer: the sum of all root-to-leaf paths."

    constraints = [
        "1 <= nums.length <= 15",
        "110 <= nums[i] <= 489",
        "nums is sorted ascending, represents valid tree with depth < 5"
    ]

    explanation = """Build a hash map: key = (depth, position), value = node value. The root is at (1, 1). For each node, its left child is at (d+1, 2*p-1) and right child at (d+1, 2*p). Use DFS: add the node value to the current path sum, and when we reach a leaf (no children in the map), add the path sum to the result."""

    answer = """class Solution:
    def pathSum(self, nums: list[int]) -> int:
        tree = {}
        for num in nums:
            d, p, v = num // 100, (num % 100) // 10, num % 10
            tree[(d, p)] = v
        
        result = 0
        
        def dfs(depth, pos, path_sum):
            nonlocal result
            if (depth, pos) not in tree:
                return
            path_sum += tree[(depth, pos)]
            left = (depth + 1, 2 * pos - 1)
            right = (depth + 1, 2 * pos)
            if left not in tree and right not in tree:
                result += path_sum
            else:
                dfs(depth + 1, 2 * pos - 1, path_sum)
                dfs(depth + 1, 2 * pos, path_sum)
        
        if nums:
            dfs(1, 1, 0)
        return result"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def pathSum(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.pathSum(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int pathSum(vector<int>& nums) {
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
            while (isdigit(input[i])) { val = val * 10 + (input[i] - '0'); i++; }
            res.push_back(val);
        } else i++;
    }
    return res;
}

int main() {
    string str;
    if (getline(cin, str)) {
        vector<int> nums = parseArray(str);
        Solution sol;
        cout << sol.pathSum(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int pathSum(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        else return new int[0];
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String str = sc.nextLine().trim();
            int[] nums = parseArray(str);
            Solution sol = new Solution();
            System.out.println(sol.pathSum(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var pathSum = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(pathSum(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int pathSum(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int* parseArray(char* input, int* outSize) {
    int cap = 20, size = 0, i = 0;
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
    *outSize = size;
    return res;
}

int main() {
    char str[500];
    if (fgets(str, sizeof(str), stdin)) {
        int numsSize;
        int* nums = parseArray(str, &numsSize);
        printf("%d\\n", pathSum(nums, numsSize));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[113,215,221]", "expected_output": "12", "is_sample": True},
        {"input": "[113,221]", "expected_output": "4", "is_sample": True},
        {"input": "[111]", "expected_output": "1", "is_sample": False},
        {"input": "[113,225,232,325,334]", "expected_output": "situated", "is_sample": False},
        {"input": "[113,215,221,325,336]", "expected_output": "27", "is_sample": False},
        {"input": "[119,217,221,329,335]", "expected_output": "37", "is_sample": False},
        {"input": "[115,211,213,311,312,313,314]", "expected_output": "40", "is_sample": False},
        {"input": "[111,211,212,311,312,313,314,411,412,413,414,415,416,417,418]", "expected_output": "84", "is_sample": False},
        {"input": "[119,215,221,313,322,335]", "expected_output": "51", "is_sample": False},
        {"input": "[117,213,225,319,325,338]", "expected_output": "53", "is_sample": False}
    ]
    # Compute expected outputs using the answer function
    def solve(nums_list):
        tree = {}
        for num in nums_list:
            d, p, v = num // 100, (num % 100) // 10, num % 10
            tree[(d, p)] = v
        result = [0]
        def dfs(depth, pos, path_sum):
            if (depth, pos) not in tree: return
            path_sum += tree[(depth, pos)]
            left = (depth + 1, 2 * pos - 1)
            right = (depth + 1, 2 * pos)
            if left not in tree and right not in tree:
                result[0] += path_sum
            else:
                dfs(depth + 1, 2 * pos - 1, path_sum)
                dfs(depth + 1, 2 * pos, path_sum)
        dfs(1, 1, 0)
        return result[0]

    for t in test_cases:
        nums_list = json.loads(t["input"])
        t["expected_output"] = str(solve(nums_list))

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
        "topics": ["Array", "Tree", "Depth-First Search"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
