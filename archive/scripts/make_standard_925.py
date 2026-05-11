import json
import os

def generate_json():
    problem_id = 925
    title = "Long Pressed Name"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>925. Long Pressed Name</h3>
<p>Your friend is typing his <code>name</code> into a keyboard. Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code> characters of the keyboard. Return <code>true</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> name = "alex", typed = "aaleex"
<strong>Output:</strong> true
<strong>Explanation: </strong>\'a\' and \'e\' in \'alex\' were long pressed.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> name = "saeed", typed = "ssaaedd"
<strong>Output:</strong> false
<strong>Explanation: </strong>\'e\' must have been pressed twice, but it was not in the typed output.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= name.length, typed.length &lt;= 1000</code></li>
	<li><code>name</code> and <code>typed</code> consist of only lowercase English letters.</li>
</ul>"""

    input_format = "Two lines: first string is 'name', second string is 'typed'."
    output_format = "A single string 'true' or 'false'."
    
    constraints = [
        "1 <= name.length, typed.length <= 1,000",
        "Lowercase English letters only.",
        "O(N + M) time complexity.",
        "O(1) extra space."
    ]
    
    explanation = """To check if 'typed' could be a long-pressed version of 'name':
1. **The Two-Pointer Strategy**:
   - Use pointer `i` for `name` and pointer `j` for `typed`.
   - Iterate through `typed` until the end.
   - For each character `typed[j]`:
     - If `i < len(name)` and `name[i] == typed[j]`: This is a direct match. Increment both `i` and `j`.
     - Else if `j > 0` and `typed[j] == typed[j-1]`: This character is a long-press repetition of the previous character. Increment `j`.
     - Otherwise: This character doesn't match the current required character in `name` AND is not a continuation of the previous one. Return `false`.
2. **Post-Loop Verification**:
   - After the loop finishes, we must have exhausted all characters in `name` (`i == len(name)`).
3. **Complexity**:
   - Time Complexity: O(N + M) where N is the length of `name` and M is the length of `typed`.
   - Space Complexity: O(1) as we only use two pointer variables."""
    
    answer = """def isLongPressedName(name: str, typed: str) -> bool:
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j == 0 or typed[j] != typed[j-1]:
            return False
    return i == len(name)"""

    boilerplate = {
        "python": "import sys\n\ndef isLongPressedName(name, typed):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        name = lines[0].strip()\n        typed = lines[1].strip()\n        print('true' if isLongPressedName(name, typed) else 'false')",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nbool isLongPressedName(string name, string typed) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean isLongPressedName(String name, String typed) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function isLongPressedName(name, typed) {\n    // User logic\n}",
        "c": "bool isLongPressedName(char* name, char* typed) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "alex\\naaleex", "expected_output": "true", "is_sample": True},
        {"input": "saeed\\nssaaedd", "expected_output": "false", "is_sample": True},
        {"input": "leelee\\nlleeelee", "expected_output": "true", "is_sample": False},
        {"input": "a\\nb", "expected_output": "false", "is_sample": False},
        {"input": "abcd\\nabcd", "expected_output": "true", "is_sample": False},
        {"input": "abc\\nabcd", "expected_output": "false", "is_sample": False},
        {"input": "vtkgn\\nvtkgnn", "expected_output": "true", "is_sample": False},
        {"input": "alex\\naalexxrv", "expected_output": "false", "is_sample": False},
        # Stress cases
        {"input": "a" * 1000 + "\\n" + "a" * 1000, "expected_output": "true", "is_sample": False},
        {"input": "a" + "\\n" + "a" * 1000, "expected_output": "true", "is_sample": False}
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

    output_path = "801-1000/925_Long_Pressed_Name.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
