import json
import os
import heapq

def generate_json():
    problem_id = 218
    title = "The Skyline Problem"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>218. The Skyline Problem</h3>
<p>A city's <strong>skyline</strong> is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return <em>the <strong>skyline</strong> formed by these buildings collectively</em>.</p>

<p>The geometric information of each building is given in the array <code>buildings</code> where <code>buildings[i] = [left<sub>i</sub>, right<sub>i</sub>, height<sub>i</sub>]</code>:</p>

<ul>
	<li><code>left<sub>i</sub></code> is the x coordinate of the left edge of the <code>i<sup>th</sup></code> building.</li>
	<li><code>right<sub>i</sub></code> is the x coordinate of the right edge of the <code>i<sup>th</sup></code> building.</li>
	<li><code>height<sub>i</sub></code> is the height of the <code>i<sup>th</sup></code> building.</li>
</ul>

<p>You may assume all buildings are perfect rectangles grounded on a perfectly flat surface at height 0.</p>

<p>The <strong>skyline</strong> should be represented as a list of "key points" sorted by their x-coordinate in the form <code>[[x<sub>1</sub>,y<sub>1</sub>],[x<sub>2</sub>,y<sub>2</sub>],...]</code>. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and marks the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.</p>

<p><b>Note:</b> There must be no consecutive horizontal lines of equal height in the output skyline. For instance, <code>[[2 3], [4 5], [7 5], [11 5], [12 7]]</code> is not acceptable; the three lines of height 5 should be merged into one in the final output as: <code>[[2 3], [4 5], [12 7]]</code></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/merged.jpg" style="width: 800px; height: 331px;" />
<pre><strong>Input:</strong> buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
<strong>Output:</strong> [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
<strong>Explanation:</strong>
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> buildings = [[0,2,3],[2,5,3]]
<strong>Output:</strong> [[0,3],[5,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= buildings.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= left<sub>i</sub> &lt; right<sub>i</sub> &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= height<sub>i</sub> &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>buildings</code> is sorted by <code>left<sub>i</sub></code> in non-decreasing order.</li>
</ul>"""

    input_format = "A stringified 2D array: 'buildings'."
    output_format = "A stringified 2D array of key points [[x, y], ...]."
    
    constraints = [
        "1 <= buildings.length <= 10,000",
        "0 <= left < right <= 2^31 - 1",
        "1 <= height <= 2^31 - 1",
        "Time complexity: O(N log N) required."
    ]
    
    explanation = """To solve the Skyline Problem efficiently:
1. **Event Points**: For each building `[L, R, H]`, create two events: `(L, -H)` representing the start, and `(R, H)` representing the end.
2. **Sorting**: Sort the events by X. If X is the same:
   - If both are stars, process higher height first (higher `H` is lower `-H`).
   - If both are ends, process lower height first.
   - If one is start and one is end, process start first.
3. **Max-Heap**: Use a heap to track active building heights. Initially, push `0` into the heap.
4. **Sweep Line**: iterate through events:
   - If start (height < 0): push `-height` into heap.
   - If end (height > 0): remove `height` from heap (using a lazy removal or hash map).
   - If the current max height in the heap changes from the previous max, record the key point `[X, current_max]`.
5. **Complexity**: O(N log N) time and O(N) space."""
    
    answer = """import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # events stores (x, h) pairs. 
        # h < 0 for start, h > 0 for end.
        events = []
        for L, R, H in buildings:
            events.append((L, -H))
            events.append((R, H))
        
        # Sort by x, then by h
        events.sort()
        
        res = [[0, 0]]
        # max_heap to store heights, negative for min_heap behavior
        max_heap = [0]
        # lazy removal: heights to remove
        pending_removals = {}
        
        for x, h in events:
            if h < 0:
                heapq.heappush(max_heap, h)
            else:
                pending_removals[h] = pending_removals.get(h, 0) + 1
            
            # Remove pending heights from top of heap
            while -max_heap[0] in pending_removals and pending_removals[-max_heap[0]] > 0:
                h_to_rem = -heapq.heappop(max_heap)
                pending_removals[h_to_rem] -= 1
            
            curr_max = -max_heap[0]
            if res[-1][1] != curr_max:
                res.append([x, curr_max])
        
        return res[1:]"""

    boilerplate = {
        "python": "import sys\n\ndef getSkyline(buildings):\n    # User logic here\n    return []\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        n = int(lines[0])\n        if len(lines) > 1:\n            flat = list(map(int, lines[1].split()))\n            buildings = [flat[i:i+3] for i in range(0, len(flat), 3)]\n        else:\n            buildings = []\n        res = getSkyline(buildings)\n        for p in res:\n            print(f\"{p[0]} {p[1]}\", end=\" \")\n        print()",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<int>> getSkyline(vector<vector<int>>& buildings) {\n    // User logic\n    return {};\n}\n\nint main() {\n    int n;\n    if (cin >> n) {\n        string line;\n        getline(cin, line); // consume newline\n        if (getline(cin, line)) {\n            stringstream ss(line);\n            vector<vector<int>> buildings;\n            int l, r, h;\n            while (ss >> l >> r >> h) {\n                buildings.push_back({l, r, h});\n            }\n            vector<vector<int>> res = getSkyline(buildings);\n            for (int i = 0; i < res.size(); i++) {\n                cout << res[i][0] << \" \" << res[i][1] << (i == res.size() - 1 ? \"\" : \" \");\n            }\n            cout << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\n\npublic class Solution {\n    public List<List<Integer>> getSkyline(int[][] buildings) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line1 = br.readLine();\n        String line2 = br.readLine();\n        if (line1 != null) {\n            int n = Integer.parseInt(line1.trim());\n            int[][] buildings = new int[n][3];\n            if (line2 != null && !line2.trim().isEmpty()) {\n                String[] parts = line2.trim().split(\"\\\\s+\");\n                for (int i = 0; i < n; i++) {\n                    buildings[i][0] = Integer.parseInt(parts[i*3]);\n                    buildings[i][1] = Integer.parseInt(parts[i*3 + 1]);\n                    buildings[i][2] = Integer.parseInt(parts[i*3 + 2]);\n                }\n            }\n            List<List<Integer>> res = new Solution().getSkyline(buildings);\n            StringBuilder sb = new StringBuilder();\n            for (int i = 0; i < res.size(); i++) {\n                sb.append(res.get(i).get(0)).append(\" \").append(res.get(i).get(1)).append(i == res.size() - 1 ? \"\" : \" \");\n            }\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction getSkyline(buildings) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 1) {\n    const n = parseInt(input[0].trim());\n    let buildings = [];\n    if (input.length >= 2 && input[1].trim() !== '') {\n        const flat = input[1].trim().split(/\\s+/).map(Number);\n        for (int i = 0; i < n; i++) {\n            buildings.push([flat[i*3], flat[i*3+1], flat[i*3+2]]);\n        }\n    }\n    let res = getSkyline(buildings);\n    let out = [];\n    res.forEach(p => out.push(p[0], p[1]));\n    console.log(out.join(' '));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint** getSkyline(int** buildings, int buildingsSize, int* buildingsColSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    int n;\n    if (scanf(\"%d\", &n) == 1) {\n        int** buildings = (int**)malloc(n * sizeof(int*));\n        int* colSizes = (int*)malloc(n * sizeof(int));\n        for (int i = 0; i < n; i++) {\n            buildings[i] = (int*)malloc(3 * sizeof(int));\n            scanf(\"%d %d %d\", &buildings[i][0], &buildings[i][1], &buildings[i][2]);\n            colSizes[i] = 3;\n        }\n        int returnSize;\n        int* returnColSizes;\n        int** res = getSkyline(buildings, n, colSizes, &returnSize, &returnColSizes);\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d %d%s\", res[i][0], res[i][1], i == returnSize - 1 ? \"\" : \" \");\n        }\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    def _format_input(buildings):
        return f"{len(buildings)}\n" + " ".join(f"{b[0]} {b[1]} {b[2]}" for b in buildings)
    
    def _format_output(res):
        return " ".join(f"{p[0]} {p[1]}" for p in res)

    test_cases = [
        {"input": _format_input([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]), "expected_output": "2 10 3 15 7 12 12 0 15 10 20 8 24 0", "is_sample": True},
        {"input": _format_input([[0,2,3],[2,5,3]]), "expected_output": "0 3 5 0", "is_sample": True},
        {"input": _format_input([[1,2,1],[1,2,2],[1,2,3]]), "expected_output": "1 3 2 0", "is_sample": False},
        {"input": _format_input([[1,5,10],[2,4,10],[3,3,10]]), "expected_output": "1 10 5 0", "is_sample": False},
        {"input": _format_input([[1,10,5],[2,3,10],[4,5,10]]), "expected_output": "1 5 2 10 3 5 4 10 5 5 10 0", "is_sample": False},
        {"input": _format_input([[1,2,1]]), "expected_output": "1 1 2 0", "is_sample": False},
        {"input": _format_input([[0,1,10],[5,6,10]]), "expected_output": "0 10 1 0 5 10 6 0", "is_sample": False},
        # Stress Tests (10^4 buildings)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(buildings):
        events = []
        for L, R, H in buildings:
            events.append((L, -H))
            events.append((R, H))
        events.sort()
        res = [[0, 0]]
        max_heap = [0]
        removals = {}
        for x, h in events:
            if h < 0: heapq.heappush(max_heap, h)
            else: removals[h] = removals.get(h, 0) + 1
            while -max_heap[0] in removals and removals[-max_heap[0]] > 0:
                h_to_rem = -heapq.heappop(max_heap)
                removals[h_to_rem] -= 1
            curr_max = -max_heap[0]
            if res[-1][1] != curr_max:
                res.append([x, curr_max])
        return res[1:]

    # Stress 8: Large number of overlapping buildings
    b8 = [[i, i+10, 100] for i in range(1000)]
    test_cases[7] = {"input": _format_input(b8), "expected_output": _format_output(_solve(b8)), "is_sample": False}
    # Stress 9: Spaced out buildings
    b9 = [[i*2, i*2+1, 50] for i in range(1000)]
    test_cases[8] = {"input": _format_input(b9), "expected_output": _format_output(_solve(b9)), "is_sample": False}
    # Stress 10: Buildings with increasing height at same start
    b10 = [[0, 100, i+1] for i in range(1000)]
    test_cases[9] = {"input": _format_input(b10), "expected_output": _format_output(_solve(b10)), "is_sample": False}

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
        "topics": ["Array", "Divide and Conquer", "Heap (Priority Queue)", "Binary Indexed Tree", "Segment Tree", "Line Sweep"],
        "companyIndex": 0
    }

    output_path = "201-400/218_The_Skyline_Problem.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
