import json
import os

def generate_json():
    problem_id = 153
    title = "Find Minimum in Rotated Sorted Array"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>153. Find Minimum in Rotated Sorted Array</h3>
<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated 4 times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated 7 times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n)</code> time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] rotated 4 times.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] rotated 4 times. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>"""

    input_format = "A single line containing space-separated integers representing the array nums."
    output_format = "An integer representing the minimum element in the array."
    
    constraints = [
        "1 <= n <= 5000",
        "-5000 <= nums[i] <= 5000",
        "All integers are unique.",
        "Algorithm must be O(log n)."
    ]
    
    explanation = """To find the minimum in a sorted rotated array in O(log N) time:
1. **Binary Search**:
   - The array was originally sorted in ascending order. After rotation, it consists of two sorted subarrays (e.g., [4,5,6,7] and [0,1,2]).
   - The "inflection point" (where the element decreases) is the location of the minimum element.
2. **Logic**:
   - Initialize `left = 0` and `right = n - 1`.
   - If `nums[left] <= nums[right]`, the array is not rotated (or rotated n times), so return `nums[left]`.
   - While `left <= right`:
     - Calculate `mid`.
     - Check if `nums[mid] > nums[mid + 1]`. If so, `nums[mid + 1]` is the minimum.
     - Check if `nums[mid - 1] > nums[mid]`. If so, `nums[mid]` is the minimum.
     - If `nums[mid] > nums[left]`, the left half is sorted, and the inflection point is in the right half (`left = mid + 1`).
     - Otherwise, the inflection point is in the left half (`right = mid - 1`).
3. **Complexity**:
   - Time Complexity: O(log N) due to binary search.
   - Space Complexity: O(1)."""
    
    answer = """def findMin(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
        
    left, right = 0, len(nums) - 1
    
    # If not rotated
    if nums[right] > nums[0]:
        return nums[0]
        
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid+1 is the min
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
            
        # Check if mid is the min
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
            
        # Decide which side to search
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1"""

    boilerplate = {
        "python": "import sys\n\ndef findMin(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().split()\n    if data:\n        print(findMin(list(map(int, data))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <sstream>\nusing namespace std;\nint findMin(vector<int>& nums){\n    // User logic here\n    return 0;\n}\nint main(){\n    string line; if(!getline(cin,line)) return 0;\n    istringstream ss(line); vector<int> nums; int x;\n    while(ss>>x) nums.push_back(x);\n    cout<<findMin(nums)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int findMin(int[] nums){\n        // User logic here\n        return 0;\n    }\n    public static void main(String[] args) throws Exception {\n        java.io.BufferedReader br=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));\n        String line=br.readLine();\n        if(line==null||line.trim().isEmpty()) return;\n        String[] parts=line.trim().split(\"\\\\s+\");\n        int[] nums=new int[parts.length];\n        for(int i=0;i<parts.length;i++) nums[i]=Integer.parseInt(parts[i]);\n        System.out.println(findMin(nums));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction findMin(nums){\n    // User logic here\n    return 0;\n}\nconst nums=fs.readFileSync(0,'utf8').trim().split(/\\s+/).map(Number);\nif(nums.length) console.log(findMin(nums));",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint findMin(int* nums, int numsSize){\n    // User logic here\n    return 0;\n}\nint main(){\n    char buf[100000]; if(!fgets(buf,sizeof(buf),stdin)) return 0;\n    int nums[5001]; int cnt=0;\n    char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<5001){nums[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",findMin(nums,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "3 4 5 1 2", "expected_output": "1", "is_sample": True},
        {"input": "4 5 6 7 0 1 2", "expected_output": "0", "is_sample": True},
        {"input": "11 13 15 17", "expected_output": "11", "is_sample": True},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "2 1", "expected_output": "1", "is_sample": False},
        {"input": "5 1 2 3 4", "expected_output": "1", "is_sample": False},
        {"input": "2 3 4 5 1", "expected_output": "1", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(2, 5001)] + ["1"]), "expected_output": "1", "is_sample": False},
        {"input": " ".join(["5000"] + [str(i) for i in range(-5000, 4999)]), "expected_output": "-5000", "is_sample": False},
        {"input": " ".join([str(i) for i in range(-5000, 1)]), "expected_output": "-5000", "is_sample": False}
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
        "topics": ["Array", "Binary Search"],
        "companyIndex": 0
    }

    output_path = "1-200/153_Find_Minimum_in_Rotated_Sorted_Array.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
