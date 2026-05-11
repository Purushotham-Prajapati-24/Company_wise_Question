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
        "python": (
            "import sys\n"
            "import json\n"
            "import random\n"
            "from collections import defaultdict\n\n"
            "class RandomizedCollection:\n"
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
            "            if commands[i] == 'RandomizedCollection':\n"
            "                obj = RandomizedCollection()\n"
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
            "#include <unordered_set>\n"
            "#include <algorithm>\n"
            "#include <cstdlib>\n"
            "using namespace std;\n\n"
            "class RandomizedCollection {\n"
            "public:\n"
            "    RandomizedCollection() {\n"
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
            "            RandomizedCollection* obj = nullptr;\n"
            "            cout << \"[\";\n"
            "            for (int k = 0; k < commands.size(); k++) {\n"
            "                if (k > 0) cout << \",\";\n"
            "                if (commands[k] == \"RandomizedCollection\") {\n"
            "                    obj = new RandomizedCollection();\n"
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
            "class RandomizedCollection {\n"
            "    public RandomizedCollection() {\n"
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
            "                RandomizedCollection obj = null;\n"
            "                System.out.print(\"[\");\n"
            "                for (int k = 0; k < commands.size(); k++) {\n"
            "                    if (k > 0) System.out.print(\",\");\n"
            "                    String cmd = commands.get(k);\n"
            "                    if (cmd.equals(\"RandomizedCollection\")) {\n"
            "                        obj = new RandomizedCollection();\n"
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
            "var RandomizedCollection = function() {\n"
            "    // User logic here\n"
            "};\n\n"
            "/**\n * @param {number} val\n * @return {boolean}\n */\n"
            "RandomizedCollection.prototype.insert = function(val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "};\n\n"
            "/**\n * @param {number} val\n * @return {boolean}\n */\n"
            "RandomizedCollection.prototype.remove = function(val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "};\n\n"
            "/**\n * @return {number}\n */\n"
            "RandomizedCollection.prototype.getRandom = function() {\n"
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
            "            if (commands[i] === 'RandomizedCollection') {\n"
            "                obj = new RandomizedCollection();\n"
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
            "} RandomizedCollection;\n\n"
            "RandomizedCollection* randomizedCollectionCreate() {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "bool randomizedCollectionInsert(RandomizedCollection* obj, int val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "}\n\n"
            "bool randomizedCollectionRemove(RandomizedCollection* obj, int val) {\n"
            "    // User logic here\n"
            "    return true;\n"
            "}\n\n"
            "int randomizedCollectionGetRandom(RandomizedCollection* obj) {\n"
            "    // User logic here\n"
            "    return 0;\n"
            "}\n\n"
            "void randomizedCollectionFree(RandomizedCollection* obj) {\n"
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
            "            RandomizedCollection* obj = NULL;\n"
            "            printf(\"[\");\n"
            "            for (int k = 0; k < cmdCount; k++) {\n"
            "                if (k > 0) printf(\",\");\n"
            "                if (strcmp(commands[k], \"RandomizedCollection\") == 0) {\n"
            "                    obj = randomizedCollectionCreate();\n"
            "                    printf(\"null\");\n"
            "                } else if (strcmp(commands[k], \"insert\") == 0) {\n"
            "                    printf(randomizedCollectionInsert(obj, argsArr[k]) ? \"true\" : \"false\");\n"
            "                } else if (strcmp(commands[k], \"remove\") == 0) {\n"
            "                    printf(randomizedCollectionRemove(obj, argsArr[k]) ? \"true\" : \"false\");\n"
            "                } else if (strcmp(commands[k], \"getRandom\") == 0) {\n"
            "                    printf(\"%d\", randomizedCollectionGetRandom(obj));\n"
            "                }\n"
            "            }\n"
            "            printf(\"]\\n\");\n"
            "            if (obj) randomizedCollectionFree(obj);\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
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
