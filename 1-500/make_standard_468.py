import json
import os

def generate_json():
    problem_id = 468
    title = "Validate IP Address"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>468. Validate IP Address</h3>
<p>Given a string <code>queryIP</code>, return <code>"IPv4"</code> if IP is a valid IPv4 address, <code>"IPv6"</code> if IP is a valid IPv6 address or <code>"Neither"</code> if IP is not a correct IP of any type.</p>

<p><strong>A valid IPv4</strong> address is an IP in the form <code>"x<sub>1</sub>.x<sub>2</sub>.x<sub>3</sub>.x<sub>4</sub>"</code> where <code>0 &lt;= x<sub>i</sub> &lt;= 255</code> and <code>x<sub>i</sub></code> <strong>cannot contain</strong> leading zeros. For example, <code>"192.168.1.1"</code> and <code>"192.168.1.0"</code> are valid IPv4 addresses while <code>"192.168.01.1"</code>, <code>"192.168.1.00"</code>, and <code>"192.168@1.1"</code> are invalid IPv4 addresses.</p>

<p><strong>A valid IPv6</strong> address is an IP in the form <code>"x<sub>1</sub>:x<sub>2</sub>:x<sub>3</sub>:x<sub>4</sub>:x<sub>5</sub>:x<sub>6</sub>:x<sub>7</sub>:x<sub>8</sub>"</code> where:</p>
<ul>
	<li><code>1 &lt;= x<sub>i</sub>.length &lt;= 4</code></li>
	<li><code>x<sub>i</sub></code> is a <strong>hexadecimal string</strong> which may contain digits, lowercase English letters (<code>'a'</code> to <code>'f'</code>) and upper-case English letters (<code>'A'</code> to <code>'F'</code>).</li>
	<li>Leading zeros are allowed in <code>x<sub>i</sub></code>.</li>
</ul>

<p>For example, <code>"2001:0db8:85a3:0000:0000:8a2e:0370:7334"</code> and <code>"2001:db8:85a3:0:0:8A2E:0370:7334"</code> are valid IPv6 addresses, while <code>"2001:0db8:85a3::8A2E:0370:7334"</code> and <code>"02001:0db8:85a3:0000:0000:8a2e:0370:7334"</code> are invalid IPv6 addresses.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> queryIP = "172.16.254.1"
<strong>Output:</strong> "IPv4"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
<strong>Output:</strong> "IPv6"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> queryIP = "256.256.256.256"
<strong>Output:</strong> "Neither"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>queryIP</code> consists only of English letters, digits and the characters <code>'.'</code> and <code>':'</code>.</li>
</ul>"""

    input_format = "Line 1: A string `queryIP`."
    output_format = "A string: \"IPv4\", \"IPv6\", or \"Neither\"."
    
    constraints = [
        "queryIP consists only of English letters, digits, '.', and ':'."
    ]
    
    explanation = "Check for '.' or ':' to determine the potential IP type. For IPv4, split by '.' and ensure there are exactly 4 parts, each part is a number between 0 and 255, and no part has leading zeros unless it is '0'. For IPv6, split by ':' and ensure there are exactly 8 parts, each part has length between 1 and 4, and contains only valid hexadecimal characters."
    
    answer = """class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4: return "Neither"
            for p in parts:
                if not p or (p[0] == '0' and len(p) > 1) or not p.isdigit() or int(p) > 255:
                    return "Neither"
            return "IPv4"
        elif ':' in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8: return "Neither"
            hex_chars = set("0123456789abcdefABCDEF")
            for p in parts:
                if not p or len(p) > 4 or not all(c in hex_chars for c in p):
                    return "Neither"
            return "IPv6"
        return "Neither"
"""

    boilerplate = {
        "python": "import sys\n\nclass Solution:\n    def validIPAddress(self, queryIP: str) -> str:\n        # User logic here\n        return \"\"\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        queryIP = line.strip('\"').strip(\"'\")\n        sol = Solution()\n        print(sol.validIPAddress(queryIP))",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string validIPAddress(string queryIP) {\n        // User logic here\n        return \"\";\n    }\n};\n\nint main() {\n    string s; if (cin >> s) {\n        if (s[0] == '\"') s = s.substr(1, s.length() - 2);\n        cout << Solution().validIPAddress(s) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public String validIPAddress(String queryIP) {\n        // User logic here\n        return \"\";\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim().replace(\"\\\"\", \"\");\n            System.out.println(new Solution().validIPAddress(s));\n        }\n    }\n}",
        "javascript": "/**\n * @param {string} queryIP\n * @return {string}\n */\nvar validIPAddress = function(queryIP) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const queryIP = input.replace(/^\"|\"$/g, '');\n    console.log(validIPAddress(queryIP));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n\nchar* validIPAddress(char* queryIP) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    char b[1024]; if (scanf(\"%s\", b) != EOF) printf(\"%s\\n\", validIPAddress(b));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "\"172.16.254.1\"", "expected_output": "IPv4", "is_sample": True},
        {"input": "\"2001:0db8:85a3:0:0:8A2E:0370:7334\"", "expected_output": "IPv6", "is_sample": True},
        {"input": "\"256.256.256.256\"", "expected_output": "Neither", "is_sample": True},
        {"input": "\"192.168.01.1\"", "expected_output": "Neither", "is_sample": False},
        {"input": "\"192.168.1.00\"", "expected_output": "Neither", "is_sample": False},
        {"input": "\"2001:0db8:85a3::8A2E:0370:7334\"", "expected_output": "Neither", "is_sample": False},
        {"input": "\"02001:0db8:85a3:0000:0000:8a2e:0370:7334\"", "expected_output": "Neither", "is_sample": False},
        {"input": "\"1.1.1.1.\"", "expected_output": "Neither", "is_sample": False},
        {"input": "\"1:2:3:4:5:6:7:8:9\"", "expected_output": "Neither", "is_sample": False},
        {"input": "\"2001:db8:85a3:0:0:8A2E:0370:7334\"", "expected_output": "IPv6", "is_sample": False}
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
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Validate_IP_Address.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
