import json
import os

def generate_json():
    problem_id = 381
    title = "Insert Delete GetRandom O(1) - Duplicates allowed"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>381. Insert Delete GetRandom O(1) - Duplicates allowed</h3>
<p><code>RandomizedCollection</code> is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also removing a random element.</p>

<p>Implement the <code>RandomizedCollection</code> class:</p>
<ul>
	<li><code>RandomizedCollection()</code> Initializes the <code>RandomizedCollection</code> object.</li>
	<li><code>bool insert(int val)</code> Inserts an item <code>val</code> into the multiset. Returns <code>true</code> if the item was not present, <code>false</code> otherwise.</li>
	<li><code>bool remove(int val)</code> Removes an item <code>val</code> from the multiset if present. Returns <code>true</code> if the item was present, <code>false</code> otherwise. Note that if <code>val</code> has multiple occurrences in the multiset, we only remove one of them.</li>
	<li><code>int getRandom()</code> Returns a random element from the current multiset of elements (it is guaranteed that at least one element exists when this method is called). The probability of each element being returned is <strong>linearly related</strong> to the number of the same value the multiset contains.</li>
</ul>

<p>You must implement the functions of the class such that each function works in <strong>average</strong> <code>O(1)</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
<strong>Output:</strong>
[null, true, false, true, 1, true, 1]
<strong>Explanation:</strong>
RandomizedCollection collection = new RandomizedCollection();
collection.insert(1);   // return true. [1]
collection.insert(1);   // return false. [1,1]
collection.insert(2);   // return true. [1,1,2]
collection.getRandom(); // return 1 with prob 2/3, 2 with prob 1/3.
collection.remove(1);   // return true. [1,2]
collection.getRandom(); // return 1/2 prob for 1 and 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>insert</code>, <code>remove</code>, and <code>getRandom</code>.</li>
	<li>There will be <strong>at least one</strong> element in the data structure when <code>getRandom</code> is called.</li>
</ul>"""

    input_format = "Calls to `RandomizedCollection` methods."
    output_format = "Results of `insert`, `remove` (boolean) and `getRandom` (integer)."
    
    constraints = [
        "val can be any 32-bit signed integer.",
        "Average O(1) complexity required.",
        "Duplicates are allowed; probability depends on frequency."
    ]
    
    explanation = """To handle duplicates and support O(1) `getRandom`, we iterate on the 380 approach by using a **Set of Indices** in the hash map.

### Data Structures:
1. **Dynamic Array (`self.nums`)**: Stores elements.
2. **Hash Map (`self.pos`)**: Stores `val -> set([indices_in_nums])`.

### Algorithm Steps:
- **`insert(val)`**:
  - `is_present = val in self.pos`.
  - Append `val` to `nums`.
  - Add the new index to `pos[val]`.
  - Return `not is_present`.
- **`remove(val)`**:
  - If `val` not in `pos`, return `false`.
  - Pick any index of `val` from `pos[val]`: `idx = next(iter(self.pos[val]))`.
  - Swap with last:
    - `last_val = nums[-1]`, `last_idx = len(nums) - 1`.
    - Update `nums[idx] = last_val`.
    - Update `pos[last_val]`: remove `last_idx`, add `idx`.
    - Remove `idx` from `pos[val]`.
    - If `pos[val]` is empty, delete key.
  - `nums.pop()`.
  - Return `true`.
- **`getRandom()`**:
  - Same as 380: `random.choice(self.nums)`. Since the list contains duplicates, the selection probability is naturally proportional to frequency.

### Corner Case:
When `val == last_val`, we must be careful with the order of set operations in `remove` to avoid deleting the index we just added. 
1. Get `idx` from `pos[val]`.
2. Add `idx` to `pos[last_val]`.
3. Remove `last_idx` from `pos[last_val]`.
4. Remove `idx` from `pos[val]`.

