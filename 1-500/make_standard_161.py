import json
import os

def generate_json():
    problem_id = 161
    title = "One Edit Distance"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>161. One Edit Distance</h3>
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if they are exactly <strong>one edit distance</strong> apart, otherwise return <code>false</code>.</p>

<p>A string <code>s</code> is said to be one edit distance apart from a string <code>t</code> if you can transform <code>s</code> into <code>t</code> by performing <strong>exactly one</strong> of the following operations:</p>
<ul>
    <li><strong>Insert</strong> exactly one character into <code>s</code> to get <code>t</code>.</li>
    <li><strong>Delete</strong> exactly one character from <code>s</code> to get <code>t</code>.</li>
    <li><strong>Replace</strong> exactly one character of <code>s</code> with a different character to get <code>t</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ab", t = "acb"
<strong>Output:</strong> true
<strong>Explanation:</strong> We can insert 'c' into s to get t.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "", t = ""
<strong>Output:</strong> false
<strong>Explanation:</strong> We cannot get t from s by performing only one step.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= s.length, t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase letters, uppercase letters, and digits.</li>
</ul>"""

    input_format = "Two lines. Line 1: string s. Line 2: string t."
    output_format = "A boolean value (true or false)."
    
    constraints = [
        "0 <= s.length, t.length <= 10^4",
        "lowercase, uppercase, and digits."
    ]
    
    explanation = """To determine if two strings are exactly one edit distance apart:
1. **Compare Lengths**:
   - If the difference in lengths is greater than 1, they cannot be one edit distance apart. Return `false`.
2. **Iterate and Compare Characters**:
   - Loop through both strings simultaneously.
   - At the first position `i` where `s[i] != t[i]`:
     - If `len(s) == len(t)`: The strings must be identical after position `i` (Replacement). Check `s[i+1:] == t[i+1:]`.
     - If `len(s) < len(t)`: String `t` must contain the rest of `s` after position `i` (Insertion into `s`). Check `s[i:] == t[i+1:]`.
     - If `len(s) > len(t)`: String `s` must contain the rest of `t` after position `i` (Deletion from `s`). Check `s[i+1:] == t[i:]`.
3. **Handle Completion**:
   - If the loop finishes without finding a difference, it means one string is a prefix of the other. They are one edit distance apart only if the length difference is exactly 1.
4. **Complexity**:
   - Time Complexity: O(N) where N is the length of the shorter string.
   - Space Complexity: O(1) or O(N) depending on substring handling in the language."""
    
    answer = """def isOneEditDistance(s: str, t: str) -> bool:
    ns, nt = len(s), len(t)
    
    # Ensure s is shorter or equal to t
    if ns > nt:
        return isOneEditDistance(t, s)
        
    if nt - ns > 1:
        return False
        
    for i in range(ns):
        if s[i] != t[i]:
            if ns == nt:
                # Replacement
                return s[i+1:] == t[i+1:]
            else:
                # Insertion (in s)
                return s[i:] == t[i+1:]
                
    # No difference found, so s is prefix of t
    return ns + 1 == nt"""

    boilerplate = {
        "python": "import sys\n\ndef isOneEditDistance(s, t):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    s = lines[0] if len(lines) > 0 else \"\"\n    t = lines[1] if len(lines) > 1 else \"\"\n    print(\"true\" if isOneEditDistance(s, t) else \"false\")",
        "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\nbool isOneEditDistance(string s, string t) {\n    // User logic here\n    return false;\n}\nint main(){\n    string s=\"\", t=\"\"; \n    getline(cin,s); if(!s.empty()&&s.back()=='\\r')s.pop_back();\n    getline(cin,t); if(!t.empty()&&t.back()=='\\r')t.pop_back();\n    cout<<(isOneEditDistance(s, t)?\"true\":\"false\")<<endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\npublic class Main {\n    public static boolean isOneEditDistance(String s, String t) {\n        // User logic here\n        return false;\n    }\n    public static void main(String[] args) throws Exception {\n        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));\n        String s=br.readLine(); if(s==null) s=\"\";\n        String t=br.readLine(); if(t==null) t=\"\";\n        System.out.println(isOneEditDistance(s, t)?\"true\":\"false\");\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction isOneEditDistance(s, t) {\n    // User logic here\n    return false;\n}\nconst lines=fs.readFileSync(0,'utf8').split('\\n');\nlet s=lines.length>0?lines[0]:\"\", t=lines.length>1?lines[1]:\"\";\nif(s.endsWith('\\r'))s=s.slice(0,-1); if(t.endsWith('\\r'))t=t.slice(0,-1);\nconsole.log(isOneEditDistance(s, t)?\"true\":\"false\");",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n#include <stdbool.h>\nbool isOneEditDistance(char* s, char* t) {\n    // User logic here\n    return false;\n}\nint main(){\n    char s[10005]={0}, t[10005]={0};\n    if(fgets(s,sizeof(s),stdin)){int l=strlen(s);while(l>0&&(s[l-1]=='\\n'||s[l-1]=='\\r'))s[--l]='\\0';}\n    if(fgets(t,sizeof(t),stdin)){int l=strlen(t);while(l>0&&(t[l-1]=='\\n'||t[l-1]=='\\r'))t[--l]='\\0';}\n    printf(\"%s\\n\",isOneEditDistance(s, t)?\"true\":\"false\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "ab\\nacb", "expected_output": "true", "is_sample": True},
        {"input": "hb\\nh", "expected_output": "true", "is_sample": True},
        {"input": "\\n", "expected_output": "false", "is_sample": True},
        {"input": "abc\\nabc", "expected_output": "false", "is_sample": False},
        {"input": "abc\\nabde", "expected_output": "false", "is_sample": False},
        {"input": "a\\nb", "expected_output": "true", "is_sample": False},
        {"input": "A\\na", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "a"*5000 + "\\n" + "a"*5001, "expected_output": "true", "is_sample": False},
        {"input": "a"*5000 + "\\n" + "a"*4999, "expected_output": "true", "is_sample": False},
        {"input": "a"*10000 + "\\n" + "a"*5000 + "b" + "a"*4999, "expected_output": "true", "is_sample": False}
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
        "companyIndex": 0
    }

    output_path = "1-200/161_One_Edit_Distance.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
