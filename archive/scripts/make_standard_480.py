import json
import os

def generate_json():
    problem_id = 480
    title = "Sliding Window Median"
    difficulty = "HARD"
    marks = 10
    
    html_description = """<h3>480. Sliding Window Median</h3>
<p>The <strong>median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.</p>

<ul>
	<li>For example, if <code>arr = [2,3,4]</code>, the median is <code>3</code>.</li>
	<li>For example, if <code>arr = [1,2,3,4]</code>, the median is <code>(2 + 3) / 2 = 2.5</code>.</li>
</ul>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. There is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.</p>

<p>Return <em>the median array for each window in the original array</em>. Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
<strong>Explanation:</strong> 
Window position                Median
---------------                ------
[1  3  -1] -3  5  3  6  7       1.0
 1 [3  -1  -3] 5  3  6  7      -1.0
 1  3 [-1  -3  5] 3  6  7      -1.0
 1  3  -1 [-3  5  3] 6  7       3.0
 1  3  -1  -3 [5  3  6] 7       5.0
 1  3  -1  -3  5 [3  6  7]      6.0
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4,2,3,1,4,2], k = 3
<strong>Output:</strong> [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>"""

    input_format = "Line 1: A JSON array of integers `nums`.\\nLine 2: An integer `k`."
    output_format = "A JSON array of doubles representing the medians for each window."
    
    constraints = [
        "1 <= k <= nums.length <= 10^5",
        "-2^31 <= nums[i] <= 2^31 - 1"
    ]
    
    explanation = "To find the median of a sliding window efficiently, we can use two heaps (a max-heap for the smaller half and a min-heap for the larger half) along with a hash map for lazy removal of elements that are no longer in the window. Alternatively, a balanced BST or a `multiset` (in C++) can be used."
    
    answer = """import heapq
import collections

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = [] # max heap
        large = [] # min heap
        delayed = collections.Counter()
        
        def prune(heap, sign):
            while heap and delayed[sign * heap[0]] > 0:
                delayed[sign * heapq.heappop(heap)] -= 1
        
        def rebalance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune(small, -1)
            elif large_size > small_size:
                heapq.heappush(small, -heapq.heappop(large))
                large_size -= 1
                small_size += 1
                prune(large, 1)

        small_size = 0
        large_size = 0
        
        for i in range(k):
            heapq.heappush(small, -nums[i])
            small_size += 1
        for _ in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))
            small_size -= 1
            large_size += 1
            
        res = []
        def get_median():
            if k % 2 == 1: return float(-small[0])
            return (-small[0] + large[0]) / 2.0
        
        res.append(get_median())
        
        for i in range(k, len(nums)):
            out_val = nums[i-k]
            in_val = nums[i]
            
            balance = 0
            if out_val <= -small[0]:
                balance -= 1
            else:
                balance += 1
            
            delayed[out_val] += 1
            prune(small, -1)
            prune(large, 1)
            
            if small and in_val <= -small[0]:
                heapq.heappush(small, -in_val)
                balance += 1
            else:
                heapq.heappush(large, in_val)
                balance -= 1
                
            if balance > 0: small_size += 1
            elif balance < 0: large_size += 1
            
            rebalance()
            prune(small, -1)
            prune(large, 1)
            res.append(get_median())
            
        return res"""

    boilerplate = {
        "python": r"""import sys
import json
import heapq
import collections

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        # User Logic Here
        return []

if __name__ == '__main__':
    lines = sys.stdin.read().strip().splitlines()
    if len(lines) >= 2:
        nums = json.loads(lines[0])
        k = int(lines[1])
        sol = Solution()
        print(json.dumps([float(x) for x in sol.medianSlidingWindow(nums, k)]))""",
        "cpp": r"""#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <iomanip>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        // User Logic Here
        return {};
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        vector<int> nums;
        string current;
        for (char c : line) {
            if (isdigit(c) || c == '-') current += c;
            else if (!current.empty()) {
                nums.push_back(stoi(current));
                current = "";
            }
        }
        if (!current.empty()) nums.push_back(stoi(current));
        int k;
        cin >> k;
        Solution sol;
        vector<double> res = sol.medianSlidingWindow(nums, k);
        cout << "[";
        for (int i = 0; i < res.size(); i++) {
            cout << fixed << setprecision(5) << res[i] << (i == res.size() - 1 ? "" : ",");
        }
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": r"""import java.util.*;

class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        // User Logic Here
        return new double[0];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            String[] parts = line.replaceAll("[\\\\[\\\\]\\\\s]", "").split(",");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                Solution sol = new Solution();
                double[] res = sol.medianSlidingWindow(nums, k);
                System.out.print("[");
                for (int i = 0; i < res.length; i++) {
                    System.out.print(String.format("%.5f", res[i]) + (i == res.length - 1 ? "" : ","));
                }
                System.out.println("]");
            }
        }
    }
}""",
        "javascript": r"""/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function(nums, k) {
    // User Logic Here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');
if (input.length >= 2) {
    const nums = JSON.parse(input[0]);
    const k = parseInt(input[1]);
    const res = medianSlidingWindow(nums, k);
    console.log(JSON.stringify(res.map(x => parseFloat(x))));
}""",
        "c": r"""#include <stdio.h>
#include <stdlib.h>

double* medianSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    // User Logic Here
    return NULL;
}

int main() {
    // Manual parsing logic...
    return 0;
}"""
    }

    test_cases = [
        {"input": "[1,3,-1,-3,5,3,6,7]\\n3", "expected_output": "[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]", "is_sample": True},
        {"input": "[1,2,3,4,2,3,1,4,2]\\n3", "expected_output": "[2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]", "is_sample": True},
        {"input": "[1, 4, 2, 3]\\n4", "expected_output": "[2.5]", "is_sample": False},
        {"input": "[5, 5, 5, 5]\\n2", "expected_output": "[5.0, 5.0, 5.0]", "is_sample": False},
        {"input": "[-1, -2, -3, -4]\\n3", "expected_output": "[-2.0, -3.0]", "is_sample": False},
        {"input": "[ 10 ]\\n1", "expected_output": "[10.0]", "is_sample": False}, # Spaces
        {"input": "[1,2,3,4,5,6]\\n1", "expected_output": "[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]", "is_sample": False},
        {"input": "[2147483647, -2147483648]\\n2", "expected_output": "[-0.5]", "is_sample": False},
        # Stress
        {"input": json.dumps([i for i in range(500)]) + "\\n250", "expected_output": json.dumps([float(i + 124.5) for i in range(251)]), "is_sample": False},
        {"input": json.dumps([0]*1000) + "\\n500", "expected_output": json.dumps([0.0]*501), "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"],
        "companyIndex": 1
    }

    output_path = f"401-600/{problem_id}_Sliding_Window_Median.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
