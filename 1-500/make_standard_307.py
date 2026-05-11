import json
import os

def generate_json():
    problem_id = 307
    title = "Range Sum Query - Mutable"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>307. Range Sum Query - Mutable</h3>
<p>Given an integer array <code>nums</code>, handle multiple queries of the following types:</p>

<ol>
	<li><strong>Update</strong> the value of an element in <code>nums</code>.</li>
	<li>Calculate the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> where <code>left &lt;= right</code>.</li>
</ol>

<p>Implement the <code>NumArray</code> class:</p>
<ul>
	<li><code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
	<li><code>void update(int index, int val)</code> Updates the value of <code>nums[index]</code> to be <code>val</code>.</li>
	<li><code>int sumRange(int left, int right)</code> Returns the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> (i.e., <code>nums[left] + nums[left + 1] + ... + nums[right]</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
<strong>Output:</strong>
[null, 9, null, 8]

<strong>Explanation:</strong>
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>0 &lt;= index &lt; nums.length</code></li>
	<li><code>-100 &lt;= val &lt;= 100</code></li>
	<li><code>0 &lt;= left &lt;= right &lt; nums.length</code></li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>update</code> and <code>sumRange</code>.</li>
</ul>"""

    input_format = "A list of strings for commands and a list of arguments."
    output_format = "A list of results (null for void methods, integers for sumRange)."
    
    constraints = [
        "1 <= nums.length <= 30,000",
        "At most 30,000 calls to update and sumRange."
    ]
    
    explanation = """To handle frequent point updates and range sum queries efficiently ($O(\log N)$ for both):
1. **Fenwick Tree (BIT)**: This is the most space-efficient way to handle cumulative sums and updates.
2. **Operations**:
   - `update(index, val)`: Find the difference `diff = val - original_nums[index]`. Update the BIT at `index + 1` by adding `diff`.
   - `sumRange(left, right)`: Calculate `query(right + 1) - query(left)`.
3. **BIT Logic**:
   - `query(i)`: Sum of elements from index 1 to i. Traverse parents using `i -= i & -i`.
   - `updateBIT(i, diff)`: Add `diff` to indices and their ancestors using `i += i & -i`.
4. **Complexity Analysis**:
   - Initialization: O(N log N) or O(N).
   - Update: O(log N).
   - Query: O(log N).
   - Space: O(N) to store the BIT and original nums."""
    
    answer = """class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)
        # Build BIT in O(N log N)
        for i in range(self.n):
            self.init_update(i, nums[i])
            
    def init_update(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & (-i)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.init_update(index, diff)

    def get_sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(right) - self.get_sum(left - 1)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass NumArray:\n    def __init__(self, nums):\n        # User logic here\n        pass\n    def update(self, index, val):\n        pass\n    def sumRange(self, left, right):\n        return 0\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    # Lethal extraction for commands and arguments\n    # Example input: [\"NumArray\", \"sumRange\"] \\n [[[1, 3, 5]], [0, 2]]\n    parts = re.findall(r'\\[.*\\]', raw_input, re.DOTALL)\n    commands = json.loads(parts[0])\n    arguments = json.loads(parts[1])\n    \n    obj = None\n    results = []\n    for cmd, args in zip(commands, arguments):\n        if cmd == 'NumArray':\n            obj = NumArray(args[0])\n            results.append(None)\n        elif cmd == 'update':\n            obj.update(args[0], args[1])\n            results.append(None)\n        elif cmd == 'sumRange':\n            results.append(obj.sumRange(args[0], args[1]))\n    print(json.dumps(results))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\nusing namespace std;\n\nclass NumArray {\npublic:\n    NumArray(vector<int>& nums) {}\n    void update(int index, int val) {}\n    int sumRange(int left, int right) { return 0; }\n};\n\n// Minimal JSON-like parser for simple nested arrays\nvector<string> parseStrings(string s) {\n    vector<string> res;\n    regex re(\"\\\"(.*?)\\\"\");\n    smatch m;\n    while (regex_search(s, m, re)) {\n        res.push_back(m[1]);\n        s = m.suffix();\n    }\n    return res;\n}\n\nint main() {\n    string input, line;\n    while(getline(cin, line)) input += line + \" \";\n    \n    size_t first_bracket = input.find('[');\n    size_t second_bracket = input.find('[', first_bracket + 1);\n    \n    string cmd_str = input.substr(first_bracket, input.find(']', first_bracket) - first_bracket + 1);\n    string arg_str = input.substr(input.find('[', input.find(']', first_bracket)));\n\n    vector<string> commands = parseStrings(cmd_str);\n    \n    // Crude but effective for this specific problem's arguments\n    NumArray* obj = nullptr;\n    cout << \"[\";\n    \n    // We'll use a simplified loop. For a real environment, we'd need a robust JSON library.\n    // Here we manually skip to NumArray's nums array.\n    size_t pos = arg_str.find(\"[[\") + 2;\n    vector<int> nums;\n    while(arg_str[pos] != ']') {\n        if(isdigit(arg_str[pos]) || arg_str[pos] == '-') {\n            nums.push_back(stoi(arg_str.substr(pos)));\n            while(isdigit(arg_str[pos]) || arg_str[pos] == '-') pos++;\n        } else pos++;\n    }\n    obj = new NumArray(nums);\n    cout << \"null\";\n    \n    size_t arg_pos = arg_str.find(\"],\", pos) + 2;\n    for(size_t i = 1; i < commands.size(); i++) {\n        cout << \",\";\n        if(commands[i] == \"update\") {\n            int idx = stoi(arg_str.substr(arg_str.find('[', arg_pos) + 1));\n            int val = stoi(arg_str.substr(arg_str.find(',', arg_str.find('[', arg_pos)) + 1));\n            obj->update(idx, val);\n            cout << \"null\";\n        } else if(commands[i] == \"sumRange\") {\n            int l = stoi(arg_str.substr(arg_str.find('[', arg_pos) + 1));\n            int r = stoi(arg_str.substr(arg_str.find(',', arg_str.find('[', arg_pos)) + 1));\n            cout << obj->sumRange(l, r);\n        }\n        arg_pos = arg_str.find(\"],\", arg_pos + 1) + 2;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class NumArray {\n    public NumArray(int[] nums) {}\n    public void update(int index, int val) {}\n    public int sumRange(int left, int right) { return 0; }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        StringBuilder sb = new StringBuilder();\n        while(sc.hasNextLine()) sb.append(sc.nextLine());\n        String input = sb.toString();\n\n        List<String> cmds = new ArrayList<>();\n        Matcher m = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(input.substring(0, input.indexOf(\"]\") + 1));\n        while(m.find()) cmds.add(m.group(1));\n\n        String argStr = input.substring(input.indexOf(\"[\", input.indexOf(\"]\")));\n        NumArray obj = null;\n        List<Object> results = new ArrayList<>();\n\n        // Manual extraction for simplicity in competitive programming context\n        Pattern p = Pattern.compile(\"\\\\[([\\\\d\\\\s,.-]*)\\\\]\");\n        Matcher am = p.matcher(argStr);\n        int idx = 0;\n        while(am.find() && idx < cmds.size()) {\n            String content = am.group(1).trim();\n            if(cmds.get(idx).equals(\"NumArray\")) {\n                // The first arg is special: [[1,3,5]]\n                // So we need to find the innermost array\n                Matcher inner = Pattern.compile(\"\\\\[([\\\\d\\\\s,.-]*)\\\\]\").matcher(argStr);\n                inner.find();\n                String[] parts = inner.group(1).split(\",\");\n                int[] nums = new int[parts.length];\n                for(int i=0; i<parts.length; i++) nums[i] = Integer.parseInt(parts[i].trim());\n                obj = new NumArray(nums);\n                results.add(null);\n                // Skip the am.find() since we consumed one more bracket level manually or adjust logic\n            } else if(cmds.get(idx).equals(\"update\")) {\n                String[] parts = content.split(\",\");\n                obj.update(Integer.parseInt(parts[0].trim()), Integer.parseInt(parts[1].trim()));\n                results.add(null);\n            } else {\n                String[] parts = content.split(\",\");\n                results.add(obj.sumRange(Integer.parseInt(parts[0].trim()), Integer.parseInt(parts[1].trim())));\n            }\n            idx++;\n        }\n        System.out.println(results.toString().replace(\" \", \"\").replace(\"null\", \"null\"));\n    }\n}",
        "javascript": "const fs = require('fs');\n\nclass NumArray {\n    constructor(nums) {}\n    update(index, val) {}\n    sumRange(left, right) { return 0; }\n}\n\nconst input = fs.readFileSync(0, 'utf-8').trim();\nconst matches = input.match(/\\[.*\\]/sg);\nconst commands = JSON.parse(matches[0]);\nconst args = JSON.parse(matches[1]);\n\nlet obj = null;\nconst results = [];\nfor (let i = 0; i < commands.length; i++) {\n    if (commands[i] === 'NumArray') {\n        obj = new NumArray(args[i][0]);\n        results.push(null);\n    } else if (commands[i] === 'update') {\n        obj.update(args[i][0], args[i][1]);\n        results.push(null);\n    } else {\n        results.push(obj.sumRange(args[i][0], args[i][1]));\n    }\n}\nconsole.log(JSON.stringify(results));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\ntypedef struct { int* tree; int n; } NumArray;\n\nNumArray* numArrayCreate(int* nums, int numsSize) { return NULL; }\nvoid numArrayUpdate(NumArray* obj, int index, int val) {}\nint numArraySumRange(NumArray* obj, int left, int right) { return 0; }\nvoid numArrayFree(NumArray* obj) {}\n\nint main() {\n    char buf[65536];\n    int len = 0, ch;\n    while((ch = getchar()) != EOF) buf[len++] = ch;\n    buf[len] = '\\0';\n\n    // Parse commands\n    char* p = strstr(buf, \"[\");\n    char cmds[100][20]; int cmd_count = 0;\n    char* q = p + 1;\n    while(*q != ']') {\n        if(*q == '\"') {\n            char* end = strchr(q + 1, '\"');\n            strncpy(cmds[cmd_count], q + 1, end - q - 1);\n            cmds[cmd_count++][end - q - 1] = '\\0';\n            q = end + 1;\n        } else q++;\n    }\n\n    // Parse arguments\n    p = strstr(q, \"[\");\n    NumArray* obj = NULL;\n    printf(\"[\");\n    for(int i = 0; i < cmd_count; i++) {\n        if(i > 0) printf(\",\");\n        if(strcmp(cmds[i], \"NumArray\") == 0) {\n            int nums[30000], sz = 0;\n            while(*p != '[') p++; p++; // skip [[\n            while(*p != ']') {\n                if(isdigit(*p) || *p == '-') { nums[sz++] = strtol(p, &p, 10); } else p++;\n            }\n            obj = numArrayCreate(nums, sz);\n            printf(\"null\");\n        } else {\n            while(*p != '[') p++;\n            int a = strtol(p + 1, &p, 10);\n            while(*p != ',') p++;\n            int b = strtol(p + 1, &p, 10);\n            if(strcmp(cmds[i], \"update\") == 0) {\n                numArrayUpdate(obj, a, b);\n                printf(\"null\");\n            } else {\n                printf(\"%d\", numArraySumRange(obj, a, b));\n            }\n        }\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }

    test_cases = [
        {"input": '["NumArray", "sumRange", "update", "sumRange"]\n[[1, 3, 5], [0, 2], [1, 2], [0, 2]]', "expected_output": "[null, 9, null, 8]", "is_sample": True},
        {"input": '["NumArray", "sumRange"]\n[[10], [0, 0]]', "expected_output": "[null, 10]", "is_sample": False},
        {"input": '["NumArray", "update", "sumRange"]\n[[10], [0, 5], [0, 0]]', "expected_output": "[null, null, 5]", "is_sample": False},
        {"input": '["NumArray", "sumRange", "update", "sumRange", "update", "sumRange"]\n[[1, 1, 1, 1], [0, 3], [0, 2], [0, 3], [3, 0], [0, 3]]', "expected_output": "[null, 4, null, 5, null, 4]", "is_sample": False},
        {"input": '["NumArray", "sumRange"]\n[[[1,2,3,4,5]], [1, 3]]', "expected_output": "[null, 9]", "is_sample": False},
        {"input": '["NumArray", "update", "sumRange"]\n[[[1,2,3]], [1, 5], [0, 2]]', "expected_output": "[null, null, 9]", "is_sample": False},
        {"input": '["NumArray", "sumRange"]\n[[[100]], [0, 0]]', "expected_output": "[null, 100]", "is_sample": False},
        {"input": '["NumArray", "update", "update", "sumRange"]\n[[[5,2,8,4]], [0, 1], [3, 2], [0, 3]]', "expected_output": "[null, null, null, 13]", "is_sample": False},
        {"input": '["NumArray", "sumRange", "sumRange"]\n[[[1,2,3,4,5]], [0, 0], [4, 4]]', "expected_output": "[null, 1, 5]", "is_sample": False},
        {"input": '["NumArray", "update", "sumRange"]\n[[[-1,-2,-3]], [0, 1], [0, 2]]', "expected_output": "[null, null, -4]", "is_sample": False}
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
        "topics": ["Array", "Binary Indexed Tree", "Segment Tree"],
        "companyIndex": 0
    }

    output_path = "201-400/307_Range_Sum_Query_Mutable.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
