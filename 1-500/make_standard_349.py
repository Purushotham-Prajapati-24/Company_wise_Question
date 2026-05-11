import json
import os

def solve_intersection(nums1, nums2):
    return sorted(set(nums1) & set(nums2))

def generate_json():
    problem_id = 349
    title = "Intersection of Two Arrays"
    difficulty = "Easy"
    marks = 10

    html_description = """<h3>349. Intersection of Two Arrays</h3>
<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>.</p>
<p>Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
\t<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "Line 1: space-separated integers for `nums1`.\nLine 2: space-separated integers for `nums2`."
    output_format = "A sorted array of unique intersection elements, formatted as `[a,b,c]`."

    constraints = [
        "1 <= nums1.length, nums2.length <= 1000",
        "0 <= nums1[i], nums2[i] <= 1000"
    ]

    explanation = """We need unique elements present in both arrays.

### Approach — Hash Set:
1. Convert `nums1` to a set: `set1 = set(nums1)`.
2. Iterate through `nums2`; if an element is in `set1`, add it to a result set.
3. Return the result set as a sorted list.

### Complexity:
- **Time**: O(M + N) — building and probing the hash set.
- **Space**: O(min(M, N)) — for the result set."""

    answer = """def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return sorted(set(nums1) & set(nums2))"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\nclass Solution:\n    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    # Lethal parsing: find all bracketed number groups\n    matches = re.findall(r'\\[([^\\]]*)\\]', input_data)\n    if len(matches) >= 2:\n        nums1 = [int(x) for x in re.findall(r'-?\\d+', matches[0])]\n        nums2 = [int(x) for x in re.findall(r'-?\\d+', matches[1])]\n        res = Solution().intersection(nums1, nums2)\n        res.sort()\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {\n        // User logic here\n        return {};\n    }\n};\n\nvector<int> parse(string s) {\n    vector<int> r;\n    regex e(\"-?\\\\d+\");\n    for (sregex_iterator i(s.begin(), s.end(), e), d; i != d; ++i) r.push_back(stoi(i->str()));\n    return r;\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n\n    regex r(\"\\\\[([^\\\\]]*)\\\\]\");\n    auto it = sregex_iterator(input.begin(), input.end(), r);\n    auto ed = sregex_iterator();\n\n    if (it != ed) {\n        vector<int> n1 = parse(it->str());\n        if (++it != ed) {\n            vector<int> n2 = parse(it->str());\n            Solution sol;\n            vector<int> res = sol.intersection(n1, n2);\n            sort(res.begin(), res.end());\n            cout << \"[\";\n            for (int i = 0; i < res.size(); i++) {\n                cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n            }\n            cout << \"]\" << endl;\n        }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int[] intersection(int[] nums1, int[] nums2) {\n        // User logic here\n        return new int[0];\n    }\n}\n\npublic class Main {\n    static int[] parse(String s) {\n        List<Integer> l = new ArrayList<>();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(s);\n        while (m.find()) l.add(Integer.parseInt(m.group()));\n        return l.stream().mapToInt(i -> i).toArray();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n\n        Matcher m = Pattern.compile(\"\\\\[([^\\\\]]*)\\\\]\").matcher(input);\n        if (m.find()) {\n            int[] n1 = parse(m.group());\n            if (m.find()) {\n                int[] n2 = parse(m.group());\n                Solution sol = new Solution();\n                int[] res = sol.intersection(n1, n2);\n                Arrays.sort(res);\n                System.out.println(Arrays.toString(res).replace(\" \", \"\"));\n            }\n        }\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\n/**\n * @param {number[]} nums1\n * @param {number[]} nums2\n * @return {number[]}\n */\nvar intersection = function(nums1, nums2) {\n    // User logic here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const matches = input.match(/\\[([^\\]]*)\\]/g);\n    if (matches && matches.length >= 2) {\n        const n1 = JSON.parse(matches[0]);\n        const n2 = JSON.parse(matches[1]);\n        const res = intersection(n1, n2);\n        res.sort((a, b) => a - b);\n        console.log(JSON.stringify(res).replace(/ /g, ''));\n    }\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\n/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint compare(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint main() {\n    static int n1[10001], n2[10001];\n    int c1 = 0, c2 = 0, val;\n    char ch;\n\n    while ((ch = getchar()) != '[' && ch != EOF);\n    while (scanf(\"%d\", &val) == 1) {\n        n1[c1++] = val;\n        if ((ch = getchar()) == ']') break;\n    }\n\n    while ((ch = getchar()) != '[' && ch != EOF);\n    while (scanf(\"%d\", &val) == 1) {\n        n2[c2++] = val;\n        if ((ch = getchar()) == ']') break;\n    }\n\n    int rs = 0;\n    int* res = intersection(n1, c1, n2, c2, &rs);\n    if (res) {\n        qsort(res, rs, sizeof(int), compare);\n        printf(\"[\");\n        for (int i = 0; i < rs; i++) {\n            printf(\"%d%s\", res[i], (i == rs - 1 ? \"\" : \",\"));\n        }\n        printf(\"]\\n\");\n        free(res);\n    } else {\n        printf(\"[]\\n\");\n    }\n    return 0;\n}"
    }


    # Precompute stress test data
    # Stress 1: large arrays with half overlap
    import random
    random.seed(42)
    s1_nums1 = list(range(500)) + list(range(0, 500, 2))   # 750 elements
    s1_nums2 = list(range(0, 1000, 2))                     # even numbers 0-998
    s1_out = solve_intersection(s1_nums1, s1_nums2)

    # Stress 2: full overlap (identical arrays of max size)
    s2_base = list(range(1000))
    s2_out = solve_intersection(s2_base, s2_base)

    # Stress 3: no overlap at all
    s3_nums1 = list(range(500))
    s3_nums2 = list(range(500, 1000))
    s3_out = solve_intersection(s3_nums1, s3_nums2)   # empty

    test_cases = [
        # 2 sample cases
        {"input": "[1,2,2,1]\n[2,2]", "expected_output": "[2]", "is_sample": True},
        {"input": "[4,9,5]\n[9,4,9,8,4]", "expected_output": "[4,9]", "is_sample": True},
        # 5 diverse cases
        {"input": "[1,2,3]\n[4,5,6]", "expected_output": "[]", "is_sample": False},
        {"input": "[1,1,1]\n[1,1,1]", "expected_output": "[1]", "is_sample": False},
        {"input": "[0,1,2,3,4]\n[3,4,5,6]", "expected_output": "[3,4]", "is_sample": False},
        {"input": "[1000]\n[1000]", "expected_output": "[1000]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8,9,10]\n[2,4,6,8,10,12]", "expected_output": "[2,4,6,8,10]", "is_sample": False},
        # 3 stress cases (precomputed)
        {
            "input": json.dumps(s1_nums1) + "\n" + json.dumps(s1_nums2),
            "expected_output": "[" + ",".join(map(str, s1_out)) + "]",
            "is_sample": False
        },
        {
            "input": json.dumps(s2_base) + "\n" + json.dumps(s2_base),
            "expected_output": "[" + ",".join(map(str, s2_out)) + "]",
            "is_sample": False
        },
        {
            "input": json.dumps(s3_nums1) + "\n" + json.dumps(s3_nums2),
            "expected_output": "[]",
            "is_sample": False
        },
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
        "topics": ["Array", "Hash Table", "Two Pointers", "Binary Search", "Sorting"],
        "companyIndex": 1
    }

    output_path = "301-500/349_Intersection_of_Two_Arrays.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
