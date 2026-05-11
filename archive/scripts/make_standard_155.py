import json
import os

def generate_json():
    problem_id = 155
    title = "Min Stack"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>155. Min Stack</h3>
<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<p>Implement the <code>MinStack</code> class:</p>

<ul>
	<li><code>MinStack()</code> initializes the stack object.</li>
	<li><code>void push(int val)</code> pushes the element <code>val</code> onto the stack.</li>
	<li><code>void pop()</code> removes the element on the top of the stack.</li>
	<li><code>int top()</code> gets the top element of the stack.</li>
	<li><code>int getMin()</code> retrieves the minimum element in the stack.</li>
</ul>

<p>You must implement a solution with <code>O(1)</code> time complexity for each function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>Output</strong>
[null,null,null,null,-3,null,0,-2]

<strong>Explanation</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on <strong>non-empty</strong> stacks.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>"""

    input_format = "Two lines. Line 1: space-separated operations. Line 2: space-separated JSON-style argument arrays."
    output_format = "A list of return values formatted as JSON."
    
    constraints = [
        "-2^31 <= val <= 2^31 - 1",
        "Operations called on non-empty stacks.",
        "At most 3 * 10^4 calls.",
        "O(1) time complexity for each function."
    ]
    
    explanation = """To implement a Min Stack with O(1) retrieval of the minimum element:
1. **Two Stacks Approach**:
   - Maintain a primary `stack` to store all pushed values.
   - Maintain a auxiliary `min_stack` to store the minimum value encountered so far at each level of the primary stack.
