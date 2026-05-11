import json
import os

def generate_json():
    problem_id = 27
    title = "Remove Element"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>27. Remove Element</h3>
<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong>. The order of the elements may be changed. Then return <em>the number of elements in </em><code>nums</code><em> which are not equal to </em><code>val</code>.</p>

<p>Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>
<p>The judge will test your solution with the following code:</p>
<pre>
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equal to val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>"""

    input_format = "An array of integers nums and an integer val."
    output_format = "The number of elements not equal to val (k)."
    
    constraints = [
        "0 <= nums.length <= 100",
        "0 <= nums[i] <= 50",
        "0 <= val <= 100"
    ]
    
    explanation = """To remove elements in-place:
1. **Two Pointers**: Use a pointer `k` to track the position where the next "valid" element should be placed.
2. **Iteration**: Iterate through the array with a pointer `i`.
3. **Condition**: If `nums[i] != val`:
   - Assign `nums[k] = nums[i]`.
   - Increment `k`.
4. **Return**: The value of `k` at the end is the count of elements not equal to `val`.
5. **Complexity**:
   - **Time**: $O(N)$
   - **Space**: $O(1)$."""
    
    answer = """def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k"""

    boilerplate = {
        "python": "import sys, json\n\ndef removeElement(nums, val):\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    data = json.loads(sys.stdin.read())\n    print(removeElement(data['nums'], data['val']))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int removeElement(vector<int>& nums, int val) {\n        // implementation\n        return 0;\n    }\n};",
        "java": "class Solution {\n    public int removeElement(int[] nums, int val) {\n        // implementation\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums\n * @param {number} val\n * @return {number}\n */\nvar removeElement = function(nums, val) {\n    \n};",
        "c": "int removeElement(int* nums, int numsSize, int val){\n    \n}"
    }

    test_cases = [
        {"input": '{"nums": [3,2,2,3], "val": 3}', "expected_output": "2", "is_sample": True},
        {"input": '{"nums": [0,1,2,2,3,0,4,2], "val": 2}', "expected_output": "5", "is_sample": True},
        {"input": '{"nums": [], "val": 0}', "expected_output": "0", "is_sample": False},
        {"input": '{"nums": [1], "val": 1}', "expected_output": "0", "is_sample": False},
        {"input": '{"nums": [1], "val": 2}', "expected_output": "1", "is_sample": False},
        {"input": '{"nums": [2,2,2], "val": 2}', "expected_output": "0", "is_sample": False},
        {"input": '{"nums": [3,3,3], "val": 2}', "expected_output": "3", "is_sample": False},
        {"input": '{"nums": [4,5], "val": 4}', "expected_output": "1", "is_sample": False},
        {"input": '{"nums": [1,2,3,4,5], "val": 3}', "expected_output": "4", "is_sample": False},
        {"input": '{"nums": [1,2,3,4,5], "val": 6}', "expected_output": "5", "is_sample": False}
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

    output_path = "1-100/27_Remove_Element.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
