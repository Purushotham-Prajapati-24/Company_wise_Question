import json
import os

def generate_json():
    problem_id = 2612
    title = "Minimum Reverse Operations"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>2612. Minimum Reverse Operations</h3>
<p>You are given an integer <code>n</code> and an integer <code>p</code> which represents the initial position of a <strong>1</strong> in a <strong>0-indexed</strong> array of length <code>n</code>. All other elements are <code>0</code>.</p>

<p>You are also given an integer array <code>banned</code> containing indices that you cannot occupy. All indices in <code>banned</code> initially contain <code>0</code>, and <code>p</code> is <strong>not</strong> in <code>banned</code>.</p>

<p>In one operation, you can choose a <strong>subarray</strong> of size <code>k</code> such that the <code>1</code> is currently in that subarray, and <strong>reverse</strong> the subarray. The <code>1</code> will then be at its new position after the reverse.</p>

<p>Return <em>an integer array</em> <code>ans</code> <em>of length</em> <code>n</code> <em>where</em> <code>ans[i]</code> <em>is the <strong>minimum</strong> number of operations to bring the 1 to position</em> <code>i</code><em>, or </em><code>-1</code><em> if it is impossible.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, p = 0, banned = [1,2], k = 4
<strong>Output:</strong> [0,-1,-1,1]
<strong>Explanation:</strong> Initially 1 is at [0,0,0,0], but 1 is at index 0. Banned are [1,2]. 
After 1st reverse of size 4 subarray [0,1,2,3], 1 moves from 0 to 3. 
Final pos 3 is reached in 1 move. Pos 1 and 2 are banned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, p = 0, banned = [2,4], k = 3
<strong>Output:</strong> [0,-1,1,-1,-1]
<strong>Explanation:</strong> 
- Initially 1 is at pos 0.
- Reverse subarrays of size 3 containing index 0: [0,1,2]. Pos 0 moves to pos 2, but 2 is banned.
- Wait, subarrays containing 0 of size 3 is only [0,1,2]. Reversing [0,1,2] moves 0 to 2.
- In this case only pos 2 is reachable from 0 in 1 move, but since 2 is banned, it is unreachable.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= p &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned.length &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned[i] &lt;= n - 1</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li><code>p</code> is not in <code>banned</code>.</li>
	<li>All values in <code>banned</code> are distinct.</li>
</ul>
"""

    input_format = "Integers `n`, `p`, an array `banned`, and an integer `k` provided as `[n, p, banned, k]` in JSON."
    output_format = "An array of integers representing minimum moves."

    constraints = [
        "1 <= n <= 10^5",
        "0 <= p < n",
        "1 <= k <= n"
    ]

    explanation = """To solve minimum reverse operations:
1. This is a Shortest Path problem on a graph where nodes are positions 0 to `n-1`. Use BFS.
2. For a position `i`, reversing a subarray of size `k` containing `i` moves the 1 to a new position `j`.
3. The possible values of `j` form a range. Specifically, if the subarray starts at `L` and ends at `L+k-1`, the new position after reverse is `j = (L + (L+k-1)) - i = 2L + k - 1 - i`.
4. As `L` varies such that the subarray contains `i` (i.e., `max(0, i-k+1) <= L <= min(i, n-k)`), the values of `j` form a range `[j_min, j_max]` where every second value in the range is reachable (sharing the same parity as `i + k - 1`).
5. Use two sets (or `SortedList` / balanced BST) to store unvisited nodes with even and odd indices separately for efficient range queries and removals during BFS."""

    answer = """from collections import deque
import bisect

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        banned_set = set(banned)
        unvisited = [set(), set()]
        for i in range(n):
            if i != p and i not in banned_set:
                unvisited[i % 2].add(i)
        
        # Using sorted lists to make range queries efficient
        # In Python, we can use a sorted list or just manually maintain a sorted array
        even_unvisited = sorted(list(unvisited[0]))
        odd_unvisited = sorted(list(unvisited[1]))
        avail = [even_unvisited, odd_unvisited]
        
        res = [-1] * n
        res[p] = 0
        q = deque([p])
        
        while q:
            curr = q.popleft()
            
            # Subarray [L, L+k-1] contains curr: max(0, curr-k+1) <= L <= min(curr, n-k)
            # New pos j = 2L + k - 1 - curr
            L_min = max(0, curr - k + 1)
            L_max = min(curr, n - k)
            j_min = 2 * L_min + k - 1 - curr
            j_max = 2 * L_max + k - 1 - curr
            
            p_idx = j_min % 2
            target_list = avail[p_idx]
            
            # Find all j in [j_min, j_max] in target_list
            idx_start = bisect.bisect_left(target_list, j_min)
            idx_end = bisect.bisect_right(target_list, j_max)
            
            to_remove = []
            for i in range(idx_start, idx_end):
                next_pos = target_list[i]
                res[next_pos] = res[curr] + 1
                q.append(next_pos)
                to_remove.append(next_pos)
                
            # Efficiently remove from target_list
            if to_remove:
                # Re-constructing list is slow if many removals, but target_list size decreases
                # For n=10^5, this is generally okay if nodes are visited once
                new_list = []
                # Actually, a better way is to delete them in reverse to preserve indices
                for i in range(idx_end - 1, idx_start - 1, -1):
                    target_list.pop(i)
        return res"""

    boilerplate = {
        "python": """import sys
