import json
import os

def solve_top_k(nums, k):
    from collections import Counter
    counts = Counter(nums)
    return sorted(counts.keys(), key=lambda x: -counts[x])[:k]

def generate_json():
    problem_id = 347
    title = "Top K Frequent Elements"
    difficulty = "Medium"
    marks = 10

    html_description = """<h3>347. Top K Frequent Elements</h3>
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the </em><code>k</code><em> most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
\t<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
\t<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
\t<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>"""

    input_format = "Line 1: space-separated integers for `nums`.\nLine 2: integer `k`."
    output_format = "The k most frequent elements as a sorted array `[a,b,c]`."

    constraints = [
        "1 <= nums.length <= 100,000",
        "-10^4 <= nums[i] <= 10^4",
        "k is in range [1, number of unique elements]",
        "The answer is guaranteed to be unique"
    ]

    explanation = """To find the top-k frequent elements faster than O(N log N):

### Bucket Sort Approach — O(N):
1. **Count Frequencies**: `counts = Counter(nums)` → `{1:3, 2:2, 3:1}`.
2. **Build Buckets**: An array `buckets` where index = frequency; `buckets[i]` holds all elements with that frequency.
3. **Collect from right**: Traverse buckets right-to-left, collecting elements until we have `k`.

### Complexity:
- **Time**: O(N) — dominates counting and bucket traversal.
- **Space**: O(N) — for the frequency map and buckets."""

    answer = """import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\nclass Solution:\n    def topKFrequent(self, nums: list[int], k: int) -> list[int]:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    all_ints = list(map(int, re.findall(r'-?\\d+', input_data)))\n    if all_ints:\n        k = all_ints[-1]\n        nums = all_ints[:-1]\n        res = Solution().topKFrequent(nums, k)\n        res.sort()\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<int> topKFrequent(vector<int>& nums, int k) {\n        // User logic here\n        return {};\n    }\n};\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n\n    regex re(\"-?\\\\d+\");\n    vector<int> all_ints;\n    auto begin = sregex_iterator(input.begin(), input.end(), re);\n    auto end = sregex_iterator();\n    for (auto i = begin; i != end; ++i) all_ints.push_back(stoi(i->str()));\n\n    if (!all_ints.empty()) {\n        int k = all_ints.back();\n        all_ints.pop_back();\n        Solution sol;\n        vector<int> res = sol.topKFrequent(all_ints, k);\n        sort(res.begin(), res.end());\n        cout << \"[\";\n        for (int i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \",\");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public int[] topKFrequent(int[] nums, int k) {\n        // User logic here\n        return new int[0];\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n        \n        List<Integer> allInts = new ArrayList<>();\n        Matcher m = Pattern.compile(\"-?\\\\d+\").matcher(input);\n        while (m.find()) allInts.add(Integer.parseInt(m.group()));\n\n        if (!allInts.isEmpty()) {\n            int k = allInts.get(allInts.size() - 1);\n            int[] nums = new int[allInts.size() - 1];\n            for (int i = 0; i < nums.length; i++) nums[i] = allInts.get(i);\n\n            Solution sol = new Solution();\n            int[] res = sol.topKFrequent(nums, k);\n            Arrays.sort(res);\n            System.out.println(Arrays.toString(res).replace(\" \", \"\"));\n        }\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\n/**\n * @param {number[]} nums\n * @param {number} k\n * @return {number[]}\n */\nvar topKFrequent = function(nums, k) {\n    // User logic here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const allInts = (input.match(/-?\\d+/g) || []).map(Number);\n    if (allInts.length > 0) {\n        const k = allInts.pop();\n        const res = topKFrequent(allInts, k);\n        res.sort((a, b) => a - b);\n        console.log(JSON.stringify(res).replace(/ /g, ''));\n    }\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\n/**\n * Note: The returned array must be malloced, assume caller calls free().\n */\nint* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint compare(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint main() {\n    static int nums[1000001];\n    int count = 0;\n    int val;\n    char ch;\n    \n    while (scanf(\"%d\", &val) == 1) {\n        nums[count++] = val;\n        while ((ch = getchar()) != EOF && !isdigit(ch) && ch != '-' && ch != '[' && ch != ']' && ch != ',');\n        if (ch != EOF) ungetc(ch, stdin);\n    }\n\n    if (count > 0) {\n        int k = nums[count - 1];\n        int returnSize = 0;\n        int* res = topKFrequent(nums, count - 1, k, &returnSize);\n        qsort(res, returnSize, sizeof(int), compare);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], (i == returnSize - 1 ? \"\" : \",\"));\n        }\n        printf(\"]\\n\");\n        free(res);\n    }\n    return 0;\n}"
    }


    # Precompute stress test data
    import random
    random.seed(42)

    # Stress 1: large array, k=10
    s1_nums = [random.randint(0, 99) for _ in range(100000)]
    s1_k = 10
    s1_res = sorted(solve_top_k(s1_nums, s1_k))

    # Stress 2: all same element
    s2_nums = [5] * 100000
    s2_k = 1
    s2_res = [5]

    # Stress 3: 10000 unique elements, k=50
    s3_nums = list(range(-5000, 5000)) * 2  # 20000 elements, each appears twice
    random.shuffle(s3_nums)
    s3_k = 50
    s3_res = sorted(solve_top_k(s3_nums, s3_k))

    test_cases = [
        # 2 sample cases
        {"input": "[1,1,1,2,2,3]\n2", "expected_output": "[1,2]", "is_sample": True},
        {"input": "[1]\n1", "expected_output": "[1]", "is_sample": True},
        # 5 diverse cases
        {"input": "[1,1,2,2,2,3,3,3,3]\n2", "expected_output": "[2,3]", "is_sample": False},
        {"input": "[-1,-1,2,2,2,3]\n2", "expected_output": "[-1,2]", "is_sample": False},
        {"input": "[1,1,1,1,1]\n1", "expected_output": "[1]", "is_sample": False},
        {"input": "[4,4,4,4,6,6,6,8,8,1,2,3]\n2", "expected_output": "[4,6]", "is_sample": False},
        {"input": "[1,2,2,3,3,3,4,4,4,4]\n3", "expected_output": "[2,3,4]", "is_sample": False},
        # 3 stress cases (precomputed)
        {
            "input": json.dumps(s1_nums) + "\n" + str(s1_k),
            "expected_output": json.dumps(s1_res).replace(" ", ""),
            "is_sample": False
        },
        {
            "input": json.dumps(s2_nums) + "\n" + str(s2_k),
            "expected_output": "[5]",
            "is_sample": False
        },
        {
            "input": json.dumps(s3_nums) + "\n" + str(s3_k),
            "expected_output": json.dumps(s3_res).replace(" ", ""),
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
        "topics": ["Array", "Hash Table", "Divide and Conquer", "Sorting", "Heap (Priority Queue)", "Bucket Sort", "Quickselect"],
        "companyIndex": 1
    }

    output_path = "301-500/347_Top_K_Frequent_Elements.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
