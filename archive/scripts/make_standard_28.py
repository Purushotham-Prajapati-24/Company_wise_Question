import json
import os

def generate_json():
    problem_id = 28
    title = "Find the Index of the First Occurrence in a String"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>28. Find the Index of the First Occurrence in a String</h3>
<p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;sad&quot; occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>"""

    input_format = "Line 1: The string 'haystack'.\nLine 2: The string 'needle'."
    output_format = "An integer representing the first index of 'needle' in 'haystack'."
    
    constraints = [
        "1 <= haystack.length, needle.length <= 10^4",
        "haystack and needle consist of only lowercase English characters."
    ]
    
    explanation = """To find the first occurrence of a 'needle' string within a 'haystack' string:
1. Iterate through the `haystack` from index `i = 0` up to `len(haystack) - len(needle)`. This ensures there are enough characters remaining in `haystack` to potentially match `needle`.
2. For each index `i`, check if the substring `haystack[i : i + len(needle)]` is equal to `needle`.
3. If a match is found, return the current index `i` immediately as it is the first occurrence.
4. If the loop finishes without any matches being found, return -1.
5. While more advanced string-searching algorithms like Knuth-Morris-Pratt (KMP) or Boyer-Moore exist, the sliding window approach with string comparison is efficient for the given constraints.

Time Complexity: O(H * N) in the worst case (where H and N are lengths of haystack and needle), though average performance is much faster.
Space Complexity: O(1) beyond the input strings."""
    
    answer = """def strStr(haystack, needle):
    if not needle:
        return 0
    h_len = len(haystack)
    n_len = len(needle)
    for i in range(h_len - n_len + 1):
        if haystack[i : i + n_len] == needle:
            return i
    return -1"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef strStr(haystack, needle):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    haystack = input_data[0].strip() if len(input_data) > 0 else \"\"\n    needle = input_data[1].strip() if len(input_data) > 1 else \"\"\n    print(strStr(haystack, needle))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint strStr(string haystack, string needle) {\n    // User logic\n    return -1;\n}\n\nint main() {\n    string h, n;\n    if (getline(cin, h)) {\n        if (h.length() > 0 && h[h.length()-1] == '\\r') h.pop_back();\n        if (getline(cin, n)) {\n            if (n.length() > 0 && n[n.length()-1] == '\\r') n.pop_back();\n            cout << strStr(h, n) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int strStr(String haystack, String needle) {\n        // User logic\n        return -1;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String h = sc.nextLine().trim();\n            if (sc.hasNextLine()) {\n                String n = sc.nextLine().trim();\n                System.out.println(strStr(h, n));\n            }\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction strStr(haystack, needle) {\n    // User logic\n    return -1;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nif (input.length >= 2) {\n    const haystack = input[0].trim();\n    const needle = input[1].trim();\n    console.log(strStr(haystack, needle));\n} else {\n    console.log(-1);\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n\nint strStr(char * haystack, char * needle) {\n    // User logic\n    return -1;\n}\n\nint main() {\n    char h[10005];\n    char n[10005];\n    if (scanf(\"%s\", h) == 1 && scanf(\"%s\", n) == 1) {\n        printf(\"%d\\n\", strStr(h, n));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "sadbutsad\nsad", "expected_output": "0", "is_sample": True},
        {"input": "leetcode\nleeto", "expected_output": "-1", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "hello\nll", "expected_output": "2", "is_sample": False},
        {"input": "aaaaa\nbba", "expected_output": "-1", "is_sample": False},
        {"input": "mississippi\nissip", "expected_output": "4", "is_sample": False},
        {"input": "abc\nabc", "expected_output": "0", "is_sample": False},
        {"input": "a\na", "expected_output": "0", "is_sample": False},
        # Last three: Stress tests
        {"input": "a"*5000 + "\na"*100, "expected_output": "0", "is_sample": False},
        {"input": "a"*5000 + "\nb", "expected_output": "-1", "is_sample": False},
        {"input": "ab" * 2500 + "\nba", "expected_output": "1", "is_sample": False}
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
        "topics": ["Two Pointers", "String", "String Matching"],
        "companyIndex": 0
    }

    output_path = "1-200/28_Find_the_Index_of_the_First_Occurrence_in_a_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
