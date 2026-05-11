import json
import os

def generate_json():
    problem_id = 406
    title = "Queue Reconstruction by Height"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>406. Queue Reconstruction by Height</h3>
<p>You are given an array of people, <code>people</code>, which are the attributes of some people in a queue (not necessarily in order). Each <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> person of height <code>h<sub>i</sub></code> with exactly <code>k<sub>i</sub></code> other people in front who have a height greater than or equal to <code>h<sub>i</sub></code>.</p>

<p>Reconstruct and return the queue. The returned queue should be formatted as an array <code>queue</code>, where <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> is the attributes of the <code>j<sup>th</sup></code> person in the queue (<code>queue[0]</code> is the person at the front of the queue).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>Output:</strong> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>Explanation:</strong>
Person 0 has height 5 with no one taller or the same height in front.
Person 1 has height 7 with no one taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front (5 and 7).
Person 3 has height 6 with one person taller or the same height in front (7).
Person 4 has height 4 with four persons taller or the same height in front (5, 7, 5, and 6).
Person 5 has height 7 with one person taller or the same height in front (7 from person 1).
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>Output:</strong> [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= people.length &lt;= 2000</code></li>
	<li><code>0 &lt;= h<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k<sub>i</sub> &lt; people.length</code></li>
	<li>It is guaranteed that the queue can be reconstructed.</li>
</ul>"""

    input_format = "An array of `[h, k]`."
    output_format = "Sorted list of `[h, k]`."
    
    constraints = [
        "1 <= people.length <= 2000",
        "It's always possible to reconstruct."
    ]
    
    explanation = """To reconstruct the queue, we can take a **Greedy** approach by sorting and then inserting.

### Key Observation:
- We want to place the **tallest** people first. Why? Because taller people don't care about shorter people in terms of $k$; they only keep track of people same or taller than them.
- If multiple people have the same height, we should process the one with the smaller $k$ first.

### Algorithm Steps:
1. **Sort**: Sort the `people` array in:
   - **Descending** order of height $h$.
   - **Ascending** order of $k$ (for the same height).
2. **Insert**: Iterate through the sorted people:
   - For each person `[h, k]`, insert them into the resulting queue at index `k`.
   - Because we process from tallest to shortest, the existing people in the list are all taller or equal to the current person. Thus, the index $k$ correctly satisfies the condition of having $k$ people taller than them in front.

### Complexity Analysis:
- **Time Complexity**: $O(N^2)$, where $N$ is the number of people. Sorting takes $O(N \log N)$ and inserting $N$ times into a list takes $O(N^2)$ overall in the worst case.
- **Space Complexity**: $O(N)$ to store the output."""
    
    answer = """class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height ascending (negative for descending) and k ascending
        # [7,0], [7,1], [6,1], [5,0]...
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        # Inserting tall people first ensures they stay counted properly
        for p in people:
            queue.insert(p[1], p)
            
        return queue"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:\n        # Your logic here\n        pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        people = json.loads(raw_input)\n        sol = Solution()\n        print(json.dumps(sol.reconstructQueue(people)))",
        "cpp": "class Solution {\npublic:\n    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {\n        // Your logic here\n        return {};\n    }\n};",
        "java": "public class Solution {\n    public int[][] reconstructQueue(int[][] people) {\n        // Your logic here\n        return new int[0][0];\n    }\n}",
        "javascript": "/**\n * @param {number[][]} people\n * @return {number[][]}\n */\nvar reconstructQueue = function(people) {\n    // Your logic here\n};",
        "c": "int** reconstructQueue(int** people, int peopleSize, int* peopleColSize, int* returnSize, int** returnColumnSizes) {\n    // Your logic here\n    return NULL;\n}"
    }

    test_cases = [
        {"input": '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]', "expected_output": "[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]", "is_sample": True},
        {"input": '[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]', "expected_output": "[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]", "is_sample": True},
        {"input": '[[1,0]]', "expected_output": "[[1,0]]", "is_sample": False},
        {"input": '[[1,0],[2,0]]', "expected_output": "[[2,0],[1,0]]", "is_sample": False},
        {"input": '[[1,0],[1,1]]', "expected_output": "[[1,0],[1,1]]", "is_sample": False},
        {"input": '[[5,0],[5,1],[5,2]]', "expected_output": "[[5,0],[5,1],[5,2]]", "is_sample": False},
        {"input": '[[5,2],[5,0],[5,1]]', "expected_output": "[[5,0],[5,1],[5,2]]", "is_sample": False},
        # Stress cases
        {"input": '[[i, 0] for i in range(2000)]', "expected_output": "[[i, 0] for i in range(1999, -1, -1)]", "is_sample": False},
        {"input": '[[0, i] for i in range(2000)]', "expected_output": "[[0, i] for i in range(2000)]", "is_sample": False},
        {"input": '[[10**6, 0]]', "expected_output": "[[1000000, 0]]", "is_sample": False}
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
        "topics": ["Array", "Greedy", "Sorting", "Tree", "Binary Indexed Tree", "Segment Tree"],
        "companyIndex": 1
    }

    output_path = "301-500/406_Queue_Reconstruction_by_Height.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
