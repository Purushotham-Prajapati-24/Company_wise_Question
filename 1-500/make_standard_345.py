import json
import os

def solve_reverse_vowels(s):
    s_list = list(s)
    vowels = set("aeiouAEIOU")
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return "".join(s_list)

def generate_json():
    problem_id = 345
    title = "Reverse Vowels of a String"
    difficulty = "Easy"
    marks = 10

    html_description = """<h3>345. Reverse Vowels of a String</h3>
<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>
<p>The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>, and they can appear in both lower and upper cases, more than once.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "hello"
<strong>Output:</strong> "holle"
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> "leotcede"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
\t<li><code>s</code> consists of printable ASCII characters.</li>
</ul>"""

    input_format = "A single string `s` on one line (no quotes)."
    output_format = "A single string with only the vowels reversed (no quotes)."

    constraints = [
        "1 <= s.length <= 300,000",
        "s consists of printable ASCII characters."
    ]

    explanation = """To reverse only the vowels in a string, use the **Two Pointers** technique.

### Algorithm Steps:
1. **Identify Vowels**: Use a set for O(1) lookup: `{'a','e','i','o','u','A','E','I','O','U'}`.
2. **Initialize Pointers**: `left = 0`, `right = len(s) - 1`.
3. **Loop** while `left < right`:
   - Advance `left` until `s[left]` is a vowel.
   - Advance `right` until `s[right]` is a vowel.
   - Swap `s[left]` and `s[right]`, then increment `left` and decrement `right`.
4. Return `"".join(s)`.

### Complexity:
- **Time**: O(N) — each character visited at most once.
- **Space**: O(N) — temporary list for immutable string."""

    answer = """def reverseVowels(s: str) -> str:
    s_list = list(s)
    vowels = set("aeiouAEIOU")
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return "".join(s_list)"""

    boilerplate = {
        "python": "import sys\nimport re\n\nclass Solution:\n    def reverseVowels(self, s: str) -> str:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    match = re.search(r'\"([^\"]*)\"', input_data)\n    s = match.group(1) if match else input_data.strip('\"')\n    \n    sol = Solution()\n    print(sol.reverseVowels(s))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    string reverseVowels(string s) {\n        // User logic here\n        return \"\";\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n\n    regex s_re(R\"(\"([^\"]*)\")\");\n    smatch m;\n    string s = \"\";\n    if (regex_search(input, m, s_re)) s = m[1].str();\n    else s = input; // Fallback\n\n    Solution sol;\n    cout << sol.reverseVowels(s) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public String reverseVowels(String s) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n\n        String s = \"\";\n        Matcher m = Pattern.compile(\"\\\"([^\\\"]*)\\\"\").matcher(input);\n        if (m.find()) s = m.group(1);\n        else s = input.trim().replace(\"\\\"\", \"\");\n\n        Solution sol = new Solution();\n        System.out.println(sol.reverseVowels(s));\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\n/**\n * @param {string} s\n * @return {string}\n */\nvar reverseVowels = function(s) {\n    // User logic here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const match = input.match(/\"([^\"]*)\"/);\n    const s = match ? match[1] : input.replace(/\"/g, '');\n\n    console.log(reverseVowels(s));\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* reverseVowels(char* s) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    static char buffer[1000000];\n    int len = fread(buffer, 1, 999999, stdin); buffer[len] = '\\0';\n\n    char *s = buffer;\n    char *start = strchr(buffer, '\"');\n    if (start) {\n        start++;\n        char *end = strchr(start, '\"');\n        if (end) {\n            *end = '\\0';\n            s = start;\n        }\n    }\n\n    printf(\"%s\\n\", reverseVowels(s));\n    return 0;\n}"
    }


    # Precompute stress test data
    stress1_s = "hello" * 60000           # 300000 chars
    stress1_out = solve_reverse_vowels(stress1_s)

    stress2_s = ("A" * 150000) + ("a" * 150000)
    stress2_out = ("a" * 150000) + ("A" * 150000)

    stress3_s = "bcdfg" * 60000           # 300000 chars, no vowels at all
    stress3_out = stress3_s               # unchanged

    test_cases = [
        # 2 sample cases from LeetCode
        {"input": "hello", "expected_output": "holle", "is_sample": True},
        {"input": "leetcode", "expected_output": "leotcede", "is_sample": True},
        # 5 diverse cases
        {"input": "aA", "expected_output": "Aa", "is_sample": False},
        {"input": "race car", "expected_output": "race car", "is_sample": False},
        {"input": "abcde", "expected_output": "ebcda", "is_sample": False},
        {"input": "bcdfg", "expected_output": "bcdfg", "is_sample": False},
        {"input": "AaEeIiOoUu", "expected_output": "uUoOiIeEaA", "is_sample": False},
        # 3 stress cases (actual computed values)
        {"input": stress1_s, "expected_output": stress1_out, "is_sample": False},
        {"input": stress2_s, "expected_output": stress2_out, "is_sample": False},
        {"input": stress3_s, "expected_output": stress3_out, "is_sample": False},
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
        "companyIndex": 1
    }

    output_path = "301-500/345_Reverse_Vowels_of_a_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
