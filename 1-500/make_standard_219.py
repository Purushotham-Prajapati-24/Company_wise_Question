import json
import os

def generate_json():
    problem_id = 219
    title = "Contains Duplicate II"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>219. Contains Duplicate II</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: integer k. Line 2: space-separated integers for nums."
    output_format = "true if the condition is met, false otherwise."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "-10^9 <= nums[i] <= 10^9",
        "0 <= k <= 10^5",
        "O(N) time complexity expected.",
        "O(min(N, k)) space complexity expected."
    ]
    
    explanation = """To detect duplicates within distance `k`:
1. **Sliding Window with Hash Set**:
   - Maintain a hash set `window` containing the last `k` elements.
   - For each element `nums[i]` at index `i`:
     - If `nums[i]` is in the `window`, then we've found a duplicate within distance `k`. Return `true`.
     - Add `nums[i]` to the `window`.
     - If the size of the `window` exceeds `k`, remove the oldest element (`nums[i - k]`).
2. **Alternative (Hash Map)**:
   - Store the last seen index of each element in a hash map.
   - If `nums[i]` is in the map and `i - last_index <= k`, return `true`.
   - Update `last_index` for `nums[i]`.
3. **Complexity**:
   - Time Complexity: O(N) since we iterate through the array once.
   - Space Complexity: O(min(N, k)) for the sliding window set."""
    
    answer = """def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True
        window.add(nums[i])
        if len(window) > k:
            window.remove(nums[i - k])
    return False"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef containsNearbyDuplicate(nums, k):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    nums_all = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    if len(nums_all) >= 1:\n        k = nums_all[0]\n        nums = nums_all[1:]\n        print(\"true\" if containsNearbyDuplicate(nums, k) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nbool containsNearbyDuplicate(vector<int>& nums, int k) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int k, val;\n    if (!(cin >> k)) return 0;\n    vector<int> nums;\n    while (cin >> val) nums.push_back(val);\n    cout << (containsNearbyDuplicate(nums, k) ? \"true\" : \"false\") << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean containsNearbyDuplicate(int[] nums, int k) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int k = sc.nextInt();\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) {\n            list.add(sc.nextInt());\n        }\n        int[] nums = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n        System.out.println(new Solution().containsNearbyDuplicate(nums, k) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction containsNearbyDuplicate(nums, k) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst numsAll = (input.match(/-?\\d+/g) || []).map(Number);\nif (numsAll.length >= 1) {\n    const k = numsAll[0];\n    const nums = numsAll.slice(1);\n    console.log(containsNearbyDuplicate(nums, k) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\nbool containsNearbyDuplicate(int* nums, int numsSize, int k) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int k, val;\n    if (scanf(\"%d\", &k) != 1) return 0;\n    int cap = 1000, size = 0;\n    int* nums = (int*)malloc(cap * sizeof(int));\n    while (scanf(\"%d\", &val) == 1) {\n        if (size >= cap) { cap *= 2; nums = (int*)realloc(nums, cap * sizeof(int)); }\n        nums[size++] = val;\n    }\n    printf(\"%s\\n\", containsNearbyDuplicate(nums, size, k) ? \"true\" : \"false\");\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "3\\n1 2 3 1", "expected_output": "true", "is_sample": True},
        {"input": "1\\n1 0 1 1", "expected_output": "true", "is_sample": True},
        {"input": "2\\n1 2 3 1 2 3", "expected_output": "false", "is_sample": True},
        {"input": "1\\n1 2", "expected_output": "false", "is_sample": False},
        {"input": "5\\n1 2 1", "expected_output": "true", "is_sample": False},
        {"input": "1\\n1 1", "expected_output": "true", "is_sample": False},
        {"input": "0\\n1 1", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "100000\\n" + " ".join([str(i) for i in range(100000)]), "expected_output": "false", "is_sample": False},
        {"input": "1\\n" + " ".join(["42"]*100000), "expected_output": "true", "is_sample": False},
        {"input": "50000\\n" + " ".join([str(i) for i in range(50000)]) + " 0", "expected_output": "true", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = "1-200/219_Contains_Duplicate_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
