import json
import os

def generate_json():
    problem_id = 315
    title = "Count of Smaller Numbers After Self"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>315. Count of Smaller Numbers After Self</h3>
<p>You are given an integer array <code>nums</code> and you are required to return a new <code>counts</code> array. The <code>counts</code> array has the property that <code>counts[i]</code> is the number of smaller elements to the right of <code>nums[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [5,2,6,1]
<strong>Output:</strong> [2,1,1,0]
<strong>Explanation:</strong>
To the right of 5 there are <b>2</b> smaller elements (2 and 1).
To the right of 2 there is <b>1</b> smaller element (1).
To the right of 6 there is <b>1</b> smaller element (1).
To the right of 1 there is <b>0</b> smaller element.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [-1,-1]
<strong>Output:</strong> [0,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>"""

    input_format = "An array of integers `nums`."
    output_format = "An array of integers `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`."
    
    constraints = [
        "1 <= nums.length <= 10^5",
        "-10^4 <= nums[i] <= 10^4"
    ]
    
    explanation = """The problem asks to count smaller elements to the right of each element in an array. A naive $O(N^2)$ approach will exceed the time limit ($N=10^5$). 

The most optimized approach uses a **Binary Indexed Tree (BIT)** or **Fenwick Tree** after coordinate compression.

### Algorithm Steps:
1. **Coordinate Compression**: Since the range of values is small ($-10^4$ to $10^4$), but the number of elements is large, we map each unique value in `nums` to its rank (1 to $K$). This allows us to use the ranks as indices in the BIT.
2. **Backward Traversal**: Process the array from right to left. For each element `nums[i]`:
   - Use the BIT to query the number of elements already seen (visited to its right) that have a rank smaller than the current rank of `nums[i]`.
   - Update the BIT by incrementing the frequency of the current element's rank.
3. **BIT Operations**:
   - `update(idx, delta)`: Adds `delta` to index `idx` and propagates updates to ancestors.
   - `query(idx)`: Returns the prefix sum up to `idx` in $O(\log K)$ time.

### Complexity Analysis:
- **Time Complexity**: $O(N \log N)$, where $N$ is the length of the array. Coordinate compression takes $O(N \log N)$ and performing $N$ updates/queries on a BIT takes $O(N \log K)$ where $K \le N$.
- **Space Complexity**: $O(N)$ to store the BIT, ranks, and the result array."""
    
    answer = """class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(idx, val, bit, n):
            while idx <= n:
                bit[idx] += val
                idx += idx & (-idx)
        
        def query(idx, bit):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
        
        # Coordinate Compression
        unique_sorted = sorted(list(set(nums)))
        rank = {val: i + 1 for i, val in enumerate(unique_sorted)}
        m = len(unique_sorted)
        
        bit = [0] * (m + 1)
        res = []
        
        # Traverse from right to left
        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]
            res.append(query(r - 1, bit))
            update(r, 1, bit, m)
            
        return res[::-1]"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef countSmaller(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        nums = json.loads(data)\n        print(json.dumps(countSmaller(nums)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <sstream>\nusing namespace std;\n\nvector<int> countSmaller(vector<int>& nums) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string line;\n    getline(cin, line);\n    line.erase(remove(line.begin(), line.end(), '['), line.end());\n    line.erase(remove(line.begin(), line.end(), ']'), line.end());\n    vector<int> nums;\n    stringstream ss(line);\n    string token;\n    while (getline(ss, token, ',')) {\n        if (!token.empty()) nums.push_back(stoi(token));\n    }\n    vector<int> res = countSmaller(nums);\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        if (i) cout << \",\";\n        cout << res[i];\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<Integer> countSmaller(int[] nums) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        String line = sc.nextLine().trim().replaceAll(\"[\\\\[\\\\]\\\\s]\", \"\");\n        String[] parts = line.split(\",\");\n        int[] nums = new int[parts.length];\n        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);\n        List<Integer> res = new Solution().countSmaller(nums);\n        System.out.println(res.toString().replace(\" \", \"\"));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction countSmaller(nums) {\n    // User logic here\n    return [];\n}\n\nconst nums = JSON.parse(fs.readFileSync(0, 'utf-8').trim());\nconsole.log(JSON.stringify(countSmaller(nums)));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint* countSmaller(int* nums, int numsSize, int* returnSize) {\n    // User logic here\n    *returnSize = numsSize;\n    return (int*)calloc(numsSize, sizeof(int));\n}\n\nint main() {\n    char buf[65536];\n    fgets(buf, sizeof(buf), stdin);\n    int nums[100005], size = 0;\n    char* p = buf;\n    int neg = 0;\n    while (*p) {\n        if (*p == '-') { neg = 1; p++; }\n        else if (*p >= '0' && *p <= '9') {\n            int v = strtol(p, &p, 10);\n            nums[size++] = neg ? -v : v;\n            neg = 0;\n        } else { neg = 0; p++; }\n    }\n    int returnSize = 0;\n    int* res = countSmaller(nums, size, &returnSize);\n    printf(\"[\");\n    for (int i = 0; i < returnSize; i++) {\n        if (i) printf(\",\");\n        printf(\"%d\", res[i]);\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": "[5,2,6,1]", "expected_output": "[2,1,1,0]", "is_sample": True},
        {"input": "[-1]", "expected_output": "[0]", "is_sample": True},
        {"input": "[1,2,3,4]", "expected_output": "[0,0,0,0]", "is_sample": False},
        {"input": "[4,3,2,1]", "expected_output": "[3,2,1,0]", "is_sample": False},
        {"input": "[1,0,-1]", "expected_output": "[2,1,0]", "is_sample": False},
        {"input": "[1,1,1,1]", "expected_output": "[0,0,0,0]", "is_sample": False},
        {"input": "[2,0,1,0,0]", "expected_output": "[3,0,1,0,0]", "is_sample": False},
        {"input": "[5,4,3,2,1]", "expected_output": "[4,3,2,1,0]", "is_sample": False},
        {"input": "[0,0,0,0,0]", "expected_output": "[0,0,0,0,0]", "is_sample": False},
        {"input": "[3,1,2]", "expected_output": "[2,0,0]", "is_sample": False}
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
        "topics": ["Array", "Divide and Conquer", "Binary Indexed Tree", "Segment Tree", "Merge Sort", "Ordered Set"],
        "companyIndex": 1
    }

    output_path = "301-500/315_Count_of_Smaller_Numbers_After_Self.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
