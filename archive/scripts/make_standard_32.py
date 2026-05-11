import json
import os

def generate_json():
    problem_id = 32
    title = "Longest Valid Parentheses"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>32. Longest Valid Parentheses</h3>
<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, return <em>the length of the longest valid (well-formed) parentheses </em> <span class="text-filler"><em>substring</em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)()())&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()()&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, or <code>&#39;)&#39;</code>.</li>
</ul>"""

    input_format = "A single string 's' containing only characters '(' and ')'."
    output_format = "An integer representing the length of the longest valid parentheses substring."
    
    constraints = [
        "0 <= s.length <= 3 * 10^4",
        "s[i] is '(' or ')'."
    ]
    
    explanation = """To find the length of the longest valid parentheses substring:
1. Use a stack to track indices of parentheses. Initialize the stack with `-1` to serve as a boundary for the first potential valid substring.
2. Iterate through the string:
   - If the current character is '(':
     - Push its index onto the stack.
   - If the current character is ')':
     - Pop the top index from the stack.
     - If the stack becomes empty after popping:
       - Push the current index onto the stack. This index now acts as the new boundary for subsequent valid substrings.
     - If the stack is not empty:
       - Calculate the length of the current valid substring as `current_index - stack_top_index`.
       - Update the maximum length found so far.
3. This single-pass stack approach correctly handles nested and consecutive valid parentheses.

Time Complexity: O(N) where N is the length of the string.
Space Complexity: O(N) for the stack in the worst case."""
    
    answer = """def longestValidParentheses(s):
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef longestValidParentheses(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data.startswith('\"') and data.endswith('\"'):\n        data = data[1:-1]\n    print(longestValidParentheses(data))",
        "cpp": "#include <iostream>\n#include <string>\n\nusing namespace std;\n\nint longestValidParentheses(string s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string s;\n    if (cin >> s) {\n        if (s.length() >= 2 && s.front() == '\"' && s.back() == '\"') {\n            s = s.substr(1, s.length() - 2);\n        }\n        cout << longestValidParentheses(s) << endl;\n    } else {\n        cout << longestValidParentheses(\"\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int longestValidParentheses(String s) {\n        // User logic\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNext()) {\n            String s = sc.next();\n            if (s.length() >= 2 && s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) {\n                s = s.substring(1, s.length() - 1);\n            }\n            System.out.println(longestValidParentheses(s));\n        } else {\n            System.out.println(longestValidParentheses(\"\"));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction longestValidParentheses(s) {\n    // User logic\n    return 0;\n}\n\nlet input = fs.readFileSync(0, 'utf-8').trim();\nif (input.length >= 2 && input.startsWith('\"') && input.endsWith('\"')) {\n    input = input.slice(1, -1);\n}\nconsole.log(longestValidParentheses(input));",
        "c": "#include <stdio.h>\n#include <string.h>\n\nint longestValidParentheses(char * s) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    char s[30005];\n    if (scanf(\"%30004s\", s) == 1) {\n        int len = strlen(s);\n        if (len >= 2 && s[0] == '\"' && s[len-1] == '\"') {\n            s[len-1] = '\\0';\n            printf(\"%d\\n\", longestValidParentheses(s + 1));\n        } else {\n            printf(\"%d\\n\", longestValidParentheses(s));\n        }\n    } else {\n        char empty[] = \"\";\n        printf(\"%d\\n\", longestValidParentheses(empty));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "(()", "expected_output": "2", "is_sample": True},
        {"input": ")()())", "expected_output": "4", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "\"\"", "expected_output": "0", "is_sample": False},
        {"input": "((()))", "expected_output": "6", "is_sample": False},
        {"input": "()()()", "expected_output": "6", "is_sample": False},
        {"input": "(()())", "expected_output": "6", "is_sample": False},
        {"input": "()(()", "expected_output": "2", "is_sample": False},
        # Last three: Stress tests
        {"input": "("*100 + ")"*100, "expected_output": "200", "is_sample": False},
        {"input": ")"*100, "expected_output": "0", "is_sample": False},
        {"input": "()"*100, "expected_output": "200", "is_sample": False}
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
        "topics": ["String", "Dynamic Programming", "Stack"],
        "companyIndex": 0
    }

    output_path = "1-200/32_Longest_Valid_Parentheses.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
