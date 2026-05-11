import json
import os

def generate_json():
    problem_id = 541
    title = "Reverse String II"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>541. Reverse String II</h3>
<p>Given a string <code>s</code> and an integer <code>k</code>, reverse the first <code>k</code> characters for every <code>2k</code> characters counting from the start of the string.</p>

<p>If there are fewer than <code>k</code> characters left, reverse all of them. If there are less than <code>2k</code> but greater than or equal to <code>k</code> characters, then reverse the first <code>k</code> characters and leave the other as original.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcdefg", k = 2
<strong>Output:</strong> "bacdfeg"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "bacd"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines. Line 1: integer k. Line 2: string s."
    output_format = "A single string representing the modified s."
    
    constraints = [
        "1 <= s.length <= 10^4",
        "1 <= k <= 10^4",
        "O(N) time complexity.",
        "O(N) space complexity."
    ]
    
    explanation = """To transform the string according to the given rules:
1. **Iterate in Chunks**:
   - Iterate through the string in steps of `2k`.
   - For each chunk starting at index `i`:
     - The segment to reverse is `s[i : i + k]`.
     - Reverse this segment and join it with the rest of the chunk.
2. **Handling End Condition**:
   - The slicing syntax `s[i : i + k]` in Python automatically handles cases where `i + k` is out of bounds (it just takes until the end of the string).
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of `s`, as we process each character a constant number of times.
   - Space Complexity: O(N) to store the modified string (or list of characters)."""
    
    answer = """def reverseStr(s: str, k: int) -> str:
    a = list(s)
    for i in range(0, len(a), 2 * k):
        a[i : i + k] = reversed(a[i : i + k])
    return "".join(a)"""

    boilerplate = {
        "python": "import sys\n\ndef reverseStr(s, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        k = int(lines[0])\n        s = lines[1]\n        print(reverseStr(s, k))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nstring reverseStr(string s, int k) {\n    // User logic\n    return \"\";\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String reverseStr(String s, int k) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function reverseStr(s, k) {\n    // User logic\n}",
        "c": "char* reverseStr(char* s, int k) {\n    // User logic\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "2\\nabcdefg", "expected_output": "bacdfeg", "is_sample": True},
        {"input": "2\\nabcd", "expected_output": "bacd", "is_sample": True},
        {"input": "3\\nabc", "expected_output": "cba", "is_sample": True},
        {"input": "1\\nabc", "expected_output": "abc", "is_sample": False},
        {"input": "10\\nabc", "expected_output": "cba", "is_sample": False},
        {"input": "2\\na", "expected_output": "a", "is_sample": False},
        {"input": "3\\nabcdef", "expected_output": "cbadef", "is_sample": False},
        # Stress cases
        {"input": "2\\n" + "a"*10000, "expected_output": "a"*10000, "is_sample": False},
        {"input": "1\\n" + "abcdefghij", "expected_output": "abcdefghij", "is_sample": False},
        {"input": "5000\\n" + "a"*5000 + "b"*5000, "expected_output": "a"*5000 + "b"*5000, "is_sample": False}
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 0
    }

    output_path = "401-600/541_Reverse_String_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
