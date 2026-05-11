import json
import os


def generate_json():
    problem_id = 269
    title = "Alien Dictionary"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>269. Alien Dictionary</h3>
<p>There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.</p>

<p>You are given a list of strings <code>words</code> from the alien language's dictionary, where the strings in <code>words</code> are <strong>sorted lexicographically</strong> by the rules of this new language.</p>

<p>Return <em>a string of the unique letters in the new alien language sorted in <strong>lexicographically increasing order</strong> by the new language's rules. If there is no solution, return </em><code>""</code><em>. If there are multiple solutions, return <strong>any of them</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["wrt","wrf","er","ett","rftt"]
<strong>Output:</strong> "wertf"</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["z","x"]
<strong>Output:</strong> "zx"</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["z","x","z"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> The order is invalid, so return "".</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
</ul>"""

    input_format = "A list of space-separated strings representing the dictionary."
    output_format = "A string representing the character order, or an empty string if invalid."
    
    constraints = []
    
    explanation = """HARD problem on ."""
    
    answer = """import collections

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = collections.defaultdict(set)
        in_degree = {c: 0 for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return "" # Invalid prefix
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
                    
        queue = collections.deque([c for c in in_degree if in_degree[c] == 0])
        res = []
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        if len(res) < len(in_degree):
            return "" # Cycle detected
        return "".join(res)"""

    boilerplate = {
        "python": "import sys\nimport re\n\ndef alienOrder(words: list[str]) -> str:\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read()\n    # Lethal parsing: extract all strings between quotes\n    words = re.findall(r'\"([^\"]+)\"', raw_input)\n    if not words:\n        words = raw_input.strip().split()\n        # Filter out labels\n        words = [w for w in words if w not in ['words', '=']]\n    \n    print(alienOrder(words))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n\nusing namespace std;\n\nstring alienOrder(vector<string>& words) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    string input;\n    char ch;\n    while (cin.get(ch)) input += ch;\n    \n    vector<string> words;\n    regex re_str(R\"(\"([^\"]+)\")\");\n    smatch match;\n    string::const_iterator searchStart(input.cbegin());\n    while (regex_search(searchStart, input.cend(), match, re_str)) {\n        words.push_back(match[1]);\n        searchStart = match.suffix().first;\n    }\n    \n    if (words.empty()) {\n        // Fallback to space-separated\n        regex re_word(R\"(\\b[a-z]+\\b)\");\n        searchStart = input.cbegin();\n        while (regex_search(searchStart, input.cend(), match, re_word)) {\n            string w = match[0];\n            if (w != \"words\") words.push_back(w);\n            searchStart = match.suffix().first;\n        }\n    }\n\n    cout << alienOrder(words) << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    public String alienOrder(String[] words) {\n        // User logic here\n        return \"\";\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        if (sc.hasNext()) {\n            String input = sc.next();\n            List<String> list = new ArrayList<>();\n            Matcher m = Pattern.compile(\"\\\"([^\\\"]+)\\\"\").matcher(input);\n            while (m.find()) {\n                list.add(m.group(1));\n            }\n            if (list.isEmpty()) {\n                String[] parts = input.trim().split(\"\\\\s+\");\n                for (String p : parts) if (!p.equals(\"words\") && !p.equals(\"=\")) list.add(p);\n            }\n            System.out.println(new Solution().alienOrder(list.toArray(new String[0])));\n        }\n    }\n}",
        "javascript": "const fs = require('fs');\n\nfunction alienOrder(words) {\n    // User logic here\n    return \"\";\n}\n\nconst input = fs.readFileSync(0, 'utf-8');\nlet words = (input.match(/\"([^\"]+)\"/g) || []).map(s => s.replace(/\"/g, ''));\nif (words.length === 0) {\n    words = input.trim().split(/\\s+/).filter(w => w !== 'words' && w !== '=');\n}\n\nconsole.log(alienOrder(words));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\nchar* alienOrder(char** words, int wordsSize) {\n    // User logic here\n    return \"\";\n}\n\nint main() {\n    static char buffer[1000000];\n    char** words = malloc(1000 * sizeof(char*));\n    int size = 0;\n    \n    if (fread(buffer, 1, 999999, stdin) > 0) {\n        char *p = buffer;\n        while (*p) {\n            if (*p == '\"') {\n                char *start = p + 1;\n                char *end = strchr(start, '\"');\n                if (end) {\n                    int len = end - start;\n                    words[size] = malloc(len + 1);\n                    strncpy(words[size], start, len);\n                    words[size][len] = '\\0';\n                    size++;\n                    p = end + 1;\n                    continue;\n                }\n            }\n            p++;\n        }\n        \n        if (size == 0) {\n            // Fallback to space split\n            char *token = strtok(buffer, \" \\t\\n\\r[]=\");\n            while (token) {\n                if (strcmp(token, \"words\") != 0) {\n                    words[size++] = strdup(token);\n                }\n                token = strtok(NULL, \" \\t\\n\\r[]=\");\n            }\n        }\n    }\n    \n    char* res = alienOrder(words, size);\n    printf(\"%s\\n\", res ? res : \"\");\n    return 0;\n}"
    }

    test_cases = [{"input": "wrt wrf er ett rftt", "expected_output": "wertf", "is_sample": True},
        {"input": "z x", "expected_output": "zx", "is_sample": True},
        {"input": "z x z", "expected_output": "", "is_sample": True},
        {"input": "abc ab", "expected_output": "", "is_sample": False}, # Invalid prefix
        {"input": "a b c", "expected_output": "abc", "is_sample": False},
        {"input": "z z", "expected_output": "z", "is_sample": False},
        {"input": "ab ac", "expected_output": "abc", "is_sample": False}, # b < c, a is first
        {"input": "zy zx", "expected_output": "yxz", "is_sample": False}, # y < x
        {"input": "wrt wrf er ett rftt", "expected_output": "wertf", "is_sample": False},
        {"input": "ri h i", "expected_output": "rih", "is_sample": False}]

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
        "topics": ["Array", "String", "Depth-First Search", "Breadth-First Search", "Graph", "Topological Sort"],
        "companyIndex": 0
    }

    output_path = ""
    if not output_path or output_path == "":
        output_path = f"CompanyQuestion/STANDARD/{problem_id}_{title.replace(' ', '_')}.json"
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
