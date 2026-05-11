import json
import os

def generate_json():
    problem_id = 223
    title = "Rectangle Area"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>223. Rectangle Area</h3>
<p>Given the coordinates of two <strong>axis-aligned</strong> rectangles in a 2D plane, return <em>the total area covered by the two rectangles</em>.</p>

<p>The first rectangle is defined by its <strong>bottom-left</strong> corner <code>(ax1, ay1)</code> and its <strong>top-right</strong> corner <code>(ax2, ay2)</code>.</p>

<p>The second rectangle is defined by its <strong>bottom-left</strong> corner <code>(bx1, by1)</code> and its <strong>top-right</strong> corner <code>(bx2, by2)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="Rectangle Area" src="https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png" style="width: 700px; height: 365px;" />
<pre><strong>Input:</strong> ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
<strong>Output:</strong> 45
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>4</sup> &lt;= ax1 &lt;= ax2 &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= ay1 &lt;= ay2 &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= bx1 &lt;= bx2 &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= by1 &lt;= by2 &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "8 space-separated integers on a single line: ax1, ay1, ax2, ay2, bx1, by1, bx2, by2."
    output_format = "An integer representing the total area."
    
    constraints = [
        "-10,000 <= coordinates <= 10,000",
        "Rectangles are axis-aligned.",
        "Constant time complexity O(1) required."
    ]
    
    explanation = """To find the total area covered by two rectangles:
1. **Individual Areas**:
   - Area A = `(ax2 - ax1) * (ay2 - ay1)`
   - Area B = `(bx2 - bx1) * (by2 - by1)`
2. **Intersection**:
   - The intersection is also a rectangle (if it exists).
   - Intersection Width = `max(0, min(ax2, bx2) - max(ax1, bx1))`
   - Intersection Height = `max(0, min(ay2, by2) - max(ay1, by1))`
   - Intersection Area = `Intersection_Width * Intersection_Height`
3. **Total Area**:
   - Total = `Area_A + Area_B - Intersection_Area`.
4. **Complexity**:
   - O(1) time and O(1) space."""
    
    answer = """class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Intersection boundaries
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        
        return area_a + area_b - (overlap_width * overlap_height)"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    if len(nums) >= 8:\n        print(computeArea(*nums[:8]))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nlong long computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int a, b, c, d, e, f, g, h;\n    if (cin >> a >> b >> c >> d >> e >> f >> g >> h) {\n        cout << computeArea(a, b, c, d, e, f, g, h) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public long computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextInt()) {\n            int a = sc.nextInt(); int b = sc.nextInt(); int c = sc.nextInt(); int d = sc.nextInt();\n            int e = sc.nextInt(); int f = sc.nextInt(); int g = sc.nextInt(); int h = sc.nextInt();\n            System.out.println(new Solution().computeArea(a, b, c, d, e, f, g, h));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst nums = (input.match(/-?\\d+/g) || []).map(Number);\nif (nums.length >= 8) {\n    console.log(computeArea(...nums.slice(0, 8)));\n}",
        "c": "#include <stdio.h>\n\nlong long computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int a, b, c, d, e, f, g, h;\n    if (scanf(\"%d %d %d %d %d %d %d %d\", &a, &b, &c, &d, &e, &f, &g, &h) == 8) {\n        printf(\"%lld\\n\", computeArea(a, b, c, d, e, f, g, h));\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "-3 0 3 4 0 -1 9 2", "expected_output": "45", "is_sample": True},
        {"input": "-2 -2 2 2 -2 -2 2 2", "expected_output": "16", "is_sample": True},
        {"input": "0 0 1 1 1 1 2 2", "expected_output": "2", "is_sample": False},
        {"input": "0 0 10 10 2 2 8 8", "expected_output": "100", "is_sample": False},
        {"input": "0 0 1 1 2 2 3 3", "expected_output": "2", "is_sample": False},
        {"input": "-100 -100 100 100 -100 -100 100 100", "expected_output": "40000", "is_sample": False},
        {"input": "-1 -1 1 1 -2 -2 -1.5 -1.5", "expected_output": "4", "is_sample": False}, # typo in expected? no, -2 to -1.5 is 0.5x0.5=0.25? wait ints only.
        {"input": "-5 -5 5 5 5 5 10 10", "expected_output": "125", "is_sample": False},
        {"input": "-10000 -10000 10000 10000 -10000 -10000 10000 10000", "expected_output": "400000000", "is_sample": False},
        {"input": "-10000 -10000 -9999 -9999 9999 9999 10000 10000", "expected_output": "2", "is_sample": False}
    ]
    
    def _solve(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        a1 = (ax2-ax1)*(ay2-ay1)
        a2 = (bx2-bx1)*(by2-by1)
        ow = max(0, min(ax2,bx2)-max(ax1,bx1))
        oh = max(0, min(ay2,by2)-max(ay1,by1))
        return a1+a2-(ow*oh)

    # Correct input 7
    test_cases[6] = {"input": "-1 -1 1 1 -2 -2 -1 -1", "expected_output": str(_solve(-1,-1,1,1,-2,-2,-1,-1)), "is_sample": False}
    # Stress 9: Max coordinates
    test_cases[8] = {"input": "-10000 -10000 10000 10000 -10000 -10000 10000 10000", "expected_output": str(_solve(-10000,-10000,10000,10000,-10000,-10000,10000,10000)), "is_sample": False}
    # Stress 10: Just touch
    test_cases[9] = {"input": "0 0 10 10 10 10 20 20", "expected_output": str(_solve(0,0,10,10,10,10,20,20)), "is_sample": False}

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
        "topics": ["Math", "Geometry"],
        "companyIndex": 0
    }

    output_path = "201-400/223_Rectangle_Area.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
