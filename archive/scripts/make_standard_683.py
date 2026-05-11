import json
import os

def generate_json():
    problem_id = 683
    title = "K Empty Slots"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>683. K Empty Slots</h3>
<p>You have <code>n</code> bulbs in a row numbered from <code>1</code> to <code>n</code>. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are turned on after <code>n</code> days.</p>

<p>You are given an array <code>bulbs</code> of length <code>n</code> where <code>bulbs[i] = x</code> means that on the <code>(i+1)<sup>th</sup></code> day, we will turn on the bulb at position <code>x</code> where <code>i</code> is <strong>0-indexed</strong> and <code>x</code> is <strong>1-indexed</strong>.</p>

<p>Given an integer <code>k</code>, return <em>the <strong>minimum day number</strong> such that there exists two <strong>turned on</strong> bulbs that have exactly</em> <code>k</code> <em>bulbs between them that are all turned off</em>. If there isn't such day, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> bulbs = [1,3,2], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong>
On the first day: bulbs[0] = 1, first bulb is turned on: [1, 0, 0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1, 0, 1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1, 1, 1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> bulbs = [1,2,3], k = 1
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>n == bulbs.length</code></li>
    <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= bulbs[i] &lt;= n</code></li>
    <li><code>bulbs</code> is a permutation of numbers from <code>1</code> to <code>n</code>.</li>
    <li><code>0 &lt;= k &lt;= 2 * 10<sup>4</sup></code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array `bulbs`.\nLine 2: Integer `k`."
    output_format = "An integer: minimum day or -1."

    constraints = [
        "1 <= n <= 2 * 10^4",
        "bulbs is a permutation of 1 to n",
        "0 <= k <= 2 * 10^4"
    ]

    explanation = """Build a `days` array where days[i] = day the bulb at position i+1 turns on. Use a sliding window of size k+2. For each window [left, right] (right = left+k+1), check if all bulbs inside (left+1 to right-1) have days >= max(days[left], days[right]). The answer is the earliest such valid day."""

    answer = """class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * (n + 1)
        for day, pos in enumerate(bulbs, 1):
            days[pos] = day
        
        result = float('inf')
        left, right = 1, k + 2
        
        while right <= n:
            valid = True
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    right = i + k + 1
                    valid = False
                    break
            if valid:
                result = min(result, max(days[left], days[right]))
                left = right
                right = left + k + 1
        
        return result if result != float('inf') else -1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        # User logic here
        return -1

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        bulbs = json.loads(raw[0])
        k = int(raw[1])
        sol = Solution()
        print(sol.kEmptySlots(bulbs, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int kEmptySlots(vector<int>& bulbs, int k) {
        // User logic here
        return -1;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            int val = 0;
            while (isdigit(input[i])) { val = val * 10 + (input[i] - '0'); i++; }
            res.push_back(val);
        } else i++;
    }
    return res;
}

int main() {
    string b_str, k_str;
    if (getline(cin, b_str) && getline(cin, k_str)) {
        vector<int> bulbs = parseArray(b_str);
        int k = stoi(k_str);
        Solution sol;
        cout << sol.kEmptySlots(bulbs, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int kEmptySlots(int[] bulbs, int k) {
        // User logic here
        return -1;
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
            String b_str = sc.nextLine().trim();
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                int[] bulbs = parseArray(b_str);
                Solution sol = new Solution();
                System.out.println(sol.kEmptySlots(bulbs, k));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} bulbs
 * @param {number} k
 * @return {number}
 */
var kEmptySlots = function(bulbs, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const bulbs = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(kEmptySlots(bulbs, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int kEmptySlots(int* bulbs, int bulbsSize, int k) {
    // User logic here
    return -1;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
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
    char b_str[500000];
    if (fgets(b_str, sizeof(b_str), stdin)) {
        int bulbsSize;
        int* bulbs = parseArray(b_str, &bulbsSize);
        int k;
        if (scanf("%d", &k) == 1) {
            printf("%d\\n", kEmptySlots(bulbs, bulbsSize, k));
        }
        free(bulbs);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(bulbs, k):
        n = len(bulbs)
        days = [0] * (n + 1)
        for day, pos in enumerate(bulbs, 1):
            days[pos] = day
        result = float('inf')
        left, right = 1, k + 2
        while right <= n:
            valid = True
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    right = i + k + 1
                    valid = False
                    break
            if valid:
                result = min(result, max(days[left], days[right]))
                left = right
                right = left + k + 1
        return result if result != float('inf') else -1

    test_cases_data = [
        ([1,3,2], 1),
        ([1,2,3], 1),
        ([3,1,2], 1),
        ([1,2,3,4,5], 2),
        ([5,4,3,2,1], 0),
        ([2,1,4,3], 1),
        ([1,3,5,2,4], 2),
        (list(range(1, 20001)), 1),
        (list(range(20000, 0, -1)), 0),
        ([1,3,2,4], 1)
    ]

    test_cases = []
    for i, (bulbs, k) in enumerate(test_cases_data):
        inp = json.dumps(bulbs) + "\\n" + str(k)
        out = str(solve(bulbs, k))
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
        "topics": ["Array", "Binary Search Indexed Set", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
