import json
import os

def generate_json():
    problem_id = 561
    title = "Array Partition"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>561. Array Partition</h3>
<p>Given an integer array <code>nums</code> of <code>2n</code> integers, group these integers into <code>n</code> pairs <code>(a<sub>1</sub>, b<sub>1</sub>), (a<sub>2</sub>, b<sub>2</sub>), ..., (a<sub>n</sub>, b<sub>n</sub>)</code> such that the sum of <code>min(a<sub>i</sub>, b<sub>i</sub>)</code> for all <code>i</code> is <strong>maximized</strong>. Return <em>the maximized sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,4,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -&gt; min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -&gt; min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -&gt; min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [6,2,6,5,1,2]
<strong>Output:</strong> 9
<strong>Explanation:</strong> The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
    <li><code>nums.length == 2 * n</code></li>
    <li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line: a JSON array of integers `nums`."
    output_format = "An integer representing the maximized sum."

    constraints = [
        "1 <= n <= 10^4",
        "nums.length == 2 * n",
        "-10^4 <= nums[i] <= 10^4"
    ]

    explanation = """To maximize the sum of minimums, sort the array and pair adjacent elements. The sum is exactly the sum of elements at even indices in the sorted array."""

    answer = """class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.arrayPairSum(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<int> nums;
        size_t p = 0;
        while (p < input.length()) {
            if (input[p] == '-' || isdigit(input[p])) {
                size_t next;
                nums.push_back(stoi(input.substr(p), &next));
                p += next;
            } else p++;
        }
        Solution sol;
        cout << sol.arrayPairSum(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int arrayPairSum(int[] nums) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
            List<Integer> list = new ArrayList<>();
            if (!raw.isEmpty()) {
                String[] parts = raw.split(",");
                for (String p : parts) list.add(Integer.parseInt(p.trim()));
            }
            int[] nums = new int[list.size()];
            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
            Solution sol = new Solution();
            System.out.println(sol.arrayPairSum(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(arrayPairSum(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int arrayPairSum(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int main() {
    char input[1000000];
    if (fgets(input, sizeof(input), stdin)) {
        int cap = 10, size = 0, i = 0;
        int* nums = (int*)malloc(cap * sizeof(int));
        while (input[i] && input[i] != '\\n') {
            if (input[i] == '-' || isdigit(input[i])) {
                int val, off = 0;
                sscanf(input + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                if (size == cap) { cap *= 2; nums = realloc(nums, cap * sizeof(int)); }
                nums[size++] = val;
                i += off;
            } else i++;
        }
        printf("%d\\n", arrayPairSum(nums, size));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,4,3,2]", "expected_output": "4", "is_sample": True},
        {"input": "[6,2,6,5,1,2]", "expected_output": "9", "is_sample": True},
        {"input": "[1,1]", "expected_output": "1", "is_sample": False},
        {"input": "[-10,10,20,-20]", "expected_output": "-10", "is_sample": False},
        {"input": "[0,0,0,0]", "expected_output": "0", "is_sample": False},
        {"input": "[-1,-2,-3,-4]", "expected_output": "-6", "is_sample": False},
        {"input": "[7,3,1,0,0,6]", "expected_output": "7", "is_sample": False},
        {"input": "[" + ",".join([str((i%100)-50) for i in range(20000)]) + "]", "expected_output": "-5000", "is_sample": False},
        {"input": "[" + ",".join(["10000"] * 20000) + "]", "expected_output": "100000000", "is_sample": False},
        {"input": "[" + ",".join([str(i) for i in range(20000)]) + "]", "expected_output": str(sum(range(0, 20000, 2))), "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_text": html_description,
        "difficulty": difficulty,
        "marks": 10,
        "input_format": input_format,
        "output_format": output_format,
        "constraints": constraints,
        "explanation": explanation,
        "answer": answer,
        "boilerplate": boilerplate,
        "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Sorting", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
