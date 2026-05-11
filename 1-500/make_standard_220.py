import json
import os

def generate_json():
    problem_id = 220
    title = "Contains Duplicate III"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>220. Contains Duplicate III</h3>
<p>You are given an integer array <code>nums</code> and two integers <code>indexDiff</code> and <code>valueDiff</code>.</p>

<p>Find a pair of indices <code>(i, j)</code> such that:</p>

<ul>
	<li><code>i != j</code>,</li>
	<li><code>abs(i - j) &lt;= indexDiff</code>,</li>
	<li><code>abs(nums[i] - nums[j]) &lt;= valueDiff</code>.</li>
</ul>

<p>Return <code>true</code><em> if such a pair exists or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> i = 0, j = 3, abs(i - j) &lt;= 3 and abs(nums[i] - nums[j]) &lt;= 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> No pair satisfies the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= indexDiff &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= valueDiff &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Three lines. Line 1: indexDiff. Line 2: valueDiff. Line 3: space-separated integers for nums."
    output_format = "true if the condition is met, false otherwise."
    
    constraints = [
        "2 <= nums.length <= 10^5",
        "O(N) time complexity expected using Bucketing.",
        "O(indexDiff) space complexity expected."
    ]
    
    explanation = """To find duplicates within index distance `indexDiff` and value distance `valueDiff`:
1. **Bucketing (Bucket Sort Logic)**:
   - We divide the range of values into buckets of size `valueDiff + 1`.
   - The bucket ID for a value `x` is `x // (valueDiff + 1)`. 
   - *Note*: For negative numbers, handle the floor division carefully or offset the values.
2. **Logic**:
   - For each number `nums[i]` in the array:
     - Check its bucket. If the bucket already contains a value, we've found a pair within `valueDiff`.
     - Check the adjacent buckets (bucket - 1 and bucket + 1). If either contains a value `y` such that `abs(x - y) <= valueDiff`, we've found a pair.
     - Add `nums[i]` to its bucket.
     - maintain the window: If index `i >= indexDiff`, remove the element at `nums[i - indexDiff]` from its bucket.
3. **Complexity**:
   - Time Complexity: O(N) as each element is inserted and deleted once from a dictionary.
   - Space Complexity: O(indexDiff) for the dictionary storing elements in the current window."""
    
    answer = """def containsNearbyAlmostDuplicate(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    if valueDiff < 0: return False
    buckets = {}
    width = valueDiff + 1
    
    for i, x in enumerate(nums):
        b_id = x // width
        
        # Check current bucket
        if b_id in buckets:
            return True
        # Check neighboring buckets
        if (b_id - 1) in buckets and abs(x - buckets[b_id - 1]) <= valueDiff:
            return True
        if (b_id + 1) in buckets and abs(x - buckets[b_id + 1]) <= valueDiff:
            return True
            
        buckets[b_id] = x
        if i >= indexDiff:
            del buckets[nums[i - indexDiff] // width]
            
    return False"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    nums_all = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    if len(nums_all) >= 2:\n        indexDiff = nums_all[0]\n        valueDiff = nums_all[1]\n        nums = nums_all[2:]\n        print(\"true\" if containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nbool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int idxD, valD, val;\n    if (!(cin >> idxD >> valD)) return 0;\n    vector<int> nums;\n    while (cin >> val) nums.push_back(val);\n    cout << (containsNearbyAlmostDuplicate(nums, idxD, valD) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int idxD = sc.nextInt();\n        if (!sc.hasNextInt()) return;\n        int valD = sc.nextInt();\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) {\n            list.add(sc.nextInt());\n        }\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n        System.out.println(new Solution().containsNearbyAlmostDuplicate(nums, idxD, valD) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst numsAll = (input.match(/-?\\d+/g) || []).map(Number);\nif (numsAll.length >= 2) {\n    const indexDiff = numsAll[0];\n    const valueDiff = numsAll[1];\n    const nums = numsAll.slice(2);\n    console.log(containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nbool containsNearbyAlmostDuplicate(int* nums, int numsSize, int indexDiff, int valueDiff) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int idxD, valD, val;\n    if (scanf(\"%d %d\", &idxD, &valD) != 2) return 0;\n    int cap = 1000, size = 0;\n    int* nums = (int*)malloc(cap * sizeof(int));\n    while (scanf(\"%d\", &val) == 1) {\n        if (size >= cap) { cap *= 2; nums = (int*)realloc(nums, cap * sizeof(int)); }\n        nums[size++] = val;\n    }\n    if (size > 0) {\n        printf(\"%s\\n\", containsNearbyAlmostDuplicate(nums, size, idxD, valD) ? \"true\" : \"false\");\n    }\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3\\n0\\n1 2 3 1", "expected_output": "true", "is_sample": True},
        {"input": "2\\n3\\n1 5 9 1 5 9", "expected_output": "false", "is_sample": True},
        {"input": "1\\n1\\n1 2 3", "expected_output": "true", "is_sample": True},
        {"input": "2\\n2\\n1 4 1 1", "expected_output": "true", "is_sample": False},
        {"input": "1\\n100\\n-1 100", "expected_output": "true", "is_sample": False},
        {"input": "1\\n0\\n1 1", "expected_output": "true", "is_sample": False},
        {"input": "1\\n0\\n1 2", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "100000\\n0\\n" + " ".join([str(i) for i in range(100000)]), "expected_output": "false", "is_sample": False},
        {"input": "100000\\n1000000000\\n" + " ".join([str(i) for i in range(100000)]), "expected_output": "true", "is_sample": False},
        {"input": "1\\n0\\n" + " ".join(["42"]*100000), "expected_output": "true", "is_sample": False}
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
        "topics": ["Array", "Sliding Window", "Sorting", "Bucket Sort", "Ordered Set"],
        "companyIndex": 0
    }

    output_path = "1-200/220_Contains_Duplicate_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
