import json
import os

def generate_json():
    problem_id = 433
    title = "Minimum Genetic Mutation"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>433. Minimum Genetic Mutation</h3>
<p>A gene string can be represented by an 8-character long string, with choices from <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.</p>

<p>Suppose we need to investigate a mutation from a gene string <code>startGene</code> to a gene string <code>endGene</code>, where one mutation is defined as one single character changed in the gene string.</p>

<ul>
	<li>For example, <code>"AACCGGTT" --&gt; "AACCGGTA"</code> is one mutation.</li>
</ul>

<p>There is also a gene bank <code>bank</code> that records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.</p>

<p>Given the two gene strings <code>startGene</code> and <code>endGene</code> and the gene bank <code>bank</code>, return <em>the minimum number of mutations needed to mutate from </em><code>startGene</code><em> to </em><code>endGene</code>. If there is no such a mutation, return <code>-1</code>.</p>

<p>Note that the starting point is assumed to be valid, so it might not be included in the bank.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>startGene.length == endGene.length == 8</code></li>
	<li><code>bank[i].length == 8</code></li>
	<li><code>startGene</code>, <code>endGene</code>, and <code>bank[i]</code> consist of characters <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.</li>
</ul>"""

    input_format = "Three lines: startGene, endGene, and bank (JSON array of strings)."
    output_format = "An integer representing the minimum number of mutations."
    
    constraints = [
        "0 <= bank.length <= 10",
        "startGene.length == endGene.length == 8",
        "bank[i].length == 8",
        "Genes consist of 'A', 'C', 'G', and 'T'."
    ]
    
    explanation = """Finding the minimum number of mutations is equivalent to finding the shortest path in an unweighted graph where each node is a valid gene string and an edge exists between two nodes if they differ by exactly one character. Breadth-First Search (BFS) is ideal for finding the shortest path in such a graph."""
    
    answer = """from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            curr, steps = queue.popleft()
            if curr == endGene:
                return steps
            
            for i in range(len(curr)):
                for char in 'ACGT':
                    if char == curr[i]: continue
                    mutation = curr[:i] + char + curr[i+1:]
                    if mutation in bank_set and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, steps + 1))
        return -1"""

    boilerplate = {
        "python": "import sys\nimport json\nfrom collections import deque\n\nclass Solution:\n    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 3:\n        startGene = lines[0].strip()\n        endGene = lines[1].strip()\n        bank = json.loads(lines[2].strip())\n        sol = Solution()\n        print(sol.minMutation(startGene, endGene, bank))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <unordered_set>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int minMutation(string startGene, string endGene, vector<string>& bank) {\n        // User logic here\n        return -1;\n    }\n};\n\nint main() {\n    string start, end, bankLine;\n    if (cin >> start >> end) {\n        cin.ignore();\n        if (getline(cin, bankLine)) {\n            vector<string> realBank;\n            int i = 0;\n            while(i < bankLine.length()){\n                if(bankLine[i] == '\"'){\n                    int j = i+1;\n                    while(j < bankLine.length() && bankLine[j] != '\"') j++;\n                    realBank.push_back(bankLine.substr(i+1, j-i-1));\n                    i = j;\n                }\n                i++;\n            }\n            Solution sol;\n            cout << sol.minMutation(start, end, realBank) << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int minMutation(String startGene, String endGene, String[] bank) {\n        // User logic here\n        return -1;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String start = sc.nextLine().trim();\n            if (sc.hasNextLine()) {\n                String end = sc.nextLine().trim();\n                if (sc.hasNextLine()) {\n                    String bankLine = sc.nextLine().trim();\n                    List<String> bank = new ArrayList<>();\n                    int i = 0;\n                    while(i < bankLine.length()){\n                        if(bankLine.charAt(i) == '\"'){\n                            int j = i+1;\n                            while(j < bankLine.length() && bankLine.charAt(j) != '\"') j++;\n                            bank.add(bankLine.substring(i+1, j));\n                            i = j;\n                        }\n                        i++;\n                    }\n                    Solution sol = new Solution();\n                    System.out.println(sol.minMutation(start, end, bank.toArray(new String[0])));\n                }\n            }\n        }\n    }\n}",
        "javascript": "var minMutation = function(startGene, endGene, bank) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 3) {\n    const start = input[0].trim();\n    const end = input[1].trim();\n    const bank = JSON.parse(input[2].trim());\n    console.log(minMutation(start, end, bank));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint minMutation(char* startGene, char* endGene, char** bank, int bankSize) {\n    // User logic here\n    return -1;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "AACCGGTT\\nAACCGGTA\\n[\\\"AACCGGTA\\\"]", "expected_output": "1", "is_sample": True},
        {"input": "AACCGGTT\\nAAACGGTA\\n[\\\"AACCGGTA\\\",\\\"AACCGCTA\\\",\\\"AAACGGTA\\\"]", "expected_output": "2", "is_sample": True},
        {"input": "AACCGGTT\\nAACCGGTA\\n[]", "expected_output": "-1", "is_sample": False},
        {"input": "AAAAAAAA\\nCCCCCCCC\\n[\\\"AAAAAAAC\\\",\\\"AAAAAACC\\\",\\\"AAAAACCC\\\",\\\"AAAACCCC\\\",\\\"AAACCCCC\\\",\\\"AACCCCCC\\\",\\\"ACCCCCCC\\\",\\\"CCCCCCCC\\\"]", "expected_output": "8", "is_sample": False},
        {"input": "AACCGGTT\\nAACCGGTT\\n[\\\"AACCGGTT\\\"]", "expected_output": "0", "is_sample": False},
        {"input": "AAAAAAAA\\nAAAAAAAT\\n[ \\\"AAAAAAAT\\\" ]", "expected_output": "1", "is_sample": False}, # Spaces
        {"input": "AAAAAAAC\\nAAAAAAAT\\n[\\\"AAAAAAAT\\\"]", "expected_output": "1", "is_sample": False},
        {"input": "TTAAAAAA\\nAAAAAAAA\\n[\\\"TAAAAAAA\\\",\\\"AAAAAAAA\\\"]", "expected_output": "2", "is_sample": False},
        # Stress
        {"input": "AAAAAAAA\\nTTTTTTTT\\n[\\\"AAAAAAAT\\\",\\\"AAAAAATT\\\",\\\"AAAAATTT\\\",\\\"AAAATTTT\\\",\\\"AAATTTTT\\\",\\\"AATTTTTT\\\",\\\"ATTTTTTT\\\",\\\"TTTTTTTT\\\"]", "expected_output": "8", "is_sample": False},
        {"input": "AAAAAAAA\\nAAAAAAAA\\n[]", "expected_output": "0", "is_sample": False}
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
        "topics": ["Hash Table", "String", "BFS"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Minimum_Genetic_Mutation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
