import json
import os

def generate_json():
    problem_id = 1025
    title = "Divisor Game"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1025. Divisor Game</h3>
<p>Alice and Bob take turns playing a game, with Alice starting first.</p>

<p>Initially, there is a number <code>n</code> on the chalkboard. On each player's turn, that player makes a move consisting of:</p>

<ul>
	<li>Choosing any <code>x</code> such that <code>0 &lt; x &lt; n</code> and <code>n % x == 0</code>.</li>
	<li>Replacing the number <code>n</code> on the chalkboard with <code>n - x</code>.</li>
</ul>

<p>Also, if a player cannot make a move, they lose the game.</p>

<p>Return <code>true</code> if and only if Alice wins the game, assuming both players play optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice chooses 1, and Bob has no more moves.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice chooses 1, Bob chooses 1, and Alice has no more moves.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>"""

    input_format = "A single integer `n`."
    output_format = "`true` if Alice wins, otherwise `false`."

    constraints = ["1 <= n <= 1000"]

    explanation = """Alice wins if and only if n is even. 
If n is even, Alice can subtract 1 to make it odd. Then any divisor Bob chooses for that odd number must be odd, resulting in an even number again (odd - odd = even).
Eventually, Alice will reach 2 and win. If n starts odd, Bob will eventually win by the same logic."""

    answer = """class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0"""

    boilerplate = {
        "python": """import sys

class Solution:
    def divisorGame(self, n: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        n = int(line)
        sol = Solution()
        print("true" if sol.divisorGame(n) else "false")""",
        "cpp": """#include <iostream>

using namespace std;

class Solution {
public:
    bool divisorGame(int n) {
        // User logic here
        return false;
    }
};

int main() {
    int n;
    if (cin >> n) {
        Solution sol;
        cout << (sol.divisorGame(n) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean divisorGame(int n) {
        // User logic here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(new Solution().divisorGame(n));
        }
    }
}""",
        "javascript": """var divisorGame = function(n) {
    // User logic here
    return false;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(divisorGame(parseInt(input)));
}""",
        "c": """#include <stdio.h>
#include <stdbool.h>

bool divisorGame(int n) {
    // User logic here
    return false;
}

int main() {
    int n;
    if (scanf("%d", &n) == 1) {
        printf("%s\\n", divisorGame(n) ? "true" : "false");
    }
    return 0;
}"""
    }

    def solve(n):
        return n % 2 == 0

    test_cases_data = [2, 3, 1, 4, 10, 21, 100, 999, 1000, 500]
    test_cases = []
    for i, n in enumerate(test_cases_data):
        test_cases.append({
            "input": str(n),
            "expected_output": "true" if solve(n) else "false",
            "is_sample": i < 2
        })

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "Dynamic Programming", "Brainteaser", "Game Theory"], "companyIndex": 0
    }

    output_path = f"1001-1200/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
