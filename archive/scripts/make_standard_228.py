import json
import os

def generate_json():
    problem_id = 228
    title = "Summary Ranges"
    difficulty = "EASY"
    marks = 5
    
    html_description = """<h3>228. Summary Ranges</h3>
<p>You are given a <strong>sorted unique</strong> integer array <code>nums</code>.</p>

<p>A <strong>range</strong> <code>[a,b]</code> is the set of all integers from <code>a</code> to <code>b</code> (inclusive).</p>

<p>Return <em>the <strong>smallest sorted</strong> list of ranges that <strong>cover all the numbers in the array exactly</strong></em>. That is, each element of <code>nums</code> is covered by exactly one of the ranges, and there is no integer <code>x</code> such that <code>x</code> is in one of the ranges but not in <code>nums</code>.</p>

<p>Each range <code>[a,b]</code> in the list should be output as:</p>

<ul>
	<li><code>"a-&gt;b"</code> if <code>a != b</code></li>
	<li><code>"a"</code> if <code>a == b</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,2,4,5,7]
<strong>Output:</strong> ["0-&gt;2","4-&gt;5","7"]
<strong>Explanation:</strong> The ranges are:
[0,2] --&gt; "0-&gt;2"
[4,5] --&gt; "4-&gt;5"
[7,7] --&gt; "7"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,2,3,4,6,8,9]
<strong>Output:</strong> ["0","2-&gt;4","6","8-&gt;9"]
<strong>Explanation:</strong> The ranges are:
[0,0] --&gt; "0"
[2,4] --&gt; "2-&gt;4"
[6,6] --&gt; "6"
[8,9] --&gt; "8-&gt;9"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 20</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>All the values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>"""

    input_format = "A stringified 1D array of integers."
    output_format = "A stringified array of range strings."
    
    constraints = [
        "nums.length <= 20 (Note: LeetCode official is larger, but let's stick to user request's scope if provided, or standard 10^4)",
        "Sorted unique integers.",
        "Output format: 'a->b' or 'a'."
    ]
    
    # Note: LeetCode official constraints are usually around 10^4 for this. 
    # I'll use 10^4 for stress tests but mention 20 as per the example text if needed.
    
    explanation = """To summarize ranges in a sorted unique array:
1. **Iteration**: Loop through the array while maintaining a `start` pointer for the current range.
2. **Logic**:
   - For each element at index `i`, check if `nums[i+1]` is equal to `nums[i] + 1`.
   - If not, the current range `[nums[start], nums[i]]` ends.
   - Format the range: if `start == i` use `"start"`, else `"start->i"`.
3. **Complexity**:
   - Time: O(N) where N is the length of the array.
   - Space: O(1) beyond the output list."""
    
    answer = """class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")
            i += 1
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef summaryRanges(nums):\n    # User logic\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if not data: sys.exit()\n    print(json.dumps(summaryRanges(json.loads(data))))",
        "cpp": "vector<string> summaryRanges(vector<int>& nums) { /* logic */ return {}; }",
        "java": "public List<String> summaryRanges(int[] nums) { /* logic */ return null; }",
        "javascript": "var summaryRanges = function(nums) { /* logic */ };",
        "c": "char ** summaryRanges(int* nums, int numsSize, int* returnSize) { /* logic */ return NULL; }"
    }

    test_cases = [
        {"input": "[0,1,2,4,5,7]", "expected_output": '["0->2", "4->5", "7"]', "is_sample": True},
        {"input": "[0,2,3,4,6,8,9]", "expected_output": '["0", "2->4", "6", "8->9"]', "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[-1]", "expected_output": '["-1"]', "is_sample": False},
        {"input": "[-2147483648, -2147483647, 2147483647]", "expected_output": '["-2147483648->-2147483647", "2147483647"]', "is_sample": False},
        {"input": "[1,3,5,7,9]", "expected_output": '["1", "3", "5", "7", "9"]', "is_sample": False},
        {"input": "[1,2,3,4,5]", "expected_output": '["1->5"]', "is_sample": False},
        # Stress Tests (Up to 10^4)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_sr(nums):
        if not nums: return []
        res = []
        i = 0
        while i < len(nums):
            s = nums[i]
            while i+1 < len(nums) and nums[i+1] == nums[i]+1: i += 1
            res.append(str(s) if s == nums[i] else f"{s}->{nums[i]}")
            i += 1
        return res

    # Stress 8: 10,000 contiguous
    n8 = list(range(10000))
    test_cases[7] = {"input": json.dumps(n8), "expected_output": json.dumps(_solve_sr(n8)), "is_sample": False}
    # Stress 9: 10,000 isolated
    n9 = [i*2 for i in range(10000)]
    test_cases[8] = {"input": json.dumps(n9), "expected_output": json.dumps(_solve_sr(n9)), "is_sample": False}
    # Stress 10: 10,000 random bursts
    n10 = []
    curr = 0
    import random
    random.seed(42)
    for _ in range(500):
        burst = random.randint(1, 20)
        n10.extend(list(range(curr, curr + burst)))
        curr += burst + random.randint(2, 5)
    test_cases[9] = {"input": json.dumps(n10), "expected_output": json.dumps(_solve_sr(n10)), "is_sample": False}

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
        "topics": ["Array"],
        "companyIndex": 0
    }

    output_path = "201-400/228_Summary_Ranges.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
