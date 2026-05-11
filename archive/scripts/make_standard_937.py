import json
import os

def generate_json():
    problem_id = 937
    title = "Reorder Data in Log Files"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>937. Reorder Data in Log Files</h3>
<p>You are given an array of <code>logs</code>. Each log is a space-delimited string of words, where the first word is the <strong>identifier</strong>.</p>

<p>There are two types of logs:</p>

<ul>
    <li><b>Letter-logs</b>: All words (except the identifier) consist of lowercase English letters.</li>
    <li><b>Digit-logs</b>: All words (except the identifier) consist of digits.</li>
</ul>

<p>Reorder these logs so that:</p>

<ol>
    <li>The <strong>letter-logs</strong> come before all <strong>digit-logs</strong>.</li>
    <li>The <strong>letter-logs</strong> are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.</li>
    <li>The <strong>digit-logs</strong> maintain their relative ordering.</li>
</ol>

<p>Return <em>the final order of the logs</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
<strong>Output:</strong> ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
<strong>Explanation:</strong>
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
<strong>Output:</strong> ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= logs.length &lt;= 100</code></li>
    <li><code>3 &lt;= logs[i].length &lt;= 100</code></li>
    <li>All the tokens of <code>logs[i]</code> are separated by a single space.</li>
    <li><code>logs[i]</code> is guaranteed to have an identifier and at least one word after the identifier.</li>
</ul>"""

    input_format = "A single line containing the JSON array `logs`."
    output_format = "A JSON array representing the reordered logs."

    constraints = [
        "1 <= logs.length <= 100",
        "3 <= logs[i].length <= 100",
        "At least one word after identifier"
    ]

    explanation = """Separate the logs into two lists: letter-logs and digit-logs. For letter-logs, use a custom sort key that first considers the content (everything after the identifier) and then the identifier itself. Digit-logs should maintain their original order. Finally, concatenate the sorted letter-logs and the digit-logs in their original order."""

    answer = """class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def get_key(log):
            id_, content = log.split(" ", 1)
            return (0, content, id_) if content[0].isalpha() else (1,)

        return sorted(logs, key=get_key)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        logs = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.reorderLogFiles(logs)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> logs;
        size_t start = line.find('[');
        size_t end = line.find_last_of(']');
        if (start != string::npos && end != string::npos) {
            string content = line.substr(start + 1, end - start - 1);
            size_t pos = 0;
            while ((pos = content.find('"')) != string::npos) {
                content.erase(0, pos + 1);
                pos = content.find('"');
                logs.push_back(content.substr(0, pos));
                content.erase(0, pos + 1);
            }
        }
        Solution sol;
        auto res = sol.reorderLogFiles(logs);
        cout << "[";
        for (int i=0; i<res.size(); ++i) cout << "\\"" << res[i] << "\\"" << (i==res.size()-1 ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        // User logic here
        return new String[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            line = line.substring(1, line.length()-1);
            String[] logs = line.split("\\",\\"");
            for (int i=0; i<logs.length; i++) logs[i] = logs[i].replace("\\"", "");
            Solution sol = new Solution();
            String[] res = sol.reorderLogFiles(logs);
            System.out.println(Arrays.toString(res).replace(", ", ","));
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(reorderLogFiles(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** reorderLogFiles(char** logs, int logsSize, int* returnSize) {
    // User logic here
    *returnSize = logsSize;
    return logs;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        printf("[]\\n");
    }
    return 0;
}"""
    }

    def solve(logs):
        def get_key(log):
            id_, content = log.split(" ", 1)
            return (0, content, id_) if content[0].isalpha() else (1,)
        return sorted(logs, key=get_key)

    test_cases_data = [
        ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
        ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
        ["let1 art can", "let1 art can"],
        ["dig1 1", "dig2 2", "dig3 3"],
        ["let1 a", "let2 a", "let1 b"],
        ["let1 a b c", "dig1 1 2 3", "let2 a b c"],
        ["a1 2 3", "a1 b c"],
        ["1 2 3", "a b c"],
        ["let1 art can", "let2 art can", "let3 art can"],
        ["z x y", "a b c", "1 2 3"]
    ]

    test_cases = []
    for i, logs in enumerate(test_cases_data):
        inp = json.dumps(logs).replace(" ", "")
        out = json.dumps(solve(logs)).replace(" ", "")
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
        "topics": ["Array", "String", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
