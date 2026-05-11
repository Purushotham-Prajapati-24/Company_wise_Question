import json
import os

def generate_json():
    problem_id = 341
    title = "Flatten Nested List Iterator"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>341. Flatten Nested List Iterator</h3>
<p>You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.</p>

<p>Implement the <code>NestedIterator</code> class:</p>

<ul>
	<li><code>NestedIterator(List&lt;NestedInteger&gt; nestedList)</code> Initializes the iterator with the nested list <code>nestedList</code>.</li>
	<li><code>int next()</code> Returns the next integer in the nested list.</li>
	<li><code>boolean hasNext()</code> Returns <code>true</code> if there are still some integers in the nested list, and <code>false</code> otherwise.</li>
</ul>

<p>Your code will be tested with the following pseudocode:</p>

<pre>
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to res
return res
</pre>

<p>If <code>res</code> matches the expected flattened list, then your code will be judged as correct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nestedList = [[1,1],2,[1,1]]
<strong>Output:</strong> [1,1,2,1,1]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nestedList = [1,[4,[6]]]
<strong>Output:</strong> [1,4,6]
<strong>Explanation:</strong> By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nestedList.length &lt;= 500</code></li>
	<li>The values of the integers in the nested list are in the range <code>[-10<sup>6</sup>, 10<sup>6</sup>]</code>.</li>
</ul>"""

    input_format = "A recursive nested list of `NestedInteger` objects."
    output_format = "Flattened list of integers."
    
    constraints = [
        "1 <= nestedList.length <= 500",
        "Values in range [-10^6, 10^6]"
    ]
    
    explanation = """To implement the `NestedIterator`, the most efficient approach is to use a **Stack** to store the nested lists and integers lazily. This ensures we don't need to flatten the entire list upfront (useful for very deep/large lists).

### Algorithm Steps:
1. **Initialize**: 
   - Store the initial `nestedList` in a stack in reverse order so that we can pop elements from the end in $O(1)$ while maintaining the original sequence.
2. **`hasNext()`**:
   - The key logic resides here. We want `hasNext` to always leave the top of the stack as an integer or return `false` if empty.
   - While the top of the stack is not an integer:
     - Pop the top object (which must be a list).
     - Push the elements of the popped list back onto the stack in **reverse order**.
   - If the stack is empty after processing, return `false`. Otherwise, the top element is guaranteed to be an integer. Return `true`.
3. **`next()`**:
   - Always call `hasNext()` first to ensure the top element is an integer.
   - Pop the top element and return its integer value.

### Complexity Analysis:
- **Time Complexity**:
  - `Constructor`: $O(N)$, where $N$ is the number of elements in the top-level list.
  - `hasNext()`: $O(1)$ amortized. Each nested element is pushed and popped exactly once across all calls.
  - `next()`: $O(1)$ assuming `hasNext()` has been called.
