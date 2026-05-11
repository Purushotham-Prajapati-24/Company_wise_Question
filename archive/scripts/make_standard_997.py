import json
import os

def generate_json():
    problem_id = 997
    title = "Find the Town Judge"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>997. Find the Town Judge</h3>
<p>In a town, there are <code>n</code> people labeled from <code>1</code> to <code>n</code>. There is a rumor that one of these people is secretly the town judge.</p>

<p>If the town judge exists, then:</p>

<ol>
	<li>The town judge trusts nobody.</li>
	<li>Everybody (except for the town judge) trusts the town judge.</li>
	<li>There is exactly one person that satisfies properties 1 and 2.</li>
</ol>

<p>You are given an array <code>trust</code> where <code>trust[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> representing that the person labeled <code>a<sub>i</sub></code> trusts the person labeled <code>b<sub>i</sub></code>. If a trust relationship does not exist in <code>trust</code> array, then such a trust relationship does not exist.</p>

<p>Return <em>the label of the town judge if the town judge exists and can be identified, or return </em><code>-1</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> n = 2, trust = [[1,2]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> n = 3, trust = [[1,3],[2,3]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> n = 3, trust = [[1,3],[2,3],[3,1]]
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= trust.length &lt;= 10<sup>4</sup></code></li>
	<li><code>trust[i].length == 2</code></li>
	<li>All the pairs of <code>trust</code> are <strong>unique</strong>.</li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n</code></li>
</ul>"""

    input_format = "Line 1: integer n. Line 2: space-separated pairs ai bi representation of trust."
    output_format = "An integer representing the town judge label, or -1 if not found."
    
    constraints = [
        "1 <= n <= 1000",
        "0 <= trust.length <= 10,000",
        "Unique pairs.",
        "O(E + N) time complexity.",
        "O(N) extra space."
    ]
    
    explanation = """To find the town judge efficiently:
1. **The Insight (In-degree vs Out-degree)**:
   - Each person can be represented as a node in a graph.
   - If person `a` trusts person `b`, there is an edge from `a` to `b`.
   - The town judge must have an in-degree of `n-1` (everyone trusts them) and an out-degree of `0` (they trust no one).
2. **Algorithm Strategy (Trust Scores)**:
   - Create a single array `trust_scores` of size `n + 1`.
   - Iterate through every trust pair `[a, b]`:
     - Decrement `trust_scores[a]` (out-degree).
     - Increment `trust_scores[b]` (in-degree).
3. **Conclusion**:
   - Iterate through people from `1` to `n`.
   - If `trust_scores[i] == n - 1`, person `i` is the judge.
   - If no such person is found or if more than one person could satisfy it (though constraints guarantee at most one), return -1.
4. **Complexity**:
   - Time Complexity: O(E + N) where E is the number of trust relationships and N is the number of people.
   - Space Complexity: O(N) to store the scores."""
    
    answer = """def findJudge(n: int, trust: list[list[int]]) -> int:
    if n == 1 and not trust: return 1
    
    scores = [0] * (n + 1)
    for a, b in trust:
        scores[a] -= 1
        scores[b] += 1
        
    for i in range(1, n + 1):
        if scores[i] == n - 1:
            return i
            
    return -1"""

    boilerplate = {
        "python": "import sys\n\ndef findJudge(n, trust):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if lines:\n        n = int(lines[0].strip())\n        pairs = []\n        if len(lines) > 1:\n            raw = list(map(int, lines[1].strip().split()))\n            for i in range(0, len(raw), 2):\n                pairs.append([raw[i], raw[i+1]])\n        print(findJudge(n, pairs))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nint findJudge(int n, vector<vector<int>>& trust) {\n    // User logic\n    return -1;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int findJudge(int n, int[][] trust) {\n        // User logic\n        return -1;\n    }\n}",
        "javascript": "function findJudge(n, trust) {\n    // User logic\n}",
        "c": "int findJudge(int n, int** trust, int trustSize, int* trustColSize) {\n    // User logic\n    return -1;\n}"
    }

    test_cases = [
        {"input": "2\\n1 2", "expected_output": "2", "is_sample": True},
        {"input": "3\\n1 3 2 3", "expected_output": "3", "is_sample": True},
        {"input": "3\\n1 3 2 3 3 1", "expected_output": "-1", "is_sample": True},
        {"input": "1\\n", "expected_output": "1", "is_sample": False},
        {"input": "2\\n", "expected_output": "-1", "is_sample": False},
        {"input": "3\\n1 2 2 3", "expected_output": "-1", "is_sample": False},
        {"input": "4\\n1 3 1 4 2 3 2 4 4 3", "expected_output": "3", "is_sample": False},
        {"input": "4\\n1 2 1 3 2 1 2 3 4 1 4 2 4 3", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": "1000\\n" + " ".join([f"{i} 1000" for i in range(1, 1000)]), "expected_output": "1000", "is_sample": False},
        {"input": "1000\\n" + " ".join([f"{i} {i+1 if i < 1000 else 1}" for i in range(1, 1001)]), "expected_output": "-1", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Graph"],
        "companyIndex": 0
    }

    output_path = "801-1000/997_Find_the_Town_Judge.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
