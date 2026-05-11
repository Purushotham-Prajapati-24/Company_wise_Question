import json
import os

def generate_json():
    problem_id = 324
    title = "Wiggle Sort II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>324. Wiggle Sort II</h3>
<p>Given an integer array <code>nums</code>, reorder it such that <code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>.</p>

<p>You may assume the input array always has a valid answer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,5,1,1,6,4]
<strong>Output:</strong> [1,6,1,5,1,4]
<strong>Explanation:</strong> [1,4,1,5,1,6] is also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,2,2,3,1]
<strong>Output:</strong> [2,3,1,3,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5000</code></li>
	<li>It is guaranteed that there will be an answer for the given input <code>nums</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow Up:</strong> Can you do it in <code>O(n)</code> time and/or <code>O(1)</code> extra space?"""

    input_format = "An integer array `nums`."
    output_format = "Modify the array `nums` in-place (or return it depending on caller)."
    
    constraints = [
        "1 <= nums.length <= 50,000",
        "0 <= nums[i] <= 5000"
    ]
    
    explanation = """To reorder an array into a wiggle pattern ($nums[0] < nums[1] > nums[2] < nums[3]...$), the most efficient $O(N)$ approach involves finding the median of the array and using virtual indexing.

### Algorithm Steps:
1. **Find the Median**: Use the **QuickSelect** algorithm (or `statistics.median` in Python for simplicity, though sorted median is $O(N \log N)$) to find the median of the array. Let's call it `mid`.
2. **Virtual Indexing**: We want to place numbers larger than `mid` in odd positions (1, 3, 5...) and numbers smaller than `mid` in even positions (0, 2, 4...) from right to left to avoid duplicates clashing.
   - Index mapping function: $f(i) = (1 + 2i) \pmod{n \text{ or } n|1}$.
3. **Partition (Dutch National Flag)**: Perform a 3-way partition using the mapped indices:
   - If `mapped_num > mid`: Move to the "left" side of the virtual array (odd positions).
   - If `mapped_num < mid`: Move to the "right" side of the virtual array (even positions).
   - If `mapped_num == mid`: Keep in the middle of the virtual array.

### Complexity Analysis:
- **Time Complexity**: $O(N)$. QuickSelect takes $O(N)$ on average and the 3-way partition is $O(N)$.
- **Space Complexity**: $O(1)$ extra space if including virtual mapping (excluding the input array and recursion stack). In Python, since `nums.sort()` is highly optimized, the sorting-based $O(N \log N)$ solution is also very popular: `nums.sort(); nums[::2], nums[1::2] = nums[:(n+1)//2][::-1], nums[(n+1)//2:][::-1]`."""
    
    answer = """class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Most optimized Pythonic approach is O(N log N) sorting
        # due to low overhead, but O(N) is the theoretical goal.
        # We will use the sorting approach for robustness in Python environments.
        n = len(nums)
        nums.sort()
        mid = (n + 1) // 2
        # Use two halves in reverse order to ensure wiggle condition
        # and handle duplicate elements correctly at the boundaries.
        small = nums[:mid][::-1]
        large = nums[mid:][::-1]
        
        nums[::2] = small
        nums[1::2] = large"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def wiggleSort(self, nums: list[int]) -> None:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        nums = json.loads(raw_input)\n        sol = Solution()\n        sol.wiggleSort(nums)\n        print(json.dumps(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nclass Solution {\npublic:\n    void wiggleSort(vector<int>& nums) {\n        // Your logic here\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<int> nums;\n        if (line.length() >= 2) {\n            line = line.substr(1, line.length() - 2);\n            if (!line.empty()) {\n                stringstream ss(line);\n                string item;\n                while (getline(ss, item, ',')) {\n                    nums.push_back(stoi(item));\n                }\n            }\n        }\n        Solution sol;\n        sol.wiggleSort(nums);\n        cout << \"[\";\n        for (size_t i = 0; i < nums.size(); ++i) {\n            cout << nums[i] << (i < nums.size() - 1 ? \",\" : \"\");\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public void wiggleSort(int[] nums) {\n        // Your logic here\n    }\n\n    public static void main(String[] args) {\n        Scanner scanner = new Scanner(System.in);\n        if (scanner.hasNextLine()) {\n            String line = scanner.nextLine().trim();\n            if (line.length() >= 2) {\n                line = line.substring(1, line.length() - 1);\n            }\n            int[] nums;\n            if (line.isEmpty()) {\n                nums = new int[0];\n            } else {\n                String[] parts = line.split(\",\");\n                nums = new int[parts.length];\n                for (int i = 0; i < parts.length; i++) {\n                    nums[i] = Integer.parseInt(parts[i].trim());\n                }\n            }\n            Solution sol = new Solution();\n            sol.wiggleSort(nums);\n            System.out.print(\"[\");\n            for (int i = 0; i < nums.length; i++) {\n                System.out.print(nums[i] + (i < nums.length - 1 ? \",\" : \"\"));\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @return {void} Do not return anything, modify nums in-place instead.\n */\nvar wiggleSort = function(nums) {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync('/dev/stdin', 'utf-8').trim().split('\\n');\nif (input.length >= 1 && input[0]) {\n    const nums = JSON.parse(input[0]);\n    wiggleSort(nums);\n    console.log(JSON.stringify(nums));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nvoid wiggleSort(int* nums, int numsSize) {\n    // Your logic here\n}\n\nint main() {\n    char line[500000];\n    if (fgets(line, sizeof(line), stdin)) {\n        line[strcspn(line, \"\\r\\n\")] = 0;\n        int capacity = 100;\n        int* nums = malloc(capacity * sizeof(int));\n        int size = 0;\n        char* ptr = line;\n        while (*ptr && *ptr != '[') ptr++;\n        if (*ptr == '[') ptr++;\n        while (*ptr && *ptr != ']') {\n            int val;\n            int charsRead;\n            if (sscanf(ptr, \"%d%n\", &val, &charsRead) == 1) {\n                if (size >= capacity) {\n                    capacity *= 2;\n                    nums = realloc(nums, capacity * sizeof(int));\n                }\n                nums[size++] = val;\n                ptr += charsRead;\n            } else {\n                ptr++;\n            }\n        }\n        wiggleSort(nums, size);\n        printf(\"[\");\n        for (int i = 0; i < size; i++) {\n            printf(\"%d%s\", nums[i], i < size - 1 ? \",\" : \"\");\n        }\n        printf(\"]\\n\");\n        free(nums);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,5,1,1,6,4]", "expected_output": "[1,6,1,5,1,4]", "is_sample": True},
        {"input": "[1,3,2,2,3,1]", "expected_output": "[2,3,1,3,1,2]", "is_sample": True},
        {"input": "[1,1,2,2,3,3]", "expected_output": "[2,3,1,2,1,3]", "is_sample": False},
        {"input": "[4,5,5,6]", "expected_output": "[5,6,4,5]", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "[2,3,1]", "is_sample": False},
        {"input": "[1,2,3,4]", "expected_output": "[2,4,1,3]", "is_sample": False},
        {"input": "[10,9,8,7,6,5,4,3,2,1]", "expected_output": "[5,10,4,9,3,8,2,7,1,6]", "is_sample": False},
        # Stress cases
        {"input": json.dumps([i % 5 for i in range(50000)]), "expected_output": "...", "is_sample": False},
        {"input": json.dumps([1] * 25000 + [2] * 25000), "expected_output": "...", "is_sample": False},
        {"input": json.dumps(list(range(50000))), "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Sorting", "QuickSelect"],
        "companyIndex": 1
    }

    output_path = "301-500/324_Wiggle_Sort_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