- **Space Complexity**: $O(D)$, where $D$ is the maximum depth of nesting, plus the total number of elements in the stack at any given time."""
    
    answer = """class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Store in reverse order to pop efficiently from the end
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        # Based on hasNext() logic, top must be an integer
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # If top is a list, pop it and expand its items back onto stack
            self.stack.pop()
            # Push all elements of the list in reverse order
            self.stack.extend(top.getList()[::-1])
        return False"""

    boilerplate = {
        "python": "import sys\nimport json\nimport re\n\nclass NestedInteger:\n    def __init__(self, val): self.val = val\n    def isInteger(self) -> bool: return isinstance(self.val, int)\n    def getInteger(self) -> int: return self.val if self.isInteger() else None\n    def getList(self) -> list: return self.val if not self.isInteger() else None\n\nclass NestedIterator:\n    def __init__(self, nestedList: [NestedInteger]):\n        # User logic here\n        pass\n\n    def next(self) -> int: \n        # User logic here\n        pass\n\n    def hasNext(self) -> bool:\n        # User logic here\n        pass\n\ndef parse_nested(data):\n    res = []\n    for item in data: res.append(NestedInteger(parse_nested(item)) if isinstance(item, list) else NestedInteger(item))\n    return res\n\nif __name__ == '__main__':\n    input_data = sys.stdin.read().strip()\n    match = re.search(r'\\[.*\\]', input_data, re.DOTALL)\n    if match:\n        data = json.loads(match.group())\n        nestedList = parse_nested(data)\n        it = NestedIterator(nestedList)\n        res = []\n        while it.hasNext(): res.append(it.next())\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <stack>\n#include <algorithm>\n#include <regex>\nusing namespace std;\n\nclass NestedInteger {\npublic:\n    bool isInt; int val; vector<NestedInteger> list;\n    NestedInteger(int v) : isInt(true), val(v) {}\n    NestedInteger(vector<NestedInteger> l) : isInt(false), list(l) {}\n    bool isInteger() const { return isInt; }\n    int getInteger() const { return val; }\n    const vector<NestedInteger>& getList() const { return list; }\n};\n\nclass NestedIterator {\npublic:\n    NestedIterator(vector<NestedInteger> &nestedList) {\n        // User logic here\n    }\n\n    int next() {\n        // User logic here\n        return 0;\n    }\n\n    bool hasNext() {\n        // User logic here\n        return false;\n    }\n};\n\nvector<NestedInteger> parse_cpp(string& s, int& i) {\n    vector<NestedInteger> res; while (i < s.length()) {\n        if (s[i] == '[') { i++; res.push_back(NestedInteger(parse_cpp(s, i))); }\n        else if (s[i] == ']') { i++; return res; }\n        else if (isdigit(s[i]) || s[i] == '-') {\n            int start = i; if (s[i] == '-') i++; while (i < s.length() && isdigit(s[i])) i++;\n            res.push_back(NestedInteger(stoi(s.substr(start, i - start))));\n        } else i++;\n    } return res;\n}\n\nint main() {\n    string input((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    regex re(R\"(\\[.*\\])\"); smatch m;\n    if (regex_search(input, m, re)) {\n        string s = m.str(); int i = 1; vector<NestedInteger> nl = parse_cpp(s, i);\n        NestedIterator it(nl); cout << \"[\"; bool first = true;\n        while (it.hasNext()) { if (!first) cout << \",\"; cout << it.next(); first = false; }\n        cout << \"]\" << endl;\n    } return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\ninterface NestedInteger { boolean isInteger(); Integer getInteger(); List<NestedInteger> getList(); }\n\nclass NestedIntegerImpl implements NestedInteger {\n    private Integer val; private List<NestedInteger> list;\n    public NestedIntegerImpl(int val) { this.val = val; }\n    public NestedIntegerImpl(List<NestedInteger> list) { this.list = list; }\n    public boolean isInteger() { return val != null; }\n    public Integer getInteger() { return val; }\n    public List<NestedInteger> getList() { return list; }\n}\n\npublic class Solution implements Iterator<Integer> {\n    public Solution(List<NestedInteger> nestedList) {\n        // User logic here\n    }\n\n    @Override public Integer next() {\n        // User logic here\n        return 0;\n    }\n\n    @Override public boolean hasNext() {\n        // User logic here\n        return false;\n    }\n\n    private static List<NestedInteger> parse(String s, int[] pos) {\n        List<NestedInteger> res = new ArrayList<>();\n        while (pos[0] < s.length()) {\n            char c = s.charAt(pos[0]);\n            if (c == '[') { pos[0]++; res.add(new NestedIntegerImpl(parse(s, pos))); }\n            else if (c == ']') { pos[0]++; return res; }\n            else if (Character.isDigit(c) || c == '-') {\n                int start = pos[0]; if (c == '-') pos[0]++;\n                while (pos[0] < s.length() && Character.isDigit(s.charAt(pos[0]))) pos[0]++;\n                res.add(new NestedIntegerImpl(Integer.parseInt(s.substring(start, pos[0]))));\n            } else pos[0]++;\n        } return res;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\");\n        String input = sc.hasNext() ? sc.next() : \"\";\n        Matcher m = Pattern.compile(\"\\\\[.*\\\\]\", Pattern.DOTALL).matcher(input);\n        if (m.find()) {\n            int[] pos = {1}; List<NestedInteger> nl = parse(m.group(), pos);\n            Solution it = new Solution(nl);\n            StringBuilder sb = new StringBuilder(\"[\");\n            while (it.hasNext()) { sb.append(it.next()); if (it.hasNext()) sb.append(\",\"); }\n            sb.append(\"]\"); System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "\"use strict\";\n\nconst fs = require('fs');\n\nvar NestedIterator = function(nestedList) {\n    // User logic here\n};\n\nNestedIterator.prototype.hasNext = function() {\n    // User logic here\n};\n\nNestedIterator.prototype.next = function() {\n    // User logic here\n};\n\nfunction main() {\n    const input = fs.readFileSync(0, 'utf8');\n    const match = input.match(/\\[.*\\]/s);\n    if (match) {\n        const data = JSON.parse(match[0]);\n        function wrap(d) { return d.map(x => ({ isInteger: () => !Array.isArray(x), getInteger: () => Array.isArray(x) ? null : x, getList: () => Array.isArray(x) ? wrap(x) : null })); }\n        const it = new NestedIterator(wrap(data));\n        const res = [];\n        while (it.hasNext()) res.push(it.next());\n        console.log(JSON.stringify(res).replace(/ /g, ''));\n    }\n}\n\nmain();",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <ctype.h>\n#include <string.h>\n\nstruct NestedInteger { bool isInt; int val; struct NestedInteger** list; int listSize; };\nstruct NestedIterator { int dummy; };\n\nstruct NestedIterator* nestedIteratorCreate(struct NestedInteger** nestedList, int nestedListSize) {\n    // User logic here\n    return NULL;\n}\n\nbool nestedIteratorHasNext(struct NestedIterator *iter) {\n    // User logic here\n    return false;\n}\n\nint nestedIteratorNext(struct NestedIterator *iter) {\n    // User logic here\n    return 0;\n}\n\nstruct NestedInteger* parse_c(char* s, int* i) {\n    struct NestedInteger* ni = (struct NestedInteger*)malloc(sizeof(struct NestedInteger));\n    if (s[*i] == '[') {\n        (*i)++; ni->isInt = false; ni->list = NULL; ni->listSize = 0;\n        while (s[*i] != ']' && s[*i] != '\\0') {\n            if (s[*i] == '[' || isdigit(s[*i]) || s[*i] == '-') {\n                ni->list = (struct NestedInteger**)realloc(ni->list, (ni->listSize + 1) * sizeof(struct NestedInteger*));\n                ni->list[ni->listSize++] = parse_c(s, i);\n            } else (*i)++;\n        } if (s[*i] == ']') (*i)++;\n    } else {\n        int start = *i; if (s[*i] == '-') (*i)++; while (isdigit(s[*i])) (*i)++;\n        char temp[32]; strncpy(temp, s + start, *i - start); temp[*i - start] = '\\0';\n        ni->isInt = true; ni->val = atoi(temp);\n    } return ni;\n}\n\nint main() {\n    static char buffer[1000000];\n    int len = fread(buffer, 1, 999999, stdin); buffer[len] = '\\0';\n    char* start = strchr(buffer, '[');\n    if (start) {\n        int i = 0; struct NestedInteger* root = parse_c(start, &i);\n        struct NestedIterator* it = nestedIteratorCreate(root->list, root->listSize);\n        printf(\"[\"); bool first = true;\n        while (nestedIteratorHasNext(it)) { if (!first) printf(\",\"); printf(\"%d\", nestedIteratorNext(it)); first = false; }\n        printf(\"]\\n\");\n    } return 0;\n}"
    }

    test_cases = [
        {"input": "[[1,1],2,[1,1]]", "expected_output": "[1,1,2,1,1]", "is_sample": True},
        {"input": "[1,[4,[6]]]", "expected_output": "[1,4,6]", "is_sample": True},
        {"input": "[]", "expected_output": "[]", "is_sample": False},
        {"input": "[[]]", "expected_output": "[]", "is_sample": False},
        {"input": "[[[]]]", "expected_output": "[]", "is_sample": False},
        {"input": "[1, [2, [3, [4, [5]]]]]", "expected_output": "[1,2,3,4,5]", "is_sample": False},
        {"input": "[[1], [2], [3]]", "expected_output": "[1,2,3]", "is_sample": False},
                # Stress cases
        {"input": "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]", "expected_output": "[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199]", "is_sample": False},
        {"input": "[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99], [100], [101], [102], [103], [104], [105], [106], [107], [108], [109], [110], [111], [112], [113], [114], [115], [116], [117], [118], [119], [120], [121], [122], [123], [124], [125], [126], [127], [128], [129], [130], [131], [132], [133], [134], [135], [136], [137], [138], [139], [140], [141], [142], [143], [144], [145], [146], [147], [148], [149], [150], [151], [152], [153], [154], [155], [156], [157], [158], [159], [160], [161], [162], [163], [164], [165], [166], [167], [168], [169], [170], [171], [172], [173], [174], [175], [176], [177], [178], [179], [180], [181], [182], [183], [184], [185], [186], [187], [188], [189], [190], [191], [192], [193], [194], [195], [196], [197], [198], [199]]", "expected_output": "[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199]", "is_sample": False},
        {"input": "[[[0]], [[1]], [[2]], [[3]], [[4]], [[5]], [[6]], [[7]], [[8]], [[9]], [[10]], [[11]], [[12]], [[13]], [[14]], [[15]], [[16]], [[17]], [[18]], [[19]], [[20]], [[21]], [[22]], [[23]], [[24]], [[25]], [[26]], [[27]], [[28]], [[29]], [[30]], [[31]], [[32]], [[33]], [[34]], [[35]], [[36]], [[37]], [[38]], [[39]], [[40]], [[41]], [[42]], [[43]], [[44]], [[45]], [[46]], [[47]], [[48]], [[49]], [[50]], [[51]], [[52]], [[53]], [[54]], [[55]], [[56]], [[57]], [[58]], [[59]], [[60]], [[61]], [[62]], [[63]], [[64]], [[65]], [[66]], [[67]], [[68]], [[69]], [[70]], [[71]], [[72]], [[73]], [[74]], [[75]], [[76]], [[77]], [[78]], [[79]], [[80]], [[81]], [[82]], [[83]], [[84]], [[85]], [[86]], [[87]], [[88]], [[89]], [[90]], [[91]], [[92]], [[93]], [[94]], [[95]], [[96]], [[97]], [[98]], [[99]], [[100]], [[101]], [[102]], [[103]], [[104]], [[105]], [[106]], [[107]], [[108]], [[109]], [[110]], [[111]], [[112]], [[113]], [[114]], [[115]], [[116]], [[117]], [[118]], [[119]], [[120]], [[121]], [[122]], [[123]], [[124]], [[125]], [[126]], [[127]], [[128]], [[129]], [[130]], [[131]], [[132]], [[133]], [[134]], [[135]], [[136]], [[137]], [[138]], [[139]], [[140]], [[141]], [[142]], [[143]], [[144]], [[145]], [[146]], [[147]], [[148]], [[149]], [[150]], [[151]], [[152]], [[153]], [[154]], [[155]], [[156]], [[157]], [[158]], [[159]], [[160]], [[161]], [[162]], [[163]], [[164]], [[165]], [[166]], [[167]], [[168]], [[169]], [[170]], [[171]], [[172]], [[173]], [[174]], [[175]], [[176]], [[177]], [[178]], [[179]], [[180]], [[181]], [[182]], [[183]], [[184]], [[185]], [[186]], [[187]], [[188]], [[189]], [[190]], [[191]], [[192]], [[193]], [[194]], [[195]], [[196]], [[197]], [[198]], [[199]]]", "expected_output": "[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199]", "is_sample": False}
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
        "topics": ["Stack", "Tree", "Design", "Queue", "Iterator"],
        "companyIndex": 1
    }

    output_path = "301-500/341_Flatten_Nested_List_Iterator.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
