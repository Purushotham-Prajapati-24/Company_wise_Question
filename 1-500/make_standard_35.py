import json
import os

def generate_json():
    problem_id = 35
    title = "Search Insert Position"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>35. Search Insert Position</h3>
<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i], target &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
</ul>"""

    input_format = "Line 1: Space-separated integers for the array 'nums'.\nLine 2: An integer 'target'."
    output_format = "An integer representing the index where 'target' is found or should be inserted."
    
    constraints = [
        "1 <= nums.length <= 10^4",
        "-10^4 <= nums[i], target <= 10^4",
        "nums contains distinct values sorted in ascending order.",
        "Algorithm must be O(log n)."
    ]
    
    explanation = """To find the search insert position in O(log N) time:
1. Use a standard binary search approach.
2. Initialize two pointers: `low = 0` and `high = len(nums) - 1`.
3. While `low <= high`:
   - Calculate the middle index `mid = (low + high) // 2`.
   - If `nums[mid] == target`, the target is already present at index `mid`. Return `mid`.
   - If `nums[mid] < target`, the target must be in the right half. Update `low = mid + 1`.
   - If `nums[mid] > target`, the target must be in the left half. Update `high = mid - 1`.
4. If the target is not found after the loop finishes, the `low` pointer will be at the correct insertion index. This is because `low` always moves to the first element greater than `target`.
5. Return `low`.

Time Complexity: O(log N) due to binary search.
Space Complexity: O(1)."""
    
    answer = """def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\nimport re\n\ndef searchInsert(nums, target):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    if len(nums) >= 2:\n        target = nums.pop()\n        print(searchInsert(nums, target))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint searchInsert(vector<int>& nums, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string line;\n    vector<int> all_nums;\n    while (getline(cin, line)) {\n        for (char &c : line) if (c == ',' || c == '[' || c == ']' || c == '=') c = ' ';\n        stringstream ss(line);\n        string part;\n        while (ss >> part) {\n            if (part == \"nums\" || part == \"target\") continue;\n            try { all_nums.push_back(stoi(part)); } catch(...) {}\n        }\n    }\n    if (all_nums.size() >= 2) {\n        int target = all_nums.back();\n        all_nums.pop_back();\n        cout << searchInsert(all_nums, target) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int searchInsert(int[] nums, int target) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> allNums = new ArrayList<>();\n        while (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[^0-9-]\", \"\");\n            if (!s.isEmpty()) try { allNums.add(Integer.parseInt(s)); } catch(Exception e) {}\n        }\n        if (allNums.size() >= 2) {\n            int target = allNums.get(allNums.size() - 1);\n            int[] nums = new int[allNums.size() - 1];\n            for (int i = 0; i < allNums.size() - 1; i++) nums[i] = allNums.get(i);\n            System.out.println(searchInsert(nums, target));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction searchInsert(nums, target) {\n    // User logic\n    return 0;\n}\n\nconst data = fs.readFileSync(0, 'utf-8');\nconst allNums = (data.match(/-?\\d+/g) || []).map(Number);\nif (allNums.length >= 2) {\n    const target = allNums.pop();\n    console.log(searchInsert(allNums, target));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint searchInsert(int* nums, int numsSize, int target) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int* all_nums = malloc(100000 * sizeof(int));\n    int count = 0;\n    char line[1000];\n    while (fgets(line, sizeof(line), stdin)) {\n        char* p = line;\n        while (*p) {\n            while (*p && !isdigit(*p) && *p != '-') p++;\n            if (*p) {\n                all_nums[count++] = atoi(p);\n                if (*p == '-') p++;\n                while (*p && isdigit(*p)) p++;\n            }\n        }\n    }\n    if (count >= 2) {\n        int target = all_nums[count-1];\n        printf(\"%d\\n\", searchInsert(all_nums, count - 1, target));\n    }\n    free(all_nums);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 3 5 6\n5", "expected_output": "2", "is_sample": True},
        {"input": "1 3 5 6\n2", "expected_output": "1", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1 3 5 6\n7", "expected_output": "4", "is_sample": False},
        {"input": "1 3 5 6\n0", "expected_output": "0", "is_sample": False},
        {"input": "1\n0", "expected_output": "0", "is_sample": False},
        {"input": "1\n1", "expected_output": "0", "is_sample": False},
        {"input": "1\n2", "expected_output": "1", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(100)]) + "\n50", "expected_output": "50", "is_sample": False},
        {"input": " ".join([str(i*2) for i in range(100)]) + "\n199", "expected_output": "100", "is_sample": False},
        {"input": " ".join([str(i*2) for i in range(100)]) + "\n-1", "expected_output": "0", "is_sample": False}
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

    output_path = "1-200/35_Search_Insert_Position.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
