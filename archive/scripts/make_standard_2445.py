import json
import os

def generate_json():
    problem_id = 2445
    title = "Number of Nodes With Value One"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>2445. Number of Nodes With Value One</h3>
<p>There is a <strong>complete binary tree</strong> with <code>n</code> nodes, labeled from <code>1</code> to <code>n</code>. For each node <code>v</code>, its left child is <code>2 * v</code> and its right child is <code>2 * v + 1</code>, if they exist.</p>

<p>Initially, all nodes have a value of <code>0</code>.</p>

<p>You are given an integer array <code>queries</code>. For each <code>queries[i]</code>, you should flip the values of all nodes in the <strong>subtree</strong> rooted at the node <code>queries[i]</code>.</p>

<p>Return <em>the total number of nodes with a value of <code>1</code> after all queries are made.</em></p>

<p>Flipping a value means changing <code>0</code> to <code>1</code> and <code>1</code> to <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/ex1.jpg" style="width: 250px; height: 161px;" />
<pre>
<strong>Input:</strong> n = 5, queries = [1,2,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The diagram above shows the tree after each query.
- Initially, all nodes are 0.
- Query 1: Flip subtree 1. Nodes {1,2,3,4,5} become 1.
- Query 2: Flip subtree 2. Nodes {2,4,5} become 0.
- Query 3: Flip subtree 5. Node {5} becomes 1.
Total nodes with value 1: {1,3,5} which is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/10/19/ex2.jpg" style="width: 100px; height: 81px;" />
<pre>
<strong>Input:</strong> n = 3, queries = [2,3,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The diagram above shows the tree after each query.
- Initially, all nodes are 0.
- Query 1: Flip subtree 2. Node {2} becomes 1.
- Query 2: Flip subtree 3. Node {3} becomes 1.
- Query 3: Flip subtree 3. Node {3} becomes 0.
Total nodes with value 1: {2} which is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries[i] &lt;= n</code></li>
</ul>
"""

    input_format = "An integer `n` and an integer array `queries` provided as `[n, queries]` in JSON."
    output_format = "An integer representing the total number of nodes with value 1."

    constraints = [
        "1 <= n <= 10^5",
        "1 <= queries.length <= 10^5",
        "1 <= queries[i] <= n"
    ]

    explanation = """To count nodes with value 1:
1. Flipping a subtree rooted at `u` is equivalent to adding 1 to the 'flip count' of all nodes in that subtree.
2. A node `v` will have value 1 if the sum of 'flip counts' of all its ancestors (including itself) is odd.
3. First, count how many times each node `u` was picked as a query root. Let this be `cnt[u]`.
4. Traverse the tree starting from the root (node 1).
5. For each node `v`, maintain the current path XOR sum from the root to `v`.
6. `current_xor_sum[v] = current_xor_sum[parent(v)] ^ (cnt[v] % 2)`.
7. If `current_xor_sum[v] == 1`, increment the total count of 1s.
8. Recursively visit children `2*v` and `2*v + 1` if they are <= `n`."""

    answer = """class Solution:
    def numberOfNodes(self, n: int, queries: list[int]) -> int:
        flip_counts = [0] * (n + 1)
        for q in queries:
            flip_counts[q] += 1
            
        res = 0
        current_state = [0] * (n + 1)
        
        for i in range(1, n + 1):
            parent = i // 2
            current_state[i] = current_state[parent] ^ (flip_counts[i] % 2)
            if current_state[i] == 1:
                res += 1
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numberOfNodes(self, n: int, queries: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, queries = json.loads(raw)
        sol = Solution()
        print(sol.numberOfNodes(n, queries))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numberOfNodes(int n, vector<int>& queries) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0];
        vector<int> queries = j[1].get<vector<int>>();
        Solution sol;
        cout << sol.numberOfNodes(n, queries) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int numberOfNodes(int n, int[] queries) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (Integer) data[0];
            int[] queries = mapper.convertValue(data[1], int[].class);
            System.out.println(new Solution().numberOfNodes(n, queries));
        }
    }
}""",
        "javascript": """var numberOfNodes = function(n, queries) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, queries] = JSON.parse(input);
    console.log(numberOfNodes(n, queries));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int numberOfNodes(int n, int* queries, int queriesSize) {
    // User logic here
    return 0;
}

int main() {
    int n;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    if (scanf("%d", &n) == 1) {
        while ((c = getchar()) != EOF && c != '[');
        int cap = 1024, s = 0;
        int* queries = malloc(cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (s >= cap) { cap *= 2; queries = realloc(queries, cap * sizeof(int)); }
            scanf("%d", &queries[s++]);
        }
        printf("%d\\n", numberOfNodes(n, queries, s));
        free(queries);
    }
    return 0;
}"""
    }

    def solve(n, queries):
        cnt = [0] * (n + 1)
        for q in queries: cnt[q] += 1
        res = 0
        state = [0] * (n + 1)
        for i in range(1, n + 1):
            parent = i // 2
            state[i] = state[parent] ^ (cnt[i] % 2)
            if state[i] == 1: res += 1
        return res

    test_cases_data = [
        [5, [1,2,5]],      # Sample 1
        [3, [2,3,3]],      # Sample 2
        [1, [1]],          # Root only
        [1, [1,1]],        # Double flip
        [7, [1]],          # Full tree
        [7, [2,3]],        # Symmetric
        [10, [1,4,7,10]],  
        # Stress tests
        [100000, [1]*100000],
        [100000, list(range(1, 100001))],
        [100000, [i for i in range(1, 100001, 2)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1]))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Tree", "Binary Tree", "Breadth-First Search", "Depth-First Search"], "companyIndex": 0
    }

    output_path = f"2401-2600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
