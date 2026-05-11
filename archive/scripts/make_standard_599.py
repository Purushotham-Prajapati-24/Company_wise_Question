import json
import os

def generate_json():
    problem_id = 599
    title = "Minimum Index Sum of Two Lists"
    difficulty = "EASY"
    marks = 5

    html_description = """<h3>599. Minimum Index Sum of Two Lists</h3>
<p>Given two arrays of strings <code>list1</code> and <code>list2</code>, find the <strong>common strings with the least index sum</strong>.</p>

<p>A <strong>common string</strong> is a string that appeared in both <code>list1</code> and <code>list2</code>.</p>

<p>A <strong>common string with the least index sum</strong> is a common string such that if it appeared at <code>list1[i]</code> and <code>list2[j]</code> then <code>i + j</code> should be the minimum value among all the other <strong>common strings</strong>.</p>

<p>Return all the <strong>common strings with the least index sum</strong>. Return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
<strong>Output:</strong> ["Shogun"]
<strong>Explanation:</strong> The only common string is "Shogun".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
<strong>Output:</strong> ["Shogun"]
<strong>Explanation:</strong> The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
<strong>Output:</strong> ["sad","happy"]
<strong>Explanation:</strong> There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= list1.length, list2.length &lt;= 1000</code></li>
    <li><code>1 &lt;= list1[i].length, list2[i].length &lt;= 30</code></li>
    <li><code>list1[i]</code> and <code>list2[i]</code> consist of spaces <code>' '</code> and English letters.</li>
    <li>All the strings of <code>list1</code> are <strong>unique</strong>.</li>
    <li>All the strings of <code>list2</code> are <strong>unique</strong>.</li>
    <li>There is at least a common string between <code>list1</code> and <code>list2</code>.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: A JSON array of strings `list1`.\nLine 2: A JSON array of strings `list2`."
    output_format = "A JSON array of strings, sorted lexicographically (to ensure deterministic output)."

    constraints = [
        "1 <= list1.length, list2.length <= 1000",
        "Strings only contain English letters and spaces."
    ]

    explanation = """Use a hash map to store indices of the strings from list1. Then loop through list2 and check if the string exists in the hash map. If it does, calculate the sum of indices. Keep track of the minimum sum and the corresponding strings."""

    answer = """class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {res: i for i, res in enumerate(list1)}
        min_sum = float('inf')
        res = []
        
        for j, res2 in enumerate(list2):
            if res2 in index_map:
                curr_sum = j + index_map[res2]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    res = [res2]
                elif curr_sum == min_sum:
                    res.append(res2)
                    
        return res"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        list1 = json.loads(raw[0])
        list2 = json.loads(raw[1])
        sol = Solution()
        ans = sol.findRestaurant(list1, list2)
        ans.sort()
        print(json.dumps(ans))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        // User logic here
        return {};
    }
};

vector<string> parseStringArray(string input) {
    auto isWhitespace = [](char c) { return c == ' ' || c == '\\n' || c == '\\r' || c == '\\t'; };
    vector<string> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '"') {
            size_t j = i + 1;
            string s = "";
            while (j < input.length() && input[j] != '"') {
                if (input[j] == '\\\\') {
                    s += input[j+1];
                    j += 2;
                } else {
                    s += input[j];
                    j++;
                }
            }
            res.push_back(s);
            i = j + 1;
        } else {
            i++;
        }
    }
    return res;
}

