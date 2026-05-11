import json
import os
import math

def generate_json():
    problem_id = 875
    title = "Koko Eating Bananas"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>875. Koko Eating Bananas</h3>
<p>Koko loves to eat bananas. There are <code>n</code> piles of bananas, the <code>i<sup>th</sup></code> pile has <code>piles[i]</code> bananas. The guards have gone and will come back in <code>h</code> hours.</p>

<p>Koko can decide her bananas-per-hour eating speed of <code>k</code>. Each hour, she chooses some pile of bananas and eats <code>k</code> bananas from that pile. If the pile has less than <code>k</code> bananas, she eats all of them instead and will not eat any more bananas during this hour.</p>

<p>Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.</p>

<p>Return <em>the minimum integer </em><code>k</code><em> such that she can eat all the bananas within </em><code>h</code><em> hours</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> piles = [3,6,7,11], h = 8
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> piles = [30,11,23,4,20], h = 5
<strong>Output:</strong> 30
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> piles = [30,11,23,4,20], h = 6
<strong>Output:</strong> 23
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= piles.length &lt;= 10<sup>4</sup></code></li>
    <li><code>piles.length &lt;= h &lt;= 10<sup>9</sup></code></li>
    <li><code>1 &lt;= piles[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `piles`\nLine 2: integer `h`"
    output_format = "An integer representing the minimum speed `k`."

    constraints = [
        "1 <= piles.length <= 10^4",
        "piles.length <= h <= 10^9",
        "1 <= piles[i] <= 10^9"
    ]

    explanation = """To find the minimum speed `k`, we can perform a binary search on the range of possible speeds. The minimum speed `k` is 1, and the maximum speed `k` is the maximum value in `piles` (as she only eats one pile per hour). For each speed `k` in our binary search, we calculate the total time it would take to finish all piles. If the time is within `h`, we try a smaller speed; otherwise, we try a larger speed."""

    answer = """import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def timeToEat(k):
            return sum(math.ceil(p / k) for p in piles)
        
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if timeToEat(mid) <= h:
                high = mid
            else:
                low = mid + 1
        return low"""

    boilerplate = {
        "python": """import sys
import json
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        piles = json.loads(raw[0].strip())
        h = int(raw[1].strip())
        sol = Solution()
        print(sol.minEatingSpeed(piles, h))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // User logic here
        return 0;
    }
};

vector<int> parseArray(string s) {
    auto res = vector<int>();
    size_t i = 1;
    while (i < s.length() - 1) {
        if (isdigit(s[i])) {
            long long val=0; int off=0;
            sscanf(s.c_str()+i, "%lld%n", &val, &off);
            res.push_back((int)val); i += off;
        } else i++;
    }
    return res;
}

int main() {
    string pStr; int h;
    if (cin >> pStr >> h) {
        auto piles = parseArray(pStr);
        Solution sol;
        cout << sol.minEatingSpeed(piles, h) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
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
        if (sc.hasNext()) {
            int[] piles = parseArray(sc.next());
            int h = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.minEatingSpeed(piles, h));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    let piles = JSON.parse(input[0]);
    let h = parseInt(input[1]);
    console.log(minEatingSpeed(piles, h));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minEatingSpeed(int* piles, int pilesSize, int h) {
    // User logic here
    return 0;
}

int main() {
    char input[100000]; int h;
    if (scanf("%s %d", input, &h) == 2) {
        int cap = 100, sz = 0;
        int* arr = malloc(cap * sizeof(int));
        char* token = strtok(input+1, ",]");
        while (token != NULL) {
            if (sz == cap) arr = realloc(arr, (cap *= 2) * sizeof(int));
            arr[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%d\\n", minEatingSpeed(arr, sz, h));
        free(arr);
    }
    return 0;
}"""
    }

    def solve(piles, h):
        def timeToEat(k):
            res = 0
            for p in piles:
                res += math.ceil(p / k)
            return res
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if timeToEat(mid) <= h:
                high = mid
            else:
                low = mid + 1
        return low

    test_cases_data = [
        ([3,6,7,11], 8),
        ([30,11,23,4,20], 5),
        ([30,11,23,4,20], 6),
        ([1,1,1,1,1,1,1,1], 8),
        ([1000000000], 1000000000),
        ([1,2,3,4,10], 20),
        ([312884470,968560155,612328766,742185563,156474448,531232876], 1000000000),
        ([30,11,23,4,20], 100),
        ([4,11,20,23,30], 10),
        ([10], 15)
    ]

    test_cases = []
    for i, (piles, h) in enumerate(test_cases_data):
        inp = f"{json.dumps(piles).replace(' ', '')}\n{h}"
        out = str(solve(piles, h))
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
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
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
