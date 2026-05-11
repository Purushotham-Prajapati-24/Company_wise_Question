import json
import os

def generate_json():
    problem_id = 125
    title = "Valid Palindrome"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>125. Valid Palindrome</h3>
<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "A man, a plan, a canal: Panama"
<strong>Output:</strong> true
<strong>Explanation:</strong> "amanaplanacanalpanama" is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "race a car"
<strong>Output:</strong> false
<strong>Explanation:</strong> "raceacar" is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = " "
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>"""

    input_format = "A single line containing the string s."
    output_format = "true if s is a valid palindrome, otherwise false."
    
    constraints = [
        "1 <= s.length <= 2 * 10^5",
        "s contains only printable ASCII characters."
    ]
    
    explanation = """To check if a string is a valid palindrome efficiently:
1. **Two-Pointer Approach**:
   - Initialize two pointers: `left = 0` and `right = len(s) - 1`.
   - While `left < right`:
     - Move `left` forward if `s[left]` is not alphanumeric.
     - Move `right` backward if `s[right]` is not alphanumeric.
     - Compare `s[left]` and `s[right]` (case-insensitively). If they don't match, return `false`.
1. **Space Efficiency**:
   - This approach uses O(1) extra space because we don't create a new filtered string.
2. **Complexity**:
   - Time Complexity: O(N) as we scan the string once.
   - Space Complexity: O(1)."""
    
    answer = """def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True"""

    boilerplate = {
        "python": "import sys\n\ndef isPalindrome(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read()\n    # strip trailing newline only\n    if line.endswith('\\n'): line = line[:-1]\n    print(str(isPalindrome(line)).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <cctype>\nusing namespace std;\nbool isPalindrome(string s) {\n    // User logic\n    return true;\n}\nint main() {\n    string line; if(!getline(cin,line)) return 0;\n    cout << (isPalindrome(line) ? \"true\" : \"false\") << endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static boolean isPalindrome(String s) {\n        // User logic\n        return true;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line = br.readLine();\n        if(line==null) line=\"\";\n        System.out.println(isPalindrome(line) ? \"true\" : \"false\");\n    }\n}",
        "javascript": "const fs = require('fs');\nfunction isPalindrome(s) {\n    // User logic\n    return true;\n}\nlet line = fs.readFileSync(0,'utf8');\nif(line.endsWith('\\n')) line=line.slice(0,-1);\nconsole.log(isPalindrome(line) ? 'true' : 'false');",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n#include <ctype.h>\n#include <string.h>\nbool isPalindrome(char* s) {\n    // User logic\n    return true;\n}\nint main() {\n    char buf[200002]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int len=strlen(buf); if(len>0&&buf[len-1]=='\\n') buf[--len]='\\0';\n    printf(\"%s\\n\",isPalindrome(buf)?\"true\":\"false\"); return 0;\n}"
    }

    test_cases = [
        {"input": "A man, a plan, a canal: Panama", "expected_output": "true", "is_sample": True},
        {"input": "race a car", "expected_output": "false", "is_sample": True},
        {"input": " ", "expected_output": "true", "is_sample": True},
        {"input": "ab_a", "expected_output": "true", "is_sample": False},
        {"input": "0P", "expected_output": "false", "is_sample": False},
        {"input": "a.", "expected_output": "true", "is_sample": False},
        {"input": ".,", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "a" * 200000, "expected_output": "true", "is_sample": False},
        {"input": "ab" * 100000, "expected_output": "false", "is_sample": False},
        {"input": ("a"*100000 + "b" + "a"*100000), "expected_output": "true", "is_sample": False}
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

    output_path = "1-200/125_Valid_Palindrome.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
