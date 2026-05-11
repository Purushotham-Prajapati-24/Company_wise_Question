import json
import os

def generate_json():
    problem_id = 609
    title = "Find Duplicate File in System"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>609. Find Duplicate File in System</h3>
<p>Given a list <code>paths</code> of directory info, including the directory path, and all the files with contents in this directory, return <em>all the duplicate files in the file system in terms of their paths</em>. You may return the answer in <strong>any order</strong>.</p>

<p>A group of duplicate files consists of at least two files that have the same content.</p>

<p>A single directory info string in the input list has the following format:</p>

<ul>
    <li><code>"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"</code></li>
</ul>

<p>It means there are <code>n</code> files <code>(f1.txt, f2.txt ... fn.txt)</code> with content <code>(f1_content, f2_content ... fn_content)</code> respectively in the directory <code>root/d1/d2/.../dm</code>. Note that <code>n &gt;= 1</code> and <code>m &gt;= 0</code>. If <code>m = 0</code>, it means the directory is just the root directory.</p>

<p>The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:</p>

<ul>
    <li><code>"directory_path/file_name.txt"</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
<strong>Output:</strong> [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
<strong>Output:</strong> [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= paths.length &lt;= 2 * 10<sup>4</sup></code></li>
    <li><code>1 &lt;= paths[i].length &lt;= 3000</code></li>
    <li><code>1 &lt;= sum(paths[i].length) &lt;= 5 * 10<sup>5</sup></code></li>
    <li><code>paths[i]</code> consist of English letters, digits, <code>'/'</code>, <code>'.'</code>, <code>'('</code>, <code>')'</code>, and <code>' '</code>.</li>
    <li>You may assume no files or directories share the same name in the same directory.</li>
    <li>You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.</li>
</ul>"""

    input_format = "A single line: A JSON array of strings `paths`."
    output_format = "A JSON array of array of strings, where each sub-array contains paths to files with the same content. Sorted lexicographically."

    constraints = [
        "1 <= paths.length <= 2 * 10^4",
        "Strings follow the specified format.",
        "Output is a 2D array of sorted arrays."
    ]

    explanation = """Use a hash map where the key is the file content and the value is a list of file paths. Parse each string into a directory and its files. For each file, extract its path and content, putting the path into the list corresponding to the content in the map. Finally, filter the map values to include only groups with at least 2 file paths."""

    answer = """from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_map = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for file_info in parts[1:]:
                # file_info = "f1.txt(f1_content)"
                name_end = file_info.find('(')
                file_name = file_info[:name_end]
                content = file_info[name_end+1:-1]
                content_map[content].append(f"{directory}/{file_name}")
                
        return [group for group in content_map.values() if len(group) > 1]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        paths = json.loads(raw)
        sol = Solution()
        ans = sol.findDuplicate(paths)
        for group in ans:
            group.sort()
        ans.sort(key=lambda x: x[0])
        print(json.dumps(ans))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
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
    string input;
    if (getline(cin, input)) {
        vector<string> paths = parseStringArray(input);
        Solution sol;
        vector<vector<string>> ans = sol.findDuplicate(paths);
        for (auto& group : ans) sort(group.begin(), group.end());
        sort(ans.begin(), ans.end());
        cout << "[";
        for (size_t i = 0; i < ans.size(); i++) {
            cout << "[";
            for (size_t j = 0; j < ans[i].size(); j++) {
                cout << "\\"" << ans[i][j] << "\\"" << (j + 1 == ans[i].size() ? "" : ",");
            }
            cout << "]" << (i + 1 == ans.size() ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        // User logic here
        return new ArrayList<>();
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
            String[] paths = parseStringArray(str1);
            Solution sol = new Solution();
            List<List<String>> ans = sol.findDuplicate(paths);
            for (List<String> group : ans) Collections.sort(group);
            ans.sort((a,b) -> a.get(0).compareTo(b.get(0)));
            System.out.print("[");
            for (int i = 0; i < ans.size(); i++) {
                System.out.print("[");
                for (int j = 0; j < ans.get(i).size(); j++) {
                    System.out.print("\\"" + ans.get(i).get(j) + "\\"" + (j + 1 == ans.get(i).size() ? "" : ","));
                }
                System.out.print("]" + (i + 1 == ans.size() ? "" : ","));
            }
            System.out.println("]");
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} paths
 * @return {string[][]}
 */
var findDuplicate = function(paths) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const paths = JSON.parse(input);
    const ans = findDuplicate(paths);
    for (let group of ans) group.sort();
    ans.sort((a, b) => a[0].localeCompare(b[0]));
    console.log(JSON.stringify(ans));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char*** findDuplicate(char** paths, int pathsSize, int* returnSize, int** returnColumnSizes) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int cmpStr(const void* a, const void* b) { return strcmp(*(char**)a, *(char**)b); }
int cmpGrp(const void* a, const void* b) { 
    char** grpA = *(char***)a; 
    char** grpB = *(char***)b; 
    return strcmp(grpA[0], grpB[0]); 
}

char** parseStringArray(char* input, int* outSize) {
    int cap = 10, size = 0, i = 0;
    char** res = (char**)malloc(cap * sizeof(char*));
    while (input[i] && input[i] != '\\n') {
        if (input[i] == '"') {
            int j = i + 1;
            char buffer[5000] = {0};
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
    char input[500000];
    if (fgets(input, sizeof(input), stdin)) {
        int pathsSize;
        char** paths = parseStringArray(input, &pathsSize);
        int returnSize;
        int* returnColumnSizes;
        char*** ans = findDuplicate(paths, pathsSize, &returnSize, &returnColumnSizes);
        for(int i=0; i<returnSize; i++) {
            qsort(ans[i], returnColumnSizes[i], sizeof(char*), cmpStr);
        }
        qsort(ans, returnSize, sizeof(char**), cmpGrp);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("[");
            for (int j = 0; j < returnColumnSizes[i]; j++) {
                printf("\\"%s\\"%s", ans[i][j], j + 1 == returnColumnSizes[i] ? "" : ",");
            }
            printf("]%s", i + 1 == returnSize ? "" : ",");
        }
        printf("]\\n");
        // Memory leak expected in standard C boilerplate since no deep free given. 
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": '["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]', "expected_output": '[["root/4.txt","root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]', "is_sample": True},
        {"input": '["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]', "expected_output": '[["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt"]]', "is_sample": True},
        {"input": '["root/a 1.txt(abcd)","root/b 2.txt(abcd)","root/c 3.txt(abcd)"]', "expected_output": '[["root/a/1.txt","root/b/2.txt","root/c/3.txt"]]', "is_sample": False},
        {"input": '["root/a 1.txt(A)","root/b 2.txt(B)"]', "expected_output": '[]', "is_sample": False},
        {"input": '["x/y 1.t(a) 2.t(b) 3.t(a) 4.t(b)"]', "expected_output": '[["x/y/1.t","x/y/3.t"],["x/y/2.t","x/y/4.t"]]', "is_sample": False},
        {"input": '["a b(z)","c d(z) e(y)","f g(y)"]', "expected_output": '[["a/b","c/d"],["c/e","f/g"]]', "is_sample": False},
        {"input": '["a/b/c 1.t(1)","a/b/c 2.t(1)"]', "expected_output": '[["a/b/c/1.t","a/b/c/2.t"]]', "is_sample": False},
        {"input": '["root/x ' + " ".join(f"{i}.txt({i})" for i in range(100)) + '","root/y ' + " ".join(f"{i}.txt({i})" for i in range(100)) + '"]', 
         "expected_output": '[' + ",".join('["root/x/' + str(i) + '.txt","root/y/' + str(i) + '.txt"]' for i in range(100)) + ']', "is_sample": False},
        {"input": '["root/a 1(aa)","root/b 2(aa)","root/c 3(aa)","root/d 4(aa)"]', "expected_output": '[["root/a/1","root/b/2","root/c/3","root/d/4"]]', "is_sample": False},
        {"input": '["root/a 1.txt(abc) 2.txt(def)","root/b 3.txt(abc) 4.txt(def)"]', "expected_output": '[["root/a/1.txt","root/b/3.txt"],["root/a/2.txt","root/b/4.txt"]]', "is_sample": False}
    ]
    # Sorting expected output manually
    for t in test_cases:
        if t["expected_output"] == '[]': continue
        exp = json.loads(t["expected_output"])
        for g in exp: g.sort()
        exp.sort(key=lambda x: x[0])
        t["expected_output"] = json.dumps(exp).replace(" ", "")

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

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
