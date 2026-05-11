import json
import os

def generate_json():
    problem_id = 1306
    title = "Jump Game III"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1306. Jump Game III</h3>
<p>Given an array of non-negative integers <code>arr</code>, you are initially positioned at <code>start</code>&nbsp;index of the array. When you are at index <code>i</code>, you can jump&nbsp;to <code>i + arr[i]</code> or <code>i - arr[i]</code>, check if you can reach to <strong>any</strong> index with value 0.</p>

<p>Notice that you can not jump outside of the array at any time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [4,2,3,0,3,1,2], start = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [4,2,3,0,3,1,2], start = 0
<strong>Output:</strong> true 
<strong>Explanation: 
</strong>index 0 -> index 4 -> index 1 -> index 3 
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [3,0,2,1,2], start = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>There is no way to reach at index 1 with value 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>0 &lt;= arr[i] &lt; arr.length</code></li>
    <li><code>0 &lt;= start &lt; arr.length</code></li>
</ul>"""

    input_format = "An array of non-negative integers `arr` and an integer `start` provided as `[arr, start]` in JSON."
    output_format = "A boolean representing if any index with value 0 is reachable."

    constraints = [
        "1 <= arr.length <= 5 * 10^4",
        "0 <= arr[i] < arr.length",
        "0 <= start < arr.length"
    ]

    explanation = """To determine reachability:
1. Use Breadth-First Search (BFS) or Depth-First Search (DFS) starting from the provided `start` index.
2. For each current index `i`, we can transition to `i + arr[i]` and `i - arr[i]` if they are within the array boundaries.
3. If we find an index with value 0, return `true`.
4. Keep track of visited indices to avoid cycles and redundant work.
5. If the search finishes without finding any 0, return `false`."""

    answer = """class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        queue = [start]
        visited = {start}
        
        while queue:
            curr = queue.pop(0)
            if arr[curr] == 0:
                return True
            
            for next_idx in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append(next_idx)
        return False"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        args = json.loads(raw)
        arr = args[0]
        start = args[1]
        sol = Solution()
        print(sol.canReach(arr, start))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>

using namespace std;

class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        // User logic here
        return false;
    }
};

int main() {
    printf("true\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean canReach(int[] arr, int start) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("true");
    }
}""",
        "javascript": """/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [arr, start] = JSON.parse(input);
    console.log(canReach(arr, start));
}""",
        "c": """#include <stdio.h>
#include <stdbool.h>

bool canReach(int* arr, int arrSize, int start) {
    // User logic here
    return false;
}

int main() {
    printf("true\\n");
    return 0;
}"""
    }

    def solve(arr, start):
        q = [start]; v = {start}
        while q:
            c = q.pop(0)
            if arr[c] == 0: return True
            for nxt in [c + arr[c], c - arr[c]]:
                if 0 <= nxt < len(arr) and nxt not in v:
                    v.add(nxt); q.append(nxt)
        return False

    test_cases_data = [
        ([4,2,3,0,3,1,2], 5),
        ([4,2,3,0,3,1,2], 0),
        ([3,0,2,1,2], 2),
        ([0], 0),
        ([1,0], 0),
        ([1,0], 1),
        ([1,1,1,1,1,1,0], 0),
        ([1,1,1,1,1,1,2], 0),
        ([0,1,2,3], 3),
        ([2,2,0,2,2], 4)
    ]

    test_cases = []
    for i, data_pair in enumerate(test_cases_data):
        arr, start = data_pair
        inp = json.dumps([arr, start]).replace(" ", "")
        out = str(solve(arr, start)).lower()
        is_sample = i < 3
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
        "topics": ["Array", "BFS", "DFS"],
        "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
