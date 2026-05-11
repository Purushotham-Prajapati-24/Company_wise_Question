import json
import os
import collections
import heapq

def generate_json():
    problem_id = 1054
    title = "Distant Barcodes"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1054. Distant Barcodes</h3>
<p>In a warehouse, there is a row of barcodes, where the <code>i<sup>th</sup></code> barcode is <code>barcodes[i]</code>.</p>

<p>Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> barcodes = [1,1,1,2,2,2]
<strong>Output:</strong> [1,2,1,2,1,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> barcodes = [1,1,1,1,2,2,3,3]
<strong>Output:</strong> [1,3,1,3,1,2,1,2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= barcodes.length &lt;= 10000</code></li>
	<li><code>1 &lt;= barcodes[i] &lt;= 10000</code></li>
</ul>
"""

    input_format = "An array of integers `barcodes` provided as `[barcodes]` in JSON."
    output_format = "An array of integers representing the rearranged barcodes."

    constraints = [
        "1 <= barcodes.length <= 10000",
        "1 <= barcodes[i] <= 10000"
    ]

    explanation = """To rearrange barcodes so no two adjacent are equal:
1. Count the frequency of each barcode.
2. Place the most frequent barcode first in even positions (0, 2, 4, ...).
3. If you run out of even positions, start filling odd positions (1, 3, 5, ...).
4. Fill all other barcodes in the remaining positions.
5. This ensures that the most frequent element never occupies adjacent positions since it is guaranteed an answer exists (max frequency <= (N+1)//2)."""

    answer = """class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        count = collections.Counter(barcodes)
        sorted_barcodes = sorted(count.items(), key=lambda x: -x[1])
        
        n = len(barcodes)
        res = [0] * n
        i = 0
        for code, freq in sorted_barcodes:
            for _ in range(freq):
                if i >= n:
                    i = 1
                res[i] = code
                i += 2
        return res"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        # User logic here
        return barcodes

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        barcodes = json.loads(raw)
        if isinstance(barcodes[0], list): barcodes = barcodes[0]
        sol = Solution()
        print(sol.rearrangeBarcodes(barcodes))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        // User logic here
        return barcodes;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json.parse(line);
        vector<int> barcodes;
        if (j.is_array() && j.size() > 0 && j[0].is_array()) barcodes = j[0].get<vector<int>>();
        else barcodes = j.get<vector<int>>();
        Solution sol;
        vector<int> res = sol.rearrangeBarcodes(barcodes);
        cout << json(res).dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        // User logic here
        return barcodes;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object raw = mapper.readValue(sc.nextLine(), Object.class);
            int[] barcodes;
            if (raw instanceof List && !((List)raw).isEmpty() && ((List)raw).get(0) instanceof List) {
                barcodes = mapper.convertValue(((List)raw).get(0), int[].class);
            } else {
                barcodes = mapper.convertValue(raw, int[].class);
            }
            int[] res = new Solution().rearrangeBarcodes(barcodes);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var rearrangeBarcodes = function(barcodes) {
    // User logic here
    return barcodes;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let barcodes = JSON.parse(input);
    if (Array.isArray(barcodes[0])) barcodes = barcodes[0];
    const res = rearrangeBarcodes(barcodes);
    console.log(JSON.stringify(res));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int* rearrangeBarcodes(int* barcodes, int barcodesSize, int* returnSize) {
    // User logic here
    *returnSize = barcodesSize;
    return barcodes;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 128, s = 0;
    int* barcodes = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; barcodes = realloc(barcodes, cap * sizeof(int)); }
        scanf("%d", &barcodes[s++]);
    }
    int rs;
    int* res = rearrangeBarcodes(barcodes, s, &rs);
    printf("[");
    for (int i = 0; i < rs; i++) printf("%d%s", res[i], i == rs - 1 ? "" : ",");
    printf("]\\n");
    free(barcodes);
    return 0;
}"""
    }

    def solve(barcodes):
        count = collections.Counter(barcodes)
        sorted_codes = sorted(count.items(), key=lambda x: -x[1])
        n = len(barcodes)
        res = [0] * n
        i = 0
        for code, freq in sorted_codes:
            for _ in range(freq):
                if i >= n: i = 1
                res[i] = code
                i += 2
        return res

    test_cases_data = [
        [[1,1,1,2,2,2]],               # Sample 1
        [[1,1,1,1,2,2,3,3]],           # Sample 2
        [[1,2,1,2,1,2]],
        [[1,1,2,2]],
        [[7,7,7,8,8,7,7]],             # Guaranteed answer exists
        [[1]],
        [[1,2,3,4]],
        # Stress tests
        [[1]*5000 + [2]*5000],
        [[i%100 for i in range(10000)]],
        [[100]*5001 + [1]*5000]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0].copy())).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Heap (Priority Queue)", "Greedy", "Counting Sort"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
