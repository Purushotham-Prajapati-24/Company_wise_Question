import json
import os

def generate_json():
    problem_id = 452
    title = "Minimum Number of Arrows to Burst Balloons"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>452. Minimum Number of Arrows to Burst Balloons</h3>
<p>There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code>points</code> where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code> denotes a balloon whose <strong>horizontal diameter</strong> stretches between <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code>. You do not know the exact y-coordinates of the balloons.</p>

<p>Arrows can be shot up <strong>directly vertically</strong> (in the positive y-direction) from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> is <strong>burst</strong> by an arrow shot at <code>x</code> if <code>x<sub>start</sub> &lt;= x &lt;= x<sub>end</sub></code>. There is <strong>no limit</strong> to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.</p>

<p>Given the array <code>points</code>, return <em>the <strong>minimum</strong> number of arrows that must be shot to burst all balloons</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> points = [[10,16],[2,8],[1,6],[7,12]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 12, bursting the balloons [10,16] and [7,12].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> points = [[1,2],[3,4],[5,6],[7,8]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One arrow needs to be shot for each balloon for a total of 4 arrows.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> points = [[1,2],[2,3],[3,4],[4,5]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-2<sup>31</sup> &lt;= x<sub>start</sub> &lt; x<sub>end</sub> &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A JSON 2D array of integers `points`."
    output_format = "An integer representing the minimum number of arrows."
    
    constraints = [
        "1 <= points.length <= 10^5",
        "points[i].length == 2",
        "-2^31 <= xstart < xend <= 2^31 - 1"
    ]
    
    explanation = "This is a greedy problem. Sort the balloons by their end coordinates. Shoot an arrow at the end of the first balloon. This arrow will burst all balloons that start before or at this end point. For the next unburst balloon, shoot another arrow at its end point and repeat."
    
    answer = """class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        curr_end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > curr_end:
                arrows += 1
                curr_end = points[i][1]
        return arrows"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def findMinArrowShots(self, points: list[list[int]]) -> int:\n        # User logic here\n        return 0\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        points = json.loads(raw_input)\n        sol = Solution()\n        print(sol.findMinArrowShots(points))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int findMinArrowShots(vector<vector<int>>& points) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        line.erase(remove(line.begin(), line.end(), '['), line.end());\n        line.erase(remove(line.begin(), line.end(), ']'), line.end());\n        line.erase(remove(line.begin(), line.end(), ' '), line.end());\n        if (line.empty()) { cout << 0 << endl; return 0; }\n        stringstream ss(line);\n        string item;\n        vector<vector<int>> points;\n        vector<int> current;\n        while (getline(ss, item, ',')) {\n            current.push_back(stoi(item));\n            if (current.size() == 2) { points.push_back(current); current.clear(); }\n        }\n        Solution sol;\n        cout << sol.findMinArrowShots(points) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int findMinArrowShots(int[][] points) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine().replaceAll(\"[\\\\[\\\\] ]\", \"\");\n            if (line.isEmpty()) { System.out.println(0); return; }\n            String[] parts = line.split(\",\");\n            int[][] points = new int[parts.length / 2][2];\n            for (int i = 0; i < points.length; i++) {\n                points[i][0] = Integer.parseInt(parts[2*i]);\n                points[i][1] = Integer.parseInt(parts[2*i + 1]);\n            }\n            System.out.println(new Solution().findMinArrowShots(points));\n        }\n    }\n}",
        "javascript": "var findMinArrowShots = function(points) {\n    // User logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const points = JSON.parse(input);\n    console.log(findMinArrowShots(points));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint findMinArrowShots(int** points, int pointsSize, int* pointsColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[10,16],[2,8],[1,6],[7,12]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1,2],[3,4],[5,6],[7,8]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1,2],[2,3],[3,4],[4,5]]", "expected_output": "2", "is_sample": True},
        {"input": "[[1,10]]", "expected_output": "1", "is_sample": False},
        {"input": "[ [1, 2], [2, 3] ]", "expected_output": "1", "is_sample": False}, # Spaces
        {"input": "[[1,2],[3,4]]", "expected_output": "2", "is_sample": False},
        {"input": "[[1,10],[2,3],[4,5],[6,7],[8,9]]", "expected_output": "5", "is_sample": False},
        {"input": "[[1,5],[2,6],[3,7]]", "expected_output": "1", "is_sample": False},
        {"input": "[[-2147483648,2147483647],[-2147483648,2147483647]]", "expected_output": "1", "is_sample": False},
        {"input": json.dumps([[i, i+1] for i in range(100)]), "expected_output": "50", "is_sample": False}
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
        "topics": ["Array", "Greedy", "Sorting"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Minimum_Number_of_Arrows_to_Burst_Balloons.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
