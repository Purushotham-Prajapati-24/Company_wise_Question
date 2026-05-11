import json
import os

def generate_json():
    problem_id = 207
    title = "Course Schedule"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>207. Course Schedule</h3>
<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you must first take course <code>1</code>.</li>
</ul>

<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li>All the pairs <code>prerequisites[i]</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "Line 1: numCourses. Line 2: flat space-separated integers for prerequisites (e.g., [1,0], [0,1] -> 1 0 0 1)."
    output_format = "true if all courses can be finished, false otherwise."
    
    constraints = [
        "numCourses: [1, 2000]",
        "prerequisites: [0, 5000]",
        "O(V+E) time complexity expected.",
        "Cycle detection in directed graph required."
    ]
    
    explanation = """To determine if all courses can be finished (cycle detection in a directed graph):
1. **Kahn's Algorithm (BFS Topological Sort)**:
   - Represent the courses as nodes in a graph.
   - For each prerequisite `[a, b]`, add a directed edge from `b` to `a` (b -> a).
2. **Algorithm Steps**:
   - Calculate the **in-degree** of each node (number of prerequisites).
   - Add all nodes with an in-degree of 0 to a queue.
   - While the queue is not empty:
     - Dequeue a course `curr`.
     - Increment the count of courses that can be finished.
     - For each neighbor `next` of `curr`:
       - Decrement its in-degree.
       - If its in-degree becomes 0, enqueue it.
3. **Condition**:
   - If the total count of finished courses equals `numCourses`, return `true` (no cycles). Otherwise, return `false`.
4. **Complexity**:
   - Time Complexity: O(V + E) where V is `numCourses` and E is the number of `prerequisites`.
   - Space Complexity: O(V + E) to store the adjacency list."""
    
    answer = """import collections

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # Build adjacency list and in-degree map
    adj = collections.defaultdict(list)
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
        
    # Queue for nodes with 0 in-degree
    queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    
    while queue:
        curr = queue.popleft()
        count += 1
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return count == numCourses"""

    # Boilerplate with standard I/O for 5 languages
    boilerplate = {
        "python": "import sys\n\ndef canFinish(numCourses, prerequisites):\n    # User logic here\n    return False\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        n_courses = int(lines[0])\n        if len(lines) > 1:\n            p_flat = list(map(int, lines[1].split()))\n            prereqs = [p_flat[i:i+2] for i in range(0, len(p_flat), 2)]\n        else:\n            prereqs = []\n        print(\"true\" if canFinish(n_courses, prereqs) else \"false\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nbool canFinish(int numCourses, vector<vector<int>>& prerequisites) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1)) {\n        int numCourses = stoi(line1);\n        vector<vector<int>> prerequisites;\n        if (getline(cin, line2)) {\n            stringstream ss(line2);\n            int a, b;\n            while (ss >> a >> b) {\n                prerequisites.push_back({a, b});\n            }\n        }\n        cout << (canFinish(numCourses, prerequisites) ? \"true\" : \"false\") << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public boolean canFinish(int numCourses, int[][] prerequisites) {\n        // User logic here\n        return false;\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null) {\n            int numCourses = Integer.parseInt(line1.trim());\n            List<int[]> list = new ArrayList<>();\n            if (line2 != null && !line2.trim().isEmpty()) {\n                String[] parts = line2.trim().split(\"\\\\s+\");\n                for (int i = 0; i < parts.length; i += 2) {\n                    list.add(new int[]{Integer.parseInt(parts[i]), Integer.parseInt(parts[i+1])});\n                }\n            }\n            int[][] prereqs = list.toArray(new int[list.size()][]);\n            System.out.println(new Solution().canFinish(numCourses, prereqs) ? \"true\" : \"false\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction canFinish(numCourses, prerequisites) {\n    // User logic here\n    return false;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 1) {\n    let numCourses = parseInt(input[0].trim());\n    let prerequisites = [];\n    if (input.length >= 2 && input[1].trim() !== '') {\n        let parts = input[1].trim().split(/\\\\s+/).map(Number);\n        for (let i = 0; i < parts.length; i += 2) {\n            prerequisites.push([parts[i], parts[i+1]]);\n        }\n    }\n    console.log(canFinish(numCourses, prerequisites) ? \"true\" : \"false\");\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\nbool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {\n    // User logic here\n    return false;\n}\n\nint main() {\n    int numCourses;\n    if (scanf(\"%d\", &numCourses) == 1) {\n        int capacity = 1000;\n        int** prereqs = (int**)malloc(capacity * sizeof(int*));\n        int size = 0;\n        int a, b;\n        while (scanf(\"%d %d\", &a, &b) == 2) {\n            if (size >= capacity) {\n                capacity *= 2;\n                prereqs = (int**)realloc(prereqs, capacity * sizeof(int*));\n            }\n            prereqs[size] = (int*)malloc(2 * sizeof(int));\n            prereqs[size][0] = a;\n            prereqs[size][1] = b;\n            size++;\n        }\n        int* colSizes = (int*)malloc(size * sizeof(int));\n        for (int i = 0; i < size; i++) colSizes[i] = 2;\n        printf(\"%s\\n\", canFinish(numCourses, prereqs, size, colSizes) ? \"true\" : \"false\");\n        for (int i = 0; i < size; i++) free(prereqs[i]);\n        free(prereqs);\n        free(colSizes);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2\\n1 0", "expected_output": "true", "is_sample": True},
        {"input": "2\\n1 0 0 1", "expected_output": "false", "is_sample": True},
        {"input": "1\\n", "expected_output": "true", "is_sample": True},
        {"input": "3\\n1 0 2 1", "expected_output": "true", "is_sample": False},
        {"input": "3\\n1 0 0 1", "expected_output": "false", "is_sample": False},
        {"input": "4\\n1 0 2 1 3 2", "expected_output": "true", "is_sample": False},
        {"input": "4\\n1 0 2 0 3 1 3 2", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "2000\\n", "expected_output": "true", "is_sample": False},
        {"input": "3\\n0 1 1 2 2 0", "expected_output": "false", "is_sample": False},
        {"input": "5\\n1 0 2 1 3 2 4 3 0 4", "expected_output": "false", "is_sample": False}
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
        "topics": ["Depth-First Search", "Breadth-First Search", "Graph", "Topological Sort"],
        "companyIndex": 0
    }

    output_path = "1-200/207_Course_Schedule.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
