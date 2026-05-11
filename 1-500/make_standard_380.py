import json
import os

def generate_json():
    problem_id = 380
    title = "Insert Delete GetRandom O(1)"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>380. Insert Delete GetRandom O(1)</h3>
<p>Implement the <code>RandomizedSet</code> class:</p>

<ul>
	<li><code>RandomizedSet()</code> Initializes the <code>RandomizedSet</code> object.</li>
	<li><code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if the item was not present, <code>false</code> otherwise.</li>
	<li><code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if the item was present, <code>false</code> otherwise.</li>
	<li><code>int getRandom()</code> Returns a random element from the current set of elements (it is guaranteed that at least one element exists when this method is called). Each element must have the <b>same probability</b> of being returned.</li>
</ul>

<p>You must implement the functions of the class such that each function works in <strong>average</strong> <code>O(1)</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
<strong>Output:</strong>
[null, true, false, true, 2, true, false, 2]
<strong>Explanation:</strong>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>insert</code>, <code>remove</code>, and <code>getRandom</code>.</li>
	<li>There will be <strong>at least one</strong> element in the data structure when <code>getRandom</code> is called.</li>
</ul>"""

    input_format = "Calls to `RandomizedSet` methods."
    output_format = "Results of `insert`, `remove` (boolean) and `getRandom` (integer)."
    
    constraints = [
        "val can be any 32-bit signed integer.",
        "Average O(1) complexity required.",
        "Total calls <= 200,000."
    ]
    
    explanation = """To achieve average $O(1)$ for all operations including `getRandom`, we need a combination of two data structures:

### Data Structures:
1. **Dynamic Array (`self.nums`)**: Stores the actual elements. This allows `getRandom` to be $O(1)$ by picking a random index.
2. **Hash Map (`self.pos`)**: Stores the value as the key and its index in `self.nums` as the value. This allows $O(1)$ lookup for `insert` and `remove`.

### Algorithm Steps:
- **`insert(val)`**:
  - Check if `val` is already in `pos`. If yes, return `false`.
  - Append `val` to `nums`.
  - Store the index in `pos[val] = len(nums) - 1`.
  - Return `true`.
- **`remove(val)`**:
  - Check if `val` is in the set. If no, return `false`.
  - Find the index of `val`: `idx = pos[val]`.
  - Swap the element at `idx` with the **last element** in `nums`.
    - `last_val = nums[-1]`
    - `nums[idx] = last_val`
    - `pos[last_val] = idx`
  - Remove the last element from `nums.pop()`.
  - Delete `val` from `pos`.
  - Return `true`.
- **`getRandom()`**:
  - Pick a random index `random.randint(0, len(nums) - 1)` and return `nums[index]`.

