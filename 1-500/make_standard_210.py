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
        "python": "import sys\nimport json\nimport re\n\ndef findOrder(numCourses, prerequisites):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if input_data:\n        num_match = re.findall(r'-?\\d+', input_data[0])\n        numCourses = int(num_match[-1]) if num_match else 0\n        \n        all_nums = []\n        for line in input_data[1:]:\n            all_nums.extend(re.findall(r'-?\\d+', line))\n        \n        prerequisites = []\n        for i in range(0, len(all_nums) - 1, 2):\n            prerequisites.append([int(all_nums[i]), int(all_nums[i+1])])\n            \n        print(json.dumps(findOrder(numCourses, prerequisites)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nvector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        regex num_re(\"[-]?\\\\d+\");\n        smatch m;\n        int numCourses = 0;\n        if (regex_search(line, m, num_re)) numCourses = stoi(m.str());\n\n        vector<int> all_nums;\n        while (getline(cin, line)) {\n            auto words_begin = sregex_iterator(line.begin(), line.end(), num_re);\n            auto words_end = sregex_iterator();\n            for (sregex_iterator i = words_begin; i != words_end; ++i) all_nums.push_back(stoi(i->str()));\n        }\n\n        vector<vector<int>> prerequisites;\n        for (size_t i = 0; i + 1 < all_nums.size(); i += 2) {\n            prerequisites.push_back({all_nums[i], all_nums[i+1]});\n        }\n\n        vector<int> res = findOrder(numCourses, prerequisites);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \", \");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int[] findOrder(int numCourses, int[][] prerequisites) {\n        // User logic here\n        return new int[0];\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        if (line == null) return;\n\n        Matcher m = Pattern.compile(\"[-]?\\\\d+\").matcher(line);\n        int numCourses = 0;\n        if (m.find()) numCourses = Integer.parseInt(m.group());\n\n        List<Integer> allNums = new ArrayList<>();\n        while ((line = br.readLine()) != null) {\n            m = Pattern.compile(\"[-]?\\\\d+\").matcher(line);\n            while (m.find()) allNums.add(Integer.parseInt(m.group()));\n        }\n\n        int[][] prerequisites = new int[allNums.size() / 2][2];\n        for (int i = 0; i < allNums.size() - 1; i += 2) {\n            prerequisites[i / 2][0] = allNums.get(i);\n            prerequisites[i / 2][1] = allNums.get(i + 1);\n        }\n\n        int[] res = new Solution().findOrder(numCourses, prerequisites);\n        System.out.println(Arrays.toString(res));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findOrder(numCourses, prerequisites) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length > 0) {\n    const numCourses = parseInt(input[0].match(/[-]?\\d+/)?.[0] || 0);\n    const allNums = [];\n    for (let i = 1; i < input.length; i++) {\n        const matches = input[i].match(/[-]?\\d+/g);\n        if (matches) allNums.push(...matches.map(Number));\n    }\n    const prerequisites = [];\n    for (let i = 0; i < allNums.length - 1; i += 2) {\n        prerequisites.push([allNums[i], allNums[i+1]]);\n    }\n    const res = findOrder(numCourses, prerequisites);\n    console.log(JSON.stringify(res));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint* findOrder(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    static char line[1000000];\n    if (fgets(line, sizeof(line), stdin)) {\n        int numCourses = 0;\n        char* p = line; while (*p && !isdigit(*p) && *p != '-') p++;\n        if (*p) numCourses = strtol(p, &p, 10);\n\n        int* all_nums = malloc(200000 * sizeof(int));\n        int count = 0;\n        while (fgets(line, sizeof(line), stdin)) {\n            p = line;\n            while (*p) {\n                if (isdigit(*p) || *p == '-') all_nums[count++] = strtol(p, &p, 10);\n                else p++;\n            }\n        }\n\n        int prereqSize = count / 2;\n        int** prereqs = malloc(prereqSize * sizeof(int*));\n        int* colSizes = malloc(prereqSize * sizeof(int));\n        for (int i = 0; i < prereqSize; i++) {\n            prereqs[i] = malloc(2 * sizeof(int));\n            prereqs[i][0] = all_nums[i * 2];\n            prereqs[i][1] = all_nums[i * 2 + 1];\n            colSizes[i] = 2;\n        }\n\n        int returnSize = 0;\n        int* res = findOrder(numCourses, prereqs, prereqSize, colSizes, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], i == returnSize - 1 ? \"\" : \", \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
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
