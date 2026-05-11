import json
import os

def generate_json():
    problem_id = 280
    title = "Wiggle Sort"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>280. Wiggle Sort</h3>
<p>Given an unsorted array <code>nums</code>, reorder it <strong>in-place</strong> such that <code>nums[0] &lt;= nums[1] &gt;= nums[2] &lt;= nums[3]...</code>.</p>

<p>For example, given <code>nums = [3, 5, 2, 1, 6, 4]</code>, one possible answer is <code>[1, 6, 2, 5, 3, 4]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,5,2,1,6,4]
<strong>Output:</strong> [3,5,1,6,2,4]
<strong>Explanation:</strong> [1,6,2,5,3,4] is also a valid answer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A stringified array of integers `nums`."
    output_format = "A stringified array containing the wiggle-sorted numbers."
    
    constraints = [
        "1 <= n <= 50,000",
        "0 <= nums[i] <= 10,000"
    ]
    
    explanation = """To wiggle sort an array in O(n) time and O(1) space:
1. **Greedy Traversal**: We iterate through the array once.
2. **Comparison Logic**:
   - If the current index `i` is **odd**, `nums[i]` should be greater than or equal to `nums[i-1]`. If not, we swap them.
   - If the current index `i` is **even** (and `i > 0`), `nums[i]` should be less than or equal to `nums[i-1]`. If not, we swap them.
3. **In-place swap**: Swapping adjacent elements doesn't break the wiggle property of elements already processed.
4. **Complexity Analysis**:
   - Time: O(N) since we visit each element only once.
   - Space: O(1) as we modify the array in-place."""
    
    answer = """class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # 1. Iterate through the array
        for i in range(len(nums) - 1):
            # 2. Check if the current order violates the wiggle condition
            # Index i even: nums[i] <= nums[i+1]
            # Index i odd: nums[i] >= nums[i+1]
            if (i % 2 == 0 and nums[i] > nums[i+1]) or (i % 2 == 1 and nums[i] < nums[i+1]):
                # 3. Swap the elements in place
                nums[i], nums[i+1] = nums[i+1], nums[i]"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef wiggleSort(nums: list[int]) -> None:\n    # User logic here (modify nums in-place)\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        nums = json.loads(input_data)\n        wiggleSort(nums)\n        print(json.dumps(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nvoid wiggleSort(vector<int>& nums) {\n    // User logic here\n}\n\nint main() {\n    vector<int> nums;\n    int x;\n    while (cin >> x) nums.push_back(x);\n    wiggleSort(nums);\n    for (int i = 0; i < (int)nums.size(); i++) {\n        if (i) cout << ' ';\n        cout << nums[i];\n    }\n    cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public void wiggleSort(int[] nums) {\n        // User logic here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] nums = list.stream().mapToInt(i -> i).toArray();\n        new Solution().wiggleSort(nums);\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < nums.length; i++) {\n            if (i > 0) sb.append(' ');\n            sb.append(nums[i]);\n        }\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction wiggleSort(nums) {\n    // User logic here\n}\n\nconst nums = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/).map(Number);\nwiggleSort(nums);\nconsole.log(nums.join(' '));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nvoid wiggleSort(int* nums, int numsSize) {\n    // User logic here\n}\n\nint main() {\n    int* nums = malloc(100000 * sizeof(int));\n    int size = 0;\n    while (scanf(\"%d\", &nums[size]) == 1) size++;\n    wiggleSort(nums, size);\n    for (int i = 0; i < size; i++) {\n        if (i) printf(\" \");\n        printf(\"%d\", nums[i]);\n    }\n    printf(\"\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,5,2,1,6,4]", "expected_output": "[3,5,1,6,2,4]", "is_sample": True},
        {"input": "[1,2,3]", "expected_output": "[1,3,2]", "is_sample": True},
        {"input": "[1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[2,1]", "expected_output": "[1,2]", "is_sample": False},
        {"input": "[1,1,1]", "expected_output": "[1,1,1]", "is_sample": False},
        {"input": "[6,5,4,3,2,1]", "expected_output": "[5,6,3,4,1,2]", "is_sample": False},
        {"input": "[1,2,3,4,5,6]", "expected_output": "[1,3,2,5,4,6]", "is_sample": False},
        # Stress cases
        {"input": "[" + ",".join([str(i) for i in range(50000)]) + "]", "expected_output": "...", "is_sample": False},
        {"input": "[" + ",".join([str(i%100) for i in range(50000)]) + "]", "expected_output": "...", "is_sample": False},
        {"input": "[" + ",".join(["5000"]*50000) + "]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Sorting", "Greedy"],
        "companyIndex": 0
    }

    output_path = "201-400/280_Wiggle_Sort.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
