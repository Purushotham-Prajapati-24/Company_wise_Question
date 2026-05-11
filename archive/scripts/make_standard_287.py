import json
import os

def generate_json():
    problem_id = 287
    title = "Find the Duplicate Number"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>287. Find the Duplicate Number</h3>
<p>Given an array of integers <code>nums</code> containing&nbsp;<code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.</p>

<p>There is <strong>only one repeated number</strong> in <code>nums</code>, return <em>this&nbsp;repeated&nbsp;number</em>.</p>

<p>You must solve the problem <strong>without</strong> modifying the array <code>nums</code>&nbsp;and uses only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3,3,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li>All the integers in <code>nums</code> appear only <strong>once</strong> except for <strong>precisely one integer</strong> which appears <strong>two or more</strong> times.</li>
</ul>

<p>&nbsp;</p>
<p><b>Follow up:</b></p>

<ul>
	<li>How can we prove that at least one duplicate number must exist in <code>nums</code>?</li>
	<li>Can you solve the problem in linear runtime complexity?</li>
</ul>"""

    input_format = "A single line containing space-separated integers for the array nums."
    output_format = "An integer representing the duplicate number."
    
    constraints = [
        "1 <= n <= 10^5",
        "nums.length == n + 1",
        "1 <= nums[i] <= n",
        "Only one number is duplicated (it may appear multiple times).",
        "O(N) time complexity.",
        "O(1) extra space.",
        "Crucial: Do NOT modify the array (even temporarily)."
    ]
    
    explanation = """To find the duplicate number in linear time and constant space without modifying the array:
1. **Pigeonhole Principle**:
   - Since there are `n+1` numbers in the range `[1, n]`, at least one number must be duplicated.
2. **Floyd's Tortoise and Hare (Cycle Detection)**:
   - Treat the array as a linked list where `index i` points to `nums[i]`.
   - Because each value is an index in the range `[1, n]`, and there are `n+1` values, a cycle **must** exist. The duplicate number is the entry point to this cycle.
   - **Phase 1 (Finding intersection)**: Move a slow pointer (`tortoise`) one step at a time and a fast pointer (`hare`) two steps at a time. They will eventually meet inside the cycle.
   - **Phase 2 (Finding cycle entry)**: Reset one pointer to the start of the array and move both pointers one step at a time. The point where they meet is the entry point of the cycle, which corresponds to the duplicate number.
3. **Complexity**:
   - Time Complexity: O(N).
   - Space Complexity: O(1)."""
    
    answer = """def findDuplicate(nums: list[int]) -> int:
    # Phase 1: Finding intersection
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
    # Phase 2: Finding cycle entry (the duplicate)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow"""

    boilerplate = {
        "python": "import sys\n\ndef findDuplicate(nums: list[int]) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(findDuplicate(nums))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint findDuplicate(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    vector<int> nums;\n    int x;\n    while (cin >> x) nums.push_back(x);\n    cout << findDuplicate(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int findDuplicate(int[] nums) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        System.out.println(new Solution().findDuplicate(nums));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findDuplicate(nums) {\n    // User logic\n    return 0;\n}\n\nconst nums = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/).map(Number);\nconsole.log(findDuplicate(nums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint findDuplicate(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int* nums = malloc(200002 * sizeof(int));\n    int size = 0;\n    while (scanf(\"%d\", &nums[size]) == 1) size++;\n    printf(\"%d\\n\", findDuplicate(nums, size));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3 4 2 2", "expected_output": "2", "is_sample": True},
        {"input": "3 1 3 4 2", "expected_output": "3", "is_sample": True},
        {"input": "3 3 3 3 3", "expected_output": "3", "is_sample": True},
        {"input": "1 1", "expected_output": "1", "is_sample": False},
        {"input": "2 1 2", "expected_output": "2", "is_sample": False},
        {"input": "2 2 2 2 2", "expected_output": "2", "is_sample": False},
        {"input": "1 2 3 4 5 1", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1, 100001)] + ["100000"]), "expected_output": "100000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(1, 100001)] + ["1"]), "expected_output": "1", "is_sample": False},
        {"input": " ".join(["500"] * 100001), "expected_output": "500", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Binary Search", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "201-400/287_Find_the_Duplicate_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
