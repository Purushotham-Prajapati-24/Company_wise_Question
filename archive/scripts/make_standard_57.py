import json
import os

def generate_json():
    problem_id = 57
    title = "Insert Interval"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>57. Insert Interval</h3>
<p>You are given an array of non-overlapping intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> sorted in ascending order by <code>start<sub>i</sub></code>. You are also given an interval <code>newInterval = [start, end]</code> that represents the start and end of another interval.</p>

<p>Insert <code>newInterval</code> into <code>intervals</code> such that <code>intervals</code> is still sorted in ascending order by <code>start<sub>i</sub></code> and <code>intervals</code> still does not have any overlapping intervals (merge overlapping intervals if necessary).</p>

<p>Return <code>intervals</code><em> after the insertion</em>.</p>

<p><strong>Note:</strong> You don't need to modify <code>intervals</code> in-place. You can make a new array and return it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:</strong> Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals</code> is sorted by <code>start<sub>i</sub></code> in <strong>ascending</strong> order.</li>
	<li><code>newInterval.length == 2</code></li>
	<li><code>0 &lt;= start &lt;= end &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An array of non-overlapping intervals sorted by start and a new interval to insert."
    output_format = "An array of non-overlapping intervals after insertion and merging."
    
    constraints = [
        "0 <= intervals.length <= 10^4",
        "Intervals sorted by start",
        "0 <= start <= end <= 10^5"
    ]
    
    explanation = """To insert and merge an interval into a sorted list:
1. **Three Phases**:
   - **Phase 1: Before Overlap**: Add all intervals that end before `newInterval` starts (`interval[1] < newInterval[0]`).
   - **Phase 2: During Overlap**: Merge intervals that overlap with `newInterval` (`interval[0] <= newInterval[1]`). Update `newInterval`'s start and end to the minimum/maximum of overlapped ranges.
   - **Phase 3: After Overlap**: Add the merged `newInterval` and all remaining intervals.
2. **Complexity**:
   - **Time**: $O(N)$ (single pass).
   - **Space**: $O(N)$ for the result list."""
    
    answer = """def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)
    
    # Phase 1: Left of newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
        
    # Phase 2: Overlapping
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    
    # Phase 3: Right of newInterval
    while i < n:
        res.append(intervals[i])
        i += 1
        
    return res"""

    boilerplate = {
        "python": "import sys\n\ndef insert(intervals, newInterval):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().strip().splitlines()\n    intervals = []\n    for line in lines[:-1]:\n        if line.strip():\n            a, b = map(int, line.split())\n            intervals.append([a, b])\n    ni = list(map(int, lines[-1].split()))\n    res = insert(intervals, ni)\n    print('[' + ','.join('[' + str(a) + ',' + str(b) + ']' for a, b in res) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\n\nusing namespace std;\n\nvector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<vector<int>> intervals;\n    vector<int> lastPair;\n    vector<string> lines;\n    while (getline(cin, line)) { if (!line.empty()) lines.push_back(line); }\n    for (int i = 0; i < (int)lines.size() - 1; i++) {\n        stringstream ss(lines[i]);\n        int a, b;\n        if (ss >> a >> b) intervals.push_back({a, b});\n    }\n    stringstream ss(lines.back());\n    int a, b;\n    ss >> a >> b;\n    vector<int> newInterval = {a, b};\n    auto res = insert(intervals, newInterval);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"[\" << res[i][0] << \",\" << res[i][1] << \"]\";\n        if (i + 1 < (int)res.size()) cout << \",\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int[][] insert(int[][] intervals, int[] newInterval) {\n        // User logic\n        return new int[0][0];\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<int[]> list = new ArrayList<>();\n        while (sc.hasNextInt()) {\n            int a = sc.nextInt();\n            if (!sc.hasNextInt()) break;\n            int b = sc.nextInt();\n            list.add(new int[]{a, b});\n        }\n        int[] newInterval = list.remove(list.size() - 1);\n        int[][] intervals = list.toArray(new int[0][]);\n        int[][] res = insert(intervals, newInterval);\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.length; i++) {\n            sb.append(\"[\").append(res[i][0]).append(\",\").append(res[i][1]).append(\"]\");\n            if (i + 1 < res.length) sb.append(\",\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction insert(intervals, newInterval) {\n    // User logic\n    return [];\n}\n\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n').filter(l => l.trim());\nconst intervals = lines.slice(0, -1).map(l => l.trim().split(/\\s+/).map(Number));\nconst newInterval = lines[lines.length - 1].trim().split(/\\s+/).map(Number);\nconst res = insert(intervals, newInterval);\nconsole.log('[' + res.map(p => '[' + p[0] + ',' + p[1] + ']').join(',') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    int buff[20001][2];\n    int size = 0;\n    while (size < 20001 && scanf(\"%d %d\", &buff[size][0], &buff[size][1]) == 2) size++;\n    int newInterval[2] = {buff[size-1][0], buff[size-1][1]};\n    size--;\n    int** intervals = (int**)malloc(size * sizeof(int*));\n    for (int i = 0; i < size; i++) intervals[i] = buff[i];\n    int colSizes[20001];\n    for (int i = 0; i < size; i++) colSizes[i] = 2;\n    int returnSize = 0;\n    int* returnColumnSizes = NULL;\n    int niColSize = 2;\n    int** res = insert(intervals, size, colSizes, newInterval, 2, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[%d,%d]\", res[i][0], res[i][1]);\n        if (i + 1 < returnSize) printf(\",\");\n        if (res[i]) free(res[i]);\n    }\n    printf(\"]\\n\");\n    if (returnColumnSizes) free(returnColumnSizes);\n    if (res) free(res);\n    free(intervals);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3\n6 9\n2 5", "expected_output": "[[1,5],[6,9]]", "is_sample": True},
        {"input": "1 2\n3 5\n6 7\n8 10\n12 16\n4 8", "expected_output": "[[1,2],[3,10],[12,16]]", "is_sample": True},
        {"input": "5 7", "expected_output": "[[5,7]]", "is_sample": False},
        {"input": "1 5\n2 3", "expected_output": "[[1,5]]", "is_sample": False},
        {"input": "1 5\n6 8", "expected_output": "[[1,5],[6,8]]", "is_sample": False},
        {"input": "1 5\n0 0", "expected_output": "[[0,0],[1,5]]", "is_sample": False},
        {"input": "1 5\n0 3", "expected_output": "[[0,5]]", "is_sample": False},
        {"input": "1 5\n3 7", "expected_output": "[[1,7]]", "is_sample": False},
        {"input": "1 2\n6 7\n3 5", "expected_output": "[[1,2],[3,5],[6,7]]", "is_sample": False},
        {"input": "3 5\n6 7\n0 1", "expected_output": "[[0,1],[3,5],[6,7]]", "is_sample": False}
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
        "topics": ["Array"],
        "companyIndex": 0
    }

    output_path = "1-200/57_Insert_Interval.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
