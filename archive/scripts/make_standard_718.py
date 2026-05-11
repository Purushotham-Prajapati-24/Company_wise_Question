import json
import os

def generate_json():
    problem_id = 718
    title = "Maximum Length of Repeated Subarray"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>718. Maximum Length of Repeated Subarray</h3>
<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>the maximum length of a subarray that appears in <strong>both</strong> arrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The repeated subarray with maximum length is [3,2,1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The repeated subarray with maximum length is [0,0,0,0,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
    <li><code>0 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `nums1`.\nLine 2: JSON array `nums2`."
    output_format = "An integer: the maximum length of a repeated subarray."

    constraints = [
        "1 <= nums1.length, nums2.length <= 1000",
        "0 <= nums1[i], nums2[i] <= 100"
    ]

    explanation = """Use DP. `dp[i][j]` takes the longest repeated subarray ending at `nums1[i-1]` and `nums2[j-1]`. If `nums1[i-1] == nums2[j-1]`, then `dp[i][j] = dp[i-1][j-1] + 1`; else `dp[i][j] = 0`. The maximum value in `dp` is the answer."""

    answer = """class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [0] * (m + 1)
        max_len = 0
        
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
        
        return max_len"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        nums1 = json.loads(raw[0])
        nums2 = json.loads(raw[1])
        sol = Solution()
        print(sol.findLength(nums1, nums2))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            int val = 0;
            while (isdigit(input[i])) { val = val * 10 + (input[i]-'0'); i++; }
            res.push_back(val);
        } else i++;
    }
    return res;
}

int main() {
    string n_str, k_str;
    if (getline(cin, n_str) && getline(cin, k_str)) {
        vector<int> nums1 = parseArray(n_str);
        vector<int> nums2 = parseArray(k_str);
        Solution sol;
        cout << sol.findLength(nums1, nums2) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        // User logic here
        return 0;
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String n_str = sc.nextLine().trim();
            if (sc.hasNextLine()) {
                String k_str = sc.nextLine().trim();
                int[] nums1 = parseArray(n_str);
                int[] nums2 = parseArray(k_str);
                Solution sol = new Solution();
                System.out.println(sol.findLength(nums1, nums2));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findLength = function(nums1, nums2) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const nums1 = JSON.parse(input[0]);
    const nums2 = JSON.parse(input[1]);
    console.log(findLength(nums1, nums2));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int findLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // User logic here
    return 0;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
            int val, off = 0;
            sscanf(input+i, "%d%n", &val, &off);
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
    char n_str[50000], k_str[50000];
    if (fgets(n_str, sizeof(n_str), stdin) && fgets(k_str, sizeof(k_str), stdin)) {
        int nums1Size, nums2Size;
        int* nums1 = parseArray(n_str, &nums1Size);
        int* nums2 = parseArray(k_str, &nums2Size);
        printf("%d\\n", findLength(nums1, nums1Size, nums2, nums2Size));
        free(nums1);
        free(nums2);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [0] * (m + 1)
        max_len = 0
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0
        return max_len

    test_cases_data = [
        ([1,2,3,2,1], [3,2,1,4,7]),
        ([0,0,0,0,0], [0,0,0,0,0]),
        ([1,2,3], [4,5,6]),
        ([1,2,3], [1,2,3]),
        ([5,4,3,2,1], [1,2,3,4,5]),
        ([0,1,1,1,1], [1,0,1,0,1]),
        ([10,20,30,40], [20,30,40,50]),
        ([1]*1000, [1]*1000),
        ([x % 100 for x in range(1000)], [x % 100 for x in range(500, 1500)]),
        ([x for x in range(1000)], [x for x in range(500, 1000, 2)])
    ]

    test_cases = []
    for i, (nums1, nums2) in enumerate(test_cases_data):
        inp = json.dumps(nums1) + "\\n" + json.dumps(nums2)
        out = str(solve(nums1, nums2))
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
        "topics": ["Array", "Binary Search", "Dynamic Programming", "Sliding Window", "String Matching", "Hash Function"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
