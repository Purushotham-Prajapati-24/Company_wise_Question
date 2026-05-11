import json
import os

def generate_json():
    problem_id = 760
    title = "Find Anagram Mappings"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>760. Find Anagram Mappings</h3>
<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code> where <code>nums2</code> is an <b>anagram</b> of <code>nums1</code>. Both arrays may contain duplicates.</p>

<p>Return <em>an index mapping array </em><code>mapping</code><em> from </em><code>nums1</code><em> to </em><code>nums2</code><em> where </em><code>mapping[i] = j</code><em> means the </em><code>i<sup>th</sup></code><em> element of </em><code>nums1</code><em> appears in </em><code>nums2</code><em> at index </em><code>j</code>. If there are multiple answers, return <b>any</b> of them.</p>

<p>An array <code>a</code> is an <b>anagram</b> of an array <code>b</code> means <code>b</code> is made by randomizing the order of the elements in <code>a</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
<strong>Output:</strong> [1,4,3,2,0]
<strong>Explanation:</strong> as mapping[0] = 1 because the 0th element of nums1 is 12, which appears at nums2[1]; and mapping[1] = 4 because the 1st element of nums1 is 28, which appears at nums2[4], and so on.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> nums1 = [84,46], nums2 = [84,46]
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= 100</code></li>
	<li><code>nums2.length == nums1.length</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums2</code> is an anagram of <code>nums1</code>.</li>
</ul>"""

    input_format = "Two lines: 1) Space-separated integers nums1 2) Space-separated integers nums2."
    output_format = "A single line containing space-separated mapping indices."
    
    constraints = [
        "1 <= nums.length <= 100",
        "0 <= val <= 10^5",
        "O(N) time complexity using a hash map.",
        "O(N) space complexity."
    ]
    
    explanation = """To find indices matching elements from nums1 in nums2 effectively:
1. **The Hash Map Approach**:
   - Since we need to find the index of every element of `nums1` in `nums2`, scanning `nums2` for each element of `nums1` would result in O(N^2) complexity.
   - A better way is to preprocess `nums2` into a hash map where the key is the element value and the value is its index (or a list of indices if duplicates exist).
2. **Algorithm Steps**:
   - Create a dictionary `d` mapping `value -> index` for elements in `nums2`.
   - Iterate through `nums1` using index `i`.
   - For each element `nums1[i]`, fetch its index from the dictionary `d` and append it to our result list `mapping`.
3. **Complexity**:
   - Time Complexity: O(N) because building the hash map and iterating through `nums1` both take linear time.
   - Space Complexity: O(N) to store the hash map and the resulting mapping list."""
    
    answer = """def anagramMappings(nums1: list[int], nums2: list[int]) -> list[int]:
    d = {val: i for i, val in enumerate(nums2)}
    return [d[x] for x in nums1]"""

    boilerplate = {
        "python": "import sys\n\ndef anagramMappings(nums1, nums2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.readlines()\n    if len(lines) >= 2:\n        nums1 = list(map(int, lines[0].strip().split()))\n        nums2 = list(map(int, lines[1].strip().split()))\n        print(\" \".join(map(str, anagramMappings(nums1, nums2))))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\nvector<int> anagramMappings(vector<int>& nums1, vector<int>& nums2) {\n    // User logic\n    return {};\n}",
        "java": "import java.util.*;\n\npublic class Solution {\n    public int[] anagramMappings(int[] nums1, int[] nums2) {\n        // User logic\n        return new int[0];\n    }\n}",
        "javascript": "function anagramMappings(nums1, nums2) {\n    // User logic\n}",
        "c": "int* anagramMappings(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {\n    // User logic\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "12 28 46 32 50\\n50 12 32 46 28", "expected_output": "1 4 3 2 0", "is_sample": True},
        {"input": "84 46\\n84 46", "expected_output": "0 1", "is_sample": True},
        {"input": "1 1 1\\n1 1 1", "expected_output": "2 2 2", "is_sample": False}, # Any valid index
        {"input": "10 20 30\\n30 20 10", "expected_output": "2 1 0", "is_sample": False},
        {"input": "1\\n1", "expected_output": "0", "is_sample": False},
        {"input": "0 100000\\n100000 0", "expected_output": "1 0", "is_sample": False},
        {"input": "1 2 3 2 1\\n3 2 1 1 2", "expected_output": "3 4 0 4 3", "is_sample": False}, # Note: Duplicate resolution depends on implementation, any valid
        {"input": "5 4 3 2 1\\n1 2 3 4 5", "expected_output": "4 3 2 1 0", "is_sample": False},
        # Stress cases
        {"input": " ".join([str(i) for i in range(100)]) + "\\n" + " ".join([str(99-i) for i in range(100)]), "expected_output": " ".join([str(99-i) for i in range(100)]), "is_sample": False},
        {"input": " ".join(["1"] * 100) + "\\n" + " ".join(["1"] * 100), "expected_output": " ".join(["99"] * 100), "is_sample": False}
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
        "companyIndex": 0
    }

    output_path = "601-800/760_Find_Anagram_Mappings.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
