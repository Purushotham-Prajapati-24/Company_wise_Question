import json
import os

def generate_json():
    problem_id = 859
    title = "Buddy Strings"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>859. Buddy Strings</h3>
<p>Given two strings <code>s</code> and <code>goal</code>, return <code>true</code> <em>if you can swap two letters in </em><code>s</code><em> so the result is equal to </em><code>goal</code><em>, otherwise, return </em><code>false</code><em>.</em></p>

<p>Swapping letters is defined as taking two indices <code>i</code> and <code>j</code> (0-indexed) such that <code>i != j</code> and swapping the characters at <code>s[i]</code> and <code>s[j]</code>.</p>

<ul>
	<li>For example, swapping at indices <code>0</code> and <code>2</code> in <code>"abcd"</code> results in <code>"cbad"</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "ab", goal = "ba"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "ab", goal = "ab"
<strong>Output:</strong> false
<strong>Explanation:</strong> The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "aa", goal = "aa"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, goal.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>goal</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines, each containing a string."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= s.length, goal.length <= 20,000",
        "Lowercase English letters only.",
        "O(N) time complexity.",
        "O(1) alphabet-size extra space."
    ]
    
    explanation = """To check if two strings are buddy strings:
1. **Initial Checks**:
   - If lengths of `s` and `goal` are different, return `false`.
2. **The "Duplicate Swap" Case**:
   - If `s == goal`:
     - We must perform exactly one swap. This swap must preserve the string's equality.
     - This is only possible if there is at least one character in `s` that appears multiple times (a duplicate).
     - Return `true` if `len(set(s)) < len(s)`.
3. **The "Character Substitution" Case**:
   - If `s != goal`:
     - Compare characters of `s` and `goal` at every index.
     - Collect indices `i` where `s[i] != goal[i]`.
     - To be buddy strings, there must be exactly 2 such indices.
     - Let these indices be `i` and `j`. Check if `s[i] == goal[j]` and `s[j] == goal[i]`.
4. **Complexity**:
   - Time Complexity: O(N) to traverse the strings.
   - Space Complexity: O(1) extra space (or O(26) for the character set)."""
    
    answer = """def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
        
    if s == goal:
        return len(set(s)) < len(s)
        
    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append(i)
            
    if len(diff) != 2:
        return False
        
    i, j = diff
    return s[i] == goal[j] and s[j] == goal[i]"""

    boilerplate = {
        "python": "import sys\n\ndef buddyStrings(s, goal):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        s = lines[0].strip()\n        goal = lines[1].strip()\n        print('true' if buddyStrings(s, goal) else 'false')",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nbool buddyStrings(string s, string goal) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean buddyStrings(String s, String goal) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function buddyStrings(s, goal) {\n    // User logic\n}",
        "c": "bool buddyStrings(char* s, char* goal) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "ab\\nba", "expected_output": "true", "is_sample": True},
        {"input": "ab\\nab", "expected_output": "false", "is_sample": True},
        {"input": "aa\\naa", "expected_output": "true", "is_sample": True},
        {"input": "aaaaaaabc\\naaaaaaaacb", "expected_output": "true", "is_sample": False},
        {"input": "abcd\\nbad", "expected_output": "false", "is_sample": False},
        {"input": "abcdef\\nabcdeg", "expected_output": "false", "is_sample": False},
        {"input": "abc\\nabc", "expected_output": "false", "is_sample": False},
        {"input": "cabbba\\nabbbac", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "a" * 20000 + "\\n" + "a" * 20000, "expected_output": "true", "is_sample": False},
        {"input": "a" * 10000 + "b" * 10000 + "\\n" + "a" * 10000 + "b" * 10000, "expected_output": "true", "is_sample": False}
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
        "topics": ["Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = "801-1000/859_Buddy_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
