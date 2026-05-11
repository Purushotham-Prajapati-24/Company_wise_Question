import json
import os

def generate_json():
    problem_id = 162
    title = "Find Peak Element"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>162. Find Peak Element</h3>
<p>A peak element is an element that is strictly greater than its neighbors.</p>

<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, find a peak element, and return its index. If the array contains multiple peaks, return the index to <strong>any of the peaks</strong>.</p>

<p>You may imagine that <code>nums[-1] = nums[n] = -&infin;</code>. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.</p>

<p>You must write an algorithm that runs in <code>O(log n)</code> time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 is a peak element and your function should return the index number 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,3,5,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>nums[i] != nums[i + 1]</code> for all valid <code>i</code>.</li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the index of any peak element."
    
    constraints = [
        "1 <= nums.length <= 1000",
        "-2^31 <= nums[i] <= 2^31 - 1",
        "O(log n) time complexity required.",
        "nums[i] != nums[i+1]."
    ]
    
    explanation = """To find a peak element in O(log N) time:
1. **Binary Search**:
   - A peak exists in any array where neighbors are unequal and boundaries are negative infinity.
   - We can use binary search by comparing `nums[mid]` with its neighbor `nums[mid + 1]`.
2. **Logic**:
   - If `nums[mid] < nums[mid + 1]`, we are on an upward slope. A peak must exist to the right. Move `left = mid + 1`.
   - If `nums[mid] >= nums[mid + 1]`, we are on a downward slope or at a peak. A peak must exist to the left (including `mid`). Move `right = mid`.
   - Finally, `left == right` will point to a peak index.
3. **Complexity**:
   - Time Complexity: O(log N).
   - Space Complexity: O(1)."""
    
    answer = """def findPeakElement(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left"""

    boilerplate = {
        "python": "import sys\n\ndef findPeakElement(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(findPeakElement(list(map(int, data))))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\nint findPeakElement(vector<int>& nums) {\n    // User logic here\n    return 0;\n}\nint main() {\n    vector<int> nums; int x;\n    while(cin >> x) nums.push_back(x);\n    if(!nums.empty()) cout << findPeakElement(nums) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int findPeakElement(int[] nums) {\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while(sc.hasNextInt()) list.add(sc.nextInt());\n        if(!list.isEmpty()){\n            int[] nums = new int[list.size()];\n            for(int i=0; i<list.size(); i++) nums[i] = list.get(i);\n            System.out.println(findPeakElement(nums));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction findPeakElement(nums) {\n    // User logic here\n    return 0;\n}\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nif(input.length > 0 && input[0] !== '') {\n    console.log(findPeakElement(input.map(Number)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\nint findPeakElement(int* nums, int numsSize) {\n    // User logic here\n    return 0;\n}\nint main() {\n    int capacity = 1005, size = 0, x;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    while(scanf(\"%d\", &x) == 1) nums[size++] = x;\n    if(size > 0) printf(\"%d\\n\", findPeakElement(nums, size));\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 2 3 1", "expected_output": "2", "is_sample": True},
        {"input": "1 2 1 3 5 6 4", "expected_output": "5", "is_sample": True},
        {"input": "1", "expected_output": "0", "is_sample": False},
        {"input": "1 2", "expected_output": "1", "is_sample": False},
        {"input": "2 1", "expected_output": "0", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "4", "is_sample": False},
        {"input": "5 4 3 2 1", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(1000)]), "expected_output": "999", "is_sample": False},
        {"input": " ".join([str(1000 - i) for i in range(1000)]), "expected_output": "0", "is_sample": False},
        {"input": "1 3 2 4 1 5 6 7 2", "expected_output": "...", "is_sample": False}
    ]
    
    def _is_peak(nums, idx):
        val = nums[idx]
        left = nums[idx-1] if idx > 0 else float('-inf')
        right = nums[idx+1] if idx < len(nums)-1 else float('-inf')
        return val > left and val > right

    # For the last case, we update it to show any index that is a peak.
    # Our checker will check if nums[res] is a peak.
    # But for JSON "expected_output" we can provide one valid index.
    test_cases[9]["expected_output"] = "1" # (3 is a peak in 1 3 2 ...)

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

    output_path = "1-200/162_Find_Peak_Element.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
