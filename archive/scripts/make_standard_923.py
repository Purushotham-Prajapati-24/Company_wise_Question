import json
import os
from collections import Counter

def generate_json():
    problem_id = 923
    title = "3Sum With Multiplicity"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>923. 3Sum With Multiplicity</h3>
<p>Given an integer array <code>arr</code>, and an integer <code>target</code>, return the number of tuples <code>i, j, k</code> such that <code>i &lt; j &lt; k</code> and <code>arr[i] + arr[j] + arr[k] == target</code>.</p>

<p>As the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [1,1,2,2,3,3,4,4,5,5], target = 8
<strong>Output:</strong> 20
<strong>Explanation: </strong>
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [1,1,2,2,2,2], target = 5
<strong>Output:</strong> 12
<strong>Explanation: </strong>
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [2,1,3], target = 6
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>3 &lt;= arr.length &lt;= 3000</code></li>
    <li><code>0 &lt;= arr[i] &lt;= 100</code></li>
    <li><code>0 &lt;= target &lt;= 300</code></li>
</ul>"""

    input_format = "A line containing a JSON array `arr` and a second line with integer `target`."
    output_format = "An integer representing the count modulo 10^9 + 7."

    constraints = [
        "3 <= arr.length <= 3000",
        "0 <= arr[i] <= 100",
        "0 <= target <= 300"
    ]

    explanation = """Since the range of values in `arr` is small ([0, 100]), we can use a frequency map. Iterate through all possible combinations of three values (i, j, k) that sum to `target`. For each combination, calculate the number of ways to pick those values using combinations (nCr).
- Case 1: i < j < k: ways = count[i] * count[j] * count[k]
- Case 2: i == j < k: ways = count[i] * (count[i] - 1) / 2 * count[k]
- Case 3: i < j == k: ways = count[i] * count[j] * (count[j] - 1) / 2
- Case 4: i == j == k: ways = count[i] * (count[i] - 1) * (count[i] - 2) / 6"""

    answer = """from collections import Counter

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        ans = 0
        
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) // 2
                    elif i == j == k:
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    
                    ans %= MOD
                    j += 1
                    k -= 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        arr = json.loads(raw[0])
        target = int(raw[1])
        sol = Solution()
        print(sol.threeSumMulti(arr, target))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string input) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < input.length() - 1) {
        if (isdigit(input[i])) {
            int val = 0; int off=0;
            sscanf(input.c_str()+i, "%d%n", &val, &off);
            res.push_back(val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string line;
    if (getline(cin, line)) {
        auto arr = parseArray(line);
        int target;
        cin >> target;
        Solution sol;
        cout << sol.threeSumMulti(arr, target) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int threeSumMulti(int[] arr, int target) {
        // User logic here
        return 0;
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
        if (sc.hasNextLine()) {
            String line = sc.nextLine();
            int[] arr = parseArray(line);
            int target = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.threeSumMulti(arr, target));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var threeSumMulti = function(arr, target) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\n|\\r\\n/);
if (input.length >= 2) {
    console.log(threeSumMulti(JSON.parse(input[0]), parseInt(input[1])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int threeSumMulti(int* arr, int arrSize, int target) {
    // User logic here
    return 0;
}

int main() {
    char line[10000];
    if (scanf("%s", line) == 1) {
        int sz = 0, cap = 100;
        int* arr = malloc(cap * sizeof(int));
        char* token = strtok(line+1, ",]");
        while (token != NULL) {
            if (sz == cap) arr = realloc(arr, (cap *= 2) * sizeof(int));
            arr[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        int target;
        scanf("%d", &target);
        printf("%d\\n", threeSumMulti(arr, sz, target));
        free(arr);
    }
    return 0;
}"""
    }

    def solve(arr, target):
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        ans = 0
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T: j += 1
                elif y + z > T: k -= 1
                else:
                    if i < j < k: ans += count[x] * count[y] * count[z]
                    elif i == j < k: ans += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k: ans += count[x] * count[y] * (count[y] - 1) // 2
                    elif i == j == k: ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    ans %= MOD
                    j += 1; k -= 1
        return ans

    test_cases_data = [
        ([1,1,2,2,3,3,4,4,5,5], 8),
        ([1,1,2,2,2,2], 5),
        ([2,1,3], 6),
        ([1,1,1], 3),
        ([0,0,0], 0),
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 30),
        ([0,10,20,30,40,50,60,70,80,90,100], 150),
        ([1,2,1,2,1,2,1,2], 4),
        ([1,1,1,1,1,1,1,1,1,1], 3),
        ([100,100,100,100,100], 300)
    ]

    test_cases = []
    for i, (arr, target) in enumerate(test_cases_data):
        inp = f"{json.dumps(arr).replace(' ', '')}\n{target}"
        out = str(solve(arr, target))
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
        "topics": ["Array", "Hash Table", "Two Pointers", "Sorting", "Counting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