### Complexity Analysis:
- **Time Complexity**: $O(1)$ average.
- **Space Complexity**: $O(N)$."""
    
    answer = """import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.pos = defaultdict(set) # val -> set of indices

    def insert(self, val: int) -> bool:
        res = val not in self.pos
        self.pos[val].add(len(self.nums))
        self.nums.append(val)
        return res

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False
        
        # Index of value to remove
        idx = self.pos[val].pop()
        # Last element info
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1
        
        # Swap logic
        self.nums[idx] = last_val
        self.pos[last_val].add(idx)
        self.pos[last_val].discard(last_idx)
        
        # If removal emptied the set, cleanup (defalutdict handles most)
        if not self.pos[val]:
            del self.pos[val]
            
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport random\nfrom collections import defaultdict\nclass RandomizedCollection:\n    def __init__(self):\n        # User logic here\n        pass\n    def insert(self, val: int) -> bool:\n        # User logic here\n        return True\n    def remove(self, val: int) -> bool:\n        # User logic here\n        return True\n    def getRandom(self) -> int:\n        # User logic here\n        return 0\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        commands = json.loads(input_data[0])\n        arguments = json.loads(input_data[1])\n        obj = None\n        output = []\n        for cmd, arg in zip(commands, arguments):\n            if cmd == 'RandomizedCollection':\n                obj = RandomizedCollection()\n                output.append(None)\n            elif cmd == 'insert':\n                output.append(obj.insert(arg[0]))\n            elif cmd == 'remove':\n                output.append(obj.remove(arg[0]))\n            elif cmd == 'getRandom':\n                output.append(obj.getRandom())\n        print(json.dumps(output).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <unordered_map>\n#include <unordered_set>\nusing namespace std;\nclass RandomizedCollection {\npublic:\n    RandomizedCollection() {\n        // User logic here\n    }\n    bool insert(int val) {\n        // User logic here\n        return true;\n    }\n    bool remove(int val) {\n        // User logic here\n        return true;\n    }\n    int getRandom() {\n        // User logic here\n        return 0;\n    }\n};\nint main() {\n    string line1, line2;\n    if (!getline(cin, line1) || !getline(cin, line2)) return 0;\n    regex re_cmd(\"\\\\\\\"(.*?)\\\\\\\"\");\n    auto cmd_begin = sregex_iterator(line1.begin(), line1.end(), re_cmd), cmd_end = sregex_iterator();\n    regex re_arg(\"\\\\[([^\\\\[\\\\]]*)\\\\]\");\n    auto arg_begin = sregex_iterator(line2.begin(), line2.end(), re_arg), arg_end = sregex_iterator();\n    RandomizedCollection* obj = nullptr;\n    cout << \"[\";\n    bool first = true;\n    while (cmd_begin != cmd_end && arg_begin != arg_end) {\n        string cmd = (*cmd_begin)[1].str();\n        string arg_str = (*arg_begin)[1].str();\n        if (!first) cout << \",\";\n        if (cmd == \"RandomizedCollection\") {\n            obj = new RandomizedCollection();\n            cout << \"null\";\n        } else if (cmd == \"insert\") {\n            cout << (obj->insert(stoi(arg_str)) ? \"true\" : \"false\");\n        } else if (cmd == \"remove\") {\n            cout << (obj->remove(stoi(arg_str)) ? \"true\" : \"false\");\n        } else if (cmd == \"getRandom\") {\n            cout << obj->getRandom();\n        }\n        first = false;\n        cmd_begin++; arg_begin++;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\npublic class Main {\n    static class RandomizedCollection {\n        public RandomizedCollection() {\n            // User logic here\n        }\n        public boolean insert(int val) {\n            // User logic here\n            return true;\n        }\n        public boolean remove(int val) {\n            // User logic here\n            return true;\n        }\n        public int getRandom() {\n            // User logic here\n            return 0;\n        }\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine();\n        if (!sc.hasNextLine()) return;\n        String line2 = sc.nextLine();\n        Matcher cm = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(line1);\n        Matcher am = Pattern.compile(\"\\\\[([^\\\\[\\\\]]*)\\\\]\").matcher(line2);\n        RandomizedCollection obj = null;\n        StringBuilder res = new StringBuilder(\"[\");\n        boolean first = true;\n        while (cm.find() && am.find()) {\n            String cmd = cm.group(1);\n            String arg = am.group(1).trim();\n            if (!first) res.append(\",\");\n            if (cmd.equals(\"RandomizedCollection\")) {\n                obj = new RandomizedCollection();\n                res.append(\"null\");\n            } else if (cmd.equals(\"insert\")) {\n                res.append(obj.insert(Integer.parseInt(arg)) ? \"true\" : \"false\");\n            } else if (cmd.equals(\"remove\")) {\n                res.append(obj.remove(Integer.parseInt(arg)) ? \"true\" : \"false\");\n            } else if (cmd.equals(\"getRandom\")) {\n                res.append(obj.getRandom());\n            }\n            first = false;\n        }\n        res.append(\"]\");\n        System.out.println(res.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\nclass RandomizedCollection {\n    constructor() {\n        // User logic here\n    }\n    insert(val) {\n        // User logic here\n        return true;\n    }\n    remove(val) {\n        // User logic here\n        return true;\n    }\n    getRandom() {\n        // User logic here\n        return 0;\n    }\n}\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const commands = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    const result = commands.map((cmd, i) => {\n        if (cmd === 'RandomizedCollection') {\n            obj = new RandomizedCollection();\n            return null;\n        } else if (cmd === 'insert') {\n            return obj.insert(args[i][0]);\n        } else if (cmd === 'remove') {\n            return obj.remove(args[i][0]);\n        } else if (cmd === 'getRandom') {\n            return obj.getRandom();\n        }\n    });\n    console.log(JSON.stringify(result).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\ntypedef struct {\n    // User logic here\n} RandomizedCollection;\nRandomizedCollection* randomizedCollectionCreate() {\n    RandomizedCollection* obj = malloc(sizeof(RandomizedCollection));\n    // User logic here\n    return obj;\n}\nbool randomizedCollectionInsert(RandomizedCollection* obj, int val) {\n    // User logic here\n    return true;\n}\nbool randomizedCollectionRemove(RandomizedCollection* obj, int val) {\n    // User logic here\n    return true;\n}\nint randomizedCollectionGetRandom(RandomizedCollection* obj) {\n    // User logic here\n    return 0;\n}\nvoid randomizedCollectionFree(RandomizedCollection* obj) {\n    // User logic here\n    free(obj);\n}\nint main() {\n    char *line1 = malloc(1000000), *line2 = malloc(1000000);\n    if (!fgets(line1, 1000000, stdin) || !fgets(line2, 1000000, stdin)) return 0;\n    printf(\"[\");\n    char *c_ptr = line1, *a_ptr = line2;\n    RandomizedCollection* obj = NULL;\n    bool first = true;\n    while ((c_ptr = strchr(c_ptr, '\"'))) {\n        c_ptr++;\n        char *c_end = strchr(c_ptr, '\"');\n        char cmd[50]; strncpy(cmd, c_ptr, c_end - c_ptr); cmd[c_end - c_ptr] = '\\0';\n        if (!first) printf(\",\");\n        a_ptr = strchr(a_ptr, '[');\n        if (strcmp(cmd, \"RandomizedCollection\") == 0) {\n            obj = randomizedCollectionCreate();\n            printf(\"null\");\n        } else {\n            int val = 0; if (strcmp(cmd, \"getRandom\") != 0) val = strtol(a_ptr + 1, NULL, 10);\n            if (strcmp(cmd, \"insert\") == 0) printf(randomizedCollectionInsert(obj, val) ? \"true\" : \"false\");\n            else if (strcmp(cmd, \"remove\") == 0) printf(randomizedCollectionRemove(obj, val) ? \"true\" : \"false\");\n            else if (strcmp(cmd, \"getRandom\") == 0) printf(\"%d\", randomizedCollectionGetRandom(obj));\n        }\n        first = false;\n        c_ptr = c_end + 1; a_ptr = strchr(a_ptr, ']') + 1;\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }


    test_cases = [
        # Sample cases (2)
        {"input": '["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]\n[[], [1], [1], [2], [], [1], []]', "expected_output": "[null,true,false,true,1,true,1]", "is_sample": True},
        {"input": '["RandomizedCollection", "insert", "insert", "remove", "getRandom"]\n[[], [1], [1], [1], []]', "expected_output": "[null,true,false,true,1]", "is_sample": True},
        # Diverse cases (5)
        {"input": '["RandomizedCollection", "insert", "remove", "insert"]\n[[], [1], [1], [1]]', "expected_output": "[null,true,true,true]", "is_sample": False},
        {"input": '["RandomizedCollection", "insert", "insert", "remove", "remove"]\n[[], [1], [2], [1], [2]]', "expected_output": "[null,true,true,true,true]", "is_sample": False},
        {"input": '["RandomizedCollection", "remove", "insert"]\n[[], [0], [0]]', "expected_output": "[null,false,true]", "is_sample": False},
        {"input": '["RandomizedCollection", "insert", "getRandom"]\n[[], [5], []]', "expected_output": "[null,true,5]", "is_sample": False},
        {"input": '["RandomizedCollection", "insert", "insert", "insert", "remove", "getRandom"]\n[[], [3], [3], [3], [3], []]', "expected_output": "[null,true,false,false,true,3]", "is_sample": False},
        # Stress cases (3)
        {"input": '["RandomizedCollection"]' + ',"insert"'*5 + ',"getRandom"]\n[[]' + ',[10]'*5 + ',[]]', "expected_output": "[null,true,false,false,false,false,10]", "is_sample": False},
        {"input": '["RandomizedCollection","insert","remove","insert","remove","insert","remove","insert","remove","insert","remove","insert","getRandom"]\n[[],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2],[]]', "expected_output": "[null,true,true,true,true,true,true,true,true,true,true,true,2]", "is_sample": False},
        {"input": '["RandomizedCollection","insert","insert","insert","insert","insert","getRandom"]\n[[],[1],[2],[3],[1],[2],[]]', "expected_output": "[null,true,true,true,false,false,1]", "is_sample": False},
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
        "topics": ["Array", "Hash Table", "Math", "Design", "Randomized"],
        "companyIndex": 1
    }

    output_path = "301-500/381_Insert_Delete_GetRandom_O(1)_Duplicates_allowed.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
