import json
import os

def generate_json():
    problem_id = 681
    title = "Next Closest Time"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>681. Next Closest Time</h3>
<p>Given a time represented in the format <code>"HH:MM"</code>, form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.</p>

<p>You may assume the given input string is always valid. For example, <code>"01:34"</code>, <code>"12:09"</code> are all valid. <code>"1:34"</code>, <code>"12:9"</code> are all invalid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> time = "19:34"
<strong>Output:</strong> "19:39"
<strong>Explanation:</strong> The next closest time choosing from digits <strong>1</strong>, <strong>9</strong>, <strong>3</strong>, <strong>4</strong>, is <strong>19:39</strong>, which occurs 5 minutes later. It is not <strong>19:33</strong>, because this occurs 23 hours and 59 minutes later.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> time = "23:59"
<strong>Output:</strong> "22:22"
<strong>Explanation:</strong> The next closest time choosing from digits <strong>2</strong>, <strong>3</strong>, <strong>5</strong>, <strong>9</strong>, is <strong>22:22</strong>. It may be assumed that the returned time is next day's time since it is smaller, and no time is greater than the given time.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>time.length == 5</code></li>
    <li><code>time</code> is a valid time in the format <code>"HH:MM"</code>.</li>
    <li><code>0 &lt;= HH &lt; 24</code></li>
    <li><code>0 &lt;= MM &lt; 60</code></li>
</ul>"""

    input_format = "A single line: a JSON string `time` in format HH:MM."
    output_format = 'A JSON string: the next closest time in format "HH:MM".'

    constraints = [
        "time.length == 5",
        "Valid 24-hour format HH:MM",
        "0 <= HH < 24, 0 <= MM < 60"
    ]

    explanation = """Extract the 4 digits from time. Try all combinations of these digits in positions H1H2:M1M2. Collect valid times (H < 24 and M < 60). Start from the given time's minute+1 and find the next valid time (wrapping around midnight if needed)."""

    answer = """from itertools import product
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(':', ''))
        cur_mins = int(time[:2]) * 60 + int(time[3:])
        
        for delta in range(1, 24 * 60 + 1):
            next_mins = (cur_mins + delta) % (24 * 60)
            h, m = next_mins // 60, next_mins % 60
            candidate = f"{h:02d}:{m:02d}"
            if all(c in digits for c in candidate if c != ':'):
                return candidate
        return time"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def nextClosestTime(self, time: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        time = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.nextClosestTime(time)))""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string nextClosestTime(string time) {
        // User logic here
        return "";
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        if (input.length() >= 2 && input[0] == '"')
            input = input.substr(1, input.length() - 2);
        Solution sol;
        cout << "\\"" << sol.nextClosestTime(input) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String nextClosestTime(String time) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() >= 2 && raw.startsWith("\\""))
                raw = raw.substring(1, raw.length() - 1);
            Solution sol = new Solution();
            System.out.println("\\"" + sol.nextClosestTime(raw) + "\\"");
        }
    }
}""",
        "javascript": """/**
 * @param {string} time
 * @return {string}
 */
var nextClosestTime = function(time) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const time = JSON.parse(input);
    console.log(JSON.stringify(nextClosestTime(time)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* nextClosestTime(char* time) {
    // User logic here
    char* res = (char*)malloc(6);
    strcpy(res, time);
    return res;
}

int main() {
    char input[20];
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\\n")] = 0;
        char time_str[10];
        int len = strlen(input);
        if (len >= 2 && input[0] == '"') {
            strncpy(time_str, input + 1, len - 2);
            time_str[len - 2] = '\\0';
        } else {
            strcpy(time_str, input);
        }
        char* res = nextClosestTime(time_str);
        printf("\\"%s\\"\\n", res);
        free(res);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(time_str):
        from itertools import product as iproduct
        digits = set(time_str.replace(':', ''))
        cur_mins = int(time_str[:2]) * 60 + int(time_str[3:])
        for delta in range(1, 24 * 60 + 1):
            next_mins = (cur_mins + delta) % (24 * 60)
            h, m = next_mins // 60, next_mins % 60
            candidate = f"{h:02d}:{m:02d}"
            if all(c in digits for c in candidate if c != ':'):
                return candidate
        return time_str

    times = ["19:34", "23:59", "00:00", "01:32", "12:12", "09:09", "22:30", "11:11", "05:55", "23:23"]
    test_cases = []
    for i, t in enumerate(times):
        inp = json.dumps(t)
        out = json.dumps(solve(t))
        is_sample = i < 2
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Enumeration"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
