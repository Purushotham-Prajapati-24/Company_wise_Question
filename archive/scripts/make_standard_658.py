import json
import os

def generate_json():
    problem_id = 658
    title = "Find K Closest Elements"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>658. Find K Closest Elements</h3>
<p>Given a <strong>sorted</strong> integer array <code>arr</code>, two integers <code>k</code> and <code>x</code>, return the <code>k</code> closest integers to <code>x</code> in the array. The result should also be sorted in ascending order.</p>

<p>An integer <code>a</code> is closer to <code>x</code> than an integer <code>b</code> if:</p>

<ul>
    <li><code>|a - x| &lt; |b - x|</code>, or</li>
    <li><code>|a - x| == |b - x|</code> and <code>a &lt; b</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = 3
<strong>Output:</strong> [1,2,3,4]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = -1
<strong>Output:</strong> [1,2,3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= k &lt;= arr.length</code></li>
    <li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
    <li><code>arr</code> is sorted in <strong>ascending order</strong>.</li>
    <li><code>-10<sup>4</sup> &lt;= arr[i], x &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Three lines:\nLine 1: JSON array `arr`.\nLine 2: Integer `k`.\nLine 3: Integer `x`."
    output_format = "A JSON array of the k closest elements in ascending order."

    constraints = [
        "1 <= k <= arr.length",
        "1 <= arr.length <= 10^4",
        "arr is sorted in ascending order",
        "-10^4 <= arr[i], x <= 10^4"
    ]

    explanation = """Use binary search to find the left boundary of the k-element window. Use two pointers left=0 and right=len(arr)-k. While left < right, compare the distance of arr[mid] and arr[mid+k] to x, and shrink the window accordingly."""

    answer = """class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 3:
        arr = json.loads(raw[0])
        k = int(raw[1])
        x = int(raw[2])
        sol = Solution()
        print(json.dumps(sol.findClosestElements(arr, k, x)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        // User logic here
        return {};
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '-' || isdigit(input[i])) {
            size_t next;
            res.push_back(stoi(input.substr(i), &next));
            i += next;
        } else i++;
    }
    return res;
}

int main() {
    string arr_str, k_str, x_str;
    if (getline(cin, arr_str) && getline(cin, k_str) && getline(cin, x_str)) {
        vector<int> arr = parseArray(arr_str);
        int k = stoi(k_str);
        int x = stoi(x_str);
        Solution sol;
        vector<int> ans = sol.findClosestElements(arr, k, x);
        cout << "[";
        for (size_t i = 0; i < ans.size(); i++)
            cout << ans[i] << (i + 1 == ans.size() ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        else return new int[0];
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String arr_str = sc.nextLine().trim();
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                if (sc.hasNextInt()) {
                    int x = sc.nextInt();
                    int[] arr = parseArray(arr_str);
                    Solution sol = new Solution();
                    List<Integer> ans = sol.findClosestElements(arr, k, x);
                    System.out.print("[");
                    for (int i = 0; i < ans.size(); i++)
                        System.out.print(ans.get(i) + (i + 1 == ans.size() ? "" : ","));
                    System.out.println("]");
                }
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 3) {
    const arr = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    const x = parseInt(input[2], 10);
    console.log(JSON.stringify(findClosestElements(arr, k, x)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* findClosestElements(int* arr, int arrSize, int k, int x, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

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
    char arr_str[500000];
    if (fgets(arr_str, sizeof(arr_str), stdin)) {
        int arrSize;
        int* arr = parseArray(arr_str, &arrSize);
        int k, x;
        if (scanf("%d\\n%d", &k, &x) == 2) {
            int returnSize;
            int* ans = findClosestElements(arr, arrSize, k, x, &returnSize);
            printf("[");
            for (int i = 0; i < returnSize; i++)
                printf("%d%s", ans[i], i + 1 == returnSize ? "" : ",");
            printf("]\\n");
            if (ans) free(ans);
        }
        free(arr);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,2,3,4,5]\\n4\\n3", "expected_output": "[1,2,3,4]", "is_sample": True},
        {"input": "[1,2,3,4,5]\\n4\\n-1", "expected_output": "[1,2,3,4]", "is_sample": True},
        {"input": "[1,2,3,4,5]\\n4\\n10", "expected_output": "[2,3,4,5]", "is_sample": False},
        {"input": "[1,3,5,7,9]\\n3\\n6", "expected_output": "[5,7,9]", "is_sample": False},
        {"input": "[1,2,2,2,3,4,5]\\n3\\n2", "expected_output": "[2,2,2]", "is_sample": False},
        {"input": "[-5,-3,-1,1,3,5]\\n4\\n0", "expected_output": "[-3,-1,1,3]", "is_sample": False},
        {"input": "[1,1,1,1,1]\\n3\\n1", "expected_output": "[1,1,1]", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(10000)) + "]\\n100\\n5000", "expected_output": "[" + ",".join(str(i) for i in range(4950, 5050)) + "]", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(10000)) + "]\\n1\\n0", "expected_output": "[0]", "is_sample": False},
        {"input": "[" + ",".join(str(i) for i in range(10000)) + "]\\n5000\\n9999", "expected_output": "[" + ",".join(str(i) for i in range(5000, 10000)) + "]", "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Binary Search", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
