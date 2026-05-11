import json
import os

def generate_json():
    problem_id = 186
    title = "Reverse Words in a String II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>186. Reverse Words in a String II</h3>
<p>Given a <strong>character array </strong><code>s</code>, reverse the order of the <strong>words</strong> in the array.</p>

<p>A <strong>word</strong> is defined as a sequence of non-space characters. The words in <code>s</code> are separated by a <strong>single space</strong>.</p>

<p>You must solve the problem <strong>in-place</strong>, meaning you cannot allocate extra space for another array or data structure.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
<strong>Output:</strong> ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["a"]
<strong>Output:</strong> ["a"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is an English letter (uppercase or lowercase), digit, or space <code>' '</code>.</li>
	<li>There is <strong>at least one word</strong> in <code>s</code>.</li>
	<li><code>s</code> does not contain leading or trailing spaces.</li>
	<li>All the words in <code>s</code> are guaranteed to be separated by a single space.</li>
</ul>"""

    input_format = "A single line containing the string (representing the character array)."
    output_format = "The modified string with reversed words."
    
    constraints = [
        "1 <= s.length <= 10^5",
        "O(1) extra space.",
        "In-place modification required."
    ]
    
    explanation = """To reverse the words in a character array in-place:
1. **Reverse the Entire Array**:
   - First, reverse the entire character array. This puts the words in the correct order but each word is reversed individually.
2. **Reverse Each Individual Word**:
   - Iterate through the array and find the boundaries of each word (delimited by spaces).
   - Reverse each word's characters to restore their original order within the now-correctly-ordered sentence.
3. **Complexity**:
   - Time Complexity: O(N) because each character is reversed twice.
   - Space Complexity: O(1) as we modify the array in-place."""
    
    answer = """def reverseWords(s: list[str]) -> None:
    def reverse(l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
    # Step 1: Reverse the whole array
    reverse(0, len(s) - 1)
    
    # Step 2: Reverse each word
    n = len(s)
    start = 0
    for end in range(n + 1):
        if end == n or s[end] == ' ':
            reverse(start, end - 1)
            start = end + 1"""

    boilerplate = {
        "python": "import sys\n\ndef reverseWords(s):\n    # User logic here (s is a list of characters)\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().rstrip('\\n')\n    if data:\n        s_list = list(data)\n        reverseWords(s_list)\n        print(\"\".join(s_list))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nvoid reverseWords(vector<char>& s) {\n    // User logic\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<char> s(line.begin(), line.end());\n        reverseWords(s);\n        for (char c : s) cout << c;\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public void reverseWords(char[] s) {\n        // User logic\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line != null) {\n            char[] s = line.toCharArray();\n            Solution sol = new Solution();\n            sol.reverseWords(s);\n            System.out.println(new String(s));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction reverseWords(s) {\n    // User logic (s is an array of characters)\n}\n\nconst input = fs.readFileSync(0, 'utf-8').replace(/\\r?\\n$/, '');\nif (input.length > 0) {\n    let s = input.split('');\n    reverseWords(s);\n    console.log(s.join(''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nvoid reverseWords(char* s, int sSize) {\n    // User logic\n}\n\nint main() {\n    char* s = NULL;\n    size_t len = 0;\n    int read;\n    // Note: getline is POSIX, but for simple stdin we can read with a loop or a large buffer\n    char buffer[200000];\n    if (fgets(buffer, sizeof(buffer), stdin)) {\n        int sSize = strlen(buffer);\n        if (sSize > 0 && buffer[sSize-1] == '\\n') {\n            buffer[sSize-1] = '\\0';\n            sSize--;\n        }\n        if (sSize > 0 && buffer[sSize-1] == '\\r') {\n            buffer[sSize-1] = '\\0';\n            sSize--;\n        }\n        reverseWords(buffer, sSize);\n        printf(\"%s\\n\", buffer);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "the sky is blue", "expected_output": "blue is sky the", "is_sample": True},
        {"input": "a", "expected_output": "a", "is_sample": True},
        {"input": "hello world", "expected_output": "world hello", "is_sample": False},
        {"input": "123 456", "expected_output": "456 123", "is_sample": False},
        {"input": "A B C D", "expected_output": "D C B A", "is_sample": False},
        {"input": "word", "expected_output": "word", "is_sample": False},
        {"input": "much better now", "expected_output": "now better much", "is_sample": False},
        # Stress cases
        {"input": "a"*50000 + " " + "b"*50000, "expected_output": "b"*50000 + " " + "a"*50000, "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": " ".join([str(i) for i in range(99, -1, -1)]), "is_sample": False},
        {"input": "one two three", "expected_output": "three two one", "is_sample": False}
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

    output_path = "1-200/186_Reverse_Words_in_a_String_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
