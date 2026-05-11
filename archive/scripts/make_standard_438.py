import json
import os

def generate_json():
    problem_id = 438
    title = "Find All Anagrams in a String"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>438. Find All Anagrams in a String</h3>
<p>Given two strings <code>s</code> and <code>p</code>, return <em>an array of all the start indices of </em><code>p</code>'s <em>anagrams in </em><code>s</code>. You may return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "cbaebabacd", p = "abc"
<strong>Output:</strong> [0,6]
<strong>Explanation:</strong>
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abab", p = "ab"
<strong>Output:</strong> [0,1,2]
<strong>Explanation:</strong>
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>p</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines: string `s` and string `p`."
    output_format = "A JSON array of integers representing the start indices."
    
    constraints = [
        "1 <= s.length, p.length <= 3 * 10^4",
        "s and p consist of lowercase English letters."
    ]
    
    explanation = """Use a sliding window of size `len(p)` over string `s`. Maintain a frequency count (array of size 26) of characters in the current window and compare it with the frequency count of string `p`. If they match, the start index of the window is an anagram index. Optimization: Instead of comparing full arrays, maintain a 'match' counter or just compare the arrays if they are small."""
    
    answer = """class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s): return res
        
        p_count = [0] * 26
        s_count = [0] * 26
        for char in p:
            p_count[ord(char) - ord('a')] += 1
            
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_count == p_count:
                res.append(i - len(p) + 1)
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # User Logic Here
        pass

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        s = lines[0].strip()
        p = lines[1].strip()
        sol = Solution()
        print(json.dumps(sol.findAnagrams(s, p)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        // User Logic Here
        return {};
    }
};

int main() {
    string s, p;
    if (cin >> s >> p) {
        Solution sol;
        vector<int> res = sol.findAnagrams(s, p);
        cout << \"[\";
        for (int i = 0; i < (int)res.size(); i++) {
            cout << res[i] << (i == (int)res.size() - 1 ? \"\" : \",\");
        }
        cout << \"]\" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // User Logic Here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine().trim();
            if (sc.hasNextLine()) {
                String p = sc.nextLine().trim();
                Solution sol = new Solution();
                List<Integer> res = sol.findAnagrams(s, p);
                System.out.print(\"[\");
                for (int i = 0; i < res.size(); i++) {
                    System.out.print(res.get(i) + (i == res.size() - 1 ? \"\" : \",\"));
                }
                System.out.println(\"]\");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    const s = input[0].trim();
    const p = input[1].trim();
    console.log(JSON.stringify(findAnagrams(s, p)).replace(/\\s/g, ''));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* findAnagrams(char* s, char* p, int* returnSize) {
    // User Logic Here
    return NULL;
}

int main() {
    char s[30005], p[30005];
    if (scanf(\"%s %s\", s, p) != EOF) {
        int returnSize = 0;
        int* res = findAnagrams(s, p, &returnSize);
        printf(\"[\");
        for (int i = 0; i < returnSize; i++) {
            printf(\"%d%s\", res[i], (i == returnSize - 1 ? \"\" : \",\"));
        }
        printf(\"]\\n\");
        free(res);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "cbaebabacd\\nabc", "expected_output": "[0,6]", "is_sample": True},
        {"input": "abab\\nab", "expected_output": "[0,1,2]", "is_sample": True},
        {"input": "aaaaaaaaaa\\naaaaaaaaaa", "expected_output": "[0]", "is_sample": False},
        {"input": "abc\\ndef", "expected_output": "[]", "is_sample": False},
        {"input": "a\\na", "expected_output": "[0]", "is_sample": False},
        {"input": "abacaba\\naba", "expected_output": "[0,2,4]", "is_sample": False},
        {"input": " helloworld \\n low ", "expected_output": "[3]", "is_sample": False}, # Spaces
        {"input": "zzzzzzzz\\nz", "expected_output": "[0,1,2,3,4,5,6,7]", "is_sample": False},
        # Stress
        {"input": "a"*30000 + "\\n" + "a"*15000, "expected_output": str(list(range(15001))).replace(" ", ""), "is_sample": False},
        {"input": "abcdefg\\nabcdefg", "expected_output": "[0]", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Sliding Window"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Find_All_Anagrams_in_a_String.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
