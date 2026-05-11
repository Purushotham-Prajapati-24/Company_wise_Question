import json
import os
import heapq

def generate_json():
    problem_id = 295
    title = "Find Median from Data Stream"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>295. Find Median from Data Stream</h3>
<p>The <b>median</b> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.</p>

<ul>
	<li>For example, for <code>arr = [2,3,4]</code>, the median is <code>3</code>.</li>
	<li>For example, for <code>arr = [2,3]</code>, the median is <code>(2 + 3) / 2 = 2.5</code>.</li>
</ul>

<p>Implement the MedianFinder class:</p>

<ul>
	<li><code>MedianFinder()</code> initializes the <code>MedianFinder</code> object.</li>
	<li><code>void addNum(int num)</code> adds the integer <code>num</code> from the data stream to the data structure.</li>
	<li><code>double findMedian()</code> returns the median of all elements so far. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
<strong>Output</strong>
[null, null, null, 1.5, null, 2.0]

<strong>Explanation</strong>
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-10<sup>5</sup> &lt;= num &lt;= 10<sup>5</sup></code></li>
	<li>There will be at least one element in the data structure before calling <code>findMedian</code>.</li>
	<li>At most <code>5 * 10<sup>4</sup></code> calls will be made to <code>addNum</code> and <code>findMedian</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>If all integer numbers from the stream are in the range <code>[0, 100]</code>, how would you optimize your solution?</li>
	<li>If <code>99%</code> of all integer numbers from the stream are in the range <code>[0, 100]</code>, how would you optimize your solution?</li>
</ul>"""

    input_format = "Line 1: Number of operations m. Next m lines: either 'addNum X' or 'findMedian'."
    output_format = "For each 'findMedian' command, output the median on a new line (formatted to 1 decimal place)."
    
    constraints = [
        "Time Complexity: addNum O(log N), findMedian O(1).",
        "Space Complexity: O(N).",
        "Total operations: 5 * 10^4."
    ]
    
    explanation = """To find the median from a data stream efficiently:
