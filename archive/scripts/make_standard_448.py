import json
import os

def generate_json():
    problem_id = 448
    title = "Find All Numbers Disappeared in an Array"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>448. Find All Numbers Disappeared in an Array</h3>
<p>Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.</p>"""

    input_format = "A JSON array of integers `nums`."
    output_format = "A JSON array of the disappeared numbers (sorted in ascending order)."
    
    constraints = [
        "n == nums.length",
        "1 <= n <= 10^5",
        "1 <= nums[i] <= n"
    ]
    
    explanation = "Mark the presence of each element by negating the value at the corresponding index. Iterate through the array; for each `nums[i]`, find the index `idx = abs(nums[i]) - 1` and set `nums[idx] = -abs(nums[idx])`. Finally, collect all indices `j` such that `nums[j] > 0`, and return `j+1`."
    
    answer = """class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i, n in enumerate(nums) if n > 0]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # User Logic Here
        return []

if __name__ == '__main__':
    raw_input = sys.stdin.read().strip()
    if raw_input:
        try:
            nums = json.loads(raw_input)
            sol = Solution()
            print(json.dumps(sol.findDisappearedNumbers(nums)).replace(" ", ""))
        except:
            print("[]")
    else:
        print("[]")""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        // User Logic Here
        return {};
    }
};

int main() {
    string input;
    if (getline(cin, input)) {
        vector<int> nums;
        string current;
        for (char c : input) {
            if (isdigit(c) || c == '-') current += c;
            else if (!current.empty()) {
                nums.push_back(stoi(current));
                current = "";
            }
        }
        if (!current.empty()) nums.push_back(stoi(current));
        
        Solution sol;
        vector<int> result = sol.findDisappearedNumbers(nums);
        cout << "[";
        for (int i = 0; i < result.size(); ++i) {
            cout << result[i] << (i == result.size() - 1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // User Logic Here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String input = sc.nextLine();
            String[] parts = input.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
            int[] nums;
            if (parts.length == 1 && parts[0].isEmpty()) {
                nums = new int[0];
            } else {
                nums = new int[parts.length];
                for (int i = 0; i < parts.length; i++) {
                    nums[i] = Integer.parseInt(parts[i]);
                }
            }
            Solution sol = new Solution();
            List<Integer> result = sol.findDisappearedNumbers(nums);
            StringBuilder sb = new StringBuilder("[");
            for (int i = 0; i < result.size(); i++) {
                sb.append(result.get(i));
                if (i < result.size() - 1) sb.append(",");
            }
            sb.append("]");
            System.out.println(sb.toString());
        }
    }
}""",
        "javascript": """/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    try {
        const nums = JSON.parse(input);
        console.log(JSON.stringify(findDisappearedNumbers(nums)).replace(/\\s/g, ''));
    } catch (e) {
        console.log("[]");
    }
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    // User Logic Here
    return NULL;
}

int main() {
    char* line = NULL;
    size_t len = 0;
    if (getline(&line, &len, stdin) != -1) {
        int* nums = malloc(100005 * sizeof(int));
        int numsSize = 0;
        char* p = line;
        while (*p) {
            if (isdigit(*p) || *p == '-') {
                nums[numsSize++] = strtol(p, &p, 10);
            } else {
                p++;
            }
        }
        int returnSize = 0;
        int* result = findDisappearedNumbers(nums, numsSize, &returnSize);
        printf("[");
        for (int i = 0; i < returnSize; i++) {
            printf("%d%s", result[i], i == returnSize - 1 ? "" : ",");
        }
        printf("]\\n");
        free(nums);
        if (result) free(result);
    }
    free(line);
    return 0;
}"""
    }

    test_cases = [
        {"input": "[4,3,2,7,8,2,3,1]", "expected_output": "[5,6]", "is_sample": True},
        {"input": "[1,1]", "expected_output": "[2]", "is_sample": True},
        {"input": "[2,2]", "expected_output": "[1]", "is_sample": False},
        {"input": "[1]", "expected_output": "[]", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "[]", "is_sample": False},
        {"input": "[  3, 3, 3  ]", "expected_output": "[1,2]", "is_sample": False}, # Spaces
        {"input": "[1,1,1]", "expected_output": "[2,3]", "is_sample": False},
        {"input": "[5,4,3,2,1]", "expected_output": "[]", "is_sample": False},
        # Stress cases
        {"input": json.dumps(list(range(1, 10001))), "expected_output": "[]", "is_sample": False},
        {"input": json.dumps([1]*1000 + [5]*500), "expected_output": json.dumps([i for i in range(1, 1501) if i != 1 and i != 5]).replace(" ", ""), "is_sample": False}
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
        "topics": ["Array", "Hash Table"],
        "companyIndex": 1
    }

    output_path = f"301-500/{problem_id}_Find_All_Numbers_Disappeared_in_an_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
