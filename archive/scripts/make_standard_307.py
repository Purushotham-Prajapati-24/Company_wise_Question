import json
import os

def generate_json():
    problem_id = 307
    title = "Range Sum Query - Mutable"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>307. Range Sum Query - Mutable</h3>
<p>Given an integer array <code>nums</code>, handle multiple queries of the following types:</p>

<ol>
	<li><strong>Update</strong> the value of an element in <code>nums</code>.</li>
	<li>Calculate the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> where <code>left &lt;= right</code>.</li>
</ol>

<p>Implement the <code>NumArray</code> class:</p>
<ul>
	<li><code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
	<li><code>void update(int index, int val)</code> Updates the value of <code>nums[index]</code> to be <code>val</code>.</li>
	<li><code>int sumRange(int left, int right)</code> Returns the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> (i.e., <code>nums[left] + nums[left + 1] + ... + nums[right]</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
<strong>Output:</strong>
[null, 9, null, 8]

<strong>Explanation:</strong>
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>0 &lt;= index &lt; nums.length</code></li>
	<li><code>-100 &lt;= val &lt;= 100</code></li>
	<li><code>0 &lt;= left &lt;= right &lt; nums.length</code></li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>update</code> and <code>sumRange</code>.</li>
</ul>"""

    input_format = "A list of strings for commands and a list of arguments."
    output_format = "A list of results (null for void methods, integers for sumRange)."
    
    constraints = [
        "1 <= nums.length <= 30,000",
        "At most 30,000 calls to update and sumRange."
    ]
    
    explanation = """To handle frequent point updates and range sum queries efficiently ($O(\log N)$ for both):
1. **Fenwick Tree (BIT)**: This is the most space-efficient way to handle cumulative sums and updates.
2. **Operations**:
   - `update(index, val)`: Find the difference `diff = val - original_nums[index]`. Update the BIT at `index + 1` by adding `diff`.
   - `sumRange(left, right)`: Calculate `query(right + 1) - query(left)`.
3. **BIT Logic**:
   - `query(i)`: Sum of elements from index 1 to i. Traverse parents using `i -= i & -i`.
   - `updateBIT(i, diff)`: Add `diff` to indices and their ancestors using `i += i & -i`.
4. **Complexity Analysis**:
   - Initialization: O(N log N) or O(N).
   - Update: O(log N).
   - Query: O(log N).
   - Space: O(N) to store the BIT and original nums."""
    
    answer = """class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)
        # Build BIT in O(N log N)
        for i in range(self.n):
            self.init_update(i, nums[i])
            
    def init_update(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & (-i)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.init_update(index, diff)

    def get_sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(right) - self.get_sum(left - 1)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass NumArray:\n    def __init__(self, nums):\n        # User logic here\n        pass\n    def update(self, index, val):\n        pass\n    def sumRange(self, left, right):\n        return 0\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    commands = json.loads(lines[0].strip())\n    arguments = json.loads(lines[1].strip())\n    obj = None\n    results = []\n    for cmd, args in zip(commands, arguments):\n        if cmd == 'NumArray':\n            obj = NumArray(args[0])\n            results.append(None)\n        elif cmd == 'update':\n            obj.update(args[0], args[1])\n            results.append(None)\n        elif cmd == 'sumRange':\n            results.append(obj.sumRange(args[0], args[1]))\n    print(json.dumps(results))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nclass NumArray {\npublic:\n    NumArray(vector<int>& nums) {\n        // User logic here\n    }\n    void update(int index, int val) {\n        // User logic here\n    }\n    int sumRange(int left, int right) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    // Command-based input: read commands and args\n    // User logic here\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class NumArray {\n    public NumArray(int[] nums) {\n        // User logic here\n    }\n    public void update(int index, int val) {\n        // User logic here\n    }\n    public int sumRange(int left, int right) {\n        // User logic here\n        return 0;\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass NumArray {\n    constructor(nums) {\n        // User logic here\n    }\n    update(index, val) {\n        // User logic here\n    }\n    sumRange(left, right) {\n        // User logic here\n        return 0;\n    }\n}\n\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst commands = JSON.parse(lines[0]);\nconst args = JSON.parse(lines[1]);\nlet obj = null;\nconst results = [];\nfor (let i = 0; i < commands.length; i++) {\n    if (commands[i] === 'NumArray') { obj = new NumArray(args[i][0]); results.push(null); }\n    else if (commands[i] === 'update') { obj.update(args[i][0], args[i][1]); results.push(null); }\n    else if (commands[i] === 'sumRange') results.push(obj.sumRange(args[i][0], args[i][1]));\n}\nconsole.log(JSON.stringify(results));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct { int* data; int size; } NumArray;\n\nNumArray* numArrayCreate(int* nums, int numsSize) {\n    // User logic here\n    return NULL;\n}\nvoid numArrayUpdate(NumArray* obj, int index, int val) {}\nint numArraySumRange(NumArray* obj, int left, int right) { return 0; }\nvoid numArrayFree(NumArray* obj) { if(obj) free(obj); }\n\nint main() {\n    // User logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["NumArray", "sumRange", "update", "sumRange"]\n[[1, 3, 5], [0, 2], [1, 2], [0, 2]]', "expected_output": "[null, 9, null, 8]", "is_sample": True},
        {"input": '["NumArray", "sumRange"]\n[[10], [0, 0]]', "expected_output": "[null, 10]", "is_sample": False},
        {"input": '["NumArray", "update", "sumRange"]\n[[10], [0, 5], [0, 0]]', "expected_output": "[null, null, 5]", "is_sample": False},
        {"input": '["NumArray", "sumRange", "update", "sumRange", "update", "sumRange"]\n[[1, 1, 1, 1], [0, 3], [0, 2], [0, 3], [3, 0], [0, 3]]', "expected_output": "[null, 4, null, 5, null, 4]", "is_sample": False},
        {"input": '["NumArray", "sumRange"]\n[[[1,2,3,4,5]], [1, 3]]', "expected_output": "[null, 9]", "is_sample": False},
        {"input": '["NumArray", "update", "sumRange"]\n[[[1,2,3]], [1, 5], [0, 2]]', "expected_output": "[null, null, 9]", "is_sample": False},
        {"input": '["NumArray", "sumRange"]\n[[[100]], [0, 0]]', "expected_output": "[null, 100]", "is_sample": False},
        {"input": '["NumArray", "update", "update", "sumRange"]\n[[[5,2,8,4]], [0, 1], [3, 2], [0, 3]]', "expected_output": "[null, null, null, 13]", "is_sample": False},
        {"input": '["NumArray", "sumRange", "sumRange"]\n[[[1,2,3,4,5]], [0, 0], [4, 4]]', "expected_output": "[null, 1, 5]", "is_sample": False},
        {"input": '["NumArray", "update", "sumRange"]\n[[[-1,-2,-3]], [0, 1], [0, 2]]', "expected_output": "[null, null, -4]", "is_sample": False}
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
        "topics": ["Array", "Binary Indexed Tree", "Segment Tree"],
        "companyIndex": 0
    }

    output_path = "201-400/307_Range_Sum_Query_Mutable.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
