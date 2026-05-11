import json
import os

def generate_json():
    problem_id = 582
    title = "Kill Process"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>582. Kill Process</h3>
<p>You have <code>n</code> processes forming a rooted tree structure. You are given two integer arrays <code>pid</code> and <code>ppid</code>, where <code>pid[i]</code> is the ID of the <code>i<sup>th</sup></code> process and <code>ppid[i]</code> is the ID of the <code>i<sup>th</sup></code> process's parent process.</p>

<p>Each process has only one parent process, but may have one or more children processes. Only one process has <code>ppid[i] = 0</code>, which means this process has no parent process (the root of the tree).</p>

<p>When a process is killed, all of its children processes will be killed. No order is required for the final answer.</p>

<p>Given an integer <code>kill</code> representing the ID of a process you want to kill, return <em>a list of the IDs of the processes that will be killed. You may return the answer in <strong>any order</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
<strong>Output:</strong> [5,10]
<strong>Explanation:</strong>&nbsp;
           3
         /   \\
        1     5
             /
            10
Kill 5 will also kill 10.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> pid = [1], ppid = [0], kill = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == pid.length</code></li>
    <li><code>n == ppid.length</code></li>
    <li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= pid[i] &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>0 &lt;= ppid[i] &lt;= 5 * 10<sup>4</sup></code></li>
    <li>Only one process has no parent (i.e., <code>ppid[i] == 0</code>).</li>
    <li>All the values of <code>pid</code> are <strong>unique</strong>.</li>
    <li><code>kill</code> is <strong>guaranteed</strong> to be in <code>pid</code>.</li>
</ul>"""

    input_format = "Three lines:\nLine 1: JSON array `pid`.\nLine 2: JSON array `ppid`.\nLine 3: Integer `kill`."
    output_format = "A JSON array of killed processes."

    constraints = [
        "1 <= n <= 5 * 10^4",
        "1 <= pid[i] <= 5 * 10^4",
        "0 <= ppid[i] <= 5 * 10^4",
        "All values of pid are unique"
    ]

    explanation = """Build a hash map (adjacency list) mapping each parent ID to a list of its children IDs. Then, use Breadth-First Search (BFS) or Depth-First Search (DFS) starting from the `kill` node to collect all reachable descendants."""

    answer = """from collections import defaultdict, deque
class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)
            
        res = []
        q = deque([kill])
        while q:
            curr = q.popleft()
            res.append(curr)
            for child in tree[curr]:
                q.append(child)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 3:
        pid = json.loads(raw[0])
        ppid = json.loads(raw[1])
        kill = int(raw[2])
        sol = Solution()
        ans = sol.killProcess(pid, ppid, kill)
        ans.sort()
        print(json.dumps(ans))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        // User logic here
        return {};
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t p = 0;
    while (p < input.length()) {
        if (input[p] == '-' || isdigit(input[p])) {
            size_t next;
            res.push_back(stoi(input.substr(p), &next));
            p += next;
        } else p++;
    }
    return res;
}

