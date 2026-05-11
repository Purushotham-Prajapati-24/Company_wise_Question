import json
import os

def generate_json():
    problem_id = 204
    title = "Count Primes"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>204. Count Primes</h3>
<p>Given an integer <code>n</code>, return <em>the number of prime numbers that are strictly less than</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>"""

    input_format = "A single integer n."
    output_format = "An integer representing the count of primes strictly less than n."
    
    constraints = [
        "0 <= n <= 5 * 10^6",
        "O(N log log N) time complexity expected.",
        "O(N) space complexity expected."
    ]
    
    explanation = """To count primes strictly less than `n` efficiently:
1. **Sieve of Eratosthenes**:
   - Create a boolean array `isPrime` of size `n`, initialized to `True`.
   - Set `isPrime[0]` and `isPrime[1]` to `False` (0 and 1 are not prime).
2. **Logic**:
   - Iterate from `p = 2` up to `sqrt(n)`:
     - If `isPrime[p]` is `True`:
       - Mark all multiples of `p` starting from `p*p` as `False` (i.e., `isPrime[p*p], isPrime[p*p+p], ...`).
3. **Count**:
   - The number of `True` values remaining in the array is the count of primes.
4. **Complexity**:
   - Time Complexity: O(N log log N).
   - Space Complexity: O(N) to store the boolean array."""
    
    answer = """def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)"""

    boilerplate = {
        "python": "import sys\n\ndef countPrimes(n):\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        print(countPrimes(int(data)))",
        "cpp": "#include <iostream>\n\nusing namespace std;\n\nint countPrimes(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        cout << countPrimes(n) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int countPrimes(int n) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null && !line.trim().isEmpty()) {\n            int n = Integer.parseInt(line.trim());\n            System.out.println(new Solution().countPrimes(n));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction countPrimes(n) {\n    // User logic\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input !== '') {\n    console.log(countPrimes(parseInt(input)));\n}",
        "c": "#include <stdio.h>\n\nint countPrimes(int n) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        printf(\"%d\\n\", countPrimes(n));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "10", "expected_output": "4", "is_sample": True},
        {"input": "0", "expected_output": "0", "is_sample": True},
        {"input": "1", "expected_output": "0", "is_sample": True},
        {"input": "2", "expected_output": "0", "is_sample": False},
        {"input": "3", "expected_output": "1", "is_sample": False},
        {"input": "5", "expected_output": "2", "is_sample": False},
        {"input": "100", "expected_output": "25", "is_sample": False},
        # Stress cases
        {"input": "5000000", "expected_output": "348513", "is_sample": False},
        {"input": "100000", "expected_output": "9592", "is_sample": False},
        {"input": "499979", "expected_output": "41537", "is_sample": False}
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
        "topics": ["Array", "Math", "Enumeration", "Number Theory"],
        "companyIndex": 0
    }

    output_path = "1-200/204_Count_Primes.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
