import json
import os

def generate_json():
    problem_id = 852
    title = "Peak Index in a Mountain Array"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>852. Peak Index in a Mountain Array</h3>
<p>An array <code>arr</code> is a <strong>mountain</strong> if the following properties hold:</p>
<ul>
    <li><code>arr.length &gt;= 3</code></li>
    <li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
        <ul>
            <li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
            <li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
        </ul>
    </li>
</ul>

<p>Given a mountain array <code>arr</code>, return the index <code>i</code> such that <code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code>.</p>

<p>You must solve it in <code>O(log(arr.length))</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [0,1,0]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [0,2,1,0]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [0,10,5,2]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>3 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
    <li><code>arr</code> is <strong>guaranteed</strong> to be a mountain array.</li>
</ul>"""

    input_format = "A single line containing the JSON array `arr`."
    output_format = "An integer representing the peak index."

    constraints = [
        "3 <= arr.length <= 100000",
        "arr is a mountain array",
        "O(log n) complexity required"
    ]

    explanation = """To achieve O(log n) complexity, use binary search. We perform binary search on the array. At each step, if `arr[mid] < arr[mid + 1]`, the peak must be to the right (at or after `mid + 1`). Otherwise, the peak is to the left (at or before `mid`)."""

    answer = """class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        arr = json.loads(raw)
        sol = Solution()
        print(sol.peakIndexInMountainArray(arr))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < input.length() - 1) {
        if (isdigit(input[i]) || input[i] == '-') {
            int val = 0; int off=0;
            sscanf(input.c_str()+i, "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string input;
    if (cin >> input) {
        auto arr = parseArray(input);
        Solution sol;
        cout << sol.peakIndexInMountainArray(arr) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String input = sc.next();
            input = input.substring(1, input.length()-1);
            String[] parts = input.split(",");
            int[] arr = new int[parts.length];
            for (int i=0; i<parts.length; i++) arr[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.peakIndexInMountainArray(arr));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(peakIndexInMountainArray(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int peakIndexInMountainArray(int* arr, int arrSize) {
    // User logic here
    return 0;
}

int main() {
    char input[100000];
    if (scanf("%s", input) == 1) {
        int cap = 100, sz = 0;
        int* resArr = malloc(cap * sizeof(int));
        char* token = strtok(input + 1, ",]");
        while (token != NULL) {
            if (sz == cap) resArr = realloc(resArr, (cap *= 2) * sizeof(int));
            resArr[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%d\\n", peakIndexInMountainArray(resArr, sz));
        free(resArr);
    }
    return 0;
}"""
    }

    def solve(arr):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low

    test_cases_data = [
        [0,1,0],
        [0,2,1,0],
        [0,10,5,2],
        [3,4,5,1],
        [24,69,100,99,79,78,67,36,26,19],
        [0,1,2,3,4,5,4,3,2,1],
        [0,1,2,3,4,5,6,10,9,8,7,6,5,4,3,2,1,0],
        [0,1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0],
        [0,1,2,3,4,3,2,1,0],
        [0,10,11,9,8]
    ]

    test_cases = []
    for i, arr in enumerate(test_cases_data):
        inp = json.dumps(arr).replace(" ", "")
        out = str(solve(arr))
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
