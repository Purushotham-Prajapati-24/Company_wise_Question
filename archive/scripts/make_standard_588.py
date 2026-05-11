import json
import os

def generate_json():
    problem_id = 588
    title = "Design In-Memory File System"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>588. Design In-Memory File System</h3>
<p>Design an in-memory file system that simulates the following functions:</p>

<ul>
	<li><code>ls(path)</code>: 
	<ul>
		<li>If the <code>path</code> is a file path, return a list that only contains this file's name.</li>
		<li>If the <code>path</code> is a directory path, return the list of file and directory names in this directory.</li>
		<li>The output should be in <strong>lexicographical order</strong>.</li>
	</ul>
	</li>
	<li><code>mkdir(path)</code>: Given a directory path that does not exist, create a new directory according to the path. If the intermediate directories in the path do not exist, create them as well.</li>
	<li><code>addContentToFile(filePath, content)</code>: 
	<ul>
		<li>If the <code>filePath</code> does not exist, create the file containing the given <code>content</code>.</li>
		<li>If the <code>filePath</code> already exists, append the given <code>content</code> to the original content.</li>
	</ul>
	</li>
	<li><code>readContentFromFile(filePath)</code>: Return the content in the file at <code>filePath</code>.</li>
</ul>

<p>All paths are absolute paths which begin with <code>'/'</code> and do not end with <code>'/'</code> (unless the path is just <code>"/"</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> 
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
<strong>Output:</strong> 
[null, [], null, null, ["a"], "hello"]
</pre>
"""

    input_format = "A list of strings representing methods to call and a list of lists representing the arguments to pass to each call."
    output_format = "A list of results from each method call."
    
    constraints = [
        "1 <= path.length, filePath.length <= 100",
        "Lowercase English letters only.",
        "Total function calls <= 1000"
    ]
    
    explanation = """To design the In-Memory File System:
1. Use a trie-like structure where each node represents a directory or file.
2. Each node contains a `children` dictionary mapping names to child nodes.
3. Each node also includes a `content` field for files and an `isFile` boolean flag.
4. For `ls`, traverse the tree based on the path strings.
5. For `mkdir`, create all intermediate directories along the path.
6. For `addContentToFile`, create the file node if necessary and append content.
7. For `readContentFromFile`, navigate to the node and return its `content`."""
    
    answer = """class Node:
    def __init__(self):
        self.children = {}
        self.content = ""
        self.isFile = False

class FileSystem:
    def __init__(self):
        self.root = Node()
        
    def traverse(self, path):
        curr = self.root
        if path == "/":
            return curr
        parts = path.split("/")[1:]
        for p in parts:
            if p not in curr.children:
                curr.children[p] = Node()
            curr = curr.children[p]
        return curr

    def ls(self, path):
        curr = self.root
        if path != "/":
            parts = path.split("/")[1:]
            for p in parts:
                curr = curr.children[p]
        if curr.isFile:
            return [path.split("/")[-1]]
        return sorted(list(curr.children.keys()))

    def mkdir(self, path):
        self.traverse(path)

    def addContentToFile(self, filePath, content):
        curr = self.traverse(filePath)
        curr.isFile = True
        curr.content += content

    def readContentFromFile(self, filePath):
        curr = self.traverse(filePath)
        return curr.content"""

    boilerplate = {
        "python": "class FileSystem:\\n    def __init__(self):\\n        pass",
        "cpp": "class FileSystem { public: vector<string> ls(string path) {} void mkdir(string path) {} void addContentToFile(string filePath, string content) {} string readContentFromFile(string filePath) {} };",
        "java": "class FileSystem { public FileSystem() {} public List<String> ls(String path) {} public void mkdir(String path) {} public void addContentToFile(String filePath, String content) {} public String readContentFromFile(String filePath) {} }",
        "javascript": "var FileSystem = function() {};",
        "c": "typedef struct { } FileSystem;"
    }

    test_cases = [
        {"input": "['FileSystem', 'ls', 'mkdir', 'addContentToFile', 'ls', 'readContentFromFile']\\n[[], ['/'], ['/a/b/c'], ['/a/b/c/d', 'hello'], ['/'], ['/a/b/c/d']]", "expected_output": "[null, [], null, null, ['a'], 'hello']", "is_sample": True},
        {"input": "['FileSystem', 'mkdir', 'ls', 'ls']\\n[[], ['/abc'], ['/'], ['/abc']]", "expected_output": "[null, null, ['abc'], []]", "is_sample": True},
        {"input": "['FileSystem', 'ls']\\n[[], ['/']]", "expected_output": "[null, []]", "is_sample": False},
        {"input": "['FileSystem', 'mkdir', 'mkdir', 'ls']\\n[[], ['/a'], ['/b'], ['/']]", "expected_output": "[null, null, null, ['a', 'b']]", "is_sample": False},
        {"input": "['FileSystem', 'addContentToFile', 'readContentFromFile']\\n[[], ['/test', 'content'], ['/test']]", "expected_output": "[null, null, 'content']", "is_sample": False},
        {"input": "['FileSystem', 'addContentToFile', 'addContentToFile', 'readContentFromFile']\\n[[], ['/test', 'hello'], ['/test', 'world'], ['/test']]", "expected_output": "[null, null, null, 'helloworld']", "is_sample": False},
        {"input": "['FileSystem', 'mkdir', 'mkdir', 'ls']\\n[[], ['/dir1/dir2'], ['/dir1/dir3'], ['/dir1']]", "expected_output": "[null, null, null, ['dir2', 'dir3']]", "is_sample": False},
        {"input": str(["FileSystem"] + ["mkdir"]*100 + ["ls"]) + "\\n" + str([[]] + [["/p" + str(i)] for i in range(100)] + [["/"]]), "expected_output": "[null" + ", null"*100 + ", " + str(sorted(["p"+str(i) for i in range(100)])) + "]", "is_sample": False},
        {"input": "['FileSystem', 'addContentToFile', 'addContentToFile', 'readContentFromFile']\\n[[], ['/long', 'a'*50], ['/long', 'b'*50], ['/long']]", "expected_output": "[null, null, null, '" + "a"*50 + "b"*50 + "']", "is_sample": False},
        {"input": "['FileSystem', 'mkdir', 'addContentToFile', 'ls']\\n[[], ['/a/b/c'], ['/a/b/c/file', 'txt'], ['/a/b/c']]", "expected_output": "[null, null, null, ['file']]", "is_sample": False}
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
        "topics": ["Design", "Trie"],
        "companyIndex": 0
    }

    output_path = "401-600/588_Design_In-Memory_File_System.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
