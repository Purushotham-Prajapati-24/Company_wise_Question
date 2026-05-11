import json
import os

def generate_json():
    problem_id = 157
    title = "Read N Characters Given Read4"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>157. Read N Characters Given Read4</h3>
<p>Given a <code>file</code> and an integer <code>n</code>, read <code>n</code> characters from the <code>file</code> and store them in a destination buffer <code>buf</code>. This is a <strong>one-time</strong> read operation.</p>

<p>You have a helper API <code>read4(buf4)</code> that reads 4 consecutive characters from the file and stores them in a buffer array <code>buf4</code>. It returns the actual number of characters read.</p>

<p>The <code>read</code> function will be called only <strong>once</strong> for each test case.</p>

<p><strong>Note:</strong></p>
<ul>
	<li>The <code>read4</code> API is provided for you.</li>
	<li>You do not have access to the file directly.</li>
	<li>The destination buffer <code>buf</code> is guaranteed to be large enough to hold <code>n</code> characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> file = "abc", n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> After calling your read method, buf should contain "abc". We read 3 characters, so return 3. 
Note that "abc" has 3 characters, so we read all of them.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> file = "abcde", n = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> After calling your read method, buf should contain "abcde". We read 5 characters, so return 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= file.length &lt;= 500</code></li>
	<li><code>file</code> consist of English letters and digits.</li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>"""

    input_format = "Two lines. Line 1: string s (content of the file). Line 2: integer n (number of characters to read)."
    output_format = "An integer representing the number of characters read."
    
    constraints = [
        "1 <= file.length <= 500",
        "1 <= n <= 1000",
        "read4 API is provided."
    ]
    
    explanation = """To implement `read(buf, n)` using `read4(buf4)`:
1. **Iterative Read**:
   - Loop until we have read `n` characters or reached the end of the file.
   - In each iteration, call `read4` to fill a temporary buffer of size 4.
2. **Transfer Data**:
   - Calculate how many characters from the temporary buffer should be moved to the main buffer `buf`. This is `min(chars_read_by_read4, n - total_chars_read)`.
   - Copy these characters to `buf`.
   - Update the `total_chars_read` counter.
3. **Termination**:
   - If `read4` returns fewer than 4 characters, it means the end of the file (EOF) has been reached. Break the loop.
4. **Complexity**:
   - Time Complexity: O(N) where N is the number of characters to read.
   - Space Complexity: O(1) for the internal temporary buffer."""
    
    answer = """def read(buf, n):
    \"\"\"
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    \"\"\"
    total = 0
    buf4 = [''] * 4
    
    while total < n:
        count = read4(buf4)
        if count == 0:
            break
            
        # Determine how many to copy
        can_copy = min(count, n - total)
        for i in range(can_copy):
            buf[total] = buf4[i]
            total += 1
            
        if count < 4:
            break
            
    return total"""

    boilerplate = {
        "python": "import sys\n\n# External state for read4 simulation\nclass FileStream:\n    def __init__(self, content):\n        self.content = content\n        self.pos = 0\n    def read4(self, buf4):\n        count = 0\n        while count < 4 and self.pos < len(self.content):\n            buf4[count] = self.content[self.pos]\n            self.pos += 1\n            count += 1\n        return count\n\ndef read(buf, n):\n    # User logic here (use the global read4 below)\n    pass\n\nfs = None\ndef read4(buf4):\n    global fs\n    return fs.read4(buf4)\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        file_content = lines[0]\n        n = int(lines[1])\n        fs = FileStream(file_content)\n        buf = [''] * n\n        actual_read = read(buf, n)\n        print(actual_read)",
        "cpp": "#include <iostream>\n#include <string>\n#include <algorithm>\nusing namespace std;\nstatic string _file; static int _fpos=0;\nint read4(char*buf4){int cnt=0;while(cnt<4&&_fpos<(int)_file.size())buf4[cnt++]=_file[_fpos++];return cnt;}\nint read(char*buf, int n){\n    // User logic here\n    return 0;\n}\nint main(){\n    string fname; int n;\n    if(!getline(cin,fname)||!(cin>>n)) return 0;\n    _file=fname; _fpos=0;\n    char buf[1001]={};\n    cout<<read(buf,n)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static String _file; static int _fpos=0;\n    static int read4(char[]buf4){int cnt=0;while(cnt<4&&_fpos<_file.length())buf4[cnt++]=_file.charAt(_fpos++);return cnt;}\n    public static int read(char[]buf, int n){\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        _file=br.readLine(); int n=Integer.parseInt(br.readLine().trim());\n        _fpos=0; char[]buf=new char[n];\n        System.out.println(read(buf,n));\n    }\n}",
        "javascript": "const fs=require('fs');\nlet _file='',_fpos=0;\nfunction read4(buf4){let cnt=0;while(cnt<4&&_fpos<_file.length)buf4[cnt++]=_file[_fpos++];return cnt;}\nfunction read(buf,n){\n    // User logic here\n    return 0;\n}\nconst lines=fs.readFileSync(0,'utf8').split('\\n');\n_file=lines[0]; _fpos=0;\nconst n=parseInt(lines[1]);\nconsole.log(read([],n));",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\nstatic char _file[502]; static int _fpos=0;\nint read4(char*buf4){int cnt=0;while(cnt<4&&_file[_fpos])buf4[cnt++]=_file[_fpos++];return cnt;}\nint read(char*buf, int n){\n    // User logic here\n    return 0;\n}\nint main(){\n    char nstr[20];\n    if(!fgets(_file,sizeof(_file),stdin)||!fgets(nstr,sizeof(nstr),stdin)) return 0;\n    int l=strlen(_file); if(l>0&&_file[l-1]=='\\n')_file[--l]='\\0';\n    _fpos=0; int n=atoi(nstr);\n    char buf[1001]={};\n    printf(\"%d\\n\",read(buf,n)); return 0;\n}"
    }

    test_cases = [
        {"input": "abc\\n4", "expected_output": "3", "is_sample": True},
        {"input": "abcde\\n5", "expected_output": "5", "is_sample": True},
        {"input": "abcde\\n4", "expected_output": "4", "is_sample": False},
        {"input": "leetcode\\n10", "expected_output": "8", "is_sample": False},
        {"input": "a\\n1", "expected_output": "1", "is_sample": False},
        {"input": "12345678\\n2", "expected_output": "2", "is_sample": False},
        {"input": "testing123\\n20", "expected_output": "10", "is_sample": False},
        # Stress cases
        {"input": "a"*500 + "\\n1000", "expected_output": "500", "is_sample": False},
        {"input": "x"*500 + "\\n500", "expected_output": "500", "is_sample": False},
        {"input": "abcdefghij"*50 + "\\n3", "expected_output": "3", "is_sample": False}
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
        "topics": ["Array", "Simulation", "Interactive"],
        "companyIndex": 0
    }

    output_path = "1-200/157_Read_N_Characters_Given_Read4.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
