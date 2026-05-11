import json
import os


def generate_json():
    problem_id = 269
    title = "Alien Dictionary"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>269. Alien Dictionary</h3>
<p>There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.</p>

<p>You are given a list of strings <code>words</code> from the alien language's dictionary, where the strings in <code>words</code> are <strong>sorted lexicographically</strong> by the rules of this new language.</p>

<p>Return <em>a string of the unique letters in the new alien language sorted in <strong>lexicographically increasing order</strong> by the new language's rules. If there is no solution, return </em><code>""</code><em>. If there are multiple solutions, return <strong>any of them</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["wrt","wrf","er","ett","rftt"]
<strong>Output:</strong> "wertf"</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["z","x"]
<strong>Output:</strong> "zx"</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["z","x","z"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> The order is invalid, so return "".</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
</ul>"""

    input_format = "A list of space-separated strings representing the dictionary."
    output_format = "A string representing the character order, or an empty string if invalid."
    
    constraints = []
    
    explanation = """HARD problem on ."""
    
    answer = """import collections

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = collections.defaultdict(set)
        in_degree = {c: 0 for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return "" # Invalid prefix
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
                    
        queue = collections.deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        if len(res) < len(in_degree):
            return "" # Cycle detected
        return "".join(res)"""

    boilerplate = {
        "python": "import sys\n\ndef alienOrder(words: list[str]) -> str:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().split()\n    print(alienOrder(input_data))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nstring alienOrder(vector<string>& words) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    vector<string> words;\n    string w;\n    while (cin >> w) {\n        words.push_back(w);\n    }\n    string res = alienOrder(words);\n    cout << res << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public String alienOrder(String[] words) {\n        // User logic\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<String> list = new ArrayList<>();\n        while (sc.hasNext()) {\n            list.add(sc.next());\n        }\n        System.out.println(new Solution().alienOrder(list.toArray(new String[0])));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction alienOrder(words) {\n    // User logic\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/);\nif (input.length > 0 && input[0] !== '') {\n    console.log(alienOrder(input));\n} else {\n    console.log(\"\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nchar* alienOrder(char** words, int wordsSize) {\n    // User logic\n    return \"\";\n}\n\nint main() {\n    char** words = malloc(1000 * sizeof(char*));\n    int size = 0;\n    char w[105];\n    while (scanf(\"%104s\", w) == 1) {\n        words[size++] = strdup(w);\n    }\n    char* res = alienOrder(words, size);\n    printf(\"%s\\n\", res ? res : \"\");\n    return 0;\n}"
    }

    test_cases = [{"input": "wrt wrf er ett rftt", "expected_output": "wertf", "is_sample": True},
        {"input": "z x", "expected_output": "zx", "is_sample": True},
        {"input": "z x z", "expected_output": "", "is_sample": True},
        {"input": "abc ab", "expected_output": "", "is_sample": False}, # Invalid prefix
        {"input": "a b c", "expected_output": "abc", "is_sample": False},
        {"input": "z z", "expected_output": "z", "is_sample": False},
        {"input": "ab ac", "expected_output": "abc", "is_sample": False}, # b < c, a is first
        {"input": "zy zx", "expected_output": "yxz", "is_sample": False}, # y < x
        {"input": "wrt wrf er ett rftt", "expected_output": "wertf", "is_sample": False},
        {"input": "ri h i", "expected_output": "rih", "is_sample": False}]

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
        "topics": ["Array", "String", "Depth-First Search", "Breadth-First Search", "Graph", "Topological Sort"],
        "companyIndex": 0
    }

    output_path = ""
    if not output_path or output_path == "":
        output_path = f"CompanyQuestion/STANDARD/{problem_id}_{title.replace(' ', '_')}.json"
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
