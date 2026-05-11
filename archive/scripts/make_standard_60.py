import json
import os
import math

def generate_json():
    problem_id = 60
    title = "Permutation Sequence"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>60. Permutation Sequence</h3>
<p>The set <code>[1, 2, 3, ..., n]</code> contains a total of <code>n!</code> unique permutations.</p>

<p>By listing and labeling all of the permutations in order, we get the following sequence for <code>n = 3</code>:</p>

<ol>
	<li><code>"123"</code></li>
	<li><code>"132"</code></li>
	<li><code>"213"</code></li>
	<li><code>"231"</code></li>
	<li><code>"312"</code></li>
	<li><code>"321"</code></li>
</ol>

<p>Given <code>n</code> and <code>k</code>, return the <code>k<sup>th</sup></code> permutation sequence.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 3
<strong>Output:</strong> "213"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 4, k = 9
<strong>Output:</strong> "2314"
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "123"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
	<li><code>1 &lt;= k &lt;= n!</code></li>
</ul>"""

    input_format = "Two space-separated integers 'n' and 'k'."
    output_format = "A string representing the k-th permutation sequence."
    
    constraints = [
        "1 <= n <= 9",
        "1 <= k <= n!"
    ]
    
    explanation = """To find the k-th permutation sequence without generating all permutations:
1. **Factorial System**: There are `n!` total permutations. If we fix the first digit, there are `(n-1)!` permutations for the remaining `n-1` positions.
2. **Mathematical Selection**:
   - Convert `k` to 0-indexed: `k = k - 1`.
   - Maintain a list of available numbers: `[1, 2, ..., n]`.
   - For each position from left to right (using `i` from `n-1` down to `0`):
     - Calculate the factorial of the current group size: `fact = (i)!`.
     - The index of the number to pick from the available list is `idx = k // fact`.
     - Append `numbers[idx]` to the result and remove it from the list.
     - Update `k` for the next position: `k = k % fact`.
3. **Example (n=3, k=3)**:
   - numbers = [1, 2, 3], k = 2 (0-indexed).
   - i = 2: fact = 2! = 2. idx = 2 // 2 = 1. Pick numbers[1] = '2'. res = "2". numbers = [1, 3], k = 2 % 2 = 0.
   - i = 1: fact = 1! = 1. idx = 0 // 1 = 0. Pick numbers[0] = '1'. res = "21". numbers = [3], k = 0 % 1 = 0.
   - i = 0: fact = 0! = 1. idx = 0 // 1 = 0. Pick numbers[0] = '3'. res = "213".
4. **Complexity**:
   - Time Complexity: O(n^2) because we iterate `n` times and potentially remove an element from a list in each step (which is O(n)).
   - Space Complexity: O(n) to store the result and the list of numbers."""
    
    answer = """import math

def getPermutation(n, k):
    # Create a list of numbers to use
    numbers = [str(i) for i in range(1, n + 1)]
    # Convert k to 0-indexed
    k -= 1
    res = []
    
    # Pre-calculate factorial of (n-1)
    fact = math.factorial(n - 1)
    
    for i in range(n - 1, -1, -1):
        # Calculate index of the next number
        idx = k // fact
        res.append(numbers.pop(idx))
        
        # Update k
        k %= fact
        
        # Update factorial for the next iteration (n-2), (n-3)...
        if i > 0:
            fact //= i
            
    return \"\".join(res)"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\nimport math\n\ndef getPermutation(n, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip().split()\n    if len(data) >= 2:\n        n = int(data[0])\n        k = int(data[1])\n        print(getPermutation(n, k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <numeric>\n\nusing namespace std;\n\nstring getPermutation(int n, int k) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    int n, k;\n    if (cin >> n >> k) {\n        cout << getPermutation(n, k) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String getPermutation(int n, int k) {\n        // User logic\n        return \"\";\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            int k = sc.nextInt();\n            System.out.println(getPermutation(n, k));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction getPermutation(n, k) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/).map(Number);\nif (input.length >= 2) {\n    console.log(getPermutation(input[0], input[1]));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* getPermutation(int n, int k) {\n    // User logic here\n    char* result = (char*)malloc(n + 1);\n    result[0] = '\\0';\n    return result;\n}\n\nint main() {\n    int n, k;\n    if (scanf(\"%d %d\", &n, &k) == 2) {\n        char* res = getPermutation(n, k);\n        printf(\"%s\\n\", res);\n        free(res);\n    }\n    return 0;\n}"
    }

    def _get_p(n, k):
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        res = []
        fact = math.factorial(n-1)
        for i in range(n-1, -1, -1):
            idx = k // fact
            res.append(nums.pop(idx))
            k %= fact
            if i > 0: fact //= i
        return "".join(res)

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "3 3", "expected_output": "213", "is_sample": True},
        {"input": "4 9", "expected_output": "2314", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "3 1", "expected_output": "123", "is_sample": False},
        {"input": "1 1", "expected_output": "1", "is_sample": False},
        {"input": "2 1", "expected_output": "12", "is_sample": False},
        {"input": "2 2", "expected_output": "21", "is_sample": False},
        {"input": "9 1", "expected_output": "123456789", "is_sample": False},
        # Last three: Stress tests
        {"input": "9 362880", "expected_output": "987654321", "is_sample": False},
        {"input": "9 181440", "expected_output": "549876321", "is_sample": False},
        {"input": "9 40321", "expected_output": "213456789", "is_sample": False}
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
        "topics": ["Math", "Recursion"],
        "companyIndex": 0
    }

    output_path = "1-200/60_Permutation_Sequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
