import json
import os

def generate_json():
    problem_id = 394
    title = "Decode String"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>394. Decode String</h3>
<p>Given an encoded string, return its decoded string.</p>

<p>The encoding rule is: <code>k[encoded_string]</code>, where the <code>encoded_string</code> inside the square brackets is being repeated exactly <code>k</code> times. Note that <code>k</code> is guaranteed to be a positive integer.</p>

<p>You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, <code>k</code>. For example, there will not be input like <code>3a</code> or <code>2[4]</code>.</p>

<p>The test cases are generated so that the length of the output will never exceed <code>10<sup>5</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "3[a]2[bc]"
<strong>Output:</strong> "aaabcbc"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "3[a2[c]]"
<strong>Output:</strong> "accaccacc"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "2[abc]3[cd]ef"
<strong>Output:</strong> "abcabccdcdcdef"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 30</code></li>
	<li><code>s</code> consists of lowercase English letters, digits, and square brackets <code>'[]'</code>.</li>
	<li><code>s</code> is guaranteed to be <strong>a valid</strong> input.</li>
	<li>All the integers in <code>s</code> are in the range <code>[1, 300]</code>.</li>
</ul>"""

    input_format = "An encoded string `s`."
    output_format = "A decoded string."
    
    constraints = [
        "1 <= s.length <= 30",
        "Integers k are between [1, 300].",
        "Output length <= 10^5."
    ]
    
    explanation = """To decode the string, we need to handle nested structures, which makes a **Stack** or **Recursion** ideal.

### Stack Approach:
We can maintain a stack to store the current multiplier `k` and the string formed *before* the current bracket.

### Algorithm Steps:
1. **Initialize**: `stack = []`, `curr_num = 0`, `curr_str = ""`.
2. **Iterate through $s$**:
   - If **Digit**: Update `curr_num = curr_num * 10 + int(digit)`.
   - If **'['**: 
     - Push the current string and the current number into the stack: `stack.append((curr_str, curr_num))`.
     - Reset `curr_str = ""`, `curr_num = 0`.
   - If **']'**:
     - Pop from stack: `last_str, num = stack.pop()`.
     - Update: `curr_str = last_str + num * curr_str`.
   - If **Letter**: Append to `curr_str`: `curr_str += letter`.
3. **Result**: Return `curr_str`.

### Complexity Analysis:
- **Time Complexity**: $O(L)$, where $L$ is the length of the decoded string. We build the string once.
- **Space Complexity**: $O(D)$, where $D$ is the maximum depth of nesting, used for the stack."""
    
    answer = """class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += char
        return curr_str"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def decodeString(self, s: str) -> str:
        # User Logic Here
        pass

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    if s:
        if s.startswith('"') and s.endswith('"'): s = s[1:-1]
        sol = Solution()
        print(json.dumps(sol.decodeString(s)))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
        // User Logic Here
        return "";
    }
};

int main() {
    string s;
    if (getline(cin, s)) {
        if (s.size() >= 2 && s.front() == '"' && s.back() == '"') s = s.substr(1, s.size() - 2);
        Solution sol;
        cout << sol.decodeString(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String decodeString(String s) {
        // User Logic Here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine().trim();
            if (s.startsWith("\\\"") && s.endsWith("\\\"")) s = s.substring(1, s.length() - 1);
            Solution sol = new Solution();
            System.out.println(sol.decodeString(s));
        }
    }
}""",
        "javascript": """var decodeString = function(s) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let s = input;
    if (s.startsWith('"') && s.endsWith('"')) s = s.slice(1, -1);
    console.log(JSON.stringify(decodeString(s)));
}""",
        "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char* decodeString(char* s) {
    // User Logic Here
    return "";
}

int main() {
    char s[10005];
    if (fgets(s, 10005, stdin)) {
        s[strcspn(s, "\\n")] = 0;
        char *ptr = s;
        if (s[0] == '"') { ptr++; s[strlen(s)-1] = 0; }
        printf("%s\\n", decodeString(ptr));
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "3[a]2[bc]", "expected_output": '"aaabcbc"', "is_sample": True},
        {"input": "3[a2[c]]", "expected_output": '"accaccacc"', "is_sample": True},
        # 5 Diverse
        {"input": "2[abc]3[cd]ef", "expected_output": '"abcabccdcdcdef"', "is_sample": False},
        {"input": "abc3[cd]xyz", "expected_output": '"abccdcdcdxyz"', "is_sample": False},
        {"input": "10[a]", "expected_output": '"aaaaaaaaaa"', "is_sample": False},
        {"input": "2[2[b]]", "expected_output": '"bbbb"', "is_sample": False},
        {"input": "z1[y]x", "expected_output": '"zyx"', "is_sample": False},
        # 3 Stress
        {"input": "100[a]", "expected_output": '"' + "a" * 100 + '"', "is_sample": False},
        {"input": "2[3[4[b]]]", "expected_output": '"' + "b" * 24 + '"', "is_sample": False},
        {"input": "1[2[3[4[5[a]]]]]", "expected_output": '"' + "a" * 120 + '"', "is_sample": False}
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
        "topics": ["String", "Stack", "Recursion"],
        "companyIndex": 1
    }

    output_path = "301-500/394_Decode_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
