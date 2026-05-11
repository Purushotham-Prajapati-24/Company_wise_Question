import json
import os

def generate_json():
    problem_id = 387
    title = "First Unique Character in a String"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>387. First Unique Character in a String</h3>
<p>Given a string <code>s</code>, <em>find the first non-repeating character in it and return its index</em>. If it does not exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "loveleetcode"
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "aabb"
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>"""

    input_format = "A string `s`."
    output_format = "An integer index."
    
    constraints = [
        "1 <= s.length <= 100,000",
        "s consists of only lowercase English letters."
    ]
    
    explanation = """To find the first unique character efficiently, we can use two linear passes.

### Algorithm Steps:
1. **First Pass ($O(N)$)**:
   - Count the frequency of each character in the string using a hash map or an array of size 26 (since the alphabet is lowercase English).
2. **Second Pass ($O(N)$)**:
   - Iterate through the string again.
   - For each character at index `i`, check its frequency in the map.
   - If the frequency is 1, return `i`.
3. **Handle No Unique**:
   - If the second loop finishes without finding a unique character, return -1.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, as we visit each character twice.
- **Space Complexity**: $O(1)$ extra space, as the hash map/array only stores up to 26 lowercase English characters."""
    
    answer = """class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def firstUniqChar(self, s: str) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    s = sys.stdin.read().strip()\n    if s:\n        if s.startswith('\"') and s.endswith('\"'):\n            s = s[1:-1]\n        sol = Solution()\n        print(json.dumps(sol.firstUniqChar(s)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int firstUniqChar(string s) {\n        // User logic here\n        return -1;\n    }\n};\n\nint main() {\n    string s;\n    if (getline(cin, s)) {\n        if (s.size() >= 2 && s.front() == '\"' && s.back() == '\"') {\n            s = s.substr(1, s.size() - 2);\n        }\n        Solution sol;\n        cout << sol.firstUniqChar(s) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int firstUniqChar(String s) {\n        // User logic here\n        return -1;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) {\n                s = s.substring(1, s.length() - 1);\n            }\n            Solution sol = new Solution();\n            System.out.println(sol.firstUniqChar(s));\n        }\n    }\n}",
        "javascript": "var firstUniqChar = function(s) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    let s = input;\n    if (s.startsWith('\"') && s.endsWith('\"')) s = s.slice(1, -1);\n    console.log(JSON.stringify(firstUniqChar(s)));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n\nint firstUniqChar(char* s) {\n    // User logic here\n    return -1;\n}\n\nint main() {\n    char s[100005];\n    if (fgets(s, 100005, stdin)) {\n        s[strcspn(s, \"\\n\")] = 0;\n        char *ptr = s;\n        if (*ptr == '\"') {\n            ptr++;\n            s[strlen(s)-1] = 0;\n        }\n        printf(\"%d\\n\", firstUniqChar(ptr));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "leetcode", "expected_output": "0", "is_sample": True},
        {"input": "loveleetcode", "expected_output": "2", "is_sample": True},
        # 5 Diverse
        {"input": "aabb", "expected_output": "-1", "is_sample": False},
        {"input": "a", "expected_output": "0", "is_sample": False},
        {"input": "zz", "expected_output": "-1", "is_sample": False},
        {"input": "ab", "expected_output": "0", "is_sample": False},
        {"input": "abcdeabcde", "expected_output": "-1", "is_sample": False},
        # 3 Stress
        {"input": "a" * 100000 + "b", "expected_output": "100000", "is_sample": False},
        {"input": "abcdefghijklmnopqrstuvwxyz" * 3846 + "a", "expected_output": "-1", "is_sample": False},
        {"input": "abcde" + "f" * 99995, "expected_output": "0", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Queue", "Counting"],
        "companyIndex": 1
    }

    output_path = "301-500/387_First_Unique_Character_in_a_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
