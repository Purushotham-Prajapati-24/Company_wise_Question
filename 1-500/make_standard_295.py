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
        "python": "import sys\nimport re\nimport json\n\nclass MedianFinder:\n    def __init__(self):\n        # User logic here\n        pass\n    def addNum(self, num):\n        # User logic here\n        pass\n    def findMedian(self):\n        # User logic here\n        return 0.0\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    try:\n        data = re.findall(r'\\[.*?\\]', raw_input, re.DOTALL)\n        cmds = json.loads(data[0])\n        args = json.loads(data[1])\n    except:\n        parts = raw_input.strip().split('\\n')\n        cmds = json.loads(parts[0])\n        args = json.loads(parts[1])\n\n    obj = None\n    results = []\n    for i, cmd in enumerate(cmds):\n        if cmd == 'MedianFinder':\n            obj = MedianFinder()\n            results.append(None)\n        elif cmd == 'addNum':\n            obj.addNum(args[i][0])\n            results.append(None)\n        elif cmd == 'findMedian':\n            results.append(float(obj.findMedian()))\n    \n    print(json.dumps(results).replace('None', 'null'))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <iomanip>\n\nusing namespace std;\n\nclass MedianFinder {\npublic:\n    MedianFinder() {}\n    void addNum(int num) {}\n    double findMedian() { return 0.0; }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_cmd(R\"(\"(\\w+)\")\");\n    auto cmd_begin = sregex_iterator(input.begin(), input.end(), re_cmd);\n    auto end = sregex_iterator();\n    \n    vector<string> cmds;\n    for (auto i = cmd_begin; i != end; ++i) cmds.push_back(i->str(1));\n    \n    MedianFinder* obj = nullptr;\n    cout << \"[\";\n    int cidx = 0;\n    for (const string& cmd : cmds) {\n        if (cidx > 0) cout << \",\";\n        if (cmd == \"MedianFinder\") {\n            obj = new MedianFinder();\n            cout << \"null\";\n        } else if (cmd == \"addNum\") {\n            static int arg_pos_add = 0;\n            if (arg_pos_add == 0) arg_pos_add = input.find(\"[\", input.find(\"]\") + 1);\n            regex re_arg(R\"(-?\\d+)\");\n            auto i = sregex_iterator(input.begin() + arg_pos_add, input.end(), re_arg);\n            for (int k = 0; k < cidx; k++) { ++i; }\n            obj->addNum(stoi(i->str()));\n            cout << \"null\";\n        } else if (cmd == \"findMedian\") {\n            cout << fixed << setprecision(5) << obj->findMedian();\n        }\n        cidx++;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class MedianFinder {\n        public MedianFinder() {}\n        public void addNum(int num) {}\n        public double findMedian() { return 0.0; }\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        List<String> cmds = new ArrayList<>();\n        Matcher mCmd = Pattern.compile(\"\\\"(\\\\w+)\\\"\").matcher(input.split(\"\\\\n\")[0]);\n        while (mCmd.find()) cmds.add(mCmd.group(1));\n\n        MedianFinder obj = null;\n        List<Object> results = new ArrayList<>();\n        for (int i = 0; i < cmds.size(); i++) {\n            String cmd = cmds.get(i);\n            if (cmd.equals(\"MedianFinder\")) {\n                obj = new MedianFinder();\n                results.add(null);\n            } else if (cmd.equals(\"addNum\")) {\n                // Extract arg\n                obj.addNum(0);\n                results.add(null);\n            } else if (cmd.equals(\"findMedian\")) {\n                results.add(obj.findMedian());\n            }\n        }\n        System.out.println(results.toString().replace(\" \", \"\").toLowerCase());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass MedianFinder {\n    constructor() {}\n    addNum(num) {}\n    findMedian() { return 0.0; }\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst parts = input.split('\\n');\nconst cmds = JSON.parse(parts[0]);\nconst args = JSON.parse(parts[1]);\n\nlet obj = null;\nconst results = [];\nfor (let i = 0; i < cmds.length; i++) {\n    if (cmds[i] === 'MedianFinder') {\n        obj = new MedianFinder();\n        results.push(null);\n    } else if (cmds[i] === 'addNum') {\n        obj.addNum(args[i][0]);\n        results.push(null);\n    } else if (cmds[i] === 'findMedian') {\n        results.push(obj.findMedian());\n    }\n}\nconsole.log(JSON.stringify(results));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    printf(\"[]\\n\");\n    return 0;\n}"
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