import json
import bisect
from collections import deque

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        n, p, banned, k = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.minReverseOperations(n, p, banned, k)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        int n = j[0], p = j[1];
        vector<int> banned = j[2].get<vector<int>>();
        int k = j[3];
        Solution sol;
        vector<int> res = sol.minReverseOperations(n, p, banned, k);
        json out = res;
        cout << out.dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        // User logic here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int n = (Integer) data[0], p = (Integer) data[1];
            int[] banned = mapper.convertValue(data[2], int[].class);
            int k = (Integer) data[3];
            int[] res = new Solution().minReverseOperations(n, p, banned, k);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var minReverseOperations = function(n, p, banned, k) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [n, p, banned, k] = JSON.parse(input);
    console.log(JSON.stringify(minReverseOperations(n, p, banned, k)).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* minReverseOperations(int n, int p, int* banned, int bannedSize, int k, int* returnSize) {
    // User logic here
    return NULL;
}

int main() {
    int n, p, k;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    if (scanf("%d", &n) == 1) {
        while ((c = getchar()) != EOF && c != ',');
        scanf("%d", &p);
        while ((c = getchar()) != EOF && c != '[');
        int cap = 128, s = 0;
        int* banned = malloc(cap * sizeof(int));
        while (1) {
            while ((c = getchar()) != EOF && !isdigit(c) && c != ']');
            if (c == EOF || c == ']') break;
            ungetc(c, stdin);
            if (s >= cap) { cap *= 2; banned = realloc(banned, cap * sizeof(int)); }
            scanf("%d", &banned[s++]);
        }
        while ((c = getchar()) != EOF && c != ',');
        scanf("%d", &k);
        int retSize;
        int* res = minReverseOperations(n, p, banned, s, k, &retSize);
        printf("[");
        for (int i=0; i<retSize; i++) {
            printf("%d", res[i]);
            if (i < retSize - 1) printf(",");
        }
        printf("]\\n");
        free(banned); free(res);
    }
    return 0;
}"""
    }

    def solve(n, p, banned, k):
        import bisect
        from collections import deque
        bSet = set(banned)
        avail = [[], []]
        for i in range(n):
            if i != p and i not in bSet: avail[i%2].append(i)
        res = [-1] * n
        res[p] = 0
        q = deque([p])
        while q:
            curr = q.popleft()
            L_min = max(0, curr - k + 1)
            L_max = min(curr, n - k)
            j_min = 2 * L_min + k - 1 - curr
            j_max = 2 * L_max + k - 1 - curr
            target = avail[j_min % 2]
            l_idx = bisect.bisect_left(target, j_min)
            r_idx = bisect.bisect_right(target, j_max)
            for i in range(l_idx, r_idx):
                nxt = target[i]
                res[nxt] = res[curr] + 1
                q.append(nxt)
            if l_idx < r_idx: del target[l_idx:r_idx]
        return res

    test_cases_data = [
        [4, 0, [1,2], 4], # Sample 1
        [5, 0, [2,4], 3], # Sample 2
        [1, 0, [], 1],    # Single
        [10, 5, [], 2],   # No banned
        [10, 5, [0,1,2,3,4,6,7,8,9], 2], # All banned
        [4, 2, [0,1,3], 1], # k=1
        [10, 0, [], 10],   # k=n
        # Stress tests
        [100000, 0, [], 2],
        [100000, 50000, [], 100],
        [100000, 0, [i for i in range(2, 100000, 2)], 3]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1], t[2], t[3])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 512, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Breadth-First Search", "Ordered Set"], "companyIndex": 0
    }

    output_path = f"2601-2800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