int main() {
    string p_str, pp_str, k_str;
    if (getline(cin, p_str) && getline(cin, pp_str) && getline(cin, k_str)) {
        vector<int> pid = parseArray(p_str);
        vector<int> ppid = parseArray(pp_str);
        int kill = stoi(k_str);
        Solution sol;
        vector<int> ans = sol.killProcess(pid, ppid, kill);
        sort(ans.begin(), ans.end());
        cout << "[";
        for (size_t i = 0; i < ans.size(); i++) {
            cout << ans[i] << (i + 1 == ans.size() ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    static List<Integer> parseArray(String raw) {
        List<Integer> res = new ArrayList<>();
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        if (!raw.isEmpty()) {
            for (String p : raw.split(",")) res.add(Integer.parseInt(p.trim()));
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String p_str = sc.nextLine().trim();
            if (sc.hasNextLine()) {
                String pp_str = sc.nextLine().trim();
                List<Integer> pid = parseArray(p_str);
                List<Integer> ppid = parseArray(pp_str);
                if (sc.hasNextInt()) {
                    int kill = sc.nextInt();
                    Solution sol = new Solution();
                    List<Integer> ans = sol.killProcess(pid, ppid, kill);
                    Collections.sort(ans);
                    System.out.print("[");
                    for (int i = 0; i < ans.size(); i++) {
                        System.out.print(ans.get(i) + (i + 1 == ans.size() ? "" : ","));
                    }
                    System.out.println("]");
                }
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} pid
 * @param {number[]} ppid
 * @param {number} kill
 * @return {number[]}
 */
var killProcess = function(pid, ppid, kill) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 3) {
    const pid = JSON.parse(input[0]);
    const ppid = JSON.parse(input[1]);
    const kill = parseInt(input[2], 10);
    const ans = killProcess(pid, ppid, kill);
    ans.sort((a,b)=>a-b);
    console.log(JSON.stringify(ans));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* killProcess(int* pid, int pidSize, int* ppid, int ppidSize, int kill, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int cmp(const void* a, const void* b) { return *(int*)a - *(int*)b; }

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '-' || isdigit(input[i])) {
            int val, off = 0;
            sscanf(input + i, "%d%n", &val, &off);
            if (!off) { i++; continue; }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
            res[size++] = val;
            i += off;
        } else i++;
    }
    *outSize = size;
    return res;
}

int main() {
    char p_str[500000], pp_str[500000], k_str[50];
    if (fgets(p_str, sizeof(p_str), stdin) && fgets(pp_str, sizeof(pp_str), stdin) && fgets(k_str, sizeof(k_str), stdin)) {
        int pidSize, ppidSize;
        int* pid = parseArray(p_str, &pidSize);
        int* ppid = parseArray(pp_str, &ppidSize);
        int kill;
        sscanf(k_str, "%d", &kill);
        int returnSize;
        int* ans = killProcess(pid, pidSize, ppid, ppidSize, kill, &returnSize);
        if (ans) qsort(ans, returnSize, sizeof(int), cmp);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("%d%s", ans[i], i + 1 == returnSize ? "" : ",");
        }
        printf("]\\n");
        if (ans) free(ans);
        free(pid);
        free(ppid);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,3,10,5]\\n[3,0,5,3]\\n5", "expected_output": "[5, 10]", "is_sample": True},
        {"input": "[1]\\n[0]\\n1", "expected_output": "[1]", "is_sample": True},
        {"input": "[1,3,10,5]\\n[3,0,5,3]\\n3", "expected_output": "[1, 3, 5, 10]", "is_sample": False},
        {"input": "[1,2,3,4,5]\\n[0,1,1,2,2]\\n1", "expected_output": "[1, 2, 3, 4, 5]", "is_sample": False},
        {"input": "[1,2,3,4,5]\\n[0,1,1,2,2]\\n2", "expected_output": "[2, 4, 5]", "is_sample": False},
        {"input": "[10,20,30,40,50]\\n[0,10,20,30,40]\\n30", "expected_output": "[30, 40, 50]", "is_sample": False},
        {"input": "[10,20,30,40,50]\\n[0,10,20,30,40]\\n50", "expected_output": "[50]", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(1, 20000)) + "]\\n[" + ",".join([str(i-1) for i in range(1, 20000)]) + "]\\n1", "expected_output": "[" + ", ".join(str(i) for i in range(1, 20000)) + "]", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(1, 20000)) + "]\\n[" + ",".join(["0", "1"] + ["2"] * 19997) + "]\\n2", "expected_output": "[" + ", ".join(str(i) for i in range(2, 20000)) + "]", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(1, 20000)) + "]\\n[" + ",".join(["0"] + ["1"] * 19998) + "]\\n1", "expected_output": "[" + ", ".join(str(i) for i in range(1, 20000)) + "]", "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Array", "Hash Table"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
