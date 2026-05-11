import json
import os

def generate_json():
    problem_id = 56
    title = "Merge Intervals"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>56. Merge Intervals</h3>
<p>Given an array of <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An array of intervals where intervals[i] = [start, end]."
    output_format = "An array of merged intervals."
    
    constraints = [
        "1 <= intervals.length <= 10^4",
        "intervals[i].length == 2",
        "0 <= start <= end <= 10^4"
    ]
    
    explanation = """To merge overlapping intervals:
1. **Sort Intervals**: Sort by the starting points `intervals[i][0]`.
2. **Merging Logic**:
   - Initialize an empty list `merged`.
   - Iterate through the sorted intervals.
   - For each interval:
     - If `merged` is empty or the current interval's start is greater than the last merged interval's end, add it to `merged`.
     - Otherwise, the intervals overlap: update the end of the last merged interval to `max(last_merged_end, current_interval_end)`.
3. **Complexity**:
   - **Time**: $O(N \log N)$ (sorting dominated).
   - **Space**: $O(N)$ for sorting or $O(1)$ if sorted in-place (excluding result storage)."""
    
    answer = """def merge(intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged"""

    boilerplate = {
        "python": "import sys\n\ndef merge(intervals):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().strip().splitlines()\n    intervals = []\n    for line in lines:\n        if line.strip():\n            parts = line.split()\n            intervals.append([int(parts[0]), int(parts[1])])\n    res = merge(intervals)\n    print('[' + ','.join('[' + str(a) + ',' + str(b) + ']' for a, b in res) + ']')",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <sstream>\n\nusing namespace std;\n\nvector<vector<int>> merge(vector<vector<int>>& intervals) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string line;\n    vector<vector<int>> intervals;\n    while (getline(cin, line)) {\n        if (line.empty()) continue;\n        stringstream ss(line);\n        int a, b;\n        if (ss >> a >> b) intervals.push_back({a, b});\n    }\n    auto res = merge(intervals);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"[\" << res[i][0] << \",\" << res[i][1] << \"]\";\n        if (i + 1 < (int)res.size()) cout << \",\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int[][] merge(int[][] intervals) {\n        // User logic\n        return new int[0][0];\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<int[]> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(new int[]{sc.nextInt(), sc.nextInt()});\n        int[][] res = merge(list.toArray(new int[0][]));\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.length; i++) {\n            sb.append(\"[\").append(res[i][0]).append(\",\").append(res[i][1]).append(\"]\");\n            if (i + 1 < res.length) sb.append(\",\");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction merge(intervals) {\n    // User logic\n    return [];\n}\n\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n').filter(l => l.trim());\nconst intervals = lines.map(l => l.trim().split(/\\s+/).map(Number));\nconst res = merge(intervals);\nconsole.log('[' + res.map(p => '[' + p[0] + ',' + p[1] + ']').join(',') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    int buff[20001][2];\n    int size = 0;\n    while (size < 20000 && scanf(\"%d %d\", &buff[size][0], &buff[size][1]) == 2) size++;\n    int** intervals = (int**)malloc(size * sizeof(int*));\n    for (int i = 0; i < size; i++) intervals[i] = buff[i];\n    int colSizes[20001];\n    for (int i = 0; i < size; i++) colSizes[i] = 2;\n    int returnSize = 0;\n    int* returnColumnSizes = NULL;\n    int** res = merge(intervals, size, colSizes, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[%d,%d]\", res[i][0], res[i][1]);\n        if (i + 1 < returnSize) printf(\",\");\n        if (res[i]) free(res[i]);\n    }\n    printf(\"]\\n\");\n    if (returnColumnSizes) free(returnColumnSizes);\n    if (res) free(res);\n    free(intervals);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "1 3\n2 6\n8 10\n15 18", "expected_output": "[[1,6],[8,10],[15,18]]", "is_sample": True},
        {"input": "1 4\n4 5", "expected_output": "[[1,5]]", "is_sample": True},
        {"input": "1 10", "expected_output": "[[1,10]]", "is_sample": False},
        {"input": "1 10\n2 3\n4 5\n6 7\n8 9", "expected_output": "[[1,10]]", "is_sample": False},
        {"input": "0 4\n1 4", "expected_output": "[[0,4]]", "is_sample": False},
        {"input": "0 1\n1 4", "expected_output": "[[0,4]]", "is_sample": False},
        {"input": "1 4\n2 3", "expected_output": "[[1,4]]", "is_sample": False},
        {"input": "1 5\n6 10", "expected_output": "[[1,5],[6,10]]", "is_sample": False},
        {"input": "1 2\n2 3\n3 4\n4 5", "expected_output": "[[1,5]]", "is_sample": False},
        {"input": "0 0\n0 0", "expected_output": "[[0,0]]", "is_sample": False}
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
        "topics": ["Array", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/56_Merge_Intervals.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
