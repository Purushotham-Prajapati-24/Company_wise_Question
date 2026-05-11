import json
import os

def generate_json():
    problem_id = 592
    title = "Fraction Addition and Subtraction"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>592. Fraction Addition and Subtraction</h3>
<p>Given a string <code>expression</code> representing an expression of fraction addition and subtraction, return the calculation result in string format.</p>

<p>The final result should be an <a href="https://en.wikipedia.org/wiki/Irreducible_fraction" target="_blank">irreducible fraction</a>. If your final result is an integer, change it to the format of a fraction that has a denominator <code>1</code>. So in this case, <code>2</code> should be converted to <code>2/1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> expression = "-1/2+1/2"
<strong>Output:</strong> "0/1"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> expression = "-1/2+1/2+1/3"
<strong>Output:</strong> "1/3"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> expression = "1/3-1/2"
<strong>Output:</strong> "-1/6"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li>The input string only contains <code>'0'</code> to <code>'9'</code>, <code>'/'</code>, <code>'+'</code> and <code>'-'</code>. So does the output.</li>
    <li>Each fraction (input and output) has the format <code>&plusmn;numerator/denominator</code>. If the first input fraction or the output is positive, then <code>'+'</code> will be omitted.</li>
    <li>The input only contains valid <strong>irreducible fractions</strong>, where the <strong>numerator</strong> and <strong>denominator</strong> of each fraction will always be in the range <code>[1, 10]</code>. If the denominator is <code>1</code>, it means this fraction is actually an integer in a fraction format defined above.</li>
    <li>The number of given fractions will be in the range <code>[1, 10]</code>.</li>
    <li>The numerator and denominator of the <strong>final result</strong> are guaranteed to be valid and in the range of <strong>32-bit</strong> int.</li>
</ul>"""

    input_format = "A single line: a JSON string `expression`."
    output_format = "A JSON string of the calculated irreducible fraction."

    constraints = [
        "expression only contains '0' to '9', '/', '+' and '-'",
        "Number of elements in the expression is in [1, 10]"
    ]

    explanation = """Parse the string into numerators and denominators. Maintain a running sum of the fractions. Use the greatest common divisor (GCD) to reduce the fraction to its irreducible form at the end (or progressively)."""

    answer = """import re
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\\d+', expression)))
        numerator = 0
        denominator = 1
        for i in range(0, len(nums), 2):
            num = nums[i]
            den = nums[i+1]
            numerator = numerator * den + num * denominator
            denominator *= den
            g = math.gcd(abs(numerator), abs(denominator))
            numerator //= g
            denominator //= g
        return f"{numerator}/{denominator}" """

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        expression = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.fractionAddition(expression)))""",
        "cpp": """#include <iostream>
#include <string>
#include <numeric>
#include <sstream>

using namespace std;

class Solution {
public:
    string fractionAddition(string expression) {
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
        cout << "\\"" << sol.fractionAddition(input) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String fractionAddition(String expression) {
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
            System.out.println("\\"" + sol.fractionAddition(raw) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string} expression
 * @return {string}
 */
var fractionAddition = function(expression) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const expression = JSON.parse(input);
    console.log(JSON.stringify(fractionAddition(expression)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* fractionAddition(char* expression) {
    // User logic here
    char* res = (char*)malloc(50);
    strcpy(res, "");
    return res;
}

int main() {
    char input[100];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char expression[100];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(expression, input + 1, len - 2);
            expression[len - 2] = '\\0';
        } else {
            strcpy(expression, input);
        }
        char* res = fractionAddition(expression);
        printf("\\"%s\\"\\n", res);
        free(res);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"-1/2+1/2"', "expected_output": '"0/1"', "is_sample": True},
        {"input": '"-1/2+1/2+1/3"', "expected_output": '"1/3"', "is_sample": True},
        {"input": '"1/3-1/2"', "expected_output": '"-1/6"', "is_sample": True},
        {"input": '"5/3+1/3"', "expected_output": '"2/1"', "is_sample": False},
        {"input": '"1/10+1/10+1/10+1/10"', "expected_output": '"2/5"', "is_sample": False},
        {"input": '"-5/2+10/3+7/9"', "expected_output": '"29/18"', "is_sample": False},
        {"input": '"1/2-1/2"', "expected_output": '"0/1"', "is_sample": False},
        
        {"input": '"' + "+".join("10/9" for _ in range(10)) + '"', "expected_output": '"100/9"', "is_sample": False},
        {"input": '"' + "".join("-10/9" for _ in range(10)) + '"', "expected_output": '"-100/9"', "is_sample": False},
        {"input": '"' + "".join(("+1/3" if i%2==0 else "-1/2") for i in range(10)) + '"', "expected_output": '"-5/6"', "is_sample": False}
    ]
    test_cases[9]["input"] = '"' + "+1/3-1/2+1/3-1/2+1/3-1/2+1/3-1/2+1/3-1/2".lstrip('+') + '"'


    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "String", "Simulation"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
