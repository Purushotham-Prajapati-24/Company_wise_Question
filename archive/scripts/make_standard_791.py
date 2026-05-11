import json
import os

def generate_json():
    problem_id = 791
    title = "Custom Sort String"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>791. Custom Sort String</h3>
<p>You are given two strings <code>order</code> and <code>s</code>. All the characters of <code>order</code> are <b>unique</b> and were sorted in some custom order previously.</p>

<p>Permute the characters of <code>s</code> so that they match the order that <code>order</code> was sorted. More specifically, if a character <code>x</code> occurs before a character <code>y</code> in <code>order</code>, then <code>x</code> should occur before <code>y</code> in the permuted string.</p>

<p>Return <em>any permutation of </em><code>s</code><em> that satisfies this property.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> order = "cba", s = "abcd"
<strong>Output:</strong> "cbad"
<strong>Explanation:</strong> 
"a", "b", "c" appear in order, so the order of them in s should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> order = "bcafg", s = "abcd"
<strong>Output:</strong> "bcad"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= order.length &lt;= 26</code></li>
	<li><code>1 &lt;= s.length &lt;= 200</code></li>
	<li><code>order</code> and <code>s</code> consist of lowercase English letters.</li>
	<li>All the characters of <code>order</code> are <b>unique</b>.</li>
</ul>"""

    input_format = "Two lines: 1) order string 2) s string."
    output_format = "A single string representing a valid permutation of s."
    
    constraints = [
        "1 <= order.length <= 26",
        "1 <= s.length <= 200",
        "O(S + O) time complexity.",
        "O(S) space complexity."
    ]
    
    explanation = """To permute string `s` matching the sequence of character in `order`:
1. **The Counting Strategy**:
   - Instead of using a complex sorting comparator, it's more efficient to count the frequencies of characters in `s`.
   - Characters in `order` define the primary sequence.
   - Characters not in `order` can be appended at the end.
2. **Algorithm Steps**:
   - Create a frequency map (or count array of size 26) for string `s`.
   - Iterate through each character `char` in `order`:
     - Append `char` to the result string `count[char]` times.
     - Set `count[char] = 0` to mark it as processed.
   - Iterate through the remaining keys in the frequency map (characters in `s` but not in `order`):
     - Append each character to the result string its remaining count times.
3. **Complexity**:
   - Time Complexity: O(order.length + s.length) or essentially O(N + M). 
   - Space Complexity: O(1) extra space since characters are only lowercase English letters (26). Output string takes O(M)."""
    
    answer = """from collections import Counter

def customSortString(order: str, s: str) -> str:
    count = Counter(s)
    res = []
    
    # 1. First deal with characters in order
    for char in order:
        res.append(char * count[char])
        count[char] = 0
    
    # 2. Append remaining characters
    for char in count:
        res.append(char * count[char])
        
    return "".join(res)"""

    boilerplate = {
        "python": "import sys\nfrom collections import Counter\n\ndef customSortString(order, s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        order = lines[0].strip()\n        s = lines[1].strip()\n        print(customSortString(order, s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <unordered_map>\n\nusing namespace std;\n\nstring customSortString(string order, string s) {\n    // User logic\n    return \"\";\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String customSortString(String order, String s) {\n        // User logic\n        return \"\";\n    }\n}",
        "javascript": "function customSortString(order, s) {\n    // User logic\n}",
        "c": "char* customSortString(char* order, char* s) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "cba\\nabcd", "expected_output": "cbad", "is_sample": True},
        {"input": "bcafg\\nabcd", "expected_output": "bcad", "is_sample": True},
        {"input": "a\\nbbb", "expected_output": "bbb", "is_sample": False},
        {"input": "zyx\\nabc", "expected_output": "abc", "is_sample": False},
        {"input": "k\\njjjkkklll", "expected_output": "kkkjjjlll", "is_sample": False},
        {"input": "abc\\n", "expected_output": "", "is_sample": False},
        {"input": "cba\\naaabbbccc", "expected_output": "cccbbbaaa", "is_sample": False},
        {"input": "xyz\\nabcyx", "expected_output": "xyabc", "is_sample": False},
        # Stress cases
        {"input": "abcdefghijklmnopqrstuvwxyz\\n" + "z" * 200, "expected_output": "z" * 200, "is_sample": False},
        {"input": "z\\n" + "abcdefghijklmnopqrstuvwxyz", "expected_output": "zabcdefghijklmnopqrstuvwxy", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sorting"],
        "companyIndex": 0
    }

    output_path = "601-800/791_Custom_Sort_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
