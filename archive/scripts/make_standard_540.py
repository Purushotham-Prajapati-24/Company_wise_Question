import json
import os

def generate_json():
    problem_id = 540
    title = "Single Element in a Sorted Array"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>540. Single Element in a Sorted Array</h3>
<p>You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.</p>

<p>Return <em>the single element that appears only once</em>.</p>

<p>Your solution must run in <code>O(log n)</code> time and <code>O(1)</code> space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,2,3,3,4,4,8,8]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,3,7,7,10,11,11]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A single line: a JSON array of integers `nums`."
    output_format = "An integer: the single element."

    constraints = [
        "1 <= nums.length <= 10^5",
        "0 <= nums[i] <= 10^5"
    ]

    explanation = """Use binary search. At any mid index: if mid is even and nums[mid] == nums[mid+1], the single element is to the right. If mid is odd and nums[mid] == nums[mid-1], single element is to the right. Otherwise it is to the left. This gives O(log n) time."""

    answer = """class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.singleNonDuplicate(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
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
            if (isdigit(input[p])) {
                size_t next;
                nums.push_back(stoi(input.substr(p), &next));
                p += next;
            } else { p++; }
        }
        Solution sol;
        cout << sol.singleNonDuplicate(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int singleNonDuplicate(int[] nums) {
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
                for (String p : raw.split(",")) list.add(Integer.parseInt(p.trim()));
            }
            int[] nums = new int[list.size()];
            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
            Solution sol = new Solution();
            System.out.println(sol.singleNonDuplicate(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(singleNonDuplicate(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int singleNonDuplicate(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int main() {
    char input[500000];
    if (fgets(input, sizeof(input), stdin)) {
        int cap = 10, size = 0, i = 0;
        int* nums = (int*)malloc(cap * sizeof(int));
        while (input[i]) {
            if (isdigit(input[i])) {
                int val, off = 0;
                sscanf(input + i, "%d%n", &val, &off);
                if (!off) { i++; continue; }
                if (size == cap) { cap *= 2; nums = realloc(nums, cap * sizeof(int)); }
                nums[size++] = val;
                i += off;
            } else i++;
        }
        printf("%d\\n", singleNonDuplicate(nums, size));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[1,1,2,3,3,4,4,8,8]", "expected_output": "2", "is_sample": True},
        {"input": "[3,3,7,7,10,11,11]", "expected_output": "10", "is_sample": True},

        # Five Diverse Cases
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,1,2]", "expected_output": "2", "is_sample": False},
        {"input": "[0,1,1]", "expected_output": "0", "is_sample": False},
        {"input": "[1,1,2,2,3,3,4,4,5]", "expected_output": "5", "is_sample": False},
        {"input": "[1,2,2,3,3]", "expected_output": "1", "is_sample": False},

        # Three Stress Test Cases
        {"input": "[" + ",".join([f"{i},{i}" for i in range(49999)]).replace(",", ",", -1) + ",49999]", "expected_output": "49999", "is_sample": False},
        {"input": "[0," + ",".join([f"{i},{i}" for i in range(1, 50000)]) + "]", "expected_output": "0", "is_sample": False},
        {"input": "[" + ",".join([f"{i},{i}" for i in range(24999)]) + ",24999," + ",".join([f"{i},{i}" for i in range(25000, 50000)]) + "]", "expected_output": "24999", "is_sample": False}
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
