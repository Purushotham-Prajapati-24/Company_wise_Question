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
        "python": "import sys\nimport json\n\ndef hIndex(citations):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        citations = json.loads(input_data)\n        print(hIndex(citations))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint hIndex(vector<int>& citations) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    vector<int> citations;\n    int x;\n    while (cin >> x) citations.push_back(x);\n    cout << hIndex(citations) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int hIndex(int[] citations) {\n        // User logic here\n        return 0;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        List<Integer> list = new ArrayList<>();\n        while (sc.hasNextInt()) list.add(sc.nextInt());\n        int[] arr = list.stream().mapToInt(i -> i).toArray();\n        System.out.println(new Solution().hIndex(arr));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction hIndex(citations) {\n    // User logic here\n    return 0;\n}\n\nconst citations = fs.readFileSync(0, 'utf-8').trim().split(/\\s+/).map(Number);\nconsole.log(hIndex(citations));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n\nint hIndex(int* citations, int citationsSize) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    int* citations = malloc(10000 * sizeof(int));\n    int size = 0;\n    while (scanf(\"%d\", &citations[size]) == 1) size++;\n    printf(\"%d\\n\", hIndex(citations, size));\n    return 0;\n}"
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
