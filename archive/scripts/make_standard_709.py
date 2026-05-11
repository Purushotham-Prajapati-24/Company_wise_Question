import json
import os

def generate_json():
    problem_id = 709
    title = "To Lower Case"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>709. To Lower Case</h3>
<p>Given a string <code>s</code>, return <em>the string after replacing every uppercase letter with the same lowercase letter</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "Hello"
<strong>Output:</strong> "hello"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "here"
<strong>Output:</strong> "here"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "LOVELY"
<strong>Output:</strong> "lovely"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of printable ASCII characters.</li>
</ul>"""

    input_format = "A single line containing string s."
    output_format = "The string s with all uppercase characters converted to lowercase."
    
    constraints = [
        "1 <= s.length <= 100",
        "ASCII printable characters.",
        "O(N) time complexity.",
        "O(N) space for the result."
    ]
    
    explanation = """To convert a string to lowercase without using built-in library functions:
1. **ASCII Recognition**:
   - Uppercase letters 'A' to 'Z' have ASCII values from 65 to 90.
   - Lowercase letters 'a' to 'z' have ASCII values from 97 to 122.
   - The difference between corresponding upper and lower case letters is exactly 32.
2. **Algorithm**:
   - Iterate through each character `c` in the string.
   - Check if `c` is within the range `['A', 'Z']`.
   - If yes, convert it by adding 32 to its ASCII value (`chr(ord(c) + 32)`).
   - If no, keep the character as it is.
3. **Complexity**:
   - Time Complexity: O(N) to iterate through the string once.
   - Space Complexity: O(N) to store and return the modified string."""
    
    answer = """def toLowerCase(s: str) -> str:
    res = []
    for char in s:
        if 'A' <= char <= 'Z':
            res.append(chr(ord(char) + 32))
        else:
            res.append(char)
    return "".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef toLowerCase(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        print(toLowerCase(line))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nstring toLowerCase(string s) {\n    // User logic\n    return \"\";\n}",
        "java": "public class Solution {\n    public String toLowerCase(String s) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function toLowerCase(s) {\n    // User logic\n}",
        "c": "char* toLowerCase(char* s) {\n    // User logic\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "Hello", "expected_output": "hello", "is_sample": True},
        {"input": "here", "expected_output": "here", "is_sample": True},
        {"input": "LOVELY", "expected_output": "lovely", "is_sample": True},
        {"input": "A", "expected_output": "a", "is_sample": False},
        {"input": "z", "expected_output": "z", "is_sample": False},
        {"input": "123!@#", "expected_output": "123!@#", "is_sample": False},
        {"input": "AbCdEfG", "expected_output": "abcdefg", "is_sample": False},
        {"input": "alpHaBET", "expected_output": "alphabet", "is_sample": False},
        # Stress cases
        {"input": "A" * 100, "expected_output": "a" * 100, "is_sample": False},
        {"input": "Mixed 123 CASE!", "expected_output": "mixed 123 case!", "is_sample": False}
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
        "topics": ["String"],
        "companyIndex": 0
    }

    output_path = "601-800/709_To_Lower_Case.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
