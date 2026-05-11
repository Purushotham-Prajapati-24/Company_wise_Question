import json
import os

def generate_json():
    problem_id = 2418
    title = "Sort the People"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>2418. Sort the People</h3>
<p>You are given an array of strings <code>names</code>, and an array <code>heights</code> that consists of <strong>distinct</strong> positive integers. Both arrays are of length <code>n</code>.</p>

<p>For each index <code>i</code>, <code>names[i]</code> and <code>heights[i]</code> denote the name and height of the <code>i<sup>th</sup></code> person.</p>

<p>Return <code>names</code><em> sorted in <strong>descending</strong> order by the people&#39;s heights</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> names = [&quot;Mary&quot;,&quot;John&quot;,&quot;Emma&quot;], heights = [180,165,170]
<strong>Output:</strong> [&quot;Mary&quot;,&quot;Emma&quot;,&quot;John&quot;]
<strong>Explanation:</strong> Mary is the tallest, followed by Emma and John.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> names = [&quot;Alice&quot;,&quot;Bob&quot;,&quot;Bob&quot;], heights = [155,185,150]
<strong>Output:</strong> [&quot;Bob&quot;,&quot;Alice&quot;,&quot;Bob&quot;]
<strong>Explanation:</strong> The first Bob is the tallest, followed by Alice and the second Bob.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == names.length == heights.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= names[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>names[i]</code> consists of lower and upper case English letters.</li>
	<li>All the values of <code>heights</code> are distinct.</li>
</ul>
"""

    input_format = "An array of strings `names` and an array of integers `heights` provided as `[names, heights]` in JSON."
    output_format = "An array of strings sorted descending by heights."

    constraints = [
        "1 <= n <= 10^3",
        "names[i].length <= 20",
        "heights are distinct"
    ]

    explanation = """To sort people by height in descending order:
1. Pair each name with its corresponding height.
2. Sort these pairs based on the height in descending order.
3. Extract the names from the sorted pairs and return them."""

    answer = """class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        combined = sorted(zip(heights, names), reverse=True)
        return [name for height, name in combined]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        names, heights = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.sortPeople(names, heights)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        // User logic here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<string> names = j[0].get<vector<string>>();
        vector<int> heights = j[1].get<vector<int>>();
        Solution sol;
        vector<string> res = sol.sortPeople(names, heights);
        json out = res;
        cout << out.dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // User logic here
        return new String[0];
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            String[] names = mapper.convertValue(data[0], String[].class);
            int[] heights = mapper.convertValue(data[1], int[].class);
            String[] res = new Solution().sortPeople(names, heights);
            System.out.println(mapper.writeValueAsString(res).replace(" ", ""));
        }
    }
}""",
        "javascript": """var sortPeople = function(names, heights) {
    // User logic here
    return [];
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [names, heights] = JSON.parse(input);
    console.log(JSON.stringify(sortPeople(names, heights)).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char** sortPeople(char** names, int namesSize, int* heights, int heightsSize, int* returnSize) {
    // User logic here
    return names;
}

char* read_json_string() {
    int c;
    while ((c = getchar()) != EOF && c != '"');
    if (c == EOF) return NULL;
    int cap = 128, len = 0;
    char* str = malloc(cap);
    while ((c = getchar()) != EOF && c != '"') {
        if (len + 1 >= cap) { cap *= 2; str = realloc(str, cap); }
        str[len++] = c;
    }
    str[len] = '\\0';
    return str;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int n_cap = 100, n_size = 0;
    char** names = malloc(n_cap * sizeof(char*));
    while (1) {
        char* s = read_json_string();
        if (!s) break;
        if (n_size >= n_cap) { n_cap *= 2; names = realloc(names, n_cap * sizeof(char*)); }
        names[n_size++] = s;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']') break;
    }
    while ((c = getchar()) != EOF && c != '[');
    int h_cap = 100, h_size = 0;
    int* heights = malloc(h_cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (h_size >= h_cap) { h_cap *= 2; heights = realloc(heights, h_cap * sizeof(int)); }
        scanf("%d", &heights[h_size++]);
    }
    int retSize;
    char** res = sortPeople(names, n_size, heights, h_size, &retSize);
    printf("[");
    for (int i=0; i<retSize; i++) {
        printf("\\"%s\\"", res[i]);
        if (i < retSize - 1) printf(",");
    }
    printf("]\\n");
    return 0;
}"""
    }

    def solve(names, heights):
        combined = sorted(zip(heights, names), reverse=True)
        return [name for height, name in combined]

    test_cases_data = [
        [["Mary","John","Emma"], [180,165,170]], # Sample 1
        [["Alice","Bob","Bob"], [155,185,150]], # Sample 2
        [["A","B","C"], [1,2,3]],              # Descending heights needed
        [["Z","Y","X"], [10,20,30]], 
        [["Single"], [100]],                    # Single person
        [["A","B","C","D","E"], [10,50,30,20,40]],
        [["Small","Large"], [5,10]],
        # Stress tests
        [[f"P{i}" for i in range(1000)], list(range(1, 1001))],
        [[f"Name{i}" for i in range(1000)], list(range(1000, 0, -1))],
        [["X"]*1000, [i for i in range(1000, 2000)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 2})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "String", "Sorting"], "companyIndex": 0
    }

    output_path = f"2401-2600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
