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
        "python": "import sys, re, json\n\ndef insert(intervals, newInterval):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read()\n    nums = [int(x) for x in re.findall(r'-?\\d+', data)]\n    newInterval = nums[-2:]\n    intervals = [nums[i:i+2] for i in range(0, len(nums)-2, 2)]\n    print(json.dumps(insert(intervals, newInterval)).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {\n        // User Logic Here\n        return {};\n    }\n};\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    regex rgx(\"-?\\\\d+\");\n    sregex_iterator iter(input.begin(), input.end(), rgx), end;\n    vector<int> nums;\n    while (iter != end) { nums.push_back(stoi(iter->str())); iter++; }\n    vector<int> newInterval = {nums[nums.size()-2], nums[nums.size()-1]};\n    vector<vector<int>> intervals;\n    for (size_t i = 0; i + 1 < nums.size() - 2; i += 2) intervals.push_back({nums[i], nums[i+1]});\n    Solution sol;\n    vector<vector<int>> res = sol.insert(intervals, newInterval);\n    cout << \"[\";\n    for (size_t i = 0; i < res.size(); i++) cout << \"[\" << res[i][0] << \",\" << res[i][1] << \"]\" << (i == res.size() - 1 ? \"\" : \",\");\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int[][] insert(int[][] intervals, int[] newInterval) {\n        // User Logic Here\n        return new int[0][0];\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        List<Integer> list = new ArrayList<>();\n        while (m.find()) list.add(Integer.parseInt(m.group()));\n        int[] newInterval = {list.get(list.size() - 2), list.get(list.size() - 1)};\n        int[][] intervals = new int[(list.size() - 2) / 2][2];\n        for (int i = 0; i < intervals.length; i++) {\n            intervals[i][0] = list.get(2 * i); intervals[i][1] = list.get(2 * i + 1);\n        }\n        Solution sol = new Solution();\n        int[][] res = sol.insert(intervals, newInterval);\n        System.out.print(\"[\");\n        for (int i = 0; i < res.length; i++) System.out.print(\"[\" + res[i][0] + \",\" + res[i][1] + \"]\" + (i == res.length - 1 ? \"\" : \",\"));\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {number[][]} intervals\n * @param {number[]} newInterval\n * @return {number[][]}\n */\nvar insert = function(intervals, newInterval) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const nums = (input.match(/-?\\d+/g) || []).map(Number);\n    const newInterval = nums.slice(-2);\n    const intervals = [];\n    for (let i = 0; i + 1 < nums.length - 2; i += 2) intervals.push([nums[i], nums[i+1]]);\n    console.log(JSON.stringify(insert(intervals, newInterval)).replace(/\\s/g, ''));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n\nint** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {\n    // User Logic Here\n    return NULL;\n}\n\nint main() {\n    int capacity = 10000, size = 0;\n    int* nums = malloc(capacity * sizeof(int));\n    int found = 0, sign = 1, c;\n    long long current = 0;\n    while ((c = getchar()) != EOF) {\n        if (isdigit(c)) {\n            if (!found) { found = 1; current = c - '0'; } else current = current * 10 + (c - '0');\n        } else if (c == '-') {\n            if (found) { if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); } nums[size++] = (int)(current * sign); found = 0; sign = 1; }\n            int next = getchar();\n            if (isdigit(next)) { sign = -1; current = next - '0'; found = 1; } else ungetc(next, stdin);\n        } else {\n            if (found) { if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); } nums[size++] = (int)(current * sign); found = 0; sign = 1; }\n        }\n    }\n    if (found) { if (size == capacity) { capacity *= 2; nums = realloc(nums, capacity * sizeof(int)); } nums[size++] = (int)(current * sign); }\n    int newInterval[2] = {nums[size-2], nums[size-1]};\n    int intervalsCount = (size - 2) / 2;\n    int** intervals = malloc(intervalsCount * sizeof(int*));\n    int* colSizes = malloc(intervalsCount * sizeof(int));\n    for (int i = 0; i < intervalsCount; i++) {\n        intervals[i] = malloc(2 * sizeof(int));\n        intervals[i][0] = nums[2*i]; intervals[i][1] = nums[2*i+1];\n        colSizes[i] = 2;\n    }\n    int returnSize = 0, *returnColumnSizes = NULL;\n    int** res = insert(intervals, intervalsCount, colSizes, newInterval, 2, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) printf(\"[%d,%d]%s\", res[i][0], res[i][1], (i == returnSize - 1 ? \"\" : \",\"));\n    printf(\"]\\n\");\n    return 0;\n}"
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
