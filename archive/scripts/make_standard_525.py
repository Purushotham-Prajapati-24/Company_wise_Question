import json
import os

def generate_json():
    problem_id = 525
    title = "Contiguous Array"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>525. Contiguous Array</h3>
<p>Given a binary array <code>nums</code>, return <em>the maximum length of a contiguous subarray with an equal number of </em><code>0</code><em> and </em><code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>"""

    input_format = "A single line: a JSON array of integers `nums`."
    output_format = "An integer representing the maximum length."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "nums[i] is either 0 or 1"
    ]
    
    explanation = """We can use a hash map to keep track of the running sum. We substitute 0 with -1, and add the value to the running sum. If the sum is already in the hash map, it means the subarray between the previous index and the current index has an equal number of 0s and 1s."""
    
    answer = """class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0
        max_len = 0
        hash_map = {0: -1}
        for i, val in enumerate(nums):
            count += 1 if val == 1 else -1
            if count in hash_map:
                max_len = max(max_len, i - hash_map[count])
            else:
                hash_map[count] = i
        return max_len"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(sol.findMaxLength(nums))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
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
            } else {
                p++;
            }
        }
        Solution sol;
        cout << sol.findMaxLength(nums) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int findMaxLength(int[] nums) {
        // User logic here
        return 0;
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
            System.out.println(sol.findMaxLength(nums));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(findMaxLength(nums));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int findMaxLength(int* nums, int numsSize) {
    // User logic here
    return 0;
}

int main() {
    char input[500000];
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
        
        printf("%d\\n", findMaxLength(nums, size));
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[0,1]", "expected_output": "2", "is_sample": True},
        {"input": "[0,1,0]", "expected_output": "2", "is_sample": True},
        
        # Five Diverse Cases
        {"input": "[0,0,0,1,1,1]", "expected_output": "6", "is_sample": False},
        {"input": "[1,1,1,1]", "expected_output": "0", "is_sample": False},
        {"input": "[0,0,0]", "expected_output": "0", "is_sample": False},
        {"input": "[1,0,1,0,1,1,1,1,0,0]", "expected_output": "6", "is_sample": False},
        {"input": "[1]", "expected_output": "0", "is_sample": False},
        
        # Three Stress Test Cases (strict JSON format)
        {"input": "[" + ",".join(["1", "0"] * 25000) + "]", "expected_output": "50000", "is_sample": False},
        {"input": "[" + ",".join(["0"] * 50000) + "]", "expected_output": "0", "is_sample": False},
        {"input": "[" + ",".join(["1"] * 25000 + ["0"] * 25000) + "]", "expected_output": "50000", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Prefix Sum"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
