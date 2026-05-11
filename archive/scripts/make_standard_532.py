import json
import os

def generate_json():
    problem_id = 532
    title = "K diff Pairs in an Array"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>532. K-diff Pairs in an Array</h3>
<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the number of <b>unique</b> k-diff pairs in the array</em>.</p>

<p>A <strong>k-diff</strong> pair is an integer pair <code>(nums[i], nums[j])</code>, where the following are true:</p>
<ul>
	<li><code>0 &lt;= i, j &lt; nums.length</code></li>
	<li><code>i != j</code></li>
	<li><code>|nums[i] - nums[j]| == k</code></li>
</ul>
<p><strong>Note</strong> that <code>|val|</code> denotes the absolute value of <code>val</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,1,4,1,5], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of <strong>unique</strong> pairs.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,5], k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,1,5,4], k = 0
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is one 0-diff pair in the array, (1, 1).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>"""

    input_format = "Two lines: Line 1: A JSON array of integers `nums`. Line 2: An integer `k`."
    output_format = "An integer representing the number of unique pairs."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "-10^7 <= nums[i] <= 10^7",
        "0 <= k <= 10^7"
    ]
    
    explanation = """To find unique pairs efficiently, we can count the frequency of each number using a hash map. If k > 0, we check if num + k exists in the map for each unique num. If k == 0, we check if any num has a frequency greater than 1."""
    
    answer = """from collections import Counter
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)
        pairs = 0
        if k > 0:
            for num in counts:
                if num + k in counts:
                    pairs += 1
        elif k == 0:
            for num in counts:
                if counts[num] > 1:
                    pairs += 1
        return pairs"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums = json.loads(raw[0])
        k = int(raw[1].strip())
        sol = Solution()
        print(sol.findPairs(nums, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    string n_str, k_str;
    if (getline(cin, n_str) && getline(cin, k_str)) {
        vector<int> nums;
        size_t p = 0;
        while (p < n_str.length()) {
            if (n_str[p] == '-' || isdigit(n_str[p])) {
                size_t next;
                nums.push_back(stoi(n_str.substr(p), &next));
                p += next;
            } else {
                p++;
            }
        }
        int k = stoi(k_str);
        Solution sol;
        cout << sol.findPairs(nums, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int findPairs(int[] nums, int k) {
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
            
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.findPairs(nums, k));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(findPairs(nums, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int findPairs(int* nums, int numsSize, int k) {
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
        while (input[i] != '\\0' && input[i] != '\\n') {
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
        
        int k;
        if (scanf("%d", &k) == 1) {
            printf("%d\\n", findPairs(nums, size, k));
        }
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": "[3,1,4,1,5]\\n2", "expected_output": "2", "is_sample": True},
        {"input": "[1,2,3,4,5]\\n1", "expected_output": "4", "is_sample": True},
        
        # Five Diverse Cases
        {"input": "[1,3,1,5,4]\\n0", "expected_output": "1", "is_sample": False},
        {"input": "[1,1,1,1,1]\\n0", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3,4,5]\\n10", "expected_output": "0", "is_sample": False},
        {"input": "[0,0,0,0]\\n0", "expected_output": "1", "is_sample": False},
        {"input": "[-1,-2,-3]\\n1", "expected_output": "2", "is_sample": False},
        
        # Three Stress Test Cases (strict JSON format limits bounds)
        {"input": "[" + ",".join(["1"] * 5000 + ["2"] * 5000) + "]\\n1", "expected_output": "1", "is_sample": False},
        {"input": "[" + ",".join([str(x) for x in range(10000)]) + "]\\n9999", "expected_output": "1", "is_sample": False},
        {"input": "[" + ",".join(["1"] * 10000) + "]\\n0", "expected_output": "1", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Two Pointers", "Binary Search", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
