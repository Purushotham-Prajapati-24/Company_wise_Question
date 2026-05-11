import json
import os

def generate_json():
    problem_id = 5
    title = "Longest Palindromic Substring"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>5. Longest Palindromic Substring</h3>
<p>Given a string <code>s</code>, return <em>the longest palindromic substring</em> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "babad"
<strong>Output:</strong> "bab"
<strong>Explanation:</strong> "aba" is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "cbbd"
<strong>Output:</strong> "bb"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>
"""

    input_format = "A single line containing the string 's'."
    output_format = "A string representing the longest palindromic substring."
    
    constraints = [
        "1 <= s.length <= 1000",
        "s consists of digits and English letters."
    ]
    
    explanation = """To find the longest palindromic substring:
1. Iterate through each character in the string, treating it as the potential center of a palindrome.
2. For each center, consider two cases:
   - **Odd-length palindrome**: Center is a single character (e.g., 'aba', center 'b').
   - **Even-length palindrome**: Center is between two characters (e.g., 'abba', center between 'b' and 'b').
3. For each case, expand outwards as long as the characters match and we remain within string bounds.
4. Keep track of the starting index and maximum length of the palindrome found so far.
5. After checking all centers, return the substring starting from the tracked index with the maximum length.

Time Complexity: O(N^2) where N is the string length.
Space Complexity: O(1) beyond the resulting substring."""
    
    answer = """def longestPalindrome(s):
    if not s:
        return ""
    start, max_len = 0, 1
    
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
        
    for i in range(len(s)):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        length = max(len1, len2)
        if length > max_len:
            max_len = length
            start = i - (length - 1) // 2
            
    return s[start:start + max_len]"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef longestPalindrome(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    s = data[0] if len(data) > 0 else \"\"\n    print(longestPalindrome(s))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nstring longestPalindrome(string s) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string s;\n    if (getline(cin, s)) {\n        if (!s.empty() && s.back() == '\\r') s.pop_back();\n        cout << longestPalindrome(s) << endl;\n    } else {\n        cout << longestPalindrome(\"\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String longestPalindrome(String s) {\n        // User logic\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine();\n            System.out.println(longestPalindrome(s));\n        } else {\n            System.out.println(longestPalindrome(\"\"));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction longestPalindrome(s) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length > 0) {\n    let s = input[0];\n    if (s.endsWith('\\r')) s = s.slice(0, -1);\n    console.log(longestPalindrome(s));\n} else {\n    console.log(longestPalindrome(\"\"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* longestPalindrome(char* s) {\n    // User logic\n    return strdup(\"\");\n}\n\nint main() {\n    char s[100000];\n    if (fgets(s, sizeof(s), stdin)) {\n        s[strcspn(s, \"\\r\\n\")] = 0;\n        char* res = longestPalindrome(s);\n        printf(\"%s\\n\", res ? res : \"\");\n    } else {\n        char* res = longestPalindrome(\"\");\n        printf(\"%s\\n\", res ? res : \"\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "babad", "expected_output": "bab", "is_sample": True},
        {"input": "cbbd", "expected_output": "bb", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "a", "expected_output": "a", "is_sample": False},
        {"input": "ac", "expected_output": "a", "is_sample": False},
        {"input": "racecar", "expected_output": "racecar", "is_sample": False},
        {"input": "abbcccbbb", "expected_output": "bbb", "is_sample": False},
        {"input": "aaaa", "expected_output": "aaaa", "is_sample": False},
        # Last three: Stress tests
        {"input": "a" * 1000, "expected_output": "a" * 1000, "is_sample": False},
        {"input": "abcde" * 200, "expected_output": "a", "is_sample": False},
        {"input": "a" * 500 + "b" + "a" * 499, "expected_output": "a" * 499 + "b" + "a" * 499, "is_sample": False}
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
        "topics": ["String", "Dynamic Programming"],
        "companyIndex": 0
    }

    output_path = "1-200/5_Longest_Palindromic_Substring.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
