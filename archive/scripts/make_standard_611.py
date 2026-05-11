import json
import os

def generate_json():
    problem_id = 611
    title = "Valid Triangle Number"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>611. Valid Triangle Number</h3>
<p>Given an integer array <code>nums</code>, return <em>the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,2,3,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 1000</code></li>
    <li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing a JSON array of integers `nums`."
    output_format = "An integer representing the number of valid triangle triplets."

    constraints = [
        "1 <= nums.length <= 1000",
        "0 <= nums[i] <= 1000"
    ]

    explanation = """To form a valid triangle, the sum of any two sides must be greater than the third side. If we sort the lengths, we only need to check if a + b > c where c is the largest side. So, we can sort the array first. Then, iterate c from the end of the array. For each c, use a two-pointer approach (left and right) to find all pairs (a, b) such that a + b > c."""

    answer = """class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.triangleNumber(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 1;
    while (i < input.length() && input[i] != ']') {
        if (isdigit(input[i])) {
            int val = 0;
            while (isdigit(input[i])) {
                val = val * 10 + (input[i] - '0');
                i++;
            }
            res.push_back(val);
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string str;
    if (getline(cin, str)) {
        vector<int> nums = parseArray(str);
        Solution sol;
        cout << sol.triangleNumber(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int triangleNumber(int[] nums) {
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
            System.out.println(sol.triangleNumber(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(triangleNumber(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int triangleNumber(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
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
    char str[500000];
    if (fgets(str, sizeof(str), stdin)) {
        int numsSize;
        int* nums = parseArray(str, &numsSize);
        printf("%d\\n", triangleNumber(nums, numsSize));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[2,2,3,4]", "expected_output": "3", "is_sample": True},
        {"input": "[4,2,3,4]", "expected_output": "4", "is_sample": True},
        {"input": "[0,1,0]", "expected_output": "0", "is_sample": False},
        {"input": "[1,1,1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "0", "is_sample": False},
        {"input": "[10,21,22,100]", "expected_output": "1", "is_sample": False},
        {"input": "[2,2,2,2]", "expected_output": "4", "is_sample": False},
        {"input": "[" + ",".join("1" for _ in range(1000)) + "]", "expected_output": "166167000", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(1000)) + "]", "expected_output": "166167000", "is_sample": False},
        {"input": "[" + ",".join(str(10**i % 1000) for i in range(1000)) + "]", "expected_output": "164670", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Binary Search", "Greedy", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
