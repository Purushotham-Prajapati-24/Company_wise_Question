import json
import os

def generate_json():
    problem_id = 1256
    title = "Encode Number"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1256. Encode Number</h3>
<p>Given a non-negative integer <code>num</code>, return its <em>encoding</em> string.</p>

<p>The encoding is done by converting the integer to a string using a sequence from the following table:</p>
<pre>
n | f(n)
--|-----
0 | ""
1 | "0"
2 | "1"
3 | "00"
4 | "01"
5 | "10"
6 | "11"
7 | "000"
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = 23
<strong>Output:</strong> "1000"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = 107
<strong>Output:</strong> "101100"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A non-negative integer `num` as a JSON number."
    output_format = "A string representing the encoded result."

    constraints = [
        "0 <= num <= 10^9"
    ]

    explanation = """To encode the number `n`:
1. Observe the sequence: it's basically the binary representation of `n+1` without the leading '1'.
2. For example:
   - n=0: 0+1=1 (binary "1") -> ""
   - n=1: 1+1=2 (binary "10") -> "0"
   - n=2: 2+1=3 (binary "11") -> "1"
   - n=3: 3+1=4 (binary "100") -> "00"
   - n=23: 23+1=24 (binary "11000") -> "1000"
3. Calculation: `bin(num + 1)[3:]`"""

    answer = """class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def encode(self, num: int) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        num = int(raw)
        sol = Solution()
        print(sol.encode(num))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <bitset>

using namespace std;

class Solution {
public:
    string encode(int num) {
        // User logic here
        return "";
    }
};

int main() {
    int num;
    if (cin >> num) {
        Solution sol;
        cout << sol.encode(num) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String encode(int num) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            System.out.println(new Solution().encode(sc.nextInt()));
        }
    }
}""",
        "javascript": """var encode = function(num) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').strip();
if (input) {
    console.log(encode(parseInt(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * encode(int num){
    // User logic here
    return "";
}

int main() {
    int num;
    if(scanf("%d", &num) == 1) {
        printf("%s\\n", encode(num));
    }
    return 0;
}"""
    }

    def solve(num):
        return bin(num + 1)[3:]

    test_cases_data = [
        23,           # Sample 1
        107,          # Sample 2
        0,            # Edge zero
        1,            # Edge one
        2,            # Edge two
        3,            # Edge three
        7,            # Edge seven
        # Stress tests
        10**9,
        10**9 - 1,
        123456789
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = str(t)
        out = solve(t)
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "String", "Bit Manipulation"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
