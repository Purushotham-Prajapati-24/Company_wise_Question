import json
import os

def generate_json():
    problem_id = 373
    title = "Find K Pairs with Smallest Sums"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>373. Find K Pairs with Smallest Sums</h3>
<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code> sorted in <strong>non-decreasing order</strong> and an integer <code>k</code>.</p>

<p>Define a pair <code>(u, v)</code> which consists of one element from <code>nums1</code> and one element from <code>nums2</code>.</p>

<p>Return <em>the </em><code>k</code><em> pairs </em><code>(u<sub>1</sub>, v<sub>1</sub>), (u<sub>2</sub>, v<sub>2</sub>), ..., (u<sub>k</sub>, v<sub>k</sub>)</code><em> with the smallest sums</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums1 = [1,7,11], nums2 = [2,4,6], k = 3
<strong>Output:</strong> [[1,2],[1,4],[1,6]]
<strong>Explanation:</strong> The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums1 = [1,1,2], nums2 = [1,2,3], k = 2
<strong>Output:</strong> [[1,1],[1,1]]
<strong>Explanation:</strong> The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums1</code> and <code>nums2</code> both are sorted in <strong>non-decreasing order</strong>.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>k &lt;= nums1.length * nums2.length</code></li>
</ul>"""

    input_format = "Two sorted integer arrays `nums1`, `nums2` and an integer `k`."
    output_format = "A list of $k$ list representing pairs with smallest sums."
    
    constraints = [
        "1 <= nums1.length, nums2.length <= 100,000",
        "nums1, nums2 are sorted.",
        "1 <= k <= 10,000"
    ]
    
    explanation = """To find the $k$ pairs with the smallest sums efficiently from two sorted arrays, we can use a **Min-Heap**.

### Key Concept:
Since the arrays are sorted, the smallest possible pair is always `(nums1[0], nums2[0])`. The next smallest pair will be either `(nums1[1], nums2[0])` or `(nums1[0], nums2[1])`. We can generalize this by exploring possible pairs starting from $0$.

### Algorithm Steps:
1. **Initialize Heap**: Push the first $min(k, len(nums1))$ elements of `nums1` paired with `nums2[0]` into a min-heap.
   - The heap stores `(sum, index1, index2)`.
   - `heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))` for $i \in [0, k)$.
2. **Loop $k$ times**:
   - Extract the smallest element from the heap: `(current_sum, i, j)`.
   - Store the pair `[nums1[i], nums2[j]]` in the result.
   - If `j + 1 < len(nums2)`:
     - Push the next available pair with the same `nums1[i]`: `(nums1[i] + nums2[j+1], i, j+1)`.
3. **Optimality**: Because arrays are sorted, we greedily explore the smallest sums.

### Example Walkthrough (nums1=[1,7], nums2=[2,4,6], k=3):
- Heap: `[(1+2, 0, 0), (7+2, 1, 0)]`
- Pop `(3, 0, 0)`, pair `[1,2]`. Push `(1+4, 0, 1)`.
- Heap: `[(5, 0, 1), (9, 1, 0)]`
- Pop `(5, 0, 1)`, pair `[1,4]`. Push `(1+6, 0, 2)`.
- Heap: `[(7, 0, 2), (9, 1, 0)]`
- Pop `(7, 0, 2)`, pair `[1,6]`. Stop (we have $k=3$).

### Complexity Analysis:
- **Time Complexity**: $O(K \log K)$, where $K$ is the number of pairs to return.
- **Space Complexity**: $O(K)$ to store at most $K$ elements in the heap."""
    
    answer = """import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2:
            return res
            
        # Min-heap to store (sum, i, j)
        pq = []
        
        # Optimization: We only need to start with at most k elements from nums1
        for i in range(min(len(nums1), k)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
            
        while pq and len(res) < k:
            curr_sum, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            
            # If we extract (i, j), the next smallest candidate for this row is (i, j+1)
            if j + 1 < len(nums2):
                heapq.heappush(pq, (nums1[i] + nums2[j+1], i, j+1))
                
        return res"""

    boilerplate = {
        "python": "import sys\nimport json\nimport heapq\n\nclass Solution:\n    def kSmallestPairs(self, nums1, nums2, k):\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        nums1 = data['nums1']\n        nums2 = data['nums2']\n        k = data['k']\n        sol = Solution()\n        print(json.dumps(sol.kSmallestPairs(nums1, nums2, k)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n#include <algorithm>\nusing namespace std;\n\nclass Solution {\npublic:\n    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {\n        // Your logic here\n        return {};\n    }\n};",
        "java": "import java.util.*;\n\npublic class Solution {\n    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {\n        // Your logic here\n        return new ArrayList<>();\n    }\n}",
        "javascript": "/**\n * @param {number[]} nums1\n * @param {number[]} nums2\n * @param {number} k\n * @return {number[][]}\n */\nvar kSmallestPairs = function(nums1, nums2, k) {\n    // Your logic here\n};",
        "c": "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the arrays are returned as *returnColumnSizes array.\n */\nint** kSmallestPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize, int** returnColumnSizes) {\n    // Your logic here\n    return NULL;\n}"
    }

    test_cases = [
        {"input": '{"nums1": [1,7,11], "nums2": [2,4,6], "k": 3}', "expected_output": "[[1,2],[1,4],[1,6]]", "is_sample": True},
        {"input": '{"nums1": [1,1,2], "nums2": [1,2,3], "k": 2}', "expected_output": "[[1,1],[1,1]]", "is_sample": True},
        {"input": '{"nums1": [1,2], "nums2": [3], "k": 3}', "expected_output": "[[1,3],[2,3]]", "is_sample": False},
        {"input": '{"nums1": [1], "nums2": [2], "k": 1}', "expected_output": "[[1,2]]", "is_sample": False},
        {"input": '{"nums1": [1,1,1], "nums2": [1,1,1], "k": 9}', "expected_output": "[[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]", "is_sample": False},
        {"input": '{"nums1": [1,2,11], "nums2": [2,4,6], "k": 3}', "expected_output": "[[1,2],[2,2],[1,4]]", "is_sample": False},
        {"input": '{"nums1": [-10,-4,0,0,6], "nums2": [3,5,6,7,8,100], "k": 10}', "expected_output": "...", "is_sample": False},
        # Stress cases
        {"input": '{"nums1": [i for i in range(100000)], "nums2": [i for i in range(100000)], "k": 10000}', "expected_output": "...", "is_sample": False},
        {"input": '{"nums1": [-1000000000], "nums2": [-1000000000], "k": 1}', "expected_output": "[[-1000000000,-1000000000]]", "is_sample": False},
        {"input": '{"nums1": [1,1,1], "nums2": [1,1,1], "k": 2}', "expected_output": "[[1,1],[1,1]]", "is_sample": False}
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
        "topics": ["Array", "Heap (Priority Queue)"],
        "companyIndex": 1
    }

    output_path = "301-500/373_Find_K_Pairs_with_Smallest_Sums.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
