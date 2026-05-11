import json
import os

def generate_json():
    problem_id = 58
    title = "Length of Last Word"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>58. Length of Last Word</h3>
<p>Given a string <code>s</code> consisting of words and spaces, return <em>the length of the <strong>last</strong> word in the string.</em></p>

<p>A <strong>word</strong> is a maximal substring consisting of non-space characters only.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> s = "Hello World"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The last word is "World" with length 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> s = "   fly me   to   the moon  "
<strong>Output:</strong> 4
<strong>Explanation:</strong> The last word is "moon" with length 4.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> s = "luffy is still joyboy"
<strong>Output:</strong> 6
<strong>Explanation:</strong> The last word is "joyboy" with length 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only English letters and spaces <code>' '</code>.</li>
	<li>There will be at least one word in <code>s</code>.</li>
</ul>"""

    input_format = "A string s consisting of English letters and spaces."
    output_format = "An integer representing the length of the last word."
    
    constraints = [
        "1 <= s.length <= 10^4",
        "s contains only letters and spaces",
        "At least one word present"
    ]
    
    explanation = """To find the length of the last word:
1. **Trim Trailing spaces**: Start from the end of the string and skip all trailing space characters.
2. **Count Characters**: Continue iterating backwards from the first non-space character found, incrementing a count until a space is encountered or the beginning of the string is reached.
3. **Return Count**: The final count is the length of the last word.
4. **Complexity**:
   - **Time**: $O(N)$ (one pass from the end).
   - **Space**: $O(1)$."""
    
    answer = """def lengthOfLastWord(s):
    count = 0
    i = len(s) - 1
    
    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
        
    # Count last word characters
    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1
        
    return count"""

    boilerplate = {
        "python": "import sys\n\ndef lengthOfLastWord(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    s = sys.stdin.readline()\n    # Strip only newline, preserve internal spaces\n    if s.endswith('\\n'):\n        s = s[:-1]\n    print(lengthOfLastWord(s))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint lengthOfLastWord(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s;\n    getline(cin, s);\n    cout << lengthOfLastWord(s) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int lengthOfLastWord(String s) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String s = sc.hasNextLine() ? sc.nextLine() : \"\";\n        System.out.println(lengthOfLastWord(s));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction lengthOfLastWord(s) {\n    // User logic\n    return 0;\n}\n\nconst s = fs.readFileSync(0, 'utf8').replace(/\\n$/, '');\nconsole.log(lengthOfLastWord(s));",
        "c": "#include <stdio.h>\n#include <string.h>\n\nint lengthOfLastWord(char* s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char s[10001];\n    if (fgets(s, sizeof(s), stdin)) {\n        int len = strlen(s);\n        if (len > 0 && s[len-1] == '\\n') s[len-1] = '\\0';\n        printf(\"%d\\n\", lengthOfLastWord(s));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "Hello World", "expected_output": "5", "is_sample": True},
        {"input": "   fly me   to   the moon  ", "expected_output": "4", "is_sample": True},
        {"input": "luffy is still joyboy", "expected_output": "6", "is_sample": True},
        {"input": "a", "expected_output": "1", "is_sample": False},
        {"input": " a ", "expected_output": "1", "is_sample": False},
        {"input": "abc def   ", "expected_output": "3", "is_sample": False},
        {"input": "Today is a nice day", "expected_output": "3", "is_sample": False},
        {"input": "word", "expected_output": "4", "is_sample": False},
        {"input": "   spaces   word   ", "expected_output": "4", "is_sample": False},
        {"input": "Multiple words in a sentence", "expected_output": "8", "is_sample": False}
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

    output_path = "1-200/58_Length_of_Last_Word.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
