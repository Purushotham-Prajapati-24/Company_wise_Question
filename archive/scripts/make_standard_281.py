import json
import os

def generate_json():
    problem_id = 281
    title = "Zigzag Iterator"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>281. Zigzag Iterator</h3>
<p>Given two vectors of integers <code>v1</code> and <code>v2</code>, implement an iterator to return their elements alternately.</p>

<p>Implement the <code>ZigzagIterator</code> class:</p>
<ul>
	<li><code>ZigzagIterator(List[int] v1, List[int] v2)</code> initializes the object with the two vectors <code>v1</code> and <code>v2</code>.</li>
	<li><code>boolean hasNext()</code> returns <code>true</code> if the iterator still has elements, and <code>false</code> otherwise.</li>
	<li><code>int next()</code> returns the next element of the zigzag iterator and moves the pointer to the next element.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> v1 = [1,2], v2 = [3,4,5,6]
<strong>Output:</strong> [1,3,2,4,5,6]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> v1 = [1], v2 = []
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> v1 = [], v2 = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= v1.length, v2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= v1.length + v2.length &lt;= 2000</code></li>
	<li><code>-10<sup>9</sup> &lt;= v1[i], v2[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if you are given <code>k</code> vectors? How well can your code be extended to such a case?</p>"""

    input_format = "Two stringified arrays of integers `v1` and `v2`."
    output_format = "A stringified array containing the elements in zigzag order."
    
    constraints = [
        "0 <= v1.length, v2.length <= 1,000",
        "1 <= total length <= 2,000",
        "-10^9 <= value <= 10^9"
    ]
    
    explanation = """To implement an iterator that returns elements in a zigzag (alternating) order:
1. **Queue of Iterators**: Use a collection (like `collections.deque`) to store pointers (iterators) for each non-empty vector.
2. **Zigzag Logic**:
   - `ZigzagIterator(v1, v2)`: If `v1` is not empty, add its iterator (or a pair `[vector, current_index]`) to the queue. Same for `v2`.
   - `next()`:
     - Pop the first iterator from the queue.
     - Retrieve the next value from that iterator.
     - increment the index for that vector. If there are still more elements in that vector, add its updated state back to the end of the queue.
     - Return the retrieved value.
   - `hasNext()`: Returns true if the queue is not empty.
3. **Follow-up (k vectors)**: This queue-based design naturally extends to `k` vectors without any change in the logic of `next()` and `hasNext()`.
4. **Complexity Analysis**:
   - Time: O(1) for each `next()` and `hasNext()` call.
   - Space: O(k) where k is the number of vectors, to store the pointers/queue."""
    
    answer = """import collections

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        # 1. Use a queue of lists (each list contains a pointer to the vector and its current index)
        self.queue = collections.deque()
        if v1:
            self.queue.append([v1, 0])
        if v2:
            self.queue.append([v2, 0])

    def next(self) -> int:
        # 2. Pop the front vector state
        vec, idx = self.queue.popleft()
        val = vec[idx]
        
        # 3. Add back to queue if it still has elements
        if idx + 1 < len(vec):
            self.queue.append([vec, idx + 1])
            
        return val

    def hasNext(self) -> bool:
        # 4. Returns true as long as there's something in the queue
        return len(self.queue) > 0"""

    boilerplate = {
        "python": "import sys\nimport json\nimport collections\n\nclass ZigzagIterator:\n    def __init__(self, v1, v2):\n        # User logic here\n        pass\n    def next(self) -> int:\n        # User logic here\n        pass\n    def hasNext(self) -> bool:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    # Boilerplate to handle input and call iterator methods\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\nusing namespace std;\n\nclass ZigzagIterator {\npublic:\n    ZigzagIterator(vector<int>& v1, vector<int>& v2) {\n        // User logic here\n    }\n\n    int next() {\n        // User logic here\n        return 0;\n    }\n\n    bool hasNext() {\n        // User logic here\n        return false;\n    }\n};",
        "java": "import java.util.*;\n\npublic class ZigzagIterator {\n    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {\n        // User logic here\n    }\n\n    public int next() {\n        // User logic here\n        return 0;\n    }\n\n    public boolean hasNext() {\n        // User logic here\n        return false;\n    }\n}",
        "javascript": "/**\n * @constructor\n * @param {Integer[]} v1\n * @param {Integer[]} v2\n */\nvar ZigzagIterator = function ZigzagIterator(v1, v2) {\n    // User logic here\n};\n\n/**\n * @return {boolean}\n */\nZigzagIterator.prototype.hasNext = function hasNext() {\n    // User logic here\n};\n\n/**\n * @return {integer}\n */\nZigzagIterator.prototype.next = function next() {\n    // User logic here\n};",
        "c": "struct ZigzagIterator {\n    // User logic here\n};\n\nstruct ZigzagIterator* zigzagIteratorCreate(int* v1, int v1Size, int* v2, int v2Size) {\n    // User logic here\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "[1,2]\\n[3,4,5,6]", "expected_output": "[1,3,2,4,5,6]", "is_sample": True},
        {"input": "[1]\\n[]", "expected_output": "[1]", "is_sample": True},
        {"input": "[]\\n[1]", "expected_output": "[1]", "is_sample": True},
        {"input": "[]\\n[]", "expected_output": "[]", "is_sample": False},
        {"input": "[1,2,3,4,5,6]\\n[1,2]", "expected_output": "[1,1,2,2,3,4,5,6]", "is_sample": False},
        {"input": "[1,3,5]\\n[2,4,6]", "expected_output": "[1,2,3,4,5,6]", "is_sample": False},
        {"input": "[1,3,5]\\n[2,4]", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        # Stress cases
        {"input": "[" + ",".join([str(i) for i in range(1000)]) + "]\\n[" + ",".join([str(i) for i in range(1000)]) + "]", "expected_output": "...", "is_sample": False},
        {"input": "[" + ",".join(["1"]*1000) + "]\\n[2]", "expected_output": "...", "is_sample": False},
        {"input": "[1]\\n[" + ",".join(["2"]*1000) + "]", "expected_output": "...", "is_sample": False}
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
        "topics": ["Array", "Design", "Queue", "Iterator"],
        "companyIndex": 0
    }

    output_path = "201-400/281_Zigzag_Iterator.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
