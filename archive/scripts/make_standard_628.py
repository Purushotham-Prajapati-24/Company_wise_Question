import json
import os

def generate_json():
    problem_id = 628
    title = "Maximum Product of Three Numbers"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>628. Maximum Product of Three Numbers</h3>
<p>Given an integer array <code>nums</code>, <em>find three numbers whose product is maximum and return the maximum product</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 24
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [-1,-2,-3]
<strong>Output:</strong> -6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line: JSON array of integers `nums`."
    output_format = "An integer: the maximum product of three numbers."

    constraints = [
        "3 <= nums.length <= 10^4",
        "-1000 <= nums[i] <= 1000"
    ]

    explanation = """Sort the array. The maximum product is either the product of the three largest numbers, or the product of the two smallest (most negative) numbers and the largest number. Return the max of these two candidates."""

    answer = """class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.maximumProduct(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '-' || isdigit(input[i])) {
            size_t next;
            res.push_back(stoi(input.substr(i), &next));
            i += next;
        } else i++;
    }
    return res;
}

int main() {
    string str;
    if (getline(cin, str)) {
        vector<int> nums = parseArray(str);
        Solution sol;
        cout << sol.maximumProduct(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int maximumProduct(int[] nums) {
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
            System.out.println(sol.maximumProduct(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(maximumProduct(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int maximumProduct(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '-' || isdigit(input[i])) {
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
    char str[500000];
    if (fgets(str, sizeof(str), stdin)) {
        int numsSize;
        int* nums = parseArray(str, &numsSize);
        printf("%d\\n", maximumProduct(nums, numsSize));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,2,3]", "expected_output": "6", "is_sample": True},
        {"input": "[1,2,3,4]", "expected_output": "24", "is_sample": True},
        {"input": "[-1,-2,-3]", "expected_output": "-6", "is_sample": False},
        {"input": "[-100,-100,1,2,3]", "expected_output": "30000", "is_sample": False},
        {"input": "[-1,-2,1,2,3]", "expected_output": "6", "is_sample": False},
        {"input": "[0,0,0,1000]", "expected_output": "0", "is_sample": False},
        {"input": "[-1000,-1000,-1000]", "expected_output": "-1000000000", "is_sample": False},
        {"input": "[" + ",".join(str(-1000 + i) for i in range(10000)) + "]", "expected_output": str(997 * 998 * 999), "is_sample": False},
        {"input": "[" + ",".join("-1000" for _ in range(9999)) + ",1000]", "expected_output": str((-1000) * (-1000) * 1000), "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(10000)) + "]", "expected_output": str(9999 * 9998 * 9997), "is_sample": False}
    ]

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
        "topics": ["Array", "Math", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
