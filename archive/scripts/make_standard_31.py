import json
import os

def generate_json():
    problem_id = 31
    title = "Next Permutation"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>31. Next Permutation</h3>
<p>A <strong>permutation</strong> of an array of integers is an arrangement of its members into a sequence or linear order.</p>

<ul>
	<li>For example, for <code>arr = [1,2,3]</code>, the following are all the permutations of <code>arr</code>: <code>[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]</code>.</li>
</ul>

<p>The <strong>next permutation</strong> of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the <strong>next permutation</strong> of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).</p>

<ul>
	<li>For example, the next permutation of <code>arr = [1,2,3]</code> is <code>[1,3,2]</code>.</li>
	<li>Similarly, the next permutation of <code>arr = [2,3,1]</code> is <code>[3,1,2]</code>.</li>
	<li>While the next permutation of <code>arr = [3,2,1]</code> is <code>[1,2,3]</code> because <code>[3,2,1]</code> does not have a lexicographically larger rearrangement.</li>
</ul>

<p>Given an array of integers <code>nums</code>, <em>find the next permutation of</em> <code>nums</code>.</p>

<p>The replacement must be <strong><a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a></strong> and use only constant extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,5]
<strong>Output:</strong> [1,5,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>
"""

    input_format = "A single line containing space-separated integers for the array 'nums'."
    output_format = "A list of integers representing the next permutation."
    
    constraints = [
        "1 <= nums.length <= 100",
        "0 <= nums[i] <= 100",
        "Must be in-place with O(1) extra space."
    ]
    
    explanation = """To find the next lexicographically greater permutation of an array:
1. Traverse the array from right to left to find the first element `nums[i]` that is smaller than its successor `nums[i+1]`. This `nums[i]` is called the 'pivot'.
2. If no such pivot exists (i.e., the array is in descending order), it is the last possible permutation. Reverse the entire array to transform it into its smallest possible order (ascending).
3. If a pivot is found:
   - Search the array again from right to left for the first element `nums[j]` that is strictly greater than the pivot `nums[i]`.
   - Swap `nums[i]` and `nums[j]`.
   - Reverse the portion of the array to the right of index `i` (from `i + 1` to the end). This ensures the suffix is in the smallest possible lexicographical order.
4. This approach ensures the smallest possible lexicographical increment.

Time Complexity: O(N) where N is the length of the array.
Space Complexity: O(1) as the operation is in-place."""
    
    answer = """def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # Reverse suffix
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef nextPermutation(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        nums = [int(x) for x in data.split()]\n        nextPermutation(nums)\n        print(nums)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nvoid nextPermutation(vector<int>& nums) {\n    // User logic\n}\n\nint main() {\n    vector<int> nums;\n    int num;\n    while (cin >> num) nums.push_back(num);\n    \n    nextPermutation(nums);\n    \n    cout << \"[\";\n    for (int i = 0; i < nums.size(); i++) {\n        cout << nums[i] << (i < nums.size() - 1 ? \", \" : \"\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static void nextPermutation(int[] nums) {\n        // User logic\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        \n        int[] nums = new int[list.size()];\n        for(int i=0; i<list.size(); i++) nums[i] = list.get(i);\n        \n        nextPermutation(nums);\n        \n        System.out.print(\"[\");\n        for(int i=0; i<nums.length; i++) {\n            System.out.print(nums[i] + (i < nums.length - 1 ? \", \" : \"\"));\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction nextPermutation(nums) {\n    // User logic\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    const nums = input.map(Number);\n    nextPermutation(nums);\n    console.log(\"[\" + nums.join(\", \") + \"]\");\n} else {\n    console.log(\"[]\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid nextPermutation(int* nums, int numsSize) {\n    // User logic\n}\n\nint main() {\n    int capacity = 1000;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int size = 0, val;\n    while (scanf(\"%d\", &val) == 1) {\n        if (size == capacity) {\n            capacity *= 2;\n            nums = (int*)realloc(nums, capacity * sizeof(int));\n        }\n        nums[size++] = val;\n    }\n    \n    nextPermutation(nums, size);\n    \n    printf(\"[\");\n    for (int i = 0; i < size; i++) {\n        printf(\"%d\", nums[i]);\n        if (i < size - 1) printf(\", \");\n    }\n    printf(\"]\\n\");\n    free(nums);\n    return 0;\n}"
    }

    def _next_ref(nums_in):
        nums = list(nums_in)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        return nums

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3", "expected_output": str(_next_ref([1,2,3])), "is_sample": True},
        {"input": "3 2 1", "expected_output": str(_next_ref([3,2,1])), "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1 1 5", "expected_output": str(_next_ref([1,1,5])), "is_sample": False},
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "1 3 2", "expected_output": "[2, 1, 3]", "is_sample": False},
        {"input": "2 3 1", "expected_output": "[3, 1, 2]", "is_sample": False},
        {"input": "5 4 7 5 3 2", "expected_output": "[5, 5, 2, 3, 4, 7]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(20)]), "expected_output": str(_next_ref(range(20))), "is_sample": False},
        {"input": " ".join([str(i) for i in range(20, 0, -1)]), "expected_output": str(_next_ref(range(20, 0, -1))), "is_sample": False},
        {"input": " ".join(["50"]*50), "expected_output": str([50]*50), "is_sample": False}
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
        "topics": ["Array", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/31_Next_Permutation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
