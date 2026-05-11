import json
import os

def generate_json():
    problem_id = 1209
    title = "Remove All Adjacent Duplicates in String II"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1209. Remove All Adjacent Duplicates in String II</h3>
<p>You are given a string <code>s</code> and an integer <code>k</code>, a <code>k</code> duplicate removal consists of choosing <code>k</code> adjacent and equal letters from <code>s</code> and removing them, causing the left and the right side of the deleted substring to concatenate together.</p>

<p>We repeatedly make <code>k</code> duplicate removals on <code>s</code> until we no longer can.</p>

<p>Return <em>the final string after all such duplicate removals have been made</em>. It is guaranteed that the answer is unique.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "abcd"
<strong>Explanation:</strong> There's nothing to delete.</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "deeedbbcccbdaa", k = 3
<strong>Output:</strong> "aa"
<strong>Explanation: </strong>
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "pbbcggttciiippooaais", k = 2
<strong>Output:</strong> "ps"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> only contains lower case English letters.</li>
</ul>"""

    input_format = "A string `s` and an integer `k` as a JSON array `[s, k]`."
    output_format = "A string representing the final result."

    constraints = [
        "1 <= s.length <= 10^5",
        "2 <= k <= 10^4",
        "s contains only lower case English letters"
    ]

    explanation = """To remove all adjacent duplicate groups of size `k`:
1. Use a stack to store pairs of `(character, count)`.
2. Iterate through the string character by character.
3. If the stack is not empty and the current character matches the top character on the stack:
   - Increment the count for the top element.
   - If the count reaches `k`, pop the character from the stack.
4. If the current character does not match the top element, push `(character, 1)` onto the stack.
5. Finally, reconstruct the string from the stack by repeating each character its corresponding count of times."""

    answer = """class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, count)
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return "".join(char * count for char, count in stack)"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        s, k = json.loads(raw)
        sol = Solution()
        print(sol.removeDuplicates(s, k))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string removeDuplicates(string s, int k) {
        // User logic here
        return "";
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        json j = json::parse(line);
        Solution sol;
        cout << sol.removeDuplicates(j[0], j[1]) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class Solution {
    public String removeDuplicates(String s, int k) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            Object[] data = mapper.readValue(sc.nextLine(), Object[].class);
            System.out.println(new Solution().removeDuplicates((String)data[0], (Integer)data[1]));
        }
    }
}""",
        "javascript": """var removeDuplicates = function(s, k) {
    // User logic here
    return "";
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [s, k] = JSON.parse(input);
    console.log(removeDuplicates(s, k));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * removeDuplicates(char * s, int k){
    // User logic here
    return "";
}

int main() {
    // Boilerplate for string parsing
    return 0;
}"""
    }

    def solve(s, k):
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return "".join(char * count for char, count in stack)

    test_cases_data = [
        ["abcd", 2],               # Sample 1
        ["deeedbbcccbdaa", 3],      # Sample 2
        ["pbbcggttciiippooaais", 2], # Sample 3
        ["aaabbb", 3],             # Full removal
        ["aaabbb", 2],             # Partial removal
        ["a", 2],                  # Single
        ["abcde", 2],              # No removal
        # Stress tests
        ["a" * 1000, 2],
        ["a" * 1000, 1000],
        ["ab" * 500, 2]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = solve(t[0], t[1])
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 3})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["String", "Stack"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
