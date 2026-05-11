import json
import os

def generate_json():
    problem_id = 132
    title = "Palindrome Partitioning II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>132. Palindrome Partitioning II</h3>
<p>Given a string <code>s</code>, partition <code>s</code> such that every substring of the partition is a <strong>palindrome</strong>.</p>

<p>Return <em>the <strong>minimum</strong> cuts needed for a palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The palindrome partitioning ["aa","b"] could be produced using 1 cut.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "ab"
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing the string s."
    output_format = "An integer representing the minimum cuts needed."
    
    constraints = [
        "1 <= s.length <= 2000",
        "s contains only lowercase English letters."
    ]
    
    explanation = """To find the minimum cuts for palindrome partitioning:
1. **Dynamic Programming**: We define `dp[i]` as the minimum cuts needed for the prefix `s[0...i]`.
2. **Palindrome Precomputation**: Use another DP table `is_pal[i][j]` to check if `s[i...j]` is a palindrome in O(1) after O(N^2) precomputation.
3. **Transition**: For each `i` (end of current prefix):
   - If `s[0...i]` is a palindrome, `dp[i] = 0`.
   - Otherwise, `dp[i] = min(dp[j] + 1)` for all `j < i` where `s[j+1...i]` is a palindrome.
4. **Complexity**:
   - Time Complexity: O(N^2) for both palindrome precomputation and the main DP transitions.
   - Space Complexity: O(N^2) for the `is_pal` table (can be optimized to O(N) by expanding from centers)."""
    
    answer = """class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
            
        # dp[i] is min cuts for s[:i]
        dp = [i - 1 for i in range(n + 1)]
        
        # Expand around centers to find palindromes and update dp
        for i in range(n):
            # Odd length palindromes
            r = 0
            while i - r >= 0 and i + r < n and s[i - r] == s[i + r]:
                dp[i + r + 1] = min(dp[i + r + 1], dp[i - r] + 1)
                r += 1
            # Even length palindromes
            r = 1
            while i - r + 1 >= 0 and i + r < n and s[i - r + 1] == s[i + r]:
                dp[i + r + 1] = min(dp[i + r + 1], dp[i - r + 1] + 1)
                r += 1
                
        return dp[n]"""

    boilerplate = {
        "python": "import sys\n\ndef minCut(s: str) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    if not s: sys.exit()\n    print(minCut(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nint minCut(string s) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int minCut(String s) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n    }\n}",
        "javascript": "/**\n * @param {string} s\n * @return {number}\n */\nvar minCut = function(s) {\n    // User logic\n};",
        "c": "int minCut(char* s) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "aab", "expected_output": "1", "is_sample": True},
        {"input": "a", "expected_output": "0", "is_sample": True},
        {"input": "ab", "expected_output": "1", "is_sample": False},
        {"input": "aba", "expected_output": "0", "is_sample": False},
        {"input": "aaaa", "expected_output": "0", "is_sample": False},
        {"input": "abcde", "expected_output": "4", "is_sample": False},
        {"input": "cdd", "expected_output": "1", "is_sample": False},
        # Stress Tests (N=2000)
        {"input": "a" * 2000, "expected_output": "0", "is_sample": False},
        {"input": "".join([chr(97 + (i % 26)) for i in range(1000)]) + "".join([chr(97 + (i % 26)) for i in range(999, -1, -1)]), "expected_output": "0", "is_sample": False},
        {"input": "abcdefghij" * 200, "expected_output": "1999", "is_sample": False}
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
        "topics": ["String", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/132_Palindrome_Partitioning_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
