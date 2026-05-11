import json
import os

def generate_json():
    problem_id = 253
    title = "Meeting Rooms II"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>253. Meeting Rooms II</h3>
<p>Given an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of conference rooms required</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>"""

    input_format = "First line: Number of intervals N. Next N lines: Two space-separated integers, start_i and end_i, representing the interval."
    output_format = "An integer representing the minimum number of rooms."
    
    constraints = [
        "1 <= intervals.length <= 10,000",
        "0 <= start < end <= 1,000,000"
    ]
    
    explanation = """To find the minimum number of rooms (maximum concurrent meetings):
1. **Sweep-line Algorithm**:
   - Extract all start times and end times into two separate lists.
   - Sort both lists.
   - Use two pointers, `s` for start and `e` for end times.
   - Iterate through the sorted start times:
     - If the current meeting starts before the earliest ending meeting (`start[s] < end[e]`), we need a new room (`curr_rooms += 1`).
     - Otherwise, a room has been freed; move the end pointer (`e += 1`).
   - The result is the maximum number of rooms needed at any point.
2. **Complexity**:
   - Time: O(N log N) due to sorting.
   - Space: O(N) to store start and end times."""
    
    answer = """class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        rooms = 0
        end_ptr = 0
        
        for s in range(len(intervals)):
            if starts[s] < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1
                
        return rooms"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef minMeetingRooms(intervals: list[list[int]]) -> int:\n    # User logic here\n    return 0\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Find all bracketed pairs [start, end]\n    pairs = re.findall(r'\\[\\s*(-?\\\\d+)\\s*,\\s*(-?\\\\d+)\\s*\\]', raw_input)\n    intervals = [[int(p[0]), int(p[1])] for p in pairs]\n    if intervals:\n        print(minMeetingRooms(intervals))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nint minMeetingRooms(vector<vector<int>>& intervals) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input, line;\n    while (getline(cin, line)) input += line + \" \";\n    \n    regex re_pair(\"\\\\[\\\\s*(-?\\\\d+)\\\\s*,\\\\s*(-?\\\\d+)\\\\s*\\\\]\");\n    auto b = sregex_iterator(input.begin(), input.end(), re_pair);\n    auto e = sregex_iterator();\n    vector<vector<int>> intervals;\n    for (auto i = b; i != e; ++i) {\n        intervals.push_back({stoi((*i)[1]), stoi((*i)[2])});\n    }\n    \n    if (!intervals.empty()) {\n        cout << minMeetingRooms(intervals) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int minMeetingRooms(int[][] intervals) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        \n        List<int[]> list = new ArrayList<>();\n        Matcher m = Pattern.compile(\"\\\\[\\\\s*(-?\\\\d+)\\\\s*,\\\\s*(-?\\\\d+)\\\\s*\\\\]\").matcher(input);\n        while (m.find()) {\n            list.add(new int[]{Integer.parseInt(m.group(1)), Integer.parseInt(m.group(2))});\n        }\n        \n        if (!list.isEmpty()) {\n            int[][] intervals = list.toArray(new int[0][]);\n            System.out.println(new Solution().minMeetingRooms(intervals));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction minMeetingRooms(intervals) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst matches = input.matchAll(/\\[\\s*(-?\\d+)\\s*,\\s*(-?\\d+)\\s*\\]/g);\nlet intervals = [];\nfor (const m of matches) {\n    intervals.push([parseInt(m[1]), parseInt(m[2])]);\n}\nif (intervals.length > 0) {\n    console.log(minMeetingRooms(intervals));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\nint minMeetingRooms(int** intervals, int intervalsSize, int* intervalsColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    static char buffer[1000000];\n    int bytes = fread(buffer, 1, sizeof(buffer)-1, stdin);\n    buffer[bytes] = '\\0';\n    \n    int** intervals = (int**)malloc(10000 * sizeof(int*));\n    int* cols = (int*)malloc(10000 * sizeof(int));\n    int count = 0;\n    \n    char* p = buffer;\n    while (*p) {\n        if (*p == '[') {\n            p++;\n            while (*p && isspace(*p)) p++;\n            if (isdigit(*p) || *p == '-') {\n                intervals[count] = (int*)malloc(2 * sizeof(int));\n                intervals[count][0] = strtol(p, &p, 10);\n                while (*p && (*p != ',')) p++;\n                if (*p == ',') p++;\n                intervals[count][1] = strtol(p, &p, 10);\n                cols[count] = 2;\n                count++;\n            }\n        } else p++;\n    }\n    \n    if (count > 0) {\n        printf(\"%d\\n\", minMeetingRooms(intervals, count, cols));\n    }\n    return 0;\n}"
    }

    def create_tc(intervals):
        res = [str(len(intervals))]
        for start, end in intervals:
            res.append(f"{start} {end}")
        return "\\n".join(res)

    test_cases = [
        {"input": create_tc([[0,30],[5,10],[15,20]]), "expected_output": "2", "is_sample": True},
        {"input": create_tc([[7,10],[2,4]]), "expected_output": "1", "is_sample": True},
        {"input": create_tc([[1,5],[5,10]]), "expected_output": "1", "is_sample": False}, # Touches (not overlapping)
        {"input": create_tc([[1,10],[2,7],[3,19],[8,12],[10,20],[11,30]]), "expected_output": "4", "is_sample": False},
        {"input": create_tc([[1,2],[1,2],[1,2]]), "expected_output": "3", "is_sample": False},
        {"input": create_tc([[1,100],[2,3],[4,5],[6,7]]), "expected_output": "2", "is_sample": False},
        {"input": create_tc([[0,1000000]]), "expected_output": "1", "is_sample": False},
    ]
    
    def _solve_rooms(intervals):
        s = sorted([i[0] for i in intervals])
        e = sorted([i[1] for i in intervals])
        ans = ep = 0
        for start in s:
            if start < e[ep]: ans += 1
            else: ep += 1
        return ans

    # Stress 8: 10,000 staggered
    i8 = [[i, i+1] for i in range(10000)]
    test_cases.append({"input": create_tc(i8), "expected_output": "1", "is_sample": False})
    # Stress 9: 10,000 all overlapping
    i9 = [[0, 1000000] for _ in range(10000)]
    test_cases.append({"input": create_tc(i9), "expected_output": "10000", "is_sample": False})
    # Stress 10: Nested
    i10 = [[i, 20000-i] for i in range(1, 10001)]
    test_cases.append({"input": create_tc(i10), "expected_output": "10000", "is_sample": False})

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
        "topics": ["Array", "Two Pointers", "Greedy", "Sorting", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = "201-400/253_Meeting_Rooms_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
