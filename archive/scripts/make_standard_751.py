import json
import os

def generate_json():
    problem_id = 751
    title = "IP to CIDR"
    difficulty = "Medium"
    marks = 20
    
    html_description = """<h3>751. IP to CIDR</h3>
<p>An IPv4 address is a string in the form <code>"x1.x2.x3.x4"</code> where <code>0 &lt;= xi &lt;= 255</code>. CIDR notation is a string in the form <code>"x1.x2.x3.x4/n"</code> where <code>n</code> is an integer <code>0 &lt;= n &lt;= 32</code>.</p>

<p>Given a starting IPv4 address <code>ip</code> and an integer <code>n</code>, return <em>a list of the <strong>shortest</strong> possible CIDR blocks that represent the range of <code>n</code> consecutive IP addresses starting from <code>ip</code></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ip = "255.0.0.7", n = 10
<strong>Output:</strong> ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
<strong>Explanation:</strong>
The IP addresses are:
255.0.0.7  -> 11111111 00000000 00000000 00000111
255.0.0.8  -> 11111111 00000000 00000000 00001000
...
255.0.0.16 -> 11111111 00000000 00000000 00010000
Shortest blocks for [7, 16]:
- 7/32 (1 address)
- 8/29 (8 addresses: 8-15)
- 16/32 (1 address)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ip = "117.145.102.62", n = 8
<strong>Output:</strong> ["117.145.102.62/32","117.145.102.63/32","117.145.102.64/29","117.145.102.72/32"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>ip</code> is a valid IPv4 address.</li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li>Every implied address will be a valid IPv4 address.</li>
</ul>
"""

    input_format = "A string representing the 'ip' and an integer 'n'."
    output_format = "A JSON array of CIDR block strings."
    
    constraints = [
        "ip is a valid IPv4 address.",
        "1 <= n <= 1000",
        "Every address ip + x (x < n) is valid."
    ]
    
    explanation = """To convert an IP range to CIDR blocks efficiently:
1. **IP to Integer**: Convert the dot-notation IPv4 address to a 32-bit integer.
2. **Greedy CIDR Selection**:
   - For the current IP (as an integer), find the number of trailing zeros in its binary representation. This tells us the largest block size allowed by its alignment (e.g., if it ends in `...1000`, it's 8-aligned).
   - The number of addresses in a block with mask `/m` is $2^{32-m}$.
   - We must also ensure the block size doesn't exceed the remaining count `n`.
   - The greedy choice for block size length `L` is `min(largest power of 2 factor of current IP, largest power of 2 <= n)`.
3. **Format Conversion**: Convert the integer back to dot-notation and append the mask `/32 - log2(block_size)`.
4. **Update**: Add the block size to the IP and subtract from `n`.

Time Complexity: O(log N) as we reduce n by at least 1 each step (usually more).
Space Complexity: O(log N) for the size of the result list."""
    
    answer = """def ipToCIDR(ip, n):
    def ipToInt(ip):
        res = 0
        for part in ip.split('.'):
            res = res * 256 + int(part)
        return res
    
    def intToIp(val):
        return "{}.{}.{}.{}".format((val >> 24) & 255, (val >> 16) & 255, (val >> 8) & 255, val & 255)
    
    val = ipToInt(ip)
    res = []
    while n > 0:
        # Find the lowest set bit (rightmost 1)
        # val & -val gives the value of the trailing zero alignment
        # e.g. 0...1000 (8) & -8 => 8.
        # If val is 0, we treat it as 2^32 alignment (but here n is small)
        if val == 0:
            step = 1 << 31
        else:
            step = val & -val
            
        while step > n:
            step >>= 1
            
        # step = 2^(32-mask) => mask = 32 - bit_length(step-1) or similar
        mask = 32
        tmp = step
        while tmp > 1:
            tmp >>= 1
            mask -= 1
            
        res.append(intToIp(val) + "/" + str(mask))
        val += step
        n -= step
        
    return res"""

    boilerplate = {
        "python": "import sys\nimport json\n\ndef ipToCIDR(ip, n):\n    # User logic here\n    pass\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 2:\n        ip = lines[0].strip()\n        n = int(lines[1].strip())\n        print(json.dumps(ipToCIDR(ip, n)))",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n\nusing namespace std;\n\nvector<string> ipToCIDR(string ip, int n) {\n    return {};\n}",
        "java": "import java.util.*;\n\nclass Solution {\n    public List<String> ipToCIDR(String ip, int n) {\n        return new ArrayList<>();\n    }\n}",
        "javascript": "var ipToCIDR = function(ip, n) {\n    return [];\n};",
        "c": "char** ipToCIDR(char* ip, int n, int* returnSize) {\n    return NULL;\n}"
    }

    test_cases = [
        {"input": "255.0.0.7\\n10", "expected_output": "[\"255.0.0.7/32\",\"255.0.0.8/29\",\"255.0.0.16/32\"]", "is_sample": True},
        {"input": "117.145.102.62\\n8", "expected_output": "[\"117.145.102.62/32\",\"117.145.102.63/32\",\"117.145.102.64/29\",\"117.145.102.72/32\"]", "is_sample": True},
        # Diverse cases
        {"input": "255.255.255.255\\n1", "expected_output": "[\"255.255.255.255/32\"]", "is_sample": False},
        {"input": "0.0.0.0\\n1", "expected_output": "[\"0.0.0.0/32\"]", "is_sample": False},
        {"input": "1.1.1.1\\n2", "expected_output": "[\"1.1.1.1/32\",\"1.1.1.2/32\"]", "is_sample": False},
        {"input": "10.0.0.0\\n32", "expected_output": "[\"10.0.0.0/27\"]", "is_sample": False},
        {"input": "192.168.1.0\\n255", "expected_output": "[\"192.168.1.0/25\",\"192.168.1.128/26\",\"192.168.1.192/27\",\"192.168.1.224/28\",\"192.168.1.240/29\",\"192.168.1.248/30\",\"192.168.1.252/31\",\"192.168.1.254/32\"]", "is_sample": False},
        # Stress cases
        {"input": "0.0.0.0\\n1000", "expected_output": "[\"0.0.0.0/23\",\"0.0.2.0/24\",\"0.0.3.0/25\",\"0.0.3.128/26\",\"0.0.3.192/27\",\"0.0.3.224/28\",\"0.0.3.240/31\"]", "is_sample": False},
        {"input": "1.1.1.1\\n1000", "expected_output": "[\"1.1.1.1/32\",\"1.1.1.2/31\",\"1.1.1.4/30\",\"1.1.1.8/29\",\"1.1.1.16/28\",\"1.1.1.32/27\",\"1.1.1.64/26\",\"1.1.1.128/25\",\"1.1.2.0/24\",\"1.1.3.0/25\",\"1.1.3.128/26\",\"1.1.3.192/27\",\"1.1.3.224/28\",\"1.1.3.240/29\",\"1.1.3.248/30\"]", "is_sample": False},
        {"input": "255.255.255.0\\n256", "expected_output": "[\"255.255.255.0/24\"]", "is_sample": False}
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
        "topics": ["String", "Bit Manipulation"],
        "companyIndex": 0
    }

    output_path = "601-800/751_IP_to_CIDR.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
