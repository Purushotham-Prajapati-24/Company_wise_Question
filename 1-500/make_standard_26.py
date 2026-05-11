import json
import os

def generate_json():
    problem_id = 26
    title = "Remove Duplicates from Sorted Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>26. Remove Duplicates from Sorted Array</h3>
<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> such that each unique element appears only <strong>once</strong>. The relative order of the elements should be kept the <strong>same</strong>. Then return <em>the number of unique elements in </em><code>nums</code>.</p>

<p>Consider the number of unique elements of <code>nums</code> to be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the unique elements in the order they were present in <code>nums</code> initially. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>
"""

    input_format = "A single line containing space-separated integers for the array 'nums'."
    output_format = "An integer 'k' representing the number of unique elements, followed by the first 'k' elements of the modified array."
    
    constraints = [
        "1 <= nums.length <= 3 * 10^4",
        "-100 <= nums[i] <= 100",
        "nums is sorted in non-decreasing order."
    ]
    
    explanation = """To remove duplicates from a sorted array in-place:
1. Since the array is sorted, all duplicate elements will be located adjacent to each other.
2. Use two pointers: `i` (the slow pointer) and `j` (the fast pointer).
3. Initialize `i = 0`. The element at `nums[i]` is the first unique element.
4. Iterate `j` from 1 to the end of the array:
   - If `nums[j]` is not equal to `nums[i]`, it means we have found a new unique element.
   - Increment `i` to move to the next position available for a unique element.
   - Copy the value of `nums[j]` to `nums[i]`.
5. After the loop, the first `i + 1` elements of the array are the unique elements in their original order.
6. Return `i + 1` as the count of unique elements.

Time Complexity: O(N) where N is the length of the array.
Space Complexity: O(1) as the modification is done in-place."""
    
    answer = """def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef removeDuplicates(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        nums = [int(x) for x in data.split()]\n        k = removeDuplicates(nums)\n        print(k)\n        if k > 0:\n            print(\" \".join(map(str, nums[:k])))\n    else:\n        print(0)",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint removeDuplicates(vector<int>& nums) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    vector<int> nums;\n    int num;\n    while (cin >> num) nums.push_back(num);\n    int k = removeDuplicates(nums);\n    cout << k << endl;\n    for (int i = 0; i < k; i++) {\n        cout << nums[i] << (i < k - 1 ? \" \" : \"\");\n    }\n    if (k > 0) cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int removeDuplicates(int[] nums) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        \n        int[] nums = new int[list.size()];\n        for(int i=0; i<list.size(); i++) nums[i] = list.get(i);\n        \n        int k = removeDuplicates(nums);\n        System.out.println(k);\n        for(int i=0; i<k; i++) {\n            System.out.print(nums[i] + (i < k - 1 ? \" \" : \"\"));\n        }\n        if (k > 0) System.out.println();\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction removeDuplicates(nums) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    const nums = input.map(Number);\n    const k = removeDuplicates(nums);\n    console.log(k);\n    if (k > 0) {\n        console.log(nums.slice(0, k).join(' '));\n    }\n} else {\n    console.log(0);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint removeDuplicates(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int capacity = 1000;\n    int* nums = (int*)malloc(capacity * sizeof(int));\n    int size = 0, val;\n    while (scanf(\"%d\", &val) == 1) {\n        if (size == capacity) {\n            capacity *= 2;\n            nums = (int*)realloc(nums, capacity * sizeof(int));\n        }\n        nums[size++] = val;\n    }\n    \n    int k = removeDuplicates(nums, size);\n    printf(\"%d\\n\", k);\n    for (int i = 0; i < k; i++) {\n        printf(\"%d\", nums[i]);\n        if (i < k - 1) printf(\" \");\n    }\n    if (k > 0) printf(\"\\n\");\n    free(nums);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 1 2", "expected_output": "2\\n1 2", "is_sample": True},
        {"input": "0 0 1 1 1 2 2 3 3 4", "expected_output": "5\\n0 1 2 3 4", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "1 2 3", "expected_output": "3\\n1 2 3", "is_sample": False},
        {"input": "1 1 1 1 1", "expected_output": "1\\n1", "is_sample": False},
        {"input": "-100 -100 0 100 100", "expected_output": "3\\n-100 0 100", "is_sample": False},
        {"input": "-1 0 0 0 0 1", "expected_output": "3\\n-1 0 1", "is_sample": False},
        {"input": "1 1", "expected_output": "1\\n1", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i//10) for i in range(100)]), "expected_output": "10\\n0 1 2 3 4 5 6 7 8 9", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-50, 50)]), "expected_output": "100\\n" + " ".join([str(i) for i in range(-50, 50)]), "is_sample": False},
        {"input": " ".join(["100"] * 100), "expected_output": "1\\n100", "is_sample": False}
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

    output_path = "1-200/26_Remove_Duplicates_from_Sorted_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
