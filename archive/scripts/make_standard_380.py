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
        "python": (
            "import sys\n"
            "import json\n"
            "import random\n\n"
            "class RandomizedSet:\n"
            "    def __init__(self):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def insert(self, val: int) -> bool:\n"
            "        # User logic here\n"
            "        return True\n\n"
            "    def remove(self, val: int) -> bool:\n"
            "        # User logic here\n"
            "        return True\n\n"
            "    def getRandom(self) -> int:\n"
            "        # User logic here\n"
            "        return 0\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().strip().splitlines()\n"
            "    if len(lines) >= 2:\n"
            "        commands = json.loads(lines[0])\n"
            "        args = json.loads(lines[1])\n"
            "        obj = None\n"
            "        output = []\n"
            "        for i in range(len(commands)):\n"
            "            if commands[i] == 'RandomizedSet':\n"
            "                obj = RandomizedSet()\n"
            "                output.append(None)\n"
            "            elif commands[i] == 'insert':\n"
            "                output.append(obj.insert(args[i][0]))\n"
            "            elif commands[i] == 'remove':\n"
            "                output.append(obj.remove(args[i][0]))\n"
            "            elif commands[i] == 'getRandom':\n"
            "                output.append(obj.getRandom())\n"
            "        print(json.dumps(output).replace(' ', ''))\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n"
            "#include <unordered_map>\n"
            "#include <algorithm>\n"
            "#include <cstdlib>\n"
            "using namespace std;\n\n"
            "class RandomizedSet {\n"
            "public:\n"
            "    RandomizedSet() {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    bool insert(int val) {\n"
            "        // User logic here\n"
            "        return true;\n"
            "    }\n"
            "    \n"
            "    bool remove(int val) {\n"
            "        // User logic here\n"
            "        return true;\n"
            "    }\n"
            "    \n"
            "    int getRandom() {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    string line1;\n"
            "    if (getline(cin, line1)) {\n"
            "        vector<string> commands;\n"
            "        for (int i = 0; i < line1.length(); i++) {\n"
            "            if (line1[i] == '\"') {\n"
            "                int j = i + 1;\n"
            "                while (j < line1.length() && line1[j] != '\"') j++;\n"
            "                commands.push_back(line1.substr(i + 1, j - i - 1));\n"
            "                i = j;\n"
            "            }\n"
            "        }\n"
            "        string line2;\n"
            "        if (getline(cin, line2)) {\n"
            "            vector<vector<int>> args;\n"
            "            int i = 0;\n"
            "            while (i < line2.length() && line2[i] != '[') i++;\n"
            "            i++;\n"
            "            while (i < line2.length()) {\n"
            "                if (line2[i] == '[') {\n"
            "                    int j = i + 1;\n"
            "                    vector<int> curr;\n"
            "                    while (j < line2.length() && line2[j] != ']') {\n"
            "                        if (line2[j] == '-' || (line2[j] >= '0' && line2[j] <= '9')) {\n"
            "                            int v = 0, sign = 1;\n"
            "                            if (line2[j] == '-') { sign = -1; j++; }\n"
            "                            while (j < line2.length() && line2[j] >= '0' && line2[j] <= '9') {\n"
            "                                v = v * 10 + (line2[j] - '0'); j++;\n"
            "                            }\n"
            "                            curr.push_back(v * sign);\n"
            "                            j--;\n"
            "                        }\n"
            "                        j++;\n"
            "                    }\n"
            "                    args.push_back(curr);\n"
            "                    i = j;\n"
            "                }\n"
            "                i++;\n"
            "            }\n"
            "            RandomizedSet* obj = nullptr;\n"
            "            cout << \"[\";\n"
            "            for (int k = 0; k < commands.size(); k++) {\n"
            "                if (k > 0) cout << \",\";\n"
            "                if (commands[k] == \"RandomizedSet\") {\n"
            "                    obj = new RandomizedSet();\n"
            "                    cout << \"null\";\n"
            "                } else if (commands[k] == \"insert\") {\n"
            "                    cout << (obj->insert(args[k][0]) ? \"true\" : \"false\");\n"
            "                } else if (commands[k] == \"remove\") {\n"
            "                    cout << (obj->remove(args[k][0]) ? \"true\" : \"false\");\n"
            "                } else if (commands[k] == \"getRandom\") {\n"
            "                    cout << obj->getRandom();\n"
            "                }\n"
            "            }\n"
            "            cout << \"]\" << endl;\n"
            "            delete obj;\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        ),
        "java": (
            "import java.util.*;\n\n"
            "class RandomizedSet {\n"
            "    public RandomizedSet() {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    public boolean insert(int val) {\n"
            "        // User logic here\n"
            "        return true;\n"
            "    }\n"
            "    \n"
            "    public boolean remove(int val) {\n"
            "        // User logic here\n"
            "        return true;\n"
            "    }\n"
            "    \n"
            "    public int getRandom() {\n"
            "        // User logic here\n"
            "        return 0;\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        if (sc.hasNextLine()) {\n"
            "            String line1 = sc.nextLine();\n"
            "            List<String> commands = new ArrayList<>();\n"
            "            int i = 0;\n"
            "            while (i < line1.length()) {\n"
            "                if (line1.charAt(i) == '\"') {\n"
            "                    int j = i + 1;\n"
            "                    while (j < line1.length() && line1.charAt(j) != '\"') j++;\n"
            "                    commands.add(line1.substring(i + 1, j));\n"
            "                    i = j;\n"
            "                }\n"
            "                i++;\n"
            "            }\n"
            "            if (sc.hasNextLine()) {\n"
            "                String line2 = sc.nextLine();\n"
            "                List<List<Integer>> argList = new ArrayList<>();\n"
            "                i = 0;\n"
            "                while (i < line2.length() && line2.charAt(i) != '[') i++;\n"
            "                i++;\n"
            "                while (i < line2.length()) {\n"
            "                    if (line2.charAt(i) == '[') {\n"
            "                        int j = i + 1;\n"
            "                        List<Integer> curr = new ArrayList<>();\n"
            "                        while (j < line2.length() && line2.charAt(j) != ']') {\n"
            "                            char c = line2.charAt(j);\n"
            "                            if (c == '-' || (c >= '0' && c <= '9')) {\n"
            "                                int v = 0, sign = 1;\n"
            "                                if (c == '-') { sign = -1; j++; }\n"
            "                                while (j < line2.length() && line2.charAt(j) >= '0' && line2.charAt(j) <= '9') {\n"
            "                                    v = v * 10 + (line2.charAt(j) - '0'); j++;\n"
            "                                }\n"
            "                                curr.add(v * sign);\n"
            "                                j--;\n"
            "                            }\n"
            "                            j++;\n"
            "                        }\n"
            "                        argList.add(curr);\n"
            "                        i = j;\n"
            "                    }\n"
            "                    i++;\n"
            "                }\n"
            "                RandomizedSet obj = null;\n"
            "                System.out.print(\"[\");\n"
            "                for (int k = 0; k < commands.size(); k++) {\n"
            "                    if (k > 0) System.out.print(\",\");\n"
            "                    String cmd = commands.get(k);\n"
            "                    if (cmd.equals(\"RandomizedSet\")) {\n"
            "                        obj = new RandomizedSet();\n"
            "                        System.out.print(\"null\");\n"
            "                    } else if (cmd.equals(\"insert\")) {\n"
            "                        System.out.print(obj.insert(argList.get(k).get(0)) ? \"true\" : \"false\");\n"
            "                    } else if (cmd.equals(\"remove\")) {\n"
            "                        System.out.print(obj.remove(argList.get(k).get(0)) ? \"true\" : \"false\");\n"
            "                    } else if (cmd.equals(\"getRandom\")) {\n"
            "                        System.out.print(obj.getRandom());\n"
            "                    }\n"
            "                }\n"
            "                System.out.println(\"]\");\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "/**\n * Initialize your data structure here.\n */\n"
            "var RandomizedSet = function() {\n"
            "    // User logic here\n"
            "};\n\n"
            "/**\n * @param {number} val\n * @return {boolean}\n */\n"
            "RandomizedSet.prototype.insert = function(val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "};\n\n"
            "/**\n * @param {number} val\n * @return {boolean}\n */\n"
            "RandomizedSet.prototype.remove = function(val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "};\n\n"
            "/**\n * @return {number}\n */\n"
            "RandomizedSet.prototype.getRandom = function() {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "};\n\n"
            "const fs = require('fs');\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').trim().split('\\n');\n"
            "    if (input.length >= 2) {\n"
            "        const commands = JSON.parse(input[0]);\n"
            "        const args = JSON.parse(input[1]);\n"
            "        let obj = null;\n"
            "        const output = [];\n"
            "        for (let i = 0; i < commands.length; i++) {\n"
            "            if (commands[i] === 'RandomizedSet') {\n"
            "                obj = new RandomizedSet();\n"
            "                output.push(null);\n"
            "            } else if (commands[i] === 'insert') {\n"
            "                output.push(obj.insert(args[i][0]));\n"
            "            } else if (commands[i] === 'remove') {\n"
            "                output.push(obj.remove(args[i][0]));\n"
            "            } else if (commands[i] === 'getRandom') {\n"
            "                output.push(obj.getRandom());\n"
            "            }\n"
            "        }\n"
            "        console.log(JSON.stringify(output).replace(/ /g, ''));\n"
            "    }\n"
            "}\n"
            "main();\n"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <stdlib.h>\n"
            "#include <stdbool.h>\n"
            "#include <string.h>\n\n"
            "typedef struct {\n"
            "    // User logic here\n"
            "} RandomizedSet;\n\n"
            "RandomizedSet* randomizedSetCreate() {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "bool randomizedSetInsert(RandomizedSet* obj, int val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "}\n\n"
            "bool randomizedSetRemove(RandomizedSet* obj, int val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "}\n\n"
            "int randomizedSetGetRandom(RandomizedSet* obj) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "void randomizedSetFree(RandomizedSet* obj) {\n"
            "    // User logic here\n"
            "}\n\n"
            "int main() {\n"
            "    char line[200000];\n"
            "    if (fgets(line, sizeof(line), stdin)) {\n"
            "        char* commands[100000];\n"
            "        int cmdCount = 0;\n"
            "        int i = 0;\n"
            "        while (line[i]) {\n"
            "            if (line[i] == '\"') {\n"
            "                int j = i + 1;\n"
            "                while (line[j] && line[j] != '\"') j++;\n"
            "                line[j] = '\\0';\n"
            "                commands[cmdCount++] = line + i + 1;\n"
            "                i = j;\n"
            "            }\n"
            "            i++;\n"
            "        }\n"
            "        if (fgets(line, sizeof(line), stdin)) {\n"
            "            int argsArr[100000];\n"
            "            int argCount = 0;\n"
            "            i = 0;\n"
            "            while (line[i] && line[i] != '[') i++;\n"
            "            i++;\n"
            "            while (line[i]) {\n"
            "                if (line[i] == '[') {\n"
            "                    int j = i + 1;\n"
            "                    int val = 0; \n"
            "                    while (line[j] && line[j] != ']') {\n"
            "                        if (line[j] == '-' || (line[j] >= '0' && line[j] <= '9')) {\n"
            "                            int v = 0, sign = 1;\n"
            "                            if (line[j] == '-') { sign = -1; j++; }\n"
            "                            while (line[j] >= '0' && line[j] <= '9') {\n"
            "                                v = v * 10 + (line[j] - '0'); j++;\n"
            "                            }\n"
            "                            val = v * sign;\n"
            "                            j--;\n"
            "                        }\n"
            "                        j++;\n"
            "                    }\n"
            "                    argsArr[argCount++] = val;\n"
            "                    i = j;\n"
            "                }\n"
            "                i++;\n"
            "            }\n"
            "            RandomizedSet* obj = NULL;\n"
            "            printf(\"[\");\n"
            "            for (int k = 0; k < cmdCount; k++) {\n"
            "                if (k > 0) printf(\",\");\n"
            "                if (strcmp(commands[k], \"RandomizedSet\") == 0) {\n"
            "                    obj = randomizedSetCreate();\n"
            "                    printf(\"null\");\n"
            "                } else if (strcmp(commands[k], \"insert\") == 0) {\n"
            "                    printf(randomizedSetInsert(obj, argsArr[k]) ? \"true\" : \"false\");\n"
            "                } else if (strcmp(commands[k], \"remove\") == 0) {\n"
            "                    printf(randomizedSetRemove(obj, argsArr[k]) ? \"true\" : \"false\");\n"
            "                } else if (strcmp(commands[k], \"getRandom\") == 0) {\n"
            "                    printf(\"%d\", randomizedSetGetRandom(obj));\n"
            "                }\n"
            "            }\n"
            "            printf(\"]\\n\");\n"
            "            if (obj) randomizedSetFree(obj);\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
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
