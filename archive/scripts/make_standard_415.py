import json
import os

def generate_json():
    problem_id = 415
    title = "Add Strings"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>415. Add Strings</h3>
<p>Given two non-negative integers, <code>num1</code> and <code>num2</code> represented as string, return <em>the sum of</em> <code>num1</code> <em>and</em> <code>num2</code> <em>as a string</em>.</p>

<p>You must solve the problem without using any built-in library for handling large integers (such as <code>BigInteger</code>). You must also not convert the inputs to integers directly.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num1 = "11", num2 = "123"
<strong>Output:</strong> "134"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num1 = "456", num2 = "77"
<strong>Output:</strong> "533"
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> num1 = "0", num2 = "0"
<strong>Output:</strong> "0"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= num1.length, num2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>num1</code> and <code>num2</code> consist of only digits.</li>
	<li><code>num1</code> and <code>num2</code> don't have any leading zeros except for the zero itself.</li>
</ul>"""

    input_format = "Two strings `num1` and `num2`."
    output_format = "A string representing the sum."
    
    constraints = [
        "1 <= lengths <= 10,000",
        "No direct int() or BigInteger usage.",
        "Manual addition required."
    ]
    
    explanation = """To add two large numbers represented as strings without direct conversion, we simulate the standard pencil-and-paper addition algorithm."""
    
    answer = """class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1
        while p1 >= 0 or p2 >= 0 or carry:
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0
            s = d1 + d2 + carry
            res.append(str(s % 10))
            carry = s // 10
            p1, p2 = p1 - 1, p2 - 1
        return "".join(res[::-1])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        num1 = lines[0].strip()
        num2 = lines[1].strip()
        if num1.startswith('"') and num1.endswith('"'): num1 = num1[1:-1]
        if num2.startswith('"') and num2.endswith('"'): num2 = num2[1:-1]
        sol = Solution()
        print(json.dumps(sol.addStrings(num1, num2)))""",
        "cpp": """#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    string addStrings(string num1, string num2) {
        // User Logic Here
        return "";
    }
};

int main() {
    string num1, num2;
    if (getline(cin, num1) && getline(cin, num2)) {
        if (num1.size() >= 2 && num1.front() == '"' && num1.back() == '"') num1 = num1.substr(1, num1.size() - 2);
        if (num2.size() >= 2 && num2.front() == '"' && num2.back() == '"') num2 = num2.substr(1, num2.size() - 2);
        Solution sol;
        cout << sol.addStrings(num1, num2) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String addStrings(String num1, String num2) {
        // User Logic Here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String num1 = sc.nextLine().trim();
            if (num1.startsWith("\\\"") && num1.endsWith("\\\"")) num1 = num1.substring(1, num1.length() - 1);
            if (sc.hasNextLine()) {
                String num2 = sc.nextLine().trim();
                if (num2.startsWith("\\\"") && num2.endsWith("\\\"")) num2 = num2.substring(1, num2.length() - 1);
                Solution sol = new Solution();
                System.out.println(sol.addStrings(num1, num2));
            }
        }
    }
}""",
        "javascript": """var addStrings = function(num1, num2) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    let num1 = input[0].trim();
    let num2 = input[1].trim();
    if (num1.startsWith('"') && num1.endswith('"')) num1 = num1.slice(1, -1);
    if (num2.startsWith('"') && num2.endswith('"')) num2 = num2.slice(1, -1);
    console.log(JSON.stringify(addStrings(num1, num2)));
}""",
        "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* addStrings(char* num1, char* num2) {
    // User Logic Here
    return "";
}

int main() {
    char num1[10005], num2[10005];
    if (fgets(num1, 10005, stdin) && fgets(num2, 10005, stdin)) {
        num1[strcspn(num1, "\\n")] = 0;
        num2[strcspn(num2, "\\n")] = 0;
        char *p1 = num1, *p2 = num2;
        if (*p1 == '"') { p1++; num1[strlen(num1)-1] = 0; }
        if (*p2 == '"') { p2++; num2[strlen(num2)-1] = 0; }
        printf("%s\\n", addStrings(p1, p2));
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"11"\n"123"', "expected_output": '"134"', "is_sample": True},
        {"input": '"456"\n"77"', "expected_output": '"533"', "is_sample": True},
        {"input": '"0"\n"0"', "expected_output": '"0"', "is_sample": False},
        {"input": '"999"\n"1"', "expected_output": '"1000"', "is_sample": False},
        {"input": '"1"\n"9"', "expected_output": '"10"', "is_sample": False},
        {"input": '"123456789"\n"987654321"', "expected_output": '"1111111110"', "is_sample": False},
        {"input": '"100"\n"200"', "expected_output": '"300"', "is_sample": False},
        # 3 Stress
        {"input": '"' + "9" * 1000 + '"\n"1"', "expected_output": '"1' + "0" * 1000 + '"', "is_sample": False},
        {"input": '"' + "1" * 1000 + '"\n"' + "2" * 1000 + '"', "expected_output": '"' + "3" * 1000 + '"', "is_sample": False},
        {"input": '"0"\n"123456789"', "expected_output": '"123456789"', "is_sample": False}
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
        "topics": ["Math", "String", "Simulation"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Add_Strings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
