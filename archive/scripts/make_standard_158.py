import json
import os

def generate_json():
    problem_id = 158
    title = "Read N Characters Given Read4 II - Call multiple times"
    difficulty = "Hard"
    marks = 10
    
    html_description = """<h3>158. Read N Characters Given Read4 II - Call multiple times</h3>
<p>Given a <code>file</code> and an integer <code>n</code>, read <code>n</code> characters from the <code>file</code> and store them in a destination buffer <code>buf</code>. This method <strong>can be called multiple times</strong>.</p>

<p>You have a helper API <code>read4(buf4)</code> that reads 4 consecutive characters from the file and stores them in a buffer array <code>buf4</code>. It returns the actual number of characters read.</p>

<p><strong>Note:</strong></p>
<ul>
    <li>The <code>read</code> function may be called <strong>multiple times</strong>.</li>
    <li>You must maintain the state (buffered characters) between calls.</li>
	<li>The destination buffer <code>buf</code> is guaranteed to be large enough to hold <code>n</code> characters.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> file = "abc", queries = [1, 2, 1]
<strong>Output:</strong> [1, 2, 0]
<strong>Explanation:</strong>
FileStream fs("abc");
read(buf, 1); // returns 1. buf = ["a"]
read(buf, 2); // returns 2. buf = ["b", "c"]
read(buf, 1); // returns 0. buf = []
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> file = "abcde", queries = [4, 1]
<strong>Output:</strong> [4, 1]
<strong>Explanation:</strong>
FileStream fs("abcde");
read(buf, 4); // returns 4. buf = ["a","b","c","d"]
read(buf, 1); // returns 1. buf = ["e"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= file.length &lt;= 500</code></li>
	<li><code>file</code> consist of English letters and digits.</li>
	<li><code>1 &lt;= queries.length &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>"""

    input_format = "Two lines. Line 1: string s (file content). Line 2: space-separated integers (queries for n)."
    output_format = "A space-separated list of integers representing the number of characters read in each call."
    
    constraints = [
        "1 <= file.length <= 500",
        "1 <= queries.length <= 100",
        "Maintain state between calls."
    ]
    
    explanation = """To implement `read(buf, n)` with multiple calls:
1. **Persistent Buffer**:
   - Use a class-level buffer (e.g., `self.queue`) to store any characters that were read from `read4` but were not used in the current `read` call.
2. **Logic**:
   - For each call to `read(buf, n)`:
     - First, try to satisfy the request using characters already in the persistent buffer.
     - If more characters are needed, call `read4` repeatedly to fetch new characters.
     - If `read4` returns more characters than needed, store the surplus in the persistent buffer for the next `read` call.
3. **Complexity**:
   - Time Complexity: O(N) where N is the total number of characters read across all calls.
   - Space Complexity: O(1) beyond the input/output buffers, since the persistent buffer keeps at most 3 characters."""
    
    answer = """class Solution:
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        idx = 0
        # Use existing buffered characters
        while idx < n and self.queue:
            buf[idx] = self.queue.pop(0)
            idx += 1
            
        # Fetch new characters from read4 if needed
        while idx < n:
            buf4 = [''] * 4
            count = read4(buf4)
            if count == 0:
                break
                
            for i in range(count):
                if idx < n:
                    buf[idx] = buf4[i]
                    idx += 1
                else:
                    self.queue.append(buf4[i])
                    
            if count < 4:
                break
                
        return idx"""

    boilerplate = {
        "python": "import sys\n\n# External state for read4 simulation\nclass FileStream:\n    def __init__(self, content):\n        self.content = content\n        self.pos = 0\n    def read4(self, buf4):\n        count = 0\n        while count < 4 and self.pos < len(self.content):\n            buf4[count] = self.content[self.pos]\n            self.pos += 1\n            count += 1\n        return count\n\nclass Solution:\n    def __init__(self):\n        self.queue = []\n    def read(self, buf, n):\n        # User logic here\n        pass\n\nfs = None\ndef read4(buf4):\n    global fs\n    return fs.read4(buf4)\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        file_content = lines[0]\n        queries = list(map(int, lines[1].split()))\n        fs = FileStream(file_content)\n        sol = Solution()\n        results = []\n        for n in queries:\n            buf = [''] * n\n            results.append(str(sol.read(buf, n)))\n        print(\" \".join(results))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <queue>\nusing namespace std;\nstatic string fileContent=\"\"; static int filePos=0;\nint read4(char*buf4){int c=0;while(c<4&&filePos<(int)fileContent.size())buf4[c++]=fileContent[filePos++];return c;}\nclass Solution {\nprivate:\n    queue<char> q;\npublic:\n    int read(char *buf, int n) {\n        // User logic\n        return 0;\n    }\n};\nint main(){\n    string content, qline;\n    if(getline(cin,content)){if(content.size()>0&&content.back()=='\\r')content.pop_back(); fileContent=content; filePos=0;\n    if(getline(cin,qline)){Solution sol;istringstream ss(qline);int n;bool f=true;\n    while(ss>>n){char buf[1001]={};int r=sol.read(buf,n);if(!f)cout<<\" \";cout<<r;f=false;}\n    cout<<endl;}}\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\npublic class Main {\n    static String fileContent=\"\"; static int filePos=0;\n    static class Solution {\n        private Queue<Character> queue = new LinkedList<>();\n        public int read4(char[] buf4){int c=0;while(c<4&&filePos<fileContent.length())buf4[c++]=fileContent.charAt(filePos++);return c;}\n        public int read(char[] buf, int n) {\n            // User logic\n            return 0;\n        }\n    }\n    public static void main(String[] args) throws Exception{\n        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));\n        String fc=br.readLine(); if(fc==null)return; fileContent=fc; filePos=0;\n        String qline=br.readLine(); if(qline==null)return;\n        String[] parts=qline.trim().split(\"\\\\s+\"); Solution sol=new Solution();\n        StringBuilder sb=new StringBuilder(); boolean f=true;\n        for(String q:parts){if(q.isEmpty())continue;int n=Integer.parseInt(q);char[]buf=new char[n];int r=sol.read(buf,n);if(!f)sb.append(\" \");sb.append(r);f=false;}\n        System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nlet fileContent='',filePos=0;\nfunction read4(buf4){let c=0;while(c<4&&filePos<fileContent.length)buf4[c++]=fileContent[filePos++];return c;}\nvar solution=function(read4){\n    let internalBuf = [];\n    return function(buf,n){\n        // User logic\n        return 0;\n    };\n};\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){fileContent=lines[0].trim();filePos=0;const queries=lines[1].trim().split(/\\s+/).map(Number);\nconst sol=solution(read4);const res=[];for(let n of queries){res.push(sol([],n));}\nconsole.log(res.join(' '));}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstatic char fileContent[10000]; static int filePos=0, fileLen=0;\nint read4(char*buf4){int c=0;while(c<4&&filePos<fileLen)buf4[c++]=fileContent[filePos++];return c;}\nint read(char*buf, int n) {\n    // User logic\n    return 0;\n}\nint main(){\n    if(fgets(fileContent,sizeof(fileContent),stdin)){\n        fileLen=strlen(fileContent);while(fileLen>0&&(fileContent[fileLen-1]=='\\n'||fileContent[fileLen-1]=='\\r'))fileContent[--fileLen]='\\0';\n        char qline[10000]; if(fgets(qline,sizeof(qline),stdin)){char*tok=strtok(qline,\" \\t\\r\\n\");int f=1;\n        while(tok){int n=atoi(tok);char*buf=(char*)malloc(n*sizeof(char));int r=read(buf,n);if(!f)printf(\" \");printf(\"%d\",r);f=0;free(buf);tok=strtok(NULL,\" \\t\\r\\n\");}\n        printf(\"\\n\");}\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "abc\\n1 2 1", "expected_output": "1 2 0", "is_sample": True},
        {"input": "abcde\\n4 1", "expected_output": "4 1", "is_sample": True},
        {"input": "abcde\\n1 1 1 1 1 1", "expected_output": "1 1 1 1 1 0", "is_sample": False},
        {"input": "leetcode\\n4 4", "expected_output": "4 4", "is_sample": False},
        {"input": "a\\n1 1", "expected_output": "1 0", "is_sample": False},
        {"input": "12345678\\n2 2 2 2 2", "expected_output": "2 2 2 2 0", "is_sample": False},
        {"input": "testing123\\n5 5 5", "expected_output": "5 5 0", "is_sample": False},
        # Stress cases
        {"input": "a"*500 + "\\n" + " ".join(["1"]*500 + ["1"]), "expected_output": " ".join(["1"]*500 + ["0"]), "is_sample": False},
        {"input": "x"*500 + "\\n500", "expected_output": "500", "is_sample": False},
        {"input": "abcdefghij"*50 + "\\n100 100 100 100 100 100", "expected_output": "100 100 100 100 100 0", "is_sample": False}
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

    output_path = "1-200/158_Read_N_Characters_Given_Read4_II_-_Call_multiple_times.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
