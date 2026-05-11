import json
import os

def generate_json():
    problem_id = 1798
    title = "Maximum Number of Consecutive Values You Can Make"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1798. Maximum Number of Consecutive Values You Can Make</h3>
<p>You are given an integer array <code>coins</code> of length <code>n</code> which represents the <code>n</code> coins you have. The value of the <code>i<sup>th</sup></code> coin is <code>coins[i]</code>. You can make some number of consecutive integer values, starting from <code>0</code>, using these coins.</p>

<p>Return the maximum number of consecutive integer values that you can make <strong>starting from 0</strong>.</p>

<p>Note that you may have multiple coins of the same value.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coins = [1,3]
<strong>Output:</strong> 2
<strong>Explanation: </strong>You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coins = [1,1,1,4]
<strong>Output:</strong> 8
<strong>Explanation: </strong>You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,10,3,1]
<strong>Output:</strong> 20</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>coins.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= coins[i] &lt;= 4 * 10<sup>4</sup></code></li>
</ul>
"""

    input_format = "An array of integers `coins` provided as `[coins]` in JSON."
    output_format = "An integer representing the maximum consecutive values."

    constraints = [
        "1 <= n <= 4 * 10^4",
        "1 <= coins[i] <= 4 * 10^4"
    ]

    explanation = """To find the maximum consecutive values:
1. Sort the coins in ascending order.
2. Maintain a variable `max_val` representing that we can make all values from `0` to `max_val`. Initially `max_val = 0`.
3. Iterate through each coin `c`:
   - If `c <= max_val + 1`, then we can extend our range to `max_val + c`.
   - If `c > max_val + 1`, we cannot make `max_val + 1`, so stop.
4. The result is the total number of values, which is `max_val + 1`."""

    answer = """class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        res = 1
        for c in coins:
            if c > res:
                break
            res += c
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        coins = json.loads(raw)
        if isinstance(coins[0], list): coins = coins[0]
        sol = Solution()
        print(sol.getMaximumConsecutive(coins))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        vector<int> coins;
        if (j.is_array() && !j.empty() && j[0].is_array()) coins = j[0].get<vector<int>>();
        else coins = j.get<vector<int>>();
        Solution sol;
        cout << sol.getMaximumConsecutive(coins) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int getMaximumConsecutive(int[] coins) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            JsonNode node = mapper.readTree(sc.nextLine());
            int[] coins;
            if (node.isArray() && node.size() > 0 && node.get(0).isArray()) {
                coins = mapper.convertValue(node.get(0), int[].class);
            } else {
                coins = mapper.convertValue(node, int[].class);
            }
            System.out.println(new Solution().getMaximumConsecutive(coins));
        }
    }
}""",
        "javascript": """var getMaximumConsecutive = function(coins) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    let coins = JSON.parse(input);
    if (Array.isArray(coins[0])) coins = coins[0];
    console.log(getMaximumConsecutive(coins));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int getMaximumConsecutive(int* coins, int coinsSize) {
    // User logic here
    return 0;
}

int main() {
    int c;
    while ((c = getchar()) != EOF && c != '[');
    int cap = 1024, s = 0;
    int* coins = malloc(cap * sizeof(int));
    while (1) {
        while ((c = getchar()) != EOF && !isdigit(c) && c != '-' && c != ']');
        if (c == EOF || c == ']') break;
        ungetc(c, stdin);
        if (s >= cap) { cap *= 2; coins = realloc(coins, cap * sizeof(int)); }
        scanf("%d", &coins[s++]);
    }
    printf("%d\\n", getMaximumConsecutive(coins, s));
    free(coins);
    return 0;
}"""
    }

    def solve(coins):
        coins.sort()
        res = 1
        for c in coins:
            if c > res: break
            res += c
        return res

    test_cases_data = [
        [[1,3]],          # Sample 1
        [[1,1,1,4]],      # Sample 2
        [[1,4,10,3,1]],   # Sample 3
        [[1]],            # Single 1
        [[2]],            # Single >1
        [[1,1,1,1]],      # Multiple 1s
        [[1,2,4,8,16]],   # Powers of 2
        # Stress tests
        [[1]*40000],
        [[i for i in range(1, 1000)], 40000], # Mixed large
        [[i%100 + 1 for i in range(40000)]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        if isinstance(t[0], list): inp = json.dumps(t[0]).replace(" ", "")
        else: inp = json.dumps(t).replace(" ", "") # Handle the case where t is the list
        
        # Adjusting input format to be [coins] as per requirements
        final_inp = "[" + inp + "]"
        
        # Logic fix for solve call
        if isinstance(t[0], list): actual_coins = t[0]
        else: actual_coins = t
        
        out = str(solve(actual_coins))
        test_cases.append({"input": final_inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Greedy", "Sorting"], "companyIndex": 0
    }

    output_path = f"1701-1900/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
