import json
import os

def generate_json():
    problem_id = 417
    title = "Pacific Atlantic Water Flow"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>417. Pacific Atlantic Water Flow</h3>
<p>There is an <code>m x n</code> rectangular island that borders both the <strong>Pacific Ocean</strong> and <strong>Atlantic Ocean</strong>. The <strong>Pacific Ocean</strong> touches the island's left and top edges, and the <strong>Atlantic Ocean</strong> touches the island's right and bottom edges.</p>

<p>The island is partitioned into a grid of square cells. You are given an <code>m x n</code> integer matrix <code>heights</code> where <code>heights[r][c]</code> represents the <strong>height above sea level</strong> of the cell at coordinate <code>(r, c)</code>.</p>

<p>The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is <strong>less than or equal to</strong> the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.</p>

<p>Return <em>a <strong>2D list</strong> of grid coordinates </em><code>result</code><em> where </em><code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code><em> denotes that rain water can flow from cell </em><code>(r<sub>i</sub>, c<sub>i</sub>)</code><em> to <strong>both</strong> the Pacific and Atlantic oceans</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" style="width: 400px; height: 400px;" />
<pre><strong>Input:</strong> heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
<strong>Output:</strong> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
<strong>Explanation:</strong> The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
&nbsp;      [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
&nbsp;      [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
&nbsp;      [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
&nbsp;      [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
&nbsp;      [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
&nbsp;      [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
&nbsp;      [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> heights = [[1]]
<strong>Output:</strong> [[0,0]]
<strong>Explanation:</strong> The water can flow from the only cell to the Pacific and Atlantic oceans.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == heights.length</code></li>
	<li><code>n == heights[r].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heights[r][c] &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An `m x n` heights matrix."
    output_format = "A list of coordinates `[r, c]`."
    
    constraints = [
        "1 <= m, n <= 200",
        "Heights up to 100,000.",
        "Must be O(MN) complexity."
    ]
    
    explanation = """To find the cells that can flow to both oceans, it's more efficient to work **backwards** from the oceans to the island.

### Key Observation:
- Water flows from high to low.
- To find which cells can reach an ocean, we start from the boundary cells of that ocean and see where water can "climb up" (neighbor height $\ge$ current height).

### Algorithm Steps:
1. **Initialize**:
   - `pacific_reachable` and `atlantic_reachable` sets/grids to store which cells can reach each ocean.
2. **Backward DFS/BFS**:
   - Start a DFS/BFS from all cells on the **Top** and **Left** edges (Pacific). Mark all reachable cells in `pacific_reachable`.
   - Start a DFS/BFS from all cells on the **Bottom** and **Right** edges (Atlantic). Mark all reachable cells in `atlantic_reachable`.
   - Only move to a neighbor if `neighbor_height >= current_height`.
3. **Intersection**:
   - The result consists of all coordinates `(r, c)` that are present in **both** sets.

### Complexity Analysis:
- **Time Complexity**: $O(M \cdot N)$, as each cell is visited at most twice (once for each ocean).
- **Space Complexity**: $O(M \cdot N)$ to store the reachability information."""
    
    answer = """class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        
        pac = [[False] * m for _ in range(n)]
        atl = [[False] * m for _ in range(n)]
        
        def dfs(r, c, visited, prev_h):
            if r < 0 or c < 0 or r >= n or c >= m or visited[r][c] or heights[r][c] < prev_h:
                return
            
            visited[r][c] = True
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # Start DFS for Pacific
        for c in range(m):
            dfs(0, c, pac, heights[0][c])
        for r in range(n):
            dfs(r, 0, pac, heights[r][0])
            
        # Start DFS for Atlantic
        for c in range(m):
            dfs(n-1, c, atl, heights[n-1][c])
        for r in range(n):
            dfs(r, m-1, atl, heights[r][m-1])
            
        res = []
        for r in range(n):
            for c in range(m):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
                    
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        heights = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.pacificAtlantic(heights)))",
        "cpp": "class Solution {\npublic:\n    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {\n        // Your logic here\n        return {};\n    }\n};",
        "java": "public class Solution {\n    public List<List<Integer>> pacificAtlantic(int[][] heights) {\n        // Your logic here\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number[][]} heights\n * @return {number[][]}\n */\nvar pacificAtlantic = function(heights) {\n    // Your logic here\n};",
        "c": "int** pacificAtlantic(int** heights, int heightsSize, int* heightsColSize, int* returnSize, int** returnColumnSizes) {\n    // Your logic here\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]", "expected_output": "[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]", "is_sample": True},
        {"input": "[[1]]", "expected_output": "[[0,0]]", "is_sample": True},
        {"input": "[[10,10,10],[10,1,10],[10,10,10]]", "expected_output": "[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]", "is_sample": False},
        {"input": "[[1,2],[3,4]]", "expected_output": "[[0,1],[1,0],[1,1]]", "is_sample": False},
        {"input": "[[10,10],[10,10]]", "expected_output": "[[0,0],[0,1],[1,0],[1,1]]", "is_sample": False},
        # Stress cases
        {"input": "[[20000]*200 for _ in range(200)]", "expected_output": "[[r, c] for r in range(200) for c in range(200)]", "is_sample": False},
        {"input": "[[j+i*200 for j in range(200)] for i in range(200)]", "expected_output": "...", "is_sample": False},
        {"input": "[[10**5 if (i+j)%2 == 0 else 0 for j in range(200)] for i in range(200)]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Depth-First Search", "Breadth-First Search", "Matrix"],
        "companyIndex": 1
    }

    output_path = "301-500/417_Pacific_Atlantic_Water_Flow.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
