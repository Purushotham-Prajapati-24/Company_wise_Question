import json
import os

def generate_json():
    problem_id = 1946
    title = "Largest Number After Mutating Substring"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1946. Largest Number After Mutating Substring</h3>
<p>You are given a string <code>num</code>, which represents a large integer. You are also given a <strong>0-indexed</strong> integer array <code>change</code> of length <code>10</code> that maps each digit <code>0-9</code> to another digit. More formally, digit <code>d</code> maps to digit <code>change[d]</code>.</p>

<p>You may <strong>mutate</strong> any <strong>substring</strong> of <code>num</code>. To mutate a substring, replace each digit <code>num[i]</code> with the digit it maps to in <code>change</code> (i.e. replace <code>num[i]</code> with <code>change[num[i] - '0']</code>).</p>

<p>Return <em>a string representing the <strong>largest</strong> possible integer after <strong>mutating</strong> (or choosing not to) any <strong>substring</strong> of</em> <code>num</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;132&quot;, change = [9,8,5,0,3,6,4,2,6,8]
<strong>Output:</strong> &quot;832&quot;
<strong>Explanation:</strong> Replace the substring &quot;1&quot;:
- 1 maps to change[1] = 8.
Thus, &quot;132&quot; becomes &quot;832&quot;.
&quot;832&quot; is the largest number possible, so return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;021&quot;, change = [9,4,3,5,7,2,1,9,0,6]
<strong>Output:</strong> &quot;943&quot;
<strong>Explanation:</strong> Replace the substring &quot;021&quot;:
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, &quot;021&quot; becomes &quot;943&quot;.
&quot;943&quot; is the largest number possible, so return it.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;5&quot;, change = [1,4,7,5,3,2,5,6,9,4]
<strong>Output:</strong> &quot;5&quot;
<strong>Explanation:</strong> &quot;5&quot; is already the largest number that can be created, so return it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> consists of only digits <code>0-9</code>.</li>
	<li><code>change.length == 10</code></li>
	<li><code>0 &lt;= change[d] &lt;= 9</code></li>
</ul>
"""

    input_format = "A string `num` and an integer array `change` provided as `[num, change]` in JSON."
    output_format = "A string representing the largest mutated number."

    constraints = [
        "1 <= num.length <= 10^5",
        "change.length == 10",
        "0 <= change[d] <= 9"
    ]

    explanation = """To find the largest number:
1. Iterate through the string `num` from left to right.
2. Find the first character `num[i]` such that its mutation `change[num[i]-'0']` strictly increases its value.
3. Once such a character is found, start mutating characters consecutively as long as the mutation results in a value that is greater than or equal to the original digit.
4. Stop mutating as soon as you encounter a digit whose mutation would decrease its value.
5. Return the potentially mutated string."""

    answer = """class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        res = list(num)
        mutated = False
        for i in range(len(res)):
            d = int(res[i])
            if change[d] > d:
                res[i] = str(change[d])
                mutated = True
            elif change[d] < d:
                if mutated:
                    break
        return "".join(res)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        # User logic here
        return num

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        num, change = json.loads(raw)
        sol = Solution()
        print(sol.maximumNumber(num, change))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string maximumNumber(string num, vector<int>& change) {
        // User logic here
        return num;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        string num = j[0].get<string>();
        vector<int> change = j[1].get<vector<int>>();
        Solution sol;
        cout << sol.maximumNumber(num, change) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String maximumNumber(String num, int[] change) {
        // User logic here
        return num;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            String num = (String) data[0];
            int[] change = mapper.convertValue(data[1], int[].class);
            System.out.println(new Solution().maximumNumber(num, change));
        }
    }
}""",
        "javascript": """var maximumNumber = function(num, change) {
    // User logic here
    return num;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [num, change] = JSON.parse(input);
    console.log(maximumNumber(num, change));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* maximumNumber(char * num, int* change, int changeSize) {
    // User logic here
    return num;
}

char* read_json_string() {
    int c;
    while ((c = getchar()) != EOF && c != '"');
    if (c == EOF) return NULL;
    int cap = 100005, len = 0;
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
    char* num = read_json_string();
    while ((c = getchar()) != EOF && c != '[');
    int change[10];
    for (int i=0; i<10; i++) {
        while ((c = getchar()) != EOF && !isdigit(c));
        ungetc(c, stdin);
        scanf("%d", &change[i]);
    }
    printf("%s\\n", maximumNumber(num, change, 10));
    free(num);
    return 0;
}"""
    }

    def solve(num, change):
        res = list(num)
        mutated = False
        for i in range(len(res)):
            d = int(res[i])
            if change[d] > d:
                res[i] = str(change[d])
                mutated = True
            elif change[d] < d:
                if mutated: break
        return "".join(res)

    test_cases_data = [
        ["132", [9,8,5,0,3,6,4,2,6,8]],   # Sample 1
        ["021", [9,4,3,5,7,2,1,9,0,6]],   # Sample 2
        ["5", [1,4,7,5,3,2,5,6,9,4]],     # Sample 3
        ["000", [1,1,1,1,1,1,1,1,1,1]],   # 0 to 1
        ["999", [0,0,0,0,0,0,0,0,0,0]],   # 9 to 0
        ["123456", [1,2,3,4,5,6,7,8,9,0]], # No strict increase
        ["123456", [2,2,3,4,5,6,7,8,9,0]], # Single increase
        # Stress tests
        ["1"*100000, [2,2,2,2,2,2,2,2,2,2]],
        ["9"*100000, [8,8,8,8,8,8,8,8,8,8]],
        ["1" + "0"*99998 + "1", [1,2,3,4,5,6,7,8,9,0]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = solve(t[0], t[1])
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "String", "Greedy"], "companyIndex": 0
    }

    output_path = f"1901-2100/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
