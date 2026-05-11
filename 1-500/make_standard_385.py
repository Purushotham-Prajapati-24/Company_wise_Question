import json
import os


def generate_json():
    problem_id = 385
    title = "Mini Parser"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>385. Mini Parser</h3>
<p>Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized <code>NestedInteger</code>.</p>

<p>Each element is either an integer or a list whose elements may also be integers or other lists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "324"
<strong>Output:</strong> 324
<strong>Explanation:</strong> You should return a NestedInteger object which contains a single integer 324.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "[123,[456,[789]]]"
<strong>Output:</strong> [123,[456,[789]]]
<strong>Explanation:</strong> Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of digits, square brackets <code>"[]"</code>, negative sign <code>"-"</code>, and commas <code>","</code>.</li>
	<li><code>s</code> is the serialization of a valid <code>NestedInteger</code>.</li>
	<li>All the integers in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.</li>
</ul>"""

    input_format = """A string s representing a nested list."""
    output_format = """The deserialized NestedInteger (as a list or integer)."""
    
    constraints = [
        "1 <= s.length <= 5 * 10^4",
        "s consists of digits, square brackets, negative signs, and commas.",
        "s is guaranteed to be a valid NestedInteger serialization."
    ]
    
    explanation = """To deserialize a nested integer string:
1. **Iterative Approach with Stack**:
   - If the first character is not '[', it's a single integer. Parse and return.
   - Otherwise, use a stack to keep track of the current `NestedInteger` (list) being built.
   - Iterate through the string:
     - '-': Mark current number as negative.
     - Digit: Accumulate the number value.
     - '[': Start a new `NestedInteger` list, push to stack.
     - ',' or ']':
       - If we were parsing a number, add it to the current list on the stack top.
       - If ']', we've finished the current list. If it's not the last list, pop it and add to the previous list on the stack.
2. **Recursive Approach**:
   - Similar logic, but use function calls to handle nested structures.

### Complexity:
- **Time Complexity**: $O(N)$, where $N$ is the length of string $s$.
- **Space Complexity**: $O(D)$, where $D$ is the maximum depth of nesting."""
    
    answer = """# Structure equivalent to LeetCode's NestedInteger
