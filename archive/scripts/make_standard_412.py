import json
import os

def generate_json():
    problem_id = 412
    title = "Fizz Buzz"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>412. Fizz Buzz</h3>
<p>Given an integer <code>n</code>, return <em>a string array </em><code>answer</code><em> (<strong>1-indexed</strong>) where:</em></p>

<ul>
	<li><code>answer[i] == "FizzBuzz"</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>.</li>
	<li><code>answer[i] == "Fizz"</code> if <code>i</code> is divisible by <code>3</code>.</li>
	<li><code>answer[i] == "Buzz"</code> if <code>i</code> is divisible by <code>5</code>.</li>
	<li><code>answer[i] == i</code> (as a string) if none of the above conditions are true.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["1","2","Fizz"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> ["1","2","Fizz","4","Buzz"]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer `n`."
    output_format = "A list of strings."
    
    constraints = [
        "1 <= n <= 10,000"
    ]
    
    explanation = """Iterate from 1 to $n$ and check divisibility by 3, 5, or both (15)."""
    
    answer = """class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0: res.append("FizzBuzz")
            elif i % 3 == 0: res.append("Fizz")
            elif i % 5 == 0: res.append("Buzz")
            else: res.append(str(i))
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # User Logic Here
        pass

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        n = int(raw_input)
        sol = Solution()
        print(json.dumps(sol.fizzBuzz(n)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        // User Logic Here
        return {};
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        vector<string> res = sol.fizzBuzz(n);
        cout << "[";
        for (int i = 0; i < res.size(); i++) {
            cout << "\\\"" << res[i] << "\\\"" << (i == res.size() - 1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<String> fizzBuzz(int n) {
        // User Logic Here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution sol = new Solution();
            List<String> res = sol.fizzBuzz(n);
            System.out.print("[");
            for (int i = 0; i < res.size(); i++) {
                System.out.print("\\\"" + res.get(i) + "\\\"" + (i == res.size() - 1 ? "" : ","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """var fizzBuzz = function(n) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const n = parseInt(input);
    console.log(JSON.stringify(fizzBuzz(n)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** fizzBuzz(int n, int* returnSize) {
    // User Logic Here
    return NULL;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        int returnSize = 0;
        char** res = fizzBuzz(n, &returnSize);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("\\\"%s\\\"%s", res[i], (i == returnSize - 1 ? "" : ","));
        }
        printf("]\\n");
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "3", "expected_output": '["1","2","Fizz"]', "is_sample": True},
        {"input": "5", "expected_output": '["1","2","Fizz","4","Buzz"]', "is_sample": True},
        {"input": "15", "expected_output": '["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]', "is_sample": False},
        {"input": "1", "expected_output": '["1"]', "is_sample": False},
        {"input": "2", "expected_output": '["1","2"]', "is_sample": False},
        {"input": "10", "expected_output": '["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz"]', "is_sample": False},
        {"input": "20", "expected_output": '["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16","17","Fizz","19","Buzz"]', "is_sample": False},
        # 3 Stress
        {"input": "100", "expected_output": json.dumps([("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)) for i in range(1, 101)]), "is_sample": False},
        {"input": "200", "expected_output": json.dumps([("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)) for i in range(1, 201)]), "is_sample": False},
        {"input": "1000", "expected_output": json.dumps([("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)) for i in range(1, 1001)]), "is_sample": False}
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

    output_path = f"301-500/{problem_id}_Fizz_Buzz.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
