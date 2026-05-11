import json
import os

def generate_json():
    problem_id = 1053
    title = "Previous Permutation With One Swap"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1053. Previous Permutation With One Swap</h3>
<p>Given an array of positive integers <code>arr</code> (not necessarily distinct), return <em>the <strong>lexicographically largest</strong> permutation that is smaller than</em> <code>arr</code>, that can be <strong>made with exactly one swap</strong>.</p>

<p>If it cannot be done, return the original array.</p>

<p><strong>Note</strong> that a swap exchanges the positions of two elements <code>arr[i]</code> and <code>arr[j]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,2,1]
<strong>Output:</strong> [3,1,2]
<strong>Explanation:</strong> Swapping 2 and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,1,5]
<strong>Output:</strong> [1,1,5]
<strong>Explanation:</strong> This is already the smallest permutation.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,9,4,6,7]
<strong>Output:</strong> [1,7,4,6,9]
<strong>Explanation:</strong> Swapping 9 and 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "An array of integers `arr` provided as `[arr]` in JSON."
    output_format = "An array of integers representing the resulting permutation."

    constraints = [
        "1 <= arr.length <= 10^4",
        "1 <= arr[i] <= 10^4"
    ]

    explanation = """To find the largest permutation smaller than arr with one swap:
1. Find the largest index `i` such that `arr[i] > arr[i+1]`. If no such index exists, return `arr`.
2. Find the largest index `j` such that `j > i` and `arr[j] < arr[i]`.
3. To maximize the result, if there are multiple `j`'s with the same value `arr[j]`, pick the smallest such `j` among the candidates (actually, the largest `j` works, but if there's a tie in `arr[j]`, pick the one at the smallest `j` to avoid repetitive values? No, pick the first one from the right that is not the same as the one to its left).
4. Swap `arr[i]` and `arr[j]`.
5. Return the modified array."""

    answer = """class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        if i < 0:
            return arr
        
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        
        while arr[j] == arr[j-1]:
            j -= 1
            
        arr[i], arr[j] = arr[j], arr[i]
        return arr"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        # User logic here
        return arr

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        arr = json.loads(raw)
        if isinstance(arr[0], list): arr = arr[0]
        sol = Solution()
        print(sol.prevPermOpt1(arr))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> prevPermOpt1(vector<int>& arr) {
        // User logic here
        return arr;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<int> arr;
        if (j.is_array() && j.size() > 0 && j[0].is_array()) arr = j[0].get<vector<int>>();
        else arr = j.get<vector<int>>();
        Solution sol;
        vector<int> res = sol.prevPermOpt1(arr);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[] prevPermOpt1(int[] arr) {
        // User logic here
        return arr;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            int[] arr;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                arr = mapper.convertValue(((List)raw).get(0), int[].class);
            } else {
                arr = mapper.convertValue(raw, int[].class);
            }
            int[] res = new Solution().prevPermOpt1(arr);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var prevPermOpt1 = function(arr) {
    // User logic here
    return arr;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let arr = JSON.parse(input);
    if (Array.isArray(arr[0])) arr = arr[0];
    const res = prevPermOpt1(arr);
    console.log(JSON.stringify(res));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* prevPermOpt1(int* arr, int arrSize, int* returnSize) {
    // User logic here
    *returnSize = arrSize;
    return arr;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* arr = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; arr = realloc(arr, cap * sizeof(int)); }
        scanf("%d", &arr[s++]);
    }
    int rs;
    int* res = prevPermOpt1(arr, s, &rs);
    printf("[");
    for (int i = 0; i < rs; i++) printf("%d%s", res[i], i == rs - 1 ? "" : ",");
    printf("]\\n");
    free(arr);
    return 0;
}"""
    }

    def solve(arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        if i < 0: return arr
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        while arr[j] == arr[j-1]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    test_cases_data = [
        [[3,2,1]],       # Sample 1 -> [3,1,2]
        [[1,1,5]],       # Sample 2 -> [1,1,5]
        [[1,9,4,6,7]],   # Sample 3 -> [1,7,4,6,9]
        [[3,1,1,3]],     # Tie case
        [[2,1,1]],       # Swap first with last? -> [1,2,1]
        [[1,2,3]],       # No swap
        [[10, 5, 2, 8]],
        # Stress tests
        [list(range(10000, 0, -1))],
        [list(range(1, 10001))],
        [[100]*1000 + [50]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0].copy())).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Greedy"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
