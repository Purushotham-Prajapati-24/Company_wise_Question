import json
import os

def generate_json():
    problem_id = 1239
    title = "Maximum Length of a Concatenated String with Unique Characters"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1239. Maximum Length of a Concatenated String with Unique Characters</h3>
<p>You are given an array of strings <code>arr</code>. A string <code>s</code> is formed by the <strong>concatenation</strong> of a <strong>subsequence</strong> of <code>arr</code> that has <strong>unique characters</strong>.</p>

<p>Return <em>the maximum possible length of</em> <code>s</code>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = ["un","iq","ue"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = ["cha","r","act","ers"]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = ["abcdefghijklmnopqrstuvwxyz"]
<strong>Output:</strong> 26
<strong>Explanation:</strong> The only string in arr has all 26 characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= arr.length &lt;= 16</code></li>
	<li><code>1 &lt;= arr[i].length &lt;= 26</code></li>
	<li><code>arr[i]</code> contains only lowercase English letters.</li>
</ul>"""

    input_format = "A list of strings `arr` in JSON format."
    output_format = "An integer representing the maximum length."

    constraints = [
        "1 <= arr.length <= 16",
        "1 <= arr[i].length <= 26",
        "arr[i] only contains lowercase English letters"
    ]

    explanation = """To find the maximum length of unique concatenations:
1. Since the number of strings is small (<= 16), we can use recursion with backtracking or bitmasking.
2. For each string in `arr`, check if its characters are unique. If not, discard it.
3. Represent each valid string as a bitmask (26 bits for 'a'-'z').
4. Start with an initial empty mask (length 0).
5. For each string's mask, see if it can be combined with existing masks in our results list (no overlapping bits).
6. If it can be combined, update the results list with the new combined mask and length.
7. The answer is the maximum length in the results list."""

    answer = """class Solution:
    def maxLength(self, arr: list[str]) -> int:
        masks = [0]
        max_len = 0
        for s in arr:
            mask = 0
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit: # Duplicates in the string itself
                    mask = 0
                    break
                mask |= bit
            if mask == 0: continue
            
            for m in masks[:]:
                if not (m & mask):
                    new_mask = m | mask
                    masks.append(new_mask)
                    max_len = max(max_len, bin(new_mask).count('1'))
        return max_len"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        arr = json.loads(raw)
        sol = Solution()
        print(sol.maxLength(arr))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxLength(vector<string>& arr) {
        // User logic here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<string> arr = json::parse(line);
        Solution sol;
        cout << sol.maxLength(arr) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public int maxLength(List<String> arr) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            List<String> arr = mapper.readValue(sc.nextLine(), List.class);
            System.out.println(new Solution().maxLength(arr));
        }
    }
}""",
        "javascript": """var maxLength = function(arr) {
    // User logic here
    return 0;
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(maxLength(JSON.parse(input)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxLength(char ** arr, int arrSize){
    // User logic here
    return 0;
}

int main() {
    // Boilerplate for array parsing
    return 0;
}"""
    }

    def solve(arr):
        masks = [0]
        max_len = 0
        for s in arr:
            mask = 0
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit:
                    mask = 0
                    break
                mask |= bit
            if mask == 0: continue
            for m in masks[:]:
                if not (m & mask):
                    new_mask = m | mask
                    masks.append(new_mask)
                    max_len = max(max_len, bin(new_mask).count('1'))
        return max_len

    test_cases_data = [
        ["un","iq","ue"],                # Sample 1
        ["cha","r","act","ers"],         # Sample 2
        ["abcdefghijklmnopqrstuvwxyz"], # Sample 3
        ["a", "b", "c", "d"],            # Disjoint
        ["aa", "bb"],                    # Individual duplicates
        ["abc", "def", "ghi", "ad"],     # Conflict
        ["abc", "def", "abc"],           # Exact duplicate
        # Stress tests
        ["abcdefghijklm", "nopqrstuvwxyz"], # Max split
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"], # 16 single
        ["a" * i for i in range(1, 17)]  # Overlapping
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
        "topics": ["Array", "String", "Backtracking", "Bit Manipulation"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
