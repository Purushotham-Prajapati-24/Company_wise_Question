import json
import os

def generate_json():
    problem_id = 503
    title = "Next Greater Element II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>503. Next Greater Element II</h3>
<p>Given a circular integer array <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return <em>the <strong>next greater number</strong> for every element in</em> <code>nums</code>.</p>

<p>The <strong>next greater number</strong> of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return <code>-1</code> for this number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [2,-1,2]
<strong>Explanation:</strong> The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,3]
<strong>Output:</strong> [2,3,4,-1,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
    <li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line: a JSON array of integers `nums`."
    output_format = "A JSON array of integers representing the next greater elements."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "-10^9 <= nums[i] <= 10^9"
    ]
    
    explanation = """Use a monotonic decreasing stack to find the next greater element. 
Since the array is circular, we can loop through the array twice (using indices from 0 to 2*n-1) and use the modulo operator to get the actual array elements. 
We push the element index into the stack and pop it whenever we find a strictly greater element, modifying the result array."""
    
    answer = """class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                pop_idx = stack.pop()
                res[pop_idx] = nums[idx]
            if i < n:
                stack.append(idx)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.nextGreaterElements(nums)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        // User logic here
        return {};
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
            } else {
                p++;
            }
        }
        
        Solution sol;
        vector<int> res = sol.nextGreaterElements(nums);
        cout << "[";
        for (size_t i = 0; i < res.size(); i++) {
            if (i > 0) cout << ",";
            cout << res[i];
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() > 1) {
                raw = raw.substring(1, raw.length() - 1);
            }
            List<Integer> list = new ArrayList<>();
            if (!raw.isEmpty()) {
                String[] parts = raw.split(",");
                for (String p : parts) {
                    list.add(Integer.parseInt(p.trim()));
                }
            }
            int[] nums = new int[list.size()];
            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);
            
            Solution sol = new Solution();
            int[] res = sol.nextGreaterElements(nums);
            
            System.out.print("[");
            for (int i = 0; i < res.length; i++) {
                if (i > 0) System.out.print(",");
                System.out.print(res[i]);
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(JSON.stringify(nextGreaterElements(nums)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElements(int* nums, int numsSize, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    char input[100000];
    if (fgets(input, sizeof(input), stdin)) {
        int capacity = 10;
        int* nums = (int*)malloc(capacity * sizeof(int));
        int size = 0;
        int i = 0;
        while (input[i] != '\\0') {
            if (input[i] == '-' || isdigit(input[i])) {
                int val;
                int offset = 0;
                sscanf(input + i, "%d%n", &val, &offset);
                if (offset == 0) {
                    i++;
                    continue;
                }
                if (size == capacity) {
                    capacity *= 2;
                    nums = (int*)realloc(nums, capacity * sizeof(int));
                }
                nums[size++] = val;
                i += offset;
            } else {
                i++;
            }
        }
        
        int returnSize = 0;
        int* res = nextGreaterElements(nums, size, &returnSize);
        printf("[");
        if (res != NULL) {
            for (int j = 0; j < returnSize; j++) {
                if (j > 0) printf(",");
                printf("%d", res[j]);
            }
            free(res);
        }
        printf("]\\n");
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[1,2,1]", "expected_output": "[2,-1,2]", "is_sample": True},
        {"input": "[1,2,3,4,3]", "expected_output": "[2,3,4,-1,4]", "is_sample": True},
        
        # Five Diverse Cases
        {"input": "[5,4,3,2,1]", "expected_output": "[-1,5,5,5,5]", "is_sample": False},
        {"input": "[1,1,1,1]", "expected_output": "[-1,-1,-1,-1]", "is_sample": False},
        {"input": "[1,5,3,6,8]", "expected_output": "[5,6,6,8,-1]", "is_sample": False},
        {"input": "[-1,0,-2,-3]", "expected_output": "[0,-1,0,0]", "is_sample": False},
        {"input": "[100]", "expected_output": "[-1]", "is_sample": False},
        
        # Three Stress Test Cases (strict JSON arrays without arbitrary spaces)
        {"input": "[1,2,3,2,1]", "expected_output": "[2,3,-1,3,2]", "is_sample": False},
        {"input": "[5,4,3,2,1,0,-1,-2]", "expected_output": "[-1,5,5,5,5,5,5,5]", "is_sample": False},
        {"input": "[-1000,-1000,-1000]", "expected_output": "[-1,-1,-1]", "is_sample": False}
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Stack", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
