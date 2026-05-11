import json
import os

def generate_json():
    problem_id = 325
    title = "Maximum Size Subarray Sum Equals k"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>325. Maximum Size Subarray Sum Equals k</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the maximum length of a subarray that sums to <code>k</code></em>. If there is none, return <code>0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,-1,5,-2,3], k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The subarray [1,-1,5,-2] sums to 3 and its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-2,-1,2,1], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [-1,2] sums to 1 and its length is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: an array of integers `nums`. Line 2: an integer `k`."
    output_format = "An integer representing the maximum subarray length or 0."
    
    constraints = [
        "1 <= nums.length <= 200,000",
        "-10^4 <= nums[i] <= 10^4",
        "-10^9 <= k <= 10^9"
    ]
    
    explanation = """To find the maximum length of a subarray with sum $k$, we use the **Prefix Sum** technique combined with a **Hash Map**.

### Key Concept:
A subarray summing to $k$ from index $j$ to $i$ (inclusive) can be expressed in terms of prefix sums:
$PrefixSum[i] - PrefixSum[j-1] = k$
This rearranges to:
$PrefixSum[j-1] = PrefixSum[i] - k$

### Algorithm Steps:
1. **Initialize**: 
   - A variable `current_sum = 0` to track the running prefix sum.
   - A variable `max_len = 0` for the result.
   - A hash map `seen` to store the *earliest* index encountered for each prefix sum. Map `{0: -1}` initially to handle subarrays starting from index 0.
2. **Iterate**:
   - For each index `i` and element `val` in `nums`:
     - Update `current_sum += val`.
     - Check if `current_sum - k` exists in the `seen` map.
     - If it exists at index `j`, a subarray with sum $k$ exists from index $j+1$ to $i$, with length `i - j`. Update `max_len = max(max_len, i - j)`.
     - Only add `current_sum` to the map if it's not already there (ensuring we keep the *first* occurrence to maximize the subarray length).

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the number of elements in the array. We traverse the array once and hash map lookups are $O(1)$ on average.
- **Space Complexity**: $O(N)$ for the hash map storing prefix sums."""
    
    answer = """class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        current_sum = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # If currentSum - k was seen before at index j:
            # sum(nums[j+1...i]) = currentSum - prefixSums[j] = k
            if current_sum - k in seen:
                max_len = max(max_len, i - seen[current_sum - k])
            
            # Store first occurrence to maximize the distance (maximize i-j)
            if current_sum not in seen:
                seen[current_sum] = i
        
        return max_len"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def maxSubArrayLen(self, nums: list[int], k: int) -> int:\n        # Your code here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        lines = raw_input.split('\\n')\n        if len(lines) >= 2:\n            nums = json.loads(lines[0])\n            k = json.loads(lines[1])\n            sol = Solution()\n            print(json.dumps(sol.maxSubArrayLen(nums, k)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <sstream>\nusing namespace std;\n\nclass Solution {\npublic:\n    int maxSubArrayLen(vector<int>& nums, int k) {\n        // Your code here\n        return 0;\n    }\n};\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1) && getline(cin, line2)) {\n        vector<int> nums;\n        if (line1.length() >= 2) {\n            line1 = line1.substr(1, line1.length() - 2);\n            if (!line1.empty()) {\n                stringstream ss(line1);\n                string item;\n                while (getline(ss, item, ',')) {\n                    nums.push_back(stoi(item));\n                }\n            }\n        }\n        int k = stoi(line2);\n        Solution sol;\n        cout << sol.maxSubArrayLen(nums, k) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int maxSubArrayLen(int[] nums, int k) {\n        // Your code here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            String line1 = scanner.nextLine().trim();\n            String line2 = scanner.nextLine().trim();\n            if (line1.length() >= 2) {\n                line1 = line1.substring(1, line1.length() - 1);\n            }\n            int[] nums;\n            if (line1.isEmpty()) {\n                nums = new int[0];\n            } else {\n                String[] parts = line1.split(\",\");\n                nums = new int[parts.length];\n                for (int i = 0; i < parts.length; i++) {\n                    nums[i] = Integer.parseInt(parts[i].trim());\n                }\n            }\n            int k = Integer.parseInt(line2);\n            Solution sol = new Solution();\n            System.out.println(sol.maxSubArrayLen(nums, k));\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @param {number} k\n * @return {number}\n */\nvar maxSubArrayLen = function(nums, k) {\n    // Your code here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const nums = JSON.parse(input[0]);\n    const k = JSON.parse(input[1]);\n    console.log(JSON.stringify(maxSubArrayLen(nums, k)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint maxSubArrayLen(int* nums, int numsSize, int k) {\n    // Your code here\n    return 0;\n}\n\nint main() {\n    char line1[2000000];\n    char line2[100];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        line1[strcspn(line1, \"\\r\\n\")] = 0;\n        line2[strcspn(line2, \"\\r\\n\")] = 0;\n        int capacity = 100;\n        int* nums = malloc(capacity * sizeof(int));\n        int size = 0;\n        char* ptr = line1;\n        while (*ptr && *ptr != '[') ptr++;\n        if (*ptr == '[') ptr++;\n        while (*ptr && *ptr != ']') {\n            int val;\n            int charsRead;\n            if (sscanf(ptr, \"%d%n\", &val, &charsRead) == 1) {\n                if (size >= capacity) {\n                    capacity *= 2;\n                    nums = realloc(nums, capacity * sizeof(int));\n                }\n                nums[size++] = val;\n                ptr += charsRead;\n            } else {\n                ptr++;\n            }\n        }\n        int k = atoi(line2);\n        printf(\"%d\\n\", maxSubArrayLen(nums, size, k));\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,-1,5,-2,3]\\n3", "expected_output": "4", "is_sample": True},
        {"input": "[-2,-1,2,1]\\n1", "expected_output": "2", "is_sample": True},
        {"input": "[1,2,3]\\n10", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3,4,1]\\n5", "expected_output": "2", "is_sample": False},
        {"input": "[-1,-1,1]\\n0", "expected_output": "2", "is_sample": False},
        {"input": "[0,0,0]\\n0", "expected_output": "3", "is_sample": False},
        {"input": "[1,1,1]\\n2", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": json.dumps([1]*50000) + "\\n50000", "expected_output": "50000", "is_sample": False},
        {"input": json.dumps([1, -1]*25000) + "\\n0", "expected_output": "50000", "is_sample": False},
        {"input": json.dumps([i for i in range(5000)]) + "\\n100", "expected_output": "5", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Prefix Sum"],
        "companyIndex": 1
    }

    output_path = "301-500/325_Maximum_Size_Subarray_Sum_Equals_k.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
