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
        "python": "import sys\n\nclass Codec:\n    def encode(self, strs: list[str]) -> str:\n        # User logic here\n        pass\n    def decode(self, s: str) -> list[str]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    codec = Codec()\n    strs = sys.stdin.read().strip().split('\\n')\n    encoded = codec.encode(strs)\n    decoded = codec.decode(encoded)\n    print(' '.join(decoded))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\nusing namespace std;\n\nclass Codec {\npublic:\n    string encode(vector<string>& strs) {\n        // User logic\n        return \"\";\n    }\n    vector<string> decode(string s) {\n        // User logic\n        return {};\n    }\n};\n\nint main() {\n    vector<string> strs;\n    string line;\n    while (getline(cin, line)) {\n        if (!line.empty()) strs.push_back(line);\n    }\n    Codec codec;\n    auto decoded = codec.decode(codec.encode(strs));\n    for (auto& s : decoded) cout << s << ' ';\n    cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String encode(List<String> strs) {\n        // User logic\n        return \"\";\n    }\n    public List<String> decode(String s) {\n        // User logic\n        return new ArrayList<>();\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<String> strs = new ArrayList<>();\n        while (sc.hasNextLine()) {\n            String l = sc.nextLine();\n            if (!l.isEmpty()) strs.add(l);\n        }\n        Solution sol = new Solution();\n        List<String> decoded = sol.decode(sol.encode(strs));\n        System.out.println(String.join(\" \", decoded));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction encode(strs) {\n    // User logic\n    return \"\";\n}\nfunction decode(s) {\n    // User logic\n    return [];\n}\n\nconst strs = fs.readFileSync(0, 'utf-8').trim().split('\\n').filter(Boolean);\nconst decoded = decode(encode(strs));\nconsole.log(decoded.join(' '));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* encode(char** strs, int size) {\n    // User logic\n    return \"\";\n}\nchar** decode(char* s, int* returnSize) {\n    // User logic\n    return NULL;\n}\n\nint main() {\n    char** strs = malloc(1000 * sizeof(char*));\n    int size = 0;\n    char line[1005];\n    while (fgets(line, sizeof(line), stdin)) {\n        line[strcspn(line, \"\\n\")] = 0;\n        if (strlen(line)) strs[size++] = strdup(line);\n    }\n    char* enc = encode(strs, size);\n    int retSize;\n    char** dec = decode(enc, &retSize);\n    for (int i = 0; i < retSize; i++) printf(\"%s \", dec[i]);\n    printf(\"\\n\");\n    return 0;\n}"
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
