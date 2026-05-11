import json
import os

def generate_json():
    problem_id = 524
    title = "Longest Word in Dictionary through Deleting"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>524. Longest Word in Dictionary through Deleting</h3>
<p>Given a string <code>s</code> and a string array <code>dictionary</code>, return <em>the longest string in the dictionary that can be formed by deleting some of the given string characters</em>.</p>

<p>If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
<strong>Output:</strong> "apple"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abpcplea", dictionary = ["a","b","c"]
<strong>Output:</strong> "a"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary.length &lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 1000</code></li>
	<li><code>s</code> and <code>dictionary[i]</code> consist of lowercase English letters.</li>
</ul>"""

    input_format = "Two lines: Line 1: A JSON string `s`. Line 2: A JSON array of strings `dictionary`."
    output_format = "A JSON string."
    
    constraints = [
        "1 <= s.length <= 1000",
        "1 <= dictionary.length <= 1000",
        "1 <= dictionary[i].length <= 1000",
        "s and dictionary[i] consist of lowercase English letters."
    ]
    
    explanation = """To find if a word from the dictionary can be formed by deleting characters from `s`, we can use a two-pointer approach checking if the word is a subsequence of `s`. We iterate through all words in the dictionary, keeping track of the longest valid word (and breaking ties with lexicographical order)."""
    
    answer = """class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        longest_word = ""
        for word in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word):
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        return longest_word"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        s = json.loads(raw[0])
        dictionary = json.loads(raw[1])
        sol = Solution()
        print(json.dumps(sol.findLongestWord(s, dictionary)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        // User logic here
        return "";
    }
};

int main() {
    string s_str, dict_str;
    if (getline(cin, s_str) && getline(cin, dict_str)) {
        string s = s_str;
        if (s.length() >= 2 && s[0] == '"') s = s.substr(1, s.length() - 2);
        
        vector<string> dictionary;
        size_t p = 0;
        while (p < dict_str.length()) {
            if (dict_str[p] == '"') {
                size_t end = dict_str.find('"', p + 1);
                if (end != string::npos) {
                    dictionary.push_back(dict_str.substr(p + 1, end - p - 1));
                    p = end + 1;
                } else break;
            } else {
                p++;
            }
        }
        Solution sol;
        cout << "\\"" << sol.findLongestWord(s, dictionary) << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s_str = sc.nextLine().trim();
            if (s_str.length() >= 2 && s_str.startsWith("\\"")) {
                s_str = s_str.substring(1, s_str.length() - 1);
            }
            if (sc.hasNextLine()) {
                String dict_str = sc.nextLine().trim();
                List<String> dictionary = new ArrayList<>();
                int p = 0;
                while (p < dict_str.length()) {
                    if (dict_str.charAt(p) == '"') {
                        int end = dict_str.indexOf('"', p + 1);
                        if (end != -1) {
                            dictionary.add(dict_str.substring(p + 1, end));
                            p = end + 1;
                        } else break;
                    } else {
                        p++;
                    }
                }
                Solution sol = new Solution();
                System.out.println("\\"" + sol.findLongestWord(s_str, dictionary) + "\\"");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {string}
 */
var findLongestWord = function(s, dictionary) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const s = JSON.parse(input[0]);
    const dictionary = JSON.parse(input[1]);
    console.log(JSON.stringify(findLongestWord(s, dictionary)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * findLongestWord(char * s, char ** dictionary, int dictionarySize) {
    // User logic here
    char * res = (char *)malloc(1);
    res[0] = '\\0';
    return res;
}

int main() {
    char s_str[2000];
    char dict_str[1000000];
    if (fgets(s_str, sizeof(s_str), stdin) && fgets(dict_str, sizeof(dict_str), stdin)) {
        s_str[strcspn(s_str, "\\n")] = 0;
        char s[2000];
        int len_s = strlen(s_str);
        if (len_s >= 2 && s_str[0] == '"') {
            strncpy(s, s_str + 1, len_s - 2);
            s[len_s - 2] = '\\0';
        } else {
            strcpy(s, s_str);
        }
        
        int capacity = 10;
        char** dictionary = (char**)malloc(capacity * sizeof(char*));
        int size = 0;
        int p = 0;
        while (dict_str[p] != '\\0') {
            if (dict_str[p] == '"') {
                int end = p + 1;
                while (dict_str[end] != '"' && dict_str[end] != '\\0') end++;
                if (dict_str[end] == '"') {
                    if (size == capacity) {
                        capacity *= 2;
                        dictionary = (char**)realloc(dictionary, capacity * sizeof(char*));
                    }
                    int word_len = end - p - 1;
                    dictionary[size] = (char*)malloc(word_len + 1);
                    strncpy(dictionary[size], dict_str + p + 1, word_len);
                    dictionary[size][word_len] = '\\0';
                    size++;
                    p = end + 1;
                } else break;
            } else {
                p++;
            }
        }
        
        char* res = findLongestWord(s, dictionary, size);
        printf("\\"%s\\"\\n", res ? res : "");
        if (res) free(res);
        for (int i = 0; i < size; i++) free(dictionary[i]);
        free(dictionary);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": '"abpcplea"\\n["ale","apple","monkey","plea"]', "expected_output": '"apple"', "is_sample": True},
        {"input": '"abpcplea"\\n["a","b","c"]', "expected_output": '"a"', "is_sample": True},
        
        # Five Diverse Cases
        {"input": '"apple"\\n["zxc","vbn"]', "expected_output": '""', "is_sample": False},
        {"input": '"bab"\\n["ba","ab","a","b"]', "expected_output": '"ab"', "is_sample": False},
        {"input": '"abce"\\n["abe","abc"]', "expected_output": '"abc"', "is_sample": False},
        {"input": '"aaa"\\n["aaa","aa","a"]', "expected_output": '"aaa"', "is_sample": False},
        {"input": '"a"\\n["b","c","a","d"]', "expected_output": '"a"', "is_sample": False},
        
        # Three Stress Test Cases (strict JSON arrays formatting boundary limits)
        {"input": '"' + 'a' * 1000 + '"\\n["' + 'a' * 1000 + '","' + 'b' * 1000 + '"]', "expected_output": '"' + 'a' * 1000 + '"', "is_sample": False},
        {"input": '"' + 'b' * 1000 + '"\\n["' + 'a' * 1000 + '"]', "expected_output": '""', "is_sample": False},
        {"input": '"xy"\\n[""x"",""y"",""xy""]'.replace('""', '"'), "expected_output": '"xy"', "is_sample": False}
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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Array", "Two Pointers", "String", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
