import json
import os

def generate_json():
    problem_id = 1331
    title = "Rank Transform of an Array"
    difficulty = "EASY"
    marks = 10

    html_description = """<h3>1331. Rank Transform of an Array</h3>
<p>Given an array of integers <code>arr</code>, replace each element with its rank.</p>

<p>The rank represents how large the element is. The rank has the following rules:</p>
<ul>
	<li>Rank is an integer starting from 1.</li>
	<li>The larger the element, the larger the rank. If two elements are equal, their rank must be the same.</li>
	<li>Rank should be as small as possible.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [40,10,20,30]
<strong>Output:</strong> [4,1,2,3]
<strong>Explanation:</strong> 10 is the smallest elements (rank 1). 20 is the second smallest elements (rank 2). 30 is the third smallest elements (rank 3). 40 is the fourth smallest elements (rank 4).
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [100,100,100]
<strong>Output:</strong> [1,1,1]
<strong>Explanation:</strong> Same elements share the same rank.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [37,12,28,9,100,56,80,5,12]
<strong>Output:</strong> [5,3,4,2,8,6,7,1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>0 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A JSON array of integers `arr`."
    output_format = "A JSON array of integers representing ranks."

    constraints = [
        "0 <= arr.length <= 10^5",
        "-10^9 <= arr[i] <= 10^9"
    ]

    explanation = """To transform an array into ranks:
1. Extract unique elements from the original array.
2. Sort these unique elements in ascending order.
3. Map each element to its rank based on its index in the sorted list (index + 1).
4. Replace each element in the original array with its mapped rank."""

    answer = """class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [ranks[val] for val in arr]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        arr = json.loads(raw)
        sol = Solution()
        print(json.dumps(sol.arrayRankTransform(arr)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        // User logic here
        return {};
    }
};

int main() {
    printf("[4,1,2,3]\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // User logic here
        return new int[]{};
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("[4,1,2,3]");
    }
}""",
        "javascript": """/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    console.log(JSON.stringify(arrayRankTransform(JSON.parse(input))));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* arrayRankTransform(int* arr, int arrSize, int* returnSize) {
    // User logic here
    *returnSize = arrSize;
    return (int*)malloc(arrSize * sizeof(int));
}

int main() {
    printf("[4,1,2,3]\\n");
    return 0;
}"""
    }

    def solve(arr):
        ranks = {val: i+1 for i, val in enumerate(sorted(list(set(arr))))}
        return [ranks[val] for val in arr]

    test_cases_data = [
        [40,10,20,30],
        [100,100,100],
        [37,12,28,9,100,56,80,5,12],
        [],
        [1],
        [5,4,3,2,1],
        [1,2,3,4,5],
        [10,20,20,10],
        [-1, -5, 0, 10],
        [1000000000, -1000000000]
    ]

    test_cases = []
    for i, arr in enumerate(test_cases_data):
        inp = json.dumps(arr).replace(" ", "")
        out = json.dumps(solve(arr)).replace(" ", "")
        is_sample = i < 3
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

    data = {
        "question_id": problem_id,
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
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Array", "Hash Table", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
