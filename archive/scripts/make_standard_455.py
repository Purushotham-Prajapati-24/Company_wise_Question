import json
import os

def generate_json():
    problem_id = 455
    title = "Assign Cookies"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>455. Assign Cookies</h3>
<p>Assume you are a awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.</p>

<p>Each child <code>i</code> has a greed factor <code>g[i]</code>, which is the minimum size of a cookie that the child will be content with; and each cookie <code>j</code> has a size <code>s[j]</code>. If <code>s[j] &gt;= g[i]</code>, we can assign the cookie <code>j</code> to the child <code>i</code>, and the child <code>i</code> will be content. Your goal is to maximize the number of your content children and output the maximum number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> g = [1,2,3], s = [1,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> g = [1,2], s = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= g.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= g[i], s[j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "Two lines, each containing a JSON array of integers: the first for greed factors `g`, and the second for cookie sizes `s`."
    output_format = "An integer representing the maximum number of content children."
    
    constraints = [
        "1 <= g.length <= 3 * 10^4",
        "0 <= s.length <= 3 * 10^4",
        "1 <= g[i], s[j] <= 2^31 - 1"
    ]
    
    explanation = "This is a greedy problem. Sort both the greed factors and the cookie sizes. Iterate through the cookies, and for each cookie, check if it can satisfy the current child with the smallest greed factor. If it can, move to the next child. Count the number of children satisfied."
    
    answer = """class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_i = 0
        cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    lines = sys.stdin.read().strip().splitlines()
    if len(lines) >= 2:
        g = json.loads(lines[0])
        s = json.loads(lines[1])
        sol = Solution()
        print(sol.findContentChildren(g, s))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // User Logic Here
        return 0;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    string current;
    for (char c : input) {
        if (isdigit(c) || c == '-') current += c;
        else if (!current.empty()) {
            res.push_back(stoi(current));
            current = "";
        }
    }
    if (!current.empty()) res.push_back(stoi(current));
    return res;
}

int main() {
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        vector<int> g = parseArray(line1);
        vector<int> s = parseArray(line2);
        Solution sol;
        cout << sol.findContentChildren(g, s) << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line1 = sc.nextLine().trim();
            int[] g = parse(line1);
            if (!sc.hasNextLine()) {
                System.out.println(0);
                return;
            }
            String line2 = sc.nextLine().trim();
            int[] s = parse(line2);
            Solution sol = new Solution();
            System.out.println(sol.findContentChildren(g, s));
        }
    }
    private static int[] parse(String input) {
        String[] parts = input.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
        if (parts.length == 0 || (parts.length == 1 && parts[0].isEmpty())) return new int[0];
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i]);
        return res;
    }
}""",
        "javascript": r"""/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');
if (input.length >= 2) {
    const g = JSON.parse(input[0]);
    const s = JSON.parse(input[1]);
    console.log(findContentChildren(g, s));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    // User Logic Here
    return 0;
}

int main() {
    // Manual parsing logic...
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,2,3]\\n[1,1]", "expected_output": "1", "is_sample": True},
        {"input": "[1,2]\\n[1,2,3]", "expected_output": "2", "is_sample": True},
        {"input": "[1,2,3]\\n[3,2,1]", "expected_output": "3", "is_sample": False},
        {"input": "[10,9,8,7]\\n[5,6,7,8]", "expected_output": "2", "is_sample": False},
        {"input": "[1,2,3]\\n[]", "expected_output": "0", "is_sample": False},
        {"input": "[]\\n[1,2,3]", "expected_output": "0", "is_sample": False},
        {"input": "[1,2,3]\\n[  1,   1 ]", "expected_output": "1", "is_sample": False}, # Spaces
        {"input": "[10^9, 10^9]\\n[10^9]", "expected_output": "1", "is_sample": False},
        # Stress
        {"input": json.dumps([i for i in range(1, 1001)]) + "\\n" + json.dumps([i for i in range(1, 1001)]), "expected_output": "1000", "is_sample": False},
        {"input": json.dumps([1000]*500) + "\\n" + json.dumps([1]*1000), "expected_output": "0", "is_sample": False}
    ]

    data = {
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Greedy", "Sorting"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Assign_Cookies.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
