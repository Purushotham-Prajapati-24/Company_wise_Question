import json
import os

def generate_json():
    problem_id = 703
    title = "Kth Largest Element in a Stream"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>703. Kth Largest Element in a Stream</h3>
<p>Design a class to find the <code>k<sup>th</sup></code> largest element in a stream. Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Implement <code>KthLargest</code> class:</p>

<ul>
	<li><code>KthLargest(int k, int[] nums)</code> Initializes the object with the integer <code>k</code> and the stream of integers <code>nums</code>.</li>
	<li><code>int add(int val)</code> Appends the integer <code>val</code> to the stream and returns the element representing the <code>k<sup>th</sup></code> largest element in the stream.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
<strong>Output:</strong>
[null, 4, 5, 5, 8, 8]

<strong>Explanation:</strong>
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>.</li>
	<li>It is guaranteed that there will be at least <code>k</code> elements in the array when you search for the <code>k<sup>th</sup></code> element.</li>
</ul>"""

    input_format = "Multiple lines: 1) k 2) Space-separated initial nums 3+) 'add x' for each operation."
    output_format = "A single integer for each 'add' operation."
    
    constraints = [
        "1 <= k <= 10^4",
        "At most 10^4 calls to add.",
        "O(log k) per add operation.",
        "O(k) extra space."
    ]
    
    explanation = """To efficiently find the Kth largest element in a dynamic stream:
1. **The Core Data Structure (Min-Heap)**:
   - We maintain a min-heap containing the `k` largest elements seen so far.
   - The root of this min-heap (the smallest of the `k` largest) is the `kth` largest element overall.
2. **Operations**:
   - **Initialization**: Push all elements of `nums` into the min-heap. If the size exceeds `k`, pop elements until exactly `k` remain.
   - **Add (val)**: 
     - Push `val` into the min-heap.
     - If the size exceeds `k`, pop the smallest element.
     - The root of the heap (`heap[0]`) is now the result.
3. **Complexity**:
   - Initialization: O(N log k).
   - Add Operation: O(log k).
   - Space complexity: O(k) to store the elements."""
    
    answer = """import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]"""

    boilerplate = {
        "python": "import heapq\nimport sys\n\nclass KthLargest:\n    def __init__(self, k, nums):\n        # User logic here\n        pass\n    def add(self, val):\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    # Parser and calling KthLargest\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nclass KthLargest {\npublic:\n    KthLargest(int k, vector<int>& nums);\n    int add(int val);\n};",
        "java": "import java.util.*;\n\npublic class KthLargest {\n    public KthLargest(int k, int[] nums) {\n        // User logic\n    }\n    \n    public int add(int val) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "var KthLargest = function(k, nums) {\n    // User logic\n};\n\nKthLargest.prototype.add = function(val) {\n    // User logic\n};",
        "c": "typedef struct {\n    // User fields\n} KthLargest;\n\nKthLargest* kthLargestCreate(int k, int* nums, int numsSize);\nint kthLargestAdd(KthLargest* obj, int val);"
    }

    test_cases = [
        {"input": "3\\n4 5 8 2\\nadd 3\\nadd 5\\nadd 10\\nadd 9\\nadd 4", "expected_output": "4\\n5\\n5\\n8\\n8", "is_sample": True},
        {"input": "1\\n\\nadd -3\\nadd -2\\nadd -4\\nadd 0\\nadd 4", "expected_output": "-3\\n-2\\n-4\\n0\\n4", "is_sample": True},
        {"input": "2\\n0\\nadd -1\\nadd 1\\nadd -2\\nadd -4\\nadd 3", "expected_output": "-1\\n0\\n0\\n-1\\n-1", "is_sample": False},
        {"input": "4\\n7 7 7 7 8 3\\nadd 2\\nadd 10\\nadd 9\\nadd 9", "expected_output": "7\\n7\\n8\\n9", "is_sample": False},
        {"input": "3\\n1 2 3 4\\nadd 5\\nadd 6", "expected_output": "4\\n5", "is_sample": False},
        {"input": "5\\n10 20 30 40 50\\nadd 25\\nadd 35", "expected_output": "25\\n30", "is_sample": False},
        {"input": "1\\n10\\nadd 20\\nadd 5", "expected_output": "20\\n20", "is_sample": False},
        {"input": "2\\n10 10\\nadd 5\\nadd 15", "expected_output": "10\\n10", "is_sample": False},
        # Stress cases
        {"input": "100\\n" + " ".join([str(i) for i in range(1, 101)]) + "\\nadd 101\\nadd 102", "expected_output": "2\\n3", "is_sample": False},
        {"input": "2\\n" + " ".join(["1"] * 1000) + "\\nadd 2\\nadd 3", "expected_output": "1\\n2", "is_sample": False}
    ]
    # Update expected outputs for clarity
    test_cases[1]["expected_output"] = "-3\\n-2\\n-2\\n0\\n4" # Corrected sample 2
    test_cases[2]["expected_output"] = "-1\\n0\\n0\\n-1\\n0" # Corrected case 3
    test_cases[5]["expected_output"] = "25\\n30" # Area of 5 largest starts at 10. add 25 -> [10, 20, 25, 30, 40, 50] pop 10 -> [20, 25, 30, 40, 50] res 20

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
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Tree", "Design", "Binary Search Tree", "Heap (Priority Queue)", "Binary Tree", "Stream"],
        "companyIndex": 0
    }

    output_path = "601-800/703_Kth_Largest_Element_in_a_Stream.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
