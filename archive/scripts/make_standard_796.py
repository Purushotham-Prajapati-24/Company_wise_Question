import json
import os

def generate_json():
    problem_id = 796
    title = "Rotate String"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>796. Rotate String</h3>
<p>Given two strings <code>s</code> and <code>goal</code>, return <code>true</code><em> if and only if </em><code>s</code><em> can become </em><code>goal</code><em> after some number of <strong>shifts</strong> on </em><code>s</code>.</p>

<p>A <strong>shift</strong> on <code>s</code> consists of moving the leftmost character of <code>s</code> to the rightmost position.</p>

<ul>
	<li>For example, if <code>s = "abcde"</code>, then it will be <code>"bcdea"</code> after one shift.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcde", goal = "cdeab"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcde", goal = "abced"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, goal.length &lt;= 100</code></li>
	<li><code>s</code> and <code>goal</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines. Line 1: string s. Line 2: string goal."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= s.length, goal.length <= 100",
        "Lowercase English letters.",
        "O(N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To check if s can become goal by rotations:
1. **Length Check**:
   - If `len(s) != len(goal)`, they can never be rotations of each other; return `false`.
2. **Concatenation Trick**:
   - All possible rotations of string `s` of length `n` are contiguous substrings of length `n` in the concatenated string `s + s`.
     - Example: `s = "abc"`, `s + s = "abcabc"`.
     - Rotations: "abc" (at index 0), "bca" (at index 1), "cab" (at index 2).
3. **Substring Search**:
   - Simply check if `goal` is a substring of `s + s`.
4. **Complexity**:
   - Time Complexity: O(N) where N is the length of `s` (using efficient substring search).
   - Space Complexity: O(N) to store the concatenated string."""
    
    answer = """def rotateString(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)"""

    boilerplate = {
        "python": "import sys\n\ndef rotateString(s, goal):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        s = lines[0].strip()\n        goal = lines[1].strip()\n        print(str(rotateString(s, goal)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nbool rotateString(string s, string goal) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean rotateString(String s, String goal) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function rotateString(s, goal) {\n    // User logic\n}",
        "c": "bool rotateString(char* s, char* goal) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "abcde\\ncdeab", "expected_output": "true", "is_sample": True},
        {"input": "abcde\\nabced", "expected_output": "false", "is_sample": True},
        {"input": "a\\na", "expected_output": "true", "is_sample": True},
        {"input": "a\\nb", "expected_output": "false", "is_sample": False},
        {"input": "ab\\nba", "expected_output": "true", "is_sample": False},
        {"input": "abc\\ndef", "expected_output": "false", "is_sample": False},
        {"input": "aaaaa\\naaaaa", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "a" * 100 + "\\n" + "a" * 100, "expected_output": "true", "is_sample": False},
        {"input": "abcdefghij"*10 + "\\n" + "bcdefghija" + "bcdefghij"*9, "expected_output": "true", "is_sample": False},
        {"input": "a" * 100 + "\\n" + "a" * 99 + "b", "expected_output": "false", "is_sample": False}
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
        "topics": ["String", "String Matching"],
        "companyIndex": 0
    }

    output_path = "601-800/796_Rotate_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
