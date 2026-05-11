import json
import os

def generate_json():
    problem_id = 67
    title = "Add Binary"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>67. Add Binary</h3>
<p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>'0'</code> or <code>'1'</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>"""

    input_format = "Two space-separated binary strings 'a' and 'b'."
    output_format = "A binary string representing the sum."
    
    constraints = [
        "1 <= a.length, b.length <= 10^4",
        "a and b consist only of '0' or '1' characters.",
        "No leading zeros except for the zero itself."
    ]
    
    explanation = """To add two binary strings:
1. **Initialize**: Use a pointer for each string (`i` for `a`, `j` for `b`) starting from the end, and a `carry` variable initialized to 0.
2. **Iteration**: Loop while `i >= 0`, `j >= 0`, or `carry > 0`:
   - Get the numeric value of the current binary digit if the pointer is within bounds; otherwise, use 0.
   - Calculate the sum of these values plus the `carry`.
   - The current bit in the total sum is `sum % 2`.
   - The new `carry` is `sum // 2`.
   - Append the current bit to a result list and move pointers to the left.
3. **Finish**: Reverse the result list and join its elements into a single string.
4. **Complexity**:
   - Time Complexity: O(max(N, M)), where N and M are the lengths of strings `a` and `b`.
   - Space Complexity: O(max(N, M)) to store the output string."""
    
    answer = """def addBinary(a, b):
    res = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        val_a = int(a[i]) if i >= 0 else 0
        val_b = int(b[j]) if j >= 0 else 0
        
        total = val_a + val_b + carry
        res.append(str(total % 2))
        carry = total // 2
        
        i -= 1
        j -= 1
        
    return "".join(res[::-1])"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys, re\n\ndef addBinary(a, b):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    strings = re.findall(r'\"(.*?)\"', data)\n    if len(strings) >= 2:\n        a, b = strings[0], strings[1]\n    else:\n        parts = data.split()\n        a = parts[0] if len(parts) > 0 else \"\"\n        b = parts[1] if len(parts) > 1 else \"\"\n    print(addBinary(a, b))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string addBinary(string a, string b) {\n        // User Logic Here\n        return \"\";\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(R\"(\"(.*?)\")\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<string> strings;\n    while (iter != end) { strings.push_back((*iter)[1]); iter++; }\n    string a, b;\n    if (strings.size() >= 2) {\n        a = strings[0]; b = strings[1];\n    } else {\n        stringstream ss(input);\n        ss >> a >> b;\n    }\n    Solution sol;\n    cout << sol.addBinary(a, b) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public String addBinary(String a, String b) {\n        // User Logic Here\n        return \"\";\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\"(.*?)\\\"\").matcher(input);\n        List<String> strings = new ArrayList<>();\n        while (m.find()) strings.add(m.group(1));\n        String a, b;\n        if (strings.size() >= 2) {\n            a = strings.get(0); b = strings.get(1);\n        } else {\n            String[] parts = input.trim().split(/\\\\s+/);\n            a = parts.length > 0 ? parts[0] : \"\";\n            b = parts.length > 1 ? parts[1] : \"\";\n        }\n        Solution sol = new Solution();\n        System.out.println(sol.addBinary(a, b));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {string} a\n * @param {string} b\n * @return {string}\n */\nvar addBinary = function(a, b) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    let strings = (input.match(/\"(.*?)\"/g) || []).map(s => s.slice(1, -1));\n    let a, b;\n    if (strings.length >= 2) {\n        a = strings[0]; b = strings[1];\n    } else {\n        let parts = input.split(/\\s+/);\n        a = parts[0] || \"\";\n        b = parts[1] || \"\";\n    }\n    console.log(addBinary(a, b));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* addBinary(char* a, char* b) {\n    // User Logic Here\n    return NULL;\n}\n\nint main() {\n    char input[2048];\n    if (!fgets(input, sizeof(input), stdin)) return 0;\n    char *a = NULL, *b = NULL;\n    char *s1 = strchr(input, '\"');\n    if (s1) {\n        char *e1 = strchr(s1 + 1, '\"');\n        if (e1) {\n            *e1 = '\\0'; a = s1 + 1;\n            char *s2 = strchr(e1 + 1, '\"');\n            if (s2) {\n                char *e2 = strchr(s2 + 1, '\"');\n                if (e2) { *e2 = '\\0'; b = s2 + 1; }\n            }\n        }\n    }\n    if (!a || !b) {\n        a = strtok(input, \" \\n\\r\");\n        b = strtok(NULL, \" \\n\\r\");\n    }\n    if (a && b) printf(\"%s\\n\", addBinary(a, b));\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "11 1", "expected_output": "100", "is_sample": True},
        {"input": "1010 1011", "expected_output": "10101", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "0 0", "expected_output": "0", "is_sample": False},
        {"input": "1 1", "expected_output": "10", "is_sample": False},
        {"input": "111 111", "expected_output": "1110", "is_sample": False},
        {"input": "100 0", "expected_output": "100", "is_sample": False},
        {"input": "0 100", "expected_output": "100", "is_sample": False},
        # Last three: Stress tests
        {"input": "1"*10000 + " 1", "expected_output": "1" + "0"*10000, "is_sample": False},
        {"input": "1"*5000 + " " + "1"*5000, "expected_output": "1" + "1"*4999 + "0", "is_sample": False},
        {"input": "1"*10000 + " " + "0"*10000, "expected_output": "1"*10000, "is_sample": False}
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
        "topics": ["Math", "String", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "1-200/67_Add_Binary.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
