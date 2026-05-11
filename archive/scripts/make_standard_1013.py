import json
import os

def generate_json():
    problem_id = 1013
    title = "Partition Array Into Three Parts With Equal Sum"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1013. Partition Array Into Three Parts With Equal Sum</h3>
<p>Given an array of integers <code>arr</code>, return <code>true</code> if we can partition the array into three <strong>non-empty</strong> parts with equal sums.</p>

<p>Formally, we can partition the array if we can find indices <code>i + 1 &lt; j</code> such that <code>(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> arr = [0,2,1,-6,6,-7,9,1,2,0,1]
<strong>Output:</strong> true
<strong>Explanation: </strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> arr = [0,2,1,-6,6,7,9,-1,2,0,1]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> arr = [3,3,6,5,-2,2,5,1,-9,4]
<strong>Output:</strong> true
<strong>Explanation: </strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the array arr."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "3 <= arr.length <= 50,000",
        "-10,000 <= arr[i] <= 10,000",
        "O(N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To determine if an array can be partitioned into three equal-sum parts:
1. **The Insight (Target Sum)**:
   - If the total sum of the array is `S`, each of the three parts must have a sum of `T = S / 3`.
   - If `S % 3 != 0`, it is impossible; return `false`.
2. **Algorithm Strategy**:
   - Calculate the total `sum(arr)`.
   - If it's not divisible by 3, return `false`.
   - Let `target = total_sum // 3`.
   - Iterate through the array once while maintaining a `current_sum`.
   - Every time `current_sum` reaches `target`, increment a `count` and reset `current_sum`.
   - Crucially, even if we find more than 3 parts that sum to `target` (possible if `target == 0`), it still means we can partition it into exactly three parts.
3. **Conclusion**:
   - Return `true` if `count >= 3`, which effectively means we found at least two split points that leave a third part with the correct sum.
4. **Complexity**:
   - Time Complexity: O(N) as we traverse the array twice (once for sum, once for partitioning).
   - Space Complexity: O(1)."""
    
    answer = """def canThreePartsEqualSum(arr: list[int]) -> bool:
    total = sum(arr)
    if total % 3 != 0:
        return False
        
    target = total // 3
    count = 0
    current_sum = 0
    
    # We only need to find 3 parts. 
    # For target=0, we might find more than 3 parts, but that still works.
    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == target:
            count += 1
            current_sum = 0
            
    return count >= 3"""

    boilerplate = {
        "python": "import sys\n\ndef canThreePartsEqualSum(arr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        arr = list(map(int, line.split()))\n        print('true' if canThreePartsEqualSum(arr) else 'false')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <numeric>\n\nusing namespace std;\n\nbool canThreePartsEqualSum(vector<int>& arr) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean canThreePartsEqualSum(int[] arr) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function canThreePartsEqualSum(arr) {\n    // User logic\n}",
        "c": "bool canThreePartsEqualSum(int* arr, int arrSize) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "0 2 1 -6 6 -7 9 1 2 0 1", "expected_output": "true", "is_sample": True},
        {"input": "0 2 1 -6 6 7 9 -1 2 0 1", "expected_output": "false", "is_sample": True},
        {"input": "3 3 6 5 -2 2 5 1 -9 4", "expected_output": "true", "is_sample": True},
        {"input": "1 1 1", "expected_output": "true", "is_sample": False},
        {"input": "1 -1 1 -1 1 -1", "expected_output": "true", "is_sample": False},
        {"input": "10 -10 10 -10 10 -10", "expected_output": "true", "is_sample": False},
        {"input": "1 1 1 1", "expected_output": "false", "is_sample": False},
        {"input": "0 0 0 0", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": " ".join(["1"] * 30000), "expected_output": "true", "is_sample": False},
        {"input": " ".join(["1"] * 50000), "expected_output": "false", "is_sample": False}
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
        "topics": ["Array", "Greedy"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1013_Partition_Array_Into_Three_Parts_With_Equal_Sum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
