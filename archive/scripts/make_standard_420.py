import json
import os

def generate_json():
    problem_id = 420
    title = "Strong Password Checker"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>420. Strong Password Checker</h3>
<p>A password is said to be strong if it satisfies all the following criteria:</p>

<ul>
	<li>It has at least <code>6</code> characters and at most <code>20</code> characters.</li>
	<li>It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.</li>
	<li>It does not contain three repeating characters in a row (e.g., <code>"Baaabb0"</code> is weak, but <code>"Baaba0"</code> is strong).</li>
</ul>

<p>Given a string <code>password</code>, return <em>the minimum number of steps required to make </em><code>password</code><em> strong</em>. If <code>password</code> is already strong, return <code>0</code>.</p>

<p>In one step, you can <strong>insert</strong> one character into the password, <strong>delete</strong> one character from the password, or <strong>replace</strong> one character of the password with another character.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> password = "a"
<strong>Output:</strong> 5
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> password = "aA1"
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> password = "1337C0d3"
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= password.length &lt;= 50</code></li>
	<li><code>password</code> consists of letters, digits, and punctuation; characters from the ASCII range 32-126.</li>
</ul>"""

    input_format = "A string `password`."
    output_format = "An integer representing the minimum steps."
    
    constraints = [
        "1 <= password.length <= 50",
        "ASCII characters 32-126 only."
    ]
    
    explanation = """To determine the minimum steps:
1. **Missing Types**: Check if the password lacks lowercase, uppercase, or digit characters. At most 3 types can be missing.
2. **Length < 6**: Steps = `max(6 - len, missing_types)`.
3. **Length 6-20**: Replace repeating triples to fix repeats. Steps = `max(replaces, missing_types)`.
4. **Length > 20**: Must delete `len - 20` characters. Use greedy logic to prioritize deletions from repeating characters of specific lengths (mod 3) to minimize necessary replacements."""
    
    answer = """class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (1 - has_lower) + (1 - has_upper) + (1 - has_digit)
        
        if n < 6:
            return max(6 - n, missing_types)
        
        replaces = 0
        one_dels, two_dels = 0, 0
        i = 0
        while i < n:
            length = 1
            while i + 1 < n and password[i] == password[i+1]:
                length += 1
                i += 1
            if length >= 3:
                replaces += length // 3
                if length % 3 == 0: one_dels += 1
                elif length % 3 == 1: two_dels += 1
            i += 1
            
        if n <= 20:
            return max(replaces, missing_types)
        
        dels = n - 20
        replaces -= min(dels, one_dels * 1) // 1
        dels_left = max(0, dels - one_dels)
        replaces -= min(dels_left, two_dels * 2) // 2
        dels_left = max(0, dels_left - two_dels * 2)
        replaces -= dels_left // 3
        
        return (n - 20) + max(replaces, missing_types)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # User Logic Here
        pass

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        if raw_input.startswith('"') and raw_input.endswith('"'): 
            raw_input = raw_input[1:-1]
        elif raw_input.startswith("'") and raw_input.endswith("'"):
            raw_input = raw_input[1:-1]
        sol = Solution()
        print(json.dumps(sol.strongPasswordChecker(raw_input)))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int strongPasswordChecker(string password) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string password;
    if (getline(cin, password)) {
        if (!password.empty() && (password.front() == '"' || password.front() == '\\'')) 
            password = password.substr(1, password.size() - 2);
        Solution sol;
        cout << sol.strongPasswordChecker(password) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int strongPasswordChecker(String password) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String password = sc.nextLine().trim();
            if (password.startsWith("\\\"") || password.startsWith("'"))
                password = password.substring(1, password.length() - 1);
            Solution sol = new Solution();
            System.out.println(sol.strongPasswordChecker(password));
        }
    }
}""",
        "javascript": """var strongPasswordChecker = function(password) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let password = input;
    if (password.startsWith('"') || password.startsWith("'"))
        password = password.slice(1, -1);
    console.log(JSON.stringify(strongPasswordChecker(password)));
}""",
        "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int strongPasswordChecker(char* password) {
    // User Logic Here
    return 0;
}

int main() {
    char password[100];
    if (fgets(password, 100, stdin)) {
        password[strcspn(password, "\\n")] = 0;
        char *p = password;
        if (*p == '"' || *p == '\\'') {
            p++;
            password[strlen(password)-1] = 0;
        }
        printf("%d\\n", strongPasswordChecker(p));
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"a"', "expected_output": "5", "is_sample": True},
        {"input": '"aA1"', "expected_output": "3", "is_sample": True},
        {"input": '"1337C0d3"', "expected_output": "0", "is_sample": False},
        {"input": '"aaa123"', "expected_output": "1", "is_sample": False},
        {"input": '"aaaAAA111"', "expected_output": "3", "is_sample": False},
        {"input": '".................."', "expected_output": "6", "is_sample": False},
        {"input": '"ababababababababababab"', "expected_output": "2", "is_sample": False},
        # 3 Stress
        {"input": '"aaaaaAAAAA00000aaaaaAAAAA00000"', "expected_output": "13", "is_sample": False},
        {"input": '"aaa111"', "expected_output": "2", "is_sample": False},
        {"input": '"bbaaaaaaaaaaaaaaacccccc"', "expected_output": "8", "is_sample": False}
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
        "topics": ["Dynamic Programming", "String", "Greedy"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Strong_Password_Checker.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
