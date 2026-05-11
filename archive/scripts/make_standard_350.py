import json
import os
from collections import Counter

def generate_json():
    problem_id = 350
    title = "Intersection of Two Arrays II"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>350. Intersection of Two Arrays II</h3>
<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must appear as many times as it shows in both arrays and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [4,9]
<strong>Explanation:</strong> [9,4] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
	<li>What if <code>nums1</code>'s size is small compared to <code>nums2</code>'s size? Which algorithm is better?</li>
	<li>What if elements of <code>nums2</code> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated integers for nums1. Line 2: space-separated integers for nums2."
    output_format = "Space-separated integers representing the intersection (including duplicates, sorted in ascending order for consistency)."
    
    constraints = [
        "1 <= nums1.length, nums2.length <= 1000",
        "0 <= nums1[i], nums2[i] <= 1000",
        "Result must reflect the frequency of shared elements.",
        "O(N + M) time complexity.",
        "O(min(N, M)) space complexity."
    ]
    
    explanation = """To find the intersection of two arrays while preserving frequencies:
1. **Hash Map Approach (Best for general cases)**:
   - Use a frequency map (e.g., `Counter` in Python) to count elements in the smaller array.
   - Iterate through the larger array. If an element exists in the map and its count > 0:
     - Add the element to the result.
     - Decrement the count in the map.
2. **Two Pointers Approach (Best if sorted)**:
   - Sort both arrays.
   - Use two pointers to compare elements. If they match, add to result and move both. If one is smaller, move that pointer.
3. **Complexity**:
   - Time Complexity: O(N + M).
   - Space Complexity: O(min(N, M)) to store the frequency map."""
    
    answer = """from collections import Counter

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    counts = Counter(nums1)
    res = []
    for x in nums2:
        if counts.get(x, 0) > 0:
            res.append(x)
            counts[x] -= 1
            
    return sorted(res)"""

    boilerplate = {
        "python": (
            "import sys\n"
            "import json\n"
            "from collections import Counter\n\n"
            "def intersect(nums1, nums2):\n"
            "    # User logic here\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    input_data = sys.stdin.read().splitlines()\n"
            "    if len(input_data) >= 2:\n"
            "        nums1 = json.loads(input_data[0].strip())\n"
            "        nums2 = json.loads(input_data[1].strip())\n"
            "        ans = intersect(nums1, nums2)\n"
            "        print(' '.join(map(str, sorted(ans))))"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <unordered_map>\n"
            "#include <algorithm>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {\n"
            "    // User logic here\n"
            "    return {};\n"
            "}\n\n"
            "vector<int> parseArray(string input) {\n"
            "    vector<int> res;\n"
            "    string val;\n"
            "    for (char c : input) {\n"
            "        if (isdigit(c) || c == '-') val += c;\n"
            "        else if (c == ',' || c == ']') {\n"
            "            if (!val.empty()) { res.push_back(stoi(val)); val = \"\"; }\n"
            "        }\n"
            "    }\n"
            "    return res;\n"
            "}\n\n"
            "int main() {\n"
            "    string line1, line2;\n"
            "    if (getline(cin, line1) && getline(cin, line2)) {\n"
            "        vector<int> nums1 = parseArray(line1);\n"
            "        vector<int> nums2 = parseArray(line2);\n"
            "        vector<int> ans = intersect(nums1, nums2);\n"
            "        sort(ans.begin(), ans.end());\n"
            "        for (size_t i = 0; i < ans.size(); i++) {\n"
            "            cout << ans[i] << (i == ans.size() - 1 ? \"\" : \" \");\n"
            "        }\n"
            "        cout << endl;\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    public static int[] intersect(int[] nums1, int[] nums2) {\n"
            "        // User logic here\n"
            "        return new int[0];\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextLine()) {\n"
            "            String line1 = sc.nextLine().trim();\n"
            "            if (!sc.hasNextLine()) return;\n"
            "            String line2 = sc.nextLine().trim();\n"
            "            \n"
            "            String[] p1 = line1.replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\").split(\",\");\n"
            "            String[] p2 = line2.replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\").split(\",\");\n"
            "            \n"
            "            int[] nums1 = new int[p1.length == 1 && p1[0].isEmpty() ? 0 : p1.length];\n"
            "            for (int i = 0; i < nums1.length; i++) nums1[i] = Integer.parseInt(p1[i]);\n"
            "            int[] nums2 = new int[p2.length == 1 && p2[0].isEmpty() ? 0 : p2.length];\n"
            "            for (int i = 0; i < nums2.length; i++) nums2[i] = Integer.parseInt(p2[i]);\n"
            "            \n"
            "            int[] ans = intersect(nums1, nums2);\n"
            "            Arrays.sort(ans);\n"
            "            StringBuilder sb = new StringBuilder();\n"
            "            for (int i = 0; i < ans.length; i++) {\n"
            "                sb.append(ans[i]);\n"
            "                if (i + 1 < ans.length) sb.append(' ');\n"
            "            }\n"
            "            System.out.println(sb.toString());\n"
            "        }\n"
            "    }\n"
            "}"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "function intersect(nums1, nums2) {\n"
            "    // User logic here\n"
            "    return [];\n"
            "}\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n"
            "    if (input.length >= 2) {\n"
            "        const nums1 = JSON.parse(input[0].trim());\n"
            "        const nums2 = JSON.parse(input[1].trim());\n"
            "        const ans = intersect(nums1, nums2);\n"
            "        ans.sort((a, b) => a - b);\n"
            "        console.log(ans.join(' '));\n"
            "    }\n"
            "}\n"
            "main();"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <string.h>\n"
            "#include <ctype.h>\n\n"
            "int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {\n"
            "    // User logic here\n"
            "    *returnSize = 0;\n"
            "    return NULL;\n"
            "}\n\n"
            "int cmpfunc(const void* a, const void* b) {\n"
            "    return (*(int*)a - *(int*)b);\n"
            "}\n\n"
            "void parseArray(char* input, int** arr, int* size) {\n"
            "    *size = 0;\n"
            "    *arr = (int*)malloc(1005 * sizeof(int));\n"
            "    char* p = input;\n"
            "    int val = 0; int sign = 1; int inNum = 0;\n"
            "    while (*p) {\n"
            "        if (*p == '-') { sign = -1; inNum = 1; }\n"
            "        else if (isdigit(*p)) { val = val * 10 + (*p - '0'); inNum = 1; }\n"
            "        else if (*p == ',' || *p == ']') {\n"
            "            if (inNum) { (*arr)[(*size)++] = val * sign; val = 0; sign = 1; inNum = 0; }\n"
            "        }\n"
            "        p++;\n"
            "    }\n"
            "}\n\n"
            "int main() {\n"
            "    char* line1 = NULL; size_t len1 = 0;\n"
            "    char* line2 = NULL; size_t len2 = 0;\n"
            "    if (getline(&line1, &len1, stdin) != -1 && getline(&line2, &len2, stdin) != -1) {\n"
            "        int* nums1; int size1;\n"
            "        parseArray(line1, &nums1, &size1);\n"
            "        int* nums2; int size2;\n"
            "        parseArray(line2, &nums2, &size2);\n"
            "        \n"
            "        int returnSize;\n"
            "        int* ans = intersect(nums1, size1, nums2, size2, &returnSize);\n"
            "        if (ans && returnSize > 0) {\n"
            "            qsort(ans, returnSize, sizeof(int), cmpfunc);\n"
            "        }\n"
            "        for (int i = 0; i < returnSize; i++) {\n"
            "            printf(\"%d%s\", ans[i], (i == returnSize - 1 ? \"\" : \" \"));\n"
            "        }\n"
            "        printf(\"\\n\");\n"
            "        \n"
            "        free(nums1);\n"
            "        free(nums2);\n"
            "        if (ans) free(ans);\n"
            "    }\n"
            "    if (line1) free(line1);\n"
            "    if (line2) free(line2);\n"
            "    return 0;\n"
            "}"
        )
    }

    test_cases = [
        {"input": "[1,2,2,1]\\n[2,2]", "expected_output": "2 2", "is_sample": True},
        {"input": "[4,9,5]\\n[9,4,9,8,4]", "expected_output": "4 9", "is_sample": True},
        {"input": "[1]\\n[1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2]\\n[3,4]", "expected_output": "", "is_sample": False},
        {"input": "[1,2,3]\\n[1,2,3]", "expected_output": "1 2 3", "is_sample": False},
        {"input": "[1,1,2,2]\\n[2,2,1,1]", "expected_output": "1 1 2 2", "is_sample": False},
        {"input": "[1,2,2]\\n[2]", "expected_output": "2", "is_sample": False},
        # Stress cases
        {"input": "[" + ",".join(["1"]*1000) + "]\\n[" + ",".join(["1"]*1000) + "]", "expected_output": " ".join(["1"]*1000), "is_sample": False},
        {"input": "[" + ",".join([str(i) for i in range(1000)]) + "]\\n[" + ",".join([str(i) for i in range(500, 1500)]) + "]", "expected_output": " ".join([str(i) for i in range(500, 1000)]), "is_sample": False},
        {"input": "[" + ",".join([str(i) for i in range(0, 1000, 2)]) + "]\\n[" + ",".join([str(i) for i in range(1, 1000, 2)]) + "]", "expected_output": "", "is_sample": False}
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
        "companyIndex": 0
    }

    output_path = "301-500/350_Intersection_of_Two_Arrays_II.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
