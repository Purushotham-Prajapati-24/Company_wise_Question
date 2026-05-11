import json
import os

def generate_json():
    problem_id = 771
    title = "Jewels and Stones"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>771. Jewels and Stones</h3>
<p>You're given strings <code>jewels</code> representing the types of stones that are jewels, and <code>stones</code> representing the stones you have. Each character in <code>stones</code> is a type of stone you have. You want to know how many of the stones you have are also jewels.</p>

<p>Letters are case sensitive, so <code>"a"</code> is considered a different type of stone from <code>"A"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> jewels = "aA", stones = "aAAbbbb"
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> jewels = "z", stones = "ZZ"
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= jewels.length, stones.length &lt;= 50</code></li>
    <li><code>jewels</code> and <code>stones</code> consist of only English letters.</li>
    <li>All the characters of <code>jewels</code> are <strong>unique</strong>.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: string `jewels`\nLine 2: string `stones`"
    output_format = "An integer representing the count of jewels."

    constraints = [
        "1 <= jewels.length, stones.length <= 50",
        "jewels and stones consist of English letters",
        "All characters in jewels are unique"
    ]

    explanation = """Convert the string `jewels` into a set of characters for O(1) lookups. Then iterate through each character in the string `stones`. If the character exists in the `jewels` set, increment your counter. Return the counter at the end."""

    answer = """class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        jewels = json.loads(raw[0]) if raw[0].startswith('"') else raw[0]
        stones = json.loads(raw[1]) if raw[1].startswith('"') else raw[1]
        if type(jewels) == str and jewels.startswith('"'): jewels = jewels[1:-1]
        if type(stones) == str and stones.startswith('"'): stones = stones[1:-1]
        sol = Solution()
        print(sol.numJewelsInStones(jewels, stones))""",
        "cpp": """#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        // User logic here
        return 0;
    }
};

int main() {
    string jewels, stones;
    if (getline(cin, jewels) && getline(cin, stones)) {
        if (jewels.front() == '"') jewels = jewels.substr(1, jewels.length() - 2);
        if (stones.front() == '"') stones = stones.substr(1, stones.length() - 2);
        Solution sol;
        cout << sol.numJewelsInStones(jewels, stones) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String jewels = sc.nextLine().trim();
            if (sc.hasNextLine()) {
                String stones = sc.nextLine().trim();
                if (jewels.startsWith("\\"")) jewels = jewels.substring(1, jewels.length() - 1);
                if (stones.startsWith("\\"")) stones = stones.substring(1, stones.length() - 1);
                Solution sol = new Solution();
                System.out.println(sol.numJewelsInStones(jewels, stones));
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    let jewels = input[0].trim();
    let stones = input[1].trim();
    if (jewels.startsWith('"')) jewels = JSON.parse(jewels);
    if (stones.startsWith('"')) stones = JSON.parse(stones);
    console.log(numJewelsInStones(jewels, stones));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int numJewelsInStones(char* jewels, char* stones) {
    // User logic here
    return 0;
}

void cleanStr(char* str) {
    int len = strlen(str);
    while (len > 0 && (str[len-1] == '\\n' || str[len-1] == '\\r')) {
        str[len-1] = '\\0';
        len--;
    }
    if (len >= 2 && str[0] == '"' && str[len-1] == '"') {
        memmove(str, str+1, len-2);
        str[len-2] = '\\0';
    }
}

int main() {
    char jewels[200], stones[200];
    if (fgets(jewels, sizeof(jewels), stdin) && fgets(stones, sizeof(stones), stdin)) {
        cleanStr(jewels);
        cleanStr(stones);
        printf("%d\\n", numJewelsInStones(jewels, stones));
    }
    return 0;
}"""
    }

    def solve(jewels, stones):
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)

    test_cases_data = [
        ("aA", "aAAbbbb"),
        ("z", "ZZ"),
        ("abc", "abcdef"),
        ("ABC", "XYZ"),
        ("a", "a" * 50),
        ("qwertyuiopasdfghjklzxcvbnm", "A" * 50),
        ("A", "a" * 25 + "A" * 25),
        ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcXYZ"),
        ("zZ", "zzZZZzZzZ"),
        ("x", "y")
    ]

    test_cases = []
    for i, (j, s) in enumerate(test_cases_data):
        inp = json.dumps(j) + "\\n" + json.dumps(s)
        out = str(solve(j, s))
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
        "topics": ["Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
