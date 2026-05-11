import json
import os

def generate_json():
    problem_id = 290
    title = "Word Pattern"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>290. Word Pattern</h3>
<p>Given a <code>pattern</code> and a string <code>s</code>, find if <code>s</code>&nbsp;follows the same pattern.</p>

<p>Here <b>follow</b> means a full match, such that there is a bijection between a letter in <code>pattern</code> and a <b>non-empty</b> word in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> pattern = "abba", s = "dog cat cat dog"
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> pattern = "abba", s = "dog cat cat fish"
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> pattern = "aaaa", s = "dog cat cat dog"
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length &lt;= 300</code></li>
	<li><code>pattern</code> contains only lowercase English letters.</li>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> contains only lowercase English letters and spaces <code>' '</code>.</li>
	<li><code>s</code> <strong>does not contain</strong> any leading or trailing spaces.</li>
	<li>All the words in <code>s</code> are separated by a <strong>single space</strong>.</li>
</ul>"""

    input_format = "Two lines. Line 1: pattern string. Line 2: space-separated words in string s."
    output_format = "true if s follows the pattern, false otherwise."
    
    constraints = [
        "1 <= pattern.length <= 300",
        "1 <= s.length <= 3000",
        "Bijection required: each char maps to exactly one word, and vice versa.",
        "O(N) time complexity.",
        "O(N) space complexity."
    ]
    
    explanation = """To determine if a string follows a word pattern:
1. **Bijection Mapping**:
   - Split the string `s` into a list of words.
   - If the number of characters in `pattern` is not equal to the number of words, they cannot match. Return `false`.
   - Use two hash maps (or dictionaries):
     - `char_to_word`: maps a character from `pattern` to a word from `s`.
     - `word_to_char`: maps a word from `s` to a character from `pattern`.
2. **Logic**:
   - Iterate through both collections simultaneously.
   - For each character `c` and word `w`:
     - If `c` is in `char_to_word`, and `char_to_word[c] != w`, the pattern is broken.
     - If `w` is in `word_to_char`, and `word_to_char[w] != c`, the pattern is broken.
     - Otherwise, add the mappings to both maps.
3. **Complexity**:
   - Time Complexity: O(N) where N is the length of the shorter input (or the number of words).
   - Space Complexity: O(M) where M is the number of unique words/characters to store in the maps."""
    
    answer = """def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
        
    char_to_word = {}
    word_to_char = {}
    
    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            char_to_word[c] = w
            
        if w in word_to_char:
            if word_to_char[w] != c:
                return False
        else:
            word_to_char[w] = c
            
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef wordPattern(pattern, s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        print(\"true\" if wordPattern(lines[0], lines[1]) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <sstream>\n#include <unordered_map>\n\nusing namespace std;\n\nbool wordPattern(string pattern, string s) {\n    // User logic\n    return false;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public boolean wordPattern(String pattern, String s) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "function wordPattern(pattern, s) {\n    // User logic\n}",
        "c": "bool wordPattern(char* pattern, char* s) {\n    // User logic\n    return false;\n}"
    }

    test_cases = [
        {"input": "abba\\ndog cat cat dog", "expected_output": "true", "is_sample": True},
        {"input": "abba\\ndog cat cat fish", "expected_output": "false", "is_sample": True},
        {"input": "aaaa\\ndog cat cat dog", "expected_output": "false", "is_sample": True},
        {"input": "abba\\ndog dog dog dog", "expected_output": "false", "is_sample": False},
        {"input": "a\\ndog", "expected_output": "true", "is_sample": False},
        {"input": "abc\\ndog cat fish", "expected_output": "true", "is_sample": False},
        {"input": "aaa\\ndog dog dog", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "abcdefg\\ndog cat fish cow bird horse pig", "expected_output": "true", "is_sample": False},
        {"input": "a"*300 + "\\n" + " ".join(["word"]*299), "expected_output": "false", "is_sample": False},
        {"input": "z"*300 + "\\n" + " ".join(["zebra"]*300), "expected_output": "true", "is_sample": False}
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

    output_path = "201-400/290_Word_Pattern.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
