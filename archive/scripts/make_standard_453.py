import json
import os

def generate_json():
    problem_id = 453
    title = "Minimum Moves to Equal Array Elements"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>453. Minimum Moves to Equal Array Elements</h3>
<p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can <strong>increment</strong> <code>n - 1</code> elements of the array by <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Only three moves are needed (remember each move increments two elements):
[1,2,3]  =&gt;  [2,3,3]  =&gt;  [3,4,3]  =&gt;  [4,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The answer is guaranteed to fit in a <strong>32-bit</strong> integer.</li>
</ul>"""

    input_format = "A JSON array of integers `nums`."
    output_format = "An integer representing the minimum number of moves."
    
    constraints = [
        "n == nums.length",
        "1 <= nums.length <= 10^5",
        "-10^9 <= nums[i] <= 10^9",
        "The answer is guaranteed to fit in a 32-bit integer."
    ]
    
    explanation = "Incrementing n-1 elements by 1 is mathematically equivalent to decrementing 1 element by 1 in terms of the relative differences between elements. To make all elements equal to the minimum value, we need to sum up the differences between each element and the minimum element: sum(nums[i] - min(nums))."
    
    answer = """class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if not nums: return 0
        min_val = min(nums)
        return sum(x - min_val for x in nums)"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        try:
            nums = json.loads(raw_input)
            sol = Solution()
            print(sol.minMoves(nums))
        except:
            print(0)
    else:
        print(0)""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<int> nums;
        string current;
        for (char c : input) {
            if (isdigit(c) || c == '-') current += c;
            else if (!current.empty()) {
                nums.push_back(stoi(current));
                current = "";
            }
        }
        if (!current.empty()) nums.push_back(stoi(current));
        Solution sol;
        cout << sol.minMoves(nums) << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int minMoves(int[] nums) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            String[] parts = input.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
            if (parts.length == 0 || (parts.length == 1 && parts[0].isEmpty())) {
                System.out.println(0);
                return;
            }
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) {
                nums[i] = Integer.parseInt(parts[i]);
            }
            Solution sol = new Solution();
            System.out.println(sol.minMoves(nums));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    try {
        const nums = JSON.parse(input);
        console.log(minMoves(nums));
    } catch (e) {
        console.log(0);
    }
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

int minMoves(int* nums, int numsSize) {
    // User Logic Here
    return 0;
}

int main() {
    // Manual parsing logic...
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,2,3]", "expected_output": "3", "is_sample": True},
        {"input": "[1,1,1]", "expected_output": "0", "is_sample": True},
        {"input": "[1,10,100]", "expected_output": "108", "is_sample": False},
        {"input": "[-100, 0, 100]", "expected_output": "300", "is_sample": False},
        {"input": "[  1, 2, 3  ]", "expected_output": "3", "is_sample": False}, # Spaces
        {"input": "[1,2,1,2,1]", "expected_output": "2", "is_sample": False},
        {"input": "[-1,-1,-1,-1]", "expected_output": "0", "is_sample": False},
        {"input": "[0, 0, 0]", "expected_output": "0", "is_sample": False},
        # Stress
        {"input": json.dumps([1] * 1000 + [1000]), "expected_output": "999", "is_sample": False},
        {"input": json.dumps(list(range(100))), "expected_output": "4950", "is_sample": False}
    ]

    data = {
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
        "topics": ["Array", "Math"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Minimum_Moves_to_Equal_Array_Elements.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
