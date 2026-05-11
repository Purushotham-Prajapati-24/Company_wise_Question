import json
import os

def generate_json():
    problem_id = 149
    title = "Max Points on a Line"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>149. Max Points on a Line</h3>
<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane, return <em>the maximum number of points that lie on the same straight line</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" style="width: 300px; height: 294px;" />
<pre><strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" style="width: 300px; height: 294px;" />
<pre><strong>Input:</strong> points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 300</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>All the <code>points</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "Two lines. Line 1: integer n (number of points). Line 2: n pairs of space-separated integers (x y)."
    output_format = "An integer representing the maximum number of points on a single line."
    
    constraints = [
        "1 <= points.length <= 300",
        "-10^4 <= xi, yi <= 10^4",
        "All points are unique."
    ]
    
    explanation = """To find the maximum number of points on a single straight line:
1. **Iterate Through Each Point**:
   - For every point `i`, calculate the slope it makes with every other point `j`.
   - A line is uniquely defined by a point and its slope.
2. **Handle Precision using GCD**:
   - Instead of storing slopes as floats (which leads to precision errors), store them as reduced fractions `(dy/gcd, dx/gcd)`.
   - `gcd(dy, dx)` is used to reduce the difference in coordinates.
3. **Hash Map for Slopes**:
   - For each fixed point `i`, use a hash map to store the frequency of each unique slope calculated with other points `j`.
   - The maximum frequency in the map plus one (the point `i` itself) is a candidate for the final answer.
4. **Complexity**:
   - Time Complexity: O(N^2 * log(MaxCoord)) where N is the number of points and log(MaxCoord) comes from the GCD calculation.
   - Space Complexity: O(N) to store frequencies in the hash map."""
    
    answer = """import math

def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n
        
    def get_gcd(a, b):
        return math.gcd(a, b)
        
    max_pts = 0
    for i in range(n):
        slopes = {}
        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            
            # Reduce to simplest fraction to handle precision
            g = get_gcd(dx, dy)
            slope = (dx // g, dy // g)
            
            slopes[slope] = slopes.get(slope, 0) + 1
            
        if slopes:
            max_pts = max(max_pts, max(slopes.values()) + 1)
        else:
            max_pts = max(max_pts, 1)
            
    return max_pts"""

    boilerplate = {
        "python": "import sys\nimport math\n\ndef maxPoints(points):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if lines:\n        n = int(lines[0].strip())\n        if n == 0:\n            print(0)\n        else:\n            coords = list(map(int, lines[1].split()))\n            points = [coords[i:i+2] for i in range(0, len(coords), 2)]\n            print(maxPoints(points))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <map>\n#include <numeric>\n#include <algorithm>\nusing namespace std;\nint maxPoints(vector<vector<int>>& points){\n    // User logic\n    return 0;\n}\nint main(){\n    int n; if(!(cin>>n)) return 0;\n    vector<vector<int>> pts(n,vector<int>(2));\n    for(int i=0;i<n;i++) cin>>pts[i][0]>>pts[i][1];\n    cout<<maxPoints(pts)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int maxPoints(int[][] points){\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        Scanner sc=new Scanner(System.in);\n        int n=sc.nextInt();\n        int[][]pts=new int[n][2];\n        for(int i=0;i<n;i++){pts[i][0]=sc.nextInt();pts[i][1]=sc.nextInt();}\n        System.out.println(maxPoints(pts));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction maxPoints(points){\n    // User logic\n    return 0;\n}\nconst nums=fs.readFileSync(0,'utf8').trim().split(/\\s+/).map(Number);\nif(nums.length){\n  const n=nums[0]; const pts=[];\n  for(let i=0;i<n;i++) pts.push([nums[1+2*i],nums[2+2*i]]);\n  console.log(maxPoints(pts));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\nint maxPoints(int** points, int pointsSize, int* pointsColSize){\n    // User logic\n    return 0;\n}\nint main(){\n    int n; if(scanf(\"%d\",&n)!=1) return 0;\n    int**pts=(int**)malloc(n*sizeof(int*)); int*cols=(int*)malloc(n*sizeof(int));\n    for(int i=0;i<n;i++){pts[i]=(int*)malloc(2*sizeof(int));scanf(\"%d %d\",&pts[i][0],&pts[i][1]);cols[i]=2;}\n    printf(\"%d\\n\",maxPoints(pts,n,cols)); return 0;\n}"
    }

    test_cases = [
        {"input": "3\\n1 1 2 2 3 3", "expected_output": "3", "is_sample": True},
        {"input": "6\\n1 1 3 2 5 3 4 1 2 3 1 4", "expected_output": "4", "is_sample": True},
        {"input": "1\\n1 1", "expected_output": "1", "is_sample": False},
        {"input": "2\\n1 1 1 2", "expected_output": "2", "is_sample": False},
        {"input": "3\\n1 1 1 2 1 3", "expected_output": "3", "is_sample": False},
        {"input": "3\\n1 1 2 1 3 1", "expected_output": "3", "is_sample": False},
        {"input": "4\\n0 0 1 1 0 1 1 0", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": "300\\n" + " ".join([f"{i} {i}" for i in range(300)]), "expected_output": "300", "is_sample": False},
        {"input": "300\\n" + " ".join([f"{i} 0" for i in range(300)]), "expected_output": "300", "is_sample": False},
        {"input": "300\\n" + " ".join([f"0 {i}" for i in range(300)]), "expected_output": "300", "is_sample": False}
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
        "topics": ["Array", "Math", "Hash Table", "Geometry"],
        "companyIndex": 0
    }

    output_path = "1-200/149_Max_Points_on_a_Line.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
