import json
import os

def generate_json():
    problem_id = 1268
    title = "Search Suggestions System"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>1268. Search Suggestions System</h3>
<p>You are given an array of strings <code>products</code> and a string <code>searchWord</code>.</p>

<p>Design a system that suggests at most three product names from <code>products</code> after each character of <code>searchWord</code> is typed. Suggested products should have a common prefix with <code>searchWord</code>. If there are more than three products with a common prefix return the three lexicographically minimums products.</p>

<p>Return <em>a list of lists of the suggested products after each character of </em><code>searchWord</code><em> is typed</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
<strong>Output:</strong> [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
<strong>Explanation:</strong> products sorted: ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> products = ["havana"], searchWord = "havana"
<strong>Output:</strong> [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
<strong>Explanation:</strong> The only word "havana" will be always suggested while typing the search word.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= products.length &lt;= 1000</code></li>
	<li><code>1 &lt;= products[i].length &lt;= 3000</code></li>
	<li><code>1 &lt;= sum(products[i].length) &lt;= 2 * 10<sup>4</sup></code></li>
	<li>All the strings of <code>products</code> are <strong>unique</strong>.</li>
	<li><code>products[i]</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= searchWord.length &lt;= 1000</code></li>
	<li><code>searchWord</code> consists of lowercase English letters.</li>
</ul>"""

    input_format = "An integer n (number of products), followed by n strings (the products), and then the searchWord string."
    output_format = "A list of lists where each sublist contains the suggestions (strings) after typing each character."
    
    constraints = []
    
    explanation = """MEDIUM problem on ."""
    
    answer = """def suggestedProducts(products, searchWord):
    products.sort()
    res = []
    prefix = ""
    i = 0
    for c in searchWord:
        prefix += c
        i = bisect.bisect_left(products, prefix, lo=i)
        res.append([w for w in products[i : i + 3] if w.startswith(prefix)])
    return res"""

    boilerplate = {
        "python": "import sys\nimport bisect\n\ndef suggestedProducts(products, searchWord):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        n = int(data[0])\n        products = data[1:1+n]\n        searchWord = data[1+n]\n        print(suggestedProducts(products, searchWord))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\nint main() {\n    int n;\n    if(cin >> n) {\n        vector<string> products(n);\n        for(int i=0; i<n; i++) cin >> products[i];\n        string searchWord; cin >> searchWord;\n        // solve and print\n    }\n    return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if(sc.hasNextInt()) {\n            int n = sc.nextInt();\n            String[] products = new String[n];\n            for(int i=0; i<n; i++) products[i] = sc.next();\n            String searchWord = sc.next();\n            // solve and print\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\nconsole.log(\"[]\");",
        "c": "#include <stdio.h>\nint main() { printf(\"[]\\n\"); return 0; }"
    }

    test_cases = [
        {"input": "5 mobile mouse moneypot monitor mousepad mouse", "expected_output": "[[\"mobile\", \"moneypot\", \"monitor\"], [\"mobile\", \"moneypot\", \"monitor\"], [\"mouse\", \"mousepad\"], [\"mouse\", \"mousepad\"], [\"mouse\", \"mousepad\"]]", "is_sample": True},
        {"input": "1 havana havana", "expected_output": "[[\"havana\"], [\"havana\"], [\"havana\"], [\"havana\"], [\"havana\"], [\"havana\"]]", "is_sample": True},
        {"input": "5 bags baggage banner box cloths bags", "expected_output": "[[\"baggage\", \"bags\", \"banner\"], [\"baggage\", \"bags\", \"banner\"], [\"baggage\", \"bags\"], [\"bags\"]]", "is_sample": True},
        {"input": "1 taxi taxi", "expected_output": "[[\"taxi\"], [\"taxi\"], [\"taxi\"], [\"taxi\"]]", "is_sample": False},
        {"input": "3 a aa aaa aa", "expected_output": "[[\"a\", \"aa\", \"aaa\"], [\"aa\", \"aaa\"]]", "is_sample": False},
        {"input": "1 abc ab", "expected_output": "[[\"abc\"], [\"abc\"]]", "is_sample": False},
        {"input": "1 abc abcd", "expected_output": "[[\"abc\"], [\"abc\"], [\"abc\"], []]", "is_sample": False},
        {"input": "2 apple apply apply", "expected_output": "[[\"apple\", \"apply\"], [\"apple\", \"apply\"], [\"apple\", \"apply\"], [\"apple\", \"apply\"], [\"apply\"]]", "is_sample": False},
        {"input": "1 hello world", "expected_output": "[[], [], [], [], []]", "is_sample": False},
        {"input": "2 ab abc a", "expected_output": "[[\"ab\", \"abc\"]]", "is_sample": False}
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
        "topics": [],
        "companyIndex": 0
    }

    output_path = ""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
