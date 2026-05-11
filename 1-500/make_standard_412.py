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
        "python": "import sys\nimport json\n\nclass Solution:\n    def fizzBuzz(self, n: int) -> list[str]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        n = int(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.fizzBuzz(n)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<string> fizzBuzz(int n) {\n        // User logic here\n        return {};\n    }\n};\n\nint main() {\n    int n;\n    if (cin >> n) {\n        Solution sol;\n        vector<string> res = sol.fizzBuzz(n);\n        cout << \"[\";\n        for (int i = 0; i < res.size(); i++) {\n            cout << \"\\\\\\\"\" << res[i] << \"\\\\\\\"\" << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<String> fizzBuzz(int n) {\n        // User logic here\n        return new ArrayList<>();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            Solution sol = new Solution();\n            List<String> res = sol.fizzBuzz(n);\n            System.out.print(\"[\");\n            for (int i = 0; i < res.size(); i++) {\n                System.out.print(\"\\\\\\\"\" + res.get(i) + \"\\\\\\\"\" + (i == res.size() - 1 ? \"\" : \",\"));\n            }\n            System.out.println(\"]\");\n        }\n    }\n}",
        "javascript": "var fizzBuzz = function(n) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const n = parseInt(input);\n    console.log(JSON.stringify(fizzBuzz(n)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar** fizzBuzz(int n, int* returnSize) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int returnSize = 0;\n        char** res = fizzBuzz(n, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"\\\\\\\"%s\\\\\\\"%s\", res[i], (i == returnSize - 1 ? \"\" : \",\"));\n        }\n        printf(\"]\\\\n\");\n    }\n    return 0;\n}"
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
