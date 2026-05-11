import json
import os

def generate_json():
    problem_id = 274
    title = "H-Index"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>274. H-Index</h3>
<p>Given an array of integers <code>citations</code> where <code>citations[i]</code> is the number of citations a researcher received for their <code>i<sup>th</sup></code> paper, return <em>the researcher's h-index</em>.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/H-index" target="_blank">definition of h-index on Wikipedia</a>: The h-index is defined as the maximum value of <code>h</code> such that the given researcher has published at least <code>h</code> papers that have each been cited at least <code>h</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> citations = [3,0,6,1,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> citations = [1,3,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == citations.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>0 &lt;= citations[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "A stringified array of integers `citations`."
    output_format = "An integer representing the h-index."
    
    constraints = [
        "1 <= n <= 5000",
        "0 <= citations[i] <= 1000"
    ]
    
    explanation = """The H-Index is the maximum `h` such that at least `h` papers have `h` or more citations.
1. **Counting Sort Approach**: Since the maximum possible h-index is `n`, we can use a counting array of size `n + 1`.
2. **Tabulation**: We count how many papers have `x` citations. If `citations[i] > n`, we count it in the `n`-th bucket (since any citation count above `n` still contributes to an h-index up to `n`).
3. **Cumulative Sum**: We iterate from `n` down to 0, maintaining a running sum of the number of papers found so far. The first value `h` where the cumulative sum is greater than or equal to `h` is the h-index.
4. **Complexity**:
   - Time: O(N) because we iterate through the array once to count and once to find the index.
   - Space: O(N) for the counting array."""
    
    answer = """class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # Use an array to count the number of papers for each citation count
        # For citation counts greater than n, we count them as n
        count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
                
        # To find the h-index, we need the cumulative number of papers starting from the highest citation
        total_papers = 0
        for h in range(n, -1, -1):
            total_papers += count[h]
            if total_papers >= h:
                return h
                
        return 0"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef hIndex(citations: list[int]) -> int:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Extract citations = [3,0,6,1,5] or just [3,0,6,1,5]\n    arr_match = re.search(r'\\[([^\\]]*)\\]', raw_input)\n    if arr_match:\n        content = arr_match.group(1)\n        citations = [int(x) for x in re.findall(r'-?\\d+', content)]\n    else:\n        citations = [int(x) for x in re.findall(r'-?\\d+', raw_input)]\n    print(hIndex(citations))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nint hIndex(vector<int>& citations) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    vector<int> citations;\n    regex re_num(R\"(-?\\d+)\");\n    \n    size_t start_pos = input.find('[');\n    size_t end_pos = input.find(']', start_pos);\n    \n    string search_target = input;\n    if (start_pos != string::npos && end_pos != string::npos) {\n        search_target = input.substr(start_pos, end_pos - start_pos + 1);\n    }\n    \n    auto words_begin = sregex_iterator(search_target.begin(), search_target.end(), re_num);\n    auto words_end = sregex_iterator();\n    \n    for (sregex_iterator i = words_begin; i != words_end; ++i) {\n        citations.push_back(stoi(i->str()));\n    }\n    \n    cout << hIndex(citations) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int hIndex(int[] citations) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        List<Integer> list = new ArrayList<>();\n        Pattern p = Pattern.compile(\"(-?\\\\d+)\");\n        \n        int start = input.indexOf('[');\n        int end = input.indexOf(']', start);\n        String searchTarget = (start != -1 && end != -1) ? input.substring(start, end + 1) : input;\n        \n        Matcher m = p.matcher(searchTarget);\n        while (m.find()) {\n            list.add(Integer.parseInt(m.group()));\n        }\n        \n        int[] arr = new int[list.size()];\n        for (int i = 0; i < list.size(); i++) arr[i] = list.get(i);\n        System.out.println(new Solution().hIndex(arr));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction hIndex(citations) {\n    // User logic here\n    return 0;\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst start = input.indexOf('[');\nconst end = input.indexOf(']', start);\nconst target = (start !== -1 && end !== -1) ? input.substring(start, end + 1) : input;\n\nconst citations = (target.match(/-?\\d+/g) || []).map(Number);\nconsole.log(hIndex(citations));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint hIndex(int* citations, int citationsSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    static char buffer[1000000];\n    int* citations = malloc(100000 * sizeof(int));\n    int size = 0;\n    \n    if (fread(buffer, 1, 999999, stdin) > 0) {\n        char *start = strchr(buffer, '[');\n        char *end = start ? strchr(start, ']') : NULL;\n        if (start && end) *end = '\\0';\n        \n        char *p = start ? start : buffer;\n        while (*p) {\n            if (isdigit(*p) || (*p == '-' && isdigit(*(p+1)))) {\n                citations[size++] = atoi(p);\n                while (*p && (isdigit(*p) || *p == '-')) p++;\n            } else {\n                p++;\n            }\n        }\n    }\n    \n    printf(\"%d\\n\", hIndex(citations, size));\n    free(citations);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[3,0,6,1,5]", "expected_output": "3", "is_sample": True},
        {"input": "[1,3,1]", "expected_output": "1", "is_sample": True},
        {"input": "[0]", "expected_output": "0", "is_sample": False},
        {"input": "[100]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "2", "is_sample": False},
        {"input": "[4,4,4,4]", "expected_output": "4", "is_sample": False},
        {"input": "[0,0,0,0]", "expected_output": "0", "is_sample": False},
        # Stress cases
        {"input": "[" + ",".join(["1000"]*5000) + "]", "expected_output": "5000", "is_sample": False},
        {"input": "[" + ",".join(["0"]*5000) + "]", "expected_output": "0", "is_sample": False},
        {"input": "[" + ",".join([str(i % 1000) for i in range(5000)]) + "]", "expected_output": "917", "is_sample": False} 
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
        "topics": ["Array", "Sorting", "Hash Table", "Counting Sort"],
        "companyIndex": 0
    }

    output_path = "201-400/274_H_Index.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
