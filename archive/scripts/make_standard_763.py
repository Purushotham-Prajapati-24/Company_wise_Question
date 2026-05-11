import json
import os

def generate_json():
    problem_id = 763
    title = "Partition Labels"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>763. Partition Labels</h3>
<p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in at most one part.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resultant string should be <code>s</code>.</p>

<p>Return <em>a list of integers representing the size of these parts</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ababcbacadefegdehijhklij"
<strong>Output:</strong> [9,7,8]
<strong>Explanation:</strong>
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "eccbbbbdec"
<strong>Output:</strong> [10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= s.length &lt;= 500</code></li>
    <li><code>s</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing the string `s`."
    output_format = "A JSON array of integers."

    constraints = [
        "1 <= s.length <= 500",
        "s consists of lowercase English letters."
    ]

    explanation = """First, find the last occurrence index for every character in the string. Then iterate over the string, keeping track of the `end` of the current partition, which is the maximum last occurrence of any character seen so far in this partition. Once your current index matches `end`, you've found a valid partition ending. Record the length and start a new partition."""

    answer = """class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        if raw.startswith('"') and raw.endswith('"'):
            s = json.loads(raw)
        else:
            s = raw
        sol = Solution()
        print(json.dumps(sol.partitionLabels(s)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        // User logic here
        return {};
    }
};

int main() {
    string s;
    if (cin >> s) {
        if (s.length() >= 2 && s.front() == '"' && s.back() == '"') {
            s = s.substr(1, s.length() - 2);
        }
        Solution sol;
        vector<int> res = sol.partitionLabels(s);
        cout << "[";
        for (size_t i = 0; i < res.size(); ++i) {
            cout << res[i] << (i + 1 == res.size() ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> partitionLabels(String s) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNext()) {
            String s = sc.next();
            if (s.length() >= 2 && s.startsWith("\\"") && s.endsWith("\\"")) {
                s = s.substring(1, s.length() - 1);
            }
            Solution sol = new Solution();
            List<Integer> res = sol.partitionLabels(s);
            System.out.print("[");
            for (int i = 0; i < res.size(); i++) {
                System.out.print(res.get(i) + (i + 1 == res.size() ? "" : ","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let s = input;
    if (s.startsWith('"') && s.endsWith('"')) {
        s = JSON.parse(s);
    }
    console.log(JSON.stringify(partitionLabels(s)).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* partitionLabels(char* s, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    char s[1000];
    if (scanf("%s", s) == 1) {
        char* str = s;
        int len = strlen(s);
        if (len >= 2 && s[0] == '"' && s[len-1] == '"') {
            s[len-1] = '\\0';
            str = s + 1;
        }
        int returnSize = 0;
        int* res = partitionLabels(str, &returnSize);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("%d%s", res[i], i == returnSize - 1 ? "" : ",");
        }
        printf("]\\n");
        if(res) free(res);
    }
    return 0;
}"""
    }

    def solve(s):
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last.get(c, 0))
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

    test_cases_data = [
        "ababcbacadefegdehijhklij",
        "eccbbbbdec",
        "a",
        "abcdefghijklmnopqrstuvwxyz",
        "aaaaaaaaaa",
        "abbbba",
        "abaccbc",
        "abccba",
        "abc" * 150,
        "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    ]

    test_cases = []
    for i, s in enumerate(test_cases_data):
        inp = json.dumps(s)
        out = json.dumps(solve(s)).replace(" ", "")
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
        "topics": ["Hash Table", "Two Pointers", "String", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
