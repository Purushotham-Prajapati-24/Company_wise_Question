import json
import os

def generate_json():
    problem_id = 282
    title = "Expression Add Operators"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>282. Expression Add Operators</h3>
<p>Given a string <code>num</code> that contains only digits and an integer <code>target</code>, return <em>all possibilities to insert the binary operators </em><code>'+'</code><em>, </em><code>'-'</code><em>, and/or </em><code>'*'</code><em> between the digits of </em><code>num</code><em> so that the resultant expression evaluates to the </em><code>target</code><em> value</em>.</p>

<p>Note that operands in the returned expressions <strong>should not</strong> contain leading zeros.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> num = "123", target = 6
<strong>Output:</strong> ["1*2*3","1+2+3"]
<strong>Explanation:</strong> Both "1*2*3" and "1+2+3" evaluate to 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> num = "232", target = 8
<strong>Output:</strong> ["2*3+2","2+3*2"]
<strong>Explanation:</strong> Both "2*3+2" and "2+3*2" evaluate to 8.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> num = "3456237490", target = 9191
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no expressions that can be created from "3456237490" to evaluate to 9191.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= num.length &lt;= 10</code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "A string of digits `num` and an integer `target`."
    output_format = "A stringified array of all valid expressions."
    
    constraints = [
        "1 <= num.length <= 10",
        "num consists of only digits.",
        "-2^31 <= target <= 2^31 - 1"
    ]
    
    explanation = """To find all expressions that evaluate to a target:
1. **Backtracking (DFS)**: We explore every possible way to split the string and insert operators.
2. **Handle Precedence (Multiplication)**: To correctly evaluate expressions with `*` (which has higher precedence than `+` and `-`), we keep track of the `current_value` and the `previous_operand`.
   - If we add `+ val`, `current_value` becomes `current_value + val` and `previous_operand` is `val`.
   - If we add `- val`, `current_value` becomes `current_value - val` and `previous_operand` is `-val`.
   - If we add `* val`, we "undo" the previous operand's effect and apply multiplication: `current_value = (current_value - previous_operand) + (previous_operand * val)`. The new `previous_operand` is `previous_operand * val`.
3. **Leading Zero Check**: Operands like "05" are invalid. Any operand starting with '0' must be exactly '0'.
4. **Base Case**: When we reach the end of the string, if `current_value == target`, we found a valid expression.
5. **Complexity Analysis**:
   - Time: O(4^N) where N is the length of `num` (at each step, we have 4 choices: split, +, -, *). Given N <= 10, this is feasible.
   - Space: O(N) for the recursion stack."""
    
    answer = """class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index, prev_operand, current_val, expression):
            if index == len(num):
                if current_val == target:
                    res.append(expression)
                return
            
            for i in range(index, len(num)):
                # Leading zero check: "05" is invalid
                if i > index and num[index] == '0':
                    break
                    
                curr_str = num[index : i + 1]
                curr_val = int(curr_str)
                
                # If we are at the start of the string, just pick the first operand
                if index == 0:
                    backtrack(i + 1, curr_val, curr_val, curr_str)
                else:
                    # Try +, -, and *
                    backtrack(i + 1, curr_val, current_val + curr_val, expression + "+" + curr_str)
                    backtrack(i + 1, -curr_val, current_val - curr_val, expression + "-" + curr_str)
                    # For multiplication, undo the effect of the previous operand
                    backtrack(i + 1, prev_operand * curr_val, (current_val - prev_operand) + (prev_operand * curr_val), expression + "*" + curr_str)
        
        backtrack(0, 0, 0, "")
        return res"""

    boilerplate = {
        "python": "import sys\nimport re\nimport json\n\ndef addOperators(num: str, target: int) -> list[str]:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    num_match = re.search(r'num\\s*=\\s*\"([^\"]+)\"', raw_input)\n    if not num_match:\n        num_match = re.search(r'\"([^\"]+)\"', raw_input)\n    num = num_match.group(1) if num_match else \"\"\n    \n    target_match = re.search(r'target\\s*=\\s*(-?\\d+)', raw_input)\n    if not target_match:\n        # Find the last integer which is likely the target\n        nums = re.findall(r'-?\\d+', raw_input)\n        target = int(nums[-1]) if nums else 0\n    else:\n        target = int(target_match.group(1))\n        \n    result = addOperators(num, target)\n    result.sort()\n    print(json.dumps(result))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <algorithm>\n\nusing namespace std;\n\nvector<string> addOperators(string num, int target) {\n    // User logic here\n    return {};\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    regex re_num_str(R\"(\"([^\"]+)\")\");\n    smatch match_num;\n    string num = \"\";\n    if (regex_search(input, match_num, re_num_str)) num = match_num.str(1);\n    \n    regex re_target(R\"(target\\s*=\\s*(-?\\d+))\");\n    smatch match_target;\n    int target = 0;\n    if (regex_search(input, match_target, re_target)) {\n        target = stoi(match_target.str(1));\n    } else {\n        regex re_any_num(R\"(-?\\d+)\");\n        auto words_begin = sregex_iterator(input.begin(), input.end(), re_any_num);\n        auto words_end = sregex_iterator();\n        for (sregex_iterator i = words_begin; i != words_end; ++i) target = stoi(i->str());\n    }\n    \n    auto res = addOperators(num, target);\n    sort(res.begin(), res.end());\n    cout << \"[\";\n    for (int i = 0; i < (int)res.size(); i++) {\n        if (i) cout << \",\";\n        cout << \"\\\"\" << res[i] << \"\\\"\";\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public List<String> addOperators(String num, int target) {\n        // User logic here\n        return new ArrayList<>();\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (!sc.hasNext()) return;\n        String input = sc.next();\n        \n        String num = \"\";\n        Matcher mNum = Pattern.compile(\"\\\"([^\\\"]+)\\\"\").matcher(input);\n        if (mNum.find()) num = mNum.group(1);\n        \n        int target = 0;\n        Matcher mTarget = Pattern.compile(\"target\\\\s*=\\\\s*(-?\\\\d+)\").matcher(input);\n        if (mTarget.find()) {\n            target = Integer.parseInt(mTarget.group(1));\n        } else {\n            Matcher mAny = Pattern.compile(\"(-?\\\\d+)\").matcher(input);\n            while (mAny.find()) target = Integer.parseInt(mAny.group());\n        }\n        \n        List<String> res = new Solution().addOperators(num, target);\n        Collections.sort(res);\n        System.out.println(res);\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction addOperators(num, target) {\n    // User logic here\n    return [];\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nconst numMatch = input.match(/\"([^\"]+)\"/);\nconst num = numMatch ? numMatch[1] : \"\";\n\nconst targetMatch = input.match(/target\\s*=\\s*(-?\\d+)/);\nlet target = 0;\nif (targetMatch) {\n    target = parseInt(targetMatch[1]);\n} else {\n    const allNums = input.match(/-?\\d+/g);\n    if (allNums) target = parseInt(allNums[allNums.length - 1]);\n}\n\nconst res = addOperators(num, target);\nres.sort();\nconsole.log(JSON.stringify(res));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar** addOperators(char* num, int target, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\n\nint main() {\n    static char buffer[100000];\n    if (fread(buffer, 1, 99999, stdin) > 0) {\n        char num[100] = \"\";\n        int target = 0;\n        \n        char *q1 = strchr(buffer, '\"');\n        if (q1) {\n            char *q2 = strchr(q1 + 1, '\"');\n            if (q2) {\n                strncpy(num, q1 + 1, q2 - q1 - 1);\n                num[q2 - q1 - 1] = '\\0';\n            }\n        }\n        \n        char *t = strstr(buffer, \"target\");\n        if (t) {\n            while (*t && !isdigit(*t) && *t != '-') t++;\n            if (*t) target = atoi(t);\n        } else {\n            // Find last number\n            char *p = buffer + strlen(buffer) - 1;\n            while (p > buffer && !isdigit(*p)) p--;\n            while (p > buffer && (isdigit(*p) || *p == '-')) p--;\n            if (p >= buffer) target = atoi(p + 1);\n        }\n        \n        int retSize;\n        char** res = addOperators(num, target, &retSize);\n        printf(\"[\");\n        for (int i = 0; i < retSize; i++) {\n            if (i) printf(\",\");\n            printf(\"\\\"%s\\\"\", res[i]);\n        }\n        printf(\"]\\n\");\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": '"123"\\n6', "expected_output": '["1+2+3","1*2*3"]', "is_sample": True},
        {"input": '"232"\\n8', "expected_output": '["2+3*2","2*3+2"]', "is_sample": True},
        {"input": '"3456237490"\\n9191', "expected_output": "[]", "is_sample": True},
        {"input": '"105"\\n5', "expected_output": '["1*0+5","10-5"]', "is_sample": False},
        {"input": '"00"\\n0', "expected_output": '["0+0","0-0","0*0"]', "is_sample": False},
        {"input": '"2147483647"\\n2147483647', "expected_output": '["2147483647"]', "is_sample": False},
        {"input": '"1"\\n1', "expected_output": '["1"]', "is_sample": False},
        # Stress cases
        {"input": '"123456789"\\n45', "expected_output": '["1+2+3+4+5+6+7+8+9"]', "is_sample": False},
        {"input": '"999"\\n81', "expected_output": '["9*9"]', "is_sample": False},
        {"input": '"12345"\\n120', "expected_output": '["1*2*3*4*5"]', "is_sample": False}
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
        "topics": ["Math", "String", "Backtracking"],
        "companyIndex": 0
    }

    output_path = "201-400/282_Expression_Add_Operators.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
