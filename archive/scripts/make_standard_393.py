import json
import os

def generate_json():
    problem_id = 393
    title = "UTF-8 Validation"
    difficulty = "MEDIUM"
    marks = 10
    
    html_description = """<h3>393 UTF-8 Validation</h3>
<p>Given an integer array <code>data</code> representing the data, return <code>true</code> if it is a valid <strong>UTF-8</strong> encoding, otherwise return <code>false</code>.</p>
<p>A character in <strong>UTF8</strong> can be from <strong>1 to 4 bytes</strong> long, subjected to the following rules:</p>
<ol>
    <li>For a 1-byte character, the first bit is a 0, followed by its Unicode code.</li>
    <li>For an n-bytes character, the first n bits are all one's, the n+1 bit is 0, followed by n-1 bytes with the most significant 2 bits being 10.</li>
</ol>
<p>This is how the layout of a multi-byte character looks like:</p>
<pre>   Byte 1          Byte 2          Byte 3          Byte 4
   0xxxxxxx
   110xxxxx    10xxxxxx
   1110xxxx    10xxxxxx    10xxxxxx
   11110xxx    10xxxxxx    10xxxxxx    10xxxxxx
</pre>
<p><code>data</code> is an array of integers. Only the <strong>least significant 8 bits</strong> of each integer is used to store the data. This means each integer represents only 1 byte of data.</p>

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> data = [197,130,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> data represents the octet sequence: 11000101 10000010 00000001.
It is a valid 2-byte character followed by a 1-byte character.</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> data = [235,140,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> data represents the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-byte character.
The next byte is a continuation byte which starts with 10 but the second continuation byte is invalid.</pre>"""

    input_format = """A list of integers representing the data bytes."""
    output_format = """A boolean (true/false) representing if the data is a valid UTF-8 encoding."""
    
    constraints = [
        "1 <= data.length <= 2 * 10^4",
        "0 <= data[i] <= 255"
    ]
    
    explanation = """We iterate through the array, determining how many bytes the current character should have based on its first byte. Then, we check if the subsequent bytes follow the continuation rule (most significant 2 bits are '10')."""
    
    answer = """class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        for num in data:
            bin_rep = format(num, '#010b')[-8:]
            if n_bytes == 0:
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1
                if n_bytes == 0: continue
                if n_bytes == 1 or n_bytes > 4: return False
            else:
                if not (bin_rep.startswith('10')): return False
            n_bytes -= 1
        return n_bytes == 0"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        # User Logic Here
        pass

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            data = json.loads(line)
        except:
            if line.startswith('[') and line.endswith(']'):
                data = [int(x.strip()) for x in line[1:-1].split(',') if x.strip()]
            else:
                data = [int(x) for x in line.split()]
        sol = Solution()
        print(json.dumps(sol.validUtf8(data)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    bool validUtf8(vector<int>& data) {
        // User Logic Here
        return false;
    }
};

int main() {
    string line;
    if (getline(cin, line)) {
        if (!line.empty() && line.front() == '"') line = line.substr(1, line.size()-2);
        if (!line.empty() && line.front() == '[') line = line.substr(1, line.size()-2);
        vector<int> data;
        stringstream ss(line);
        string val;
        while (getline(ss, val, ',')) {
            if (!val.empty()) data.push_back(stoi(val));
        }
        Solution sol;
        cout << (sol.validUtf8(data) ? "true" : "false") << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public boolean validUtf8(int[] data) {
        // User Logic Here
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.startsWith("\\\"")) line = line.substring(1, line.length()-1);
            if (line.startsWith("[")) line = line.substring(1, line.length()-1);
            String[] parts = line.split(",");
            List<Integer> list = new ArrayList<>();
            for (String s : parts) {
                if (!s.trim().isEmpty()) {
                    try {
                        list.add(Integer.parseInt(s.trim()));
                    } catch (NumberFormatException e) {}
                }
            }
            int[] data = new int[list.size()];
            for (int i=0; i<list.size(); i++) data[i] = list.get(i);
            Solution sol = new Solution();
            System.out.println(sol.validUtf8(data));
        }
    }
}""",
        "javascript": """var validUtf8 = function(data) {
    // User Logic Here
};

const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf8').trim();
if (inputData) {
    let data;
    try {
        data = JSON.parse(inputData);
    } catch(e) {
        data = inputData.split(/[\\s,[\\]]+/).filter(x => x).map(Number);
    }
    console.log(validUtf8(data));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool validUtf8(int* data, int dataSize) {
    // User Logic Here
    return false;
}

int main() {
    char line[10000];
    if (fgets(line, 10000, stdin)) {
        int* data = malloc(1000 * sizeof(int));
        int count = 0;
        char *token = strtok(line, "[], ");
        while (token != NULL) {
            data[count++] = atoi(token);
            token = strtok(NULL, "[], ");
        }
        printf("%s\\n", validUtf8(data, count) ? "true" : "false");
        free(data);
    }
    return 0;
}"""
    }

    test_cases = [
        {"input": "[197,130,1]", "expected_output": "true", "is_sample": True},
        {"input": "[235,140,4]", "expected_output": "false", "is_sample": True},
        # 5 Diverse
        {"input": "[0]", "expected_output": "true", "is_sample": False},
        {"input": "[191]", "expected_output": "false", "is_sample": False},
        {"input": "[240,162,138,147]", "expected_output": "true", "is_sample": False},
        {"input": "[248,130,130,130]", "expected_output": "false", "is_sample": False},
        {"input": "[224,130,130]", "expected_output": "true", "is_sample": False},
        # 3 Stress
        {"input": "[224,130]", "expected_output": "false", "is_sample": False},
        {"input": "[255]", "expected_output": "false", "is_sample": False},
        {"input": "[128]", "expected_output": "false", "is_sample": False}
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
        "topics": ["Array", "Bit Manipulation"],
        "companyIndex": 1
    }

    output_path = "301-500/393_UTF-8_Validation.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
