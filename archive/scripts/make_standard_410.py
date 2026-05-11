import json
import os

def generate_json():
    problem_id = 410
    title = "Split Array Largest Sum"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>410. Split Array Largest Sum</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, split <code>nums</code> into <code>k</code> non-empty continuous subarrays such that the largest sum of any subarray is <strong>minimized</strong>.</p>

<p>Return <em>the minimized largest sum of the split.</em></p>

<p>A <strong>subarray</strong> is a contiguous part of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [7,2,5,10,8], k = 2
<strong>Output:</strong> 18
<strong>Explanation:</strong> There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,5], k = 2
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are four ways to split nums into two subarrays.
The best way is to split it into [1,2] and [3,4,5], where the largest sum among the two subarrays is only 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(50, nums.length)</code></li>
</ul>"""

    input_format = "An array of integers `nums` and an integer `k`."
    output_format = "The minimized largest sum."
    
    constraints = [
        "1 <= nums.length <= 1000",
        "0 <= nums[i] <= 10^6",
        "1 <= k <= min(50, nums.length)"
    ]
    
    explanation = """Use **Binary Search on the Answer**. The range of the answer is `[max(nums), sum(nums)]`. For a chosen sum `X`, check if it's possible to split the array into `k` or fewer subarrays such that each subarray sum is at most `X`."""
    
    answer = """class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = num
                    if count > k: return False
                else:
                    curr_sum += num
            return True
            
        low, high = max(nums), sum(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        nums = json.loads(lines[0].strip())
        k = int(lines[1].strip())
        sol = Solution()
        print(json.dumps(sol.splitArray(nums, k)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string line;
    int k;
    if (getline(cin, line)) {
        if (!line.empty() && line.front() == '[') line = line.substr(1, line.size() - 2);
        stringstream ss(line);
        string val;
        vector<int> nums;
        while (getline(ss, val, ',')) {
            nums.push_back(stoi(val));
        }
        if (cin >> k) {
            Solution sol;
            cout << sol.splitArray(nums, k) << endl;
        }
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int splitArray(int[] nums, int k) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.startsWith("[")) line = line.substring(1, line.length() - 1);
            String[] parts = line.split(",");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.splitArray(nums, k));
            }
        }
    }
}""",
        "javascript": """var splitArray = function(nums, k) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0].trim());
    const k = parseInt(input[1].trim());
    console.log(JSON.stringify(splitArray(nums, k)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int splitArray(int* nums, int numsSize, int k) {
    // User Logic Here
    return 0;
}

int main() {
    char line[10000];
    int k;
    if (fgets(line, 10000, stdin)) {
        char *ptr = line;
        if (*ptr == '[') ptr++;
        int *nums = malloc(1000 * sizeof(int));
        int size = 0;
        char *token = strtok(ptr, ",]");
        while (token) {
            nums[size++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        if (scanf("%d", &k) == 1) {
            printf("%d\\n", splitArray(nums, size, k));
        }
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[7,2,5,10,8]\n2", "expected_output": "18", "is_sample": True},
        {"input": "[1,2,3,4,5]\n2", "expected_output": "9", "is_sample": True},
        # 5 Diverse
        {"input": "[1,4,4]\n3", "expected_output": "4", "is_sample": False},
        {"input": "[1,2,3]\n1", "expected_output": "6", "is_sample": False},
        {"input": "[10,5,10,10,5]\n2", "expected_output": "25", "is_sample": False},
        {"input": "[1,1,1,1,1,1]\n3", "expected_output": "2", "is_sample": False},
        {"input": "[5,10,15,20]\n2", "expected_output": "30", "is_sample": False},
        # 3 Stress
        {"input": "[0]*1000\n50", "expected_output": "0", "is_sample": False},
        {"input": "[1000000]*1000\n1", "expected_output": "1000000000", "is_sample": False},
        {"input": "[i for i in range(1, 1001)]\n10", "expected_output": "50505", "is_sample": False}
    ]

    # Convert stress test cases to actual JSON for input compatibility
    test_cases[7]["input"] = json.dumps([0]*1000) + "\n50"
    test_cases[8]["input"] = json.dumps([1000000]*1000) + "\n1"
    test_cases[9]["input"] = json.dumps([i for i in range(1, 1001)]) + "\n10"

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
        "topics": ["Array", "Binary Search", "Dynamic Programming", "Greedy"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Split_Array_Largest_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
