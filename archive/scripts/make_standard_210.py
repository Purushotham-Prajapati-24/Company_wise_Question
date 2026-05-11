import json
import os

def generate_json():
    problem_id = 210
    title = "Course Schedule II"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>210. Course Schedule II</h3>
<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you must first take course <code>1</code>.</li>
</ul>

<p>Return <em>the ordering of courses you should take to finish all courses</em>. If there are many valid answers, return <strong>any</strong> of them. If it is impossible to finish all courses, return <strong>an empty array</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>Output:</strong> [0,2,1,3]
<strong>Explanation:</strong> There are a total of 4 courses to take. To take course 1 and 2 you should have finished course 0. To take course 3 you should have finished both courses 1 and 2. A correct course order is [0,1,2,3]. Another correct order is [0,2,1,3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numCourses = 1, prerequisites = []
<strong>Output:</strong> [0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1)</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are <strong>distinct</strong>.</li>
</ul>"""

    input_format = "Line 1: numCourses. Line 2: flat space-separated integers for prerequisites."
    output_format = "Space-separated integers for the topological order, or empty string if impossible."
    
    constraints = [
        "numCourses: [1, 2000]",
        "prerequisites count up to numCourses * (numCourses - 1)",
        "O(V + E) time complexity expected.",
        "Return any valid ordering."
    ]
    
    explanation = """To find a valid course ordering (topological sort of a directed acyclic graph):
1. **Kahn's Algorithm (BFS)**:
   - Represent courses as nodes and prerequisites as directed edges (b -> a).
2. **Algorithm Steps**:
   - Construct an **adjacency list** and an **in-degree** array.
   - Enqueue all nodes with in-degree 0 into a queue.
   - Maintain a list `order` to store the topological sequence.
   - While the queue is not empty:
     - Dequeue a course `curr`.
     - Append `curr` to `order`.
     - For each neighbor `next` of `curr`:
       - Decrement its in-degree.
       - If its in-degree reaches 0, enqueue it.
3. **Cycle Detection**:
   - If the final `order` list contains `numCourses` elements, it's a valid topological sort.
   - If not, a cycle exists, and finishing all courses is impossible. Return an empty list.
4. **Complexity**:
   - Time Complexity: O(V + E) where V is `numCourses` and E is the number of `prerequisites`.
   - Space Complexity: O(V + E) to store the graph."""
    
    answer = """import collections

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = collections.defaultdict(list)
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
        
    queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return order if len(order) == numCourses else []"""

    boilerplate = {
        "python": "import sys\n\ndef findOrder(numCourses, prerequisites):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        n_courses = int(lines[0])\n        if len(lines) > 1:\n            p_flat = list(map(int, lines[1].split()))\n            prereqs = [p_flat[i:i+2] for i in range(0, len(p_flat), 2)]\n        else:\n            prereqs = []\n        res = findOrder(n_courses, prereqs)\n        print(\" \".join(map(str, res)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nvector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line1, line2;\n    if (getline(cin, line1)) {\n        int numCourses = stoi(line1);\n        vector<vector<int>> prerequisites;\n        if (getline(cin, line2)) {\n            stringstream ss(line2);\n            int a, b;\n            while (ss >> a >> b) {\n                prerequisites.push_back({a, b});\n            }\n        }\n        vector<int> res = findOrder(numCourses, prerequisites);\n        for (int i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \" \");\n        }\n        cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        // User logic\n        return new int[0];\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null) {\n            int numCourses = Integer.parseInt(line1.trim());\n            List<int[]> list = new ArrayList<>();\n            if (line2 != null && !line2.trim().isEmpty()) {\n                String[] parts = line2.trim().split(\"\\\\s+\");\n                for (int i = 0; i < parts.length; i += 2) {\n                    list.add(new int[]{Integer.parseInt(parts[i]), Integer.parseInt(parts[i+1])});\n                }\n            }\n            int[][] prereqs = list.toArray(new int[list.size()][]);\n            int[] res = new Solution().findOrder(numCourses, prereqs);\n            StringBuilder sb = new StringBuilder();\n            for (int i = 0; i < res.length; i++) {\n                sb.append(res[i]).append(i == res.length - 1 ? \"\" : \" \");\n            }\n            System.out.println(sb.toString().trim());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findOrder(numCourses, prerequisites) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 1) {\n    let numCourses = parseInt(input[0].trim());\n    let prerequisites = [];\n    if (input.length >= 2 && input[1].trim() !== '') {\n        let parts = input[1].trim().split(/\\\\s+/).map(Number);\n        for (let i = 0; i < parts.length; i += 2) {\n            prerequisites.push([parts[i], parts[i+1]]);\n        }\n    }\n    let res = findOrder(numCourses, prerequisites);\n    console.log(res.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\nint* findOrder(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize, int* returnSize) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int numCourses;\n    if (scanf(\"%d\", &numCourses) == 1) {\n        int capacity = 1000;\n        int** prereqs = (int**)malloc(capacity * sizeof(int*));\n        int size = 0;\n        int a, b;\n        while (scanf(\"%d %d\", &a, &b) == 2) {\n            if (size >= capacity) {\n                capacity *= 2;\n                prereqs = (int**)realloc(prereqs, capacity * sizeof(int*));\n            }\n            prereqs[size] = (int*)malloc(2 * sizeof(int));\n            prereqs[size][0] = a;\n            prereqs[size][1] = b;\n            size++;\n        }\n        int* colSizes = (int*)malloc(size * sizeof(int));\n        for (int i = 0; i < size; i++) colSizes[i] = 2;\n        int returnSize;\n        int* res = findOrder(numCourses, prereqs, size, colSizes, &returnSize);\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], i == returnSize - 1 ? \"\" : \" \");\n        }\n        printf(\"\\n\");\n        for (int i = 0; i < size; i++) free(prereqs[i]);\n        free(prereqs);\n        free(colSizes);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2\\n1 0", "expected_output": "0 1", "is_sample": True},
        {"input": "4\\n1 0 2 0 3 1 3 2", "expected_output": "0 1 2 3", "is_sample": True},
        {"input": "1\\n", "expected_output": "0", "is_sample": True},
        {"input": "2\\n1 0 0 1", "expected_output": "", "is_sample": False},
        {"input": "3\\n1 0 2 1", "expected_output": "0 1 2", "is_sample": False},
        {"input": "3\\n1 0 0 1", "expected_output": "", "is_sample": False},
        {"input": "4\\n1 0 2 1 3 2 0 3", "expected_output": "", "is_sample": False},
        # Stress cases
        {"input": "2000\\n", "expected_output": " ".join([str(i) for i in range(2000)]), "is_sample": False},
        {"input": "5\\n1 0 2 1 3 2 4 3", "expected_output": "0 1 2 3 4", "is_sample": False},
        {"input": "5\\n1 0 2 0 3 1 3 2 4 3", "expected_output": "0 1 2 3 4", "is_sample": False}
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

    output_path = "1-200/210_Course_Schedule_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
