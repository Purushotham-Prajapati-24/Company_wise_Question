import json
import os

def generate_json():
    problem_id = 444
    title = "Sequence Reconstruction"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>444. Sequence Reconstruction</h3>
<p>You are given an integer array <code>nums</code> of length <code>n</code> where <code>nums</code> is a permutation of the integers in the range <code>[1, n]</code>. You are also given a 2D integer array <code>sequences</code> where <code>sequences[i]</code> is a subsequence of <code>nums</code>.</p>

<p>Check if <code>nums</code> is the <strong>unique shortest common supersequence</strong> of all the sequences in <code>sequences</code>.</p>

<p>A <strong>common supersequence</strong> of all the sequences is an array that contains all of the sequences as subsequences.</p>
<ul>
	<li>The <strong>shortest</strong> common supersequence is a common supersequence with the minimum possible length.</li>
	<li>There could be multiple shortest common supersequences for the given <code>sequences</code>.</li>
</ul>

<p>For example, for <code>sequences = [[1,2],[1,3]]</code>, there are two shortest common supersequences: <code>[1,2,3]</code> and <code>[1,3,2]</code>.</p>
<p>For <code>sequences = [[1,2],[1,3],[2,3]]</code>, the only shortest common supersequence is <code>[1,2,3]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3], sequences = [[1,2],[1,3]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are two possible shortest common supersequences: [1,2,3] and [1,3,2].
The sequences [1,2] and [1,3] are subsequences of both of them.
Since nums is not the unique shortest common supersequence, return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3], sequences = [[1,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The shortest common supersequence is [1,2].
The sequence [1,2] is a subsequence of [1,2].
Since nums is not the shortest common supersequence, return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The sequences [1,2], [1,3], and [2,3] are subsequences of [1,2,3].
[1,2,3] is the only shortest common supersequence.
Since nums is the unique shortest common supersequence, return true.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is a permutation of <code>[1, n]</code>.</li>
	<li><code>1 &lt;= sequences.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sequences[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sum(sequences[i].length) &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sequences[i][j] &lt;= n</code></li>
	<li>All the vectors of <code>sequences[i]</code> are unique.</li>
</ul>"""

    input_format = "An integer array nums and a 2D integer array sequences."
    output_format = "A boolean representing if nums is the unique shortest supersequence."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """from collections import deque

def sequenceReconstruction(nums, sequences):
    n = len(nums)
    adj = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}
    
    for seq in sequences:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i+1]
            adj[u].append(v)
            in_degree[v] += 1
            
    queue = deque([i for i in in_degree if in_degree[i] == 0])
    res = []
    
    while queue:
        if len(queue) > 1:
            return False
            
        u = queue.popleft()
        res.append(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    return res == nums"""

    boilerplate = {
        "python": "import sys\n\ndef sequenceReconstruction(nums, sequences):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    nums = input_data[0].strip() if len(input_data) > 0 else \"\"\n    sequences = input_data[1].strip() if len(input_data) > 1 else \"\"\n    print(sequenceReconstruction(nums, sequences))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nint sequenceReconstruction(string nums, string sequences) {\n    // User logic\n    return 0;\n}\n\nint main() {\n    string nums; cin >> nums;\n    string sequences; cin >> sequences;\n    cout << sequenceReconstruction(nums, sequences) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); System.out.println(\"0\"); } }",
        "javascript": "const fs = require('fs'); console.log(\"0\");",
        "c": "#include <stdio.h>\nint main() { printf(\"0\\n\"); return 0; }"
}

    test_cases = [{"input": "[1,2,3]\\n[[1,2],[1,3]]", "expected_output": "false", "is_sample": True},
        {"input": "[1,2,3]\\n[[1,2]]", "expected_output": "false", "is_sample": True},
        {"input": "[1,2,3]\\n[[1,2],[1,3],[2,3]]", "expected_output": "true", "is_sample": True},
        {"input": "[1,2,3,4]\\n[[1,2],[2,3],[3,4]]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2,4,3]\\n[[1,2],[2,3],[3,4]]", "expected_output": "false", "is_sample": False},
        {"input": "[1]\\n[[1]]", "expected_output": "true", "is_sample": False},
        {"input": "[1,2]\\n[[1,2],[1,2]]", "expected_output": "true", "is_sample": False},
        # Stress tests]

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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
