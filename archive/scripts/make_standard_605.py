import json
import os

def generate_json():
    problem_id = 605
    title = "Can Place Flowers"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>605. Can Place Flowers</h3>
<p>You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in <strong>adjacent</strong> plots.</p>

<p>Given an integer array <code>flowerbed</code> containing <code>0</code>'s and <code>1</code>'s, where <code>0</code> means empty and <code>1</code> means not empty, and an integer <code>n</code>, return <code>true</code>&nbsp;<em>if</em> <code>n</code> <em>new flowers can be planted in the</em> <code>flowerbed</code> <em>without violating the no-adjacent-flowers rule and</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 1
<strong>Output:</strong> true
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> flowerbed = [1,0,0,0,1], n = 2
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= flowerbed.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>flowerbed[i]</code> is <code>0</code> or <code>1</code>.</li>
    <li>There are no two adjacent flowers in <code>flowerbed</code>.</li>
    <li><code>0 &lt;= n &lt;= flowerbed.length</code></li>
</ul>"""

    input_format = "Two lines:\nLine 1: A JSON array of integers `flowerbed`.\nLine 2: An integer `n`."
    output_format = "A boolean: `true` or `false`."

    constraints = [
        "1 <= flowerbed.length <= 2 * 10^4",
        "flowerbed[i] is 0 or 1",
        "There are no two adjacent flowers in the initial flowerbed."
    ]

    explanation = """Use a greedy approach. Iterate through the array and whenever you find a 0, check if its left and right neighbors are also 0 (or bounds). If so, plant a flower (change 0 to 1) and decrement n. Return true if n <= 0 at any point."""

    answer = """class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return False"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # User logic here
        return False

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        flowerbed = json.loads(raw[0])
        n = int(raw[1])
        sol = Solution()
        print("true" if sol.canPlaceFlowers(flowerbed, n) else "false")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // User logic here
        return false;
    }
};

vector<int> parseArray(string input) {
    vector<int> res;
    size_t i = 1;
    while (i < input.length() && input[i] != ']') {
        if (isdigit(input[i])) {
            res.push_back(input[i] - '0');
        }
        i++;
    }
    return res;
}

int main() {
    string f_str, n_str;
    if (getline(cin, f_str) && getline(cin, n_str)) {
        vector<int> flowerbed = parseArray(f_str);
        int n = stoi(n_str);
        Solution sol;
        cout << (sol.canPlaceFlowers(flowerbed, n) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // User logic here
        return false;
    }
}

public class Main {
    static int[] parseArray(String raw) {
        if (raw.length() > 1) raw = raw.substring(1, raw.length() - 1);
        else return new int[0];
        if (raw.isEmpty()) return new int[0];
        String[] parts = raw.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String f_str = sc.nextLine().trim();
            if (sc.hasNextInt()) {
                int[] flowerbed = parseArray(f_str);
                int n = sc.nextInt();
                Solution sol = new Solution();
                System.out.println(sol.canPlaceFlowers(flowerbed, n) ? "true" : "false");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const flowerbed = JSON.parse(input[0]);
    const n = parseInt(input[1], 10);
    console.log(canPlaceFlowers(flowerbed, n) ? "true" : "false");
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    // User logic here
    return false;
}

int* parseArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    int* res = (int*)malloc(cap * sizeof(int));
    while (input[i] && input[i] != '\\n') {
        if (isdigit(input[i])) {
            int val, off = 0;
            sscanf(input + i, "%d%n", &val, &off);
            if (!off) { i++; continue; }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(int)); }
            res[size++] = val;
            i += off;
        } else i++;
    }
    *outSize = size;
    return res;
}

int main() {
    char f_str[500000];
    if (fgets(f_str, sizeof(f_str), stdin)) {
        int flowerbedSize;
        int* flowerbed = parseArray(f_str, &flowerbedSize);
        int n;
        if (scanf("%d", &n) == 1) {
            printf("%s\\n", canPlaceFlowers(flowerbed, flowerbedSize, n) ? "true" : "false");
        }
        free(flowerbed);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,0,0,0,1]\\n1", "expected_output": "true", "is_sample": True},
        {"input": "[1,0,0,0,1]\\n2", "expected_output": "false", "is_sample": True},
        {"input": "[0,0,1,0,1]\\n1", "expected_output": "true", "is_sample": False},
        {"input": "[1,0,0,0,0,1]\\n2", "expected_output": "false", "is_sample": False},
        {"input": "[0,0,0,0,0]\\n3", "expected_output": "true", "is_sample": False},
        {"input": "[0]\\n1", "expected_output": "true", "is_sample": False},
        {"input": "[1]\\n0", "expected_output": "true", "is_sample": False},
        {"input": "[" + ",".join("0" for _ in range(20000)) + "]\\n10000", "expected_output": "true", "is_sample": False},
        {"input": "[" + ",".join("0" for _ in range(20000)) + "]\\n10001", "expected_output": "false", "is_sample": False},
        {"input": "[" + ",".join(("1" if i%2==0 else "0") for i in range(20000)) + "]\\n1", "expected_output": "false", "is_sample": False}
    ]

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
        "topics": ["Array", "Greedy"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
