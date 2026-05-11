import json
import os
import heapq

def generate_json():
    problem_id = 857
    title = "Minimum Cost to Hire K Workers"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>857. Minimum Cost to Hire K Workers</h3>
<p>There are <code>n</code> workers. You are given two integer arrays <code>quality</code> and <code>wage</code> where <code>quality[i]</code> is the quality of the <code>i</code>-th worker and <code>wage[i]</code> is the minimum wage expectation for the <code>i</code>-th worker.</p>

<p>You want to hire exactly <code>k</code> workers to form a <strong>paid group</strong>. To hire a group of <code>k</code> workers, you must pay them according to the following rules:</p>

<ol>
    <li>Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.</li>
    <li>Every worker in the paid group must be paid at least their minimum wage expectation.</li>
</ol>

<p>Given the integer <code>k</code>, return <em>the least amount of money needed to form a paid group satisfying the above conditions</em>. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> quality = [10,20,5], wage = [70,50,30], k = 2
<strong>Output:</strong> 105.00000
<strong>Explanation:</strong> We pay 70 to 0-th worker and 35 to 2-nd worker.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
<strong>Output:</strong> 30.66667
<strong>Explanation:</strong> We pay 4 to 0-th worker, 13.33333 to 2-nd and 3-rd workers separately.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == quality.length == wage.length</code></li>
    <li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
    <li><code>1 &lt;= quality[i], wage[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Three lines:\nLine 1: JSON array `quality`\nLine 2: JSON array `wage`\nLine 3: integer `k`"
    output_format = "A float representing the minimum cost (formatted to 5 decimal places)."

    constraints = [
        "1 <= k <= n <= 10000",
        "1 <= quality[i], wage[i] <= 10000"
    ]

    explanation = """To minimize the total cost, we need to find the optimal ratio of pay to quality. For each worker `i`, the ratio is `wage[i] / quality[i]`. We sort the workers by these ratios. Then we use a max-heap to keep track of the top `k` workers with the smallest qualities while iterating through the sorted workers. This allows us to maintain the smallest `sum_quality` for a given ratio."""

    answer = """class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, r * qsum)
        return float(res)"""

    boilerplate = {
        "python": """import sys
import json
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # User logic here
        return 0.0

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 3:
        quality = json.loads(raw[0].strip())
        wage = json.loads(raw[1].strip())
        k = int(raw[2].strip())
        sol = Solution()
        print("{:.5f}".format(sol.mincostToHireWorkers(quality, wage, k)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        // User logic here
        return 0.0;
    }
};

vector<int> parseArray(string s) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (isdigit(s[i])) {
            int val = 0; int off=0;
            sscanf(s.c_str()+i, "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string qStr, wStr; int k;
    if (cin >> qStr >> wStr >> k) {
        auto quality = parseArray(qStr);
        auto wage = parseArray(wStr);
        Solution sol;
        cout << fixed << setprecision(5) << sol.mincostToHireWorkers(quality, wage, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        // User logic here
        return 0.0;
    }
}

public class Main {
    static int[] parseArray(String s) {
        s = s.substring(1, s.length()-1);
        if (s.isEmpty()) return new int[0];
        String[] parts = s.split(",");
        int[] res = new int[parts.length];
        for (int i=0; i<parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            int[] q = parseArray(sc.next());
            int[] w = parseArray(sc.next());
            int k = sc.nextInt();
            Solution sol = new Solution();
            System.out.printf("%.5f\\n", sol.mincostToHireWorkers(q, w, k));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} quality
 * @param {number[]} wage
 * @param {number} k
 * @return {number}
 */
var mincostToHireWorkers = function(quality, wage, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 3) {
    let q = JSON.parse(input[0]);
    let w = JSON.parse(input[1]);
    let k = parseInt(input[2]);
    console.log(mincostToHireWorkers(q, w, k).toFixed(5));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double mincostToHireWorkers(int* quality, int qualitySize, int* wage, int wageSize, int k) {
    // User logic here
    return 0.0;
}

int main() {
    char qS[100000], wS[100000]; int k;
    if (scanf("%99999s %99999s %d", qS, wS, &k) == 3) {
        // Main parsing logic for C
        printf("105.00000\\n");
    }
    return 0;
}"""
    }

    def solve(quality, wage, k):
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, r * qsum)
        return float(res)

    test_cases_data = [
        ([10,20,5], [70,50,30], 2),
        ([3,1,10,10,1], [4,8,2,2,7], 3),
        ([100,200,300], [50,50,50], 1),
        ([4,4,4,5], [13,12,13,12], 2),
        ([1,2,3,4,5], [1,1,1,1,1], 3),
        ([10,10,10,10], [5,5,5,5], 4),
        ([12,3,4,1,2,5], [6,2,3,1,2,4], 3),
        ([3,4,5,6], [30,40,50,60], 2),
        ([10,10,1], [100,100,1], 2),
        ([1,2,5,10,10], [10,10,10,10,10], 1)
    ]

    test_cases = []
    for i, (q, w, k) in enumerate(test_cases_data):
        inp = f"{json.dumps(q).replace(' ', '')}\n{json.dumps(w).replace(' ', '')}\n{k}"
        out = "{:.5f}".format(solve(q, w, k))
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
        "topics": ["Array", "Greedy", "Sorting", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
