import json
import os

def generate_json():
    problem_id = 2667
    title = "Create Hello World Function"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>2667. Create Hello World Function</h3>
<p>Write a function <code>createHelloWorld</code>. It should return a new function that always returns <code>"Hello World"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> args = []
<strong>Output:</strong> "Hello World"
<strong>Explanation:</strong>
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> args = [{},null,42]
<strong>Output:</strong> "Hello World"
<strong>Explanation:</strong>
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= args.length &lt;= 10</code></li>
</ul>"""

    input_format = "An array of arguments (any type)."
    output_format = "The string 'Hello World'."
    
    constraints = [
        "0 <= args.length <= 10"
    ]
    
    explanation = """To solve this problem:
1. **Closure**: In JavaScript, a function can return another function. This is a basic demonstration of a closure.
2. **Arguments**: The returned function should accept any number of arguments (using rest parameters or simply ignoring the arguments) and return the static string `"Hello World"`.
3. **Implementation**:
```javascript
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};
```
4. **Complexity**:
   - **Time**: $O(1)$ to create and return the function.
   - **Space**: $O(1)$."""
    
    # Python equivalent for consistency in the platform
    answer = """def createHelloWorld():
    def f(*args, **kwargs):
        return "Hello World"
    return f"""

    boilerplate = {
        "python": "def createHelloWorld():\n    # implementation\n    pass\n\nif __name__ == '__main__':\n    f = createHelloWorld()\n    print(f())",
        "cpp": "#include <iostream>\n#include <string>\n#include <functional>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    // In C++, we return a lambda or std::function\n    function<string()> createHelloWorld() {\n        return []() { return \"Hello World\"; };\n    }\n};",
        "java": "import java.util.function.Supplier;\n\nclass Solution {\n    public Supplier<String> createHelloWorld() {\n        return () -> \"Hello World\";\n    }\n}",
        "javascript": "/**\n * @return {Function}\n */\nvar createHelloWorld = function() {\n    return function(...args) {\n        \n    }\n};",
        "c": "typedef char* (*func_ptr)();\n\nfunc_ptr createHelloWorld() {\n    \n}"
    }

    test_cases = [
        {"input": '{"args": []}', "expected_output": '"Hello World"', "is_sample": True},
        {"input": '{"args": [{}, null, 42]}', "expected_output": '"Hello World"', "is_sample": True},
        {"input": '{"args": [1, 2, 3]}', "expected_output": '"Hello World"', "is_sample": False},
        {"input": '{"args": ["a", "b"]}', "expected_output": '"Hello World"', "is_sample": False},
        {"input": '{"args": [true, false]}', "expected_output": '"Hello World"', "is_sample": False},
        {"input": '{"args": [[], {}]}', "expected_output": '"Hello World"', "is_sample": False},
        {"input": '{"args": [0]}', "expected_output": '"Hello World"', "is_sample": False},
        {"input": '{"args": [null]}', "expected_output": '"Hello World"', "is_sample": False},
        {"input": '{"args": [undefined]}', "expected_output": '"Hello World"', "is_sample": False}, # "undefined" string for compatibility
        {"input": '{"args": [NaN]}', "expected_output": '"Hello World"', "is_sample": False}
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
            "allowed_languages": ["javascript", "python"]
        },
        "topics": ["Closures", "Functions"],
        "companyIndex": 0
    }

    output_path = "2001-3000/2667_Create_Hello_World_Function.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
