import json
import os

def generate_json():
    problem_id = 239
    title = "Sliding Window Maximum"
    difficulty = "HARD"
    marks = 20
    
    html_description = """<h3>239. Sliding Window Maximum</h3>
<p>You are given an array of integers&nbsp;<code>nums</code>, there is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the max sliding window</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong> 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7       <strong>5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>"""

    input_format = "Two lines: first, an array of integers; second, an integer k."
    output_format = "An array of maximums for each window."
    
    constraints = [
        "1 <= nums.length <= 100,000",
        "-10,000 <= nums[i] <= 10,000",
        "1 <= k <= nums.length",
        "O(n) time complexity required."
    ]
    
    explanation = """To find the sliding window maximum in O(n) time:
1. **Monotonic Deque**: Use a deque to store indices of potential candidates for the maximum in the current window.
2. **Logic**:
   - For each element `nums[i]`:
     - **Remove out-of-bound**: If the index at the front of the deque is `i - k`, remove it (it's no longer in the window).
     - **Maintain Monotonicity**: Remove indices from the back of the deque if the corresponding values in `nums` are less than or equal to `nums[i]`. This ensures the deque is sorted such that the front always has the index of the maximum value.
     - **Add current index**: Append `i` to the back of the deque.
     - **Extract Result**: If `i >= k - 1`, the front of the deque is the maximum for the current window.
3. **Complexity**:
   - Time: O(N) because each index is added and removed from the deque at most once.
   - Space: O(K) for the deque."""
    
    answer = """from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(len(nums)):
            # remove out of window
            if dq and dq[0] == i - k:
                dq.popleft()
            # remove smaller items from back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            # record max
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\ndef maxSlidingWindow(nums, k):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        match = re.search(r'\\[.*?\\]', input_data[0])\n        str_arr = match.group(0) if match else input_data[0]\n        str_arr = str_arr.replace('[', '').replace(']', '').replace(',', ' ')\n        nums = [int(x) for x in str_arr.split()]\n        \n        num_match = re.findall(r'-?\\d+', input_data[1])\n        k = int(num_match[-1]) if num_match else 0\n        \n        print(json.dumps(maxSlidingWindow(nums, k)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <algorithm>\n#include <regex>\n\nusing namespace std;\n\nvector<int> maxSlidingWindow(vector<int>& nums, int k) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line, kLine;\n    if (getline(cin, line) && getline(cin, kLine)) {\n        regex num_re(\"[-]?\\\\d+\");\n        vector<int> nums;\n        auto words_begin = sregex_iterator(line.begin(), line.end(), num_re);\n        auto words_end = sregex_iterator();\n        for (sregex_iterator i = words_begin; i != words_end; ++i) nums.push_back(stoi(i->str()));\n        \n        smatch m;\n        int k = 0;\n        if (regex_search(kLine, m, num_re)) k = stoi(m.str());\n        \n        vector<int> res = maxSlidingWindow(nums, k);\n        cout << \"[\";\n        for (size_t i = 0; i < res.size(); i++) {\n            cout << res[i] << (i == res.size() - 1 ? \"\" : \", \");\n        }\n        cout << \"]\" << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public int[] maxSlidingWindow(int[] nums, int k) {\n        // User logic here\n        return new int[0];\n    }\n\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line = br.readLine();\n        String kLine = br.readLine();\n        if (line != null && kLine != null) {\n            List<Integer> list = new ArrayList<>();\n            Matcher m = Pattern.compile(\"[-]?\\\\d+\").matcher(line);\n            while (m.find()) list.add(Integer.parseInt(m.group()));\n            \n            int[] nums = new int[list.size()];\n            for (int i = 0; i < list.size(); i++) nums[i] = list.get(i);\n            \n            int k = 0;\n            Matcher mk = Pattern.compile(\"[-]?\\\\d+\").matcher(kLine);\n            if (mk.find()) k = Integer.parseInt(mk.group());\n            \n            int[] res = new Solution().maxSlidingWindow(nums, k);\n            System.out.println(Arrays.toString(res));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction maxSlidingWindow(nums, k) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8').split(/\\r?\\n/);\nif (input.length >= 2) {\n    const match = input[0].match(/\\[.*\\]/)?.[0] || input[0];\n    const nums = match.replace(/[\\[\\]]/g, '').split(',').map(s => parseInt(s.trim())).filter(n => !isNaN(n));\n    \n    const k = parseInt(input[1].match(/[-]?\\d+/)?.[0]);\n    \n    console.log(JSON.stringify(maxSlidingWindow(nums, k)));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nint* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {\n    // User logic here\n    *returnSize = numsSize - k + 1;\n    return NULL;\n}\n\nint main() {\n    static char line[1000000];\n    char kLine[100];\n    if (fgets(line, sizeof(line), stdin) && fgets(kLine, sizeof(kLine), stdin)) {\n        int* nums = (int*)malloc(100000 * sizeof(int));\n        int size = 0;\n        char* p = line;\n        while (*p) {\n            if (isdigit(*p) || *p == '-') {\n                nums[size++] = strtol(p, &p, 10);\n            } else p++;\n        }\n        \n        char* kp = kLine; while (*kp && !isdigit(*kp) && *kp != '-') kp++;\n        int k = atoi(kp);\n        \n        int returnSize = 0;\n        int* res = maxSlidingWindow(nums, size, k, &returnSize);\n        printf(\"[\");\n        for (int i = 0; i < returnSize; i++) {\n            printf(\"%d%s\", res[i], i == returnSize - 1 ? \"\" : \", \");\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[1,3,-1,-3,5,3,6,7]\\n3", "expected_output": "[3, 3, 5, 5, 6, 7]", "is_sample": True},
        {"input": "[1]\\n1", "expected_output": "[1]", "is_sample": True},
        {"input": "[1,-1]\\n1", "expected_output": "[1, -1]", "is_sample": False},
        {"input": "[1,-1]\\n2", "expected_output": "[1]", "is_sample": False},
        {"input": "[7,2,4]\\n2", "expected_output": "[7, 4]", "is_sample": False},
        {"input": "[1,3,1,2,0,5]\\n3", "expected_output": "[3, 3, 2, 5]", "is_sample": False},
        {"input": "[1,2,3,4,5,6,7,8]\\n4", "expected_output": "[4, 5, 6, 7, 8]", "is_sample": False},
        # Stress Tests (100,000 nodes)
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False},
        {"input": "...", "expected_output": "...", "is_sample": False}
    ]
    
    def _solve_swm(nums, k):
        from collections import deque
        dq = deque()
        res = []
        for i in range(len(nums)):
            if dq and dq[0] == i-k: dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]: dq.pop()
            dq.append(i)
            if i >= k-1: res.append(nums[dq[0]])
        return res

    # Stress 8: 100,000 sorted
    n8 = list(range(100000))
    test_cases[7] = {"input": json.dumps(n8) + "\\n5000", "expected_output": json.dumps(_solve_swm(n8, 5000)), "is_sample": False}
    # Stress 9: 100,000 reverse sorted
    n9 = list(range(100000, 0, -1))
    test_cases[8] = {"input": json.dumps(n9) + "\\n5000", "expected_output": json.dumps(_solve_swm(n9, 5000)), "is_sample": False}
    # Stress 10: 100,000 all same
    n10 = [5] * 100000
    test_cases[9] = {"input": json.dumps(n10) + "\\n1000", "expected_output": json.dumps([5] * (100000 - 1000 + 1)), "is_sample": False}

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
        "topics": ["Array", "Sliding Window", "Monotonic Queue", "Heap (Priority Queue)"],
        "companyIndex": 0
    }

    output_path = "201-400/239_Sliding_Window_Maximum.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
