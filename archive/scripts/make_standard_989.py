import json
import os

def generate_json():
    problem_id = 989
    title = "Add to Array-Form of Integer"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>989. Add to Array-Form of Integer</h3>
<p>The <strong>array-form</strong> of an integer <code>num</code> is an array representing its digits in left to right order.</p>

<ul>
	<li>For example, for <code>num = 1321</code>, the array form is <code>[1,3,2,1]</code>.</li>
</ul>

<p>Given <code>num</code>, the <strong>array-form</strong> of a non-negative integer, and an integer <code>k</code>, return <em>the <strong>array-form</strong> of the integer</em> <code>num + k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> num = [1,2,0,0], k = 34
<strong>Output:</strong> [1,2,3,4]
<strong>Explanation:</strong> 1200 + 34 = 1234
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> num = [2,7,4], k = 181
<strong>Output:</strong> [4,5,5]
<strong>Explanation:</strong> 274 + 181 = 455
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> num = [2,1,5], k = 806
<strong>Output:</strong> [1,0,2,1]
<strong>Explanation:</strong> 215 + 806 = 1021
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= num[i] &lt;= 9</code></li>
	<li><code>num</code> does not contain any leading zeros except for the zero itself.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for num. Line 2: integer k."
    output_format = "A single line containing space-separated integers for the resulting array form."
    
    constraints = [
        "1 <= num.length <= 10,000",
        "0 <= num[i] <= 9",
        "1 <= k <= 10,000",
        "O(max(N, log K)) time complexity.",
        "O(max(N, log K)) extra space for result."
    ]
    
    explanation = """To add an integer `k` to an array-form integer `num`:
1. **Schoolbook Addition**:
   - Start from the last digit of the array `num` (index `i = len(num) - 1`).
   - Add the current value of `k` to the digit at `num[i]`.
   - The new digit at this position will be `(num[i] + k) % 10`.
   - The carry for the next position will be contained in `k = (num[i] + k) // 10`.
   - Move to the previous index (`i -= 1`).
2. **Handle Remaining Carry**:
   - If the loop finishes but `k` is still greater than 0, it means there are more digits to add to the front (like `999 + 1 = 1000`).
   - Append the remaining digits of `k` to the result.
3. **Complexity**:
   - Time Complexity: O(max(N, log K)) where N is length of `num` and log K is number of digits in `k`.
   - Space Complexity: O(max(N, log K)) to store the resulting digits."""
    
    answer = """def addToArrayForm(num: list[int], k: int) -> list[int]:
    n = len(num)
    i = n - 1
    res = []
    
    # Process original digits and k
    while i >= 0 or k > 0:
        if i >= 0:
            k += num[i]
        res.append(k % 10)
        k //= 10
        i -= 1
        
    return res[::-1]"""

    boilerplate = {
        "python": "import sys\n\ndef addToArrayForm(num, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        num = list(map(int, lines[0].strip().split()))\n        k = int(lines[1].strip())\n        ans = addToArrayForm(num, k)\n        print(\" \".join(map(str, ans)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nvector<int> addToArrayForm(vector<int>& num, int k) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<Integer> addToArrayForm(int[] num, int k) {\n        // User logic\n        return new ArrayList<>();\n    }\n}",
        "javascript": "function addToArrayForm(num, k) {\n    // User logic\n}",
        "c": "int* addToArrayForm(int* num, int numSize, int k, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "1 2 0 0\\n34", "expected_output": "1 2 3 4", "is_sample": True},
        {"input": "2 7 4\\n181", "expected_output": "4 5 5", "is_sample": True},
        {"input": "2 1 5\\n806", "expected_output": "1 0 2 1", "is_sample": True},
        {"input": "0\\n23", "expected_output": "2 3", "is_sample": False},
        {"input": "9 9 9\\n1", "expected_output": "1 0 0 0", "is_sample": False},
        {"input": "1\\n9999", "expected_output": "1 0 0 0 0", "is_sample": False},
        {"input": "1 2 3\\n0", "expected_output": "1 2 3", "is_sample": False},
        {"input": "9 8 7 6\\n1234", "expected_output": "1 1 1 1 0", "is_sample": False},
        # Stress cases
        {"input": " ".join(["9"] * 10000) + "\\n1", "expected_output": "1 " + " ".join(["0"] * 10000), "is_sample": False},
        {"input": "1\\n10000", "expected_output": "1 0 0 0 1", "is_sample": False}
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
        "topics": ["Array", "Math"],
        "companyIndex": 0
    }

    output_path = "801-1000/989_Add_to_Array-Form_of_Integer.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
