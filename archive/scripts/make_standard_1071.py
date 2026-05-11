import json
import os
import math

def generate_json():
    problem_id = 1071
    title = "Greatest Common Divisor of Strings"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1071. Greatest Common Divisor of Strings</h3>
<p>For two strings <code>s</code> and <code>t</code>, we say "<code>t</code> divides <code>s</code>" if and only if <code>s = t + t + t + ... + t</code> (i.e., <code>t</code> is concatenated with itself one or more times).</p>

<p>Given two strings <code>str1</code> and <code>str2</code>, return <em>the largest string </em><code>x</code><em> such that </em><code>x</code><em> divides both </em><code>str1</code><em> and </em><code>str2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> str1 = "ABCABC", str2 = "ABC"
<strong>Output:</strong> "ABC"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> str1 = "ABABAB", str2 = "ABAB"
<strong>Output:</strong> "AB"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> str1 = "LEET", str2 = "CODE"
<strong>Output:</strong> ""
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= str1.length, str2.length &lt;= 1000</code></li>
	<li><code>str1</code> and <code>str2</code> consist of English uppercase letters.</li>
</ul>
"""

    input_format = "Two strings `str1` and `str2` provided as `[str1, str2]` in JSON."
    output_format = "A string representing the greatest common divisor string."

    constraints = [
        "1 <= str1.length, str2.length <= 1000",
        "Uppercase English letters only"
    ]

    explanation = """To find the GCD string:
1. If `str1 + str2 != str2 + str1`, then no GCD string exists, return "".
2. Otherwise, the length of the GCD string will be `gcd(len(str1), len(str2))`.
3. Return the prefix of `str1` with that length."""

    answer = """import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:math.gcd(len(str1), len(str2))]"""

    boilerplate = {
        "python": """import sys
import json
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        str1, str2 = json.loads(raw)
        sol = Solution()
        print(f'"{sol.gcdOfStrings(str1, str2)}"')""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        Solution sol;
        cout << "\\"" << sol.gcdOfStrings(j[0], j[1]) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String[] data = mapper.readValue(sc.nextLine(), String[].class);
            System.out.println("\\"" + new Solution().gcdOfStrings(data[0], data[1]) + "\\"");
        }
    }
}""",
        "javascript": """var gcdOfStrings = function(str1, str2) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [str1, str2] = JSON.parse(input);
    console.log(`"${gcdOfStrings(str1, str2)}"`);
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* gcdOfStrings(char* str1, char* str2) {
    // User logic here
    return "";
}

int main() {
    char s1[1005], s2[1005];
    int ch;
    while ((ch = getchar()) != EOF && ch != '"');
    scanf("%[^\\"]", s1);
    while ((ch = getchar()) != EOF && ch != '"');
    while ((ch = getchar()) != EOF && ch != '"');
    scanf("%[^\\"]", s2);
    printf("\\"%s\\"\\n", gcdOfStrings(s1, s2));
    return 0;
}"""
    }

    def solve(str1, str2):
        if str1 + str2 != str2 + str1: return ""
        return str1[:math.gcd(len(str1), len(str2))]

    test_cases_data = [
        ["ABCABC", "ABC"],    # Sample 1
        ["ABABAB", "ABAB"],   # Sample 2
        ["LEET", "CODE"],     # Sample 3
        ["ABC", "ABC"],
        ["AAAAAA", "AA"],
        ["AAAAA", "AAA"],     # Gcd length 1 -> "A"
        ["ABCDEF", "ABC"],
        # Stress tests
        ["A"*1000, "A"*999],
        ["AB"*500, "AB"*250],
        ["ABC"*333, "ABC"*111]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = f'"{solve(t[0], t[1])}"'
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "String"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
