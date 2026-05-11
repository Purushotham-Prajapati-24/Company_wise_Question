import json
import os

def generate_json():
    problem_id = 1257
    title = "Smallest Common Region"
    difficulty = "Medium"
    marks = 10
    
    html_description = """<h3>1257. Smallest Common Region</h3>
<p>You are given some lists of <code>regions</code> where the first region of each list includes all other regions in that list.</p>

<p>Naturally, if a region <code>x</code> contains <code>y</code> and <code>y</code> contains <code>z</code>, then <code>x</code> contains <code>z</code>.</p>

<p>Given two regions <code>region1</code> and <code>region2</code>, find the <strong>smallest</strong> region that contains both of them.</p>

<p>If you are given regions <code>r1</code>, <code>r2</code>, and <code>r3</code> such that <code>r1</code> contains <code>r2</code> and <code>r3</code>, then <code>r1</code> will be the smallest common region of <code>r2</code> and <code>r3</code>.</p>

<p>A region <code>x</code> is considered to be in the list of <code>regions</code> if it is in at least one of the sub-lists.</p>

<p>It is guaranteed the smallest common region exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong>
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
<strong>Output:</strong> "North America"
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"
<strong>Output:</strong> "Earth"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= regions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= regions[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= regions[i][j].length, region1.length, region2.length &lt;= 20</code></li>
	<li><code>region1 != region2</code></li>
	<li><code>regions[i][j]</code>, <code>region1</code>, and <code>region2</code> consist of English letters.</li>
</ul>"""

    input_format = "A list of lists regions and two strings region1 and region2."
    output_format = "A string representing the smallest common region."
    
    constraints = [
        "2 <= regions.length <= 10^4",
        "It is guaranteed a common region exists",
        "Hierarchy forms a tree"
    ]
    
    explanation = """To find the smallest common region (Lowest Common Ancestor in a tree):
1. **Build a Parent Map**: Iterate through each sub-list in `regions`. For each sub-list `[parent, child1, child2, ...]`, map every `child` to its `parent`. This effectively creates a tree where each node points to its parent.
2. **Path from Region1**: Starting from `region1`, traverse upwards to the root by repeatedly following the parent pointers. Store all regions encountered in a set (including `region1` itself).
3. **Trace from Region2**: Starting from `region2`, traverse upwards towards the root. The first region encountered that is already in the set from step 2 is the smallest common region.
4. **Complexity**:
   - **Time**: O(N * M), where N is number of sub-lists and M is average length of sub-list, to build the parent map. Finding the LCA takes O(H) where H is the height of the tree.
   - **Space**: O(N * M) to store the parent map and the set of ancestors."""
    
    answer = """def findSmallestRegion(regions, region1, region2):
    parent = {}
    for r in regions:
        p = r[0]
        for c in r[1:]:
            parent[c] = p
            
    # Ancestors of region1
    ancestors = {region1}
    while region1 in parent:
        region1 = parent[region1]
        ancestors.add(region1)
        
    # Check ancestors of region2
    while region2 not in ancestors:
        region2 = parent[region2]
        
    return region2"""

    boilerplate = {
        "python": "import sys, json\n\ndef findSmallestRegion(regions, region1, region2):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().splitlines()\n    if len(data) >= 3:\n        regions = json.loads(data[0])\n        region1 = data[1].strip().strip('\"')\n        region2 = data[2].strip().strip('\"')\n        print(findSmallestRegion(regions, region1, region2))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <unordered_map>\n#include <unordered_set>\n\nusing namespace std;\n\nclass Solution {\npublic:\n    string findSmallestRegion(vector<vector<string>>& regions, string region1, string region2) {\n        // implementation\n        return \"\";\n    }\n};",
        "java": "import java.util.*;\n\nclass Solution {\n    public String findSmallestRegion(List<List<String>> regions, String region1, String region2) {\n        // implementation\n        return \"\";\n    }\n}",
        "javascript": "/**\n * @param {string[][]} regions\n * @param {string} region1\n * @param {string} region2\n * @return {string}\n */\nvar findSmallestRegion = function(regions, region1, region2) {\n    \n};",
        "c": "char * findSmallestRegion(char *** regions, int regionsSize, int* regionsColSize, char * region1, char * region2){\n    \n}"
    }

    test_cases = [
        {"input": '[["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]]\\n"Quebec"\\n"New York"', "expected_output": '"North America"', "is_sample": True},
        {"input": '[["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]]\\n"Canada"\\n"South America"', "expected_output": '"Earth"', "is_sample": True},
        {"input": '[["A","B"],["B","C"],["C","D"]]\\n"D"\\n"C"', "expected_output": '"C"', "is_sample": False},
        {"input": '[["A","B","C"],["B","D"]]\\n"D"\\n"C"', "expected_output": '"A"', "is_sample": False},
        {"input": '[["A","B","C"],["C","E"]]\\n"B"\\n"E"', "expected_output": '"A"', "is_sample": False},
        {"input": '[["A","B"],["A","C"]]\\n"B"\\n"C"', "expected_output": '"A"', "is_sample": False},
        {"input": '[["A","B","C","D","E"]]\\n"B"\\n"E"', "expected_output": '"A"', "is_sample": False},
        {"input": '[["World", "Oceania"], ["Oceania", "Australia", "New Zealand"]]\\n"Australia"\\n"New Zealand"', "expected_output": '"Oceania"', "is_sample": False},
        {"input": '[["Root", "A", "B"], ["A", "C", "D"], ["B", "E", "F"], ["E", "G", "H"]]\\n"G"\\n"F"', "expected_output": '"Root"', "is_sample": False},
        {"input": '[["A", "B"]]\\n"A"\\n"B"', "expected_output": '"A"', "is_sample": False}
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
        "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Hash Table", "String"],
        "companyIndex": 0
    }

    output_path = "1201-1400/1257_Smallest_Common_Region.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
