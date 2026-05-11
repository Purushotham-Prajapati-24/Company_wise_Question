import json
import os

def generate_json():
    problem_id = 1472
    title = "Design Browser History"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1472. Design Browser History</h3>
<p>You have a <strong>browser</strong> of one tab where you start on the <code>homepage</code> and you can visit another <code>url</code>, get back in the history number of <code>steps</code> or move forward in the history number of <code>steps</code>.</p>

<p>Implement the <code>BrowserHistory</code> class:</p>

<ul>
	<li><code>BrowserHistory(string homepage)</code> Initializes the object with the <code>homepage</code>&nbsp;of the browser.</li>
	<li><code>void visit(string url)</code>&nbsp;Visits&nbsp;<code>url</code> from the current page. It clears up all the forward history.</li>
	<li><code>string back(int steps)</code>&nbsp;Move <code>steps</code> back in history. If you can only return <code>x</code> steps in the history and <code>steps &gt; x</code>, you will return only <code>x</code> steps. Return the current <code>url</code> after moving back in history <strong>at most</strong> <code>steps</code>.</li>
	<li><code>string forward(int steps)</code>&nbsp;Move <code>steps</code> forward in history. If you can only forward <code>x</code> steps in the history and <code>steps &gt; x</code>, you will forward only <code>x</code> steps. Return the current <code>url</code> after forwarding in history <strong>at most</strong> <code>steps</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<pre><strong>Input:</strong>
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
<strong>Output:</strong>
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

<strong>Explanation:</strong>
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= homepage.length &lt;= 20</code></li>
	<li><code>1 &lt;= url.length &lt;= 20</code></li>
	<li><code>1 &lt;= steps &lt;= 100</code></li>
	<li><code>homepage</code> and <code>url</code> consist of  '.' or lower case English letters.</li>
	<li>At most <code>5000</code>&nbsp;calls will be made to <code>visit</code>, <code>back</code>, and <code>forward</code>.</li>
</ul>"""

    input_format = "A list of method names and a list of arguments for each method."
    output_format = "A list of return values for each method."

    constraints = [
        "1 <= url.length <= 20",
        "1 <= steps <= 100",
        "At most 5000 calls"
    ]

    explanation = """To implement the BrowserHistory:
1. Use a list `history` and a pointer `curr`.
2. `visit`: Increment `curr`, truncate and append.
3. `back`: `curr = max(0, curr - steps)`, return `history[curr]`.
4. `forward`: `curr = min(len(history)-1, curr + steps)`, return `history[curr]`."""

    answer = """class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        self.history = self.history[:self.curr]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]"""

    boilerplate = {
        "python": """import sys
import json

