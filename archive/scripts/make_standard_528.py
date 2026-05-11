import json
import os

def generate_json():
    problem_id = 528
    title = "Random Pick with Weight"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>528. Random Pick with Weight</h3>
<p>You are given a <strong>0-indexed</strong> array of positive integers <code>w</code> where <code>w[i]</code> describes the <strong>weight</strong> of the <code>i<sup>th</sup></code> index.</p>

<p>You need to implement the function <code>pickIndex()</code>, which <strong>randomly</strong> picks an index in the range <code>[0, w.length - 1]</code> (<strong>inclusive</strong>) and returns it. The <strong>probability</strong> of picking an index <code>i</code> is <code>w[i] / sum(w)</code>.</p>

<ul>
    <li>For example, if <code>w = [1, 3]</code>, the probability of picking index <code>0</code> is <code>1 / (1 + 3) = 0.25</code> (i.e., <code>25%</code>), and the probability of picking index <code>1</code> is <code>3 / (1 + 3) = 0.75</code> (i.e., <code>75%</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["Solution","pickIndex"]
[[[1]],[]]
<strong>Output:</strong> [null,0]
<strong>Explanation:</strong>
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is index 0,since there is only one element in w.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong>
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
<strong>Output:</strong> [null,1,1,1,1,0]
<strong>Explanation:</strong> The probability of picking index 0 is 1/4 = 25%, and index 1 is 3/4 = 75%.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= w.length &lt;= 10<sup>4</sup></code></li>
    <li><code>1 &lt;= w[i] &lt;= 10<sup>5</sup></code></li>
    <li><code>pickIndex</code> will be called at most <code>10<sup>4</sup></code> times.</li>
</ul>"""

    input_format = "Two lines: Line 1: A JSON array of positive integers `w`. Line 2: An integer `n` (number of pickIndex calls)."
    output_format = "A JSON array of returned indices from each pickIndex call (non-deterministic but statistically valid)."

    constraints = [
        "1 <= w.length <= 10^4",
        "1 <= w[i] <= 10^5",
        "pickIndex will be called at most 10^4 times"
    ]

    explanation = """Build a prefix sum array from `w`. For each pickIndex call, generate a random number in [1, total_sum] and binary search in the prefix sum array to find the target index. This ensures each index is chosen with probability proportional to its weight."""

    answer = """import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)"""

    boilerplate = {
        "python": """import sys
import json
import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        # User logic here
        self.prefix = []

    def pickIndex(self) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        w = json.loads(raw[0])
        n = int(raw[1].strip())
        sol = Solution(w)
        results = [sol.pickIndex() for _ in range(n)]
        print(json.dumps(results))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>

using namespace std;

class Solution {
public:
    Solution(vector<int>& w) {
        // User logic here
    }
    int pickIndex() {
        // User logic here
        return 0;
    }
};

int main() {
    string w_str, n_str;
    if (getline(cin, w_str) && getline(cin, n_str)) {
        vector<int> w;
        size_t p = 0;
        while (p < w_str.length()) {
            if (isdigit(w_str[p])) {
                size_t next;
                w.push_back(stoi(w_str.substr(p), &next));
                p += next;
            } else {
                p++;
            }
        }
        int n = stoi(n_str);
        Solution sol(w);
        cout << "[";
        for (int i = 0; i < n; i++) {
            if (i > 0) cout << ",";
            cout << sol.pickIndex();
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public Solution(int[] w) {
        // User logic here
    }
    public int pickIndex() {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
            List<Integer> list = new ArrayList<>();
            if (!raw.isEmpty()) {
                for (String p : raw.split(",")) list.add(Integer.parseInt(p.trim()));
            }
            int[] w = new int[list.size()];
            for (int i = 0; i < list.size(); i++) w[i] = list.get(i);
            int n = sc.hasNextInt() ? sc.nextInt() : 1;
            Solution sol = new Solution(w);
            System.out.print("[");
            for (int i = 0; i < n; i++) {
                if (i > 0) System.out.print(",");
                System.out.print(sol.pickIndex());
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} w
 */
var Solution = function(w) {
    // User logic here
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function() {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const w = JSON.parse(input[0]);
    const n = parseInt(input[1], 10);
    const sol = new Solution(w);
    const results = [];
    for (let i = 0; i < n; i++) results.push(sol.pickIndex());
    console.log(JSON.stringify(results));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

typedef struct {
    int* prefix;
    int total;
    int size;
} Solution;

Solution* solutionCreate(int* w, int wSize) {
    // User logic here
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->prefix = NULL;
    obj->total = 0;
    obj->size = 0;
    return obj;
}

int solutionPickIndex(Solution* obj) {
    // User logic here
    return 0;
}

void solutionFree(Solution* obj) {
    if (obj->prefix) free(obj->prefix);
    free(obj);
}

int main() {
    srand((unsigned)time(NULL));
    char input[500000];
    if (fgets(input, sizeof(input), stdin)) {
        int capacity = 10;
        int* w = (int*)malloc(capacity * sizeof(int));
        int size = 0;
        int i = 0;
        while (input[i] != '\\0' && input[i] != '\\n') {
            if (isdigit(input[i])) {
                int val;
                int offset = 0;
                sscanf(input + i, "%d%n", &val, &offset);
                if (offset == 0) { i++; continue; }
                if (size == capacity) {
                    capacity *= 2;
                    w = (int*)realloc(w, capacity * sizeof(int));
                }
                w[size++] = val;
                i += offset;
            } else {
                i++;
            }
        }
        int n;
        if (scanf("%d", &n) == 1) {
            Solution* sol = solutionCreate(w, size);
            printf("[");
            for (int j = 0; j < n; j++) {
                if (j > 0) printf(",");
                printf("%d", solutionPickIndex(sol));
            }
            printf("]\\n");
            solutionFree(sol);
        }
        free(w);
    }
    return 0;
}"""
    }

    # Note: pickIndex is random. Test cases use a fixed seed or check valid range.
    # For evaluation, the expected_output lists valid indices (any valid index is accepted).
    test_cases = [
        # Two Leetcode Samples (deterministic: single element always returns 0)
        {"input": "[1]\\n1", "expected_output": "[0]", "is_sample": True},
        {"input": "[1,3]\\n1", "expected_output": "[0,1]", "is_sample": True},

        # Five Diverse Cases
        {"input": "[1,1]\\n1", "expected_output": "[0,1]", "is_sample": False},
        {"input": "[5]\\n3", "expected_output": "[0,0,0]", "is_sample": False},
        {"input": "[1,2,3]\\n1", "expected_output": "[0,1,2]", "is_sample": False},
        {"input": "[10,10,10]\\n1", "expected_output": "[0,1,2]", "is_sample": False},
        {"input": "[100000]\\n1", "expected_output": "[0]", "is_sample": False},

        # Three Stress Test Cases
        {"input": "[" + ",".join(["1"] * 10000) + "]\\n1", "expected_output": "[0]", "is_sample": False},
        {"input": "[" + ",".join(["100000"] * 10000) + "]\\n1", "expected_output": "[0]", "is_sample": False},
        {"input": "[1,99999]\\n1", "expected_output": "[0,1]", "is_sample": False}
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Math", "Binary Search", "Prefix Sum", "Randomized"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
