import json
import os

def generate_json():
    problem_id = 1095
    title = "Find in Mountain Array"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>1095. Find in Mountain Array</h3>
<p><em>(This problem is an <strong>interactive problem</strong>.)</em></p>

<p>You may recall that an array <code>arr</code> is a <strong>mountain array</strong> if and only if:</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>Given a mountain array <code>mountainArr</code>, return the <strong>minimum</strong> <code>index</code> such that <code>mountainArr.get(index) == target</code>. If such an <code>index</code> does not exist, return <code>-1</code>.</p>

<p><strong>You cannot access the mountain array directly.</strong> You may only access the array using a <code>MountainArray</code> interface:</p>

<ul>
	<li><code>MountainArray.get(k)</code> returns the element of the array at index <code>k</code> (0-indexed).</li>
	<li><code>MountainArray.length()</code> returns the length of the array.</li>
</ul>

<p>Submissions making more than <code>100</code> calls to <code>MountainArray.get</code> will be judged <em>Wrong Answer</em>. Also, any solutions that attempt to circumvent the judge will result in disqualification.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 3, mountainArr = [1,2,3,4,5,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 exists in the array, at index 2 and index 5. Return the minimum index, which is 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 3, mountainArr = [0,1,2,4,2,1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 3 does not exist in <code>mountainArr</code>, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= mountainArr.length() &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= mountainArr.get(index) &lt;= 10<sup>9</sup></code></li>
</ul>
"""

    input_format = "An integer `target` and an array `mountainArr` provided as `[target, mountainArr]` in JSON."
    output_format = "An integer representing the minimum index of the target."

    constraints = [
        "3 <= mountainArr.length <= 10^4",
        "0 <= target, values <= 10^9",
        "At most 100 calls to get()"
    ]

    explanation = """To find the target in a mountain array within 100 calls:
1. Use binary search to find the peak of the mountain. A peak is where `arr[i-1] < arr[i] > arr[i+1]`.
2. Once the peak is found at index `p`, the array is divided into two parts: `[0, p]` (increasing) and `[p+1, n-1]` (decreasing).
3. Search for the target in the increasing part `[0, p]` using standard binary search.
4. If found, return the index.
5. If not found, search for the target in the decreasing part `[p+1, n-1]` using a modified binary search for decreasing order.
6. If found, return the index. Otherwise, return -1."""

    answer = """# """

    boilerplate = {
        "python": """import sys
import json

class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.count = 0
    def get(self, index: int) -> int:
        self.count += 1
        if self.count > 100: raise Exception("Too many calls")
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        target, arr = json.loads(raw)
        ma = MountainArray(arr)
        sol = Solution()
        print(sol.findInMountainArray(target, ma))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class MountainArray {
    vector<int> arr;
    int calls = 0;
public:
    MountainArray(vector<int> a) : arr(a) {}
    int get(int index) {
        if (++calls > 100) exit(1);
        return arr[index];
    }
    int length() { return arr.size(); }
};

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        // User logic here
        return -1;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        int target = j[0].get<int>();
        vector<int> arr = j[1].get<vector<int>>();
        MountainArray ma(arr);
        Solution sol;
        cout << sol.findInMountainArray(target, ma) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

interface MountainArray {
    public int get(int index);
    public int length();
}

class MountainArrayImpl implements MountainArray {
    private int[] arr;
    private int calls = 0;
    public MountainArrayImpl(int[] a) { this.arr = a; }
    public int get(int index) {
        if (++calls > 100) System.exit(1);
        return arr[index];
    }
    public int length() { return arr.length; }
}

class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        // User logic here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int target = (int)data[0];
            int[] arr = mapper.convertValue(data[1], int[].class);
            System.out.println(new Solution().findInMountainArray(target, new MountainArrayImpl(arr)));
        }
    }
}""",
        "javascript": """function MountainArray(arr) {
    this.arr = arr;
    this.calls = 0;
    this.get = function(index) {
        if (++this.calls > 100) process.exit(1);
        return this.arr[index];
    };
    this.length = function() { return this.arr.length; };
}

var findInMountainArray = function(target, mountainArr) {
    // User logic here
    return -1;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [target, arr] = JSON.parse(input);
    const ma = new MountainArray(arr);
    console.log(findInMountainArray(target, ma));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct {
    int* data;
    int size;
    int calls;
} MountainArray;

int get(MountainArray* obj, int index) {
    obj->calls++;
    if (obj->calls > 100) exit(1);
    return obj->data[index];
}

int length(MountainArray* obj) {
    return obj->size;
}

int findInMountainArray(int target, MountainArray* mountainArr) {
    // User logic here
    return -1;
}

int main() {
    int target;
    if (scanf("%d", &target) != 1) return 0;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* data = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; data = realloc(data, cap * sizeof(int)); }
        scanf("%d", &data[s++]);
    }
    MountainArray ma = {data, s, 0};
    printf("%d\\n", findInMountainArray(target, &ma));
    free(data);
    return 0;
}"""
    }

    def solve(target, arr):
        n = len(arr)
        # Find peak
        l, r = 0, n - 1
        peak = 0
        while l <= r:
            m = (l + r) // 2
            if 0 < m < n - 1:
                if arr[m-1] < arr[m] > arr[m+1]:
                    peak = m
                    break
                elif arr[m-1] < arr[m]: l = m + 1
                else: r = m
            elif m == 0: l = m + 1
            else: r = m - 1
        
        # Search left
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target: return m
            elif arr[m] < target: l = m + 1
            else: r = m - 1
        
        # Search right
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target: return m
            elif arr[m] > target: l = m + 1
            else: r = m - 1
        return -1

    test_cases_data = [
        [3, [1,2,3,4,5,3,1]], # Sample 1
        [3, [0,1,2,4,2,1]],   # Sample 2
        [2, [1,5,2]],
        [5, [1,5,2]],
        [0, [1,3,5,4,2,0]],
        [1, [1,2,3,4,5,4,3,2,1]],
        [10, [1,2,3,10,2,1]],
        # Stress tests
        [1, [i for i in range(5000)] + [i for i in range(4998, -1, -1)]],
        [4999, [i for i in range(5000)] + [i for i in range(4998, -1, -1)]],
        [0, [i for i in range(5000)] + [i for i in range(4998, -1, -1)]]
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
        "topics": ["Array", "Binary Search", "Interactive"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
