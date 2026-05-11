import json
import os

def generate_json():
    problem_id = 34
    title = "Find First and Last Position of Element in Sorted Array"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>34. Find First and Last Position of Element in Sorted Array</h3>
<p>Given an array of integers <code>nums</code> sorted in non-decreasing order, find the starting and ending position of a given <code>target</code> value.</p>

<p>If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is a non-decreasing array.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Line 1: Space-separated integers for the array 'nums'.\nLine 2: An integer 'target'."
    output_format = "A list containing two integers: [start_index, end_index]."
    
    constraints = [
        "0 <= nums.length <= 10^5",
        "-10^9 <= nums[i], target <= 10^9",
        "nums is sorted in non-decreasing order.",
        "Algorithm must be O(log n)."
    ]
    
    explanation = """To find the first and last position of a target in a sorted array in O(log N) time:
1. Use binary search twice: once for the starting position and once for the ending position.
2. **Find Starting (Left) Position**:
   - Perform binary search. If `nums[mid] == target`, record the index and continue searching the left half (`high = mid - 1`) to see if an earlier occurrence exists.
3. **Find Ending (Right) Position**:
   - Perform binary search. If `nums[mid] == target`, record the index and continue searching the right half (`low = mid + 1`) to see if a later occurrence exists.
4. If the target is not found in the starting position search, it is guaranteed not to exist in the ending position search either.
5. Return the pair of indices `[left_index, right_index]`.

Time Complexity: O(log N) as each binary search takes O(log N).
Space Complexity: O(1)."""
    
    answer = """def searchRange(nums, target):
    def findBound(is_first):
        l, h = 0, len(nums) - 1
        res = -1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                res = mid
                if is_first:
                    h = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return res
    
    return [findBound(True), findBound(False)]"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef searchRange(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    if len(nums) >= 2:\n        target = nums.pop()\n        print(searchRange(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<int> searchRange(vector<int>& nums, int target) {\n    // User logic\n    return {-1, -1};\n}\n\nint main() {\n    string line;\n    vector<int> all_nums;\n    while (getline(cin, line)) {\n        for (char &c : line) if (c == ',' || c == '[' || c == ']' || c == '=') c = ' ';\n        stringstream ss(line);\n        string part;\n        while (ss >> part) {\n            if (part == \"nums\" || part == \"target\") continue;\n            try { all_nums.push_back(stoi(part)); } catch(...) {}\n        }\n    }\n    if (all_nums.size() >= 2) {\n        int target = all_nums.back();\n        all_nums.pop_back();\n        vector<int> res = searchRange(all_nums, target);\n        cout << \"[\" << res[0] << \", \" << res[1] << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int[] searchRange(int[] nums, int target) {\n        // User logic\n        return new int[]{-1, -1};\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> allNums = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9-]\", \"\");\n            if (!s.isEmpty()) try { allNums.add(Integer.parseInt(s)); } catch(Exception e) {}\n        }\n        if (allNums.size() >= 2) {\n            int target = allNums.get(allNums.size() - 1);\n            int[] nums = new int[allNums.size() - 1];\n            for (int i = 0; i < allNums.size() - 1; i++) nums[i] = allNums.get(i);\n            int[] res = searchRange(nums, target);\n            System.out.println(Arrays.toString(res));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction searchRange(nums, target) {\n    // User logic\n    return [-1, -1];\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst allNums = (data.match(/-?\\d+/g) || []).map(Number);\nif (allNums.length >= 2) {\n    const target = allNums.pop();\n    console.log(JSON.stringify(searchRange(allNums, target)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint* searchRange(int* nums, int numsSize, int target, int* returnSize) {\n    // User logic\n    *returnSize = 2;\n    int* res = malloc(2 * sizeof(int));\n    res[0] = -1; res[1] = -1;\n    return res;\n}\n\nint main() {\n    int* all_nums = malloc(100000 * sizeof(int));\n    int count = 0;\n    char line[1000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                all_nums[count++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    if (count >= 2) {\n        int target = all_nums[count-1];\n        int returnSize;\n        int* res = searchRange(all_nums, count - 1, target, &returnSize);\n        printf(\"[%d, %d]\\n\", res[0], res[1]);\n    }\n    free(all_nums);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "5 7 7 8 8 10\n8", "expected_output": "[3, 4]", "is_sample": True},
        {"input": "5 7 7 8 8 10\n6", "expected_output": "[-1, -1]", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "\n0", "expected_output": "[-1, -1]", "is_sample": False},
        {"input": "1\n1", "expected_output": "[0, 0]", "is_sample": False},
        {"input": "5 5 5 5 5\n5", "expected_output": "[0, 4]", "is_sample": False},
        {"input": "1 2 3\n2", "expected_output": "[1, 1]", "is_sample": False},
        {"input": "1 2 3\n0", "expected_output": "[-1, -1]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["8"] * 100) + "\n8", "expected_output": "[0, 99]", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]) + "\n0", "expected_output": "[0, 0]", "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]) + "\n99", "expected_output": "[99, 99]", "is_sample": False}
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

    output_path = "1-200/34_Find_First_and_Last_Position_of_Element_in_Sorted_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
