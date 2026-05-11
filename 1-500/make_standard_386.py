import json
import os

def generate_json():
    problem_id = 386
    title = "Lexicographical Numbers"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>386. Lexicographical Numbers</h3>
<p>Given an integer <code>n</code>, return all the numbers in the range <code>[1, n]</code> sorted in lexicographical order.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and uses <code>O(1)</code> extra space.&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 13
<strong>Output:</strong> [1,10,11,12,13,2,3,4,5,6,7,8,9]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An integer `n`."
    output_format = "A list of integers in lexicographical order."
    
    constraints = [
        "1 <= n <= 50,000",
        "O(n) time and O(1) space (excluding output)."
    ]
    
    explanation = """To generate numbers in lexicographical order, we can think of the numbers as nodes in a **Trie** where each node has up to 10 children (digits 0-9).

### Algorithm Steps:
We can simulate a Pre-order traversal of this Trie iteratively:
1. **Initialize**: Start with `curr = 1`.
2. **Loop** $n$ times:
   - Add `curr` to the result list.
   - **Try going deeper**: If `curr * 10 <= n`, the next lexicographical number is `curr * 10`.
   - **Try going wider**: 
     - If we reach the limit `n` or the number ends in `9` (e.g. `19`, `13` where $n=13$):
       - We need to backtrack. While `curr % 10 == 9` or `curr + 1 > n`, divide `curr` by 10.
     - The next number is `curr + 1`.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, as we visit each number from 1 to $N$ exactly once.
- **Space Complexity**: $O(1)$ extra space (if we don't count the output array), as we only maintain the variable `curr`."""
    
    answer = """class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def lexicalOrder(self, n: int) -> list[int]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        n = int(line)\n        sol = Solution()\n        print(json.dumps(sol.lexicalOrder(n)).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> lexicalOrder(int n) {\n        // User logic here\n        return {};\n    }\n};\n\nint main() {\n    int n;\n    if (cin >> n) {\n        Solution sol;\n        vector<int> res = sol.lexicalOrder(n);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); ++i) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<Integer> lexicalOrder(int n) {\n        // User logic here\n        return new ArrayList<>();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int n = sc.nextInt();\n            Solution sol = new Solution();\n            List<Integer> res = sol.lexicalOrder(n);\n            System.out.println(res.toString().replace(\" \", \"\"));\n        }\n    }\n}",
        "javascript": "var lexicalOrder = function(n) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const n = parseInt(input);\n    console.log(JSON.stringify(lexicalOrder(n)).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\n/**\n * Note: The returned array must be malloced.\n * *returnSize = n;\n */\nint* lexicalOrder(int n, int* returnSize) {\n    // User logic here\n    return NULL;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int returnSize = 0;\n        int* res = lexicalOrder(n, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], (i == returnSize - 1 ? \"\" : \",\"));\n        }\n        printf(\"]\\n\");\n        if (res) free(res);\n    }\n    return 0;\n}"
    }

    def get_lexical(n):
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return res

    test_cases = [
        {"input": "13", "expected_output": json.dumps(get_lexical(13)).replace(' ', ''), "is_sample": True},
        {"input": "2", "expected_output": json.dumps(get_lexical(2)).replace(' ', ''), "is_sample": True},
        # 5 Diverse
        {"input": "1", "expected_output": "[1]", "is_sample": False},
        {"input": "5", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "10", "expected_output": "[1,10,2,3,4,5,6,7,8,9]", "is_sample": False},
        {"input": "11", "expected_output": "[1,10,11,2,3,4,5,6,7,8,9]", "is_sample": False},
        {"input": "20", "expected_output": "[1,10,11,12,13,14,15,16,17,18,19,2,20,3,4,5,6,7,8,9]", "is_sample": False},
        # 3 Stress
        {"input": "50", "expected_output": json.dumps(get_lexical(50)).replace(' ', ''), "is_sample": False},
        {"input": "100", "expected_output": json.dumps(get_lexical(100)).replace(' ', ''), "is_sample": False},
        {"input": "200", "expected_output": json.dumps(get_lexical(200)).replace(' ', ''), "is_sample": False}
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
        "topics": ["Depth-First Search", "Trie"],
        "companyIndex": 1
    }

    output_path = "301-500/386_Lexicographical_Numbers.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
