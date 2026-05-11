import json
import os
from collections import defaultdict

def generate_json():
    problem_id = 49
    title = "Group Anagrams"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>49. Group Anagrams</h3>
<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "A single line containing space-separated strings for 'strs'."
    output_format = "A list of lists containing grouped anagrams. The order of groups and the order of strings within groups do not matter."
    
    constraints = [
        "1 <= strs.length <= 10^4",
        "0 <= strs[i].length <= 100",
        "strs[i] consists of lowercase English letters."
    ]
    
    explanation = """To group anagrams together efficiently:
1. Two strings are anagrams if they contain the same characters with the same frequencies.
2. We can use a hash map (dictionary) where the keys represent a unique identifier for a set of anagrams, and the values are lists of the original strings.
3. **Key Generation**:
   - **Method A (Sorting)**: Sort the characters of each string. For example, "eat", "tea", and "ate" all become "aet". This sorted string serves as the key.
   - **Method B (Categorize by Count)**: Count the frequency of each character (a-z) and use the resulting sequence of 26 counts as a key.
4. For every string in the input:
   - Generate its key.
   - Append the string to the list associated with that key in the dictionary.
5. Finally, return the values of the dictionary as a list of lists.

Complexity:
- Time Complexity: O(N * K log K) using the sorting method, where N is the number of strings and K is the maximum length of a string.
- Space Complexity: O(N * K) to store the grouped strings in the dictionary."""
    
    answer = """from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        # Sort the characters of the string to use as a key
        key = "".join(sorted(s))
        ans[key].append(s)
    
    # Return grouped values as a list of lists
    return list(ans.values())"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys\nfrom collections import defaultdict\n\ndef groupAnagrams(strs):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip().split()\n    if input_data:\n        # Handle case where strings might be empty wrapped in quotes or just space\n        print(groupAnagrams(input_data))\n    else:\n        # Likely empty input\n        print(groupAnagrams([]))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nvector<vector<string>> groupAnagrams(vector<string>& strs) {\n    // User logic\n    return {};\n}\n\nint main() {\n    string s;\n    vector<string> strs;\n    while (cin >> s) strs.push_back(s);\n    auto res = groupAnagrams(strs);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        cout << \"[\";\n        for (int j = 0; j < (int)res[i].size(); j++) {\n            cout << \"'\" << res[i][j] << \"'\";\n            if (j + 1 < (int)res[i].size()) cout << \", \";\n        }\n        cout << \"]\";\n        if (i + 1 < (int)res.size()) cout << \", \";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static List<List<String>> groupAnagrams(String[] strs) {\n        // User logic\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<String> list = new ArrayList<>();\n        while (sc.hasNext()) list.add(sc.next());\n        List<List<String>> res = groupAnagrams(list.toArray(new String[0]));\n        StringBuilder sb = new StringBuilder(\"[\");\n        for (int i = 0; i < res.size(); i++) {\n            sb.append(\"[\");\n            List<String> group = res.get(i);\n            for (int j = 0; j < group.size(); j++) {\n                sb.append(\"'\").append(group.get(j)).append(\"'\");\n                if (j + 1 < group.size()) sb.append(\", \");\n            }\n            sb.append(\"]\");\n            if (i + 1 < res.size()) sb.append(\", \");\n        }\n        sb.append(\"]\");\n        System.out.println(sb.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction groupAnagrams(strs) {\n    // User logic\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);\nconst res = groupAnagrams(input);\nconsole.log('[' + res.map(g => '[' + g.map(s => \"'\" + s + \"'\").join(', ') + ']').join(', ') + ']');",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n// C groupAnagrams is complex; skeleton placeholder\nchar*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {\n    // User logic\n    *returnSize = 0;\n    *returnColumnSizes = NULL;\n    return NULL;\n}\n\nint main() {\n    char words[1000][101];\n    int size = 0;\n    while (size < 1000 && scanf(\"%100s\", words[size]) == 1) size++;\n    char* strs[1000];\n    for (int i = 0; i < size; i++) strs[i] = words[i];\n    int returnSize = 0;\n    int* returnColumnSizes = NULL;\n    char*** res = groupAnagrams(strs, size, &returnSize, &returnColumnSizes);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        printf(\"[\");\n        for (int j = 0; j < returnColumnSizes[i]; j++) {\n            printf(\"'%s'\", res[i][j]);\n            if (j + 1 < returnColumnSizes[i]) printf(\", \");\n            free(res[i][j]);\n        }\n        printf(\"]\");\n        if (i + 1 < returnSize) printf(\", \");\n        free(res[i]);\n    }\n    printf(\"]\\n\");\n    if (returnColumnSizes) free(returnColumnSizes);\n    if (res) free(res);\n    return 0;\n}"
    }

    def _group(strs):
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        # Sort internal lists for stable expected output comparison
        res = [sorted(v) for v in d.values()]
        return sorted(res)

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "eat tea tan ate nat bat", "expected_output": str(_group(["eat","tea","tan","ate","nat","bat"])), "is_sample": True},
        {"input": "\"\"", "expected_output": "[[\"\"]]", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "a", "expected_output": "[['a']]", "is_sample": False},
        {"input": "abc cab bca xyz zyx", "expected_output": str(_group(["abc", "cab", "bca", "xyz", "zyx"])), "is_sample": False},
        {"input": "a b c d", "expected_output": str(_group(["a", "b", "c", "d"])), "is_sample": False},
        {"input": "aa aa aa", "expected_output": str(_group(["aa", "aa", "aa"])), "is_sample": False},
        {"input": "ab ba cd dc", "expected_output": str(_group(["ab", "ba", "cd", "dc"])), "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join(["a" * 100] * 1000), "expected_output": str(_group(["a" * 100] * 1000)), "is_sample": False},
        {"input": " ".join(["".join(sorted(list("abcdefghij"))) for _ in range(100)]), "expected_output": str(_group(["".join(sorted(list("abcdefghij"))) for _ in range(100)])), "is_sample": False},
        {"input": " ".join([str(i) for i in range(100)]), "expected_output": str(_group([str(i) for i in range(100)])), "is_sample": False}
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
        "topics": ["Array", "Hash Table", "String", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/49_Group_Anagrams.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
