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
        "python": """import sys
import json

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        # User Logic Here
        pass

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        height_map = json.loads(raw_input)
        sol = Solution()
        print(json.dumps(sol.trapRainWater(height_map)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<vector<int>> heightMap;
        if (line.size() >= 2) line = line.substr(1, line.size() - 2);
        size_t pos = 0;
        while ((pos = line.find('[')) != string::npos) {
            size_t end = line.find(']', pos);
            string sub = line.substr(pos + 1, end - pos - 1);
            stringstream ss(sub);
            string val;
            vector<int> row;
            while (getline(ss, val, ',')) {
                if (!val.empty()) row.push_back(stoi(val));
            }
            heightMap.push_back(row);
            line.erase(0, end + 1);
        }
        Solution sol;
        cout << sol.trapRainWater(heightMap) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int trapRainWater(int[][] heightMap) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.startsWith("[")) line = line.substring(1, line.length() - 1);
            List<int[]> matrix = new ArrayList<>();
            int start = 0;
            while ((start = line.indexOf("[", start)) != -1) {
                int end = line.indexOf("]", start);
                String[] parts = line.substring(start + 1, end).split(",");
                int[] row = new int[parts.length];
                for (int i = 0; i < parts.length; i++) row[i] = Integer.parseInt(parts[i].trim());
                matrix.add(row);
                start = end + 1;
            }
            int[][] heightMap = matrix.toArray(new int[0][]);
            Solution sol = new Solution();
            System.out.println(sol.trapRainWater(heightMap));
        }
    }
}""",
        "javascript": """var trapRainWater = function(heightMap) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(trapRainWater(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int trapRainWater(int** heightMap, int heightMapSize, int* heightMapColSize) {
    // User Logic Here
    return 0;
}

int main() {
    // Basic harness for matrix
    return 0;
}"""
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
