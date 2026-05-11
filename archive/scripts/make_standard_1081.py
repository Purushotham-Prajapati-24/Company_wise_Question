import json
import os

def generate_json():
    problem_id = 1081
    title = "Smallest Subsequence of Distinct Characters"
    difficulty = "Medium"
    marks = 15
    
    html_description = """<h3>1081. Smallest Subsequence of Distinct Characters</h3>
<p>Given a string <code>s</code>, return the <em>lexicographically smallest subsequence</em> of <code>s</code> that contains all the distinct characters of <code>s</code> exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "bcabc"
<strong>Output:</strong> "abc"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "cbacdcbc"
<strong>Output:</strong> "acdb"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This question is the same as 316: <a href="https://leetcode.com/problems/remove-duplicate-letters/" target="_blank">https://leetcode.com/problems/remove-duplicate-letters/</a>
"""

    input_format = "A single line containing the string s."
    output_format = "A string representing the lexicographically smallest subsequence of distinct characters."
    
    constraints = [
        "1 <= s.length <= 1000",
        "s consists of lowercase English letters.",
        "Must contain all distinct characters of s exactly once.",
        "O(N) time complexity.",
        "O(1) extra space (excluding result)."
    ]
    
    explanation = """To find the lexicographically smallest subsequence with all distinct characters:
1. **The Greed with Future Foresight**:
   - We process characters one by one and build the result string using a **Monotonic Stack**.
   - As we consider character $c$, if $c$ is smaller than the top of our stack, we want to pop the top and replace it with $c$ to make the result smaller.
   - However, we can only pop the top if we know it appears **later** in the string (foresight). Otherwise, we must keep it to ensure all characters are included.
2. **Algorithm Strategy**:
   - Count the frequency or find the `last_index` of each character in `s`.
   - Maintain a `stack` for the result and a `seen` set for characters already in the stack.
   - For each char `c` in `s`:
     - If `c` is already in `seen`, skip (we only need one of each).
     - While `stack` is not empty, `stack[-1] > c`, AND `last_index[stack[-1]] > current_index`:
       - `seen.remove(stack.pop())`
     - `stack.append(c)`
     - `seen.add(c)`
3. **Complexity**:
   - Time Complexity: O(N) because each character is pushed and popped at most once.
   - Space Complexity: O(1) (size of alphabet, i.e., 26 characters)."""
    
    answer = """def smallestSubsequence(s: str) -> str:
    last_occ = {c: i for i, c in enumerate(s)}
    stack = []
    seen = set()
    
    for i, char in enumerate(s):
        if char not in seen:
            while stack and char < stack[-1] and last_occ[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
    return "".join(stack)"""

    boilerplate = {
        "python": "import sys\n\ndef smallestSubsequence(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        print(smallestSubsequence(line))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <unordered_map>\n#include <stack>\n#include <unordered_set>\n\nusing namespace std;\n\nstring smallestSubsequence(string s) {\n    // User logic\n    return \"\";\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String smallestSubsequence(String s) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function smallestSubsequence(s) {\n    // User logic\n}",
        "c": "char* smallestSubsequence(char* s) {\n    // User logic\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "bcabc", "expected_output": "abc", "is_sample": True},
        {"input": "cbacdcbc", "expected_output": "acdb", "is_sample": True},
        {"input": "leetcode", "expected_output": "letcod", "is_sample": False},
        {"input": "ecadbc", "expected_output": "adbc", "is_sample": False},
        {"input": "abacaba", "expected_output": "abc", "is_sample": False},
        {"input": "z", "expected_output": "z", "is_sample": False},
        {"input": "abcd", "expected_output": "abcd", "is_sample": False},
        # Stress cases
        {"input": "abcdefghijklmnopqrstuvwxyz" * 38, "expected_output": "abcdefghijklmnopqrstuvwxyz", "is_sample": False},
        {"input": "zyxwvutsrqponmlkjihgfedcba", "expected_output": "zyxwvutsrqponmlkjihgfedcba", "is_sample": False},
        {"input": ("".join([chr(ord('a') + i % 26) for i in range(1000)])), "expected_output": "abcdefghijklmnopqrstuvwxyz", "is_sample": False}
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
        "topics": ["String", "Stack", "Greedy", "Monotonic Stack"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1081_Smallest_Subsequence_of_Distinct_Characters.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
