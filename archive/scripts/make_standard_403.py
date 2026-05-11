import json
import os

def generate_json():
    problem_id = 403
    title = "Frog Jump"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>403. Frog Jump</h3>
<p>A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not be a stone. The frog can jump on a stone, but it must not jump into the water.</p>

<p>Given a list of <code>stones</code>' positions (in units) in sorted <strong>ascending order</strong>, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be <code>1</code> unit.</p>

<p>If the frog's last jump was <code>k</code> units, its next jump must be either <code>k - 1</code>, <code>k</code>, or <code>k + 1</code> units. The frog can only jump in the forward direction.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> stones = [0,1,3,5,6,8,12,17]
<strong>Output:</strong> true
<strong>Explanation:</strong> The frog can jump to the last stone as follows: 0->1->3->5->6->8->12->17.
- Step 1: Jump 1 unit to the 2nd stone (0+1=1)
- Step 2: Jump 2 units to the 3rd stone (1+2=3)
- Step 3: Jump 2 units to the 4th stone (3+2=5)
- Step 4: Jump 1 unit to the 5th stone (5+1=6)
- Step 5: Jump 2 units to the 6th stone (6+2=8)
- Step 6: Jump 4 units to the 7th stone (8+4=12)
- Step 7: Jump 5 units to the 8th stone (12+5=17)
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> stones = [0,1,2,3,4,8,9,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= stones.length &lt;= 2000</code></li>
	<li><code>0 &lt;= stones[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>stones[0] == 0</code></li>
	<li><code>stones</code>&nbsp;is sorted in a strictly increasing order.</li>
</ul>"""

    input_format = "A list of stone positions."
    output_format = "A boolean value."
    
    constraints = [
        "2 <= stones.length <= 2000",
        "0 <= stones[i] <= 2^31 - 1",
        "stones[0] == 0"
    ]
    
    explanation = """Use Dynamic Programming with a hash set for fast stone lookup. Modell the state as (current_stone, last_jump_size)."""
    
    answer = """class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                for jump in [k-1, k, k+1]:
                    if jump > 0 and stone + jump in dp:
                        dp[stone + jump].add(jump)
        return len(dp[stones[-1]]) > 0"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canCross(self, stones: list[int]) -> bool:
        # User Logic Here
        pass

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        stones = json.loads(raw_input)
        sol = Solution()
        print(json.dumps(sol.canCross(stones)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canCross(vector<int>& stones) {
        // User Logic Here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        if (!line.empty() && line.front() == '[') line = line.substr(1, line.size() - 2);
        stringstream ss(line);
        string val;
        vector<int> stones;
        while (getline(ss, val, ',')) {
            stones.push_back(stoi(val));
        }
        Solution sol;
        cout << (sol.canCross(stones) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean canCross(int[] stones) {
        // User Logic Here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.startsWith("[")) line = line.substring(1, line.length() - 1);
            String[] parts = line.split(",");
            int[] stones = new int[parts.length];
            for (int i = 0; i < parts.length; i++) stones[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.canCross(stones));
        }
    }
}""",
        "javascript": """var canCross = function(stones) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(canCross(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool canCross(int* stones, int stonesSize) {
    // User Logic Here
    return false;
}

int main() {
    char line[10000];
    if (fgets(line, 10000, stdin)) {
        char *ptr = line;
        if (*ptr == '[') ptr++;
        int *stones = malloc(2000 * sizeof(int));
        int size = 0;
        char *token = strtok(ptr, ",]");
        while (token) {
            stones[size++] = atoi(token);
            token = strtok(NULL, ",]");
        }
        printf("%s\\n", canCross(stones, size) ? "true" : "false");
        free(stones);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[0,1,3,5,6,8,12,17]", "expected_output": "true", "is_sample": True},
        {"input": "[0,1,2,3,4,8,9,11]", "expected_output": "false", "is_sample": True},
        # 5 Diverse
        {"input": "[0,1]", "expected_output": "true", "is_sample": False},
        {"input": "[0,2]", "expected_output": "false", "is_sample": False},
        {"input": "[0,1,3,4,5,7,9,10,12]", "expected_output": "true", "is_sample": False},
        {"input": "[0,1,2,3,4,5,6,7]", "expected_output": "true", "is_sample": False},
        {"input": "[0,1,3,6,10,15,21]", "expected_output": "true", "is_sample": False},
        # 3 Stress
        {"input": "[0,1,2,4,7,11,16,22,29,37,46,56,67,79,92,106,121,137,154,172,191]", "expected_output": "true", "is_sample": False},
        {"input": "[0,1,3,6,9,12,15,18,21,24,27,30]", "expected_output": "true", "is_sample": False},
        {"input": "[0,1,2,3,100]", "expected_output": "false", "is_sample": False}
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
        "topics": ["Dynamic Programming", "Hash Table"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Frog_Jump.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
