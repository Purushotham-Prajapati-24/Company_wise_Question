import json
import os

def generate_json():
    problem_id = 424
    title = "Longest Repeating Character Replacement"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>424. Longest Repeating Character Replacement</h3>
<p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.</p>

<p>Return <em>the length of the longest substring containing the same letter you can get after performing the above operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "ABAB", k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two 'A's with two 'B's or vice versa.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "AABABBA", k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letter, which is 4.
There may exists other ways to achieve this answer too.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only uppercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>"""

    input_format = "A string s and an integer k."
    output_format = "An integer representing the maximum length."
    
    constraints = ["1 <= s.length <= 10^5", "s consists of uppercase English letters.", "0 <= k <= s.length"]
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def characterReplacement(s, k):
    count = {}
    max_f = 0
    l = 0
    res = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_f = max(max_f, count[s[r]])
        
        while (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1
            # Note: max_f doesn't need to be updated here for the algorithm to work
        res = max(res, r - l + 1)
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef characterReplacement(s, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    s = input_data[0].strip() if len(input_data) > 0 else \"\"\n    k = input_data[1].strip() if len(input_data) > 1 else \"\"\n    print(characterReplacement(s, k))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint characterReplacement(string s, string k) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s; cin >> s;\n    string k; cin >> k;\n    cout << characterReplacement(s, k) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": '"ABAB"\\n2', "expected_output": "4", "is_sample": True},
        {"input": '"AABABBA"\\n1', "expected_output": "4", "is_sample": True},
        {"input": '"AAAA"\\n2', "expected_output": "4", "is_sample": False},
        {"input": '"ABCDE"\\n1', "expected_output": "2", "is_sample": False},
        {"input": '"AABA"\\n0', "expected_output": "2", "is_sample": False},
        {"input": '"ABAA"\\n0', "expected_output": "2", "is_sample": False},
        {"input": '"AAAB"\\n0', "expected_output": "3", "is_sample": False},
        # Stress tests]

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
