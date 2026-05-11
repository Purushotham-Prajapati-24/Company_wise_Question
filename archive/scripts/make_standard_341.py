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
        "python": "import sys\nimport json\n\n# Interface provided by the platform\nclass NestedInteger:\n    def __init__(self, val):\n        self.val = val\n    def isInteger(self) -> bool:\n        return isinstance(self.val, int)\n    def getInteger(self) -> int:\n        return self.val if self.isInteger() else None\n    def getList(self) -> list:\n        return self.val if not self.isInteger() else None\n\nclass NestedIterator:\n    def __init__(self, nestedList):\n        # Your logic here\n        pass\n    \n    def next(self) -> int:\n        # Your logic here\n        pass\n    \n    def hasNext(self) -> bool:\n        # Your logic here\n        pass\n\ndef parse_nested(data):\n    res = []\n    for item in data:\n        if isinstance(item, list):\n            res.append(NestedInteger(parse_nested(item)))\n        else:\n            res.append(NestedInteger(item))\n    return res\n\nif __name__ == '__main__':\n    raw_input = sys.stdin.read().strip()\n    if raw_input:\n        data = json.loads(raw_input)\n        nestedList = parse_nested(data)\n        iter = NestedIterator(nestedList)\n        res = []\n        while iter.hasNext():\n            res.append(iter.next())\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <stack>\n#include <algorithm>\nusing namespace std;\n\n// Interface\nclass NestedInteger {\npublic:\n    bool isInt;\n    int val;\n    vector<NestedInteger> list;\n    NestedInteger(int v) : isInt(true), val(v) {}\n    NestedInteger(vector<NestedInteger> l) : isInt(false), list(l) {}\n    bool isInteger() const { return isInt; }\n    int getInteger() const { return val; }\n    const vector<NestedInteger>& getList() const { return list; }\n};\n\nclass NestedIterator {\npublic:\n    NestedIterator(vector<NestedInteger> &nestedList) {\n        // Your logic here\n    }\n    \n    int next() {\n        // Your logic here\n        return 0;\n    }\n    \n    bool hasNext() {\n        // Your logic here\n        return false;\n    }\n};\n\n// Minimal JSON-like parser for nesting\nvector<NestedInteger> parse(string& s, int& i) {\n    vector<NestedInteger> res;\n    while (i < s.length()) {\n        if (s[i] == '[') {\n            i++;\n            res.push_back(NestedInteger(parse(s, i)));\n        } else if (s[i] == ']') {\n            i++;\n            return res;\n        } else if (isdigit(s[i]) || s[i] == '-') {\n            int start = i;\n            if (s[i] == '-') i++;\n            while (i < s.length() && isdigit(s[i])) i++;\n            res.push_back(NestedInteger(stoi(s.substr(start, i - start))));\n        } else {\n            i++;\n        }\n    }\n    return res;\n}\n\nint main() {\n    string line;\n    if (getline(cin, line)) {\n        int i = 0;\n        if (line[0] == '[') i++;\n        vector<NestedInteger> nl = parse(line, i);\n        NestedIterator it(nl);\n        cout << \"[\";\n        bool first = true;\n        while (it.hasNext()) {\n            if (!first) cout << \",\";\n            cout << it.next();\n            first = false;\n        }\n        cout << \"]\\n\";\n    }\n    return 0;\n}",
        "java": "import java.util.*;\n\ninterface NestedInteger {\n    public boolean isInteger();\n    public Integer getInteger();\n    public List<NestedInteger> getList();\n}\n\nclass NestedIntegerImpl implements NestedInteger {\n    private Integer val;\n    private List<NestedInteger> list;\n    public NestedIntegerImpl(int val) { this.val = val; }\n    public NestedIntegerImpl(List<NestedInteger> list) { this.list = list; }\n    public boolean isInteger() { return val != null; }\n    public Integer getInteger() { return val; }\n    public List<NestedInteger> getList() { return list; }\n}\n\npublic class Solution implements Iterator<Integer> {\n    public Solution(List<NestedInteger> nestedList) {\n        // Your logic here\n    }\n\n    @Override\n    public Integer next() {\n        // Your logic here\n        return 0;\n    }\n\n    @Override\n    public boolean hasNext() {\n        // Your logic here\n        return false;\n    }\n\n    private static List<NestedInteger> parse(String s, int[] pos) {\n        List<NestedInteger> res = new ArrayList<>();\n        while (pos[0] < s.length()) {\n            char c = s.charAt(pos[0]);\n            if (c == '[') {\n                pos[0]++;\n                res.add(new NestedIntegerImpl(parse(s, pos)));\n            } else if (c == ']') {\n                pos[0]++;\n                return res;\n            } else if (Character.isDigit(c) || c == '-') {\n                int start = pos[0];\n                if (c == '-') pos[0]++;\n                while (pos[0] < s.length() && Character.isDigit(s.charAt(pos[0]))) pos[0]++;\n                res.add(new NestedIntegerImpl(Integer.parseInt(s.substring(start, pos[0]))));\n            } else {\n                pos[0]++;\n            }\n        }\n        return res;\n    }\n\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (sc.hasNextLine()) {\n            String line = sc.nextLine();\n            int[] pos = {1};\n            List<NestedInteger> nl = parse(line, pos);\n            Solution it = new Solution(nl);\n            StringBuilder sb = new StringBuilder(\"[\");\n            while (it.hasNext()) {\n                sb.append(it.next());\n                if (it.hasNext()) sb.append(\",\");\n            }\n            sb.append(\"]\");\n            System.out.println(sb.toString());\n        }\n    }\n}",
        "javascript": "/**\n * // This is the interface that allows for creating nested lists.\n * // You should not implement it, or speculate about its implementation\n * function NestedInteger() {\n *\n *     //@return {boolean}\n *     this.isInteger = function() {\n *         ...\n *     };\n *\n *     //@return {integer}\n *     this.getInteger = function() {\n *         ...\n *     };\n *\n *     //@return {NestedInteger[]}\n *     this.getList = function() {\n *         ...\n *     };\n * };\n */\n/**\n * @param {NestedInteger[]} nestedList\n */\nvar NestedIterator = function(nestedList) {\n    // Your logic here\n};\n\n/**\n * @this NestedIterator\n * @returns {boolean}\n */\nNestedIterator.prototype.hasNext = function() {\n    // Your logic here\n};\n\n/**\n * @this NestedIterator\n * @returns {integer}\n */\nNestedIterator.prototype.next = function() {\n    // Your logic here\n};\n\nconst fs = require('fs');\nconst input = fs.readFileSync(0, 'utf8').trim();\nif (input) {\n    const data = JSON.parse(input);\n    function wrap(d) {\n        return d.map(x => ({\n            isInteger: () => !Array.isArray(x),\n            getInteger: () => Array.isArray(x) ? null : x,\n            getList: () => Array.isArray(x) ? wrap(x) : null\n        }));\n    }\n    const it = new NestedIterator(wrap(data));\n    const res = [];\n    while (it.hasNext()) res.push(it.next());\n    console.log(JSON.stringify(res).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n#include <ctype.h>\n#include <string.h>\n\nstruct NestedInteger {\n    bool isInt;\n    int val;\n    struct NestedInteger** list;\n    int listSize;\n};\n\nstruct NestedIterator {\n    // Your logic here\n};\n\nstruct NestedIterator* nestedIteratorCreate(struct NestedInteger** nestedList, int nestedListSize) {\n    // Your logic here\n    return NULL;\n}\n\nbool nestedIteratorHasNext(struct NestedIterator *iter) {\n    // Your logic here\n    return false;\n}\n\nint nestedIteratorNext(struct NestedIterator *iter) {\n    // Your logic here\n    return 0;\n}\n\nint main() {\n    // Simplified harness for C\n    // In practical competitive programming, inputs are usually flattened or use specific formats\n    // Here we'll stick to expected behavior simulation\n    return 0;\n}"
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