2. **Logic**:
   - **push(val)**:
     - Push `val` to `stack`.
     - Push `min(val, min_stack[-1])` to `min_stack` (or just `val` if it's the first element).
   - **pop()**: Pop from both `stack` and `min_stack`.
   - **top()**: Return the top element of `stack`.
   - **getMin()**: Return the top element of `min_stack`.
3. **Complexity**:
   - Time Complexity: O(1) for all operations.
   - Space Complexity: O(N) to store the values in two stacks."""
    
    answer = """class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]"""

    boilerplate = {
        "python": "import sys\nimport json\n\n# User logic class MinStack here\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        ops = lines[0].split()\n        args = json.loads(lines[1])\n        \n        obj = None\n        res = []\n        for op, arg in zip(ops, args):\n            if op == 'MinStack':\n                obj = MinStack()\n                res.append(None)\n            elif op == 'push':\n                obj.push(arg[0])\n                res.append(None)\n            elif op == 'pop':\n                obj.pop()\n                res.append(None)\n            elif op == 'top':\n                res.append(obj.top())\n            elif op == 'getMin':\n                res.append(obj.getMin())\n        \n        print(json.dumps(res).replace('null', 'null'))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\n#include <sstream>\n#include <climits>\nusing namespace std;\nclass MinStack{\n    stack<int> st, ms;\npublic:\n    MinStack(){}\n    void push(int val){\n        // User logic\n        st.push(val);\n        ms.push(ms.empty()?val:min(val,ms.top()));\n    }\n    void pop(){st.pop();ms.pop();}\n    int top(){return st.top();}\n    int getMin(){return ms.top();}\n};\nint main(){\n    string opline,argline;\n    if(!getline(cin,opline)||!getline(cin,argline)) return 0;\n    istringstream ss(opline); vector<string> ops; string op;\n    while(ss>>op) ops.push_back(op);\n    // parse args [[],[v],...]\n    vector<vector<int>> args;\n    int i=1,n=argline.size();\n    while(i<n){\n        if(argline[i]=='['){i++;vector<int> row;\n            while(i<n&&argline[i]!=']'){\n                if(isdigit(argline[i])||(argline[i]=='-')){int neg=1;if(argline[i]=='-'){neg=-1;i++;}\n                    int v=0;while(i<n&&isdigit(argline[i]))v=v*10+(argline[i++]-'0');v*=neg;row.push_back(v);}else i++;}\n            args.push_back(row);i++;}else i++;}\n    MinStack*obj=nullptr;\n    cout<<\"[\";\n    for(int k=0;k<(int)ops.size();k++){\n        if(k)cout<<\", \";\n        if(ops[k]==\"MinStack\"){obj=new MinStack();cout<<\"null\";}\n        else if(ops[k]==\"push\"){obj->push(args[k][0]);cout<<\"null\";}\n        else if(ops[k]==\"pop\"){obj->pop();cout<<\"null\";}\n        else if(ops[k]==\"top\"){cout<<obj->top();}\n        else if(ops[k]==\"getMin\"){cout<<obj->getMin();}\n    }\n    cout<<\"]\"<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    static class MinStack{\n        Deque<int[]> st=new ArrayDeque<>();\n        MinStack(){}\n        void push(int val){\n            // User logic\n            int mn=st.isEmpty()?val:Math.min(val,st.peek()[1]);\n            st.push(new int[]{val,mn});\n        }\n        void pop(){st.pop();}\n        int top(){return st.peek()[0];}\n        int getMin(){return st.peek()[1];}\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String opline=br.readLine().trim(), argline=br.readLine().trim();\n        String[] ops=opline.split(\"\\\\s+\");\n        List<int[]> argList=new ArrayList<>();\n        int i=1,n=argline.length();\n        while(i<n){if(argline.charAt(i)=='['){i++;List<Integer> row=new ArrayList<>();\n            while(i<n&&argline.charAt(i)!=']'){char c=argline.charAt(i);\n                if(c=='-'||Character.isDigit(c)){int neg=1;if(c=='-'){neg=-1;i++;}int v=0;while(i<n&&Character.isDigit(argline.charAt(i)))v=v*10+(argline.charAt(i++)-'0');v*=neg;row.add(v);}else i++;}\n            int[]arr=new int[row.size()];for(int j=0;j<row.size();j++)arr[j]=row.get(j);argList.add(arr);i++;}else i++;}\n        MinStack obj=null;\n        StringBuilder sb=new StringBuilder(\"[\");\n        for(int k=0;k<ops.length;k++){if(k>0)sb.append(\", \");\n            if(ops[k].equals(\"MinStack\")){obj=new MinStack();sb.append(\"null\");}\n            else if(ops[k].equals(\"push\")){obj.push(argList.get(k)[0]);sb.append(\"null\");}\n            else if(ops[k].equals(\"pop\")){obj.pop();sb.append(\"null\");}\n            else if(ops[k].equals(\"top\")){sb.append(obj.top());}\n            else if(ops[k].equals(\"getMin\")){sb.append(obj.getMin());}\n        }\n        sb.append(\"]\"); System.out.println(sb);\n    }\n}",
        "javascript": "const fs=require('fs');\nclass MinStack{\n  constructor(){this.st=[];this.ms=[];}\n  push(val){\n    // User logic\n    this.st.push(val);\n    this.ms.push(this.ms.length===0?val:Math.min(val,this.ms[this.ms.length-1]));\n  }\n  pop(){this.st.pop();this.ms.pop();}\n  top(){return this.st[this.st.length-1];}\n  getMin(){return this.ms[this.ms.length-1];}\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=2){\n  const ops=lines[0].trim().split(/\\s+/);\n  const args=JSON.parse(lines[1]);\n  let obj=null; const res=[];\n  for(let i=0;i<ops.length;i++){\n    if(ops[i]==='MinStack'){obj=new MinStack();res.push(null);}\n    else if(ops[i]==='push'){obj.push(args[i][0]);res.push(null);}\n    else if(ops[i]==='pop'){obj.pop();res.push(null);}\n    else if(ops[i]==='top'){res.push(obj.top());}\n    else if(ops[i]==='getMin'){res.push(obj.getMin());}\n  }\n  console.log('['+res.map(v=>v===null?'null':v).join(', ')+']');\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <limits.h>\ntypedef struct{int val,mn;}Entry;\ntypedef struct{Entry*data;int top,cap;}MinStack;\nMinStack* minStackCreate(){MinStack*s=(MinStack*)malloc(sizeof(MinStack));s->data=(Entry*)malloc(30001*sizeof(Entry));s->top=0;s->cap=30001;return s;}\nvoid minStackPush(MinStack*obj,int val){int mn=obj->top==0?val:(val<obj->data[obj->top-1].mn?val:obj->data[obj->top-1].mn);obj->data[obj->top++]=(Entry){val,mn};}\nvoid minStackPop(MinStack*obj){if(obj->top>0)obj->top--;}\nint minStackTop(MinStack*obj){return obj->data[obj->top-1].val;}\nint minStackGetMin(MinStack*obj){return obj->data[obj->top-1].mn;}\nvoid minStackFree(MinStack*obj){free(obj->data);free(obj);}\nint main(){\n    char opline[500000],argline[500000];\n    if(!fgets(opline,sizeof(opline),stdin)||!fgets(argline,sizeof(argline),stdin)) return 0;\n    char*ops[30002]; int opc=0;\n    char*tok=strtok(opline,\" \\t\\r\\n\");\n    while(tok&&opc<30002){ops[opc++]=tok;tok=strtok(NULL,\" \\t\\r\\n\");}\n    // parse args\n    int argvals[30002]; int argcnt=0;\n    int hasval[30002]; // 1 if has int arg\n    memset(hasval,0,sizeof(hasval));\n    char*p=argline; int ai=0;\n    while(*p&&ai<opc){\n        while(*p&&*p!='[')p++;if(!*p)break;p++;\n        while(*p&&*p!=']'&&*p!=','){\n            if(*p=='-'||(*p>='0'&&*p<='9')){\n                int neg=1;if(*p=='-'){neg=-1;p++;}\n                int v=0;while(*p>='0'&&*p<='9')v=v*10+(*p++)-'0';v*=neg;\n                argvals[ai]=v;hasval[ai]=1;break;\n            }p++;\n        }\n        while(*p&&*p!=']')p++;if(*p==']')p++;\n        ai++;\n    }\n    MinStack*obj=NULL;\n    printf(\"[\");\n    for(int k=0;k<opc;k++){\n        if(k)printf(\", \");\n        if(!strcmp(ops[k],\"MinStack\")){obj=minStackCreate();printf(\"null\");}\n        else if(!strcmp(ops[k],\"push\")){minStackPush(obj,argvals[k]);printf(\"null\");}\n        else if(!strcmp(ops[k],\"pop\")){minStackPop(obj);printf(\"null\");}\n        else if(!strcmp(ops[k],\"top\")){printf(\"%d\",minStackTop(obj));}\n        else if(!strcmp(ops[k],\"getMin\")){printf(\"%d\",minStackGetMin(obj));}\n    }\n    printf(\"]\\n\"); return 0;\n}"
    }

    test_cases = [
        {"input": "MinStack push push push getMin pop top getMin\\n[[], [-2], [0], [-3], [], [], [], []]", "expected_output": "[null, null, null, null, -3, null, 0, -2]", "is_sample": True},
        {"input": "MinStack push getMin\\n[[], [1], []]", "expected_output": "[null, null, 1]", "is_sample": True},
        {"input": "MinStack push push push pop getMin\\n[[], [1], [2], [0], [], []]", "expected_output": "[null, null, null, null, null, 1]", "is_sample": False},
        {"input": "MinStack push push top getMin\\n[[], [-10], [10], [], []]", "expected_output": "[null, null, null, 10, -10]", "is_sample": False},
        {"input": "MinStack push push push getMin pop getMin pop getMin\\n[[], [5], [4], [6], [], [], [], [], []]", "expected_output": "[null, null, null, null, 4, null, 4, null, 5]", "is_sample": False},
        {"input": "MinStack push push push pop top getMin\\n[[], [2147483647], [-2147483648], [2147483647], [], [], []]", "expected_output": "[null, null, null, null, null, -2147483648, -2147483648]", "is_sample": False},
        {"input": "MinStack push push getMin\\n[[], [0], [0], []]", "expected_output": "[null, null, null, 0]", "is_sample": False},
        # Stress cases
        {"input": "MinStack" + " push"*3000 + " getMin"*1 + "\\n" + json.dumps([[]] + [[i] for i in range(3000)] + [[]]), "expected_output": "...", "is_sample": False},
        {"input": "MinStack" + " push"*3000 + " pop"*3000 + " push"*1 + " getMin"*1 + "\\n" + json.dumps([[]] + [[i] for i in range(3000)] + [[] for _ in range(3000)] + [[100]] + [[]]), "expected_output": "...", "is_sample": False},
        {"input": "MinStack" + " push"*1000 + " getMin"*1000 + "\\n" + json.dumps([[]] + [[-i] for i in range(1000)] + [[] for _ in range(1000)]), "expected_output": "...", "is_sample": False}
    ]
    
    def _solve(ops, args):
        st = []; ms = []; res = []
        for op, arg in zip(ops, args):
            if op == 'MinStack': res.append(None)
            elif op == 'push':
                v = arg[0]; st.append(v)
                if not ms or v <= ms[-1]: ms.append(v)
                else: ms.append(ms[-1])
                res.append(None)
            elif op == 'pop': st.pop(); ms.pop(); res.append(None)
            elif op == 'top': res.append(st[-1])
            elif op == 'getMin': res.append(ms[-1])
        return json.dumps(res).replace('null', 'null')

    for i in range(7, 10):
        ops = test_cases[i]["input"].split("\\n")[0].split()
        args = json.loads(test_cases[i]["input"].split("\\n")[1])
        test_cases[i]["expected_output"] = _solve(ops, args)

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
        "topics": ["Stack", "Design"],
        "companyIndex": 0
    }

    output_path = "1-200/155_Min_Stack.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
