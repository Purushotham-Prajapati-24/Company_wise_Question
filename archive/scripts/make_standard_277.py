import json
import os

def generate_json():
    problem_id = 277
    title = "Find the Celebrity"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>277. Find the Celebrity</h3>
<p>Suppose you are at a party with <code>n</code> people (labeled from <code>0</code> to <code>n - 1</code>) and among them, there may exist one celebrity. The definition of a celebrity is that all the other <code>n - 1</code> people know him/her but he/she does not know any of them.</p>

<p>You are provided with a helper function <code>bool knows(a, b)</code> that tells you whether <code>a</code> knows <code>b</code>. Implement a function <code>int findCelebrity(int n)</code>, your task is to find the celebrity (or return -1 if there is no celebrity).</p>

<p>There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> graph = [[1,1,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are three people labeled 0, 1 and 2. knows(0, 1) is True, knows(2, 1) is True. And knows(1, 0) is False, knows(1, 2) is False. So person 1 is the celebrity.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> graph = [[1,0,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> knows(0, 2) is True, knows(1, 0) is True and knows(2, 1) is True. Everyone knows someone, so there is no celebrity.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == graph.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>knows(a, b)</code> is <code>O(1)</code>.</li>
</ul>"""

    input_format = "A stringified 2D array (graph) representing the people's relationships."
    output_format = "The label of the celebrity as an integer, or -1."
    
    constraints = [
        "2 <= n <= 100",
        "knows(a, b) is O(1)."
    ]
    
    explanation = """To find the celebrity in O(n) calls to `knows(a, b)`:
1. **Find a Candidate**: Start with a candidate `person = 0`. Iterate through all other people `i`. If `knows(person, i)` is true, it means `person` cannot be the celebrity, and `i` might be. So update `candidate = i`. 
2. **Elimination Logic**: Each call to `knows(a, b)` eliminates one person:
   - If `knows(a, b)` is True, `a` cannot be the celebrity (as a celebrity knows no one).
   - If `knows(a, b)` is False, `b` cannot be the celebrity (as every person knows the celebrity).
3. **Verify Candidate**: After finding a potential `candidate`, you must verify that:
   - Everyone else knows the candidate: `knows(i, candidate)` is True for all `i != candidate`.
   - The candidate knows no one: `knows(candidate, i)` is False for all `i != candidate`.
4. **Complexity**:
   - Time: O(N) calls to `knows`.
   - Space: O(1)."""
    
    answer = """# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        
        # Step 1: Find a candidate. 
        # For each comparison, we eliminate one person.
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
                
        # Step 2: Verification. 
        # Check if everyone knows the candidate and the candidate doesn't know anyone.
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
                
        return candidate"""

    boilerplate = {
        "python": "import sys\nimport json\n\ngraph_global = []\n\ndef knows(a, b):\n    return bool(graph_global[a][b])\n\ndef findCelebrity(n: int) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        graph_global = json.loads(input_data)\n        n = len(graph_global)\n        print(findCelebrity(n))",
        "cpp": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nvector<vector<int>> GRAPH;\nbool knows(int a, int b) { return GRAPH[a][b] == 1; }\n\nint findCelebrity(int n) {\n    // User logic here\n    return -1;\n}\n\nint main() {\n    string line;\n    vector<vector<int>> g;\n    while (getline(cin, line)) {\n        if (line.empty()) continue;\n        vector<int> row;\n        for (char c : line) if (c == '0' || c == '1') row.push_back(c - '0');\n        if (!row.empty()) g.push_back(row);\n    }\n    GRAPH = g;\n    cout << findCelebrity((int)g.size()) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    static int[][] GRAPH;\n    static boolean knows(int a, int b) { return GRAPH[a][b] == 1; }\n    public int findCelebrity(int n) {\n        // User logic here\n        return -1;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String input = sc.useDelimiter(\"\\\\A\").next().trim();\n        // Parse JSON-like grid\n        String[] rows = input.replaceAll(\"[\\\\[\\\\]]\", \"\").split(\",\");\n        int side = (int)Math.sqrt(rows.length);\n        GRAPH = new int[side][side];\n        for (int i = 0; i < rows.length; i++) GRAPH[i/side][i%side] = Integer.parseInt(rows[i].trim());\n        System.out.println(new Solution().findCelebrity(side));\n    }\n}",
        "javascript": "const fs = require('fs');\nconst graph = JSON.parse(fs.readFileSync(0, 'utf-8').trim());\nconst n = graph.length;\nfunction knows(a, b) { return graph[a][b] === 1; }\n\nfunction findCelebrity(n) {\n    // User logic here\n    return -1;\n}\n\nconsole.log(findCelebrity(n));",
        "c": "#include <stdio.h>\n#include <stdbool.h>\n\nint GRAPH[200][200], N;\nbool knows(int a, int b) { return GRAPH[a][b] == 1; }\n\nint findCelebrity(int n) {\n    // User logic here\n    return -1;\n}\n\nint main() {\n    char line[10000];\n    N = 0;\n    while (fgets(line, sizeof(line), stdin)) {\n        int col = 0;\n        for (int i = 0; line[i]; i++) {\n            if (line[i] == '0' || line[i] == '1')\n                GRAPH[N][col++] = line[i] - '0';\n        }\n        if (col > 0) N++;\n    }\n    printf(\"%d\\n\", findCelebrity(N));\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,1,0],[0,1,0],[1,1,1]]", "expected_output": "1", "is_sample": True},
        {"input": "[[1,0,1],[1,1,0],[0,1,1]]", "expected_output": "-1", "is_sample": True},
        {"input": "[[1,1],[1,1]]", "expected_output": "-1", "is_sample": False},
        {"input": "[[1,0],[1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,1],[0,1]]", "expected_output": "0", "is_sample": False},
        {"input": "[[1,1,1],[0,1,0],[0,1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,0,0],[0,1,0],[0,0,1]]", "expected_output": "-1", "is_sample": False},
        # Stress cases
        {"input": "[[1 if i==j or j==50 else 0 for j in range(100)] for i in range(100)]", "expected_output": "50", "is_sample": False},
        {"input": "[[1 for j in range(100)] for i in range(100)]", "expected_output": "-1", "is_sample": False},
        {"input": "[[1 if i==j else 0 for j in range(100)] for i in range(100)]", "expected_output": "-1", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Greedy", "Graph"],
        "companyIndex": 0
    }

    output_path = "201-400/277_Find_the_Celebrity.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
