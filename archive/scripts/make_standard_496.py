import json
import os

def generate_json():
    problem_id = 496
    title = "Next Greater Element I"
    difficulty = "EASY"
    marks = 10
    
    html_description = """<h3>496. Next Greater Element I</h3>
<p>The <strong>next greater element</strong> of some element <code>x</code> in an array is the <strong>first greater</strong> element that is <strong>to the right</strong> of <code>x</code> in the same array.</p>

<p>You are given two <strong>distinct 0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code>, where <code>nums1</code> is a subset of <code>nums2</code>.</p>

<p>For each <code>0 &lt;= i &lt; nums1.length</code>, find the index <code>j</code> such that <code>nums1[i] == nums2[j]</code> and determine the <strong>next greater element</strong> of <code>nums2[j]</code> in <code>nums2</code>. If there is no next greater element, then the answer for this query is <code>-1</code>.</p>

<p>Return <em>an array </em><code>ans</code><em> of length </em><code>nums1.length</code><em> such that </em><code>ans[i]</code><em> is the <strong>next greater element</strong> as described above.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums1 = [4,1,2], nums2 = [1,3,4,2]
<strong>Output:</strong> [-1,3,-1]
<strong>Explanation:</strong> The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums1 = [2,4], nums2 = [1,2,3,4]
<strong>Output:</strong> [3,-1]
<strong>Explanation:</strong> The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums1.length &lt;= nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>4</sup></code></li>
	<li>All integers in <code>nums1</code> and <code>nums2</code> are <strong>distinct</strong>.</li>
	<li>All the integers of <code>nums1</code> also appear in <code>nums2</code>.</li>
</ul>"""

    input_format = "Line 1: A JSON array of integers `nums1`.\nLine 2: A JSON array of integers `nums2`."
    output_format = "A JSON array of integers representing the next greater elements for each value in `nums1`."
    
    constraints = [
        "1 <= nums1.length <= nums2.length <= 1000",
        "0 <= nums1[i], nums2[i] <= 10^4",
        "All integers in both arrays are distinct.",
        "nums1 is a subset of nums2."
    ]
    
    explanation = "Use a monotonic stack to find the next greater element for all numbers in `nums2`. Iterate through `nums2`, and for each element, while it is greater than the element at the top of the stack, pop from the stack and map the popped element to the current element. Store these mappings in a hash table. Finally, iterate through `nums1` and retrieve the values from the hash table."
    
    answer = """class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                mapping[stack.pop()] = n
            stack.append(n)
        return [mapping.get(n, -1) for n in nums1]"""

    boilerplate = {
        "python": r"""import sys
import json

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # User Logic Here
        return []

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        nums1 = json.loads(lines[0])
        nums2 = json.loads(lines[1])
        sol = Solution()
        print(json.dumps(sol.nextGreaterElement(nums1, nums2)))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // User Logic Here
        return {};
    }
};

vector<int> parseArray(string s) {
    vector<int> res;
    string cur = "";
    for (char c : s) {
        if (isdigit(c) || c == '-') cur += c;
        else if ((c == ',' || c == ']') && !cur.empty()) {
            res.push_back(stoi(cur));
            cur = "";
        }
    }
    return res;
}

int main() {
    string line1, line2;
    if (getline(cin, line1) && getline(cin, line2)) {
        vector<int> nums1 = parseArray(line1);
        vector<int> nums2 = parseArray(line2);
        Solution sol;
        vector<int> res = sol.nextGreaterElement(nums1, nums2);
        cout << "[";
        for (int i = 0; i < res.size(); i++) {
            cout << res[i] << (i == res.size() - 1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // User Logic Here
        return new int[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line1 = sc.nextLine().trim();
            String line2 = sc.hasNextLine() ? sc.nextLine().trim() : "";
            
            int[] nums1 = parse(line1);
            int[] nums2 = parse(line2);
            
            Solution sol = new Solution();
            int[] res = sol.nextGreaterElement(nums1, nums2);
            System.out.println(Arrays.toString(res).replace(" ", ""));
        }
    }
    
    private static int[] parse(String s) {
        if (s.isEmpty() || s.equals("[]")) return new int[0];
        String clean = s.replaceAll("[\\\\[\\\\]]", "");
        if (clean.isEmpty()) return new int[0];
        String[] parts = clean.split(",");
        int[] res = new int[parts.length];
        for (int i = 0; i < parts.length; i++) res[i] = Integer.parseInt(parts[i].trim());
        return res;
    }
}""",
        "javascript": r"""/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\n');
if (input.length >= 2) {
    const nums1 = JSON.parse(input[0]);
    const nums2 = JSON.parse(input[1]);
    console.log(JSON.stringify(nextGreaterElement(nums1, nums2)));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

int* nextGreaterElement(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    // User Logic Here
    *returnSize = nums1Size;
    return NULL;
}

int main() {
    // Manual parsing logic for two arrays...
    printf("[]\n");
    return 0;
}"""
    }

    test_cases = [
        {"input": "[4,1,2]\n[1,3,4,2]", "expected_output": "[-1, 3, -1]", "is_sample": True},
        {"input": "[2,4]\n[1,2,3,4]", "expected_output": "[3, -1]", "is_sample": True},
        {"input": "[1]\n[1,2]", "expected_output": "[2]", "is_sample": False},
        {"input": "[1,2,3]\n[1,2,3,4,5]", "expected_output": "[2, 3, 4]", "is_sample": False},
        {"input": "[5,4]\n[1,2,3,4,5]", "expected_output": "[-1, -1]", "is_sample": False},
        {"input": "[1,5]\n[1,5,2,3,4]", "expected_output": "[5, -1]", "is_sample": False},
        {"input": "[3,1,4]\n[5,4,3,2,1]", "expected_output": "[-1, -1, -1]", "is_sample": False},
        {"input": "[10,20,30]\n[10,20,30]", "expected_output": "[20, 30, -1]", "is_sample": False},
        {"input": "[100]\n[100]", "expected_output": "[-1]", "is_sample": False},
        {"input": "[1,2,3,4]\n[4,3,2,1,5]", "expected_output": "[5, 5, 5, 5]", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Stack", "Monotonic Stack"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Next_Greater_Element_I.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
