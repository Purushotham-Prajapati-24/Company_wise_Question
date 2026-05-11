import json
import os

def generate_json():
    problem_id = 1062
    title = "Longest Repeating Substring"
    difficulty = "Medium"
    marks = 15
    
    html_description = """<h3>1062. Longest Repeating Substring</h3>
<p>Given a string <code>s</code>, return the length of the longest repeating substring. If no repeating substring exists, return <code>0</code>.</p>

<p><strong>Note:</strong> Overlapping occurrences of repeating substrings are allowed, but they must start at different positions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> 0
<strong>Explanation:</strong> No repeating substring.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abbaba"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest repeating substrings are "ab" and "ba", each of which occurs twice.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "aabcaabdaab"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest repeating substring is "aab", which occurs 3 times.
</pre>

<p><strong class="example">Example 4:</strong></p>
<pre><strong>Input:</strong> s = "aaaaa"
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest repeating substring is "aaaa", which occurs twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing the string s."
    output_format = "An integer representing the length of the longest repeating substring."
    
    constraints = [
        "1 <= s.length <= 2000",
        "s consists of lowercase English letters.",
        "O(N log N) or O(N^2) time complexity is acceptable for N=2000.",
        "O(N log N) is preferred using Binary Search + Rolling Hash."
    ]
    
    explanation = """To find the length of the longest repeating substring:
1. **The Monotonic Property**:
   - If a repeating substring of length $L$ exists, then a repeating substring of length $L-1$ must also exist.
   - This allows us to use **Binary Search** to find the maximum possible length.
2. **Algorithm Strategy (Binary Search + Rolling Hash)**:
   - Perform binary search on the length $L$ in the range $[0, N-1]$.
   - For a given length `mid`, check if any substring of that length repeats.
   - We use **Rolling Hash** (Rabin-Karp) to check for duplicates in O(N).
3. **Optimized Check Function**:
   - Compute hash of the first substring of length `mid`.
   - Store it in a set.
   - Slide the window, update the hash, and check if the new hash exists in the set.
4. **Complexity Analysis**:
   - Time Complexity: O(N log N) with Binary Search and Rolling Hash.
   - Space Complexity: O(N) to store hashes in the set."""
    
    answer = """def longestRepeatingSubstring(s: str) -> int:
    n = len(s)
    nums = [ord(c) - ord('a') for c in s]
    mod = 2**63 - 1
    base = 26

    def check(length):
        if length == 0: return False
        h = 0
        for i in range(length):
            h = (h * base + nums[i]) % mod
        
        seen = {h}
        power = pow(base, length, mod)
        
        for i in range(length, n):
            h = (h * base - nums[i - length] * power + nums[i]) % mod
            if h in seen:
                return True
            seen.add(h)
        return False

    low, high = 1, n - 1
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef longestRepeatingSubstring(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        print(longestRepeatingSubstring(line))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nint longestRepeatingSubstring(string s) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int longestRepeatingSubstring(String s) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function longestRepeatingSubstring(s) {\n    // User logic\n}",
        "c": "int longestRepeatingSubstring(char* s) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "abcd", "expected_output": "0", "is_sample": True},
        {"input": "abbaba", "expected_output": "2", "is_sample": True},
        {"input": "aabcaabdaab", "expected_output": "3", "is_sample": True},
        {"input": "aaaaa", "expected_output": "4", "is_sample": True},
        {"input": "banana", "expected_output": "3", "is_sample": False},
        {"input": "abcdeabcde", "expected_output": "5", "is_sample": False},
        {"input": "x", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": "a" * 2000, "expected_output": "1999", "is_sample": False},
        {"input": "abcdefghijklmnopqrstuvwxyz" * 70, "expected_output": "1794", "is_sample": False}, # 26 * 69 + something. (70-1)*26 = 1794.
        {"input": "".join([chr(ord('a') + i % 26) for i in range(2000)]), "expected_output": str(2000 - 26), "is_sample": False}
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
        "topics": ["String", "Binary Search", "Rolling Hash", "Suffix Array", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1062_Longest_Repeating_Substring.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
