import json
import os

def generate_json():
    problem_id = 416
    title = "Partition Equal Subset Sum"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>416. Partition Equal Subset Sum</h3>
<p>Given an integer array <code>nums</code>, return <code>true</code> <em>if you can partition the array into two subsets such that the sum of the elements in both subsets is equal, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,5,11,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned as [1, 5, 5] and [11].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array cannot be partitioned into equal sum subsets.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>"""

    input_format = "An integer array `nums`."
    output_format = "A boolean value."
    
    constraints = [
        "1 <= nums.length <= 200",
        "1 <= nums[i] <= 100"
    ]
    
    explanation = """To partition the array, we must find a subset with sum equal to total_sum / 2. This is the **Subset Sum Problem**."""
    
    answer = """class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = 1
        for n in nums:
            dp |= (dp << n)
        return bool(dp & (1 << target))"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # User Logic Here
        pass

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        nums = json.loads(raw_input)
        sol = Solution()
        print(json.dumps(sol.canPartition(nums)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // User Logic Here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        if (!line.empty() && line.front() == '[') line = line.substr(1, line.size() - 2);
        stringstream ss(line);
        string val;
        vector<int> nums;
        while (getline(ss, val, ',')) {
            nums.push_back(stoi(val));
        }
        Solution sol;
        cout << (sol.canPartition(nums) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean canPartition(int[] nums) {
        // User Logic Here
        return false;
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
            Solution sol = new Solution();
            System.out.println(sol.canPartition(nums));
        }
    }
}""",
        "javascript": """var canPartition = function(nums) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(canPartition(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool canPartition(int* nums, int numsSize) {
    // User Logic Here
    return false;
}

int main() {
    char line[10000];
    if (fgets(line, 10000, stdin)) {
        char *ptr = line;
        if (*ptr == '[') ptr++;
        int *nums = malloc(200 * sizeof(int));
        int size = 0;
        char *token = strtok(ptr, ",]");
        while (token) {
            nums[size++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%s\\n", canPartition(nums, size) ? "true" : "false");
        free(nums);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,5,11,5]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,3,5]", "expected_output": "false", "is_sample": True},
        {"input": "[1,1]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,5]", "expected_output": "false", "is_sample": False},
        {"input": "[100,100]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7]", "expected_output": "true", "is_sample": False},
        {"input": "[1,3,5]", "expected_output": "false", "is_sample": False},
        # 3 Stress
        {"input": json.dumps([100]*200), "expected_output": "true", "is_sample": False},
        {"input": json.dumps([99]*200), "expected_output": "true", "is_sample": False},
        {"input": json.dumps([1]*199 + [100]), "expected_output": "false", "is_sample": False}
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
        "topics": ["Array", "Dynamic Programming"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Partition_Equal_Subset_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
