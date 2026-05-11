import json
import os

def generate_json():
    problem_id = 1009
    title = "Complement of Base 10 Integer"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1009. Complement of Base 10 Integer</h3>
<p>The <strong>complement</strong> of an integer is the integer you get when you flip all the <code>0</code>'s to <code>1</code>'s and all the <code>1</code>'s to <code>0</code>'s in its binary representation.</p>

<ul>
	<li>For example, The integer <code>5</code> is <code>"101"</code> in binary and its <strong>complement</strong> is <code>"010"</code> which is the integer <code>2</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>its complement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 0
<strong>Explanation:</strong> 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 5
<strong>Explanation:</strong> 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt; 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This problem is identical to 476: <a href="https://leetcode.com/problems/number-complement/" target="_blank">https://leetcode.com/problems/number-complement/</a>"""

    input_format = "A single line containing an integer n."
    output_format = "An integer representing the bitwise complement."
    
    constraints = [
        "0 <= n < 10^9",
        "O(log N) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To find the complement of an integer in binary:
1. **The Insight (Bit Masking)**:
   - Flipping all bits in `n` is equivalent to calculating `n XOR mask`, where `mask` is a number with all bits set (all `1`s) and the same length as the binary representation of `n`.
   - For example, if `n = 5 (101)`, then `mask = 7 (111)`. `5 ^ 7 = 2 (010)`.
2. **Algorithm Strategy**:
   - Handle the edge case `n = 0` (complement is `1`).
   - For `n > 0`, find the largest power of 2 that is less than or equal to `n`. 
   - Construct a `mask` that is `2^h - 1` (where `h` is the smallest number of bits to represent `n`).
   - Return `n ^ mask`.
3. **Complexity**:
   - Time Complexity: O(log N) as we might iterate through or calculate the bit length.
   - Space Complexity: O(1)."""
    
    answer = """def bitwiseComplement(n: int) -> int:
    if n == 0: return 1
    # Create a mask of all 1s with the same length as n
    mask = 1
    while mask < n:
        mask = (mask << 1) | 1
        
    return n ^ mask"""

    boilerplate = {
        "python": "import sys\n\ndef bitwiseComplement(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        print(bitwiseComplement(int(line)))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint bitwiseComplement(int n) {\n    // User logic\n    return 0;\n}",
        "java": "public class Solution {\n    public int bitwiseComplement(int n) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function bitwiseComplement(n) {\n    // User logic\n}",
        "c": "int bitwiseComplement(int n) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5", "expected_output": "2", "is_sample": True},
        {"input": "7", "expected_output": "0", "is_sample": True},
        {"input": "10", "expected_output": "5", "is_sample": True},
        {"input": "0", "expected_output": "1", "is_sample": False},
        {"input": "1", "expected_output": "0", "is_sample": False},
        {"input": "2", "expected_output": "1", "is_sample": False},
        {"input": "16", "expected_output": "15", "is_sample": False},
        {"input": "1000", "expected_output": "23", "is_sample": False},
        # Stress cases
        {"input": "999999999", "expected_output": "73741824", "is_sample": False},
        {"input": "1000000000", "expected_output": "73741823", "is_sample": False}
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
        "topics": ["Math", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1009_Complement_of_Base_10_Integer.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
