import json
import os

def generate_json():
    problem_id = 1166
    title = "Design File System"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>1166. Design File System</h3>
<p>You are asked to design a file system that allows you to create new paths and associate them with different values.</p>

<p>The format of a path is one or more concatenated strings of the form: <code>/</code> followed by one or more lowercase English letters. For example, "<code>/leetcode</code>" and "<code>/leetcode/problems</code>" are valid paths while an empty string <code>""</code> and "<code>/</code>" are not.</p>

<p>Implement the <code>FileSystem</code> class:</p>

<ul>
	<li><code>bool createPath(string path, int value)</code>: Creates a new <code>path</code> and associates a <code>value</code> to it if possible and returns <code>true</code>. Returns <code>false</code> if the path already exists or its parent path does not exist.</li>
	<li><code>int get(string path)</code>: Returns the value associated with <code>path</code> or returns <code>-1</code> if the path doesn't exist.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
<strong>Output:</strong> 
[null,true,1]
<strong>Explanation:</strong> 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
<strong>Output:</strong> 
[null,true,true,2,false,-1]
<strong>Explanation:</strong> 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because parent "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because "/c" doesn't exist.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of calls to the two functions is less than or equal to <code>10<sup>4</sup></code> in total.</li>
	<li><code>2 &lt;= path.length &lt;= 100</code></li>
	<li><code>1 &lt;= value &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "List of operations and their arguments."
    output_format = "List of results corresponding to the operations."
    
    constraints = [
        "Calls <= 10^4",
        "2 <= path.length <= 100",
        "Value <= 10^9"
    ]
    
    explanation = """To design a file system:
1. **Data Structure**: Use a Hash Map (dictionary) to store paths and their associated values. 
   - Keys: The full path string.
   - Values: The associated integer.
2. **createPath(path, value)**:
   - Check if `path` is empty, just "/", or if it already exists in the map. If so, return `false`.
   - Find the parent path by extracting everything before the last `/`.
   - If the parent path (except for the root "") does not exist in the map, return `false`.
   - Otherwise, add `path` to the map and return `true`.
3. **get(path)**:
   - Perform a simple lookup in the map.
4. **Complexity**:
   - Time: O(L) for both functions where L is the path length (for string manipulation and hashing).
   - Space: O(total number of paths * average path length)."""
    
    answer = """class FileSystem:
    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path in self.paths:
            return False
        
        last_slash = path.rfind("/")
        parent = path[:last_slash]
        
        # Parent must exist unless it is the root empty string
        if parent != "" and parent not in self.paths:
            return False
            
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)"""

    boilerplate = {
        "python": "class FileSystem:\n    def __init__(self):\n        pass\n    def createPath(self, path: str, value: int) -> bool:\n        # implementation\n        pass\n    def get(self, path: str) -> int:\n        # implementation\n        pass",
        "cpp": "class FileSystem {\npublic:\n    FileSystem() {}\n    bool createPath(string path, int value) {\n        // implementation\n        return false;\n    }\n    int get(string path) {\n        // implementation\n        return -1;\n    }\n};",
        "java": "import java.util.*;\nclass FileSystem {\n    public FileSystem() {}\n    public boolean createPath(String path, int value) {\n        // implementation\n        return false;\n    }\n    public int get(String path) {\n        // implementation\n        return -1;\n    }\n}",
        "javascript": "/**\n * @constructor\n */\nvar FileSystem = function() {\n    \n};\n/** \n * @param {string} path \n * @param {number} value\n * @return {boolean}\n */\nFileSystem.prototype.createPath = function(path, value) {\n    \n};\n/** \n * @param {string} path\n * @return {number}\n */\nFileSystem.prototype.get = function(path) {\n    \n};"
    }

    test_cases = [
        {"input": '["FileSystem","createPath","get"]\\n[[],["/a",1],["/a"]]', "expected_output": "[null,true,1]", "is_sample": True},
        {"input": '["FileSystem","createPath","createPath","get","createPath","get"]\\n[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]', "expected_output": "[null,true,true,2,false,-1]", "is_sample": True},
        {"input": '["FileSystem","createPath","createPath"]\\n[[],["/a",1],["/a",1]]', "expected_output": "[null,true,false]", "is_sample": False},
        {"input": '["FileSystem","createPath","get"]\\n[[],["/leet",1],["/leetcode"]]', "expected_output": "[null,true,-1]", "is_sample": False},
        {"input": '["FileSystem","createPath","createPath","createPath"]\\n[[],["/a",1],["/a/b",2],["/a/b/c",3]]', "expected_output": "[null,true,true,true]", "is_sample": False},
        {"input": '["FileSystem","get"]\\n[[],["/test"]]', "expected_output": "[null,-1]", "is_sample": False},
        {"input": '["FileSystem","createPath"]\\n[[],["/a/b",1]]', "expected_output": "[null,false]", "is_sample": False}, # parent /a doesn't exist
        {"input": '["FileSystem","createPath","createPath"]\\n[[],["/a",1],["/b",2]]', "expected_output": "[null,true,true]", "is_sample": False},
        # Stress cases
        {"input": '["FileSystem","createPath","get"]\\n[[],["/extreme",99999],["/extreme"]]', "expected_output": "[null,true,99999]", "is_sample": False},
        {"input": '["FileSystem","createPath","get"]\\n[[],["/longlongpathforstresstesting",1],["/longlongpathforstresstesting"]]', "expected_output": "[null,true,1]", "is_sample": False}
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
            "allowed_languages": ["python", "cpp", "java", "javascript"]
        },
        "topics": ["Hash Table", "String", "Design"],
        "companyIndex": 0
    }

    output_path = "1101-1200/1166_Design_File_System.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
