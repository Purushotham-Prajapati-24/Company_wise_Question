import json
import os

def generate_json():
    problem_id = 15
    title = "3Sum"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>15. 3Sum</h3>
<p>Given an integer array <code>nums</code>, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
"""

    input_format = "A single line containing space-separated integers representing 'nums'."
    output_format = "A string representing a list of unique triplets."
    
    constraints = [
        "3 <= nums.length <= 3000",
        "-10^5 <= nums[i] <= 10^5"
    ]
    
    explanation = """To find unique triplets that sum to zero in O(N^2) time:
1. Sort the input array `nums`. This allows us to use the two-pointer approach and easily skip duplicate elements.
2. Iterate through `nums` using a fixed pointer `i` up to `len(nums) - 2`:
   - If `nums[i] > 0`, break because any triple including it will sum to more than 0.
   - If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicates.
3. Initialize two pointers: `left = i + 1` and `right = len(nums) - 1`.
4. While `left < right`:
   - Calculate `sum = nums[i] + nums[left] + nums[right]`.
   - If `sum == 0`:
     - Add `[nums[i], nums[left], nums[right]]` to the result.
     - While `left < right` and `nums[left] == nums[left+1]`, increment `left`.
     - While `left < right` and `nums[right] == nums[right-1]`, decrement `right`.
     - Move both pointers inwards after processing.
   - Else if `sum < 0`, increment `left`.
   - Else `sum > 0`, decrement `right`.
5. Return the list of distinct triplets.

This method achieves O(N^2) time and O(log N) or O(N) space depending on the sorting implementation."""
    
    answer = """def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        if nums[i] > 0: break
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1
                r -= 1
    return res"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport json\n\ndef threeSum(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip().split()\n    if data:\n        nums = [int(x.strip('[],')) for x in data if x.strip('[],')]\n        res = threeSum(nums)\n        print(json.dumps(res).replace(',', ', '))\n    else:\n        print(\"[]\")",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<vector<int>> threeSum(vector<int>& nums) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int val;\n    vector<int> nums;\n    while (cin >> val) {\n        nums.push_back(val);\n    }\n    vector<vector<int>> res = threeSum(nums);\n    cout << \"[\";\n    for (size_t i = 0; i < res.size(); i++) {\n        cout << \"[\";\n        for (size_t j = 0; j < res[i].size(); j++) {\n            cout << res[i][j];\n            if (j < res[i].size() - 1) cout << \", \";\n        }\n        cout << \"]\";\n        if (i < res.size() - 1) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<Integer>> threeSum(int[] nums) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) {\n            list.add(sc.nextInt());\n        }\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) {\n            nums[i] = list.get(i);\n        }\n        List<List<Integer>> res = threeSum(nums);\n        System.out.println(res);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction threeSum(nums) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    const nums = input.map(Number);\n    const res = threeSum(nums);\n    console.log(JSON.stringify(res).replace(/,/g, \", \"));\n} else {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int capacity = 10005;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int size = 0;\n    while (scanf(\"%d\", &nums[size]) == 1) {\n        size++;\n    }\n    int returnSize;\n    int* returnColumnSizes;\n    int** res = threeSum(nums, size, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[\");\n        for (int j = 0; j < returnColumnSizes[i]; j++) {\n            printf(\"%d\", res[i][j]);\n            if (j < returnColumnSizes[i] - 1) printf(\", \");\n        }\n        printf(\"]\");\n        if (i < returnSize - 1) printf(\", \");\n    }\n    printf(\"]\\n\");\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "-1 0 1 2 -1 -4", "expected_output": "[[-1, -1, 2], [-1, 0, 1]]", "is_sample": True},
        {"input": "0 1 1", "expected_output": "[]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "0 0 0", "expected_output": "[[0, 0, 0]]", "is_sample": False},
        {"input": "-2 0 1 1 2", "expected_output": "[[-2, 0, 2], [-2, 1, 1]]", "is_sample": False},
        {"input": "-5 1 1 2 3 4", "expected_output": "[[-5, 1, 4], [-5, 2, 3]]", "is_sample": False},
        {"input": "10 -10 0", "expected_output": "[[-10, 0, 10]]", "is_sample": False},
        {"input": "-1 -1 -1 2 2", "expected_output": "[[-1, -1, 2]]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["0"] * 3000), "expected_output": "[[0, 0, 0]]", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-1500, 1500)]), "expected_output": str(threeSum([i for i in range(-1500, 1500)]) if 'threeSum' in locals() else ""), "is_sample": False},
        {"input": " ".join(["-1", "1", "0"] * 1000), "expected_output": "[[-1, 0, 1]]", "is_sample": False}
    ]
    # Update stress 2 for correct expected output
    def _3sum_ref(nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1; r -= 1
        return res

    test_cases[8]["expected_output"] = str(_3sum_ref([i for i in range(-1500, 1500)]))

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
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/15_3Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
