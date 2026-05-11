import json
import os

def generate_json():
    problem_id = 66
    title = "Plus One"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>66. Plus One</h3>
<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>'s, except for the number <code>0</code> itself.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>'s, except for the number <code>0</code> itself.</li>
</ul>"""

    input_format = "A single line containing space-separated digits."
    output_format = "A list of digits representing the incremented number."
    
    constraints = [
        "1 <= digits.length <= 100",
        "0 <= digits[i] <= 9",
        "No leading zeros except for '0' itself."
    ]
    
    explanation = """To increment a number represented as an array of digits:
1. **Traverse from Right to Left**: Start at the last digit (the least significant one).
2. **Handle Non-Carry Case**: If the current digit is less than 9, simply increment it by 1 and return the updated array.
3. **Handle Carry Case**: If the digit is 9, it becomes 0, and a carry of 1 moves to the next digit on the left.
4. **Handle overflow**: If the loop finishes and all digits were 9 (e.g., 999 -> 1000), the entire array will be zeros. In this case, prepend 1 to the array (e.g., `[1] + [0,0,0]`).
5. **Complexity**:
   - Time Complexity: O(n) where n is the number of digits.
   - Space Complexity: O(n) for the result (in Python, returning a list), but technically O(1) additional space if modified in-place."""
    
    answer = """def plusOne(digits):
    n = len(digits)
    # Loop from the end of the list to the beginning
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            # If the digit is not 9, increment and return early
            digits[i] += 1
            return digits
        # If the digit is 9, it becomes 0 and the carry continues
        digits[i] = 0
        
    # If all digits were 9, we need an extra 1 at the beginning
    return [1] + digits"""

    boilerplate = {
        "python": "import sys\n\ndef plusOne(digits):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        digits = [int(x) for x in data]\n        print(plusOne(digits))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvector<int> plusOne(vector<int>& digits) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int val;\n    vector<int> digits;\n    while (cin >> val) digits.push_back(val);\n    vector<int> res = plusOne(digits);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << res[i];\n        if (i + 1 < (int)res.size()) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int[] plusOne(int[] digits) {\n        // User logic\n        return new int[0];\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] digits = list.stream().mapToInt(i -> i).toArray();\n        int[] res = plusOne(digits);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.length; i++) {\n            sb.append(res[i]);\n            if (i + 1 < res.length) sb.append(\", \");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction plusOne(digits) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nconst res = plusOne(input);\nconsole.log('[' + res.join(', ') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint* plusOne(int* digits, int digitsSize, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int buff[101], size = 0;\n    while (size < 101 && scanf(\"%d\", &buff[size]) == 1) size++;\n    int returnSize = 0;\n    int* res = plusOne(buff, size, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"%d\", res[i]);\n        if (i + 1 < returnSize) printf(\", \");\n    }\n    printf(\"]\\n\");\n    if (res) free(res);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 2 3", "expected_output": "[1, 2, 4]", "is_sample": True},
        {"input": "4 3 2 1", "expected_output": "[4, 3, 2, 2]", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "9", "expected_output": "[1, 0]", "is_sample": False},
        {"input": "0", "expected_output": "[1]", "is_sample": False},
        {"input": "9 9 9", "expected_output": "[1, 0, 0, 0]", "is_sample": False},
        {"input": "1 9 9", "expected_output": "[2, 0, 0]", "is_sample": False},
        {"input": "8 9 9 9", "expected_output": "[9, 0, 0, 0]", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["9"] * 100), "expected_output": str([1] + [0] * 100), "is_sample": False},
        {"input": " ".join(["0"]), "expected_output": "[1]", "is_sample": False},
        {"input": "1 " + " ".join(["0"] * 98) + " 8", "expected_output": str([1] + [0] * 98 + [9]), "is_sample": False}
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

    output_path = "1-200/66_Plus_One.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
