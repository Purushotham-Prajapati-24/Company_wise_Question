import json
import os
from itertools import permutations

def generate_json():
    problem_id = 679
    title = "24 Game"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>679. 24 Game</h3>
<p>You are given an integer array <code>cards</code> of length <code>4</code>. You have four cards, each containing a number in the range <code>[1, 9]</code>. You should arrange the numbers on these cards in a mathematical expression using the operators <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, and <code>'/'</code>, returning <code>true</code> if you can get the value <code>24</code>.</p>

<p><strong>Note</strong>:</p>
<ul>
    <li>You must use all the numbers on the cards, and each number may only be used once.</li>
    <li>Only binary operations are valid; no unary negation is allowed.</li>
    <li><code>/</code> represents real division, not integer division.</li>
    <li>You cannot concatenate numbers (e.g., if your cards are <code>[1, 2]</code>, you cannot form the number <code>12</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> cards = [4,1,8,7]
<strong>Output:</strong> true
<strong>Explanation:</strong> (8-4) * (7-1) = 24
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> cards = [1,2,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>cards.length == 4</code></li>
    <li><code>1 &lt;= cards[i] &lt;= 9</code></li>
</ul>"""

    input_format = "A single line: JSON array of 4 integers `cards`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "cards.length == 4",
        "1 <= cards[i] <= 9"
    ]

    explanation = """Use backtracking. At each step, pick any two numbers from the remaining list, apply one of the four operations, replace them with the result. Repeat until one number remains. If it equals 24 (within epsilon), return true. Also handle subtraction/division both ways (a-b and b-a, a/b and b/a)."""

    answer = """from itertools import combinations

class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        EPS = 1e-6
        
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: continue
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a+b, a-b, a*b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    for c in candidates:
                        if solve(rest + [c]):
                            return True
            return False
        
        return solve([float(c) for c in cards])"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        cards = json.loads(raw)
        sol = Solution()
        print("true" if sol.judgePoint24(cards) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

class Solution {
    bool solve(vector<double> nums) {
        if (nums.size() == 1) return abs(nums[0] - 24) < 1e-6;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                vector<double> rest;
                for (int k = 0; k < n; k++) if (k != i && k != j) rest.push_back(nums[k]);
                double a = nums[i], b = nums[j];
                vector<double> cands = {a+b, a-b, a*b};
                if (abs(b) > 1e-9) cands.push_back(a / b);
                for (double c : cands) {
                    vector<double> next = rest;
                    next.push_back(c);
                    if (solve(next)) return true;
                }
            }
        }
        return false;
    }
public:
    bool judgePoint24(vector<int>& cards) {
        vector<double> nums(cards.begin(), cards.end());
        return solve(nums);
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            res.push_back(input[i] - '0');
        }
        i++;
    }
    return res;
}

int main() {
    string str;
    if (getline(cin, str)) {
        vector<int> cards = parseArray(str);
        Solution sol;
        cout << (sol.judgePoint24(cards) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    private static final double EPS = 1e-6;
    
    boolean solve(List<Double> nums) {
        if (nums.size() == 1) return Math.abs(nums.get(0) - 24) < EPS;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                List<Double> rest = new ArrayList<>();
                for (int k = 0; k < n; k++) if (k != i && k != j) rest.add(nums.get(k));
                double a = nums.get(i), b = nums.get(j);
                double[] cands = {a+b, a-b, a*b, Math.abs(b) > 1e-9 ? a/b : Double.NaN};
                for (double c : cands) {
                    if (Double.isNaN(c)) continue;
                    List<Double> next = new ArrayList<>(rest);
                    next.add(c);
                    if (solve(next)) return true;
                }
            }
        }
        return false;
    }
    
    public boolean judgePoint24(int[] cards) {
        List<Double> nums = new ArrayList<>();
        for (int c : cards) nums.add((double)c);
        return solve(nums);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
            String[] parts = raw.split(",");
            int[] cards = new int[parts.length];
            for (int i = 0; i < parts.length; i++) cards[i] = Integer.parseInt(parts[i].trim());
            Solution sol = new Solution();
            System.out.println(sol.judgePoint24(cards) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} cards
 * @return {boolean}
 */
var judgePoint24 = function(cards) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const cards = JSON.parse(input);
    console.log(judgePoint24(cards) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

bool judgePoint24(int* cards, int cardsSize) {
    // User logic here
    return false;
}

int main() {
    int cards[4];
    if (scanf("[%d,%d,%d,%d]", &cards[0], &cards[1], &cards[2], &cards[3]) == 4) {
        printf("%s\\n", judgePoint24(cards, 4) ? "true" : "false");
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(nums):
        EPS = 1e-6
        if len(nums) == 1:
            return abs(nums[0] - 24) < EPS
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                a, b = nums[i], nums[j]
                candidates = [a+b, a-b, a*b]
                if abs(b) > EPS:
                    candidates.append(a / b)
                for c in candidates:
                    if solve(rest + [c]):
                        return True
        return False

    test_cases_data = [
        [4,1,8,7], [1,2,1,2], [1,1,1,1], [5,5,5,1], [3,3,8,8],
        [8,8,3,3], [2,2,2,2], [4,4,4,4], [1,3,4,6], [2,3,4,6]
    ]

    test_cases = []
    for i, cards in enumerate(test_cases_data):
        inp = json.dumps(cards)
        out = "true" if solve([float(c) for c in cards]) else "false"
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
        "topics": ["Array", "Math", "Backtracking"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
