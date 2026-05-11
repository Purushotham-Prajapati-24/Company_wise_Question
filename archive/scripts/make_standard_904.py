import json
import os

def generate_json():
    problem_id = 904
    title = "Fruit Into Baskets"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>904. Fruit Into Baskets</h3>
<p>You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array <code>fruits</code> where <code>fruits[i]</code> is the type of fruit the <code>i<sup>th</sup></code> tree produces.</p>

<p>You want to collect as much fruit as possible. However, the owner has strict rules that you must follow:</p>

<ul>
    <li>You only have <strong>two</strong> baskets, and each basket can only hold a <strong>single type</strong> of fruit. There is no limit on the amount of fruit each basket can hold.</li>
    <li>Starting from any tree of your choice, you must pick <strong>exactly one fruit</strong> from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.</li>
    <li>Once you reach a tree with fruit that cannot fit in your baskets, you must stop.</li>
</ul>

<p>Given the integer array <code>fruits</code>, return <em>the <strong>maximum</strong> number of fruits you can pick</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> fruits = [1,2,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can pick from all 3 trees.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> fruits = [0,1,2,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can pick from [1,2,2].
If we had started at the first tree, we would only pick from [0,1].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> fruits = [1,2,3,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can pick from [2,3,2,2].
If we had started at the first tree, we would only pick from [1,2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= fruits.length &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>"""

    input_format = "A single line containing the JSON array `fruits`."
    output_format = "An integer representing the maximum number of fruits picked."

    constraints = [
        "1 <= fruits.length <= 10^5",
        "0 <= fruits[i] < fruits.length"
    ]

    explanation = """To find the maximum number of fruits, we use a sliding window approach with two pointers (`left` and `right`) and a frequency map to keep track of the fruit types in our current window. Whenever the number of fruit types exceeds 2, we increment `left` and update the map until the number of types is back to 2. The maximum window size `right - left + 1` across the process is the answer."""

    answer = """class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = {}
        l = 0
        ans = 0
        for r, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        fruits = json.loads(raw)
        sol = Solution()
        print(sol.totalFruit(fruits))""",
        "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <ctype.h>

using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
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
    string input;
    if (cin >> input) {
        auto fruits = parseArray(input);
        Solution sol;
        cout << sol.totalFruit(fruits) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int totalFruit(int[] fruits) {
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
            int[] fruits = parseArray(sc.next());
            Solution sol = new Solution();
            System.out.println(sol.totalFruit(fruits));
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(totalFruit(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int totalFruit(int* fruits, int fruitsSize) {
    // User logic here
    return 0;
}

int main() {
    char input[100000];
    if (scanf("%s", input) == 1) {
        int sz = 0, cap = 100;
        int* arr = malloc(cap * sizeof(int));
        char* token = strtok(input+1, ",]");
        while (token != NULL) {
            if (sz == cap) arr = realloc(arr, (cap *= 2) * sizeof(int));
            arr[sz++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%d\\n", totalFruit(arr, sz));
        free(arr);
    }
    return 0;
}"""
    }

    def solve(fruits):
        count = {}
        l = 0
        ans = 0
        for r, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans

    test_cases_data = [
        [1,2,1],
        [0,1,2,2],
        [1,2,3,2,2],
        [3,3,3,1,2,1,1,2,3,3,4],
        [1],
        [1,1,1,1,1],
        [1,2,1,2,3,2,2],
        [0,0,1,1,2,2,3,3],
        [1,2,3],
        [1,2,1,2,1,2]
    ]

    test_cases = []
    for i, fruits in enumerate(test_cases_data):
        inp = json.dumps(fruits).replace(" ", "")
        out = str(solve(fruits))
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
        "topics": ["Array", "Hash Table", "Sliding Window"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
