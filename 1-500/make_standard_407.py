import json
import os

def generate_json():
    problem_id = 407
    title = "Trapping Rain Water II"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>407. Trapping Rain Water II</h3>
<p>Given an <code>m x n</code> integer matrix <code>heightMap</code> representing the elevation map where <code>heightMap[i][j]</code> is the height of the terrain at cell <code>(i, j)</code>, return <em>the volume of water it can trap after raining.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg" style="width: 361px; height: 321px;" />
<pre><strong>Input:</strong> heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> After the rain, water is trapped between the blocks.
Total trapped water volume is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg" style="width: 401px; height: 321px;" />
<pre><strong>Input:</strong> heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == heightMap.length</code></li>
	<li><code>n == heightMap[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heightMap[i][j] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An `m x n` heightMap matrix."
    output_format = "An integer volume."
    
    constraints = [
        "m, n <= 200",
        "Heights up to 20,000.",
        "Must be O(MN log(MN)) complexity."
    ]
    
    explanation = """To determine the trapped water in 3D, we must find the **minimum barrier height** surrounding each cell. Use a **Min-Heap** and a **BFS** starting from the boundary."""
    
    answer = """import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]: return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        res = 0
        level = 0
        while pq:
            h, x, y = heapq.heappop(pq)
            level = max(level, h)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if heightMap[nx][ny] < level:
                        res += level - heightMap[nx][ny]
                    heapq.heappush(pq, (heightMap[nx][ny], nx, ny))
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def trapRainWater(self, heightMap: list[list[int]]) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        height_map = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.trapRainWater(height_map)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <queue>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int trapRainWater(vector<vector<int>>& heightMap) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        vector<vector<int>> heightMap;\n        if (line.size() >= 2) line = line.substr(1, line.size() - 2);\n        size_t pos = 0;\n        while ((pos = line.find('[')) != string::npos) {\n            size_t end = line.find(']', pos);\n            string sub = line.substr(pos + 1, end - pos - 1);\n            stringstream ss(sub);\n            string val;\n            vector<int> row;\n            while (getline(ss, val, ',')) {\n                if (!val.empty()) row.push_back(stoi(val));\n            }\n            heightMap.push_back(row);\n            line.erase(0, end + 1);\n        }\n        Solution sol;\n        cout << sol.trapRainWater(heightMap) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int trapRainWater(int[][] heightMap) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().trim();\n            if (line.startsWith(\"[\")) line = line.substring(1, line.length() - 1);\n            List<int[]> matrix = new ArrayList<>();\n            int start = 0;\n            while ((start = line.indexOf(\"[\", start)) != -1) {\n                int end = line.indexOf(\"]\", start);\n                String[] parts = line.substring(start + 1, end).split(\",\");\n                int[] row = new int[parts.length];\n                for (int i = 0; i < parts.length; i++) row[i] = Integer.parseInt(parts[i].trim());\n                matrix.add(row);\n                start = end + 1;\n            }\n            int[][] heightMap = matrix.toArray(new int[0][]);\n            Solution sol = new Solution();\n            System.out.println(sol.trapRainWater(heightMap));\n        }\n    }\n}",
        "javascript": "var trapRainWater = function(heightMap) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    console.log(JSON.stringify(trapRainWater(JSON.parse(input))));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint trapRainWater(int** heightMap, int heightMapSize, int* heightMapColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]', "expected_output": "4", "is_sample": True},
        {"input": '[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]', "expected_output": "10", "is_sample": True},
        # 5 Diverse
        {"input": '[[1,1,1],[1,0,1],[1,1,1]]', "expected_output": "1", "is_sample": False},
        {"input": '[[5,5,5,5],[5,1,1,5],[5,5,5,5]]', "expected_output": "8", "is_sample": False},
        {"input": '[[1,2,1],[2,1,2],[1,2,1]]', "expected_output": "0", "is_sample": False},
        {"input": '[[1]]', "expected_output": "0", "is_sample": False},
        {"input": '[[2,2,2],[2,2,2],[2,2,2]]', "expected_output": "0", "is_sample": False},
        # 3 Stress
        {"input": '[[12,13,1,12],[13,4,13,12],[13,12,12,12],[12,13,12,12]]', "expected_output": "9", "is_sample": False},
        {"input": '[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]', "expected_output": "0", "is_sample": False},
        {"input": '[[9,9,9,9,9],[9,2,1,2,9],[9,9,9,9,9]]', "expected_output": "15", "is_sample": False}
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
        "topics": ["Array", "BFS", "Heap", "Matrix"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Trapping_Rain_Water_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
