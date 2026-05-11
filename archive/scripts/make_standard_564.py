import json
import os

def generate_json():
    problem_id = 564
    title = "Find the Closest Palindrome"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>564. Find the Closest Palindrome</h3>
<p>Given a string <code>n</code> representing an integer, return <em>the closest integer (not including itself), which is a palindrome</em>. If there is a tie, return <em>the smaller one</em>.</p>

<p>The closest is defined as the absolute difference minimized between two integers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = "123"
<strong>Output:</strong> "121"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = "1"
<strong>Output:</strong> "0"
<strong>Explanation:</strong> 0 and 2 are the closest palindromes but we return the smallest which is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= n.length &lt;= 18</code></li>
    <li><code>n</code> consists of only digits.</li>
    <li><code>n</code> does not have leading zeros.</li>
    <li><code>n</code> represents an integer in the range <code>[1, 10<sup>18</sup> - 1]</code>.</li>
</ul>"""

    input_format = "A single line: a JSON string `n`."
    output_format = "A JSON string of the closest palindrome."

    constraints = [
        "1 <= n.length <= 18",
        "n consists of only digits",
        "n does not have leading zeros",
        "n represents an integer in the range [1, 10^18 - 1]"
    ]

    explanation = """The closest palindrome will be formed by mirroring the left half. There are 5 candidates:
1. Mirroring the exact left half.
2. Mirroring the left half + 1.
3. Mirroring the left half - 1.
4. Edge case: 10^(L-1) - 1 (e.g. 999).
5. Edge case: 10^L + 1 (e.g. 1001).
Compare absolute differences and return the minimum, breaking ties with the smaller value."""

    answer = """class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        candidates.add(str(10**(length - 1) - 1))
        candidates.add(str(10**length + 1))
        
        prefix = int(n[:(length + 1) // 2])
        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                cand = p + p[::-1]
            else:
                cand = p + p[:-1][::-1]
            candidates.add(cand)
            
        candidates.discard(n)
        
        def diff(x):
            return abs(int(x) - int(n))
        
        return min(candidates, key=lambda x: (diff(x), int(x)))"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n_str = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.nearestPalindromic(n_str)))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string nearestPalindromic(string n) {
        // User logic here
        return "";
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        cout << "\\"" << sol.nearestPalindromic(input) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String nearestPalindromic(String n) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() >= 2 && raw.startsWith("\\""))
                raw = raw.substring(1, raw.length() - 1);
            Solution sol = new Solution();
            System.out.println("\\"" + sol.nearestPalindromic(raw) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string} n
 * @return {string}
 */
var nearestPalindromic = function(n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const n = JSON.parse(input);
    console.log(JSON.stringify(nearestPalindromic(n)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* nearestPalindromic(char* n) {
    // User logic here
    char* res = (char*)malloc(50);
    strcpy(res, n);
    return res;
}

int main() {
    char input[100];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char n[100];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(n, input + 1, len - 2);
            n[len - 2] = '\\0';
        } else {
            strcpy(n, input);
        }
        char* res = nearestPalindromic(n);
        printf("\\"%s\\"\\n", res);
        free(res);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"123"', "expected_output": '"121"', "is_sample": True},
        {"input": '"1"', "expected_output": '"0"', "is_sample": True},
        {"input": '"10"', "expected_output": '"9"', "is_sample": False},
        {"input": '"100"', "expected_output": '"99"', "is_sample": False},
        {"input": '"99"', "expected_output": '"101"', "is_sample": False},
        {"input": '"1283"', "expected_output": '"1331"', "is_sample": False},
        {"input": '"1000"', "expected_output": '"999"', "is_sample": False},
        {"input": '"806"', "expected_output": '"808"', "is_sample": False},
        {"input": '"999999999999999999"', "expected_output": '"1000000000000000001"', "is_sample": False},
        {"input": '"123456789012345678"', "expected_output": '"12345678987654321"', "is_sample": False}
    ]

    data = {
        "question_id": problem_id,
        "question_text": html_description,
        "difficulty": difficulty,
        "marks": 10,
        "input_format": input_format,
        "output_format": output_format,
        "constraints": constraints,
        "explanation": explanation,
        "answer": answer,
        "boilerplate": boilerplate,
        "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "String"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
