import json
import os

def generate_json():
    problem_id = 33
    title = "Search in Rotated Sorted Array"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>33. Search in Rotated Sorted Array</h3>
<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong> values).</p>

<p>Prior to being passed to your function, <code>nums</code> is <strong>possibly rotated</strong> at an unknown pivot index <code>k</code> (<code>1 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,5,6,7]</code> might be rotated at pivot index <code>3</code> and become <code>[4,5,6,7,0,1,2]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the rotation and an integer <code>target</code>, return <em>the index of </em><code>target</code><em> if it is in </em><code>nums</code><em>, or </em><code>-1</code><em> if it is not in </em><code>nums</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>All values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is an ascending array that is possibly rotated.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Line 1: Space-separated integers for the array 'nums'.\nLine 2: An integer 'target'."
    output_format = "An integer representing the index of 'target' in 'nums', or -1 if not found."
    
    constraints = [
        "1 <= nums.length <= 5000",
        "-10^4 <= nums[i], target <= 10^4",
        "All values in nums are unique.",
        "nums is sorted and then possibly rotated.",
        "Algorithm must be O(log n)."
    ]
    
    explanation = """To search for a target in a rotated sorted array in O(log N) time, use a modified binary search:
1. Initialize two pointers, `low = 0` and `high = n - 1`.
2. While `low <= high`:
   - Calculate the middle index `mid = (low + high) // 2`.
   - If `nums[mid] == target`, the target is found. Return `mid`.
   - Determine which half of the current range is properly sorted:
     - Case 1: `nums[low] <= nums[mid]` (Left half is sorted):
       - If the target is within the sorted left half (`nums[low] <= target < nums[mid]`), narrow the search to the left by setting `high = mid - 1`.
       - Otherwise, the target must be in the right half, so set `low = mid + 1`.
     - Case 2: `nums[mid] < nums[high]` (Right half is sorted):
       - If the target is within the sorted right half (`nums[mid] < target <= nums[high]`), narrow the search to the right by setting `low = mid + 1`.
       - Otherwise, the target must be in the left half, so set `high = mid - 1`.
3. If the target is not found after the loop, return -1.

This logic works because at any point in a rotated sorted array, at least one half (left or right) must be sorted."""
    
    answer = """def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        # Left side is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right side is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef search(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    if len(nums) >= 2:\n        target = nums.pop()\n        print(search(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint search(vector<int>& nums, int target) {\n    // User logic\n    return -1;\n}\n\nint main() {\n    string line;\n    vector<int> all_nums;\n    while (getline(cin, line)) {\n        for (char &c : line) if (c == ',' || c == '[' || c == ']' || c == '=') c = ' ';\n        stringstream ss(line);\n        string part;\n        while (ss >> part) {\n            if (part == \"nums\" || part == \"target\") continue;\n            try { all_nums.push_back(stoi(part)); } catch(...) {}\n        }\n    }\n    if (all_nums.size() >= 2) {\n        int target = all_nums.back();\n        all_nums.pop_back();\n        cout << search(all_nums, target) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int search(int[] nums, int target) {\n        // User logic\n        return -1;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> allNums = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9-]\", \"\");\n            if (!s.isEmpty()) try { allNums.add(Integer.parseInt(s)); } catch(Exception e) {}\n        }\n        if (allNums.size() >= 2) {\n            int target = allNums.get(allNums.size() - 1);\n            int[] nums = new int[allNums.size() - 1];\n            for (int i = 0; i < allNums.size() - 1; i++) nums[i] = allNums.get(i);\n            System.out.println(search(nums, target));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction search(nums, target) {\n    // User logic\n    return -1;\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst allNums = (data.match(/-?\\d+/g) || []).map(Number);\nif (allNums.length >= 2) {\n    const target = allNums.pop();\n    console.log(search(allNums, target));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint search(int* nums, int numsSize, int target) {\n    // User logic\n    return -1;\n}\n\nint main() {\n    int* all_nums = malloc(10000 * sizeof(int));\n    int count = 0;\n    char line[1000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                all_nums[count++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    if (count >= 2) {\n        int target = all_nums[count-1];\n        printf(\"%d\\n\", search(all_nums, count - 1, target));\n    }\n    free(all_nums);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "4 5 6 7 0 1 2\n0", "expected_output": "4", "is_sample": True},
        {"input": "4 5 6 7 0 1 2\n3", "expected_output": "-1", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1\n0", "expected_output": "-1", "is_sample": False},
        {"input": "1\n1", "expected_output": "0", "is_sample": False},
        {"input": "3 1\n1", "expected_output": "1", "is_sample": False},
        {"input": "1 3\n3", "expected_output": "1", "is_sample": False},
        {"input": "6 7 1 2 3 4 5\n6", "expected_output": "0", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(50, 100)] + [str(i) for i in range(0, 50)]) + "\n0", "expected_output": "50", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\n100", "expected_output": "99", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 101)]) + "\n0", "expected_output": "-1", "is_sample": False}
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "1-200/33_Search_in_Rotated_Sorted_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
