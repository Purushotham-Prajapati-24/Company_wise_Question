import json
import os
from collections import Counter

def generate_json():
    problem_id = 76
    title = "Minimum Window Substring"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>76. Minimum Window Substring</h3>
<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>""</code>.</p>

<p>The test cases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "ADOBECODEBANC", t = "ABC"
<strong>Output:</strong> "BANC"
<strong>Explanation:</strong> The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "a", t = "a"
<strong>Output:</strong> "a"
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "a", t = "aa"
<strong>Output:</strong> ""
<strong>Explanation:</strong> Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?"""

    input_format = "Two lines: the first containing string 's' and the second containing string 't'."
    output_format = "A string representing the minimum window substring, or an empty string if none exists."
    
    constraints = [
        "1 <= s.length, t.length <= 10^5",
        "s and t consist of uppercase and lowercase English letters.",
        "Must run in O(m + n) time."
    ]
    
    explanation = """To find the minimum window substring using a sliding window:
1. **Target Counts**: Count the frequency of each character in string `t`. Let `required` be the number of unique characters in `t` that must be present in our window.
2. **Expand the Window**: Move a `right` pointer across string `s`. Keep track of the characters in the current window using a map.
   - If the current character's count in the window matches its required count in `t`, increment a `formed` counter.
3. **Shrink the Window**: Whenever `formed` equals `required`, we have a valid window. Now, try to minimize it by moving a `left` pointer:
   - Record the window's boundaries if it's the smallest found so far.
   - Remove the character at `left` from the window map.
   - If removing that character causes its count to drop below the required frequency, decrement the `formed` counter.
   - Move the `left` pointer forward.
4. **Complexity**:
   - Time Complexity: O(M + N), where M and N are lengths of `s` and `t`. Each character in `s` is processed at most twice (once by `right` and once by `left`).
   - Space Complexity: O(K), where K is the number of unique characters (at most 52)."""
    
    answer = """from collections import Counter

def minWindow(s, t):
    if not t or not s:
        return \"\"
        
    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(t)
    required = len(dict_t)
    
    # left and right pointer
    l, r = 0, 0
    formed = 0
    
    # window_counts dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}
    
    # ans tuple of (window length, left, right)
    ans = float(\"inf\"), None, None
    
    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # If the frequency of the current character added equals to the desired count in t then increment formed.
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
            
        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            char = s[l]
            
            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
                
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
                
            # Move the left pointer ahead, this would help to look for a new window.
            l += 1    
        r += 1    
        
    return \"\" if ans[0] == float(\"inf\") else s[ans[1] : ans[2] + 1]"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\nfrom collections import Counter\n\ndef minWindow(s, t):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    s = lines[0].strip() if len(lines) > 0 else \"\"\n    t = lines[1].strip() if len(lines) > 1 else \"\"\n    print(minWindow(s, t))",
        "cpp": "#include <iostream>\n#include <string>\n#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\nstring minWindow(string s, string t) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    string s, t;\n    if (getline(cin, s) && getline(cin, t)) {\n        cout << minWindow(s, t) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static String minWindow(String s, String t) {\n        // User logic\n        return \"\";\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String s = sc.hasNextLine() ? sc.nextLine() : \"\";\n        String t = sc.hasNextLine() ? sc.nextLine() : \"\";\n        System.out.println(minWindow(s, t));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction minWindow(s, t) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nconst s = input[0] ? input[0].trim() : \"\";\nconst t = input[1] ? input[1].trim() : \"\";\nconsole.log(minWindow(s, t));",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nchar* minWindow(char* s, char* t) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    char s[100001], t[100001];\n    if (fgets(s, sizeof(s), stdin)) {\n        int l = strlen(s); if (l > 0 && s[l-1] == '\\n') s[l-1] = '\\0';\n    }\n    if (fgets(t, sizeof(t), stdin)) {\n        int l = strlen(t); if (l > 0 && t[l-1] == '\\n') t[l-1] = '\\0';\n    }\n    char* res = minWindow(s, t);\n    printf(\"%s\\n\", res);\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "ADOBECODEBANC\\nABC", "expected_output": "BANC", "is_sample": True},
        {"input": "a\\na", "expected_output": "a", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "a\\naa", "expected_output": "", "is_sample": False},
        {"input": "abc\\ncab", "expected_output": "abc", "is_sample": False},
        {"input": "ab\\nba", "expected_output": "ab", "is_sample": False},
        {"input": "abc\\nb", "expected_output": "b", "is_sample": False},
        {"input": "aabacbebebe\\nabc", "expected_output": "abac", "is_sample": False},
        # Last three: Stress tests
        {"input": "a"*100000 + "\\nb", "expected_output": "", "is_sample": False},
        {"input": "a"*100000 + "\\naa", "expected_output": "aa", "is_sample": False},
        {"input": "AaBbCc"*10000 + "\\nABC", "expected_output": "AaBbC", "is_sample": False}
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

    output_path = "1-200/76_Minimum_Window_Substring.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
