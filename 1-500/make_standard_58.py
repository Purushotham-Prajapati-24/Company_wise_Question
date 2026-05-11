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
        "python": "import sys, re\n\ndef lengthOfLastWord(s):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().rstrip('\\r\\n')\n    match = re.search(r's\\\\s*=\\\\s*\"(.*)\"', data, re.DOTALL)\n    s = match.group(1) if match else (data[1:-1] if data.startswith('\"') and data.endswith('\"') else data)\n    print(lengthOfLastWord(s))",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int lengthOfLastWord(string s) {\n        // User Logic Here\n        return 0;\n    }\n};\n\nint main() {\n    string input, line, s;\n    while(getline(cin, line)) input += line + (cin.eof() ? \"\" : \"\\n\");\n    while(!input.empty() && (input.back() == '\\n' || input.back() == '\\r')) input.pop_back();\n    regex rgx(\"s\\\\s*=\\\\s*\\\"(.*)\\\"\");\n    smatch match;\n    if (regex_search(input, match, rgx)) s = match[1].str();\n    else if (input.size() >= 2 && input.front() == '\"' && input.back() == '\"') s = input.substr(1, input.size() - 2);\n    else s = input;\n    Solution sol;\n    cout << sol.lengthOfLastWord(s) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int lengthOfLastWord(String s) {\n        // User Logic Here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\"\\n\");\n        String input = sb.toString().replaceFirst(\"\\\\n$\", \"\");\n        Matcher m = Pattern.compile(\"s\\\\s*=\\\\s*\\\"(.*)\\\"\", Pattern.DOTALL).matcher(input);\n        String s = m.find() ? m.group(1) : (input.startsWith(\"\\\"\") && input.endsWith(\"\\\"\") ? input.substring(1, input.length() - 1) : input);\n        Solution sol = new Solution();\n        System.out.println(sol.lengthOfLastWord(s));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {string} s\n * @return {number}\n */\nvar lengthOfLastWord = function(s) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').replace(/\\r?\\n$/, '');\n    const match = input.match(/s\\s*=\\s*\"(.*)\"/s);\n    const s = match ? match[1] : (input.startsWith('\"') && input.endsWith('\"') ? input.slice(1, -1) : input);\n    console.log(lengthOfLastWord(s));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint lengthOfLastWord(char* s) {\n    // User Logic Here\n    return 0;\n}\n\nint main() {\n    char* input = malloc(10001);\n    int len = 0, c;\n    while ((c = getchar()) != EOF) input[len++] = c;\n    input[len] = '\\0';\n    while(len > 0 && (input[len-1] == '\\n' || input[len-1] == '\\r')) input[--len] = '\\0';\n    char* s_ptr = input;\n    char* s_eq = strstr(input, \"s = \\\"\");\n    if (s_eq) {\n        s_ptr = s_eq + 5;\n        char* last_quote = strrchr(s_ptr, '\"');\n        if (last_quote) *last_quote = '\\0';\n    } else if (input[0] == '\"' && input[len-1] == '\"') {\n        s_ptr = input + 1; input[len-1] = '\\0';\n    }\n    printf(\"%d\\n\", lengthOfLastWord(s_ptr));\n    return 0;\n}"
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
