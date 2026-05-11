import json
import os

def generate_json():
    problem_id = 259
    title = "3Sum Smaller"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>259. 3Sum Smaller</h3>
<p>Given an array of <code>n</code> integers <code>nums</code> and an integer <code>target</code>, find the number of index triplets <code>(i, j, k)</code> with <code>0 &lt;= i &lt; j &lt; k &lt; n</code> that satisfy the condition <code>nums[i] + nums[j] + nums[k] &lt; target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [-2,0,1,3], target = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [0], target = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>0 &lt;= n &lt;= 3500</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>-100 &lt;= target &lt;= 100</code></li>
</ul>"""

    input_format = "Three lines (or space-separated input): First, the number of elements N. Second, N integers representing the array nums. Third, the target integer."
    output_format = "An integer count of valid triplets."
    
    constraints = [
        "0 <= n <= 3500",
        "-100 <= nums[i] <= 100",
        "O(N^2) solution required."
    ]
    
    explanation = """To count triplets summing to less than target efficiently:
1. **Sorting**: Sort the input array `nums`.
2. **Two Pointers**: Iterate `i` from `0` to `n-3`:
   - Use two pointers, `left = i + 1` and `right = n - 1`.
   - While `left < right`:
     - Calculate `curr_sum = nums[i] + nums[left] + nums[right]`.
     - If `curr_sum < target`:
       - This means all triplets starting with `nums[i]` and `nums[left]` ending with any number from `nums[left+1]` to `nums[right]` are also valid (since the array is sorted).
       - Add `right - left` to the total count.
       - Increment `left`.
     - Otherwise, the sum is too large; decrement `right`.
3. **Complexity**:
   - Time: O(N^2).
   - Space: O(1) or O(N) depending on sorting implementation."""
    
    answer = """class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
                    
        return count"""

    boilerplate = {
        "python": "import sys\n\ndef threeSumSmaller(nums: list[int], target: int) -> int:\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if not data: sys.exit()\n    n = int(data[0])\n    nums = [int(x) for x in data[1:n+1]]\n    target = int(data[n+1])\n    print(threeSumSmaller(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint threeSumSmaller(vector<int>& nums, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        vector<int> nums(n);\n        for (int i = 0; i < n; i++) cin >> nums[i];\n        int target;\n        cin >> target;\n        cout << threeSumSmaller(nums, target) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int threeSumSmaller(int[] nums, int target) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            int[] nums = new int[n];\n            for (int i = 0; i < n; i++) {\n                nums[i] = sc.nextInt();\n            }\n            int target = sc.nextInt();\n            System.out.println(new Solution().threeSumSmaller(nums, target));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction threeSumSmaller(nums, target) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    let n = parseInt(input[0]);\n    let nums = [];\n    for (let i = 0; i < n; i++) nums.push(parseInt(input[1 + i]));\n    let target = parseInt(input[1 + n]);\n    console.log(threeSumSmaller(nums, target));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint threeSumSmaller(int* nums, int numsSize, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int* nums = (int*)malloc((n > 0 ? n : 1) * sizeof(int));\n        for (int i = 0; i < n; i++) scanf(\"%d\", &nums[i]);\n        int target;\n        scanf(\"%d\", &target);\n        printf(\"%d\\n\", threeSumSmaller(nums, n, target));\n        free(nums);\n    }\n    return 0;\n}"
    }

    def _solve_3ss(nums, target):
        nums_sorted = sorted(nums)
        count = 0
        n = len(nums_sorted)
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                if nums_sorted[i] + nums_sorted[l] + nums_sorted[r] < target:
                    count += (r - l); l += 1
                else: r -= 1
        return count

    def create_tc(nums, target):
        res = f"{len(nums)}"
        if nums:
            res += "\\n" + " ".join(map(str, nums))
        res += f"\\n{target}"
        return res

    test_cases = [
        {"input": create_tc([-2,0,1,3], 2), "expected_output": "2", "is_sample": True},
        {"input": create_tc([], 0), "expected_output": "0", "is_sample": True},
        {"input": create_tc([0], 0), "expected_output": "0", "is_sample": True},
        {"input": create_tc([1,2,3,4,5,6], 10), "expected_output": str(_solve_3ss([1,2,3,4,5,6], 10)), "is_sample": False},
        {"input": create_tc([1,1,1,1], 4), "expected_output": str(_solve_3ss([1,1,1,1], 4)), "is_sample": False},
        {"input": create_tc([-1,1,-1,1], 1), "expected_output": str(_solve_3ss([-1,1,-1,1], 1)), "is_sample": False},
        {"input": create_tc([1,2,3], 7), "expected_output": str(_solve_3ss([1,2,3], 7)), "is_sample": False},
    ]

    # Stress 8: 3500 elements all -100
    n8 = [-100] * 3500
    test_cases.append({"input": create_tc(n8, 300), "expected_output": str(_solve_3ss(n8, 300)), "is_sample": False})
    # Stress 9: 3500 elements sorted 1 to 3500
    n9 = list(range(3500))
    test_cases.append({"input": create_tc(n9, 100), "expected_output": str(_solve_3ss(n9, 100)), "is_sample": False})
    # Stress 10: Alternating vals
    n10 = [100 if i % 2 else -100 for i in range(3500)]
    test_cases.append({"input": create_tc(n10, 0), "expected_output": str(_solve_3ss(n10, 0)), "is_sample": False})

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
            "time_limit_ms": 2000,
            "memory_limit_mb": 512,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Two Pointers", "Sorting", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "201-400/259_3Sum_Smaller.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
