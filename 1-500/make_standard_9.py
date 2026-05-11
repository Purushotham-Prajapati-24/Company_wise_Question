import json
import os

def generate_json():
    problem_id = 9
    title = "Palindrome Number"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>9. Palindrome Number</h3>
<p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span data-keyword="palindrome-integer"><em><strong>palindrome</strong></em></span><em>, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?"""

    input_format = "A single integer 'x'."
    output_format = "true or false."
    
    constraints = [
        "-2^31 <= x <= 2^31 - 1"
    ]
    
    explanation = """To check if an integer is a palindrome without converting to a string:
1. Handle negative integers immediately: they are never palindromes (due to the '-' sign).
2. Handle cases where the last digit is 0: if 'x' is not 0, any number ending in 0 is not a palindrome.
3. Reverse the second half of the number and compare it with the first half.
4. To reverse only half: 
   - Extract digits from the end of 'x' and accumulate them in a 'reverted' variable.
   - Stop when 'x' becomes smaller than or equal to 'reverted'.
5. For numbers with an odd count of digits: result is based on 'x' == 'reverted // 10'.
6. For numbers with an even count: result is 'x' == 'reverted'.

This ensures O(log10(X)) time complexity and O(1) space complexity by avoiding string conversion."""
    
    answer = """def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef isPalindrome(x: int) -> bool:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().replace('[', '').replace(']', '').replace(',', ' ').split()\n    if data:\n        print(str(isPalindrome(int(data[0]))).lower())",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nbool isPalindrome(int x) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        for(char &c : s) if(c == '[' || c == ']' || c == ',') c = ' ';\n        try {\n            size_t pos;\n            int x = stoi(s, &pos);\n            cout << (isPalindrome(x) ? \"true\" : \"false\") << endl;\n        } catch (...) {}\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static boolean isPalindrome(int x) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next().replaceAll(\"[\\\\[\\\\],]\", \"\");\n            if (!s.isEmpty()) {\n                try {\n                    int x = Integer.parseInt(s);\n                    System.out.println(isPalindrome(x) ? \"true\" : \"false\");\n                } catch (NumberFormatException e) {}\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction isPalindrome(x) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf8').replace(/[\\[\\],]/g, ' ').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    console.log(isPalindrome(parseInt(input[0], 10)) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n#include <stdbool.h>\n\nbool isPalindrome(int x) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    char s[100];\n    if (scanf(\"%99s\", s) == 1) {\n        char cleaned[100];\n        int j = 0;\n        for (int i = 0; s[i]; i++) {\n            if (isdigit(s[i]) || s[i] == '-') {\n                cleaned[j++] = s[i];\n            }\n        }\n        cleaned[j] = '\\0';\n        if (j > 0) {\n            printf(\"%s\\n\", isPalindrome(atoi(cleaned)) ? \"true\" : \"false\");\n        }\n    }\n    return 0;\n}"
    }


    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "121", "expected_output": "true", "is_sample": True},
        {"input": "-121", "expected_output": "false", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "10", "expected_output": "false", "is_sample": False},
        {"input": "0", "expected_output": "true", "is_sample": False},
        {"input": "12321", "expected_output": "true", "is_sample": False},
        {"input": "1221", "expected_output": "true", "is_sample": False},
        {"input": "123", "expected_output": "false", "is_sample": False},
        # Last three: Stress tests
        {"input": "1000000001", "expected_output": "true", "is_sample": False},
        {"input": "1234567899", "expected_output": "false", "is_sample": False},
        {"input": "2147447412", "expected_output": "true", "is_sample": False}
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
        "topics": ["Math"],
        "companyIndex": 0
    }

    output_path = "1-200/9_Palindrome_Number.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
