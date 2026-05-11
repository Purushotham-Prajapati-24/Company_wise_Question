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
        "python": "import sys\nimport json\nimport random\nclass Solution:\n    def __init__(self, nums: list[int]):\n        # User logic here\n        pass\n    def reset(self) -> list[int]:\n        # User logic here\n        return []\n    def shuffle(self) -> list[int]:\n        # User logic here\n        return []\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 2:\n        cmds, args = json.loads(data[0]), json.loads(data[1])\n        obj, res = None, []\n        for c, a in zip(cmds, args):\n            if c == 'Solution':\n                obj = Solution(a[0])\n                res.append(None)\n            elif c == 'reset':\n                res.append(obj.reset())\n            elif c == 'shuffle':\n                res.append(obj.shuffle())\n        print(json.dumps(res).replace(' ', ''))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\n#include <regex>\nusing namespace std;\nclass Solution {\npublic:\n    Solution(vector<int>& nums) {\n        // User logic here\n    }\n    vector<int> reset() {\n        // User logic here\n        return {};\n    }\n    vector<int> shuffle() {\n        // User logic here\n        return {};\n    }\n};\nint main() {\n    string in((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());\n    regex ce(\"\\\\\\\"(.*?)\\\\\\\"\"), ae(\"\\\\[([\\\\d\\\\s,-]*)\\\\]\");\n    auto cit = sregex_iterator(in.begin(), in.end(), ce), ced = sregex_iterator();\n    auto ait = sregex_iterator(in.begin(), in.end(), ae), aed = sregex_iterator();\n    Solution* obj = nullptr; cout << \"[\"; bool first = true;\n    vector<int> nums;\n    if(ait != aed) {\n        string s = ait->str(1);\n        regex ne(\"-?\\\\d+\");\n        for(sregex_iterator nit(s.begin(),s.end(),ne),ned; nit!=ned; ++nit)\n            nums.push_back(stoi(nit->str()));\n        ait++;\n    }\n    while(cit != ced) {\n        string c = cit->str(1); if(!first) cout << \",\";\n        if(c == \"Solution\") { obj = new Solution(nums); cout << \"null\"; }\n        else if(c == \"reset\") {\n            vector<int> r = obj->reset();\n            cout << \"[\"; for(size_t i=0;i<r.size();i++) cout << r[i] << (i==r.size()-1?\"\":\",\"); cout << \"]\";\n        }\n        else if(c == \"shuffle\") {\n            vector<int> r = obj->shuffle();\n            cout << \"[\"; for(size_t i=0;i<r.size();i++) cout << r[i] << (i==r.size()-1?\"\":\",\"); cout << \"]\";\n        }\n        if(ait != aed) ait++;\n        first = false; cit++;\n    }\n    cout << \"]\" << endl;\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\npublic class Main {\n    static class Solution {\n        public Solution(int[] nums) {\n            // User logic here\n        }\n        public int[] reset() {\n            // User logic here\n            return new int[0];\n        }\n        public int[] shuffle() {\n            // User logic here\n            return new int[0];\n        }\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in).useDelimiter(\"\\\\A\"); if(!sc.hasNext()) return;\n        String in = sc.next();\n        Matcher cm = Pattern.compile(\"\\\\\\\"(.*?)\\\\\\\"\").matcher(in);\n        Matcher am = Pattern.compile(\"\\\\[([\\\\d\\\\s,-]*)\\\\]\").matcher(in);\n        int[] nums = new int[0];\n        if(am.find()) {\n            String s = am.group(1);\n            List<Integer> l = new ArrayList<>();\n            Matcher nm = Pattern.compile(\"-?\\\\d+\").matcher(s);\n            while(nm.find()) l.add(Integer.parseInt(nm.group()));\n            nums = l.stream().mapToInt(i->i).toArray();\n        }\n        Solution obj = null; System.out.print(\"[\"); boolean first = true;\n        while(cm.find()) {\n            String c = cm.group(1); if(!first) System.out.print(\",\");\n            if(c.equals(\"Solution\")) { obj = new Solution(nums); System.out.print(\"null\"); }\n            else if(c.equals(\"reset\")) { int[] r = obj.reset(); System.out.print(Arrays.toString(r).replace(\" \", \"\")); }\n            else if(c.equals(\"shuffle\")) { int[] r = obj.shuffle(); System.out.print(Arrays.toString(r).replace(\" \", \"\")); }\n            am.find(); first = false;\n        }\n        System.out.println(\"]\");\n    }\n}",
        "javascript": "const fs = require('fs');\nvar Solution = function(nums) {\n    // User logic here\n};\nSolution.prototype.reset = function() {\n    // User logic here\n    return [];\n};\nSolution.prototype.shuffle = function() {\n    // User logic here\n    return [];\n};\nconst input = fs.readFileSync(0, 'utf8').split('\\n');\nif(input.length >= 2) {\n    const cmds = JSON.parse(input[0]);\n    const args = JSON.parse(input[1]);\n    let obj = null;\n    let res = [];\n    for(let i=0; i<cmds.length; i++) {\n        if(cmds[i] === 'Solution') { obj = new Solution(args[i][0]); res.push(null); }\n        else if(cmds[i] === 'reset') res.push(obj.reset());\n        else if(cmds[i] === 'shuffle') res.push(obj.shuffle());\n    }\n    console.log(JSON.stringify(res).replace(/ /g, ''));\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n#include <ctype.h>\ntypedef struct {\n    // User logic here\n} Solution;\nSolution* solutionCreate(int* nums, int numsSize) {\n    // User logic here\n    return NULL;\n}\nint* solutionReset(Solution* obj, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\nint* solutionShuffle(Solution* obj, int* returnSize) {\n    // User logic here\n    *returnSize = 0;\n    return NULL;\n}\nvoid solutionFree(Solution* obj) {\n    // User logic here\n}\nint main() {\n    char *buf = malloc(2000000);\n    fread(buf, 1, 2000000, stdin);\n    char *cmds = malloc(1000000);\n    char *args = malloc(1000000);\n    char *nl = strchr(buf, '\\n');\n    if (nl) {\n        strncpy(cmds, buf, nl - buf); cmds[nl - buf] = '\\0';\n        strcpy(args, nl + 1);\n    } else {\n        strcpy(cmds, buf);\n    }\n    int nums[1000];\n    int numsSize = 0;\n    char *ap = strchr(args, '[');\n    if(ap) {\n        ap++;\n        char *ap2 = strchr(ap, '[');\n        if (ap2) {\n            ap2++;\n            while(*ap2 && *ap2 != ']') {\n                if(isdigit(*ap2) || (*ap2 == '-' && isdigit(*(ap2+1)))) {\n                    nums[numsSize++] = strtol(ap2, &ap2, 10);\n                } else ap2++;\n            }\n        }\n    }\n    Solution* obj = NULL;\n    printf(\"[\");\n    bool first = true;\n    char *p = cmds;\n    while((p = strchr(p, '\"'))) {\n        p++;\n        char *end = strchr(p, '\"');\n        if(!end) break;\n        char cmd[50];\n        strncpy(cmd, p, end-p);\n        cmd[end-p] = '\\0';\n        if(!first) printf(\",\");\n        if(strcmp(cmd, \"Solution\") == 0) {\n            obj = solutionCreate(nums, numsSize);\n            printf(\"null\");\n        }\n        else if(strcmp(cmd, \"reset\") == 0) {\n            int retSize = 0;\n            int *r = solutionReset(obj, &retSize);\n            printf(\"[\");\n            for(int i=0; i<retSize; i++) {\n                printf(\"%d%s\", r[i], (i==retSize-1?\"\":\",\"));\n            }\n            printf(\"]\");\n        }\n        else if(strcmp(cmd, \"shuffle\") == 0) {\n            int retSize = 0;\n            int *r = solutionShuffle(obj, &retSize);\n            printf(\"[\");\n            for(int i=0; i<retSize; i++) {\n                printf(\"%d%s\", r[i], (i==retSize-1?\"\":\",\"));\n            }\n            printf(\"]\");\n        }\n        first = false;\n        p = end + 1;\n    }\n    printf(\"]\\n\");\n    if(obj) solutionFree(obj);\n    free(buf); free(cmds); free(args);\n    return 0;\n}"
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
