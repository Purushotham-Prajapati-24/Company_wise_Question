import json
import os

def generate_json():
    problem_id = 1395
    title = "Count Number of Teams"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1395. Count Number of Teams</h3>
<p>There are <code>n</code> soldiers standing in a line. Each soldier is assigned a <strong>unique</strong> rating value.</p>

<p>You have to form a team of 3 soldiers amongst them under the following rules:</p>

<ul>
	<li>Choose 3 soldiers with index (<code>i, j, k</code>) with rating (<code>rating[i], rating[j], rating[k]</code>).</li>
	<li>A team is valid if: (<code>rating[i] &lt; rating[j] &lt; rating[k]</code>) or (<code>rating[i] &gt; rating[j] &gt; rating[k]</code>) where (<code>0 &lt;= i &lt; j &lt; k &lt; n</code>).</li>
</ul>

<p>Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rating = [2,5,3,4,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rating = [2,1,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can't form any team given the conditions.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rating = [1,2,3,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == rating.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= rating[i] &lt;= 10<sup>5</sup></code></li>
	<li>All the integers in <code>rating</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "A list of integers `rating` as a JSON array."
    output_format = "An integer representing the number of valid teams."

    constraints = [
        "3 <= n <= 1000",
        "Unique rating values"
    ]

    explanation = """To count the number of valid teams of size 3:
1. For each soldier `j` (representing the middle soldier in the team):
   - Count how many soldiers to their left have a smaller rating (`ll`) and how many have a larger rating (`lg`).
   - Count how many soldiers to their right have a smaller rating (`rl`) and how many have a larger rating (`rg`).
2. The number of ascending teams `(i < j < k)` with `j` in the middle is `ll * rg`.
3. The number of descending teams `(i < j < k)` with `j` in the middle is `lg * rl`.
4. Sum up `ll * rg + lg * rl` for all soldiers `j` from index 1 to `n-2`.
5. Return the total count."""

    answer = """class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        res = 0
        for j in range(1, n - 1):
            ll = lg = rl = rg = 0
            for i in range(j):
                if rating[i] < rating[j]: ll += 1
                else: lg += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]: rl += 1
                else: rg += 1
            res += (ll * rg) + (lg * rl)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numTeams(self, rating: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        rating = json.loads(raw)
        sol = Solution()
        print(sol.numTeams(rating))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numTeams(vector<int>& rating) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> rating = json::parse(line);
        Solution sol;
        cout << sol.numTeams(rating) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int numTeams(int[] rating) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            int[] rating = mapper.readValue(sc.nextLine(), int[].class);
            System.out.println(new Solution().numTeams(rating));
        }
    }
}""",
        "javascript": """var numTeams = function(rating) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(numTeams(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int numTeams(int* rating, int ratingSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(rating):
        n = len(rating)
        res = 0
        for j in range(1, n-1):
            ll = sum(1 for i in range(j) if rating[i] < rating[j])
            lg = j - ll
            rl = sum(1 for k in range(j+1, n) if rating[k] < rating[j])
            rg = (n - 1 - j) - rl
            res += ll * rg + lg * rl
        return res

    test_cases_data = [
        [2,5,3,4,1],     # Sample 1
        [2,1,3],         # Sample 2
        [1,2,3,4],       # Sample 3
        [4,3,2,1],       # Decreasing
        [1,5,10,2,8],     # Mixed
        [1,10,2,9,3],     # Up-down
        # Stress tests
        [i for i in range(1, 1001)],
        [i for i in range(1000, 0, -1)],
        [1, 1000, 2, 999, 3, 998]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = str(solve(t))
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Dynamic Programming", "Binary Indexed Tree", "Segment Tree"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
