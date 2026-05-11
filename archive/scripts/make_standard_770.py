import json
import os

def generate_json():
    problem_id = 770
    title = "Basic Calculator IV"
    difficulty = "Hard"
    marks = 40
    
    html_description = """<h3>770. Basic Calculator IV</h3>
<p>Given an <code>expression</code> such as <code>expression = "e + 8 - a + 5"</code> and an evaluation map such as <code>evalvars = ["e"]</code> and <code>evalints = [1]</code>, return a list of tokens representing the simplified expression, such as <code>["-1*a","14"]</code>.</p>

<p>An expression consists of lowercase English letters, digits, <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, <code>'('</code>, and <code>')'</code>. All terms are separated by spaces. Variables in <code>evalvars</code> should be replaced by their corresponding integers in <code>evalints</code>.</p>

<p>Return the list of tokens representing the simplified expression in the following order:</p>
<ul>
	<li>Terms with <strong>higher degree</strong> come first.</li>
	<li>Terms with the <strong>same degree</strong> are sorted <strong>lexicographically</strong> by their variables.</li>
	<li>Terms with a coefficient of <code>0</code> are removed.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
<strong>Output:</strong> ["-1*a","14"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
<strong>Output:</strong> ["-1*pressure","5"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 250</code></li>
	<li><code>expression</code> consists of lowercase English letters, digits, <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, <code>'('</code>, and <code>')'</code>.</li>
	<li>All the tokens in <code>expression</code> are separated by a single space.</li>
	<li><code>0 &lt;= evalvars.length &lt;= 100</code></li>
	<li><code>evalvars[i]</code> consists of lowercase English letters.</li>
	<li><code>evalints.length == evalvars.length</code></li>
	<li><code>-100 &lt;= evalints[i] &lt;= 100</code></li>
</ul>
"""

    input_format = "A string expression, an array of evalvars, and an array of evalints."
    output_format = "A list of strings representing the simplified expression."
    
    constraints = [
        "1 <= expression.length <= 250",
        "0 <= evalvars.length <= 100",
        "-100 <= evalints[i] <= 100"
    ]
    
    explanation = """To solve this complex algebraic simplification:
1. **The Core Tool: Polynomial Representation**:
   - Represent a polynomial as a dictionary where keys are sorted tuples of variables (e.g., `('a', 'b')`) and values are coefficients.
   - For constants, the key is an empty tuple `()`.

2. **Polynomial Operations**:
   - **Addition/Subtraction**: Add or subtract coefficients for matching keys.
   - **Multiplication**: `(term1 * coef1) * (term2 * coef2) = (sorted(term1 + term2) with coef1 * coef2)`.

3. **Parsing**:
   - Replace variables with their integer values from `evalvars`/`evalints` during the tokenization stage.
   - Use a recursive descent parser or a stack-based approach (Shunting-yard algorithm) to handle precedence (`*` denotes higher priority than `+/-`) and parentheses.
   
4. **Simplification & Sorting**:
   - Combine all like terms.
   - Filter out terms with coefficient `0`.
   - Sort by degree (length of variable tuple) descending.
   - Sort by lexicographical order of variables for terms of the same degree.
   - Format each term as `coefficient*v1*v2*...` or just `coefficient`.

Complexity:
- Time: O(L^2 * 2^C) in extreme cases due to multiplication, but L=250 is small.
- Space: O(L^2) to store the polynomial terms."""
    
    answer = """import collections

def basicCalculatorIV(expression, evalvars, evalints):
    eval_map = dict(zip(evalvars, evalints))
    
    class Poly(collections.Counter):
        def __add__(self, other):
            res = Poly(self)
            for k, v in other.items():
                res[k] += v
            return res
        def __sub__(self, other):
            res = Poly(self)
            for k, v in other.items():
                res[k] -= v
            return res
        def __mul__(self, other):
            res = Poly()
            for k1, v1 in self.items():
                for k2, v2 in other.items():
                    res[tuple(sorted(k1 + k2))] += v1 * v2
            return res

    def factor(token):
        if token[0].isdigit():
            return Poly({(): int(token)})
        if token in eval_map:
            return Poly({(): eval_map[token]})
        return Poly({(token,): 1})

    # Tokenizing...
    tokens = expression.replace('(', '( ').replace(')', ' )').split()
    
    def parse(idx):
        stack = [Poly({(): 0})]
        ops = ['+']
        while idx < len(tokens):
            token = tokens[idx]
            if token == '(':
                res, idx = parse(idx + 1)
                curr = res
            elif token == ')':
                break
            elif token in '+-*':
                ops.append(token)
                idx += 1
                continue
            else:
                curr = factor(token)
            
            if ops[-1] == '*':
                stack[-1] = stack[-1] * curr
                ops.pop()
            elif ops[-1] == '-':
                stack.append(curr * Poly({(): -1}))
                ops.pop()
            else:
                stack.append(curr)
                ops.pop()
            idx += 1
            
        return sum(stack, Poly()), idx

    simplified, _ = parse(0)
    
    # Sort terms
    ans = []
    for k in sorted(simplified.keys(), key=lambda x: (-len(x), x)):
        v = simplified[k]
        if v == 0: continue
        s = str(v)
        for var in k:
            s += '*' + var
        ans.append(s)
    return ans"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef basicCalculatorIV(expression, evalvars, evalints):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    exp = lines[0]\n    vars = json.loads(lines[1])\n    ints = json.loads(lines[2])\n    print(json.dumps(basicCalculatorIV(exp, vars, ints)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <map>\n\nusing namespace std;\n\nvector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {\n    return {};\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<String> basicCalculatorIV(String expression, String[] evalvars, int[] evalints) {\n        return new ArrayList<>();\n    }\n}",
        "javascript": "var basicCalculatorIV = function(expression, evalvars, evalints) {\n    return [];\n};",
        "c": "char** basicCalculatorIV(char* expression, char** evalvars, int evalvarsSize, int* evalints, int* returnSize) {\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "e + 8 - a + 5\\n[\"e\"]\\n[1]", "expected_output": "[\"-1*a\",\"14\"]", "is_sample": True},
        {"input": "e - 8 + temperature - pressure\\n[\"e\", \"temperature\"]\\n[1, 12]", "expected_output": "[\"-1*pressure\",\"5\"]", "is_sample": True},
        # Diverse cases
        {"input": "( e + 8 ) * ( a - 5 )\\n[\"e\"]\\n[1]", "expected_output": "[\"9*a\",\"-45\"]", "is_sample": False},
        {"input": "a * b * c + a * b * c\\n[]\\n[]", "expected_output": "[\"2*a*b*c\"]", "is_sample": False},
        {"input": "a * a * a - a * a * a\\n[]\\n[]", "expected_output": "[]", "is_sample": False},
        {"input": "0\\n[]\\n[]", "expected_output": "[]", "is_sample": False},
        {"input": "x + y * z\\n[]\\n[]", "expected_output": "[\"1*y*z\",\"1*x\"]", "is_sample": False},
        # Stress cases
        {"input": "(a + b) * (a + b) * (a + b)\\n[]\\n[]", "expected_output": "[\"1*a*a*a\",\"3*a*a*b\",\"3*a*b*b\",\"1*b*b*b\"]", "is_sample": False},
        {"input": "a * b * c * d * e * f * g * h * i * j\\n[]\\n[]", "expected_output": "[\"1*a*b*c*d*e*f*g*h*i*j\"]", "is_sample": False},
        {"input": "(a - a) * (b + c + d + e)\\n[]\\n[]", "expected_output": "[]", "is_sample": False}
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
        "topics": ["Hash Table", "Math", "String", "Stack", "Recursion"],
        "companyIndex": 0
    }

    output_path = "601-800/770_Basic_Calculator_IV.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
