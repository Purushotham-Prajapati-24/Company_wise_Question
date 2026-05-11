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
        "python": (
            "import sys\n"
            "import json\n\n"
            "def intersection(nums1, nums2):\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    input_data = sys.stdin.read().splitlines()\n"
            "    if len(input_data) >= 2:\n"
            "        nums1 = json.loads(input_data[0].strip())\n"
            "        nums2 = json.loads(input_data[1].strip())\n"
            "        res = intersection(nums1, nums2)\n"
            "        res.sort()\n"
            "        print(json.dumps(res).replace(\" \", \"\"))"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <unordered_set>\n"
            "#include <algorithm>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {\n"
            "    // User logic here\n"
            "    return {};\n"
            "}\n\n"
            "vector<int> parseArray(string input) {\n"
            "    vector<int> res;\n"
            "    string val;\n"
            "    for (char c : input) {\n"
            "        if (isdigit(c) || c == '-') val += c;\n"
            "        else if (!val.empty()) {\n"
            "            res.push_back(stoi(val));\n"
            "            val = \"\";\n"
            "        }\n"
            "    }\n"
            "    if (!val.empty()) res.push_back(stoi(val));\n"
            "    return res;\n"
            "}\n\n"
            "int main() {\n"
            "    string line1, line2;\n"
            "    if (getline(cin, line1) && getline(cin, line2)) {\n"
            "        vector<int> nums1 = parseArray(line1);\n"
            "        vector<int> nums2 = parseArray(line2);\n"
            "        auto res = intersection(nums1, nums2);\n"
            "        sort(res.begin(), res.end());\n"
            "        cout << \"[\";\n"
            "        for (size_t i = 0; i < res.size(); i++) {\n"
            "            cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n"
            "        }\n"
            "        cout << \"]\" << endl;\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "java": (
            "import java.util.*;\n"
            "import java.util.stream.Collectors;\n\n"
            "public class Main {\n"
            "    public static int[] intersection(int[] nums1, int[] nums2) {\n"
            "        // User logic here\n"
            "        return new int[0];\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextLine()) {\n"
            "            String line1 = sc.nextLine();\n"
            "            String[] p1 = line1.replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\").split(\",\");\n"
            "            int[] nums1 = Arrays.stream(p1).filter(s -> !s.isEmpty()).mapToInt(Integer::parseInt).toArray();\n"
            "            if (sc.hasNextLine()) {\n"
            "                String line2 = sc.nextLine();\n"
            "                String[] p2 = line2.replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\").split(\",\");\n"
            "                int[] nums2 = Arrays.stream(p2).filter(s -> !s.isEmpty()).mapToInt(Integer::parseInt).toArray();\n"
            "                int[] res = intersection(nums1, nums2);\n"
            "                Arrays.sort(res);\n"
            "                System.out.println(\"[\" + Arrays.stream(res).mapToObj(String::valueOf).collect(Collectors.joining(\",\")) + \"]\");\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "/**\n"
            " * @param {number[]} nums1\n"
            " * @param {number[]} nums2\n"
            " * @return {number[]}\n"
            " */\n"
            "var intersection = function(nums1, nums2) {\n"
            "    // User logic here\n"
            "    return [];\n"
            "};\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').split('\\n');\n"
            "    if (input.length >= 2) {\n"
            "        const nums1 = JSON.parse(input[0].trim());\n"
            "        const nums2 = JSON.parse(input[1].trim());\n"
            "        const res = intersection(nums1, nums2).sort((a, b) => a - b);\n"
            "        process.stdout.write(JSON.stringify(res).replace(/\\s+/g, '') + '\\n');\n"
            "    }\n"
            "}\n"
            "main();"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "#include <ctype.h>\n\n"
            "int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {\n"
            "    // User logic here\n"
            "    *returnSize = 0;\n"
            "    return NULL;\n"
            "}\n\n"
            "int cmp(const void* a, const void* b) { return *(int*)a - *(int*)b; }\n\n"
            "int main() {\n"
            "    char* line1 = NULL; size_t len1 = 0;\n"
            "    char* line2 = NULL; size_t len2 = 0;\n"
            "    if (getline(&line1, &len1, stdin) != -1 && getline(&line2, &len2, stdin) != -1) {\n"
            "        int nums1[1010], nums2[1010], n1 = 0, n2 = 0;\n"
            "        char* p = line1;\n"
            "        while (*p) {\n"
            "            if (isdigit(*p) || *p == '-') { nums1[n1++] = strtol(p, &p, 10); }\n"
            "            else p++;\n"
            "        }\n"
            "        p = line2;\n"
            "        while (*p) {\n"
            "            if (isdigit(*p) || *p == '-') { nums2[n2++] = strtol(p, &p, 10); }\n"
            "            else p++;\n"
            "        }\n"
            "        int returnSize = 0;\n"
            "        int* res = intersection(nums1, n1, nums2, n2, &returnSize);\n"
            "        if (res) qsort(res, returnSize, sizeof(int), cmp);\n"
            "        printf(\"[\");\n"
            "        for (int i = 0; i < returnSize; i++) {\n"
            "            printf(\"%d%s\", res[i], (i == returnSize - 1 ? \"\" : \",\"));\n"
            "        }\n"
            "        printf(\"]\\n\");\n"
            "        if (res) free(res);\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
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
