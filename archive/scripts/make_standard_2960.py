import json
import os

def generate_json():
    problem_id = 2960
    title = "Count Tested Devices After Test Operations"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>2960. Count Tested Devices After Test Operations</h3>
<p>You are given a <strong>0-indexed</strong> integer array <code>batteryPercentages</code> having length <code>n</code>, representing the battery percentages of <code>n</code> devices.</p>

<p>Your goal is to test these devices in the order <code>0</code> to <code>n - 1</code>, by performing the following test operations:</p>

<ul>
	<li>For each device <code>i</code> in range <code>[0, n - 1]</code>:
	<ul>
		<li>If <code>batteryPercentages[i] &gt; 0</code>:
		<ul>
			<li>Increment the count of tested devices.</li>
			<li>Decrease the battery percentage of all devices with indices <code>j</code> from <code>i + 1</code> to <code>n - 1</code> by <code>1</code>, ensuring their battery percentage never goes below <code>0</code>, i.e, <code>batteryPercentages[j] = max(0, batteryPercentages[j] - 1)</code>.</li>
			<li>Move to the next device.</li>
		</ul>
		</li>
		<li>Otherwise, move to the next device without performing any test.</li>
	</ul>
	</li>
</ul>

<p>Return <em>an integer representing the number of devices that will be tested after performing the test operations in order.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> batteryPercentages = [1,1,2,1,3]
<strong>Output:</strong> 3
<strong>Explanation: </strong>Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] &gt; 0, so there is now 1 tested device, and batteryPercentages becomes [1,0,1,0,2].
At device 1, batteryPercentages[1] == 0, so no test is performed and batteryPercentages remains the same.
At device 2, batteryPercentages[2] &gt; 0, so there are now 2 tested devices, and batteryPercentages becomes [1,0,1,0,1].
At device 3, batteryPercentages[3] == 0, so no test is performed and batteryPercentages remains the same.
At device 4, batteryPercentages[4] &gt; 0, so there are now 3 tested devices, and batteryPercentages becomes [1,0,1,0,0].
Hence, the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> batteryPercentages = [0,1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] == 0, so no test is performed and batteryPercentages remains the same.
At device 1, batteryPercentages[1] &gt; 0, so there is now 1 tested device, and batteryPercentages becomes [0,1,1].
At device 2, batteryPercentages[2] &gt; 0, so there are now 2 tested devices, and batteryPercentages becomes [0,1,0].
Hence, the answer is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == batteryPercentages.length &lt;= 100 </code></li>
	<li><code>0 &lt;= batteryPercentages[i] &lt;= 100</code></li>
</ul>
"""

    input_format = "An array of integers `batteryPercentages` provided as `[batteryPercentages]` or single array in JSON."
    output_format = "An integer representing the number of tested devices."

    constraints = [
        "1 <= batteryPercentages.length <= 100",
        "0 <= batteryPercentages[i] <= 100"
    ]

    explanation = """To count tested devices:
1. Initialize a counter `tested` to 0.
2. For each device `i` from 0 to `n-1`:
   - The actual battery percentage of device `i` is `batteryPercentages[i] - tested` (but not below 0).
   - If `batteryPercentages[i] - tested > 0`, increment `tested`.
3. Return `tested`."""

    answer = """class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        tested = 0
        for p in batteryPercentages:
            if p - tested > 0:
                tested += 1
        return tested"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        batteryPercentages = json.loads(raw)
        if isinstance(batteryPercentages[0], list): batteryPercentages = batteryPercentages[0]
        sol = Solution()
        print(sol.countTestedDevices(batteryPercentages))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countTestedDevices(vector<int>& batteryPercentages) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> batteryPercentages;
        if (j.is_array() && j.size() > 0 && j[0].is_array()) batteryPercentages = j[0].get<vector<int>>();
        else batteryPercentages = j.get<vector<int>>();
        Solution sol;
        cout << sol.countTestedDevices(batteryPercentages) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            int[] batteryPercentages;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                batteryPercentages = mapper.convertValue(((List)raw).get(0), int[].class);
            } else {
                batteryPercentages = mapper.convertValue(raw, int[].class);
            }
            System.out.println(new Solution().countTestedDevices(batteryPercentages));
        }
    }
}""",
        "javascript": """var countTestedDevices = function(batteryPercentages) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let batteryPercentages = JSON.parse(input);
    if (Array.isArray(batteryPercentages[0])) batteryPercentages = batteryPercentages[0];
    console.log(countTestedDevices(batteryPercentages));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int countTestedDevices(int* batteryPercentages, int batteryPercentagesSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* batteryPercentages = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; batteryPercentages = realloc(batteryPercentages, cap * sizeof(int)); }
        scanf("%d", &batteryPercentages[s++]);
    }
    printf("%d\\n", countTestedDevices(batteryPercentages, s));
    free(batteryPercentages);
    return 0;
}"""
    }

    def solve(batteryPercentages):
        tested = 0
        for p in batteryPercentages:
            if p - tested > 0:
                tested += 1
        return tested

    test_cases_data = [
        [[1,1,2,1,3]],     # Sample 1
        [[0,1,2]],         # Sample 2
        [[1,1,1,1,1]],
        [[5,4,3,2,1]],
        [[0,0,0,0,0]],
        [[100]],
        [[1,0,1,0,1]],
        # Stress tests
        [[100]*100],
        [[i for i in range(100)]],
        [[i%2 for i in range(100)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Simulation"], "companyIndex": 0
    }

    output_path = f"2801-3000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
