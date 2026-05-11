import json
import os

def generate_json():
    problem_id = 201
    title = "Bitwise AND of Numbers Range"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>201. Bitwise AND of Numbers Range</h3>
<p>Given two integers <code>left</code> and <code>right</code> that represent the range <code>[left, right]</code>, return <em>the bitwise AND of all numbers in this range, inclusive</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 5, right = 7
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 0, right = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> left = 1, right = 2147483647
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= left &lt;= right &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "Two integers left and right representing the range [left, right]."
    output_format = "An integer representing the bitwise AND of all numbers in the range."
    
    constraints = [
        "0 <= left <= right <= 2^31 - 1",
        "O(1) time complexity expected (per bit)."
    ]
    
    explanation = """To find the bitwise AND of all numbers in the range `[left, right]`:
1. **Identify the Common Prefix**:
   - The bitwise AND of a range follows a specific pattern: any bit that changes within the range will eventually become '0' in the final result.
   - Therefore, the result of the bitwise AND is simply the **common prefix** of the binary representations of `left` and `right`.
2. **Algorithm**:
   - While `left < right`:
     - Right shift both `left` and `right` by 1 (`left >>= 1`, `right >>= 1`).
     - Keep track of how many times you shifted (`shift_count`).
   - Once `left == right`, they represent the common prefix.
   - Shift the common prefix back to the left by `shift_count` to get the final result.
3. **Complexity**:
   - Time Complexity: O(1) because an integer has at most 32 bits.
   - Space Complexity: O(1)."""
    
    answer = """def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift"""

    boilerplate = {
        "python": "import sys\n\ndef rangeBitwiseAnd(left, right):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if len(data) >= 2:\n        print(rangeBitwiseAnd(int(data[0]), int(data[1])))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint rangeBitwiseAnd(int left, int right) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int l, r;\n    if (cin >> l >> r) {\n        cout << rangeBitwiseAnd(l, r) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int rangeBitwiseAnd(int left, int right) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            String[] parts = line.trim().split(\"\\\\s+\");\n            if (parts.length >= 2) {\n                int l = Integer.parseInt(parts[0]);\n                int r = Integer.parseInt(parts[1]);\n                System.out.println(new Solution().rangeBitwiseAnd(l, r));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction rangeBitwiseAnd(left, right) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\\\s+/);\nif (input.length >= 2) {\n    console.log(rangeBitwiseAnd(parseInt(input[0]), parseInt(input[1])));\n}",
        "c": "#include <stdio.h>\n\nint rangeBitwiseAnd(int left, int right) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int l, r;\n    if (scanf(\"%d %d\", &l, &r) == 2) {\n        printf(\"%d\\n\", rangeBitwiseAnd(l, r));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5 7", "expected_output": "4", "is_sample": True},
        {"input": "0 0", "expected_output": "0", "is_sample": True},
        {"input": "1 2147483647", "expected_output": "0", "is_sample": True},
        {"input": "10 11", "expected_output": "10", "is_sample": False},
        {"input": "1 5", "expected_output": "0", "is_sample": False},
        {"input": "16 23", "expected_output": "16", "is_sample": False},
        {"input": "20 20", "expected_output": "20", "is_sample": False},
        # Stress cases
        {"input": "2147483646 2147483647", "expected_output": "2147483646", "is_sample": False},
        {"input": "600000000 700000000", "expected_output": str(600000000 & 700000000), "is_sample": False},
        {"input": "0 2147483647", "expected_output": "0", "is_sample": False}
    ]
    
    # Correcting stress case 9 expected output
    def _solve(l, r):
        s = 0
        while l < r:
            l >>= 1
            r >>= 1
            s += 1
        return l << s
    test_cases[8]["expected_output"] = str(_solve(600000000, 700000000))

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
        "topics": ["Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/201_Bitwise_AND_of_Numbers_Range.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
