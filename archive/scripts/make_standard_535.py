import json
import os

def generate_json():
    problem_id = 535
    title = "Encode and Decode TinyURL"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>535. Encode and Decode TinyURL</h3>
<p>TinyURL is a URL shortening service where you enter a URL such as <code>https://leetcode.com/problems/design-tinyurl</code> and it returns a short URL such as <code>http://tinyurl.com/4e9iAk</code>. Design a class to encode a URL and decode a tiny URL.</p>

<p>There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded back to the original URL.</p>

<p>Implement the <code>Solution</code> class:</p>
<ul>
    <li><code>Solution()</code> Initializes the object of the system.</li>
    <li><code>String encode(String longUrl)</code> Returns a tiny URL for the given <code>longUrl</code>.</li>
    <li><code>String decode(String shortUrl)</code> Returns the original long URL for the given <code>shortUrl</code>. It is guaranteed that the given <code>shortUrl</code> was encoded by the same object.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> url = "https://leetcode.com/problems/design-tinyurl"
<strong>Output:</strong> "https://leetcode.com/problems/design-tinyurl"
<strong>Explanation:</strong>
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny URL
string ans = obj.decode(tiny); // returns the original URL (same as input)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= url.length &lt;= 10<sup>4</sup></code></li>
    <li><code>url</code> is guaranteed to be a valid URL.</li>
</ul>"""

    input_format = "A single line: a JSON string containing the URL to encode then decode."
    output_format = "A JSON string: the original URL (decode(encode(url)) must equal url)."

    constraints = [
        "1 <= url.length <= 10^4",
        "url is guaranteed to be a valid URL"
    ]

    explanation = """Use a hash map to store mappings between short codes and original URLs. Generate a unique key (e.g., incrementing counter or random hash) for each URL. The encode function stores the long URL with the key, and decode retrieves it. The short URL can be `http://tinyurl.com/{key}`."""

    answer = """class Codec:
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encode_map:
            short = self.base + str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = short
            self.decode_map[short] = longUrl
        return self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decode_map.get(shortUrl, "")"""

    boilerplate = {
        "python": """import sys
import json

class Codec:
    def encode(self, longUrl: str) -> str:
        # User logic here
        return ""

    def decode(self, shortUrl: str) -> str:
        # User logic here
        return ""

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        url = json.loads(raw)
        codec = Codec()
        tiny = codec.encode(url)
        result = codec.decode(tiny)
        print(json.dumps(result))""",
        "cpp": """#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string encode(string longUrl) {
        // User logic here
        return "";
    }
    string decode(string shortUrl) {
        // User logic here
        return "";
    }
};

int main() {
    string url_str;
    if (getline(cin, url_str)) {
        if (url_str.length() >= 2 && url_str[0] == '"') {
            url_str = url_str.substr(1, url_str.length() - 2);
        }
        Solution sol;
        string tiny = sol.encode(url_str);
        string result = sol.decode(tiny);
        cout << "\\"" << result << "\\"" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public String encode(String longUrl) {
        // User logic here
        return "";
    }
    public String decode(String shortUrl) {
        // User logic here
        return "";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String raw = sc.nextLine().trim();
            if (raw.length() >= 2 && raw.startsWith("\\"")) {
                raw = raw.substring(1, raw.length() - 1);
            }
            Solution sol = new Solution();
            String tiny = sol.encode(raw);
            String result = sol.decode(tiny);
            System.out.println("\\"" + result + "\\"");
        }
    }
}""",
        "javascript": """/**
 * Encodes a URL to a shortened URL.
 * @param {string} longUrl
 * @return {string}
 */
var encode = function(longUrl) {
    // User logic here
};

/**
 * Decodes a shortened URL to its original URL.
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const url = JSON.parse(input);
    const tiny = encode(url);
    const result = decode(tiny);
    console.log(JSON.stringify(result));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_URLS 100
#define MAX_LEN 10001

static char long_urls[MAX_URLS][MAX_LEN];
static char short_urls[MAX_URLS][MAX_LEN];
static int url_count = 0;

char* encode(char* longUrl) {
    // User logic here
    char* result = (char*)malloc(MAX_LEN);
    result[0] = '\\0';
    return result;
}

char* decode(char* shortUrl) {
    // User logic here
    char* result = (char*)malloc(MAX_LEN);
    result[0] = '\\0';
    return result;
}

int main() {
    char raw[MAX_LEN + 2];
    if (fgets(raw, sizeof(raw), stdin)) {
        raw[strcspn(raw, "\\n")] = 0;
        char url[MAX_LEN];
        int len = strlen(raw);
        if (len >= 2 && raw[0] == '"') {
            strncpy(url, raw + 1, len - 2);
            url[len - 2] = '\\0';
        } else {
            strcpy(url, raw);
        }
        char* tiny = encode(url);
        char* result = decode(tiny);
        printf("\\"%s\\"\\n", result ? result : "");
        if (tiny) free(tiny);
        if (result) free(result);
    }
    return 0;
}"""
    }

    test_cases = [
        # Two Leetcode Samples
        {"input": '"https://leetcode.com/problems/design-tinyurl"', "expected_output": '"https://leetcode.com/problems/design-tinyurl"', "is_sample": True},
        {"input": '"https://www.google.com"', "expected_output": '"https://www.google.com"', "is_sample": True},

        # Five Diverse Cases
        {"input": '"https://www.example.com/path/to/resource?query=value&other=123"', "expected_output": '"https://www.example.com/path/to/resource?query=value&other=123"', "is_sample": False},
        {"input": '"http://a.com"', "expected_output": '"http://a.com"', "is_sample": False},
        {"input": '"https://github.com/user/repo/blob/main/README.md"', "expected_output": '"https://github.com/user/repo/blob/main/README.md"', "is_sample": False},
        {"input": '"https://www.youtube.com/watch?v=dQw4w9WgXcQ"', "expected_output": '"https://www.youtube.com/watch?v=dQw4w9WgXcQ"', "is_sample": False},
        {"input": '"https://www.amazon.com/product/dp/B09XYZABC"', "expected_output": '"https://www.amazon.com/product/dp/B09XYZABC"', "is_sample": False},

        # Three Stress Test Cases (long URLs up to constraint limits)
        {"input": '"https://www.example.com/' + 'a' * 9970 + '"', "expected_output": '"https://www.example.com/' + 'a' * 9970 + '"', "is_sample": False},
        {"input": '"https://x.com/' + 'b' * 9984 + '"', "expected_output": '"https://x.com/' + 'b' * 9984 + '"', "is_sample": False},
        {"input": '"https://longdomain.example.org/verylongpath?param=' + 'c' * 9940 + '"', "expected_output": '"https://longdomain.example.org/verylongpath?param=' + 'c' * 9940 + '"', "is_sample": False}
    ]

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
        "metadata": {
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Hash Table", "String", "Design", "Hash Function"],
        "companyIndex": 0
    }

    output_path = f"401-600/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
