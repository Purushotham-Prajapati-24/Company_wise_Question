import json
import os

def generate_json():
    problem_id = 1021
    title = "Remove Outermost Parentheses"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1021. Remove Outermost Parentheses</h3>
<p>A valid parentheses string is either empty <code>""</code>, <code>"(" + A + ")"</code>, or <code>A + B</code>, where <code>A</code> and <code>B</code> are valid parentheses strings, and <code>+</code> represents string concatenation.</p>

<ul>
	<li>For example, <code>""</code>, <code>"()"</code>, <code>"(())()"</code>, and <code>"(()(()))"</code> are all valid parentheses strings.</li>
</ul>

<p>A valid parentheses string <code>s</code> is <strong>primitive</strong> if it is non-empty, and there does not exist a way to split it into <code>s = A + B</code>, with <code>A</code> and <code>B</code> non-empty valid parentheses strings.</p>

<p>Given a valid parentheses string <code>s</code>, consider its primitive decomposition: <code>s = P<sub>1</sub> + P<sub>2</sub> + ... + P<sub>k</sub></code>, where <code>P<sub>i</sub></code> are primitive valid parentheses strings.</p>

<p>Return <em><code>s</code> after removing the outermost parentheses of every primitive string in the primitive decomposition of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "(()())(())"
<strong>Output:</strong> "()()()"
<strong>Explanation:</strong> 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "(()())(())(()(()))"
<strong>Output:</strong> "()()()()(())"
<strong>Explanation:</strong> 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "()()"
<strong>Output:</strong> ""
<strong>Explanation:</strong> 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'('</code> or <code>')'</code>.</li>
	<li><code>s</code> is a valid parentheses string.</li>
</ul>"""

    input_format = "A single line containing the valid parentheses string s."
    output_format = "A single string after removing outermost parentheses."
    
    constraints = [
        "1 <= s.length <= 100,000",
        "s is valid parentheses string.",
        "O(N) time complexity.",
        "O(N) space complexity (for the result string)."
    ]
    
    explanation = """To remove the outermost parentheses of every primitive component:
1. **The Core Approach (Tracking Depth)**:
   - A primitive parentheses string like `(()())` starts with an outer `(` and ends with its matching outer `)`.
   - Any character *inside* these boundaries is part of the final result.
2. **Algorithm Strategy**:
   - Maintain a counter `opened` to track the nesting level.
   - Iterate through the string character by character:
     - If we see `(`:
       - If `opened > 0`, it means this `(` is not the outermost one for its primitive part. Append it to result.
       - Increment `opened`.
     - If we see `)`:
       - Decrement `opened`.
       - If `opened > 0`, it means this `)` is not the outermost one for its primitive part. Append it to result.
3. **Conclusion**:
   - This single pass identifies all characters that are not the "first opening" or "last closing" of any primitive part.
4. **Complexity**:
   - Time Complexity: O(N) as we traverse the string once.
   - Space Complexity: O(N) to store the result string."""
    
    answer = """def removeOuterParentheses(s: str) -> str:
    res = []
    opened = 0
    for char in s:
        if char == '(':
            if opened > 0:
                res.append(char)
            opened += 1
        else:
            opened -= 1
            if opened > 0:
                res.append(char)
    return "".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef removeOuterParentheses(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        print(removeOuterParentheses(line))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nstring removeOuterParentheses(string s) {\n    // User logic\n    return \"\";\n}",
        "java": "public class Solution {\n    public String removeOuterParentheses(String s) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function removeOuterParentheses(s) {\n    // User logic\n}",
        "c": "char* removeOuterParentheses(char* s) {\n    // User logic\n    return \"\";\n}"
    }

    test_cases = [
        {"input": "(()())(())", "expected_output": "()()()", "is_sample": True},
        {"input": "(()())(())(()(()))", "expected_output": "()()()()(())", "is_sample": True},
        {"input": "()()", "expected_output": "", "is_sample": True},
        {"input": "((()))", "expected_output": "(())", "is_sample": False},
        {"input": "((())(()))", "expected_output": "(())()", "is_sample": False},
        {"input": "()", "expected_output": "", "is_sample": False},
        {"input": "()((()))", "expected_output": "(())", "is_sample": False},
        {"input": "((())())", "expected_output": "(())()", "is_sample": False},
        # Stress cases
        {"input": "(" * 50000 + ")" * 50000, "expected_output": "(" * 49999 + ")" * 49999, "is_sample": False},
        {"input": "()" * 50000, "expected_output": "", "is_sample": False}
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
        "topics": ["String", "Stack"],
        "companyIndex": 0
    }

    output_path = "1001-1200/1021_Remove_Outermost_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
