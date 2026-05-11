import json
import os

def generate_json():
    problem_id = 371
    title = "Sum of Two Integers"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>371. Sum of Two Integers</h3>
<p>Given two integers <code>a</code> and <code>b</code>, return <em>the sum of the two integers without using the operators</em> <code>+</code> <em>and</em> <code>-</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = 1, b = 2
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = 2, b = 3
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-1000 &lt;= a, b &lt;= 1000</code></li>
</ul>"""

    input_format = "Two integers `a` and `b`."
    output_format = "An integer representing the sum."
    
    constraints = [
        "-1000 <= a, b <= 1000"
    ]
    
    explanation = """To add two integers without using the `+` or `-` operators, we use **Bit Manipulation**.

### Key Concept:
- **Sum without Carry**: Use XOR (`^`). $0+0=0, 0+1=1, 1+0=1, 1+1=0$. This is equivalent to bitwise addition without carrying.
- **Carry**: Use AND (`&`) and shift left (`<< 1`). $1+1=2$ ($10$ in binary). The carry appears only when both bits are 1.

### Algorithm Steps:
1. **Initialize**: Loop while `b != 0` (no more carry).
2. **Calculate Carry**: `carry = (a & b) << 1`.
3. **Calculate Sum (without carry)**: `a = a ^ b`.
4. **Update Carry**: `b = carry`.
5. **Python Handling (Negative Numbers)**:
   - Python integers are arbitrary precision. Negative numbers are represented using two's complement with infinite leading ones.
   - We must mask with `0xFFFFFFFF` to simulate 32-bit behavior and then check for negative overflow manually.

### Complexity Analysis:
- **Time Complexity**: $O(1)$, because the number of bits is fixed (32-bit).
- **Space Complexity**: $O(1)$."""
    
    answer = """class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b != 0:
            # XOR to add without carry
            # AND + shift to get the carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # If a is negative in 32-bit space, convert it back to Python's int representation
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def getSum(self, a: int, b: int) -> int:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        a = data['a']\n        b = data['b']\n        sol = Solution()\n        print(json.dumps(sol.getSum(a, b)))",
        "cpp": "class Solution {\npublic:\n    int getSum(int a, int b) {\n        // Your logic here\n        return 0;\n    }\n};",
        "java": "public class Solution {\n    public int getSum(int a, int b) {\n        // Your logic here\n        return 0;\n    }\n}",
        "javascript": "/**\n * @param {number} a\n * @param {number} b\n * @return {number}\n */\nvar getSum = function(a, b) {\n    // Your logic here\n};",
        "c": "int getSum(int a, int b) {\n    // Your logic here\n    return 0;\n}"
    }

    test_cases = [
        {"input": '{"a": 1, "b": 2}', "expected_output": "3", "is_sample": True},
        {"input": '{"a": 2, "b": 3}', "expected_output": "5", "is_sample": True},
        {"input": '{"a": 0, "b": 0}', "expected_output": "0", "is_sample": False},
        {"input": '{"a": -1, "b": 1}', "expected_output": "0", "is_sample": False},
        {"input": '{"a": -2, "b": -3}', "expected_output": "-5", "is_sample": False},
        {"input": '{"a": 100, "b": -10}', "expected_output": "90", "is_sample": False},
        {"input": '{"a": 1000, "b": 1000}', "expected_output": "2000", "is_sample": False},
        {"input": '{"a": -1000, "b": -1000}', "expected_output": "-2000", "is_sample": False},
        # Extreme cases
        {"input": '{"a": 2147483647, "b": -2147483648}', "expected_output": "-1", "is_sample": False},
        {"input": '{"a": 1, "b": -1}', "expected_output": "0", "is_sample": False}
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
        "companyIndex": 1
    }

    output_path = "301-500/371_Sum_of_Two_Integers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
