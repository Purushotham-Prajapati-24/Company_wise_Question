import json
import os

def generate_json():
    problem_id = 632
    title = "Smallest Range Covering Elements from K Lists"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>632. Smallest Range Covering Elements from K Lists</h3>
<p>You have <code>k</code> lists of sorted integers in <strong>non-decreasing order</strong>. Find the <strong>smallest</strong> range that includes at least one number from each of the <code>k</code> lists.</p>

<p>We define the range <code>[a, b]</code> is smaller than range <code>[c, d]</code> if <code>b - a &lt; d - c</code> <strong>or</strong> <code>a &lt; c</code> if <code>b - a == d - c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
<strong>Output:</strong> [20,24]
<strong>Explanation:</strong> 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [[1,2,3],[1,2,3],[1,2,3]]
<strong>Output:</strong> [1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>nums.length == k</code></li>
    <li><code>1 &lt;= k &lt;= 3500</code></li>
    <li><code>1 &lt;= nums[i].length &lt;= 50</code></li>
    <li><code>-10<sup>5</sup> &lt;= nums[i][j] &lt;= 10<sup>5</sup></code></li>
    <li><code>nums[i]</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>"""

    input_format = "A single line: A JSON 2D array."
    output_format = "A JSON array [a, b] representing the smallest range."

    constraints = [
        "1 <= k <= 3500",
        "1 <= nums[i].length <= 50",
        "-10^5 <= nums[i][j] <= 10^5"
    ]

    explanation = """Use a min-heap. Push the first element from each list into the heap along with its list index and element index. Track the current maximum. Pop the minimum, update the range, and push the next element from that list."""

    answer = """import heapq
class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        cur_max = float('-inf')
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            cur_max = max(cur_max, lst[0])
        
        best = [heap[0][0], cur_max]
        
        while heap:
            cur_min, i, j = heapq.heappop(heap)
            if cur_max - cur_min < best[1] - best[0]:
                best = [cur_min, cur_max]
            if j + 1 == len(nums[i]):
                break
            nxt = nums[i][j+1]
            heapq.heappush(heap, (nxt, i, j + 1))
            cur_max = max(cur_max, nxt)
            
        return best"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        # User logic here
        return [0, 0]

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        nums = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.smallestRange(nums)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        // User logic here
        return {0, 0};
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        // Simple JSON parse for 2D array
        vector<vector<int>> nums;
        vector<int> cur;
        bool inArr = false;
        int depth = 0;
        string num = "";
        bool neg = false;
        for (char c : input) {
            if (c == '[') {
                depth++;
                if (depth == 2) { inArr = true; cur.clear(); }
            } else if (c == ']') {
                if (depth == 2 && inArr) {
                    if (!num.empty()) {
                        cur.push_back((neg ? -1 : 1) * stoi(num));
                        num = "";
                        neg = false;
                    }
                    nums.push_back(cur);
                    inArr = false;
                }
                depth--;
            } else if (c == '-' && depth == 2) {
                neg = true;
            } else if (isdigit(c) && depth == 2) {
                num += c;
            } else if (c == ',' && depth == 2 && !num.empty()) {
                cur.push_back((neg ? -1 : 1) * stoi(num));
                num = "";
                neg = false;
            }
        }
        Solution sol;
        vector<int> ans = sol.smallestRange(nums);
        cout << "[" << ans[0] << "," << ans[1] << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        // User logic here
        return new int[]{0, 0};
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            // Parse 2D array
            List<List<Integer>> nums = new ArrayList<>();
            String stripped = raw.substring(1, raw.length()-1);
            int depth = 0;
            StringBuilder sb = new StringBuilder();
            for (char c : stripped.toCharArray()) {
                if (c == '[') { depth++; if (depth > 0) sb.append(c); }
                else if (c == ']') { if (depth > 0) sb.append(c); depth--;
                    if (depth == 0) {
                        String inner = sb.toString().substring(1, sb.length()-1);
                        List<Integer> row = new ArrayList<>();
                        if (!inner.isEmpty())
                            for (String p : inner.split(",")) row.add(Integer.parseInt(p.trim()));
                        nums.add(row);
                        sb = new StringBuilder();
                    }
                } else if (depth > 0) sb.append(c);
            }
            Solution sol = new Solution();
            int[] ans = sol.smallestRange(nums);
            System.out.println("[" + ans[0] + "," + ans[1] + "]");
        }
    }
}""",
        "javascript": """/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var smallestRange = function(nums) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const nums = JSON.parse(input);
    console.log(JSON.stringify(smallestRange(nums)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* smallestRange(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    // User logic here
    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = 0; res[1] = 0;
    *returnSize = 2;
    return res;
}

int main() {
    // For C, simplified parsing not included; use Python/Java/C++/JS
    int returnSize;
    int** nums = NULL;
    int numsColSize[1] = {0};
    int* ans = smallestRange(nums, 0, numsColSize, &returnSize);
    printf("[%d,%d]\\n", ans[0], ans[1]);
    free(ans);
    return 0;
}"""
    }

    test_cases = [
        {"input": "[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]", "expected_output": "[20,24]", "is_sample": True},
        {"input": "[[1,2,3],[1,2,3],[1,2,3]]", "expected_output": "[1,1]", "is_sample": True},
        {"input": "[[1],[2],[3]]", "expected_output": "[1,3]", "is_sample": False},
        {"input": "[[10,20,30],[1,15,25],[5,10,15]]", "expected_output": "[10,15]", "is_sample": False},
        {"input": "[[1,5,10],[2,6,11],[3,7,12]]", "expected_output": "[1,3]", "is_sample": False},
        {"input": "[[1,100],[2,99],[3,98],[4,97]]", "expected_output": "[1,4]", "is_sample": False},
        {"input": "[[-5,-4,-3],[-2,-1,0],[1,2,3]]", "expected_output": "[-3,1]", "is_sample": False},
        {"input": "[[" + ",".join(str(i*10) for i in range(50)) + "],[" + ",".join(str(i*10+1) for i in range(50)) + "],[" + ",".join(str(i*10+2) for i in range(50)) + "]]", "expected_output": "[0,2]", "is_sample": False},
        {"input": "[[1,50],[1,50],[1,50],[1,50],[1,50]]", "expected_output": "[1,1]", "is_sample": False},
        {"input": "[[" + ",".join(str(i) for i in range(1,51)) + "],[" + ",".join(str(i+50) for i in range(1,51)) + "]]", "expected_output": "[50,51]", "is_sample": False}
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
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Greedy", "Sliding Window", "Sorting", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
