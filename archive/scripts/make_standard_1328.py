import json
import os

def generate_json():
    problem_id = 1328
    title = "Break a Palindrome"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1328. Break a Palindrome</h3>
<p>Given a palindromic string of lowercase English letters <code>palindrome</code>, replace <strong>exactly one</strong> character with any lowercase English letter so that the resulting string is <strong>not</strong> a palindrome and that it is the <strong>lexicographically smallest</strong> one possible.</p>

<p>After replacing the character, if there are multiple ways to make the resulting string not a palindrome, return the <strong>lexicographically smallest</strong> one.</p>

<p>If there is no way to replace a character to make it not a palindrome, return an <strong>empty string</strong>.</p>

<p>A string <code>a</code> is lexicographically smaller than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, <code>a</code> has a character strictly smaller than the corresponding character in <code>b</code>. For example, <code>"abcd"</code> is lexicographically smaller than <code>"acbd"</code> because the first difference is at the second position; <code>'b'</code> is smaller than <code>'c'</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> palindrome = "abccba"
<strong>Output:</strong> "aaccba"
<strong>Explanation:</strong> There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> palindrome = "a"
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= palindrome.length &lt;= 1000</code></li>
	<li><code>palindrome</code> consists of only lowercase English letters and is a palindrome.</li>
</ul>"""

    input_format = "A string `palindrome` enclosed in quotes as a JSON string."
    output_format = "A string representing the result."

    constraints = [
        "1 <= palindrome.length <= 1000",
        "palindrome is a palindrome and consists of lowercase English letters"
    ]

    explanation = """To break a palindrome into the lexicographically smallest non-palindrome:
1. If the length of the string is 1, return an empty string (no way to break it).
2. Iterate through the first half of the string (`n // 2`).
3. If you find any character that is not 'a', change it to 'a' and return the string.
4. If all characters in the first half are 'a', then the only way to make it smallest is to change the very last character of the entire string to 'b'.
5. Return the modified string."""

    answer = """class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        n = len(palindrome)
        res = list(palindrome)
        for i in range(n // 2):
            if res[i] != 'a':
                res[i] = 'a'
                return "".join(res)
        
        res[n - 1] = 'b'
        return "".join(res)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s = json.loads(raw)
        sol = Solution()
        print(sol.breakPalindrome(s))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string breakPalindrome(string palindrome) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        string s = json::parse(line);
        Solution sol;
        cout << sol.breakPalindrome(s) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String breakPalindrome(String palindrome) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String s = mapper.readValue(sc.nextLine(), String.class);
            System.out.println(new Solution().breakPalindrome(s));
        }
    }
}""",
        "javascript": """var breakPalindrome = function(palindrome) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(breakPalindrome(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * breakPalindrome(char * palindrome){
    // User logic here
    return "";
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    def solve(palindrome):
        if len(palindrome) == 1: return ""
        n = len(palindrome)
        res = list(palindrome)
        for i in range(n // 2):
            if res[i] != 'a':
                res[i] = 'a'
                return "".join(res)
        res[n - 1] = 'b'
        return "".join(res)

    test_cases_data = [
        "abccba",       # Sample 1
        "a",            # Sample 2
        "aa",           # Change to ab
        "aba",          # Change to abb (not aaa because aaa is palindrome)
        "aaaa",         # Change to aaab
        "abdbba",       # Change to aadbba
        "bccb",         # Change to accb
        # Stress tests
        "z" * 10,
        "a" * 10,
        "a" * 9 + "b" + "a" * 9
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = solve(t)
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Greedy"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
