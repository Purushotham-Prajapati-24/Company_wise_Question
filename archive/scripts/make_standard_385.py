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
        "python": """import sys
import json

class Solution:
    def deserialize(self, s: str):
        # User Logic Here
        pass

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    if input_data:
        sol = Solution()
        # Remove exterior quotes if present from input stripping
        if input_data.startswith('"') and input_data.endswith('"'):
            input_data = input_data[1:-1]
        result = sol.deserialize(input_data)
        print(json.dumps(result).replace(' ', ''))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

// Mock NestedInteger for local testing parity
class NestedInteger {
private:
    bool is_int;
    int val;
    vector<NestedInteger> list;
public:
    NestedInteger() : is_int(false), val(0) {}
    NestedInteger(int value) : is_int(true), val(value) {}
    bool isInteger() const { return is_int; }
    int getInteger() const { return val; }
    void setInteger(int value) { is_int = true; val = value; }
    void add(const NestedInteger &ni) { is_int = false; list.push_back(ni); }
    const vector<NestedInteger> &getList() const { return list; }
};

class Solution {
public:
    NestedInteger deserialize(string s) {
        // User Logic Here
        return NestedInteger();
    }
};

void printNI(const NestedInteger& ni) {
    if (ni.isInteger()) {
        cout << ni.getInteger();
    } else {
        cout << "[";
        const vector<NestedInteger>& list = ni.getList();
        for (int i = 0; i < list.size(); ++i) {
            printNI(list[i]);
            if (i < list.size() - 1) cout << ",";
        }
        cout << "]";
    }
}

int main() {
    string s;
    if (getline(cin, s)) {
        if (s.front() == '"' && s.back() == '"') s = s.substr(1, s.size() - 2);
        Solution sol;
        NestedInteger res = sol.deserialize(s);
        printNI(res);
        cout << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class NestedInteger {
    private Integer value;
    private List<NestedInteger> list;
    public NestedInteger() { list = new ArrayList<>(); }
    public NestedInteger(int value) { this.value = value; }
    public boolean isInteger() { return value != null; }
    public Integer getInteger() { return value; }
    public void setInteger(int value) { this.value = value; }
    public void add(NestedInteger ni) {
        if (this.list == null) this.list = new ArrayList<>();
        this.list.add(ni);
    }
    public List<NestedInteger> getList() { return list; }
}

class Solution {
    public NestedInteger deserialize(String s) {
        // User Logic Here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine().trim();
            if (s.startsWith("\\\"") && s.endsWith("\\\"")) s = s.substring(1, s.length() - 1);
            Solution sol = new Solution();
            NestedInteger res = sol.deserialize(s);
            printNI(res);
            System.out.println();
        }
    }
    private static void printNI(NestedInteger ni) {
        if (ni == null) return;
        if (ni.isInteger()) {
            System.out.print(ni.getInteger());
        } else {
            System.out.print("[");
            List<NestedInteger> list = ni.getList();
            for (int i = 0; i < list.size(); i++) {
                printNI(list.get(i));
                if (i < list.size() - 1) System.out.print(",");
            }
            System.out.print("]");
        }
    }
}""",
        "javascript": """var deserialize = function(s) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();

function formatNI(ni) {
    return JSON.stringify(ni).replace(/\\s/g, '');
}

if (input) {
    let s = input;
    if (s.startsWith('"') && s.endsWith('"')) s = s.slice(1, -1);
    console.log(formatNI(deserialize(s)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct NestedInteger {
    int is_int;
    int val;
    struct NestedInteger** list;
    int list_size;
};

struct NestedInteger* deserialize(char* s) {
    // User Logic Here
    return NULL;
}

void printNI(struct NestedInteger* ni) {
    if (!ni) return;
    if (ni->is_int) {
        printf("%d", ni->val);
    } else {
        printf("[");
        for (int i = 0; i < ni->list_size; i++) {
            printNI(ni->list[i]);
            if (i < ni->list_size - 1) printf(",");
        }
        printf("]");
    }
}

int main() {
    char s[50005];
    if (fgets(s, 50005, stdin)) {
        s[strcspn(s, "\\n")] = 0;
        char *ptr = s;
        if (*ptr == '"') {
            ptr++;
            s[strlen(s)-1] = 0;
        }
        struct NestedInteger* res = deserialize(ptr);
        printNI(res);
        printf("\\n");
    }
    return 0;
}"""
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
