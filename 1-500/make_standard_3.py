import json
import os

def generate_json():
    problem_id = 3
    title = "Longest Substring Without Repeating Characters"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>3. Longest Substring Without Repeating Characters</h3>
<p>Given a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "abcabcbb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "abc", with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "bbbbb"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is "b", with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "pwwkew"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>
"""

    input_format = "A single line containing the string 's'."
    output_format = "An integer representing the maximum length of a substring without repeating characters."
    
    constraints = [
        "0 <= s.length <= 5 * 10^4",
        "s consists of English letters, digits, symbols and spaces."
    ]
    
    explanation = """To find the longest substring without repeating characters:
1. Use a 'sliding window' approach with two pointers, 'start' and 'end', to represent the current window.
2. Initialize a hash map 'char_map' to store the last seen position of each character.
3. Iterate through the string with the 'end' pointer:
   - If the current character is already in 'char_map' and its last position is within the current window:
     - Shrink the window by moving the 'start' pointer to 'char_map[s[end]] + 1'.
   - Update 'char_map[s[end]]' with the current 'end' index.
   - Calculate the window length (end - start + 1) and update the maximum length if contemporary length is larger.
4. Return the maximum length found.

Time Complexity: O(N) as we traverse the string once.
Space Complexity: O(min(N, M)) where M is the character set size."""
    
    answer = """def lengthOfLongestSubstring(s):
    char_map = {}
    max_len = 0
    start = 0
    for i in range(len(s)):
        if s[i] in char_map and char_map[s[i]] >= start:
            start = char_map[s[i]] + 1
        char_map[s[i]] = i
        max_len = max(max_len, i - start + 1)
    return max_len"""

    boilerplate = {
        "python": "import sys\n\ndef lengthOfLongestSubstring(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) > 0:\n        s = input_data[0].strip().strip('\"')\n        print(lengthOfLongestSubstring(s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nint lengthOfLongestSubstring(string s) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string s;\n    if (getline(cin, s)) {\n        if (!s.empty() && s.back() == '\\r') s.pop_back();\n        size_t first = s.find_first_not_of(\" \\t\\n\\r\\\"\");\n        if (string::npos == first) {\n            cout << lengthOfLongestSubstring(\"\") << endl;\n            return 0;\n        }\n        size_t last = s.find_last_not_of(\" \\t\\n\\r\\\"\");\n        cout << lengthOfLongestSubstring(s.substr(first, (last - first + 1))) << endl;\n    } else {\n        cout << lengthOfLongestSubstring(\"\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int lengthOfLongestSubstring(String s) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) {\n                s = s.substring(1, s.length() - 1);\n            }\n            System.out.println(lengthOfLongestSubstring(s));\n        } else {\n            System.out.println(lengthOfLongestSubstring(\"\"));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction lengthOfLongestSubstring(s) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length > 0) {\n    let s = input[0].trim();\n    if (s.startsWith('\"') && s.endsWith('\"')) s = s.slice(1, -1);\n    console.log(lengthOfLongestSubstring(s));\n} else {\n    console.log(lengthOfLongestSubstring(\"\"));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint lengthOfLongestSubstring(char * s) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char s[100005];\n    if (fgets(s, sizeof(s), stdin)) {\n        s[strcspn(s, \"\\r\\n\")] = 0;\n        char *start = s;\n        while(*start == ' ' || *start == '\"') start++;\n        char *end = s + strlen(s) - 1;\n        while(end > start && (*end == ' ' || *end == '\"')) {\n            *end = '\\0';\n            end--;\n        }\n        printf(\"%d\\n\", lengthOfLongestSubstring(start));\n    } else {\n        printf(\"%d\\n\", lengthOfLongestSubstring(\"\"));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "abcabcbb", "expected_output": "3", "is_sample": True},
        {"input": "bbbbb", "expected_output": "1", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "pwwkew", "expected_output": "3", "is_sample": False},
        {"input": "", "expected_output": "0", "is_sample": False},
        {"input": " ", "expected_output": "1", "is_sample": False},
        {"input": "au", "expected_output": "2", "is_sample": False},
        {"input": "dvdf", "expected_output": "3", "is_sample": False},
        # Last three: Stress tests
        {"input": "abcdefghijklmnopqrstuvwxyz" * 10, "expected_output": "26", "is_sample": False},
        {"input": "a" * 50000, "expected_output": "1", "is_sample": False},
        {"input": "".join([chr(i % 128) for i in range(50000)]), "expected_output": "128", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = "1-200/3_Longest_Substring_Without_Repeating_Characters.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
