import json
import os

def generate_json():
    problem_id = 692
    title = "Top K Frequent Words"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>692. Top K Frequent Words</h3>
<p>Given an array of strings <code>words</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent strings</em>.</p>

<p>Return the answer <strong>sorted</strong> by <strong>the frequency</strong> from highest to lowest. Sort the words with the same frequency by their <strong>lexicographical order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["i","love","leetcode","i","love","coding"], k = 2
<strong>Output:</strong> ["i","love"]
<strong>Explanation:</strong> "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
<strong>Output:</strong> ["the","is","sunny","day"]
<strong>Explanation:</strong> "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>1 &lt;= words.length &lt;= 500</code></li>
    <li><code>1 &lt;= words[i].length &lt;= 10</code></li>
    <li><code>words[i]</code> consists of lowercase English letters.</li>
    <li><code>k</code> is in the range <code>[1, The number of unique words[i]]</code>.</li>
</ul>"""

    input_format = "Two lines:\nLine 1: JSON array of strings `words`.\nLine 2: Integer `k`."
    output_format = "A JSON array of k strings: the top k frequent words."

    constraints = [
        "1 <= words.length <= 500",
        "1 <= words[i].length <= 10",
        "words[i] consists of lowercase English letters"
    ]

    explanation = """Count frequency of each word. Sort by (-frequency, word) to sort descending by frequency and ascending lexicographically for ties. Return the first k words."""

    answer = """from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        return sorted(count, key=lambda w: (-count[w], w))[:k]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip().split('\\n')
    if len(raw) >= 2:
        words = json.loads(raw[0])
        k = int(raw[1])
        sol = Solution()
        print(json.dumps(sol.topKFrequent(words, k)))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // User logic here
        return {};
    }
};

vector<string> parseStringArray(string input) {
    vector<string> res;
    size_t i = 0;
    while (i < input.length()) {
        if (input[i] == '"') {
            size_t j = i + 1;
            string s = "";
            while (j < input.length() && input[j] != '"') s += input[j++];
            res.push_back(s);
            i = j + 1;
        } else i++;
    }
    return res;
}

int main() {
    string w_str, k_str;
    if (getline(cin, w_str) && getline(cin, k_str)) {
        vector<string> words = parseStringArray(w_str);
        int k = stoi(k_str);
        Solution sol;
        vector<string> ans = sol.topKFrequent(words, k);
        cout << "[";
        for (size_t i = 0; i < ans.size(); i++)
            cout << "\\"" << ans[i] << "\\"" << (i + 1 == ans.size() ? "" : ",");
        cout << "]" << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    static String[] parseStringArray(String raw) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < raw.length()) {
            if (raw.charAt(i) == '"') {
                int j = i + 1;
                StringBuilder sb = new StringBuilder();
                while (j < raw.length() && raw.charAt(j) != '"') sb.append(raw.charAt(j++));
                res.add(sb.toString());
                i = j + 1;
            } else i++;
        }
        return res.toArray(new String[0]);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String w_str = sc.nextLine().trim();
            if (sc.hasNextInt()) {
                int k = sc.nextInt();
                String[] words = parseStringArray(w_str);
                Solution sol = new Solution();
                List<String> ans = sol.topKFrequent(words, k);
                System.out.print("[");
                for (int i = 0; i < ans.size(); i++)
                    System.out.print("\\"" + ans.get(i) + "\\"" + (i + 1 == ans.size() ? "" : ","));
                System.out.println("]");
            }
        }
    }
}""",
        "javascript": """/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\\n');
if (input.length >= 2) {
    const words = JSON.parse(input[0]);
    const k = parseInt(input[1], 10);
    console.log(JSON.stringify(topKFrequent(words, k)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** topKFrequent(char** words, int wordsSize, int k, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    // Simplified; use Python/Java/JS for full parsing
    printf("[]\\n");
    return 0;
}"""
    }

    # Compute expected outputs
    from collections import Counter
    def solve(words, k):
        count = Counter(words)
        return sorted(count, key=lambda w: (-count[w], w))[:k]

    test_cases_data = [
        (["i","love","leetcode","i","love","coding"], 2),
        (["the","day","is","sunny","the","the","the","sunny","is","is"], 4),
        (["a","b","a","b","c"], 1),
        (["a","a","a","a"], 1),
        (["hello","world","hello","python","world","hello"], 2),
        (["z","a","b","z","a","z"], 2),
        (["leetcode"], 1),
        (["apple","banana","apple","cherry","banana","apple"], 2),
        (["a","b","c","a","b","a","c","c","a"], 3),
        (["x","y","x","y","z","z","z","z"], 2)
    ]

    test_cases = []
    for i, (words, k) in enumerate(test_cases_data):
        inp = json.dumps(words) + "\\n" + str(k)
        out = json.dumps(solve(words, k))
        is_sample = i < 2
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
        "topics": ["Hash Table", "String", "Trie", "Sorting", "Heap (Priority Queue)", "Bucket Sort", "Counting"],
        "companyIndex": 0
    }

    output_path = f"601-800/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