### Complexity Analysis:
- **Time Complexity**: $O(1)$ average for all operations.
- **Space Complexity**: $O(N)$ to store $N$ elements."""
    
    answer = """import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {} # val -> index in nums

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        # Swap with last element to remove in O(1)
        idx = self.pos[val]
        last_val = self.nums[-1]
        
        self.nums[idx] = last_val
        self.pos[last_val] = idx
        
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)"""

    boilerplate = {
        "python": "import sys\nimport json\nimport random\nclass RandomizedSet:\n    def __init__(self):\n        # User logic here\n        pass\n    def insert(self, val: int) -> bool:\n        # User logic here\n        return True\n    def remove(self, val: int) -> bool:\n        # User logic here\n        return True\n    def getRandom(self) -> int:\n        # User logic here\n        return 0\nif __name__ == '__main__':\n    input_data = sys.stdin.read().splitlines()\n    if len(input_data) >= 2:\n        commands = json.loads(input_data[0])\n        arguments = json.loads(input_data[1])\n        obj = None\n        output = []\n        for cmd, arg in zip(commands, arguments):\n            if cmd == 'RandomizedSet':\n                obj = RandomizedSet()\n                output.append(None)\n            elif cmd == 'insert':\n                output.append(obj.insert(arg[0]))\n            elif cmd == 'remove':\n                output.append(obj.remove(arg[0]))\n            elif cmd == 'getRandom':\n                output.append(obj.getRandom())\n        print(json.dumps(output).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <regex>\n#include <unordered_map>\nusing namespace std;\nclass RandomizedSet {\npublic:\n    RandomizedSet() {\n        // User logic here\n    }\n    bool insert(int val) {\n        // User logic here\n        return true;\n    }\n    bool remove(int val) {\n        // User logic here\n        return true;\n    }\n    int getRandom() {\n        // User logic here\n        return 0;\n    }\n};\nint main() {\n    string line1, line2;\n    if (!getline(cin, line1) || !getline(cin, line2)) return 0;\n    regex re_cmd(\"\\\\\\\"(.*?)\\\\\\\"\");\n    auto cmd_begin = sregex_iterator(line1.begin(), line1.end(), re_cmd), cmd_end = sregex_iterator();\n    regex re_arg(\"\\\\[([^\\\\[\\\\]]*)\\\\]\");\n    auto arg_begin = sregex_iterator(line2.begin(), line2.end(), re_arg), arg_end = sregex_iterator();\n    RandomizedSet* obj = nullptr;\n    cout << \"[\";\n    bool first = true;\n    while (cmd_begin != cmd_end && arg_begin != arg_end) {\n        string cmd = (*cmd_begin)[1].str();\n        string arg_str = (*arg_begin)[1].str();\n        if (!first) cout << \",\";\n        if (cmd == \"RandomizedSet\") {\n            obj = new RandomizedSet();\n            cout << \"null\";\n        } else if (cmd == \"insert\") {\n            cout << (obj->insert(stoi(arg_str)) ? \"true\" : \"false\");\n        } else if (cmd == \"remove\") {\n            cout << (obj->remove(stoi(arg_str)) ? \"true\" : \"false\");\n        } else if (cmd == \"getRandom\") {\n            cout << obj->getRandom();\n        }\n        first = false;\n        cmd_begin++; arg_begin++;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\nimport json.*; // Mock or use manual\npublic class Main {\n    static class RandomizedSet {\n        public RandomizedSet() {\n            // User logic here\n        }\n        public boolean insert(int val) {\n            // User logic here\n            return true;\n        }\n        public boolean remove(int val) {\n            // User logic here\n            return true;\n        }\n        public int getRandom() {\n            // User logic here\n            return 0;\n        }\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        if (!sc.hasNextLine()) return;\n        String line1 = sc.nextLine();\n        if (!sc.hasNextLine()) return;\n        String line2 = sc.nextLine();\n        Matcher cm = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(line1);\n        Matcher am = Pattern.compile(\"\\\\[([^\\\\[\\\\]]*)\\\\]\").matcher(line2);\n        RandomizedSet obj = null;\n        StringBuilder res = new StringBuilder(\"[\");\n        boolean first = true;\n        while (cm.find() && am.find()) {\n            String cmd = cm.group(1);\n            String arg = am.group(1).trim();\n            if (!first) res.append(\",\");\n            if (cmd.equals(\"RandomizedSet\")) {\n                obj = new RandomizedSet();\n                res.append(\"null\");\n            } else if (cmd.equals(\"insert\")) {\n                res.append(obj.insert(Integer.parseInt(arg)) ? \"true\" : \"false\");\n            } else if (cmd.equals(\"remove\")) {\n                res.append(obj.remove(Integer.parseInt(arg)) ? \"true\" : \"false\");\n            } else if (cmd.equals(\"getRandom\")) {\n                res.append(obj.getRandom());\n            }\n            first = false;\n        }\n        res.append(\"]\");\n        System.out.println(res.toString());\n    }\n}",
        "javascript": "const fs = require('fs');\nclass RandomizedSet {\n    constructor() {\n        // User logic here\n    }\n    insert(val) {\n        // User logic here\n        return true;\n    }\n    remove(val) {\n        // User logic here\n        return true;\n    }\n    getRandom() {\n        // User logic here\n        return 0;\n    }\n}\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif (input.length >= 2) {\n    const commands = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    const result = commands.map((cmd, i) => {\n        if (cmd === 'RandomizedSet') {\n            obj = new RandomizedSet();\n            return null;\n        } else if (cmd === 'insert') {\n            return obj.insert(args[i][0]);\n        } else if (cmd === 'remove') {\n            return obj.remove(args[i][0]);\n        } else if (cmd === 'getRandom') {\n            return obj.getRandom();\n        }\n    });\n    console.log(JSON.stringify(result).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\ntypedef struct {\n    // User logic here\n} RandomizedSet;\nRandomizedSet* randomizedSetCreate() {\n    RandomizedSet* obj = malloc(sizeof(RandomizedSet));\n    // User logic here\n    return obj;\n}\nbool randomizedSetInsert(RandomizedSet* obj, int val) {\n    // User logic here\n    return true;\n}\nbool randomizedSetRemove(RandomizedSet* obj, int val) {\n    // User logic here\n    return true;\n}\nint randomizedSetGetRandom(RandomizedSet* obj) {\n    // User logic here\n    return 0;\n}\nvoid randomizedSetFree(RandomizedSet* obj) {\n    // User logic here\n    free(obj);\n}\nint main() {\n    char *line1 = malloc(1000000), *line2 = malloc(1000000);\n    if (!fgets(line1, 1000000, stdin) || !fgets(line2, 1000000, stdin)) return 0;\n    printf(\"[\");\n    char *c_ptr = line1, *a_ptr = line2;\n    RandomizedSet* obj = NULL;\n    bool first = true;\n    while ((c_ptr = strchr(c_ptr, '\"'))) {\n        c_ptr++;\n        char *c_end = strchr(c_ptr, '\"');\n        char cmd[50]; strncpy(cmd, c_ptr, c_end - c_ptr); cmd[c_end - c_ptr] = '\\0';\n        if (!first) printf(\",\");\n        a_ptr = strchr(a_ptr, '[');\n        if (strcmp(cmd, \"RandomizedSet\") == 0) {\n            obj = randomizedSetCreate();\n            printf(\"null\");\n        } else {\n            int val = 0; if (strcmp(cmd, \"getRandom\") != 0) val = strtol(a_ptr + 1, NULL, 10);\n            if (strcmp(cmd, \"insert\") == 0) printf(randomizedSetInsert(obj, val) ? \"true\" : \"false\");\n            else if (strcmp(cmd, \"remove\") == 0) printf(randomizedSetRemove(obj, val) ? \"true\" : \"false\");\n            else if (strcmp(cmd, \"getRandom\") == 0) printf(\"%d\", randomizedSetGetRandom(obj));\n        }\n        first = false;\n        c_ptr = c_end + 1; a_ptr = strchr(a_ptr, ']') + 1;\n    }\n    printf(\"]\\n\");\n    return 0;\n}"
    }


    test_cases = [
        # Sample cases (2)
        {"input": '["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]\n[[], [1], [2], [2], [], [1], [2], []]', "expected_output": "[null,true,false,true,2,true,false,2]", "is_sample": True},
        {"input": '["RandomizedSet", "insert", "insert", "getRandom"]\n[[], [42], [42], []]', "expected_output": "[null,true,false,42]", "is_sample": True},
        # Diverse cases (5)
        {"input": '["RandomizedSet", "insert", "insert", "remove", "getRandom"]\n[[], [10], [20], [10], []]', "expected_output": "[null,true,true,true,20]", "is_sample": False},
        {"input": '["RandomizedSet", "remove", "insert"]\n[[], [0], [0]]', "expected_output": "[null,false,true]", "is_sample": False},
        {"input": '["RandomizedSet", "insert", "insert", "remove", "remove"]\n[[], [1], [2], [1], [2]]', "expected_output": "[null,true,true,true,true]", "is_sample": False},
        {"input": '["RandomizedSet", "insert", "remove", "remove", "insert", "getRandom"]\n[[], [5], [5], [5], [5], []]', "expected_output": "[null,true,true,false,true,5]", "is_sample": False},
        {"input": '["RandomizedSet", "insert", "insert", "insert", "remove", "getRandom"]\n[[], [1], [2], [3], [2], []]', "expected_output": "[null,true,true,true,true,1]", "is_sample": False},
        # Stress cases (3)
        {"input": '["RandomizedSet"]' + ',"insert"'*10 + ',"getRandom"]\n[[]' + ',[1]'*10 + ',[]]', "expected_output": "[null,true,false,false,false,false,false,false,false,false,false,1]", "is_sample": False},
        {"input": '["RandomizedSet","insert","insert","insert","insert","insert","insert","insert","insert","insert","insert","getRandom"]\n[[],[10],[20],[30],[40],[50],[60],[70],[80],[90],[100],[]]', "expected_output": "[null,true,true,true,true,true,true,true,true,true,true,10]", "is_sample": False},
        {"input": '["RandomizedSet","insert","remove","insert","remove","insert","remove","insert","remove","insert","remove","insert","getRandom"]\n[[],[1],[1],[2],[2],[3],[3],[4],[4],[5],[5],[6],[]]', "expected_output": "[null,true,true,true,true,true,true,true,true,true,true,true,6]", "is_sample": False}
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

    output_path = "301-500/380_Insert_Delete_GetRandom_O(1).json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
