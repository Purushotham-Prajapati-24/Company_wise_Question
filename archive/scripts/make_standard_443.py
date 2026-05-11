import json
import os

def generate_json():
    problem_id = 443
    title = "String Compression"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>443. String Compression</h3>
<p>Given an array of characters <code>chars</code>, compress it using the following algorithm:</p>
<p>Begin with an empty string <code>s</code>. For each group of <strong>consecutive repeating characters</strong> in <code>chars</code>:</p>

<ul>
	<li>If the group's length is <code>1</code>, append the character to <code>s</code>.</li>
	<li>Otherwise, append the character followed by the group's length.</li>
</ul>

<p>The compressed string <code>s</code> <strong>should not be returned separately</strong>, but instead, be stored&nbsp;<strong>in the input character array&nbsp;<code>chars</code></strong>. Note that group lengths that are <code>10</code> or longer will be split into multiple characters in <code>chars</code>.</p>

<p>After you are done <strong>modifying the input array</strong>, return <em>the new length of the array</em>.</p>

<p>You must write an algorithm that uses only <strong>constant extra space</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> chars = ["a","a","b","b","c","c","c"]
<strong>Output:</strong> Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> chars = ["a"]
<strong>Output:</strong> Return 1, and the first character of the input array should be: ["a"]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
<strong>Output:</strong> Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= chars.length &lt;= 2000</code></li>
	<li><code>chars[i]</code> is a lowercase English letter, uppercase English letter, digit, or symbol.</li>
</ul>"""

    input_format = "A JSON array of characters `chars`."
    output_format = "A JSON array of the compressed characters."
    
    constraints = [
        "1 <= chars.length <= 2000",
        "Must use constant extra space."
    ]
    
    explanation = """Use two pointers: `read` to iterate through the original array and `write` to update the array in-place. For each group of identical characters, write the character and then the string representation of its count (if count > 1) using the `write` pointer."""
    
    answer = """class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def compress(self, chars: list[str]) -> int:
        # User Logic Here
        return 0

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        chars = json.loads(raw_input)
        sol = Solution()
        new_len = sol.compress(chars)
        print(json.dumps(chars[:new_len]).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        // User Logic Here
        return 0;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<char> chars;
        // Manual parsing for character array...
        for (int i = 0; i < line.length(); i++) {
            if (line[i] == '\"') {
                chars.push_back(line[i + 1]);
                i += 2;
            }
        }
        Solution sol;
        int newLen = sol.compress(chars);
        cout << \"[\";
        for (int i = 0; i < newLen; i++) {
            cout << \"\\\"\" << chars[i] << \"\\\"\" << (i == newLen - 1 ? \"\" : \",\");
        }
        cout << \"]\" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int compress(char[] chars) {
        // User Logic Here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            List<Character> list = new ArrayList<>();
            for (int i = 0; i < line.length(); i++) {
                if (line.charAt(i) == '\"') {
                    list.add(line.charAt(i + 1));
                    i += 2;
                }
            }
            char[] chars = new char[list.size()];
            for (int i = 0; i < list.size(); i++) chars[i] = list.get(i);
            Solution sol = new Solution();
            int newLen = sol.compress(chars);
            System.out.print(\"[\");
            for (int i = 0; i < newLen; i++) {
                System.out.print(\"\\\"\" + chars[i] + \"\\\"\" + (i == newLen - 1 ? \"\" : \",\"));
            }
            System.out.println(\"]\");
        }
    }
}""",
        "javascript": """/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const chars = JSON.parse(input);
    const newLen = compress(chars);
    console.log(JSON.stringify(chars.slice(0, newLen)).replace(/\\s/g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compress(char* chars, int charsSize) {
    // User Logic Here
    return 0;
}

int main() {
    return 0;
}"""
    }

    test_cases = [
        {"input": '["a","a","b","b","c","c","c"]', "expected_output": '["a","2","b","2","c","3"]', "is_sample": True},
        {"input": '["a"]', "expected_output": '["a"]', "is_sample": True},
        {"input": '["a","b","b","b","b","b","b","b","b","b","b","b","b"]', "expected_output": '["a","b","1","2"]', "is_sample": True},
        {"input": '["a","b","c"]', "expected_output": '["a","b","c"]', "is_sample": False},
        {"input": '["a","a","a","a","a"]', "expected_output": '["a","5"]', "is_sample": False},
        {"input": '["a","a","a","a","a","a","a","a","a","a"]', "expected_output": '["a","1","0"]', "is_sample": False},
        {"input": '["#","#","!","!","!"]', "expected_output": '["#","2","!","3"]', "is_sample": False},
        {"input": '["A","B","B","C","C","C"]', "expected_output": '["A","B","2","C","3"]', "is_sample": False},
        # Stress
        {"input": json.dumps(["a"]*2000), "expected_output": '["a","2","0","0","0"]', "is_sample": False},
        {"input": '["a","b","c","d","e"]', "expected_output": '["a","b","c","d","e"]', "is_sample": False}
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
        "topics": ["Two Pointers", "String"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_String_Compression.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
