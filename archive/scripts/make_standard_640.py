import json
import os

def generate_json():
    problem_id = 640
    title = "Solve the Equation"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>640. Solve the Equation</h3>
<p>Solve a given equation and return the value of <code>'x'</code> in the form of a string <code>"x=#value"</code>. The equation contains only <code>'+'</code>, <code>'-'</code> operation, the variable <code>'x'</code> and its coefficient. You should return <code>"No solution"</code> if there is no solution for the equation, or <code>"Infinite solutions"</code> if there are infinite solutions for the equation.</p>

<p>If there is exactly one solution for the equation, we ensure that the value of <code>'x'</code> is an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> equation = "x+5-3+x=6+x-2"
<strong>Output:</strong> "x=2"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> equation = "x=x"
<strong>Output:</strong> "Infinite solutions"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> equation = "2x=x"
<strong>Output:</strong> "x=0"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>3 &lt;= equation.length &lt;= 1000</code></li>
    <li><code>equation</code> has exactly one <code>'='</code>.</li>
    <li><code>equation</code> consists of integers with an absolute value in the range <code>[0, 100]</code> without any leading zeros, and the variable <code>'x'</code>.</li>
</ul>"""

    input_format = "A single line: a JSON string `equation`."
    output_format = 'A JSON string: "x=#value", "No solution", or "Infinite solutions".'

    constraints = [
        "3 <= equation.length <= 1000",
        "equation has exactly one '='"
    ]

    explanation = """Parse both sides of the equation to get coefficient of x and constant. Subtract right from left to get: coeff_diff * x = const_diff. Handle three cases: coeff != 0 gives x = -const/coeff; coeff == 0 and const == 0 gives infinite solutions; coeff == 0 and const != 0 gives no solution."""

    answer = """import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            coeff = const = 0
            expr = expr.replace('-', '+-')
            for term in expr.split('+'):
                if not term: continue
                if term == 'x': coeff += 1
                elif term == '-x': coeff -= 1
                elif term.endswith('x'): coeff += int(term[:-1])
                elif term: const += int(term)
            return coeff, const
        
        left, right = equation.split('=')
        lc, lk = parse(left)
        rc, rk = parse(right)
        dc, dk = lc - rc, rk - lk
        if dc == 0:
            return "Infinite solutions" if dk == 0 else "No solution"
        return f"x={dk // dc}" """

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def solveEquation(self, equation: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        equation = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.solveEquation(equation)))""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string solveEquation(string equation) {
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
        cout << "\\"" << sol.solveEquation(input) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String solveEquation(String equation) {
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
            System.out.println("\\"" + sol.solveEquation(raw) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string} equation
 * @return {string}
 */
var solveEquation = function(equation) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const equation = JSON.parse(input);
    console.log(JSON.stringify(solveEquation(equation)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solveEquation(char* equation) {
    // User logic here
    char* res = (char*)malloc(50);
    strcpy(res, "");
    return res;
}

int main() {
    char input[2000];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char eq[2000];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(eq, input + 1, len - 2);
            eq[len - 2] = '\\0';
        } else {
            strcpy(eq, input);
        }
        char* res = solveEquation(eq);
        printf("\\"%s\\"\\n", res);
        free(res);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"x+5-3+x=6+x-2"', "expected_output": '"x=2"', "is_sample": True},
        {"input": '"x=x"', "expected_output": '"Infinite solutions"', "is_sample": True},
        {"input": '"2x=x"', "expected_output": '"x=0"', "is_sample": False},
        {"input": '"2x+3x-6x=x+2"', "expected_output": '"x=-1"', "is_sample": False},
        {"input": '"x=x+2"', "expected_output": '"No solution"', "is_sample": False},
        {"input": '"0x=0"', "expected_output": '"Infinite solutions"', "is_sample": False},
        {"input": '"0x=1"', "expected_output": '"No solution"', "is_sample": False},
        {"input": '"100x+100=200x"', "expected_output": '"x=1"', "is_sample": False},
        {"input": '"-x+1=-x+1"', "expected_output": '"Infinite solutions"', "is_sample": False},
        {"input": '"x+1=2x-1"', "expected_output": '"x=2"', "is_sample": False}
    ]

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

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
