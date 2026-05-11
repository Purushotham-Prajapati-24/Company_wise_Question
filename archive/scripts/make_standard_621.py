import json
import os

def generate_json():
    problem_id = 621
    title = "Task Scheduler"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>621. Task Scheduler</h3>
<p>You are given an array of CPU <code>tasks</code>, each labeled with a letter from A to Z, and a number <code>n</code>. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there is a constraint: there has to be a gap of <strong>at least</strong> <code>n</code> intervals between two tasks with the same label.</p>

<p>Return the <strong>minimum</strong> number of CPU intervals required to complete all tasks.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> tasks = ["A","A","A","B","B","B"], n = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> tasks = ["A","C","A","B","D","B"], n = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> A possible sequence is: A -&gt; B -&gt; C -&gt; A -&gt; D -&gt; B.
With a cooling interval of 1, you can repeat A after just one other task has been completed.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> tasks = ["A","A","A","B","C","D","E","F","G","H","I","J","K"], n = 50
<strong>Output:</strong> 104
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= tasks.length &lt;= 10<sup>4</sup></code></li>
    <li><code>tasks[i]</code> is an uppercase English letter.</li>
    <li><code>0 &lt;= n &lt;= 100</code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array of characters (tasks).\nLine 2: Integer n."
    output_format = "An integer: the minimum number of CPU intervals."

    constraints = [
        "1 <= tasks.length <= 10^4",
        "tasks[i] is uppercase English letter",
        "0 <= n <= 100"
    ]

    explanation = """The key insight: let f = frequency of the most common task. We can form (f-1) blocks of (n+1) intervals each, plus a final block. The answer is max(len(tasks), (f-1)*(n+1) + (number of tasks with frequency == f))."""

    answer = """from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        tasks = json.loads(raw[0])
        n = int(raw[1])
        sol = Solution()
        print(sol.leastInterval(tasks, n))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // User logic here
        return 0;
    }
};

int main() {
    string t_str, n_str;
    if (getline(cin, t_str) && getline(cin, n_str)) {
        vector<char> tasks;
        for (char c : t_str)
            if (c >= 'A' && c <= 'Z') tasks.push_back(c);
        int n = stoi(n_str);
        Solution sol;
        cout << sol.leastInterval(tasks, n) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String t_str = sc.nextLine().trim();
            if (sc.hasNextInt()) {
                int n = sc.nextInt();
                List<Character> taskList = new ArrayList<>();
                for (char c : t_str.toCharArray())
                    if (c >= 'A' && c <= 'Z') taskList.add(c);
                char[] tasks = new char[taskList.size()];
                for (int i = 0; i < tasks.length; i++) tasks[i] = taskList.get(i);
                Solution sol = new Solution();
                System.out.println(sol.leastInterval(tasks, n));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const tasks = JSON.parse(input[0]);
    const n = parseInt(input[1], 10);
    console.log(leastInterval(tasks, n));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int leastInterval(char* tasks, int tasksSize, int n) {
    // User logic here
    return 0;
}

int main() {
    char t_str[100000];
    if (fgets(t_str, sizeof(t_str), stdin)) {
        char tasks[10000];
        int size = 0;
        for (int i = 0; t_str[i]; i++)
            if (t_str[i] >= 'A' && t_str[i] <= 'Z')
                tasks[size++] = t_str[i];
        int n;
        if (scanf("%d", &n) == 1)
            printf("%d\\n", leastInterval(tasks, size, n));
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '["A","A","A","B","B","B"]\\n2', "expected_output": "8", "is_sample": True},
        {"input": '["A","C","A","B","D","B"]\\n1', "expected_output": "6", "is_sample": True},
        {"input": '["A","A","A","B","B","B"]\\n0', "expected_output": "6", "is_sample": False},
        {"input": '["A","B","C","D","E","F"]\\n2', "expected_output": "6", "is_sample": False},
        {"input": '["A","A","A","A","A","A","B","C","D","E","F","G"]\\n2', "expected_output": "16", "is_sample": False},
        {"input": '["A","A","A","B","C","D","E","F","G","H","I","J","K"]\\n50', "expected_output": "104", "is_sample": False},
        {"input": '["A"]\\n0', "expected_output": "1", "is_sample": False},
        {"input": '["A","A","A","A","A","A","A","A","A","A"]\\n100', "expected_output": "910", "is_sample": False},
        {"input": '["A","A","B","B","C","C","D","D","E","E"]\\n5', "expected_output": "10", "is_sample": False},
        {"input": '["A","A","A","A","B","B","B","B","C","C","C","C"]\\n3', "expected_output": "12", "is_sample": False}
    ]

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
        "topics": ["Array", "Hash Table", "Greedy", "Sorting", "Heap (Priority Queue)", "Counting"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