class Solution:
    def deserialize(self, s: str):
        if not s: return None
        if s[0] != '[':
            return int(s)
        
        stack = []
        num, sign, has_num = 0, 1, False
        
        for i, char in enumerate(s):
            if char == '-':
                sign = -1
            elif char.isdigit():
                num = num * 10 + int(char)
                has_num = True
            elif char == '[':
                stack.append([])
            elif char == ',' or char == ']':
                if has_num:
                    stack[-1].append(sign * num)
                    num, sign, has_num = 0, 1, False
                if char == ']' and len(stack) > 1:
                    popped = stack.pop()
                    stack[-1].append(popped)
                    
        return stack[0]"""

    boilerplate = {
        "python": "import sys\nimport json\nclass Solution:\n    def deserialize(self, s: str):\n        # User logic here\n        pass\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    if input_data:\n        if input_data.startswith('\"') and input_data.endswith('\"'): input_data = input_data[1:-1]\n        result = Solution().deserialize(input_data)\n        print(json.dumps(result).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <stack>\n#include <algorithm>\nusing namespace std;\nclass NestedInteger {\nbool is_int; int val; vector<NestedInteger> list;\npublic:\nNestedInteger() : is_int(false), val(0) {}\nNestedInteger(int value) : is_int(true), val(value) {}\nbool isInteger() const { return is_int; }\nint getInteger() const { return val; }\nvoid setInteger(int value) { is_int = true; val = value; }\nvoid add(const NestedInteger &ni) { is_int = false; list.push_back(ni); }\nconst vector<NestedInteger> &getList() const { return list; }\n};\nclass Solution {\npublic:\n    NestedInteger deserialize(string s) {\n        // User logic here\n        return NestedInteger();\n    }\n};\nvoid printNI(const NestedInteger& ni) {\n    if (ni.isInteger()) cout << ni.getInteger();\n    else {\n        cout << \"[\"; const vector<NestedInteger>& list = ni.getList();\n        for (size_t i = 0; i < list.size(); ++i) { printNI(list[i]); if (i < list.size() - 1) cout << \",\"; }\n        cout << \"]\";\n    }\n}\nint main() {\n    string s; if (getline(cin, s)) {\n        s.erase(0, s.find_first_not_of(\" \\t\\n\\r\"));\n        s.erase(s.find_last_not_of(\" \\t\\n\\r\") + 1);\n        if (s.size() >= 2 && s.front() == '\"' && s.back() == '\"') s = s.substr(1, s.size() - 2);\n        printNI(Solution().deserialize(s)); cout << endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nclass NestedInteger {\nprivate Integer value; private List<NestedInteger> list;\npublic NestedInteger() { list = new ArrayList<>(); }\npublic NestedInteger(int value) { this.value = value; }\npublic boolean isInteger() { return value != null; }\npublic Integer getInteger() { return value; }\npublic void setInteger(int value) { this.value = value; }\npublic void add(NestedInteger ni) { if (this.list == null) this.list = new ArrayList<>(); this.list.add(ni); }\npublic List<NestedInteger> getList() { return list; }\n}\nclass Solution {\n    public NestedInteger deserialize(String s) {\n        // User logic here\n        return null;\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String s = sc.nextLine().trim();\n            if (s.startsWith(\"\\\"\") && s.endsWith(\"\\\"\")) s = s.substring(1, s.length() - 1);\n            printNI(new Solution().deserialize(s));\n            System.out.println();\n        }\n    }\n    private static void printNI(NestedInteger ni) {\n        if (ni == null) return;\n        if (ni.isInteger()) System.out.print(ni.getInteger());\n        else {\n            System.out.print(\"[\"); List<NestedInteger> list = ni.getList();\n            if(list != null) { for (int i = 0; i < list.size(); i++) { printNI(list.get(i)); if (i < list.size() - 1) System.out.print(\",\"); } }\n            System.out.print(\"]\");\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nvar deserialize = function(s) {\n    // User logic here\n};\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    let s = input; if (s.startsWith('\"') && s.endsWith('\"')) s = s.slice(1, -1);\n    console.log(JSON.stringify(deserialize(s)).replace(/\\s/g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\nstruct NestedInteger { int is_int; int val; struct NestedInteger** list; int list_size; };\nstruct NestedInteger* deserialize(char* s) {\n    // User logic here\n    return NULL;\n}\nvoid printNI(struct NestedInteger* ni) {\n    if (!ni) return;\n    if (ni->is_int) printf(\"%d\", ni->val);\n    else {\n        printf(\"[\");\n        for (int i = 0; i < ni->list_size; i++) { printNI(ni->list[i]); if (i < ni->list_size - 1) printf(\",\"); }\n        printf(\"]\");\n    }\n}\nint main() {\n    char s[100005];\n    if (fgets(s, 100005, stdin)) {\n        int len = strlen(s);\n        while(len > 0 && (s[len-1] == '\\n' || s[len-1] == '\\r')) s[--len] = '\\0';\n        char *ptr = s;\n        if (*ptr == '\"' && len >= 2 && s[len-1] == '\"') { ptr++; s[len-1] = '\\0'; }\n        printNI(deserialize(ptr));\n        printf(\"\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "324", "expected_output": "324", "is_sample": True},
        {"input": "[123,[456,[789]]]", "expected_output": "[123,[456,[789]]]", "is_sample": True},
        # 5 Diverse
        {"input": "-3", "expected_output": "-3", "is_sample": False},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[123,456]", "expected_output": "[123,456]", "is_sample": False},
        {"input": "[123,[-456],789]", "expected_output": "[123,[-456],789]", "is_sample": False},
        {"input": "[1,2,3,[4,5,6],7,8,9]", "expected_output": "[1,2,3,[4,5,6],7,8,9]", "is_sample": False},
        # 3 Stress
        {"input": "[" + ",".join([str(i) for i in range(100)]) + "]", "expected_output": "[" + ",".join([str(i) for i in range(100)]) + "]", "is_sample": False},
        {"input": "[" * 10 + "1" + "]" * 10, "expected_output": "[[[[[[[[[[1]]]]]]]]]]", "is_sample": False},
        {"input": "[123,[],[[],[456]],789]", "expected_output": "[123,[],[[],[456]],789]", "is_sample": False}
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
        "topics": ["Stack", "String"],
        "companyIndex": 0
    }

    output_path = "301-500/385_Mini_Parser.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
