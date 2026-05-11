import json
import os

def generate_json():
    problem_id = 775
    title = "Global and Local Inversions"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>775. Global and Local Inversions</h3>
<p>You are given an integer array <code>nums</code> of length <code>n</code> which represents a permutation of all the integers in the range <code>[0, n - 1]</code>.</p>

<p>The number of <strong>global inversions</strong> is the number of the different pairs <code>(i, j)</code> where:</p>

<ul>
    <li><code>0 &lt;= i &lt; j &lt; n</code></li>
    <li><code>nums[i] &gt; nums[j]</code></li>
</ul>

<p>The number of <strong>local inversions</strong> is the number of indices <code>i</code> where:</p>

<ul>
    <li><code>0 &lt;= i &lt; n - 1</code></li>
    <li><code>nums[i] &gt; nums[i + 1]</code></li>
</ul>

<p>Return <code>true</code> <em>if the number of global inversions is equal to the number of local inversions</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,0,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is 1 global inversion and 1 local inversion.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are 2 global inversions and 1 local inversion.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == nums.length</code></li>
    <li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= nums[i] &lt; n</code></li>
    <li><code>nums</code> is a permutation of all the numbers in the range <code>[0, n - 1]</code>.</li>
</ul>"""

    input_format = "A single line containing the exact JSON array `nums`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= n <= 10^5",
        "0 <= nums[i] < n",
        "nums is a permutation of [0, n - 1]."
    ]

    explanation = """Every local inversion is a global inversion. Thus, for the number to be equal, there can be NO global inversions that aren't local inversions. This means we cannot find any i, j with j > i+1 such that nums[i] > nums[j]. We can check this condition effectively by maintaining a running maximum of elements seen up to index i-2. If this maximum is strictly greater than nums[i], then we return false. Otherwise, true."""

    answer = """class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        max_seen = -1
        for i in range(len(nums) - 2):
            max_seen = max(max_seen, nums[i])
            if max_seen > nums[i+2]:
                return False
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print("true" if sol.isIdealPermutation(nums) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        // User logic here
        return false;
    }
};

vector<int> parseArray(string s) {
    vector<int> res;
    int i = 1;
    while(i < s.length() - 1) {
        if(isdigit(s[i])) {
            int val = 0;
            while(isdigit(s[i])) val = val * 10 + (s[i++] - '0');
            res.push_back(val);
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string s;
    if (cin >> s) {
        vector<int> nums = parseArray(s);
        Solution sol;
        cout << (sol.isIdealPermutation(nums) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isIdealPermutation(int[] nums) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String raw = sc.next();
            raw = raw.substring(1, raw.length() - 1);
            if (raw.isEmpty()) {
                Solution sol = new Solution();
                System.out.println(sol.isIdealPermutation(new int[0]) ? "true" : "false");
                return;
            }
            String[] parts = raw.split(",");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.isIdealPermutation(nums) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isIdealPermutation = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(isIdealPermutation(JSON.parse(input)) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isIdealPermutation(int* nums, int numsSize) {
    // User logic here
    return false;
}

int main() {
    int cap = 100000;
    int* nums = (int*)malloc(cap * sizeof(int));
    int size = 0;
    char c;
    while ((c = getchar()) != EOF) {
        if (c == '[') continue;
        if (c == ']') break;
        if (c >= '0' && c <= '9') {
            ungetc(c, stdin);
            int val;
            scanf("%d", &val);
            nums[size++] = val;
        }
    }
    printf("%s\\n", isIdealPermutation(nums, size) ? "true" : "false");
    free(nums);
    return 0;
}"""
    }

    def solve(nums):
        max_seen = -1
        for i in range(len(nums) - 2):
            max_seen = max(max_seen, nums[i])
            if max_seen > nums[i+2]:
                return False
        return True

    import random
    test_cases_data = [
        [1,0,2],
        [1,2,0],
        [0,1,2,3,5,4],
        [0,1,2,4,3,6,5],
        [1,0,3,2,5,4],
        [2,1,0],
        list(range(500)),
        [0, 2, 1, 3] + list(range(4, 100)),
        [i^1 for i in range(100)],
        list(range(48)) + [49, 48]
    ]

    test_cases = []
    for i, nums in enumerate(test_cases_data):
        inp = json.dumps(nums).replace(" ", "")
        out = "true" if solve(nums) else "false"
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
        "topics": ["Array", "Math"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
