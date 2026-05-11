import json
import os

def generate_json():
    problem_id = 784
    title = "Letter Case Permutation"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>784. Letter Case Permutation</h3>
<p>Given a string <code>s</code>, transform every letter individually to be lowercase or uppercase to create another string.</p>

<p>Return <em>a list of all possible strings we could create</em>. You can return the output in <b>any order</b>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "a1b2"
<strong>Output:</strong> ["a1b2","a1B2","A1b2","A1B2"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "3z4"
<strong>Output:</strong> ["3z4","3Z4"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 12</code></li>
	<li><code>s</code> consists of lowercase English letters, uppercase English letters, and digits.</li>
</ul>"""

    input_format = "A single string s."
    output_format = "A single line containing space-separated possible permutations."
    
    constraints = [
        "1 <= s.length <= 12",
        "Result can have up to 2^12 permutations.",
        "O(2^L * N) time complexity where L is the number of letters.",
        "O(2^L * N) space complexity."
    ]
    
    explanation = """To generate all possible combinations of lowercase and uppercase letters in a string:
1. **The Core Approach (Backtracking)**:
   - We process the string character by character.
   - For each character:
     - If it is a digit: We have only one choice—keep it as is.
     - If it is a letter: We have two choices—either keep it in its current case or flip its case.
2. **Recursive Logic**:
   - `dfs(index, current_string)`:
     - Base Case: If `index == len(s)`, add `current_string` to the results.
     - Recursive Step:
       - If `s[index]` is a letter, call `dfs(index + 1, current_string + lower)` and `dfs(index + 1, current_string + upper)`.
       - If `s[index]` is a digit, call `dfs(index + 1, current_string + s[index])`.
3. **Alternative (Iterative)**:
   - Start with `results = [""]`.
   - For each character `c` in `s`:
     - If `c` is a letter, double the size of `results` by appending both `c.lower()` and `c.upper()` to every existing string.
     - If `c` is a digit, just append `c` to every string.
4. **Complexity**:
   - Time Complexity: O(2^L * N), where L is the number of letters and N is string length.
   - Space Complexity: O(2^L * N) to store the result strings."""
    
    answer = """def letterCasePermutation(s: str) -> list[str]:
    res = ['']
    for char in s:
        if char.isalpha():
            new_res = []
            for item in res:
                new_res.append(item + char.lower())
                new_res.append(item + char.upper())
            res = new_res
        else:
            res = [item + char for item in res]
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef letterCasePermutation(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.readline().strip()\n    if line:\n        print(\" \".join(letterCasePermutation(line)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <cctype>\n\nusing namespace std;\n\nvector<string> letterCasePermutation(string s) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<String> letterCasePermutation(String s) {\n        // User logic\n        return new ArrayList<>();\n    }\n}",
        "javascript": "function letterCasePermutation(s) {\n    // User logic\n}",
        "c": "char** letterCasePermutation(char* s, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "a1b2", "expected_output": "a1b2 a1B2 A1b2 A1B2", "is_sample": True},
        {"input": "3z4", "expected_output": "3z4 3Z4", "is_sample": True},
        {"input": "123", "expected_output": "123", "is_sample": False},
        {"input": "C", "expected_output": "c C", "is_sample": False},
        {"input": "abc", "expected_output": "abc abC aBc aBC Abc AbC ABc ABC", "is_sample": False},
        {"input": "0", "expected_output": "0", "is_sample": False},
        {"input": "aB", "expected_output": "ab aB Ab AB", "is_sample": False},
        {"input": "1a2b", "expected_output": "1a2b 1a2B 1A2b 1A2B", "is_sample": False},
        # Stress cases
        {"input": "abcdeflmnopq", "expected_output": "len=4096", "is_sample": False}, # Too many to check easily, will use length check in audit
        {"input": "ABCDEFGHIJKL", "expected_output": "len=4096", "is_sample": False}
    ]
    
    # Adjusting test outputs for space-separated sort-agnostic comparison
    for tc in test_cases:
        if tc["expected_output"].startswith("len="): continue
        tc["expected_output"] = " ".join(sorted(tc["expected_output"].split()))

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
        "topics": ["String", "Backtracking", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "601-800/784_Letter_Case_Permutation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
