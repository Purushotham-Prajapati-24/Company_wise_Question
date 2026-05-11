import json
import os

def generate_json():
    problem_id = 1046
    title = "Last Stone Weight"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>1046. Last Stone Weight</h3>
<p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i<sup>th</sup></code> stone.</p>

<p>We are playing a game with the stones. On each turn, we choose the <strong>heaviest two stones</strong> and smash them together. Suppose the heaviest two stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>. The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are destroyed.</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has a new weight <code>y - x</code>.</li>
</ul>

<p>At the end of the game, there is <strong>at most one</strong> stone left.</p>

<p>Return <em>the weight of the last remaining stone</em>. If there are no stones left, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 1000</code></li>
</ul>"""

    input_format = "A single line containing space-separated integers for the stones weights."
    output_format = "An integer representing the weight of the last remaining stone, or 0."
    
    constraints = [
        "1 <= stones.length <= 30",
        "1 <= stones[i] <= 1000",
        "O(N log N) time complexity.",
        "O(N) space complexity (for heap)."
    ]
    
    explanation = """To simulate the stone smashing game efficiently:
1. **Max-Heap**:
   - We always need to extract the two heaviest stones. A Max-Heap is the perfect data structure for this.
   - In languages like Python, we use the `heapq` module (which is a min-heap) and store numbers as negative values to simulate a max-heap.
2. **Game Loop**:
   - While there are at least two stones in the heap:
     - Extract the two heaviest stones `y` and `x` (where `y >= x`).
     - If `y > x`, push the difference `y - x` back into the heap.
3. **Result**:
   - If the heap is not empty, return the remaining absolute value.
   - Otherwise, return `0`.
4. **Complexity**:
   - Time Complexity: O(N log N) – each insertion and extraction takes O(log N).
   - Space Complexity: O(N) to store the stones in the heap."""
    
    answer = """import heapq
def lastStoneWeight(stones: list[int]) -> int:
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)
        if y > x:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0"""

    boilerplate = {
        "python": "import sys\nimport heapq\n\ndef lastStoneWeight(stones):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        stones = list(map(int, line.split()))\n        print(lastStoneWeight(stones))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <queue>\n\nusing namespace std;\n\nint lastStoneWeight(vector<int>& stones) {\n    // User logic\n    return 0;\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int lastStoneWeight(int[] stones) {\n        // User logic\n        return 0;\n    }\n}",
        "javascript": "function lastStoneWeight(stones) {\n    // User logic\n}",
        "c": "int lastStoneWeight(int* stones, int stonesSize) {\n    // User logic\n    return 0;\n}"
    }

    test_cases = [
        {"input": "2 7 4 1 8 1", "expected_output": "1", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": True},
        {"input": "2 2", "expected_output": "0", "is_sample": True},
        {"input": "10 4 2 1", "expected_output": "3", "is_sample": False},
        {"input": "1 1 1", "expected_output": "1", "is_sample": False},
        {"input": "1 1 1 1", "expected_output": "0", "is_sample": False},
        {"input": "1000 1000 1000", "expected_output": "1000", "is_sample": False},
        # Stress/Diverse cases
        {"input": " ".join(["1000"] * 30), "expected_output": "0", "is_sample": False},
        {"input": " ".join(["999", "1000"] * 15), "expected_output": "0", "is_sample": False}, # Correction: 15 pairs of (1000-999)=1. result is 15 ones. smash 7 pairs -> 1 left. So 1. Wait. logic: [1]*15. 14 destroyed -> 1 left.
        {"input": " ".join([str(i) for i in range(1, 31)]), "expected_output": "1", "is_sample": False}
    ]
    # Small test on cases
    # 30, 29 -> 1. 28, 27 -> 1. ... 2, 1 -> 1. => 15 ones. result 1.
    test_cases[8]["expected_output"] = "1"
    test_cases[9]["expected_output"] = "1" # (30-29)=1, (28-27)=1... (2-1)=1. => 15 ones. 1.

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
        "companyIndex": 0
    }

    output_path = "1001-1200/1046_Last_Stone_Weight.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
