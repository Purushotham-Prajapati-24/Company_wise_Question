import json
import os

def generate_json():
    problem_id = 88
    title = "Merge Sorted Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>88. Merge Sorted Array</h3>
<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in <strong>non-decreasing order</strong>, and two integers <code>m</code> and <code>n</code>, representing the number of elements in <code>nums1</code> and <code>nums2</code> respectively.</p>

<p><strong>Merge</strong> <code>nums1</code> and <code>nums2</code> into a single array sorted in <strong>non-decreasing order</strong>.</p>

<p>The final sorted array should not be returned by the function, but instead be <em>stored inside the array </em><code>nums1</code>. To accommodate this, <code>nums1</code> has a length of <code>m + n</code>, where the first <code>m</code> elements represent the elements that should be merged, and the last <code>n</code> elements are set to <code>0</code> and should be ignored. <code>nums2</code> has a length of <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
<strong>Explanation:</strong> The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [1] and [].
The result of the merge is [1].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [0], m = 0, nums2 = [1], n = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>nums1.length == m + n</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= m + n &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "Line 1: m n (counts). Line 2: m space-separated integers for nums1. Line 3: n space-separated integers for nums2."
    output_format = "A single line containing m+n space-separated integers (the merged array)."
    
    constraints = [
        "0 <= m, n <= 200",
        "1 <= m + n <= 200",
        "nums1 and nums2 are sorted.",
        "Must merge in-place in nums1 (O(m+n) time, O(1) space)."
    ]
    
    explanation = """To merge two sorted arrays in-place (where the first array has extra space at the end):
1. **Three Pointers (Backwards)**:
   - Start from the end of the combined array (`p = m + n - 1`).
   - Use two pointers, `p1 = m - 1` and `p2 = n - 1`, pointing to the last valid elements of `nums1` and `nums2` respectively.
   - Compare `nums1[p1]` and `nums2[p2]`:
     - Place the larger element at `nums1[p]`.
     - Decrement the corresponding pointer (`p1` or `p2`) and the combined pointer `p`.
   - After the loop, if there are remaining elements in `nums2` (i.e., `p2 >= 0`), copy them into the beginning of `nums1`.
   - No need to check for remaining elements in `nums1` because they are already in the correct place.
2. **Complexity**:
   - Time Complexity: O(M + N).
   - Space Complexity: O(1) as we reuse the existing space in `nums1`."""
    
    answer = """def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If nums2 still has elements, copy them
    if p2 >= 0:
        nums1[:p2+1] = nums2[:p2+1]"""

    boilerplate = {
        "python": "import sys\n\ndef merge(nums1, m, nums2, n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 1:\n        m_n = lines[0].split()\n        if len(m_n) < 2: sys.exit(0)\n        m, n = int(m_n[0]), int(m_n[1])\n        nums1_base = [int(x) for x in lines[1].split()] if m > 0 else []\n        nums1 = nums1_base + [0]*n\n        nums2 = [int(x) for x in lines[2].split()] if n > 0 else []\n        merge(nums1, m, nums2, n)\n        print(*(nums1))",
        "cpp": "#include <iostream>\n#include <vector>\n\nusing namespace std;\n\nvoid merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {\n    // User logic\n}\n\nint main() {\n    int m, n;\n    if (!(cin >> m >> n)) return 0;\n    vector<int> nums1(m + n), nums2(n);\n    for(int i=0; i<m; ++i) cin >> nums1[i];\n    for(int i=0; i<n; ++i) cin >> nums2[i];\n    merge(nums1, m, nums2, n);\n    for(int i=0; i<m+n; ++i) cout << nums1[i] << (i==m+n-1 ? \"\" : \" \");\n    cout << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static void merge(int[] nums1, int m, int[] nums2, int n) {\n        // User logic\n    }\n    \n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextInt()) return;\n        int m = sc.nextInt();\n        int n = sc.nextInt();\n        int[] nums1 = new int[m + n];\n        for(int i=0; i<m; i++) nums1[i] = sc.nextInt();\n        int[] nums2 = new int[n];\n        for(int i=0; i<n; i++) nums2[i] = sc.nextInt();\n        merge(nums1, m, nums2, n);\n        for(int i=0; i<m+n; i++) System.out.print(nums1[i] + (i==m+n-1 ? \"\" : \" \"));\n        System.out.println();\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction merge(nums1, m, nums2, n) {\n    // User logic\n}\n\nconst input = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (input.length >= 1) {\n    const [m, n] = input[0].trim().split(/\\s+/).map(Number);\n    const nums1 = input[1] ? input[1].trim().split(/\\s+/).map(Number) : [];\n    const fullNums1 = nums1.concat(new Array(n).fill(0));\n    const nums2 = input[2] ? input[2].trim().split(/\\s+/).map(Number) : [];\n    merge(fullNums1, m, nums2, n);\n    console.log(fullNums1.join(' '));\n}",
        "c": "#include <stdio.h>\n\nvoid merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {\n    // User logic\n}\n\nint main() {\n    int m, n;\n    if (scanf(\"%d %d\", &m, &n) != 2) return 0;\n    int nums1[401], nums2[201];\n    for (int i = 0; i < m; i++) scanf(\"%d\", &nums1[i]);\n    for (int i = 0; i < n; i++) scanf(\"%d\", &nums2[i]);\n    merge(nums1, m + n, m, nums2, n, n);\n    for (int i = 0; i < m + n; i++) {\n        printf(\"%d\", nums1[i]);\n        if (i + 1 < m + n) printf(\" \");\n    }\n    printf(\"\\n\");\n    return 0;\n}"
    }

    def _solve(nums1, m, nums2, n):
        res = nums1[:m] + [0]*n
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if res[p1] > nums2[p2]:
                res[p] = res[p1]
                p1 -= 1
            else:
                res[p] = nums2[p2]
                p2 -= 1
            p -= 1
        if p2 >= 0:
            res[:p2+1] = nums2[:p2+1]
        return res

    def format_input(nums1, m, nums2, n):
        line1 = f"{m} {n}"
        line2 = " ".join(map(str, nums1[:m])) if m > 0 else ""
        line3 = " ".join(map(str, nums2)) if n > 0 else ""
        return f"{line1}\n{line2}\n{line3}".strip()

    test_cases = [
        {"input": format_input([1,2,3,0,0,0], 3, [2,5,6], 3), "expected_output": " ".join(map(str, _solve([1,2,3], 3, [2,5,6], 3))), "is_sample": True},
        {"input": format_input([1], 1, [], 0), "expected_output": "1", "is_sample": True},
        {"input": format_input([0], 0, [1], 1), "expected_output": "1", "is_sample": True},
        {"input": format_input([4,5,6], 3, [1,2,3], 3), "expected_output": "1 2 3 4 5 6", "is_sample": False},
        {"input": format_input([1,2,3], 3, [4,5,6], 3), "expected_output": "1 2 3 4 5 6", "is_sample": False},
        {"input": format_input([1,3,5], 3, [2,4,6], 3), "expected_output": "1 2 3 4 5 6", "is_sample": False},
        {"input": format_input([2], 1, [1], 1), "expected_output": "1 2", "is_sample": False},
        # Stress cases
        {"input": format_input(list(range(100)), 100, list(range(100)), 100), "expected_output": " ".join(map(str, sorted(list(range(100)) + list(range(100))))), "is_sample": False},
        {"input": format_input([i*2 for i in range(100)], 100, [i*2+1 for i in range(100)], 100), "expected_output": " ".join(map(str, range(200))), "is_sample": False},
        {"input": format_input([], 0, [1]*200, 200), "expected_output": " ".join(["1"]*200), "is_sample": False}
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
        "topics": ["Array", "Two Pointers", "Sorting"],
        "companyIndex": 0
    }

    output_path = "1-200/88_Merge_Sorted_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
