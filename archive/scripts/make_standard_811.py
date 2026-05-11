import json
import os
from collections import defaultdict

def generate_json():
    problem_id = 811
    title = "Subdomain Visit Count"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>811. Subdomain Visit Count</h3>
<p>A count-paired domain is a domain that has a specific count associated with it, e.g., "9001 discuss.leetcode.com". This means that the domain "discuss.leetcode.com" was visited 9001 times.</p>

<p>When a website domain is visited, all of its parent subdomains are also implicitly visited. For example, if you visit "discuss.leetcode.com", you are also visiting "leetcode.com" and "com".</p>

<p>Given an array of count-paired domains <code>cpdomains</code>, return <em>an array of the <strong>count-paired domains</strong> of each subdomain in the input</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> cpdomains = ["9001 discuss.leetcode.com"]
<strong>Output:</strong> ["9001 discuss.leetcode.com","9001 leetcode.com","9001 com"]
<strong>Explanation:</strong> We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
<strong>Output:</strong> ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
<strong>Explanation:</strong> We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" 1 time and "wiki.org" 5 times.
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= cpdomains.length &lt;= 100</code></li>
    <li><code>1 &lt;= cpdomains[i].length &lt;= 100</code></li>
    <li><code>cpdomains[i]</code> follows either the <code>"rep d1.d2.d3"</code> format or the <code>"rep d1.d2"</code> format.</li>
    <li><code>rep</code> is an int in the range <code>[1, 10<sup>4</sup>]</code>.</li>
    <li><code>d1</code>, <code>d2</code>, and <code>d3</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "A JSON array of strings `cpdomains`."
    output_format = "A JSON array of strings representing counts and subdomains."

    constraints = [
        "1 <= cpdomains.length <= 100",
        "1 <= rep <= 10000"
    ]

    explanation = """For each count-paired domain, split it into the count and the domain. Then generate all subdomains by finding each dot separator. Use a hash map to aggregate counts for each distinct subdomain."""

    answer = """class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                counts[".".join(frags[i:])] += count
        return ["{} {}".format(v, k) for k, v in counts.items()]"""

    boilerplate = {
        "python": """import sys
import json
import collections

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        cpdomains = json.loads(raw)
        sol = Solution()
        res = sol.subdomainVisits(cpdomains)
        res.sort()
        print(json.dumps(res).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        // User logic here
        return {};
    }
};

int main() {
    string input;
    if (cin >> input) {
        // Basic JSON string array parser
        vector<string> arr;
        size_t i = 1;
        while (i < input.length() - 1) {
            if (input[i] == '"') {
                i++; size_t start = i;
                while (input[i] != '"') i++;
                arr.push_back(input.substr(start, i - start));
                i++;
            } else i++;
        }
        Solution sol;
        auto res = sol.subdomainVisits(arr);
        sort(res.begin(), res.end());
        cout << "[";
        for (int i=0; i<res.size(); ++i) {
            cout << "\\"" << res[i] << "\\"" << (i+1==res.size()?"":",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            input = input.substring(1, input.length()-1);
            String[] arr;
            if (input.isEmpty()) arr = new String[0];
            else {
                String[] parts = input.split(",");
                arr = new String[parts.length];
                for (int i=0; i<parts.length; i++) {
                    String p = parts[i].trim();
                    arr[i] = p.substring(1, p.length()-1);
                }
            }
            Solution sol = new Solution();
            List<String> res = sol.subdomainVisits(arr);
            Collections.sort(res);
            System.out.print("[");
            for (int i=0; i<res.size(); i++) {
                System.out.print("\\"" + res.get(i) + "\\"" + (i+1==res.size()?"":","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const res = subdomainVisits(JSON.parse(input));
    res.sort();
    console.log(JSON.stringify(res).replace(/ /g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** subdomainVisits(char** cpdomains, int cpdomainsSize, int* returnSize) {
    // User logic here
    return NULL;
}

int main() {
    char input[20000];
    if (scanf("%s", input) == 1) {
        int cap = 100, sz = 0;
        char** arr = malloc(cap * sizeof(char*));
        size_t i = 1;
        while (input[i] && input[i+1]) {
            if (input[i] == '"') {
                i++; size_t start = i;
                while (input[i] != '"') i++;
                int len = i - start;
                arr[sz] = malloc(len + 1);
                strncpy(arr[sz], input + start, len);
                arr[sz][len] = '\\0';
                sz++; i++;
            } else i++;
        }
        int outSz;
        char** res = subdomainVisits(arr, sz, &outSz);
        printf("[");
        for (int i=0; i<outSz; i++) {
            printf("\\"%s\\"%s", res[i], i+1==outSz?"":",");
        }
        printf("]\\n");
    }
    return 0;
}"""
    }

    def solve(cpdomains):
        counts = defaultdict(int)
        for cp in cpdomains:
            c, d = cp.split()
            c = int(c)
            frags = d.split('.')
            for i in range(len(frags)):
                counts[".".join(frags[i:])] += c
        res = [f"{v} {k}" for k, v in counts.items()]
        res.sort()
        return res

    test_cases_data = [
        (["9001 discuss.leetcode.com"]),
        (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]),
        (["1000 a.b.c.d.e"]),
        (["1 a", "2 a.b", "3 a.b.c"]),
        (["999 longsubdomain.name.com", "1 longsubdomain.name.com"]),
        (["10000 x.y", "1 y"]),
        (["1 a.com", "1 b.com", "1 c.com"]),
        (["100 a.b", "200 b.c", "300 c.a"]),
        (["1 a.b.c.d", "1 b.c.d", "1 c.d", "1 d"]),
        (["1000 subdomain.with.many.parts.com"])
    ]

    test_cases = []
    for i, domains in enumerate(test_cases_data):
        inp = json.dumps(domains).replace(" ", "")
        out = json.dumps(solve(domains)).replace(" ", "")
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
        "topics": ["Array", "Hash Table", "String", "Counting"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
