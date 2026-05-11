import json
import os

def generate_json():
    problem_id = 388
    title = "Longest Absolute File Path"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>388. Longest Absolute File Path</h3>
<p>Suppose we have a file system that stores files and directories. An example of a file system as a string is <code>"dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext"</code>. The depth of a file or directory is indicated by the number of tab characters <code>\\t</code>.</p>

<p>The directory <code>dir</code> contains an empty sub-directory <code>subdir1</code> and a sub-directory <code>subdir2</code> containing a file <code>file.ext</code>.</p>

<p>The string <code>"dir\\n\\tsubdir1\\n\\t\\tsubdir11\\n\\tsubdir2\\n\\t\\tsubdir21\\n\\t\\t\\tfile.ext"</code> represents:</p>
<pre>
dir
&nbsp; &nbsp; subdir1
&nbsp; &nbsp; &nbsp; &nbsp; subdir11
&nbsp; &nbsp; subdir2
&nbsp; &nbsp; &nbsp; &nbsp; subdir21
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; file.ext
</pre>

<p>We are interested in finding the longest (number of characters) absolute path to a <b>file</b> within our file system. For example, in the second case, the longest absolute path is <code>"dir/subdir2/subdir21/file.ext"</code>, and its length is <code>32</code> (note that the double quotes are not part of the path).</p>

<p>Return <em>the length of the longest absolute path to a <b>file</b> in the abstracted file system</em>. If there is no file in the system, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/dir1.jpg" style="width: 401px; height: 151px;" />
<pre><strong>Input:</strong> input = "dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext"
<strong>Output:</strong> 20
<strong>Explanation:</strong> We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/dir2.jpg" style="width: 641px; height: 322px;" />
<pre><strong>Input:</strong> input = "dir\\n\\tsubdir1\\n\\t\\tsubdir11\\n\\tsubdir2\\n\\t\\tsubdir21\\n\\t\\t\\tfile.ext"
<strong>Output:</strong> 32
<strong>Explanation:</strong> We have two files:
"dir/subdir1/subdir11" (not a file because no dot)
"dir/subdir2/subdir21/file.ext" of length 32.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> input = "a"
<strong>Output:</strong> 0
<strong>Explanation:</strong> We do not have any files, just a directory.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= input.length &lt;= 10<sup>4</sup></code></li>
	<li><code>input</code> may contain lowercase or uppercase English letters, a new line character <code>'\\n'</code>, a tab character <code>'\\t'</code>, a dot <code>'.'</code>, a space <code>' '</code>, and digits.</li>
</ul>"""

    input_format = "A string `input` representing a file system."
    output_format = "Length of the longest absolute path to a file."
    
    constraints = [
        "1 <= input.length <= 10,000",
        "A file must contain a dot (.).",
        "Depth is determined by the number of tab characters."
    ]
    
    explanation = """To find the longest absolute path to a file, we can process each line (directory or file) and keep track of the current path length at each depth.

### Key Observation:
- This is essentially a "Depth-First Search" problem on a tree representation of the file system.
- We can track the cumulative length of directories in an array or hash map: `depth_lengths[d]` stores the length of the string from the root up to the directory at depth `d`.

### Algorithm Steps:
1. **Split the Input**: Split the string by `\\n` to get each line.
2. **Track Path Lengths**: Initialize `depth_lengths = {0: 0}`.
3. **Iterate through Lines**:
   - For each line, count the number of tabs `\\t` to determine the `depth`.
   - Calculate the length of the actual name (stripping the leading tabs).
   - If it's a **directory** (no dot):
     - Store its path length: `depth_lengths[depth + 1] = depth_lengths[depth] + len(name) + 1` (the `+1` is for the `/`).
   - If it's a **file** (contains a dot):
     - Calculate full path length: `depth_lengths[depth] + len(name)`.
     - Update global maximum.
4. **Return**: The final maximum length.