int main() {
    string str1, str2;
    if (getline(cin, str1) && getline(cin, str2)) {
        vector<string> list1 = parseStringArray(str1);
        vector<string> list2 = parseStringArray(str2);
        Solution sol;
        vector<string> ans = sol.findRestaurant(list1, list2);
        sort(ans.begin(), ans.end());
        cout << "[";
        for (size_t i = 0; i < ans.size(); i++) {
            cout << "\\"" << ans[i] << "\\"" << (i + 1 == ans.size() ? "" : ", ");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        // User logic here
        return new String[0];
    }
}

public class Main {
    static String[] parseStringArray(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '"') {
                int j = i + 1;
                StringBuilder sb = new StringBuilder();
                while (j < s.length() && s.charAt(j) != '"') {
                    if (s.charAt(j) == '\\\\' && j + 1 < s.length()) {
                        sb.append(s.charAt(j+1));
                        j += 2;
                    } else {
                        sb.append(s.charAt(j));
                        j++;
                    }
                }
                res.add(sb.toString());
                i = j + 1;
            } else {
                i++;
            }
        }
        return res.toArray(new String[0]);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String str1 = sc.nextLine();
            if (sc.hasNextLine()) {
                String str2 = sc.nextLine();
                String[] list1 = parseStringArray(str1);
                String[] list2 = parseStringArray(str2);
                Solution sol = new Solution();
                String[] ans = sol.findRestaurant(list1, list2);
                Arrays.sort(ans);
                System.out.print("[");
                for (int i = 0; i < ans.length; i++) {
                    System.out.print("\\"" + ans[i] + "\\"" + (i + 1 == ans.length ? "" : ", "));
                }
                System.out.println("]");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const list1 = JSON.parse(input[0]);
    const list2 = JSON.parse(input[1]);
    const ans = findRestaurant(list1, list2);
    ans.sort();
    console.log(JSON.stringify(ans));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** findRestaurant(char** list1, int list1Size, char** list2, int list2Size, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int cmp(const void* a, const void* b) { return strcmp(*(char**)a, *(char**)b); }

char** parseStringArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    char** res = (char**)malloc(cap * sizeof(char*));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '"') {
            int j = i + 1;
            char buffer[200] = {0};
            int k = 0;
            while (input[j] && input[j] != '"') {
                if (input[j] == '\\\\') {
                    buffer[k++] = input[j+1];
                    j += 2;
                } else {
                    buffer[k++] = input[j];
                    j++;
                }
            }
            if (size == cap) { cap *= 2; res = realloc(res, cap * sizeof(char*)); }
            res[size] = (char*)malloc(strlen(buffer) + 1);
            strcpy(res[size], buffer);
            size++;
            i = j + 1;
        } else {
            i++;
        }
    }
    *outSize = size;
    return res;
}

int main() {
    char str1[50000], str2[50000];
    if (fgets(str1, sizeof(str1), stdin) && fgets(str2, sizeof(str2), stdin)) {
        int list1Size, list2Size;
        char** list1 = parseStringArray(str1, &list1Size);
        char** list2 = parseStringArray(str2, &list2Size);
        int returnSize;
        char** ans = findRestaurant(list1, list1Size, list2, list2Size, &returnSize);
        qsort(ans, returnSize, sizeof(char*), cmp);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("\\"%s\\"%s", ans[i], i + 1 == returnSize ? "" : ", ");
            free(ans[i]);
        }
        printf("]\\n");
        free(ans);
        for(int i=0; i<list1Size; i++) free(list1[i]);
        free(list1);
        for(int i=0; i<list2Size; i++) free(list2[i]);
        free(list2);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '["Shogun","Tapioca Express","Burger King","KFC"]\\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]', "expected_output": '["Shogun"]', "is_sample": True},
        {"input": '["Shogun","Tapioca Express","Burger King","KFC"]\\n["KFC","Shogun","Burger King"]', "expected_output": '["Shogun"]', "is_sample": True},
        {"input": '["happy","sad","good"]\\n["sad","happy","good"]', "expected_output": '["happy", "sad"]', "is_sample": False},
        {"input": '["KFC"]\\n["KFC"]', "expected_output": '["KFC"]', "is_sample": False},
        {"input": '["A","B","C"]\\n["C","B","A"]', "expected_output": '["B"]', "is_sample": False},
        {"input": '["A","B","C"]\\n["A","C","B"]', "expected_output": '["A"]', "is_sample": False},
        {"input": '["A","C","B"]\\n["B","C","A"]', "expected_output": '["C"]', "is_sample": False},
        {"input": '[' + ','.join([f'"A{i}"' for i in range(1000)]) + ']\\n[' + ','.join([f'"B{i}"' for i in range(999)] + ['"A0"']) + ']', "expected_output": '["A0"]', "is_sample": False},
        {"input": '[' + ','.join([f'"B{i}"' for i in range(1000)]) + ']\\n[' + ','.join([f'"B{999-i}"' for i in range(1000)]) + ']', "expected_output": '["B499", "B500"]', "is_sample": False},
        {"input": '[' + ','.join([f'"B{i}"' for i in range(999)] + ['"Shared"']) + ']\\n[' + ','.join(['"Shared"'] + [f'"A{i}"' for i in range(999)]) + ']', "expected_output": '["Shared"]', "is_sample": False}
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
        "topics": ["Array", "Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
