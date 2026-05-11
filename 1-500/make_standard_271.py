import json
import os

def generate_json():
    problem_id = 271
    title = "Encode and Decode Strings"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>271. Encode and Decode Strings</h3>
<p>Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.</p>

<p>Machine 1 (sender) has the function:</p>
<pre>string encode(vector&lt;string&gt; strs) {
  // ... your code
  return encoded_string;
}</pre>

<p>Machine 2 (receiver) has the function:</p>
<pre>vector&lt;string&gt; decode(string s) {
  //... your code
  return strs;
}</pre>

<p>So Machine 1 does:</p>
<pre>string encoded_string = encode(strs);</pre>

<p>and Machine 2 does:</p>
<pre>vector&lt;string&gt; strs2 = decode(encoded_string);</pre>

<p><code>strs2</code> should be the same as <code>strs</code>. Implement the <code>encode</code> and <code>decode</code> methods.</p>

<p>You are not allowed to use any built-in serialization methods such as <code>eval</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> dummy_input = ["Hello","World"]
<strong>Output:</strong> ["Hello","World"]
<strong>Explanation:</strong>
One possible encoding: "5#Hello5#World"</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> dummy_input = [""]
<strong>Output:</strong> [""]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> contains any possible characters out of 256 valid ASCII characters.</li>
</ul>"""

    input_format = "A list of strings space-separated (for the sake of the standardized input format, we will assume elements are separated by space, but the problem itself handles arbitrary chars)."
    output_format = "The reconstructed list of strings."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """class Codec:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass Codec:\n    def encode(self, strs: list[str]) -> str:\n        # User logic here\n        pass\n    def decode(self, s: str) -> list[str]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Lethal parsing: find [\"a\", \"b\"] or similar\n    match = re.search(r'\\[(.*?)\\]', raw_input, re.DOTALL)\n    if match:\n        strs = re.findall(r'\"([^\"]*)\"', match.group(1))\n    else:\n        strs = raw_input.strip().split('\\n')\n        if not any('\\n' in line for line in strs):\n            strs = raw_input.strip().split()\n    \n    codec = Codec()\n    encoded = codec.encode(strs)\n    decoded = codec.decode(encoded)\n    # JSON dump for consistency\n    print(json.dumps(decoded).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Codec {\npublic:\n    string encode(vector<string>& strs) {\n        // User logic here\n        return \"\";\n    }\n    vector<string> decode(string s) {\n        // User logic here\n        return {};\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    vector<string> strs;\n    regex re_str(R\"(\"([^\"]*)\")\");\n    smatch match;\n    string::const_iterator searchStart(input.cbegin());\n    while (regex_search(searchStart, input.cend(), match, re_str)) {\n        strs.push_back(match[1]);\n        searchStart = match.suffix().first;\n    }\n    \n    if (strs.empty() && !input.empty()) {\n        // Fallback split\n        string word;\n        for (char c : input) {\n            if (isspace(c)) {\n                if (!word.empty()) strs.push_back(word);\n                word = \"\";\n            } else word += c;\n        }\n        if (!word.empty()) strs.push_back(word);\n    }\n\n    Codec codec;\n    auto decoded = codec.decode(codec.encode(strs));\n    cout << \"[\";\n    for (size_t i = 0; i < decoded.size(); i++) {\n        cout << \"\\\"\" << decoded[i] << \"\\\"\" << (i == decoded.size() - 1 ? \"\" : \",\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public String encode(List<String> strs) {\n        // User logic here\n        return \"\";\n    }\n    public List<String> decode(String s) {\n        // User logic here\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (sc.hasNext()) {\n            String input = sc.next();\n            List<String> strs = new ArrayList<>();\n            Matcher m = Pattern.compile(\"\\\"([^\\\"]*)\\\"\").matcher(input);\n            while (m.find()) {\n                strs.add(m.group(1));\n            }\n            if (strs.isEmpty()) {\n                String[] parts = input.trim().split(\"\\\\s+\");\n                for (String p : parts) if (!p.isEmpty()) strs.add(p);\n            }\n            Solution sol = new Solution();\n            List<String> decoded = sol.decode(sol.encode(strs));\n            StringBuilder sb = new StringBuilder(\"[\");\n            for (int i = 0; i < decoded.size(); i++) {\n                sb.append(\"\\\"\").append(decoded.get(i)).append(\"\\\"\").append(i == decoded.size() - 1 ? \"\" : \",\");\n            }\n            sb.append(\"]\");\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction encode(strs) {\n    // User logic here\n    return \"\";\n}\nfunction decode(s) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nlet strs = (input.match(/\"([^\"]*)\"/g) || []).map(s => s.replace(/\"/g, ''));\nif (strs.length === 0) {\n    strs = input.trim().split(/\\s+/).filter(Boolean);\n}\nconst decoded = decode(encode(strs));\nconsole.log(JSON.stringify(decoded));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* encode(char** strs, int size) {\n    // User logic here\n    return \"\";\n}\nchar** decode(char* s, int* returnSize) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    static char buffer[1000000];\n    char** strs = malloc(1000 * sizeof(char*));\n    int size = 0;\n    if (fread(buffer, 1, 999999, stdin) > 0) {\n        char *p = buffer;\n        while (*p) {\n            if (*p == '\"') {\n                char *start = p + 1;\n                char *end = strchr(start, '\"');\n                if (end) {\n                    int len = end - start;\n                    strs[size] = malloc(len + 1);\n                    strncpy(strs[size], start, len);\n                    strs[size][len] = '\\0';\n                    size++;\n                    p = end + 1;\n                    continue;\n                }\n            }\n            p++;\n        }\n        if (size == 0) {\n            char *token = strtok(buffer, \" \\t\\n\\r\");\n            while (token) {\n                strs[size++] = strdup(token);\n                token = strtok(NULL, \" \\t\\n\\r\");\n            }\n        }\n    }\n\n    char* enc = encode(strs, size);\n    int retSize;\n    char** dec = decode(enc, &retSize);\n    printf(\"[\");\n    for (int i = 0; i < retSize; i++) {\n        printf(\"\\\"%s\\\"%s\", dec[i], i == retSize - 1 ? \"\" : \",\");\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [{"input": "Hello World", "expected_output": "Hello World", "is_sample": True},
        {"input": "", "expected_output": "", "is_sample": True},
        {"input": "a b c d", "expected_output": "a b c d", "is_sample": False},
        {"input": "leet code is fun", "expected_output": "leet code is fun", "is_sample": False},
        {"input": "123#456 789", "expected_output": "123#456 789", "is_sample": False}, # Hash in string
        {"input": "VeryLongStringThatIsExactly200CharactersLong" * 4, "expected_output": "VeryLongStringThatIsExactly200CharactersLong" * 4, "is_sample": False},
        {"input": "!@#$% ^&*()", "expected_output": "!@#$% ^&*()", "is_sample": False},
        {"input": "a", "expected_output": "a", "is_sample": False},
        {"input": " ", "expected_output": " ", "is_sample": False},
        {"input": "abc def ghi", "expected_output": "abc def ghi", "is_sample": False},]

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
        "topics": ["Array", "String", "Design"],
        "companyIndex": 0
    }

    output_path = f"CompanyQuestion/STANDARD/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
