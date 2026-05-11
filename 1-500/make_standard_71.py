import json
import os

def generate_json():
    problem_id = 71
    title = "Simplify Path"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>71. Simplify Path</h3>
<p>Given an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.</p>

<p>In Unix-style file system rules:</p>

<ul>
	<li>A single period <code>'.'</code> refers to the current directory.</li>
	<li>A double period <code>'..'</code> refers to the previous directory (up one level).</li>
	<li>Any multiple consecutive slashes such as <code>'//'</code> and <code>'///'</code> are treated as a single slash <code>'/'</code>.</li>
	<li>Any other sequence of periods (e.g., <code>'...'</code>) is treated as a file/directory name.</li>
</ul>

<p>The <strong>simplified canonical path</strong> should adhere to the following rules:</p>

<ul>
	<li>The path must start with a single slash <code>'/'</code>.</li>
	<li>Directories within the path must be separated by exactly one slash <code>'/'</code>.</li>
	<li>The path must not end with a trailing slash, unless it is the root directory.</li>
	<li>The path must not have any <code>'.'</code> or <code>'..'</code> used to denote current or parent directories.</li>
</ul>

<p>Return the <strong>simplified canonical path</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> path = "/home/"
<strong>Output:</strong> "/home"
<strong>Explanation:</strong> Note that there is no trailing slash after the last directory name.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> path = "/../"
<strong>Output:</strong> "/"
<strong>Explanation:</strong> Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> path = "/home//foo/"
<strong>Output:</strong> "/home/foo"
<strong>Explanation:</strong> In the canonical path, multiple consecutive slashes are replaced by a single one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 3000</code></li>
	<li><code>path</code> consists of English letters, digits, period <code>'.'</code>, slash <code>'/'</code> or underscore <code>'_'</code>.</li>
	<li><code>path</code> is a valid absolute Unix path.</li>
</ul>"""

    input_format = "A single string 'path' representing an absolute Unix-style path."
    output_format = "A string representing the simplified canonical path."
    
    constraints = [
        "1 <= path.length <= 3000",
        "path consists of English letters, digits, '.', '/', or '_'.",
        "path starts with '/' and is a valid absolute path."
    ]
    
    explanation = """To simplify a Unix-style absolute path:
1. **Split the Path**: Use the slash (`/`) as a delimiter to split the path into individual components.
2. **Process Components using a Stack**: Iterate through each component:
   - If the component is empty (due to multiple slashes) or a single period (`.`), ignore it.
   - If the component is a double period (`..`), it means move up one directory. Pop from the stack if it's not empty (root shouldn't go further up).
   - For any other component (file or directory names like `home`, `foo`, `...`), push it onto the stack.
3. **Reconstruct the Path**: Join the components in the stack with a single slash (`/`) and prepend a leading slash.
4. **Complexity**:
   - Time Complexity: O(N), where N is the length of the path string.
   - Space Complexity: O(N) to store the components in the stack."""
    
    answer = """def simplifyPath(path):
    # Split by slash and initialize stack
    components = path.split('/')
    stack = []
    
    for part in components:
        if part == '..':
            # Go up one level if possible
            if stack:
                stack.pop()
        elif part == '.' or not part:
            # Current directory or empty part (from multiple slashes), skip
            continue
        else:
            # Directory or file name, add to stack
            stack.append(part)
            
    # Combine everything back into a canonical path
    return \"/\" + \"/\".join(stack)"""

    # STRICT boilerplate style from make_standard_120.py / 13.py
    boilerplate = {
        "python": "import sys, re\n\ndef simplifyPath(path):\n    # User Logic Here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip()\n    match = re.search(r'\"(.*?)\"', data)\n    path = match.group(1) if match else data.split('=')[-1].strip().strip('\"')\n    print(simplifyPath(path))",
        "cpp": "#include <iostream>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string simplifyPath(string path) {\n        // User Logic Here\n        return \"\";\n    }\n};\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    regex rgx(R\"(\"(.*?)\")\");\n    smatch match;\n    string path = input;\n    if (regex_search(input, match, rgx)) path = match[1];\n    else {\n        size_t pos = input.find('=');\n        if (pos != string::npos) path = input.substr(pos + 1);\n        path.erase(0, path.find_first_not_of(\" \\t\\n\\r\\\"\"));\n        path.erase(path.find_last_not_of(\" \\t\\n\\r\\\"\") + 1);\n    }\n    Solution sol;\n    cout << sol.simplifyPath(path) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\nclass Solution {\n    public String simplifyPath(String path) {\n        // User Logic Here\n        return \"\";\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while (sc.hasNextLine()) sb.append(sc.nextLine()).append(\" \");\n        String input = sb.toString();\n        Matcher m = Pattern.compile(\"\\\"(.*?)\\\"\").matcher(input);\n        String path = input.trim();\n        if (m.find()) path = m.group(1);\n        else if (input.contains(\"=\")) path = input.substring(input.lastIndexOf(\"=\") + 1).trim().replace(\"\\\"\", \"\");\n        Solution sol = new Solution();\n        System.out.println(sol.simplifyPath(path));\n    }\n}",
        "javascript": "const fs = require('fs');\n\n/**\n * @param {string} path\n * @return {string}\n */\nvar simplifyPath = function(path) {\n    // User Logic Here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8').trim();\n    const match = input.match(/\"(.*?)\"/);\n    const path = match ? match[1] : input.split('=')[1]?.trim().replace(/\"/g, '') || input;\n    console.log(simplifyPath(path));\n}\nmain();",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nchar* simplifyPath(char* path) {\n    // User Logic Here\n    return path;\n}\n\nint main() {\n    char input[4096];\n    if (fgets(input, sizeof(input), stdin)) {\n        char* start = strchr(input, '\"');\n        char* path = input;\n        if (start) {\n            path = start + 1;\n            char* end = strrchr(path, '\"');\n            if (end) *end = '\\0';\n        } else {\n            char* eq = strchr(input, '=');\n            if (eq) path = eq + 1;\n            while(*path == ' ' || *path == '\"') path++;\n            char* end = path + strlen(path) - 1;\n            while(end > path && (*end == ' ' || *end == '\"' || *end == '\\n' || *end == '\\r')) *end-- = '\\0';\n        }\n        printf(\"%s\\n\", simplifyPath(path));\n    }\n    return 0;\n}"
    }

    test_cases = [
        # First two: Sample LeetCode cases
        {"input": "/home/", "expected_output": "/home", "is_sample": True},
        {"input": "/../", "expected_output": "/", "is_sample": True},
        # Middle five: Diverse cases
        {"input": "/home//foo/", "expected_output": "/home/foo", "is_sample": False},
        {"input": "/a/./b/../../c/", "expected_output": "/c", "is_sample": False},
        {"input": "/a/../../b/../c//.//", "expected_output": "/c", "is_sample": False},
        {"input": "/.../", "expected_output": "/...", "is_sample": False},
        {"input": "/..hidden", "expected_output": "/..hidden", "is_sample": False},
        # Last three: Stress tests
        {"input": "/" + "/".join(["a"]*500) + "/..", "expected_output": "/" + "/".join(["a"]*499), "is_sample": False},
        {"input": "/" + "/".join([".."]*1000), "expected_output": "/", "is_sample": False},
        {"input": "/" + "/".join([chr(97 + (i % 26)) for i in range(1000)]), "expected_output": "/" + "/".join([chr(97 + (i % 26)) for i in range(1000)]), "is_sample": False}
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
        "topics": ["String", "Stack"],
        "companyIndex": 0
    }

    output_path = "1-200/71_Simplify_Path.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
