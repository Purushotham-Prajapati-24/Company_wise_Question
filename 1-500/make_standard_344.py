import json
import os

def generate_json():
    problem_id = 344
    title = "Reverse String"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>344. Reverse String</h3>
<p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>

<p>You must do this by modifying the input array <strong>in-place</strong> with <code>O(1)</code> extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.</li>
</ul>"""

    input_format = "A JSON array of characters `s`."
    output_format = "A JSON array of characters representing the reversed array."
    
    constraints = [
        "1 <= s.length <= 10^5",
        "Must be in-place (O(1) extra space).",
        "O(N) time complexity."
    ]
    
    explanation = """To reverse a string in-place with constant memory:
1. **Two Pointers**:
   - Initialize two pointers `left = 0` and `right = len(s) - 1`.
   - While `left < right`:
     - Swap `s[left]` and `s[right]`.
     - Increment `left`.
     - Decrement `right`.
2. **Complexity**:
   - Time Complexity: O(N) where N is the length of the string, because we perform N/2 swaps.
   - Space Complexity: O(1) as we occupy no extra space for the reversal."""
    
    answer = """def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass Solution:\n    def reverseString(self, s: list[str]) -> None:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    # Lethal parsing: Extract all quoted characters\n    s = re.findall(r'\"([^\"]*)\"', input_data)\n    \n    sol = Solution()\n    sol.reverseString(s)\n    print(json.dumps(s).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    void reverseString(vector<char>& s) {\n        // User logic here\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n\n    regex char_re(R\"(\"([^\"]*)\")\");\n    auto chars_begin = sregex_iterator(input.begin(), input.end(), char_re);\n    auto chars_end = sregex_iterator();\n\n    vector<char> s;\n    for (sregex_iterator i = chars_begin; i != chars_end; ++i) {\n        string match = (*i)[1].str();\n        s.push_back(match.empty() ? ' ' : match[0]);\n    }\n\n    Solution sol;\n    sol.reverseString(s);\n\n    cout << \"[\";\n    for (int i = 0; i < s.size(); i++) {\n        cout << \"\\\"\" << s[i] << \"\\\"\" << (i < s.size() - 1 ? \",\" : \"\");\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public void reverseString(char[] s) {\n        // User logic here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n\n        List<Character> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"\\\"([^\\\"]*)\\\"\").matcher(input);\n        while (m.find()) {\n            String match = m.group(1);\n            list.add(match.isEmpty() ? ' ' : match.charAt(0));\n        }\n\n        char[] s = new char[list.size()];\n        for (int i = 0; i < list.size(); i++) s[i] = list.get(i);\n\n        new Solution().reverseString(s);\n\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < s.length; i++) {\n            sb.append(\"\\\"\").append(s[i]).append(\"\\\"\");\n            if (i < s.length - 1) sb.append(\",\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\n/**\n * @param {character[]} s\n * @return {void} Do not return anything, modify s in-place instead.\n */\nvar reverseString = function(s) {\n    // User logic here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const matches = input.match(/\"([^\"]*)\"/g) || [];\n    const s = matches.map(m => m.slice(1, -1)[0] || ' ');\n\n    reverseString(s);\n    console.log(JSON.stringify(s).replace(/ /g, ''));\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nvoid reverseString(char* s, int sSize) {\n    // User logic here\n}\n\nint main() {\n    static char buffer[1000000];\n    int len = fread(buffer, 1, 999999, stdin); buffer[len] = '\\0';\n\n    char *s = malloc(len);\n    int sSize = 0;\n    char *ptr = buffer;\n    while ((ptr = strchr(ptr, '\"')) != NULL) {\n        ptr++;\n        char *end = strchr(ptr, '\"');\n        if (end) {\n            s[sSize++] = (end > ptr) ? *ptr : ' ';\n            ptr = end + 1;\n        } else break;\n    }\n\n    reverseString(s, sSize);\n    printf(\"[\");\n    for (int i = 0; i < sSize; i++) {\n        printf(\"\\\"%c\\\"%s\", s[i], i < sSize - 1 ? \",\" : \"\");\n    }\n    printf(\"]\\n\");\n    free(s);\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["h","e","l","l","o"]', "expected_output": '["o","l","l","e","h"]', "is_sample": True},
        {"input": '["H","a","n","n","a","h"]', "expected_output": '["h","a","n","n","a","H"]', "is_sample": True},
        {"input": '["a"]', "expected_output": '["a"]', "is_sample": False},
        {"input": '["a","b"]', "expected_output": '["b","a"]', "is_sample": False},
        {"input": '["1","2","3"]', "expected_output": '["3","2","1"]', "is_sample": False},
        {"input": '["x","y","z","w"]', "expected_output": '["w","z","y","x"]', "is_sample": False},
        {"input": '[" "," "]', "expected_output": '[" "," "]', "is_sample": False},
        # Stress cases
        {"input": json.dumps(["a"]*50000), "expected_output": json.dumps(["a"]*50000).replace(' ', ''), "is_sample": False},
        {"input": json.dumps([chr(ord('a') + i%26) for i in range(50000)]), "expected_output": json.dumps([chr(ord('a') + i%26) for i in range(50000)][::-1]).replace(' ', ''), "is_sample": False},
        {"input": json.dumps([chr(ord('A') + i%26) for i in range(100000)]), "expected_output": json.dumps([chr(ord('A') + i%26) for i in range(100000)][::-1]).replace(' ', ''), "is_sample": False}
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
        "topics": ["Two Pointers", "String", "Recursion"],
        "companyIndex": 0
    }

    output_path = "301-500/344_Reverse_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