1. **Two Heaps Logic**:
   - Maintain two heaps: a **Max-Heap** (`lower`) to store the smaller half of the numbers, and a **Min-Heap** (`upper`) to store the larger half.
   - For any odd number of elements, one heap should have exactly one more element than the other (let's say `lower`).
2. **Operations**:
   - **addNum(num)**:
     - Push `num` into `lower` (Max-Heap).
     - To maintain the half-half property, pop from `lower` and push into `upper` (Min-Heap).
     - If `upper` has more elements than `lower`, pop from `upper` and push back into `lower`.
   - **findMedian()**:
     - If the total size is even, return the average of the tops: `(maxTop + minTop) / 2`.
     - If odd, return the top of the larger heap (e.g., `maxTop` of `lower`).
3. **Complexity**:
   - `addNum`: O(log N) due to heap insertions/deletions.
   - `findMedian`: O(1) to access heap tops."""
    
    answer = """import heapq

class MedianFinder:
    def __init__(self):
        self.lower = [] # Max-heap (negative values)
        self.upper = [] # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        
        # balance: move largest in lower to upper
        heapq.heappush(self.upper, -heapq.heappop(self.lower))
        
        # ensure lower has equal or one more than upper
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2.0"""

    boilerplate = {
        "python": "import sys\nimport heapq\n\nclass MedianFinder:\n    def __init__(self):\n        # Initialize\n        pass\n    def addNum(self, num):\n        # User logic\n        pass\n    def findMedian(self):\n        # User logic\n        return 0.0\n\nif __name__ == '__main__':\n    obj = MedianFinder()\n    input_data = sys.stdin.read().splitlines()\n    if input_data:\n        m = int(input_data[0])\n        for i in range(1, m + 1):\n            parts = input_data[i].split()\n            if parts[0] == 'addNum':\n                obj.addNum(int(parts[1]))\n            elif parts[0] == 'findMedian':\n                print(f\"{obj.findMedian():.1f}\")",
        "cpp": "#include <iostream>\n#include <queue>\n#include <vector>\n#include <iomanip>\n#include <sstream>\nusing namespace std;\n\nclass MedianFinder {\npublic:\n    void addNum(int num) {}\n    double findMedian() { return 0.0; }\n};\n\nint main() {\n    MedianFinder obj;\n    int m;\n    cin >> m;\n    cin.ignore();\n    for (int i = 0; i < m; i++) {\n        string line;\n        getline(cin, line);\n        if (line.substr(0, 6) == \"addNum\") {\n            obj.addNum(stoi(line.substr(7)));\n        } else if (line == \"findMedian\") {\n            cout << fixed << setprecision(1) << obj.findMedian() << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class MedianFinder {\n    public void addNum(int num) {}\n    public double findMedian() { return 0.0; }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int m = sc.nextInt(); sc.nextLine();\n        MedianFinder obj = new MedianFinder();\n        for (int i = 0; i < m; i++) {\n            String line = sc.nextLine().trim();\n            if (line.startsWith(\"addNum\")) obj.addNum(Integer.parseInt(line.split(\" \")[1]));\n            else if (line.equals(\"findMedian\")) System.out.printf(\"%.1f%n\", obj.findMedian());\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nconst lines = fs.readFileSync(0, 'utf-8').trim().split('\\n');\nconst m = parseInt(lines[0]);\n\nclass MedianFinder {\n    constructor() { /* User logic */ }\n    addNum(num) { /* User logic */ }\n    findMedian() { return 0.0; }\n}\n\nconst obj = new MedianFinder();\nfor (let i = 1; i <= m; i++) {\n    const parts = lines[i].trim().split(' ');\n    if (parts[0] === 'addNum') obj.addNum(parseInt(parts[1]));\n    else if (parts[0] === 'findMedian') console.log(obj.findMedian().toFixed(1));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n\n// C stub for MedianFinder\nint main() {\n    int m;\n    scanf(\"%d\", &m);\n    char line[100];\n    fgets(line, sizeof(line), stdin); // consume newline\n    for (int i = 0; i < m; i++) {\n        fgets(line, sizeof(line), stdin);\n        if (strncmp(line, \"findMedian\", 10) == 0) {\n            printf(\"0.0\\n\");\n        }\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "5\\naddNum 1\\naddNum 2\\nfindMedian\\naddNum 3\\nfindMedian", "expected_output": "1.5\\n2.0", "is_sample": True},
        {"input": "2\\naddNum 1\\nfindMedian", "expected_output": "1.0", "is_sample": True},
        {"input": "3\\naddNum 1\\naddNum -1\\nfindMedian", "expected_output": "0.0", "is_sample": True},
        {"input": "8\\naddNum 1\\naddNum 2\\naddNum 3\\naddNum 4\\naddNum 5\\naddNum 6\\naddNum 7\\nfindMedian", "expected_output": "4.0", "is_sample": False},
        {"input": "9\\naddNum 1\\naddNum 2\\naddNum 3\\naddNum 4\\naddNum 5\\naddNum 6\\naddNum 7\\naddNum 8\\nfindMedian", "expected_output": "4.5", "is_sample": False},
        {"input": "4\\naddNum 10\\naddNum 20\\nfindMedian\\nfindMedian", "expected_output": "15.0\\n15.0", "is_sample": False},
        {"input": "5\\naddNum 10\\naddNum 5\\nfindMedian\\naddNum 7\\nfindMedian", "expected_output": "7.5\\n7.0", "is_sample": False},
        # Stress cases
        {"input": "10001\\n" + "\\n".join(["addNum " + str(i) for i in range(10000)]) + "\\nfindMedian", "expected_output": "4999.5", "is_sample": False},
        {"input": "10001\\n" + "\\n".join(["addNum " + str(i) for i in range(10000, 0, -1)]) + "\\nfindMedian", "expected_output": "5000.5", "is_sample": False},
        {"input": "5\\naddNum 2\\naddNum 1\\naddNum 3\\naddNum 0\\nfindMedian", "expected_output": "1.5", "is_sample": False}
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
        "topics": ["Two Heaps", "Design", "Sorting", "Data Stream"],
        "companyIndex": 0
    }

    output_path = "201-400/295_Find_Median_from_Data_Stream.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
