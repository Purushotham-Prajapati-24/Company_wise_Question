import json
import os

def generate_json():
    problem_id = 677
    title = "Map Sum Pairs"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>677. Map Sum Pairs</h3>
<p>Design a map that allows you to do the following:</p>

<ul>
	<li>Maps a string key to a given value.</li>
	<li>Returns the sum of the values that have a key with a prefix equal to a given string.</li>
</ul>

<p>Implement the <code>MapSum</code> class:</p>
<ul>
	<li><code>MapSum()</code>: Initializes the object.</li>
	<li><code>void insert(string key, int val)</code>: Inserts the <code>key-val</code> pair into the map. If the <code>key</code> already existed, the original <code>val</code> will be overridden to the new one.</li>
	<li><code>int sum(string prefix)</code>: Returns the sum of all the pairs' value whose <code>key</code> starts with the <code>prefix</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
<strong>Output:</strong>
[null, null, 3, null, 5]

<strong>Explanation:</strong>
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= key.length, prefix.length &lt;= 50</code></li>
	<li><code>key</code> and <code>prefix</code> consist of lowercase English letters.</li>
	<li><code>1 &lt;= val &lt;= 1000</code></li>
	<li>At most <code>50</code> calls to <code>insert</code> and <code>sum</code>.</li>
</ul>"""

    input_format = "Initialization, insert keys and values, and sum prefixes."
    output_format = "Integers for each sum call."
    
    constraints = [
        "key.length, prefix.length <= 50",
        "At most 50 calls to insert and sum."
    ]
    
    explanation = """To implement Map Sum Pairs:
1. **Tree Representation (Trie)**:
   - Use a Trie to store the words.
   - Each node in the Trie can store the total `sum` of values of all keys passing through it.
2. **Handling Overwrites**:
   - To correctly update the Trie sums when a key already exists, use a separate hash map `records` to store the original value for each key.
   - When `insert(key, val)` is called:
     - Determine the `delta = val - records.get(key, 0)`.
     - Update `records[key] = val`.
     - Traverse the Trie for `key`, adding `delta` to the `sum` field of each node along the path.
3. **Calculating `sum(prefix)`**:
   - Traverse the Trie using the `prefix`.
   - If the prefix doesn't exist, return 0.
   - If it exists, return the `sum` stored at the node corresponding to the last character of the prefix.
4. **Complexity Analysis**:
   - Time: O(L) for both `insert` and `sum`, where L is the length of the string.
   - Space: O(Characters in all keys) to store the Trie."""
    
    answer = """class TrieNode:
    def __init__(self):
        self.children = {}
        self.val_sum = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.records = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.records.get(key, 0)
        self.records[key] = val
        
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.val_sum += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.val_sum"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass MapSum:\n    def __init__(self):\n        pass\n    def insert(self, key, val):\n        pass\n    def sum(self, prefix):\n        pass\n\nif __name__ == '__main__':\n    # Process commands\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\nusing namespace std;\n\nclass MapSum {\npublic:\n    MapSum() {\n    }\n    void insert(string key, int val) {\n    }\n    int sum(string prefix) {\n        return 0;\n    }\n};",
        "java": "import java.util.*;\n\npublic class MapSum {\n    public MapSum() {\n    }\n    public void insert(String key, int val) {\n    }\n    public int sum(String prefix) {\n        return 0;\n    }\n}",
        "javascript": "/**\n * @constructor\n */\nvar MapSum = function() {\n};\n\n/**\n * @param {string} key\n * @param {number} val\n * @return {void}\n */\nMapSum.prototype.insert = function(key, val) {\n};\n\n/**\n * @param {string} prefix\n * @return {number}\n */\nMapSum.prototype.sum = function(prefix) {\n};",
        "c": "typedef struct {\n    // User logic\n} MapSum;\n\nMapSum* mapSumCreate() {\n}\n\nvoid mapSumInsert(MapSum* obj, char * key, int val) {\n}\n\nint mapSumSum(MapSum* obj, char * prefix) {\n}"
    }

    test_cases = [
        {"input": '["MapSum", "insert", "sum", "insert", "sum"]\\n[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]', "expected_output": "[null, null, 3, null, 5]", "is_sample": True},
        {"input": '["MapSum", "insert", "sum", "insert", "sum"]\\n[[], ["apple", 3], ["apple"], ["apple", 5], ["apple"]]', "expected_output": "[null, null, 3, null, 5]", "is_sample": False},
        {"input": '["MapSum", "insert", "sum"]\\n[[], ["apple", 3], ["banana"]]', "expected_output": "[null, null, 0]", "is_sample": False},
        {"input": '["MapSum", "insert", "sum", "sum"]\\n[[], ["abc", 3], ["a"], ["ab"]]', "expected_output": "[null, null, 3, 3]", "is_sample": False},
        {"input": '["MapSum", "insert", "insert", "sum"]\\n[[], ["a", 10], ["aa", 20], ["a"]]', "expected_output": "[null, null, null, 30]", "is_sample": False},
        {"input": '["MapSum", "insert", "sum"]\\n[[], ["hello", 1], ["hello"]]', "expected_output": "[null, null, 1]", "is_sample": False},
        # Stress cases
        {"input": '["MapSum"] + ["insert" for _ in range(50)]', "expected_output": "...", "is_sample": False},
        {"input": '["MapSum", "insert", "sum"]\\n[[], ["a"*50, 1000], ["a"*50]]', "expected_output": "[null, null, 1000]", "is_sample": False},
        {"input": '["MapSum", "insert", "sum"]\\n[[], ["z", 10], ["a"]]', "expected_output": "[null, null, 0]", "is_sample": False}
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
        "topics": ["Hash Table", "String", "Design", "Trie"],
        "companyIndex": 0
    }

    output_path = "601-800/677_Map_Sum_Pairs.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
