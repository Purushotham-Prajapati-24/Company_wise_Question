import json
import os

def generate_json():
    problem_id = 722
    title = "Remove Comments"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>722. Remove Comments</h3>
<p>Given a C++ program, remove comments from it. The program source is an array of strings <code>source</code> where <code>source[i]</code> is the <code>i</code>-th line of the source code. This represents the result of splitting the original source code string by the newline character <code>\\n</code>.</p>
<p>In C++, there are two types of comments, line comments and block comments.</p>
<ul>
	<li>The string <code>//</code> denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.</li>
	<li>The string <code>/*</code> denotes a block comment, which represents that every character until the next (non-overlapping) occurrence of <code>*/</code> should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string <code>/*/</code> does not yet terminate the block comment, as the ending <code>*/</code> overlaps the beginning <code>/*</code>.</li>
</ul>
<p>The first effective comment takes precedence over others. For example, if the string <code>//</code> occurs in a block comment, it is ignored. Similarly, if the string <code>/*</code> occurs in a line or block comment, it is also ignored.</p>
<p>If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.</p>
<p>There will be no control characters, single quote, or double quote characters. For example, <code>source = ["string s = \\"/* Not a comment. */\\";"]</code> will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)</p>
<p>It is guaranteed that every open block comment eventually closes. No <code>/*</code>, <code>//</code> alone will extend it to the next line except for block comments.</p>
<p>After removing the comments from the source code, return the source code in the same format.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
<strong>Output:</strong> ["int main()","{ ","int a, b, c;","a = b + c;","}"]
<strong>Explanation:</strong> The line by line code is visualized below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4.
The characters remaining after deleting the comments are "int main()", "{ ", "int a, b, c;", "a = b + c;", and "}".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> source = ["a/*comment", "line", "more_comment*/b"]
<strong>Output:</strong> ["ab"]
<strong>Explanation:</strong> The original source string is "a/*comment\\nline\\nmore_comment*/b", where we have a block comment. After deleting the comment, we get "ab" as the output.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= source.length &lt;= 100</code></li>
	<li><code>0 &lt;= source[i].length &lt;= 80</code></li>
	<li><code>source[i]</code> consists of printable ASCII characters.</li>
	<li>Every open block comment is eventually closed.</li>
	<li>There are no single-quote or double-quote characters in the input.</li>
</ul>
"""

    input_format = "A JSON list of strings."
    output_format = "A JSON list of strings (non-empty lines)."
    
    constraints = [
        "1 <= source.length <= 100",
        "Block comments /* ... */ can span multiple lines.",
        "Line comments // end at the end of the line.",
        "Remove empty lines from the result."
    ]
    
    explanation = """To remove comments from C++ code:
1. **State Machine / Flag**:
   - Maintain a boolean `in_block` to track if we are currently inside a `/* ... */` comment.
   - Iterate through each character of each line.
2. **Handling Block Comments**:
   - If not `in_block` and we see `/*`: set `in_block = True` and skip next character.
   - If `in_block` and we see `*/`: set `in_block = False` and skip next character.
3. **Handling Line Comments**:
   - If not `in_block` and we see `//`: break the loop for the current line (ignore rest).
4. **Buffering**:
   - Append characters to a current line buffer only if not `in_block`.
   - After processing a line, if buffer is not empty and not `in_block`, add it to results.
   - If `in_block` spans lines, continue adding to the same buffer until `in_block` is False.

Complexity:
- Time: O(N * L) where N is number of lines and L is max length.
- Space: O(N * L) for the result.
"""
    
    answer = """def removeComments(source):
    res = []
    in_block = False
    new_line = []
    for line in source:
        i = 0
        while i < len(line):
            if not in_block and i + 1 < len(line) and line[i:i+2] == '/*':
                in_block = True
                i += 1
            elif in_block and i + 1 < len(line) and line[i:i+2] == '*/':
                in_block = False
                i += 1
            elif not in_block and i + 1 < len(line) and line[i:i+2] == '//':
                break
            elif not in_block:
                new_line.append(line[i])
            i += 1
        if new_line and not in_block:
            res.append("".join(new_line))
            new_line = []
    return res"""

    boilerplate = {
        "python": "import sys\\nimport json\\n\\ndef removeComments(source):\\n    # User logic here\\n    pass\\n\\nif __name__ == '__main__':\\n    source = json.loads(sys.stdin.read().strip())\\n    print(json.dumps(removeComments(source)))",
        "cpp": "#include <iostream>\\n#include <vector>\\n#include <string>\\nusing namespace std;\\n\\nvector<string> removeComments(vector<string>& source) { return {}; }",
        "java": "class Solution { public List<String> removeComments(String[] source) { } }",
        "javascript": "var removeComments = function(source) { };",
        "c": "char** removeComments(char** source, int sourceSize, int* returnSize) { }"
    }

    test_cases = [
        {"input": '["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]', "expected_output": '["int main()", "{ ", "int a, b, c;", "a = b + c;", "}"]', "is_sample": True},
        {"input": '["a/*comment", "line", "more_comment*/b"]', "expected_output": '["ab"]', "is_sample": True},
        {"input": '["struct Node {", "    /* multiline", "       comment */", "    int x;", "};"]', "expected_output": '["struct Node {", "    int x;", "};"]', "is_sample": False},
        {"input": '["// direct line comment", "int x = 5;"]', "expected_output": '["int x = 5;"]', "is_sample": False},
        {"input": '["/* comment */", "/* another */"]', "expected_output": '[]', "is_sample": False},
        {"input": '["int x = 1; // comment", "int y = 2; /* block */", "int z = 3;"]', "expected_output": '["int x = 1; ", "int y = 2; ", "int z = 3;"]', "is_sample": False},
        {"input": '["void func() {", "  // line", "  /* block", "  */", "}"]', "expected_output": '["void func() {", "}"]', "is_sample": False},
        {"input": '["a//*b//*c", "blank", "d/*/e*//f"]', "expected_output": '["a", "blank", "df"]', "is_sample": False},
        # Stress cases
        {"input": json.dumps(["//" + "a"*78 for _ in range(100)]), "expected_output": '[]', "is_sample": False},
        {"input": json.dumps(["/*"] + ["a"*80 for _ in range(98)] + ["*/"]), "expected_output": '[]', "is_sample": False}
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
        "topics": ["Array", "String"],
        "companyIndex": 0
    }

    output_path = "601-800/722_Remove_Comments.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
