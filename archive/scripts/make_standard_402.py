import json
import os

def generate_json():
    problem_id = 402
    title = "Remove K Digits"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>402. Remove K Digits</h3>
<p>Given string num representing a non-negative integer <code>num</code>, and an integer <code>k</code>, return <em>the smallest possible integer after removing</em> <code>k</code> <em>digits from</em> <code>num</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = "1432219", k = 3
<strong>Output:</strong> "1219"
<strong>Explanation:</strong> Remove the three digits 4, 3, and 2 to form the new integer 1219 which is the smallest.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = "10200", k = 1
<strong>Output:</strong> "200"
<strong>Explanation:</strong> Remove the leading 1 and the smallest number is 200. Note that the output must not contain leading zeroes.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> num = "10", k = 2
<strong>Output:</strong> "0"
<strong>Explanation:</strong> Remove all the digits from the number and it is left with nothing which is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= k &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>num</code> does not have any leading zeros except for the zero itself.</li>
</ul>"""

    input_format = "A string `num` and an integer `k`."
    output_format = "The smallest number string."
    
    constraints = [
        "1 <= k <= num.length <= 100,000",
        "Result must not have leading zeros.",
        "Must be O(N) time complexity."
    ]
    
    explanation = """To get the smallest possible number, we want the most significant digits (the leftmost ones) to be as small as possible. This suggests a **Greedy** approach using a **Monotonic Stack**."""
    
    answer = """class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        if k > 0:
            stack = stack[:-k]
            
        res = "".join(stack).lstrip('0')
        return res if res else "0" """

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        num = lines[0].strip()
        if num.startswith('"') and num.endswith('"'): num = num[1:-1]
        k = int(lines[1].strip())
        sol = Solution()
        print(json.dumps(sol.removeKdigits(num, k)))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        // User Logic Here
        return "";
    }
};

int main() {
    string num;
    int k;
    if (getline(cin, num) && (cin >> k)) {
        if (num.size() >= 2 && num.front() == '"' && num.back() == '"') num = num.substr(1, num.size() - 2);
        Solution sol;
        cout << sol.removeKdigits(num, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String removeKdigits(String num, int k) {
        // User Logic Here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String num = sc.nextLine().trim();
            if (num.startsWith("\\\"") && num.endsWith("\\\"")) num = num.substring(1, num.length() - 1);
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.removeKdigits(num, k));
            }
        }
    }
}""",
        "javascript": """var removeKdigits = function(num, k) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    let num = input[0].trim();
    if (num.startsWith('"') && num.endsWith('"')) num = num.slice(1, -1);
    const k = parseInt(input[1].trim());
    console.log(JSON.stringify(removeKdigits(num, k)));
}""",
        "c": """#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* removeKdigits(char* num, int k) {
    // User Logic Here
    return "";
}

int main() {
    char num[100005];
    int k;
    if (fgets(num, 100005, stdin)) {
        num[strcspn(num, "\\n")] = 0;
        char *ptr = num;
        if (num[0] == '"') { ptr++; num[strlen(num)-1] = 0; }
        if (scanf("%d", &k) == 1) {
            printf("%s\\n", removeKdigits(ptr, k));
        }
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '"1432219"\n3', "expected_output": '"1219"', "is_sample": True},
        {"input": '"10200"\n1', "expected_output": '"200"', "is_sample": True},
        # 5 Diverse
        {"input": '"10"\n2', "expected_output": '"0"', "is_sample": False},
        {"input": '"9"\n1', "expected_output": '"0"', "is_sample": False},
        {"input": '"112"\n1', "expected_output": '"11"', "is_sample": False},
        {"input": '"1234567890"\n9', "expected_output": '"0"', "is_sample": False},
        {"input": '"1000"\n1', "expected_output": '"0"', "is_sample": False},
        # 3 Stress
        {"input": '"' + '1' * 100 + '"\n50', "expected_output": '"' + '1' * 50 + '"', "is_sample": False},
        {"input": '"9876543210"\n5', "expected_output": '"43210"', "is_sample": False},
        {"input": '"5432198765"\n3', "expected_output": '"2198765"', "is_sample": False}
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
        "topics": ["String", "Stack", "Greedy", "Monotonic Stack"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Remove_K_Digits.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
