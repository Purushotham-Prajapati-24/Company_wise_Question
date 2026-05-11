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
        "python": "import sys, re, json\n\ndef merge(intervals):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    intervals = [nums[i:i+2] for i in range(0, len(nums), 2)]\n    print(json.dumps(merge(intervals)).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<int>> merge(vector<vector<int>>& intervals) {\n        // User Logic Here\n        return {};\n    }\n};\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    regex rgx(\"-?\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while (iter != end) { nums.push_back(stoi(iter->str())); iter++; }\n    vector<vector<int>> intervals;\n    for (size_t i = 0; i + 1 < nums.size(); i += 2) intervals.push_back({nums[i], nums[i+1]});\n    Solution sol;\n    vector<vector<int>> res = sol.merge(intervals);\n    cout << \"[\";\n    for (size_t i = 0; i < res.size(); i++) cout << \"[\" << res[i][0] << \",\" << res[i][1] << \"]\" << (i == res.size() - 1 ? \"\" : \",\");\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int[][] merge(int[][] intervals) {\n        // User Logic Here\n        return new int[0][0];\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        int[][] intervals = new int[list.size() / 2][2];\n        for (int i = 0; i < intervals.length; i++) {\n            intervals[i][0] = list.get(2 * i); intervals[i][1] = list.get(2 * i + 1);\n        }\n        Solution sol = new Solution();\n        int[][] res = sol.merge(intervals);\n        System.out.print(\"[\");\n        for (int i = 0; i < res.length; i++) System.out.print(\"[\" + res[i][0] + \",\" + res[i][1] + \"]\" + (i == res.length - 1 ? \"\" : \",\"));\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[][]} intervals\n * @return {number[][]}\n */\nvar merge = function(intervals) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = (input.match(/-?\\d+/g) || []).map(Number);\n    const intervals = [];\n    for (let i = 0; i + 1 < nums.length; i += 2) intervals.push([nums[i], nums[i+1]]);\n    console.log(JSON.stringify(merge(intervals)).replace(/\\s/g, ''));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {\n    // User Logic Here\n    return NULL;\n}\n\nint main() {\n    int capacity = 10000, size = 0;\n    int* nums = malloc(capacity * sizeof(int));\n    int found = 0, sign = 1, c;\n    long long current = 0;\n    while ((c = getchar()) != EOF) {\n        if (isdigit(c)) {\n            if (!found) { found = 1; current = c - '0'; } else current = current * 10 + (c - '0');\n        } else if (c == '-') {\n            if (found) { if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); } nums[size++] = (int)(current * sign); found = 0; sign = 1; }\n            int next = getchar();\n            if (isdigit(next)) { sign = -1; current = next - '0'; found = 1; } else ungetc(next, stdin);\n        } else {\n            if (found) { if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); } nums[size++] = (int)(current * sign); found = 0; sign = 1; }\n        }\n    }\n    if (found) { if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); } nums[size++] = (int)(current * sign); }\n    int intervalsCount = size / 2;\n    int** intervals = malloc(intervalsCount * sizeof(int*));\n    int* colSizes = malloc(intervalsCount * sizeof(int));\n    for (int i = 0; i < intervalsCount; i++) {\n        intervals[i] = malloc(2 * sizeof(int));\n        intervals[i][0] = nums[2*i]; intervals[i][1] = nums[2*i+1];\n        colSizes[i] = 2;\n    }\n    int returnSize = 0, *returnColumnSizes = NULL;\n    int** res = merge(intervals, intervalsCount, colSizes, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) printf(\"[%d,%d]%s\", res[i][0], res[i][1], (i == returnSize - 1 ? \"\" : \",\"));\n    printf(\"]\\n\");\n    return 0;\n}"
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
