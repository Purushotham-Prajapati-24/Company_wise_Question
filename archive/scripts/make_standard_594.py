import json
import os

def generate_json():
    problem_id = 594
    title = "Longest Harmonious Subsequence"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>594. Longest Harmonious Subsequence</h3>
<p>We define a harmonious array as an array where the difference between its maximum value and its minimum value is <b>exactly</b> <code>1</code>.</p>

<p>Given an integer array <code>nums</code>, return <em>the length of its longest harmonious subsequence among all its possible subsequences</em>.</p>

<p>A <b>subsequence</b> of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,2,5,2,3,7]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest harmonious subsequence is [3,2,2,2,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the array nums."
    output_format = "A single integer representing the length of the longest harmonious subsequence."
    
    constraints = [
        "1 <= nums.length <= 2 * 10^4",
        "-10^9 <= nums[i] <= 10^9",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To find the longest harmonious subsequence:
1. **The Core Property**:
   - A harmonious subsequence must consist of exactly two values, $x$ and $x+1$.
   - The length of such a subsequence is $Count(x) + Count(x+1)$.
2. **Hash Map Counter**:
   - Traverse the array once to count the frequency of each number using a hash map (or dictionary).
3. **Calculating Success**:
   - Iterate through the keys (numbers) in the frequency map.
   - For each number $x$, check if $x+1$ exists in the map.
   - If it exists, update the maximum length: $max\_len = max(max\_len, count[x] + count[x+1])$.
4. **Complexity**:
   - Time Complexity: O(N) as we traverse the array and then the keys of the map.
   - Space Complexity: O(N) to store frequencies."""
    
    answer = """from collections import Counter
def findLHS(nums: list[int]) -> int:
    count = Counter(nums)
    res = 0
    for x in count:
        if x + 1 in count:
            res = max(res, count[x] + count[x + 1])
    return res"""

    boilerplate = {
        "python": "import sys\nfrom collections import Counter\n\ndef findLHS(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(findLHS(nums))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nint findLHS(vector<int>& nums) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int findLHS(int[] nums) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function findLHS(nums) {\n    // User logic\n}",
        "c": "int findLHS(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3 2 2 5 2 3 7", "expected_output": "5", "is_sample": True},
        {"input": "1 2 3 4", "expected_output": "2", "is_sample": True},
        {"input": "1 1 1 1", "expected_output": "0", "is_sample": True},
        {"input": "1 2 1 3 0 0 2 2 1 3 3", "expected_output": "6", "is_sample": False},
        {"input": "-1 0 -1 0 1 1", "expected_output": "4", "is_sample": False},
        {"input": "1 5 10 15 20", "expected_output": "0", "is_sample": False},
        {"input": "1 2 2 2 3 3 3 4", "expected_output": "6", "is_sample": False},
        {"input": "10 11 12 13 14 15", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i%2) for i in range(20000)]), "expected_output": "20000", "is_sample": False},
        {"input": " ".join(["1"] * 10000 + ["2"] * 10000), "expected_output": "20000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(20000)]), "expected_output": "2", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sorting"],
        "companyIndex": 0
    }

    output_path = "401-600/594_Longest_Harmonious_Subsequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
