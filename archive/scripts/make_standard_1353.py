import json
import os

def generate_json():
    problem_id = 1353
    title = "Maximum Number of Events That Can Be Attended"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>1353. Maximum Number of Events That Can Be Attended</h3>
<p>You are given an array of <code>events</code> where <code>events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>]</code>. Every event <code>i</code> starts at <code>startDay<sub>i</sub></code> and ends at <code>endDay<sub>i</sub></code>.</p>

<p>You can attend an event <code>i</code> at any day <code>d</code> where <code>startDay<sub>i</sub> &lt;= d &lt;= endDay<sub>i</sub></code>. You can only attend one event at any time <code>d</code>.</p>

<p>Return <em>the maximum number of events you can attend</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/05/e1.png" style="width: 400px; height: 267px;" />
<pre>
<strong>Input:</strong> events = [[1,2],[2,3],[3,4]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can attend all three events.
One way to attend them all is as follows:
- Attend the first event on day 1.
- Attend the second event on day 2.
- Attend the third event on day 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> events = [[1,2],[2,3],[3,4],[1,2]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= events.length &lt;= 10<sup>5</sup></code></li>
	<li><code>events[i].length == 2</code></li>
	<li><code>1 &lt;= startDay<sub>i</sub> &lt;= endDay<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An array of arrays of integers, where each inner array contains [startDay, endDay]."
    output_format = "An integer representing the maximum number of events that can be attended."
    
    constraints = [
        "1 <= events.length <= 10^5",
        "events[i].length == 2",
        "1 <= startDay_i <= endDay_i <= 10^5"
    ]
    
    explanation = """To maximize the number of events attended, we use a greedy approach with a priority queue:
1. **Sort Events**: Sort all events by their `startDay`. This allows us to process days sequentially.
2. **Priority Queue (Min-Heap)**: Use a min-heap to keep track of the `endDay` of all events that have already started but haven't been attended or expired yet.
3. **Iterate Through Days**: Iterate from day 1 up to the maximum possible day (100,000).
   - **Add New Events**: On day `d`, add the `endDay` of all events that start on day `d` to the min-heap.
   - **Remove Expired Events**: Remove events from the min-heap whose `endDay` is less than `d` (they have already passed).
   - **Attend the Earliest Deadline**: If the min-heap is not empty, attend the event with the smallest `endDay` (earliest deadline) and remove it from the heap. Increment the count of attended events.
4. **Complexity**:
   - **Time**: $O(N \log N + \max(\text{day}) \log N)$, where $N$ is the number of events. Sorting takes $O(N \log N)$, and heap operations take $O(\log N)$.
   - **Space**: $O(N)$ to store events in the priority queue."""
    
    answer = """import heapq

def maxEvents(events):
    # Sort events by starting day
    events.sort()
    n = len(events)
    res = 0
    i = 0
    min_heap = []
    
    # Iterate through each potential day
    # Or more efficiently, iterate from the earliest start day to the latest end day
    curr_day = events[0][0]
    while i < n or min_heap:
        # If heap empty, jump to the next event's start day
        if not min_heap:
            curr_day = events[i][0]
            
        # Add all events starting on curr_day
        while i < n and events[i][0] <= curr_day:
            heapq.heappush(min_heap, events[i][1])
            i += 1
            
        # Remove events that already ended before curr_day
        while min_heap and min_heap[0] < curr_day:
            heapq.heappop(min_heap)
            
        # Attend the event ending soonest
        if min_heap:
            heapq.heappop(min_heap)
            res += 1
            curr_day += 1
            
    return res"""

    boilerplate = {
        "python": "import sys, json\n\ndef maxEvents(events):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        events = json.loads(data)\n        print(maxEvents(events))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n\nusing namespace std;\n\nint maxEvents(vector<vector<int>>& events) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input;\n    if (getline(cin, input)) {\n        string cleaned = \"\";\n        for (char c : input) {\n            if (c != '[' && c != ']' && c != ' ') cleaned += c;\n        }\n        vector<vector<int>> events;\n        if (!cleaned.empty()) {\n            stringstream ss(cleaned);\n            string item;\n            vector<int> flat;\n            while (getline(ss, item, ',')) {\n                flat.push_back(stoi(item));\n            }\n            for (size_t i = 0; i < flat.size(); i += 2) {\n                events.push_back({flat[i], flat[i+1]});\n            }\n        }\n        cout << maxEvents(events) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static int maxEvents(int[][] events) {\n        // User logic here\n        return 0;\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String input = sc.nextLine();\n            input = input.replaceAll(\"\\\\[\", \"\").replaceAll(\"\\\\]\", \"\").replaceAll(\"\\\\s+\", \"\");\n            if (input.isEmpty()) {\n                System.out.println(maxEvents(new int[0][0]));\n                return;\n            }\n            String[] nums = input.split(\",\");\n            int n = nums.length / 2;\n            int[][] events = new int[n][2];\n            for (int i = 0; i < n; i++) {\n                events[i][0] = Integer.parseInt(nums[2 * i]);\n                events[i][1] = Integer.parseInt(nums[2 * i + 1]);\n            }\n            System.out.println(maxEvents(events));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maxEvents(events) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nif (input) {\n    const events = JSON.parse(input);\n    console.log(maxEvents(events));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint maxEvents(int** events, int eventsSize, int* eventsColSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char input[1000000];\n    if (fgets(input, sizeof(input), stdin)) {\n        int cap = 1000, count = 0;\n        int* flat = (int*)malloc(cap * sizeof(int));\n        char* pt = input;\n        while (*pt != '\\0') {\n            if (isdigit(*pt) || (*pt == '-' && isdigit(*(pt+1)))) {\n                if (count >= cap) {\n                    cap *= 2;\n                    flat = (int*)realloc(flat, cap * sizeof(int));\n                }\n                flat[count++] = atoi(pt);\n                while (*pt != '\\0' && (isdigit(*pt) || *pt == '-')) pt++;\n            } else {\n                pt++;\n            }\n        }\n        int n = count / 2;\n        int** events = (int**)malloc(n * sizeof(int*));\n        int* colSizes = (int*)malloc(n * sizeof(int));\n        for (int i = 0; i < n; i++) {\n            events[i] = (int*)malloc(2 * sizeof(int));\n            events[i][0] = flat[2 * i];\n            events[i][1] = flat[2 * i + 1];\n            colSizes[i] = 2;\n        }\n        printf(\"%d\\n\", maxEvents(events, n, colSizes));\n        for (int i = 0; i < n; i++) free(events[i]);\n        free(events);\n        free(colSizes);\n        free(flat);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,2],[2,3],[3,4]]", "expected_output": "3", "is_sample": True},
        {"input": "[[1,2],[2,3],[3,4],[1,2]]", "expected_output": "4", "is_sample": True},
        {"input": "[[1,4],[4,4],[2,2],[3,4],[1,1]]", "expected_output": "4", "is_sample": False},
        {"input": "[[1,100000]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,1],[1,1],[1,1]]", "expected_output": "1", "is_sample": False},
        {"input": "[[1,5],[1,5],[1,5],[1,5],[1,5]]", "expected_output": "5", "is_sample": False},
        {"input": "[[1,1],[2,2],[3,3],[4,4],[5,5]]", "expected_output": "5", "is_sample": False},
        {"input": "[[1,2],[1,2],[3,3]]", "expected_output": "3", "is_sample": False},
        {"input": json.dumps([[i, i] for i in range(1, 10001)]), "expected_output": "10000", "is_sample": False}, # Stress Large
        {"input": json.dumps([[1, 10000]] * 10), "expected_output": "10", "is_sample": False}
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
        "topics": ["Array", "Greedy", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = "1201-1400/1353_Maximum_Number_of_Events_That_Can_Be_Attended.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