class BrowserHistory:
    def __init__(self, homepage: str):
        pass
    def visit(self, url: str) -> None:
        pass
    def back(self, steps: int) -> str:
        return ""
    def forward(self, steps: int) -> str:
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().splitlines()
    if len(raw) >= 2:
        methods = json.loads(raw[0])
        arguments = json.loads(raw[1])
        obj = None
        results = []
        for m, a in zip(methods, arguments):
            if m == "BrowserHistory":
                obj = BrowserHistory(a[0])
                results.append(None)
            elif m == "visit":
                results.append(obj.visit(a[0]))
            elif m == "back":
                results.append(obj.back(a[0]))
            elif m == "forward":
                results.append(obj.forward(a[0]))
        print(json.dumps(results).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class BrowserHistory {
public:
    BrowserHistory(string homepage) {}
    void visit(string url) {}
    string back(int steps) { return ""; }
    string forward(int steps) { return ""; }
};

int main() {
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        json methods = json::parse(line1);
        json args = json::parse(line2);
        BrowserHistory* obj = nullptr;
        json results = json::array();
        for (size_t i = 0; i < methods.size(); ++i) {
            if (methods[i] == "BrowserHistory") {
                obj = new BrowserHistory(args[i][0]);
                results.push_back(nullptr);
            } else if (methods[i] == "visit") {
                obj->visit(args[i][0]);
                results.push_back(nullptr);
            } else if (methods[i] == "back") {
                results.push_back(obj->back(args[i][0]));
            } else if (methods[i] == "forward") {
                results.push_back(obj->forward(args[i][0]));
            }
        }
        cout << results.dump() << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;

class BrowserHistory {
    public BrowserHistory(String homepage) {}
    public void visit(String url) {}
    public String back(int steps) { return ""; }
    public String forward(int steps) { return ""; }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            ObjectMapper mapper = new ObjectMapper();
            String[] methods = mapper.readValue(sc.nextLine(), String[].class);
            Object[][] argArr = mapper.readValue(sc.nextLine(), Object[][].class);
            BrowserHistory obj = null;
            List<Object> results = new ArrayList<>();
            for (int i = 0; i < methods.length; i++) {
                if (methods[i].equals("BrowserHistory")) {
                    obj = new BrowserHistory((String)argArr[i][0]);
                    results.add(null);
                } else if (methods[i].equals("visit")) {
                    obj.visit((String)argArr[i][0]);
                    results.add(null);
                } else if (methods[i].equals("back")) {
                    results.add(obj.back((Integer)argArr[i][0]));
                } else if (methods[i].equals("forward")) {
                    results.add(obj.forward((Integer)argArr[i][0]));
                }
            }
            System.out.println(mapper.writeValueAsString(results).replace(" ", ""));
        }
    }
}""",
        "javascript": """var BrowserHistory = function(homepage) {
    
};
BrowserHistory.prototype.visit = function(url) {};
BrowserHistory.prototype.back = function(steps) {};
BrowserHistory.prototype.forward = function(steps) {};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\\n');
if (input.length >= 2) {
    const methods = JSON.parse(input[0]);
    const args = JSON.parse(input[1]);
    let obj = null;
    let results = [];
    for (let i = 0; i < methods.length; i++) {
        if (methods[i] === "BrowserHistory") {
            obj = new BrowserHistory(args[i][0]);
            results.push(null);
        } else if (methods[i] === "visit") {
            obj.visit(args[i][0]);
            results.push(null);
        } else if (methods[i] === "back") {
            results.push(obj.back(args[i][0]));
        } else if (methods[i] === "forward") {
            results.push(obj.forward(args[i][0]));
        }
    }
    console.log(JSON.stringify(results).replace(/ /g, ""));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char** history;
    int curr;
    int size;
    int cap;
} BrowserHistory;

BrowserHistory* browserHistoryCreate(char * homepage) {
    BrowserHistory* obj = malloc(sizeof(BrowserHistory));
    obj->cap = 10;
    obj->history = malloc(sizeof(char*) * obj->cap);
    obj->history[0] = strdup(homepage);
    obj->curr = 0;
    obj->size = 1;
    return obj;
}

void browserHistoryVisit(BrowserHistory* obj, char * url) {
    obj->curr++;
    for (int i = obj->curr; i < obj->size; i++) free(obj->history[i]);
    if (obj->curr >= obj->cap) {
        obj->cap *= 2;
        obj->history = realloc(obj->history, sizeof(char*) * obj->cap);
    }
    obj->history[obj->curr] = strdup(url);
    obj->size = obj->curr + 1;
}

char * browserHistoryBack(BrowserHistory* obj, int steps) {
    obj->curr = (obj->curr - steps < 0) ? 0 : obj->curr - steps;
    return obj->history[obj->curr];
}

char * browserHistoryForward(BrowserHistory* obj, int steps) {
    obj->curr = (obj->curr + steps >= obj->size) ? obj->size - 1 : obj->curr + steps;
    return obj->history[obj->curr];
}

void browserHistoryFree(BrowserHistory* obj) {
    for (int i = 0; i < obj->size; i++) free(obj->history[i]);
    free(obj->history);
    free(obj);
}

// Robust JSON String Parser for Boilerplate
char* read_json_string() {
    int c;
    while ((c = getchar()) != EOF && c != '"');
    if (c == EOF) return NULL;
    int cap = 128, len = 0;
    char* s = malloc(cap);
    while ((c = getchar()) != EOF && c != '"') {
        if (len + 1 >= cap) { cap *= 2; s = realloc(s, cap); }
        s[len++] = c;
    }
    s[len] = '\\0';
    return s;
}

