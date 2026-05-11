import json
import os

def generate_json():
    problem_id = 556
    title = "Next Greater Element III"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>556. Next Greater Element III</h3>
<p>Given a positive integer <code>n</code>, find the smallest integer which has exactly the same digits existing in the integer <code>n</code> and is greater in prefix than <code>n</code>. If no such positive integer exists, return <code>-1</code>.</p>

<p><b>Note</b> that the returned integer should fit in <b>32-bit integer</b>, if there is a valid answer but it does not fit in <b>32-bit integer</b>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 12
<strong>Output:</strong> 21
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 21
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A single positive integer n."
    output_format = "The smallest 32-bit integer greater than n with same digits, or -1."
    
    constraints = [
        "1 <= n <= 2^31 - 1",
        "Must fit in 32-bit signed integer.",
        "O(L) time complexity (L = digits in n).",
        "O(L) extra space."
    ]
    
    explanation = """To find the next greater integer using the same digits (Next Permutation algorithm):
1. **Convert to Digits**: Convert the number $n$ into a list of its digits.
2. **Find the Pivot**:
   - Traverse from the right to find the first digit that is smaller than the digit to its immediate right: `nums[i] < nums[i+1]`.
   - If no such pair exists, the digits are in descending order, and no larger number can be formed. Return -1.
3. **Find the Successor**:
   - Find the smallest digit to the right of index $i$ that is larger than `nums[i]`.
4. **Swap and Reverse**:
   - Swap `nums[i]` with this successor.
   - Reverse the digits to the right of index $i$ to make the suffix as small as possible.
5. **Handle Overflow**:
   - Convert the digits back to an integer.
   - If the new integer exceeds $2^{31} - 1$, return -1.
6. **Complexity**:
   - Time Complexity: O(L) where L is the number of digits.
   - Space Complexity: O(L)."""
    
    answer = """def nextGreaterElement(n: int) -> int:
    s = list(str(n))
    m = len(s)
    
    # 1. Find pivot from right
    i = m - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
        
    if i == -1:
        return -1
        
    # 2. Find smallest successor
    j = m - 1
    while s[j] <= s[i]:
        j -= 1
        
    # 3. Swap
    s[i], s[j] = s[j], s[i]
    
    # 4. Reverse suffix
    s[i+1:] = sorted(s[i+1:])
    
    res = int("".join(s))
    return res if res <= 2**31 - 1 else -1"""

    boilerplate = {
        "python": "import sys\n\ndef nextGreaterElement(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(nextGreaterElement(int(line)))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nint nextGreaterElement(int n) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int nextGreaterElement(int n) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function nextGreaterElement(n) {\n    // User logic\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint nextGreaterElement(int n) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "12", "expected_output": "21", "is_sample": True},
        {"input": "21", "expected_output": "-1", "is_sample": True},
        {"input": "123", "expected_output": "132", "is_sample": False},
        {"input": "321", "expected_output": "-1", "is_sample": False},
        {"input": "1999999999", "expected_output": "-1", "is_sample": False},
        {"input": "230241", "expected_output": "230412", "is_sample": False},
        {"input": "101", "expected_output": "110", "is_sample": False},
        # Stress cases
        {"input": "123456789", "expected_output": "123456798", "is_sample": False},
        {"input": "2147483647", "expected_output": "-1", "is_sample": False},
        {"input": "11111", "expected_output": "-1", "is_sample": False}
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
        "topics": ["Two Pointers", "String", "Math"],
        "companyIndex": 0
    }

    output_path = "401-600/556_Next_Greater_Element_III.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
