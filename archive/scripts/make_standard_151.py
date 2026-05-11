import json
import os

def generate_json():
    problem_id = 151
    title = "Reverse Words in a String"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>151. Reverse Words in a String</h3>
<p>Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.</p>

<p>A <strong>word</strong> is defined as a sequence of non-space characters. The <strong>words</strong> in <code>s</code> will be separated by at least one space.</p>

<p>Return <em>a string of the words in reverse order concatenated by a single space.</em></p>

<p><b>Note</b> that <code>s</code> may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "the sky is blue"
<strong>Output:</strong> "blue is sky the"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "  hello world  "
<strong>Output:</strong> "world hello"
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "a good   example"
<strong>Output:</strong> "example good a"
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>' '</code>.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
</ul>

<p>&nbsp;</p>
<p><b>Follow-up:&nbsp;</b>If the string data type is mutable in your language, can&nbsp;you solve it&nbsp;<b>in-place</b>&nbsp;with&nbsp;<code>O(1)</code>&nbsp;extra space?</p>"""

    input_format = "A single line containing the string s."
    output_format = "A single line containing the reversed words joined by a single space."
    
    constraints = [
        "1 <= s.length <= 10^4",
        "s contains English letters, digits, and spaces.",
        "At least one word exists."
    ]
    
    explanation = """To reverse the words in a string efficiently:
1. **Split the String**:
   - Use the built-in `split()` method which, by default, splits by any whitespace and ignores leading/trailing or multiple consecutive spaces.
   - This results in a list of words.
2. **Reverse the List**:
   - Reverse the order of elements in the list.
3. **Join the Words**:
   - Join the reversed list back into a single string using a single space `' '` as a separator.
4. **Complexity**:
   - Time Complexity: O(N) where N is the length of the string.
   - Space Complexity: O(N) to store the list of words."""
    
    answer = """def reverseWords(s: str) -> str:
    # Python's split() with no arguments handles multiple spaces automatically
    words = s.split()
    # Reverse the list of words
    words.reverse()
    # Join with a single space
    return " ".join(words)"""

    boilerplate = {
        "python": "import sys\n\ndef reverseWords(s):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    if data:\n        print(reverseWords(data.strip(\"\\n\")))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\nstring reverseWords(string s){\n    // User logic\n    return \"\";\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    cout<<reverseWords(line)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static String reverseWords(String s){\n        // User logic\n        return \"\";\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null) return;\n        System.out.println(reverseWords(line));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction reverseWords(s){\n    // User logic\n    return '';\n}\nconst line=fs.readFileSync(0,'utf8');\nconst res=reverseWords(line.replace(/\\r?\\n$/,''));\nconsole.log(res);",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nchar* reverseWords(char* s){\n    // User logic\n    return NULL;\n}\nint main(){\n    static char buf[20002]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int l=strlen(buf); if(l>0&&buf[l-1]=='\\n') buf[--l]='\\0';\n    char*res=reverseWords(buf);\n    if(res) printf(\"%s\\n\",res);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "the sky is blue", "expected_output": "blue is sky the", "is_sample": True},
        {"input": "  hello world  ", "expected_output": "world hello", "is_sample": True},
        {"input": "a good   example", "expected_output": "example good a", "is_sample": True},
        {"input": "house", "expected_output": "house", "is_sample": False},
        {"input": "EPIC FAIL", "expected_output": "FAIL EPIC", "is_sample": False},
        {"input": "1 2 3 4 5", "expected_output": "5 4 3 2 1", "is_sample": False},
        {"input": "Abc Def Ghi", "expected_output": "Ghi Def Abc", "is_sample": False},
        # Stress cases
        {"input": " " * 100 + "word" + " " * 100, "expected_output": "word", "is_sample": False},
        {"input": "a " * 5000 + "b", "expected_output": "b " + "a " * 4999 + "a", "is_sample": False},
        {"input": "123 " * 1000, "expected_output": ("123 " * 1000).strip()[::-1].replace('321', '123')[::-1], "is_sample": False}
    ]
    
    # Correction for last test case output (just reverse words)
    test_cases[9]["expected_output"] = " ".join(["123"] * 1000)

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
        "companyIndex": 0
    }

    output_path = "1-200/151_Reverse_Words_in_a_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
