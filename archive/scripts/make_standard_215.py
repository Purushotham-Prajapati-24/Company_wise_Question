import json
import os

def generate_json():
    problem_id = 215
    title = "Kth Largest Element in an Array"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>215. Kth Largest Element in an Array</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>largest element in the array</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Can you solve it without sorting?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: k. Line 2: space-separated integers for nums."
    output_format = "An integer representing the kth largest element."
    
    constraints = [
        "1 <= k <= nums.length <= 10^5",
        "O(N) time complexity expected (average).",
        "O(1) extra space complexity (ignoring recursion) is preferred."
    ]
    
    explanation = """To find the kth largest element efficiently:
1. **Quickselect Algorithm**:
   - This is based on the Partitioning logic of Quicksort.
   - Choose a pivot and partition the array around it.
   - After partitioning, if the pivot's index is exactly `n - k`, then the pivot is the kth largest element.
   - If the index is smaller, search the right side. If larger, search the left side.
2. **Heap-based approach**:
   - Keep a Min-Heap of size `k`.
   - Iterate through the array. For each element, push it into the heap. If the heap size exceeds `k`, pop the smallest element.
   - After one pass, the top of the heap is the kth largest element.
3. **Complexity**:
   - Quickselect: Average O(N), Worst-case O(N^2).
   - Min-Heap: O(N log K) time, O(K) space.
   - In most competitive environments, a randomized Quickselect or the Heap method is preferred."""
    
    answer = """import random

def findKthLargest(nums: list[int], k: int) -> int:
    def quickselect(l, r, target_idx):
        pivot_idx = random.randint(l, r)
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        
        # Partition
        store_idx = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
        nums[store_idx], nums[r] = nums[r], nums[store_idx]
        
        if store_idx == target_idx:
            return nums[store_idx]
        elif store_idx < target_idx:
            return quickselect(store_idx + 1, r, target_idx)
        else:
            return quickselect(l, store_idx - 1, target_idx)
            
    # kth largest is (len - k)th smallest
    return quickselect(0, len(nums) - 1, len(nums) - k)"""

    boilerplate = {
        "python": "import sys\n\ndef findKthLargest(nums, k):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        k = int(lines[0])\n        nums = [int(x) for x in lines[1].split()]\n        print(findKthLargest(nums, k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nint findKthLargest(vector<int>& nums, int k) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int k;\n    if (cin >> k) {\n        string line;\n        getline(cin, line); // consume newline\n        if (getline(cin, line)) {\n            stringstream ss(line);\n            int val;\n            vector<int> nums;\n            while (ss >> val) nums.push_back(val);\n            cout << findKthLargest(nums, k) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int findKthLargest(int[] nums, int k) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null && line2 != null) {\n            int k = Integer.parseInt(line1.trim());\n            String[] parts = line2.trim().split(\"\\\\s+\");\n            int[] nums = new int[parts.length];\n            for (int i = 0; i < parts.length; i++) {\n                nums[i] = Integer.parseInt(parts[i]);\n            }\n            System.out.println(new Solution().findKthLargest(nums, k));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findKthLargest(nums, k) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const k = parseInt(input[0].trim());\n    const nums = input[1].trim().split(/\\\\s+/).map(Number);\n    console.log(findKthLargest(nums, k));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint findKthLargest(int* nums, int numsSize, int k) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int k;\n    if (scanf(\"%d\", &k) == 1) {\n        int capacity = 1000;\n        int* nums = (int*)malloc(capacity * sizeof(int));\n        int size = 0;\n        int val;\n        while (scanf(\"%d\", &val) == 1) {\n            if (size >= capacity) {\n                capacity *= 2;\n                nums = (int*)realloc(nums, capacity * sizeof(int));\n            }\n            nums[size++] = val;\n        }\n        printf(\"%d\\n\", findKthLargest(nums, size, k));\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2\\n3 2 1 5 6 4", "expected_output": "5", "is_sample": True},
        {"input": "4\\n3 2 3 1 2 4 5 5 6", "expected_output": "4", "is_sample": True},
        {"input": "1\\n100", "expected_output": "100", "is_sample": True},
        {"input": "1\\n1 2 3", "expected_output": "3", "is_sample": False},
        {"input": "3\\n1 2 3", "expected_output": "1", "is_sample": False},
        {"input": "2\\n-1 -2 -3", "expected_output": "-2", "is_sample": False},
        {"input": "10\\n" + " ".join([str(i) for i in range(1, 21)]), "expected_output": "11", "is_sample": False},
        # Stress cases
        {"input": "50000\\n" + " ".join([str(i) for i in range(100000)]), "expected_output": "50000", "is_sample": False},
        {"input": "1\\n" + " ".join(["42"]*100000), "expected_output": "42", "is_sample": False},
        {"input": "100000\\n" + " ".join([str(i) for i in range(100000)]), "expected_output": "0", "is_sample": False}
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
        "topics": ["Array", "Divide and Conquer", "Sorting", "Heap (Priority Queue)", "Quickselect"],
        "companyIndex": 0
    }

    output_path = "1-200/215_Kth_Largest_Element_in_an_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
