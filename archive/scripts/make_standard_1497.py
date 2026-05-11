import json
import os

def generate_json():
    problem_id = 1497
    title = "Check If Array Pairs Are Divisible by k"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1497. Check If Array Pairs Are Divisible by k</h3>
<p>Given an array of integers <code>arr</code> of even length <code>n</code> and an integer <code>k</code>.</p>

<p>We want to divide the array into exactly <code>n / 2</code> pairs such that the sum of each pair is divisible by <code>k</code>.</p>

<p>Return <code>true</code><em> if you can find a way to do that or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5,10,6,7,8,9], k = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5,6], k = 7
<strong>Output:</strong> true
<strong>Explanation:</strong> Pairs are (1,6),(2,5) and (3,4).
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5,6], k = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> You can try all sets of 3 pairs, but the sum of no pair is divisible by 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>arr.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> is even.</li>
	<li><code>-10<sup>9</sup> &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "An array of integers `arr` and an integer `k` provided as `[arr, k]` in JSON."
    output_format = "A boolean value `true` or `false`."

    constraints = [
        "1 <= n <= 10^5",
        "n is even",
        "1 <= k <= 10^5"
    ]

    explanation = """To check if array pairs are divisible by k:
1. Count the remainders of each element when divided by `k`. Use `(x % k + k) % k` to handle negative numbers correctly.
2. For pairs to have a sum divisible by `k`, their remainders `r1` and `r2` must satisfy:
   - If `r == 0`, then the count of such elements must be even (they pair with each other).
   - If `2 * r == k`, then the count of such elements must also be even (they pair with each other).
   - Otherwise, the count of elements with remainder `r` must equal the count of elements with remainder `k - r`.
3. If all these conditions are met, return `true`; otherwise, return `false`."""

    answer = """class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        rem_count = [0] * k
        for x in arr:
            rem_count[((x % k) + k) % k] += 1
            
        if rem_count[0] % 2 != 0:
            return False
            
        for i in range(1, (k // 2) + 1):
            if i == k - i:
                if rem_count[i] % 2 != 0:
                    return False
            else:
                if rem_count[i] != rem_count[k - i]:
                    return False
        return True"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        arr, k = json.loads(raw)
        sol = Solution()
        print(str(sol.canArrange(arr, k)).lower())""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        // User logic here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> arr = j[0].get<vector<int>>();
        int k = j[1];
        Solution sol;
        cout << (sol.canArrange(arr, k) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public boolean canArrange(int[] arr, int k) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            int[] arr = mapper.convertValue(data[0], int[].class);
            int k = (Integer) data[1];
            System.out.println(new Solution().canArrange(arr, k));
        }
    }
}""",
        "javascript": """var canArrange = function(arr, k) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [arr, k] = JSON.parse(input);
    console.log(canArrange(arr, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool canArrange(int* arr, int arrSize, int k){
    // User logic here
    return false;
}

int main() {
    int c;
    // Skip to first array [
    while ((c = getchar()) != EOF && c != '[');
    int cap = 1024, s = 0;
    int* arr = malloc(cap * sizeof(int));
    while (1) {
        // Skip junk between numbers
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; arr = realloc(arr, cap * sizeof(int)); }
        scanf("%d", &arr[s++]);
    }
    // Skip to the integer k after common array closure
    while ((c = getchar()) != EOF && c != ',');
    int k;
    if (scanf("%d", &k) == 1) {
        printf("%s\\n", canArrange(arr, s, k) ? "true" : "false");
    }
    free(arr);
    return 0;
}"""
    }

    def solve(arr, k):
        rem = [0] * k
        for x in arr: rem[((x % k) + k) % k] += 1
        if rem[0] % 2 != 0: return False
        for i in range(1, (k // 2) + 1):
            if i == k - i:
                if rem[i] % 2 != 0: return False
            else:
                if rem[i] != rem[k - i]: return False
        return True

    test_cases_data = [
        [[1,2,3,4,5,10,6,7,8,9], 5], # Sample 1
        [[1,2,3,4,5,6], 7],           # Sample 2
        [[1,2,3,4,5,6], 10],          # Sample 3
        [[-1,1,-2,2,-3,3], 3],        # Negative
        [[5,5,5,5], 5],               # All same rem 0
        [[4,4,4,4], 8],               # All same rem 4 (k/2)
        [[1,4,1,4], 5],               # Mix
        # Stress tests
        [[i for i in range(100000)], 100],
        [[0]*100000, 12345],
        [[i for i in range(-50000, 50000)], 77]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t[0], t[1])).lower()
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Counting"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
