import json
import os

def generate_json():
    problem_id = 705
    title = "Design HashSet"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>705. Design HashSet</h3>
<p>Design a HashSet without using any built-in hash table libraries.</p>

<p>Implement <code>MyHashSet</code> class:</p>

<ul>
	<li><code>void add(key)</code> Inserts the value <code>key</code> into the HashSet.</li>
	<li><code>bool contains(key)</code> Returns whether the value <code>key</code> exists in the HashSet or not.</li>
	<li><code>void remove(key)</code> Removes the value <code>key</code> in the HashSet. If <code>key</code> does not exist in the HashSet, do nothing.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>Output:</strong>
[null, null, null, true, false, null, true, null, false]

<strong>Explanation:</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>, <code>remove</code>, and <code>contains</code>.</li>
</ul>"""

    input_format = "Multiple lines: Each line is one of 'add x', 'remove x', or 'contains x'."
    output_format = "'true' or 'false' for 'contains' operations. Nothing for 'add' or 'remove'."
    
    constraints = [
        "0 <= key <= 10^6",
        "No built-in hash table libraries.",
        "O(1) average time complexity.",
        "O(K + N) space complexity (where K is buckets)."
    ]
    
    explanation = """To design a HashSet from scratch:
1. **The Core Data Structure (Custom Hash Table)**:
   - Use a pre-allocated array of "buckets" to handle collisions. A prime number for the number of buckets (like 769 or 1009) helps distribute keys more evenly.
2. **Collision Strategy (Chaining)**:
   - Each bucket is a structure (like a list) containing keys that hash to the same bucket index.
   - `index = key % number_of_buckets`.
3. **Implementation**:
   - `add(key)`: If `key` is not in `buckets[index]`, Append it.
   - `remove(key)`: If `key` is in `buckets[index]`, Delete it.
   - `contains(key)`: Check if `key` exists in `buckets[index]`.
4. **Complexity**:
   - Time Complexity: O(1) average per operation (assuming good distribution).
   - Space Complexity: O(K + N) where K is the number of buckets and N is the unique keys added."""
    
    answer = """class MyHashSet:
    def __init__(self):
        self.num_buckets = 769
        self.buckets = [[] for _ in range(self.num_buckets)]
        
    def _hash(self, key):
        return key % self.num_buckets

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.buckets[idx]"""

    boilerplate = {
        "python": "import sys\n\nclass MyHashSet:\n    def __init__(self):\n        # User logic here\n        pass\n    def add(self, key):\n        pass\n    def remove(self, key):\n        pass\n    def contains(self, key):\n        return False\n\nif __name__ == '__main__':\n    # Parser and calling MyHashSet\n    pass",
        "cpp": "#include <iostream>\n#include <vector>\n#include <list>\n\nusing namespace std;\n\nclass MyHashSet {\npublic:\n    MyHashSet();\n    void add(int key);\n    void remove(int key);\n    bool contains(int key);\n};",
        "java": "import java.util.*;\n\npublic class MyHashSet {\n    public void add(int key) {\n        // User logic\n    }\n    public void remove(int key) {\n        // User logic\n    }\n    public boolean contains(int key) {\n        // User logic\n        return false;\n    }\n}",
        "javascript": "var MyHashSet = function() {\n    // User logic\n};\n\nMyHashSet.prototype.add = function(key) {\n    // User logic\n};\n\nMyHashSet.prototype.remove = function(key) {\n    // User logic\n};\n\nMyHashSet.prototype.contains = function(key) {\n    // User logic\n};",
        "c": "typedef struct {\n    // User logic\n} MyHashSet;\n\nMyHashSet* myHashSetCreate();\nvoid myHashSetAdd(MyHashSet* obj, int key);\nvoid myHashSetRemove(MyHashSet* obj, int key);\nbool myHashSetContains(MyHashSet* obj, int key);"
    }

    test_cases = [
        {"input": "add 1\\nadd 2\\ncontains 1\\ncontains 3\\nadd 2\\ncontains 2\\nremove 2\\ncontains 2", "expected_output": "true\\nfalse\\ntrue\\nfalse", "is_sample": True},
        {"input": "contains 1\\nadd 1\\ncontains 1\\nremove 1\\ncontains 1", "expected_output": "false\\ntrue\\nfalse", "is_sample": True},
        {"input": "add 1000000\\ncontains 1000000\\nremove 1000000\\ncontains 1000000", "expected_output": "true\\nfalse", "is_sample": False},
        {"input": "add 0\\nadd 769\\nadd 1538\\ncontains 0\\ncontains 769\\ncontains 1538\\nremove 769\\ncontains 769", "expected_output": "true\\ntrue\\ntrue\\nfalse", "is_sample": False},
        {"input": "contains 500\\nremove 500\\ncontains 500", "expected_output": "false\\nfalse", "is_sample": False},
        {"input": "\\n".join([f"add {i}" for i in range(10)]) + "\\n" + "\\n".join([f"contains {i}" for i in range(11)]), "expected_output": "true\\ntrue\\ntrue\\ntrue\\ntrue\\ntrue\\ntrue\\ntrue\\ntrue\\ntrue\\nfalse", "is_sample": False},
        {"input": "add 1\\nadd 1\\ncontains 1", "expected_output": "true", "is_sample": False},
        {"input": "add 10\\nremove 20\\ncontains 10", "expected_output": "true", "is_sample": False},
        # Stress cases
        {"input": "\\n".join([f"add {i}" for i in range(1000)]), "expected_output": "", "is_sample": False},
        {"input": "\\n".join([f"add 10" for i in range(500)]) + "\\ncontains 10", "expected_output": "true", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Design", "Linked List"],
        "companyIndex": 0
    }

    output_path = "601-800/705_Design_HashSet.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
