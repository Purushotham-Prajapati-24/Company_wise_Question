import json
import os

def generate_json():
    problem_id = 4
    title = "Median of Two Sorted Arrays"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>4. Median of Two Sorted Arrays</h3>
<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>
"""

    input_format = "Line 1: Space-separated integers for nums1.\nLine 2: Space-separated integers for nums2."
    output_format = "A float representing the median value."
    
    constraints = [
        "0 <= m, n <= 1000",
        "1 <= m + n <= 2000",
        "-10^6 <= nums1[i], nums2[i] <= 10^6",
        "Overall complexity: O(log(m+n))"
    ]
    
    explanation = """To find the median of two sorted arrays in O(log(min(M, N))) time:
1. Ensure nums1 is the smaller array.
2. Use binary search on the partitions of the smaller array.
3. Partition both arrays at index 'i' and 'j' such that:
   - i + j = (M + N + 1) // 2
   - All elements in left halves are less than or equal to all elements in right halves:
     - nums1[i-1] <= nums2[j]
     - nums2[j-1] <= nums1[i]
4. Once the correct partition is found:
   - If (M + N) is odd, median = max(nums1[LX], nums2[LY]).
   - If (M + N) is even, median = (max(nums1[LX], nums2[LY]) + min(nums1[RX], nums2[RY])) / 2.0.

This approach performs binary search on the shorter array, ensuring logarithmic time complexity relative to the total number of elements."""
    
    answer = """def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        partitionX = (left + right) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == m else nums1[partitionX]
        
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == n else nums2[partitionY]
        
        if maxX <= minY and maxY <= minX:
            if (m + n) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2.0
            else:
                return float(max(maxX, maxY))
        elif maxX > minY:
            right = partitionX - 1
        else:
            left = partitionX + 1"""

    # STRICT boilerplate style from make_standard_120.py
    boilerplate = {
        "python": "import sys\n\ndef findMedianSortedArrays(nums1, nums2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 2:\n        nums1 = [int(x) for x in data[0].replace('[','').replace(']','').replace(',',' ').split()]\n        nums2 = [int(x) for x in data[1].replace('[','').replace(']','').replace(',',' ').split()]\n        res = findMedianSortedArrays(nums1, nums2)\n        print(f\"{res:.5f}\")",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <iomanip>\n#include <algorithm>\n\nusing namespace std;\n\ndouble findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {\n    // User logic here\n    return 0.0;\n}\n\nvector<int> parseArray(string line) {\n    for (char &c : line) if (c == '[' || c == ']' || c == ',') c = ' ';\n    stringstream ss(line);\n    int num;\n    vector<int> res;\n    while (ss >> num) res.push_back(num);\n    return res;\n}\n\nint main() {\n    string n1, n2;\n    if (getline(cin, n1) && getline(cin, n2)) {\n        vector<int> nums1 = parseArray(n1);\n        vector<int> nums2 = parseArray(n2);\n        cout << fixed << setprecision(5) << findMedianSortedArrays(nums1, nums2) << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Main {\n    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {\n        // User logic here\n        return 0.0;\n    }\n    \n    public static int[] parseArray(String line) {\n        line = line.replaceAll(\"[\\\\[\\\\],]\", \" \").trim();\n        if (line.isEmpty()) return new int[0];\n        String[] parts = line.split(\"\\\\s+\");\n        int[] res = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i]);\n        return res;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            int[] nums1 = parseArray(sc.nextLine());\n            int[] nums2 = sc.hasNextLine() ? parseArray(sc.nextLine()) : new int[0];\n            System.out.printf(\"%.5f\\n\", findMedianSortedArrays(nums1, nums2));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction findMedianSortedArrays(nums1, nums2) {\n    // User logic here\n    return 0.0;\n}\n\nfunction parseArray(str) {\n    const parts = str.replace(/[\\\\[\\\\]]/g, ' ').replace(/,/g, ' ').trim().split(/\\s+/);\n    return parts.filter(p => p !== '').map(Number);\n}\n\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const nums1 = parseArray(input[0]);\n    const nums2 = parseArray(input[1]);\n    const res = findMedianSortedArrays(nums1, nums2);\n    console.log(res.toFixed(5));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\ndouble findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {\n    // User logic here\n    return 0.0;\n}\n\nvoid parseArray(char* line, int** nums, int* size) {\n    for (int i = 0; line[i]; i++) if (line[i] == '[' || line[i] == ']' || line[i] == ',') line[i] = ' ';\n    int cap = 100, count = 0;\n    *nums = (int*)malloc(cap * sizeof(int));\n    char* pt = line;\n    while (*pt != '\\0') {\n        if (isdigit(*pt) || (*pt == '-' && isdigit(*(pt+1)))) {\n            if (count >= cap) {\n                cap *= 2;\n                *nums = (int*)realloc(*nums, cap * sizeof(int));\n            }\n            (*nums)[count++] = atoi(pt);\n            while (*pt != '\\0' && (isdigit(*pt) || *pt == '-')) pt++;\n        } else { pt++; }\n    }\n    *size = count;\n}\n\nint main() {\n    char line1[100000];\n    char line2[100000];\n    if (fgets(line1, sizeof(line1), stdin) && fgets(line2, sizeof(line2), stdin)) {\n        int *nums1 = NULL, *nums2 = NULL;\n        int size1 = 0, size2 = 0;\n        parseArray(line1, &nums1, &size1);\n        parseArray(line2, &nums2, &size2);\n        printf(\"%.5f\\n\", findMedianSortedArrays(nums1, size1, nums2, size2));\n        free(nums1); free(nums2);\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "1 3\n2", "expected_output": "2.00000", "is_sample": True},
        {"input": "1 2\n3 4", "expected_output": "2.50000", "is_sample": True},
        # Middle five: Diverse non-duplicate cases
        {"input": "0 0\n0 0", "expected_output": "0.00000", "is_sample": False},
        {"input": " \n1", "expected_output": "1.00000", "is_sample": False},
        {"input": "2\n ", "expected_output": "2.00000", "is_sample": False},
        {"input": "1 3 8 9 15\n7 11 18 19 21 25", "expected_output": "11.00000", "is_sample": False},
        {"input": "23 26 31 35\n3 5 7 9 11 16", "expected_output": "13.50000", "is_sample": False},
        # Last three: Stress tests
        {"input": " ".join([str(i) for i in range(1000)]) + "\n" + " ".join([str(i+1000) for i in range(1000)]), "expected_output": "999.50000", "is_sample": False},
        {"input": " ".join(["1"] * 1000) + "\n" + " ".join(["9"] * 1000), "expected_output": "5.00000", "is_sample": False},
        {"input": " ".join([str(i*2) for i in range(1000)]) + "\n" + " ".join([str(i*2+1) for i in range(1000)]), "expected_output": "999.50000", "is_sample": False}
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
        "topics": ["Array", "Binary Search", "Divide and Conquer"],
        "companyIndex": 0
    }

    output_path = "1-200/4_Median_of_Two_Sorted_Arrays.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
