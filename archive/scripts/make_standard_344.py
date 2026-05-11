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
        "python": "import sys\nimport json\n\nclass Solution:\n    def reverseString(self, s: list[str]) -> None:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        s = json.loads(raw_input)\n        sol = Solution()\n        sol.reverseString(s)\n        print(json.dumps(s).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    void reverseString(vector<char>& s) {\n        // Your logic here\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<char> s;\n        for (char c : line) {\n            if (c != '[' && c != ']' && c != ',' && c != '\"') {\n                s.push_back(c);\n            }\n        }\n        Solution sol;\n        sol.reverseString(s);\n        cout << \"[\";\n        for (int i = 0; i < s.size(); ++i) {\n            cout << \"\\\"\" << s[i] << \"\\\"\" << (i < s.size() - 1 ? \",\" : \"\");\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public void reverseString(char[] s) {\n        // Your logic here\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine();\n            List<Character> list = new ArrayList<>();\n            for (char c : line.toCharArray()) {\n                if (c != '[' && c != ']' && c != ',' && c != '\"') {\n                    list.add(c);\n                }\n            }\n            char[] s = new char[list.size()];\n            for (int i = 0; i < list.size(); i++) s[i] = list.get(i);\n            Solution sol = new Solution();\n            sol.reverseString(s);\n            System.out.print(\"[\");\n            for (int i = 0; i < s.length; i++) {\n                System.out.print(\"\\\"\" + s[i] + \"\\\"\" + (i < s.length - 1 ? \",\" : \"\"));\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "/**\n * @param {character[]} s\n * @return {void} Do not return anything, modify s in-place instead.\n */\nvar reverseString = function(s) {\n    // User logic\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const s = JSON.parse(input);\n    reverseString(s);\n    console.log(JSON.stringify(s).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nvoid reverseString(char* s, int sSize) {\n    // Your logic here\n}\n\nint main() {\n    char line[200000];\n    if (fgets(line, sizeof(line), stdin)) {\n        char* s = malloc(100005);\n        int size = 0;\n        for (int i = 0; line[i]; i++) {\n            if (line[i] != '[' && line[i] != ']' && line[i] != ',' && line[i] != '\"' && line[i] != '\\n' && line[i] != '\\r') {\n                s[size++] = line[i];\n            }\n        }\n        reverseString(s, size);\n        printf(\"[\");\n        for (int i = 0; i < size; i++) {\n            printf(\"\\\"%c\\\"%s\", s[i], i < size - 1 ? \",\" : \"\");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
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
