import json
import os

def generate_json():
    problem_id = 408
    title = "Valid Word Abbreviation"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>408. Valid Word Abbreviation</h3>
<p>A string can be <strong>abbreviated</strong> by replacing any number of <strong>non-adjacent</strong>, <strong>non-empty</strong> substrings with their lengths. The lengths should not have leading zeros.</p>

<p>For example, a string such as <code>"substitution"</code> could be abbreviated as (but not limited to):</p>

<ul>
	<li><code>"s10n"</code> (<code>"s ubstitutio n"</code>)</li>
	<li><code>"sub4u4"</code> (<code>"sub stit u tion"</code>)</li>
	<li><code>"12"</code> (<code>"substitution"</code>)</li>
	<li><code>"su3i1u2on"</code> (<code>"su bst i t u ti on"</code>)</li>
	<li><code>"substitution"</code> (no substrings replaced)</li>
</ul>

<p>The following are <strong>not</strong> valid abbreviations:</p>

<ul>
	<li><code>"s55n"</code> (<code>"s ubsti tutio n"</code>, the replaced substrings are adjacent)</li>
	<li><code>"s010n"</code> (has leading zeros)</li>
	<li><code>"s0n"</code> (also has leading zeros)</li>
</ul>

<p>Given a <strong>non-empty</strong> string <code>word</code> and an abbreviation <code>abbr</code>, return <em>whether the string matches the given abbreviation</em>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> word = "internationalization", abbr = "i12iz4n"
<strong>Output:</strong> true
<strong>Explanation:</strong> The word "internationalization" can be abbreviated as "i12iz4n" ("i nternationaliz atio n").
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> word = "apple", abbr = "a2e"
<strong>Output:</strong> false
<strong>Explanation:</strong> The word "apple" cannot be abbreviated as "a2e".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 20</code></li>
	<li><code>word</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= abbr.length &lt;= 10</code></li>
	<li><code>abbr</code> consists of lowercase English letters and digits.</li>
	<li>All the integers in <code>abbr</code> will fit in a 32-bit integer.</li>
</ul>"""

    input_format = "A string word and its potential abbreviation abbr."
    output_format = "A boolean value."
    
    constraints = ["1 <= word.length <= 20", "1 <= abbr.length <= 10", "Lowercase English letters and digits only.", "No leading zeros in abbreviation lengths."]
    
    explanation = """EASY problem on ."""
    
    answer = """def validWordAbbreviation(word, abbr):
    i = j = 0
    m, n = len(word), len(abbr)
    while i < m and j < n:
        if abbr[j].isdigit():
            if abbr[j] == '0':
                return False
            num = 0
            while j < n and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == m and j == n"""

    boilerplate = {
        "python": "import sys\n\ndef validWordAbbreviation(word, abbr):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    word = input_data[0].strip() if len(input_data) > 0 else \"\"\n    abbr = input_data[1].strip() if len(input_data) > 1 else \"\"\n    print(validWordAbbreviation(word, abbr))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint validWordAbbreviation(string word, string abbr) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string word; cin >> word;\n    string abbr; cin >> abbr;\n    cout << validWordAbbreviation(word, abbr) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": '"internationalization"\\n"i12iz4n"', "expected_output": "True", "is_sample": True},
        {"input": '"apple"\\n"a2e"', "expected_output": "False", "is_sample": True},
        {"input": '"substitution"\\n"s10n"', "expected_output": "True", "is_sample": False},
        {"input": '"substitution"\\n"sub4u4"', "expected_output": "True", "is_sample": False},
        {"input": '"substitution"\\n"12"', "expected_output": "True", "is_sample": False},
        {"input": '"substitution"\\n"s010n"', "expected_output": "False", "is_sample": False},
        {"input": '"a"\\n"01"', "expected_output": "False", "is_sample": False},
        {"input": '"word"\\n"w0rd"', "expected_output": "False", "is_sample": False},
        {"input": '"a"\\n"2"', "expected_output": "False", "is_sample": False},
        {"input": '"ab"\\n"a"', "expected_output": "False", "is_sample": False},]

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
