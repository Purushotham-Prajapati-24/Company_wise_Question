import json
import os

def generate_json():
    problem_id = 591
    title = "Tag Validator"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>591. Tag Validator</h3>
<p>Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.</p>

<p>A code snippet is valid if all the following rules hold:</p>

<ol>
    <li>The code must be wrapped in a <b>valid closed tag</b>. Otherwise, the code is invalid.</li>
    <li>A <b>closed tag</b> (not necessarily valid) has exactly the following format : <code>&lt;TAG_NAME&gt;TAG_CONTENT&lt;/TAG_NAME&gt;</code>. Among them, <code>&lt;TAG_NAME&gt;</code> is the start tag, and <code>&lt;/TAG_NAME&gt;</code> is the end tag. The TAG_NAME in start and end tags must be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.</li>
    <li>A <b>valid <code>TAG_NAME</code></b> only contain <b>upper-case letters</b>, and has length in range [1,9]. Otherwise, the <code>TAG_NAME</code> is invalid.</li>
    <li>A <b>valid <code>TAG_CONTENT</code></b> may contain other valid closed tags, cdata and any characters (see note1) <b>EXCEPT</b> unmatched <code>&lt;</code>, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the <code>TAG_CONTENT</code> is invalid.</li>
    <li>A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.</li>
    <li>A <code>&lt;</code> is unmatched if you cannot find a subsequent <code>&gt;</code>. And when you find a <code>&lt;</code> or <code>&lt;/</code>, all the subsequent characters until the next <code>&gt;</code> should be parsed as TAG_NAME (not necessarily valid).</li>
    <li>The cdata has the following format : <code>&lt;![CDATA[CDATA_CONTENT]]&gt;</code>. The range of <code>CDATA_CONTENT</code> is defined as the characters between <code>&lt;![CDATA[</code> and the <b>first subsequent</b> <code>]]&gt;</code>.</li>
    <li><code>CDATA_CONTENT</code> may contain <b>any characters</b>. The function of cdata is to forbid the validator to parse <code>CDATA_CONTENT</code>, so even if it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as <b>regular characters</b>.</li>
</ol>

<p><b>Note:</b> You should treat '<code>&lt;</code>' and '<code>&gt;</code>' as regular characters in CDATA_CONTENT. You do not need to deal with any escape characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> code = "&lt;DIV&gt;This is the first line &lt;![CDATA[&lt;div&gt;]]&gt;&lt;/DIV&gt;"
<strong>Output:</strong> true
<strong>Explanation:</strong> 
The code is wrapped in a closed tag : &lt;DIV&gt; and &lt;/DIV&gt;. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> code = "&lt;DIV&gt;&gt;&gt;  ![cdata[]] &lt;![CDATA[&lt;div&gt;]&gt;]]&gt;]]&gt;&gt;]&lt;/DIV&gt;"
<strong>Output:</strong> true
<strong>Explanation:</strong>
The TAG_CONTENT is valid. Its cdata is <code>&lt;![CDATA[&lt;div&gt;]&gt;]]&gt;</code> and its content is <code>&lt;div&gt;]&gt;</code>.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> code = "&lt;A&gt;  &lt;B&gt; &lt;/A&gt;   &lt;/B&gt;"
<strong>Output:</strong> false
<strong>Explanation:</strong> Unbalanced. If "&lt;A&gt;" is closed, then "&lt;B&gt;" must be unmatched, and vice versa.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= code.length &lt;= 500</code></li>
    <li><code>code</code> consists of English letters, digits, <code>'&lt;'</code>, <code>'&gt;'</code>, <code>'/'</code>, <code>'!'</code>, <code>'['</code>, <code>']'</code>, <code>'.'</code>, and <code>' '</code>.</li>
</ul>"""

    input_format = "A single line: a JSON string `code`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= code.length <= 500",
        "code only contains English letters, digits, <, >, /, !, [, ], ., and space."
    ]

    explanation = """Use a stack to validate tags. Process string from left to right. When starting with '<', distinguish CDATA (starts with `<![CDATA[`), closing tag (`</`), and opening tag. Enforce tag length and uppercase rules. Also enforce that everything must be strictly inside exactly one root tag."""

    answer = """class Solution:
    def isValid(self, code: str) -> bool:
        if not code or code[0] != '<':
            return False
        
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            if i > 0 and len(stack) == 0:
                return False
                
            if code.startswith("<![CDATA[", i):
                j = i + 9
                i = code.find("]]>", j)
                if i < 0:
                    return False
                i += 3
            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)
                if i < 0:
                    return False
                tagname = code[j:i]
                if not stack or stack[-1] != tagname:
                    return False
                stack.pop()
                i += 1
            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)
                if i < 0:
                    return False
                tagname = code[j:i]
                if not (1 <= len(tagname) <= 9) or not all(c.isupper() for c in tagname):
                    return False
                stack.append(tagname)
                i += 1
            else:
                i += 1
                
        return len(stack) == 0"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isValid(self, code: str) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        code = json.loads(raw)
        sol = Solution()
        print("true" if sol.isValid(code) else "false")""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValid(string code) {
        // User logic here
        return false;
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        cout << (sol.isValid(input) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isValid(String code) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() >= 2 && raw.startsWith("\\""))
                raw = raw.substring(1, raw.length() - 1);
            Solution sol = new Solution();
            System.out.println(sol.isValid(raw) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {string} code
 * @return {boolean}
 */
var isValid = function(code) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const code = JSON.parse(input);
    console.log(isValid(code) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool isValid(char* code) {
    // User logic here
    return false;
}

int main() {
    char input[5000];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char code[5000];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(code, input + 1, len - 2);
            code[len - 2] = '\\0';
        } else {
            strcpy(code, input);
        }
        printf("%s\\n", isValid(code) ? "true" : "false");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"<DIV>This is the first line <![CDATA[<div>]]></DIV>"', "expected_output": "true", "is_sample": True},
        {"input": '"<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"', "expected_output": "true", "is_sample": True},
        {"input": '"<A>  <B> </A>   </B>"', "expected_output": "false", "is_sample": True},
        {"input": '"<DIV>  div tag is not closed  <DIV>"', "expected_output": "false", "is_sample": False},
        {"input": '"<DIV>  unmatched <  </DIV>"', "expected_output": "false", "is_sample": False},
        {"input": '"<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"', "expected_output": "false", "is_sample": False},
        {"input": '"<DIV> unmatched tags with invalid tag name  </1234567890> and <some/tag/with/length/larger/than/nine> </DIV>"', "expected_output": "false", "is_sample": False},
        {"input": '"<A></A><B></B>"', "expected_output": "false", "is_sample": False},
        {"input": '"<A><![CDATA[</A>]]123]]></A>"', "expected_output": "false", "is_sample": False},
        {"input": '"<A></A>"', "expected_output": "true", "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Stack"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