// Robust JSON Int Parser
int read_json_int() {
    int val;
    while (scanf("%d", &val) != 1) {
        int c = getchar();
        if (c == EOF) return 0;
    }
    return val;
}

int main() {
    // Boilerplate for method sequence parsing
    // Line 1: ["BrowserHistory","visit",...]
    // Line 2: [["homepage"],["url1"],...]
    
    // Implementation of main with actual calling logic
    char* methods[5005];
    int m_count = 0;
    int c;
    while ((c = getchar()) != EOF && c != '[');
    while (1) {
        char* m = read_json_string();
        if (!m) break;
        methods[m_count++] = m;
        while ((c = getchar()) != EOF && c != ',' && c != ']');
        if (c == ']' || c == EOF) break;
    }
    
    while ((c = getchar()) != EOF && c != '[');
    printf("[");
    BrowserHistory* obj = NULL;
    for (int i = 0; i < m_count; i++) {
        while ((c = getchar()) != EOF && c != '[');
        if (strcmp(methods[i], "BrowserHistory") == 0) {
            char* h = read_json_string();
            obj = browserHistoryCreate(h);
            printf("null"); free(h);
        } else if (strcmp(methods[i], "visit") == 0) {
            char* u = read_json_string();
            browserHistoryVisit(obj, u);
            printf("null"); free(u);
        } else if (strcmp(methods[i], "back") == 0) {
            int s = read_json_int();
            printf("\\"%s\\"", browserHistoryBack(obj, s));
        } else if (strcmp(methods[i], "forward") == 0) {
            int s = read_json_int();
            printf("\\"%s\\"", browserHistoryForward(obj, s));
        }
        while ((c = getchar()) != EOF && c != ']');
        if (i < m_count - 1) printf(",");
        free(methods[i]);
    }
    printf("]\\n");
    if (obj) browserHistoryFree(obj);
    return 0;
}"""
    }

    def solve(methods, args):
        h = [args[0][0]]
        curr = 0
        limit = 0
        results = [None]
        for m, a in zip(methods[1:], args[1:]):
            if m == "visit":
                curr += 1
                if curr >= len(h): h.append(a[0])
                else: h[curr] = a[0]
                limit = curr
                results.append(None)
            elif m == "back":
                curr = max(0, curr - a[0])
                results.append(h[curr])
            elif m == "forward":
                curr = min(limit, curr + a[0])
                results.append(h[curr])
        return results

    test_cases_data = [
        [["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"], [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]], # Sample 1
        [["BrowserHistory", "visit", "back", "forward"], [["a.com"], ["b.com"], [1], [1]]],
        [["BrowserHistory", "back", "forward"], [["h.com"], [1], [1]]],
        [["BrowserHistory", "visit", "visit"], [["a"], ["b"], ["c"]]],
        [["BrowserHistory", "visit", "back", "visit", "back"], [["a"], ["b"], [1], ["c"], [1]]],
        [["BrowserHistory", "visit", "visit", "visit", "back", "back", "back", "back"], [["a"], ["b"], ["c"], ["d"], [1], [1], [1], [1]]],
        [["BrowserHistory", "visit", "visit", "forward"], [["a"], ["b"], ["c"], [1]]],
        [["BrowserHistory", "visit", "visit", "visit", "back", "visit", "forward"], [["a"], ["b"], ["c"], ["d"], [2], ["e"], [1]]],
        [["BrowserHistory", "back", "forward", "back", "forward"], [["h"], [0], [0], [1], [1]]],
        [["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "forward", "back", "back", "forward", "forward"], [["a"],["b"],["c"],["d"],[1],[1],[1],[1],[2],[2],[2],[2]]]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t[0]).replace(" ", "") + "\\n" + json.dumps(t[1]).replace(" ", "")
        out = json.dumps(solve(t[0], t[1])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Linked List", "Stack", "Design", "Doubly-Linked List", "Data Stream"], "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
