import json
import os

def generate_json():
    problem_id = 128
    title = "Longest Consecutive Sequence"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>128. Longest Consecutive Sequence</h3>
<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>"""

    input_format = "A single line containing space-separated integers."
    output_format = "An integer representing the length of the longest consecutive sequence."
    
    constraints = [
        "0 <= nums.length <= 10^5",
        "-10^9 <= nums[i] <= 10^9."
    ]
    
    explanation = """To find the longest consecutive sequence in O(N) time:
1. **Hash Set for O(1) Lookups**:
   - Insert all numbers into a hash set.
2. **Identify Sequence Starts**:
   - Iterate through each number `num` in the set.
   - A number is the start of a sequence if `num - 1` is not in the set.
3. **Count Sequence Length**:
   - If `num` is a start, keep checking for `num + 1`, `num + 2`, ... in the set to determine the length.
   - Update the maximum length found so far.
4. **Complexity**:
   - Time Complexity: O(N) because each number is visited at most twice (once in the main loop and at most once inside the sequence-building loop).
   - Space Complexity: O(N) to store the set."""
    
    answer = """def longestConsecutive(nums):
    if not nums:
        return 0
        
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak"""

    boilerplate = {
        "python": "import sys\n\ndef longestConsecutive(nums):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    line = sys.stdin.read().strip()\n    if line:\n        nums = list(map(int, line.split()))\n        print(longestConsecutive(nums))\n    else:\n        print(0)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_set>\n#include <sstream>\nusing namespace std;\nint longestConsecutive(vector<int>& nums) {\n    // User logic\n    return 0;\n}\nint main() {\n    string line; if(!getline(cin,line)){cout<<0<<endl;return 0;}\n    istringstream ss(line); vector<int> n; int x;\n    while(ss>>x) n.push_back(x);\n    cout<<longestConsecutive(n)<<endl; return 0;\n}",
        "java": "import java.util.*;\npublic class Main {\n    public static int longestConsecutive(int[] nums) {\n        // User logic\n        return 0;\n    }\n    public static void main(String[] args) {\n        Scanner sc=new Scanner(System.in);\n        if(!sc.hasNextLine()){System.out.println(0);return;}\n        String line=sc.nextLine().trim();\n        if(line.isEmpty()){System.out.println(0);return;}\n        String[] parts=line.split(\"\\\\s+\");\n        int[] n=new int[parts.length];\n        for(int i=0;i<parts.length;i++) n[i]=Integer.parseInt(parts[i]);\n        System.out.println(longestConsecutive(n));\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction longestConsecutive(nums){\n    // User logic\n    return 0;\n}\nconst line=fs.readFileSync(0,'utf8').trim();\nif(!line){console.log(0);}\nelse{console.log(longestConsecutive(line.split(/\\s+/).map(Number)));}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint longestConsecutive(int* nums, int numsSize) {\n    // User logic\n    return 0;\n}\nint main() {\n    char buf[4000000]; if(!fgets(buf,sizeof(buf),stdin)){printf(\"0\\n\");return 0;}\n    if(strlen(buf)<=1){printf(\"0\\n\");return 0;}\n    int arr[100001],cnt=0; char*tok=strtok(buf,\" \\t\\r\\n\");\n    while(tok&&cnt<100001){arr[cnt++]=atoi(tok);tok=strtok(NULL,\" \\t\\r\\n\");}\n    printf(\"%d\\n\",longestConsecutive(arr,cnt)); return 0;\n}"
    }

    test_cases = [
        {"input": "100 4 200 1 3 2", "expected_output": "4", "is_sample": True},
        {"input": "0 3 7 2 5 8 4 6 0 1", "expected_output": "9", "is_sample": True},
        {"input": "", "expected_output": "0", "is_sample": False},
        {"input": "1", "expected_output": "1", "is_sample": False},
        {"input": "1 2 3 4 10 11 12", "expected_output": "4", "is_sample": False},
        {"input": "10 9 8 7 6 5", "expected_output": "6", "is_sample": False},
        {"input": "1 2 0 1", "expected_output": "3", "is_sample": False},
        # Stress cases
        {"input": " ".join(map(str, range(100000))), "expected_output": "100000", "is_sample": False},
        {"input": " ".join([str(i*2) for i in range(50000)]), "expected_output": "1", "is_sample": False},
        {"input": " ".join(map(str, range(50000, 0, -1))) + " " + " ".join(map(str, range(50001, 100001))), "expected_output": "100000", "is_sample": False}
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
        "topics": ["Array", "Hash Table", "Union Find"],
        "companyIndex": 0
    }

    output_path = "1-200/128_Longest_Consecutive_Sequence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
