import json
import os

def generate_json():
    problem_id = 717
    title = "1-bit and 2-bit Characters"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>717. 1-bit and 2-bit Characters</h3>
<p>We have two special characters:</p>
<ul>
    <li>The first character can be represented by one bit <code>0</code>.</li>
    <li>The second character can be represented by two bits (<code>10</code> or <code>11</code>).</li>
</ul>

<p>Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> bits = [1,0,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> bits = [1,1,1,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= bits.length &lt;= 1000</code></li>
    <li><code>bits[i]</code> is either <code>0</code> or <code>1</code>.</li>
    <li><code>bits</code> always ends with <code>0</code>.</li>
</ul>"""

    input_format = "A single line: JSON array `bits`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= bits.length <= 1000",
        "bits[i] is 0 or 1",
        "bits ends with 0"
    ]

    explanation = """Iterate from the beginning of the array. If you encounter a `1`, skip the next bit (it forms a 2-bit character). If you encounter a `0`, it's a 1-bit character. Check if the index at the loop's end equals `n - 1`. If it does, the last character was a 1-bit character."""

    answer = """class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        bits = json.loads(raw)
        sol = Solution()
        print("true" if sol.isOneBitCharacter(bits) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <ctype.h>

using namespace std;

class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        // User logic here
        return false;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 0;
    while (i < input.length()) {
        if (isdigit(input[i])) {
            res.push_back(input[i]-'0');
        }
        i++;
    }
    return res;
}

int main() {
    string n_str;
    if (getline(cin, n_str)) {
        vector<int> bits = parseArray(n_str);
        Solution sol;
        cout << (sol.isOneBitCharacter(bits) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String n_str = sc.nextLine().trim();
            int[] bits = parseArray(n_str);
            Solution sol = new Solution();
            System.out.println(sol.isOneBitCharacter(bits) ? "true" : "false");
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const bits = JSON.parse(input);
    console.log(isOneBitCharacter(bits) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool isOneBitCharacter(int* bits, int bitsSize) {
    // User logic here
    return false;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
            res[size++] = input[i] - '0';
        }
        i++;
    }
    *outSize = size;
    return res;
}

int main() {
    char n_str[10000];
    if (fgets(n_str, sizeof(n_str), stdin)) {
        int bitsSize;
        int* bits = parseArray(n_str, &bitsSize);
        printf("%s\\n", isOneBitCharacter(bits, bitsSize) ? "true" : "false");
        free(bits);
    }
    return 0;
}"""
    }

    # Compute expected outputs
    def solve(bits):
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1

    test_cases_data = [
        [1,0,0],
        [1,1,1,0],
        [0],
        [0,0],
        [1,0],
        [1,1,0],
        [0,1,0,0],
        ([1,0] * 400) + [0],
        ([1,1] * 400) + [0],
        ([1,1,1,0] * 200) + [1,0,0]
    ]

    test_cases = []
    for i, bits in enumerate(test_cases_data):
        inp = json.dumps(bits)
        out = "true" if solve(bits) else "false"
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
        "topics": ["Array"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
