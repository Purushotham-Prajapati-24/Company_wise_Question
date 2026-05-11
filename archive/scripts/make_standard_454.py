import json
import os

def generate_json():
    problem_id = 454
    title = "4Sum II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>454. 4Sum II</h3>
<p>Given four integer arrays <code>nums1</code>, <code>nums2</code>, <code>nums3</code>, and <code>nums4</code> all of length <code>n</code>, return the number of tuples <code>(i, j, k, l)</code> such that:</p>

<ul>
	<li><code>0 &lt;= i, j, k, l &lt; n</code></li>
	<li><code>nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The two tuples are:
1. (0, 0, 0, 1) -&gt; nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -&gt; nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>n == nums3.length</code></li>
	<li><code>n == nums4.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>-2<sup>28</sup> &lt;= nums1[i], nums2[i], nums3[i], nums4[i] &lt;= 2<sup>28</sup></code></li>
</ul>"""

    input_format = "Four lines, each containing a JSON array of integers `nums1`, `nums2`, `nums3`, and `nums4` respectively."
    output_format = "An integer representing the number of tuples whose sum is 0."
    
    constraints = [
        "n == nums1.length == nums2.length == nums3.length == nums4.length",
        "1 <= n <= 200",
        "-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28"
    ]
    
    explanation = "Group the four arrays into two pairs. Calculate all possible sums for (nums1, nums2) and store their frequencies in a hash map. Then, calculate all possible sums for (nums3, nums4) and for each sum `s`, check if `-s` is present in the hash map. Add the frequency of `-s` to the total count."
    
    answer = """from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1
        
        count = 0
        for c in nums3:
            for d in nums4:
                count += sum_map[-(c + d)]
        return count"""

    boilerplate = {
        "python": r"""import sys
import json
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    lines = sys.stdin.read().strip().splitlines()
    if len(lines) >= 4:
        nums1 = json.loads(lines[0])
        nums2 = json.loads(lines[1])
        nums3 = json.loads(lines[2])
        nums4 = json.loads(lines[3])
        sol = Solution()
        print(sol.fourSumCount(nums1, nums2, nums3, nums4))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        // User Logic Here
        return 0;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    string current;
    for (char c : input) {
        if (isdigit(c) || c == '-') current += c;
        else if (!current.empty()) {
            res.push_back(stoi(current));
            current = "";
        }
    }
    if (!current.empty()) res.push_back(stoi(current));
    return res;
}

int main() {
    string line1, line2, line3, line4;
    if (getline(cin, line1) && getline(cin, line2) && getline(cin, line3) && getline(cin, line4)) {
        vector<int> nums1 = parseArray(line1);
        vector<int> nums2 = parseArray(line2);
        vector<int> nums3 = parseArray(line3);
        vector<int> nums4 = parseArray(line4);
        Solution sol;
        cout << sol.fourSumCount(nums1, nums2, nums3, nums4) << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            int[][] nums = new int[4][];
            for (int i = 0; i < 4; i++) {
                if (!sc.hasNextLine()) break;
                String line = sc.nextLine().trim();
                String[] parts = line.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
                if (parts.length == 0 || (parts.length == 1 && parts[0].isEmpty())) {
                    nums[i] = new int[0];
                } else {
                    nums[i] = new int[parts.length];
                    for (int j = 0; j < parts.length; j++) {
                        nums[i][j] = Integer.parseInt(parts[j]);
                    }
                }
            }
            Solution sol = new Solution();
            System.out.println(sol.fourSumCount(nums[0], nums[1], nums[2], nums[3]));
        }
    }
}""",
        "javascript": r"""/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
var fourSumCount = function(nums1, nums2, nums3, nums4) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');
if (input.length >= 4) {
    const nums1 = JSON.parse(input[0]);
    const nums2 = JSON.parse(input[1]);
    const nums3 = JSON.parse(input[2]);
    const nums4 = JSON.parse(input[3]);
    console.log(fourSumCount(nums1, nums2, nums3, nums4));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

int fourSumCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* nums4, int nums4Size) {
    // User Logic Here
    return 0;
}

int main() {
    // Manual parsing logic...
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,2]\\n[-2,-1]\\n[-1,2]\\n[0,2]", "expected_output": "2", "is_sample": True},
        {"input": "[0]\\n[0]\\n[0]\\n[0]", "expected_output": "1", "is_sample": True},
        {"input": "[1]\\n[1]\\n[1]\\n[1]", "expected_output": "0", "is_sample": True},
        {"input": "[1,-1]\\n[-1,1]\\n[1,-1]\\n[-1,1]", "expected_output": "6", "is_sample": False},
        {"input": "[1,2,3]\\n[4,5,6]\\n[-5,-6,-7]\\n[-1,-1,-2]", "expected_output": "9", "is_sample": False},
        {"input": "[ ]\\n[ ]\\n[ ]\\n[ ]", "expected_output": "0", "is_sample": False},
        {"input": "[-1,-1]\\n[-1,-1]\\n[1,1]\\n[1,1]", "expected_output": "16", "is_sample": False},
        {"input": "[0,0,0]\\n[0,0,0]\\n[0,0,0]\\n[0,0,0]", "expected_output": "81", "is_sample": False},
        # Stress
        {"input": json.dumps([0]*200) + "\\n" + json.dumps([0]*200) + "\\n" + json.dumps([0]*200) + "\\n" + json.dumps([0]*200), "expected_output": "1600000000", "is_sample": False},
        {"input": json.dumps([i for i in range(200)]) + "\\n" + json.dumps([-i for i in range(200)]) + "\\n" + json.dumps([i for i in range(200)]) + "\\n" + json.dumps([-i for i in range(200)]), "expected_output": "2133400", "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_4Sum_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