### Complexity Analysis:
- **Time Complexity**: $O(N)$, where $N$ is the length of the input. We process each character once.
- **Space Complexity**: $O(D)$, where $D$ is the maximum depth of the file system (number of levels)."""
    
    answer = """class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        depth_len = {0: 0}
        
        for line in input.split('\\n'):
            name = line.lstrip('\\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                max_len = max(max_len, depth_len[depth] + len(name))
            else:
                depth_len[depth + 1] = depth_len[depth] + len(name) + 1
                
        return max_len"""

    boilerplate = {
        "python": "import sys\nimport json\n\nclass Solution:\n    def lengthLongestPath(self, input: str) -> int:\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    if data:\n        if (data.startswith('\"') and data.endswith('\"')) or (data.startswith(\"'\") and data.endswith(\"'\")):\n            try:\n                data = json.loads(data)\n            except:\n                data = data[1:-1]\n        data = data.replace('\\\\n', '\\n').replace('\\\\t', '\\t')\n        sol = Solution()\n        print(json.dumps(sol.lengthLongestPath(data)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <algorithm>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    int lengthLongestPath(string input) {\n        // User logic here\n        return 0;\n    }\n};\n\nint main() {\n    string raw, line;\n    while (getline(cin, line)) {\n        raw += line + (cin.eof() ? \"\" : \"\\n\");\n    }\n    string input = \"\";\n    for (size_t i = 0; i < raw.length(); ++i) {\n        if (raw[i] == '\\\\' && i + 1 < raw.length()) {\n            if (raw[i+1] == 'n') { input += '\\n'; i++; }\n            else if (raw[i+1] == 't') { input += '\\t'; i++; }\n            else input += raw[i];\n        } else {\n            input += raw[i];\n        }\n    }\n    if (input.size() >= 2 && input.front() == '\"' && input.back() == '\"') {\n        input = input.substr(1, input.size() - 2);\n    }\n    Solution sol;\n    cout << sol.lengthLongestPath(input) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public int lengthLongestPath(String input) {\n        // User logic here\n        return 0;\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) {\n            sb.append(sc.nextLine());\n            if (sc.hasNextLine()) sb.append(\"\\n\");\n        }\n        String input = sb.toString();\n        input = input.replace(\"\\\\\\\\n\", \"\\n\").replace(\"\\\\\\\\t\", \"\\t\");\n        if (input.startsWith(\"\\\"\") && input.endsWith(\"\\\"\")) {\n            input = input.substring(1, input.length() - 1);\n        }\n        Solution sol = new Solution();\n        System.out.println(sol.lengthLongestPath(input));\n    }\n}",
        "javascript": "var lengthLongestPath = function(input) {\n    // User logic here\n};\n\nconst fs = require('fs');\nlet inputData = fs.readFileSync(0, 'utf8').trim();\nif (inputData) {\n    if (inputData.startsWith('\"') && inputData.endsWith('\"')) {\n        try {\n            inputData = JSON.parse(inputData);\n        } catch(e) {\n            inputData = inputData.slice(1, -1);\n        }\n    }\n    inputData = inputData.replace(/\\\\n/g, '\\n').replace(/\\\\t/g, '\\t');\n    console.log(JSON.stringify(lengthLongestPath(inputData)));\n}",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint lengthLongestPath(char* input) {\n    // User logic here\n    return 0;\n}\n\nint main() {\n    char *input = malloc(100005 * sizeof(char));\n    char buf[1024];\n    input[0] = '\\0';\n    while (fgets(buf, 1024, stdin)) {\n        strcat(input, buf);\n    }\n    int len = strlen(input);\n    if (len > 0 && input[len-1] == '\\n') input[len-1] = '\\0';\n    printf(\"%d\\n\", lengthLongestPath(input));\n    free(input);\n    return 0;\n}"
    }

    test_cases = [
        {"input": "dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext", "expected_output": "20", "is_sample": True},
        {"input": "dir\\n\\tsubdir1\\n\\t\\tsubdir11\\n\\tsubdir2\\n\\t\\tsubdir21\\n\\t\\t\\tfile.ext", "expected_output": "32", "is_sample": True},
        # 5 Diverse
        {"input": "a", "expected_output": "0", "is_sample": False},
        {"input": "file.ext", "expected_output": "8", "is_sample": False},
        {"input": "a\\n\\tb.ext\\n\\tc.ext", "expected_output": "7", "is_sample": False},
        {"input": "dir\\n\\tsubdir1\\n\\t\\tfile1.ext\\n\\tsubdir2\\n\\t\\tfile2.ext", "expected_output": "20", "is_sample": False},
        {"input": "dir\\n\\t    file.txt", "expected_output": "16", "is_sample": False},
        # 3 Stress
        {"input": "a" * 100 + "\\n" + "\\t" * 1 + "file.ext", "expected_output": "109", "is_sample": False},
        {"input": "dir" + "\\n" + "\\t" * 50 + "file.ext", "expected_output": "62", "is_sample": False},
        {"input": "dir\\n\\ta.ext\\n\\tb.ext\\n\\tc.ext\\n\\tsubdir\\n\\t\\tlongfile.extension", "expected_output": "25", "is_sample": False}
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
        "topics": ["String", "Stack", "Tree", "Depth-First Search"],
        "companyIndex": 1
    }

    output_path = "301-500/388_Longest_Absolute_File_Path.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
