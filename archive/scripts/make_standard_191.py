import json
import os

def generate_json():
    problem_id = 191
    title = "Number of 1 Bits"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>191. Number of 1 Bits</h3>
<p>Write a function that takes the binary representation of a positive integer and returns the number of <strong>set bits</strong> it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> The input binary string <strong>1011</strong> has a total of three set bits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 128
<strong>Output:</strong> 1
<strong>Explanation:</strong> The input binary string <strong>10000000</strong> has a total of one set bit.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2147483645
<strong>Output:</strong> 30
<strong>Explanation:</strong> The input binary string <strong>1111111111111111111111111111101</strong> has a total of thirty set bits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If this function is called many times, how would you optimize it?
"""

    input_format = "A single positive integer."
    output_format = "An integer representing the count of set bits."
    
    constraints = [
        "1 <= n <= 2^31 - 1"
    ]
    
    explanation = """To count the number of set bits (1 bits) in a 32-bit integer:
1. **Brian Kernighan's Algorithm**:
   - The expression `n & (n - 1)` clears the least significant set bit in `n`.
   - By repeatedly applying this until `n` becomes 0, we can count the number of set bits.
2. **Logic**:
   - Initialize `count = 0`.
   - While `n > 0`:
     - `n = n & (n - 1)`
     - `count += 1`
   - Return `count`.
3. **Complexity**:
   - Time Complexity: O(K), where K is the number of set bits (at most 32). This is faster than checking all 32 bits one by one.
   - Space Complexity: O(1)."""
    
    answer = """def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count"""

    boilerplate = {
        "python": "import sys\n\ndef hammingWeight(n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(hammingWeight(int(line)))",
        "cpp": "#include <iostream>\n#include <cstdint>\n\nusing namespace std;\n\nint hammingWeight(uint32_t n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    uint32_t n;\n    if (cin >> n) {\n        cout << hammingWeight(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int hammingWeight(int n) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            long n = Long.parseLong(line.trim());\n            System.out.println(new Solution().hammingWeight((int)n));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction hammingWeight(n) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input !== '') {\n    console.log(hammingWeight(parseInt(input)));\n}",
        "c": "#include <stdio.h>\n#include <stdint.h>\n\nint hammingWeight(uint32_t n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    uint32_t n;\n    if (scanf(\"%u\", &n) == 1) {\n        printf(\"%d\\n\", hammingWeight(n));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "11", "expected_output": "3", "is_sample": True},
        {"input": "128", "expected_output": "1", "is_sample": True},
        {"input": "2147483645", "expected_output": "30", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "2", "expected_output": "1", "is_sample": False},
        {"input": "3", "expected_output": "2", "is_sample": False},
        {"input": "15", "expected_output": "4", "is_sample": False},
        # Stress cases
        {"input": "2147483647", "expected_output": "31", "is_sample": False},
        {"input": "1048576", "expected_output": "1", "is_sample": False},
        {"input": "16777215", "expected_output": "24", "is_sample": False}
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
        "topics": ["Binary", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/191_Number_of_1_Bits.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
