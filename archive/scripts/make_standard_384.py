import json
import os

def generate_json():
    problem_id = 384
    title = "Shuffle an Array"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>384. Shuffle an Array</h3>
<p>Given an integer array <code>nums</code>, design an algorithm to randomly shuffle the array. All permutations of the array should be <strong>equally likely</strong>.</p>

<p>Implement the <code>Solution</code> class:</p>
<ul>
	<li><code>Solution(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
	<li><code>int[] reset()</code> Resets the array to its original configuration and returns it.</li>
	<li><code>int[] shuffle()</code> Returns a random shuffling of the array.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong>
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
<strong>Output:</strong>
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
<strong>Explanation:</strong>
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li>All the elements of <code>nums</code> are <strong>unique</strong>.</li>
	<li>At most <code>5 * 10<sup>4</sup></code> calls in total will be made to <code>reset</code> and <code>shuffle</code>.</li>
</ul>"""

    input_format = "An integer array `nums` and calls to `shuffle`/`reset`."
    output_format = "The shuffled or reset array as a JSON array."
    
    constraints = [
        "1 <= nums.length <= 200",
        "Calls up to 50,000.",
        "Equally likely permutations mean O(N) shuffle."
    ]
    
    explanation = """To generate a random permutation of an array such that all permutations are equally likely, we use the **Fisher-Yates (Knuth) Shuffle** algorithm.

### Algorithm Steps:
- **`Solution(nums)`**:
  - Store a copy of the original array: `self.original = list(nums)`.
  - Maintain the current array for shuffling: `self.array = list(nums)`.
- **`reset()`**:
  - Reset `self.array` to `self.original`.
  - Return `self.array`.
- **`shuffle()`**:
  - Iterate through the array from index 0 to n-1.
  - Pick a random index `j` such that $i \\le j \\le n-1$.
  - Swap `self.array[i]` and `self.array[j]`.
  - Return resulting array.

### Complexity Analysis:
- **Time Complexity**:
  - `reset()`: $O(N)$ to copy or return the array.
  - `shuffle()`: $O(N)$ as we iterate through the list once and swap in $O(1)$.
- **Space Complexity**: $O(N)$ for storing the original configuration."""
    
    answer = """import random

def solution_driver(nums, commands, args):
    original = list(nums)
    array = list(nums)
    output = []
    for i in range(len(commands)):
        if commands[i] == 'Solution':
            array = list(nums)
            output.append(None)
        elif commands[i] == 'reset':
            array = list(original)
            output.append(list(array))
        elif commands[i] == 'shuffle':
            for j in range(len(array)):
                swap_idx = random.randrange(j, len(array))
                array[j], array[swap_idx] = array[swap_idx], array[j]
            output.append(list(array))
    return output"""

    boilerplate = {
        "python": (
            "import sys\n"
            "import json\n"
            "import random\n\n"
            "class Solution:\n"
            "    def __init__(self, nums: list):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def reset(self) -> list:\n"
            "        # User logic here\n"
            "        return []\n\n"
            "    def shuffle(self) -> list:\n"
            "        # User logic here\n"
            "        return []\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().strip().splitlines()\n"
            "    if len(lines) >= 2:\n"
            "        commands = json.loads(lines[0])\n"
            "        args = json.loads(lines[1])\n"
            "        obj = None\n"
            "        output = []\n"
            "        for i in range(len(commands)):\n"
            "            if commands[i] == 'Solution':\n"
            "                obj = Solution(args[i][0])\n"
            "                output.append(None)\n"
            "            elif commands[i] == 'reset':\n"
            "                output.append(obj.reset())\n"
            "            elif commands[i] == 'shuffle':\n"
            "                output.append(obj.shuffle())\n"
            "        print(json.dumps(output).replace(' ', ''))\n"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <string>\n"
            "#include <algorithm>\n"
            "#include <cstdlib>\n"
            "#include <ctime>\n"
            "using namespace std;\n\n"
            "class Solution {\n"
            "public:\n"
            "    Solution(vector<int>& nums) {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    vector<int> reset() {\n"
            "        // User logic here\n"
            "        return {};\n"
            "    }\n"
            "    \n"
            "    vector<int> shuffle() {\n"
            "        // User logic here\n"
            "        return {};\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    srand(time(0));\n"
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
            "            // Parse args: first element is [[nums_array]], rest are []\n"
            "            vector<int> nums;\n"
            "            int depth = 0, idx = 0;\n"
            "            while (idx < line2.length() && depth < 3) {\n"
            "                if (line2[idx] == '[') depth++;\n"
            "                idx++;\n"
            "            }\n"
            "            // Now parse numbers until we close the innermost bracket\n"
            "            while (idx < line2.length() && line2[idx] != ']') {\n"
            "                if (line2[idx] == '-' || (line2[idx] >= '0' && line2[idx] <= '9')) {\n"
            "                    int v = 0, sign = 1;\n"
            "                    if (line2[idx] == '-') { sign = -1; idx++; }\n"
            "                    while (idx < line2.length() && line2[idx] >= '0' && line2[idx] <= '9') {\n"
            "                        v = v * 10 + (line2[idx] - '0'); idx++;\n"
            "                    }\n"
            "                    nums.push_back(v * sign);\n"
            "                    idx--;\n"
            "                }\n"
            "                idx++;\n"
            "            }\n"
            "            Solution* obj = nullptr;\n"
            "            cout << \"[\";\n"
            "            for (int k = 0; k < commands.size(); k++) {\n"
            "                if (k > 0) cout << \",\";\n"
            "                if (commands[k] == \"Solution\") {\n"
            "                    obj = new Solution(nums);\n"
            "                    cout << \"null\";\n"
            "                } else if (commands[k] == \"reset\") {\n"
            "                    auto res = obj->reset();\n"
            "                    cout << \"[\";\n"
            "                    for (int j = 0; j < res.size(); j++) {\n"
            "                        if (j > 0) cout << \",\";\n"
            "                        cout << res[j];\n"
            "                    }\n"
            "                    cout << \"]\";\n"
            "                } else if (commands[k] == \"shuffle\") {\n"
            "                    auto res = obj->shuffle();\n"
            "                    cout << \"[\";\n"
            "                    for (int j = 0; j < res.size(); j++) {\n"
            "                        if (j > 0) cout << \",\";\n"
            "                        cout << res[j];\n"
            "                    }\n"
            "                    cout << \"]\";\n"
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
            "class Solution {\n"
            "    public Solution(int[] nums) {\n"
            "        // User logic here\n"
            "    }\n"
            "    \n"
            "    public int[] reset() {\n"
            "        // User logic here\n"
            "        return new int[0];\n"
            "    }\n"
            "    \n"
            "    public int[] shuffle() {\n"
            "        // User logic here\n"
            "        return new int[0];\n"
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
            "                // Parse the innermost array (nums)\n"
            "                List<Integer> numsList = new ArrayList<>();\n"
            "                int depth = 0, idx = 0;\n"
            "                while (idx < line2.length() && depth < 3) {\n"
            "                    if (line2.charAt(idx) == '[') depth++;\n"
            "                    idx++;\n"
            "                }\n"
            "                while (idx < line2.length() && line2.charAt(idx) != ']') {\n"
            "                    char c = line2.charAt(idx);\n"
            "                    if (c == '-' || (c >= '0' && c <= '9')) {\n"
            "                        int v = 0, sign = 1;\n"
            "                        if (c == '-') { sign = -1; idx++; }\n"
            "                        while (idx < line2.length() && line2.charAt(idx) >= '0' && line2.charAt(idx) <= '9') {\n"
            "                            v = v * 10 + (line2.charAt(idx) - '0'); idx++;\n"
            "                        }\n"
            "                        numsList.add(v * sign);\n"
            "                        idx--;\n"
            "                    }\n"
            "                    idx++;\n"
            "                }\n"
            "                int[] nums = new int[numsList.size()];\n"
            "                for (int k = 0; k < numsList.size(); k++) nums[k] = numsList.get(k);\n"
            "                Solution obj = null;\n"
            "                System.out.print(\"[\");\n"
            "                for (int k = 0; k < commands.size(); k++) {\n"
            "                    if (k > 0) System.out.print(\",\");\n"
            "                    String cmd = commands.get(k);\n"
            "                    if (cmd.equals(\"Solution\")) {\n"
            "                        obj = new Solution(nums);\n"
            "                        System.out.print(\"null\");\n"
            "                    } else if (cmd.equals(\"reset\")) {\n"
            "                        int[] res = obj.reset();\n"
            "                        System.out.print(\"[\");\n"
            "                        for (int j = 0; j < res.length; j++) {\n"
            "                            if (j > 0) System.out.print(\",\");\n"
            "                            System.out.print(res[j]);\n"
            "                        }\n"
            "                        System.out.print(\"]\");\n"
            "                    } else if (cmd.equals(\"shuffle\")) {\n"
            "                        int[] res = obj.shuffle();\n"
            "                        System.out.print(\"[\");\n"
            "                        for (int j = 0; j < res.length; j++) {\n"
            "                            if (j > 0) System.out.print(\",\");\n"
            "                            System.out.print(res[j]);\n"
            "                        }\n"
            "                        System.out.print(\"]\");\n"
            "                    }\n"
            "                }\n"
            "                System.out.println(\"]\");\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        "javascript": (
            "/**\n"
            " * @param {number[]} nums\n"
            " */\n"
            "var Solution = function(nums) {\n"
            "    // User logic here\n"
            "};\n\n"
            "/**\n"
            " * @return {number[]}\n"
            " */\n"
            "Solution.prototype.reset = function() {\n"
            "    // User logic here\n"
            "    return [];\n"
            "};\n\n"
            "/**\n"
            " * @return {number[]}\n"
            " */\n"
            "Solution.prototype.shuffle = function() {\n"
            "    // User logic here\n"
            "    return [];\n"
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
            "            if (commands[i] === 'Solution') {\n"
            "                obj = new Solution(args[i][0]);\n"
            "                output.push(null);\n"
            "            } else if (commands[i] === 'reset') {\n"
            "                output.push(obj.reset());\n"
            "            } else if (commands[i] === 'shuffle') {\n"
            "                output.push(obj.shuffle());\n"
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
            "#include <string.h>\n"
            "#include <time.h>\n\n"
            "typedef struct {\n"
            "    // User logic here\n"
            "} Solution;\n\n"
            "Solution* solutionCreate(int* nums, int numsSize) {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "int* solutionReset(Solution* obj, int* returnSize) {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "int* solutionShuffle(Solution* obj, int* returnSize) {\n"
            "    // User logic here\n"
            "    return NULL;\n"
            "}\n\n"
            "void solutionFree(Solution* obj) {\n"
            "    // User logic here\n"
            "}\n\n"
            "int main() {\n"
            "    srand(time(0));\n"
            "    char line1[50000];\n"
            "    if (fgets(line1, sizeof(line1), stdin)) {\n"
            "        char* commands[10000];\n"
            "        int cmdCount = 0, i = 0;\n"
            "        while (line1[i]) {\n"
            "            if (line1[i] == '\"') {\n"
            "                int j = i + 1;\n"
            "                while (line1[j] && line1[j] != '\"') j++;\n"
            "                line1[j] = '\\0';\n"
            "                commands[cmdCount++] = line1 + i + 1;\n"
            "                i = j;\n"
            "            }\n"
            "            i++;\n"
            "        }\n"
            "        char line2[50000];\n"
            "        if (fgets(line2, sizeof(line2), stdin)) {\n"
            "            // Parse innermost array (nums)\n"
            "            int nums[200], numsSize = 0, depth = 0;\n"
            "            i = 0;\n"
            "            while (line2[i] && depth < 3) {\n"
            "                if (line2[i] == '[') depth++;\n"
            "                i++;\n"
            "            }\n"
            "            while (line2[i] && line2[i] != ']') {\n"
            "                if (line2[i] == '-' || (line2[i] >= '0' && line2[i] <= '9')) {\n"
            "                    int v = 0, sign = 1;\n"
            "                    if (line2[i] == '-') { sign = -1; i++; }\n"
            "                    while (line2[i] >= '0' && line2[i] <= '9') {\n"
            "                        v = v * 10 + (line2[i] - '0'); i++;\n"
            "                    }\n"
            "                    nums[numsSize++] = v * sign;\n"
            "                    i--;\n"
            "                }\n"
            "                i++;\n"
            "            }\n"
            "            Solution* obj = NULL;\n"
            "            printf(\"[\");\n"
            "            for (int k = 0; k < cmdCount; k++) {\n"
            "                if (k > 0) printf(\",\");\n"
            "                if (strcmp(commands[k], \"Solution\") == 0) {\n"
            "                    obj = solutionCreate(nums, numsSize);\n"
            "                    printf(\"null\");\n"
            "                } else if (strcmp(commands[k], \"reset\") == 0) {\n"
            "                    int retSize = 0;\n"
            "                    int* res = solutionReset(obj, &retSize);\n"
            "                    printf(\"[\");\n"
            "                    for (int j = 0; j < retSize; j++) {\n"
            "                        if (j > 0) printf(\",\");\n"
            "                        printf(\"%d\", res[j]);\n"
            "                    }\n"
            "                    printf(\"]\");\n"
            "                } else if (strcmp(commands[k], \"shuffle\") == 0) {\n"
            "                    int retSize = 0;\n"
            "                    int* res = solutionShuffle(obj, &retSize);\n"
            "                    printf(\"[\");\n"
            "                    for (int j = 0; j < retSize; j++) {\n"
            "                        if (j > 0) printf(\",\");\n"
            "                        printf(\"%d\", res[j]);\n"
            "                    }\n"
            "                    printf(\"]\");\n"
            "                }\n"
            "            }\n"
            "            printf(\"]\\n\");\n"
            "            if (obj) solutionFree(obj);\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}\n"
        )
    }

    # NOTE: shuffle() output is non-deterministic; expected_output for shuffle calls
    # uses null (graded by checking it's a valid permutation, not exact match).
    # reset() is deterministic and can be checked exactly.
    test_cases = [
        # Sample cases (2)
        {"input": '["Solution", "shuffle", "reset", "shuffle"]\n[[[1, 2, 3]], [], [], []]', "expected_output": "[null,null,[1,2,3],null]", "is_sample": True},
        {"input": '["Solution", "reset", "shuffle"]\n[[[1]], [], []]', "expected_output": "[null,[1],null]", "is_sample": True},
        # Diverse cases (5)
        {"input": '["Solution", "shuffle", "reset"]\n[[[10, 20]], [], []]', "expected_output": "[null,null,[10,20]]", "is_sample": False},
        {"input": '["Solution", "shuffle"]\n[[[-1, -2, -3]], []]', "expected_output": "[null,null]", "is_sample": False},
        {"input": '["Solution", "shuffle", "reset"]\n[[[1, 2, 3, 4, 5]], [], []]', "expected_output": "[null,null,[1,2,3,4,5]]", "is_sample": False},
        {"input": '["Solution", "reset"]\n[[[7, 8, 9]], []]', "expected_output": "[null,[7,8,9]]", "is_sample": False},
        {"input": '["Solution", "shuffle", "shuffle", "reset"]\n[[[1, 2]], [], [], []]', "expected_output": "[null,null,null,[1,2]]", "is_sample": False},
        # Stress cases (3)
        {"input": '["Solution", "shuffle", "reset", "shuffle", "reset"]\n[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [], [], [], []]', "expected_output": "[null,null,[1,2,3,4,5,6,7,8,9,10],null,[1,2,3,4,5,6,7,8,9,10]]", "is_sample": False},
        {"input": '["Solution", "shuffle", "shuffle", "shuffle", "reset"]\n[[[100, 200, 300, 400, 500]], [], [], [], []]', "expected_output": "[null,null,null,null,[100,200,300,400,500]]", "is_sample": False},
        {"input": '["Solution", "reset", "reset", "reset"]\n[[[5, 4, 3, 2, 1]], [], [], []]', "expected_output": "[null,[5,4,3,2,1],[5,4,3,2,1],[5,4,3,2,1]]", "is_sample": False},
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
        "topics": ["Array", "Math", "Design", "Randomized"],
        "companyIndex": 1
    }

    output_path = "301-500/384_Shuffle_an_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
